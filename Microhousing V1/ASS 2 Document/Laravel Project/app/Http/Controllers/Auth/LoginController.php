<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use App\Providers\RouteServiceProvider;
use Illuminate\Foundation\Auth\AuthenticatesUsers;
use Illuminate\Support\Facades\Auth;
use Illuminate\Http\Request;

class LoginController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Login Controller
    |--------------------------------------------------------------------------
    |
    | This controller handles authenticating users for the application and
    | redirecting them to your home screen. The controller uses a trait
    | to conveniently provide its functionality to your applications.
    |
    */

    use AuthenticatesUsers;

    /**
     * Where to redirect users after login.
     *
     * @var string
     */
    //protected $redirectTo = RouteServiceProvider::HOME;
    protected function redirectTo()
    {
        if(Auth::user()->usertype=='Housingofficer')
        {
            return 'dashboard';
        }
        else
        {
            return 'dashboard_user';
        }
    }
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('guest')->except('logout');
    }
    public function login(Request $request)
{
    $this->validate($request, [
        'username' => 'required|string', 
        'password' => 'required|string|min:6',
    ]);

    
    $loginType = filter_var($request->username, FILTER_VALIDATE_EMAIL) ? 'email' : 'username';
  

    $login = [
        $loginType => $request->username,
        'password' => $request->password
    ];
  
    
    if (auth()->attempt($login)) {
        if(Auth::user()->usertype=='Housingofficer')
        {
            return redirect()->intended('/dashboard');
        }
        else
        {
            return redirect()->intended('/dashboard_user');
        }

    }
  
    return redirect()->route('login')->with(['error' => 'Email/Password salah!']);
}
}

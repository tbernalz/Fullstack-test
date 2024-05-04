//import Validation from '../../utils/validations/LoginValidation';
//import axios from 'axios';

function LoginForm() {
    return (
        <div className="section text-center">
            <h4 className="mb-4 pb-3">Log In</h4>
            <div className="form-group">
                <input type="email" name="logemail" className="form-style" placeholder="Your Email" id="logemail" autoComplete="off" />
                <i className="input-icon uil uil-at"></i>
            </div>  
            <div className="form-group mt-2">
                <input type="password" name="logpass" className="form-style" placeholder="Your Password" id="logpass" autoComplete="off" />
                <i className="input-icon uil uil-lock-alt"></i>
            </div>
            <a href="#" className="btn mt-4">submit</a>
            <p className="mb-0 mt-4 text-center"><a href="#0" className="link">Forgot your password?</a></p>
        </div>
    );
}
export default LoginForm;
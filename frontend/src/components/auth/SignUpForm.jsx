//import Validation from '../../utils/validations/LoginValidation';
//import axios from 'axios';

function SignUpForm() {
    return (
        <div className="section text-center">
            <h4 className="mb-4 pb-3">Sign Up</h4>
            <div className="form-group">
                <input type="text" name="logname" className="form-style" placeholder="Your Full Name" id="logname" autoComplete="off" />
                <i className="input-icon uil uil-user"></i>
            </div>  
            <div className="form-group mt-2">
                <input type="email" name="logemail" className="form-style" placeholder="Your Company Position" id="logemail" autoComplete="off" />
                <i className="input-icon uil uil-at"></i>
            </div>
            <div className="form-group mt-2">
                <input type="text" name="logecompanyposition" className="form-style" placeholder="Your Email" id="logecompanyposition" autoComplete="off" />
                <i className="input-icon uil-building"></i>
            </div>
            <div className="form-group mt-2">
                <input type="password" name="logpass" className="form-style" placeholder="Your Password" id="logpass" autoComplete="off" />
                <i className="input-icon uil uil-lock-alt"></i>
            </div>
            <a href="#" className="btn mt-4">submit</a>
        </div>
    );
}
export default SignUpForm;
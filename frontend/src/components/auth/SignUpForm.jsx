//import Validation from '../../utils/validations/LoginValidation';
import axios from 'axios';

function SignUpForm() {
    const handleSubmit = async (event) => {
        event.preventDefault();
        const user = {
            name: event.target.logname.value,
            email: event.target.logemail.value,
            company_position: event.target.logecompanyposition.value,
            password: event.target.logpass.value,
        };
        try {
            console.log(user);
            const response = await axios.post('/api/', user);
            console.log(response.data);
        } catch (error) {
            console.error(error.response.data);
        }
    };

    return (
        <div className="section text-center">
            <h4 className="mb-4 pb-3">Sign Up</h4>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <input type="text" name="logname" className="form-style" placeholder="Your Full Name" id="logname" autoComplete="off" />
                    <i className="input-icon uil uil-user"></i>
                </div>  
                <div className="form-group mt-2">
                    <input type="email" name="logemail" className="form-style" placeholder="Your Email" id="logemail" autoComplete="off" />
                    <i className="input-icon uil uil-at"></i>
                </div>
                <div className="form-group mt-2">
                    <input type="text" name="logecompanyposition" className="form-style" placeholder="Your Company Position" id="logecompanyposition" autoComplete="off" />
                    <i className="input-icon uil uil-building"></i>
                </div>
                <div className="form-group mt-2">
                    <input type="password" name="logpass" className="form-style" placeholder="Your Password" id="logpass" autoComplete="off" />
                    <i className="input-icon uil uil-lock-alt"></i>
                </div>
                <button type="submit" className="btn mt-4">Submit</button>
            </form>
        </div>
    );
}
export default SignUpForm;
function Validation(values){
    let error = {}
    const email_pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    const password_pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/

    // email validation
    if(values.email === ""){
        error.email = "Email should not be empty"
    }else if(!email_pattern.test(values.email)){
        error.email = "Invalid email format"
    }

    // password validation
    if(values.password === ""){
        error.password = "Password should not be empty"
    }else if(!password_pattern.test(values.password)){
        error.password = "Password should contain at least one digit, one lowercase letter, one uppercase letter, one special character, and be at least 8 characters long"
    }

    return error;
}

export default Validation;
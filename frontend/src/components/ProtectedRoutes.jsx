import { Navigate } from 'react-router-dom';

const isAuthenticated = () => {
  const token = localStorage.getItem('token');
  return token != null;
};

const ProtectedRoutes = ({ children }) => (
  isAuthenticated() ? children : <Navigate to="/" />
);

export default ProtectedRoutes;
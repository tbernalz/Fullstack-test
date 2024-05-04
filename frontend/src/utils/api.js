import axios from 'axios';

export const getEmployee = (id) => {
  return axios.get(`/api/user/${id}`);
};
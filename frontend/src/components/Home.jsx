import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Chart from 'react-apexcharts';

const Home = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    axios.get('/api/users/0')
      .then(res => {
        const user = res.data;
        setUser(user);
      })
  }, []);

  const chartOptions = {
    chart: {
      id: 'basic-bar'
    },
    xaxis: {
      categories: ['Skill 1', 'Skill 2', 'Skill 3', 'Skill 4', 'Skill 5']
    }
  };

  const series = [{
    name: 'Skills',
    data: [30, 40, 45, 50, 49]
  }];

  return (
    <div>
      {user && (
        <>
          <h1>{user.name}</h1>
          <h2>{user.id}</h2>
          <Chart options={chartOptions} series={series} type="radar" width="500" />
        </>
      )}
    </div>
  );
};

export default Home;
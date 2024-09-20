import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => (
  <div>
     Home
     <Link to='/link-bank-account' role='button'>Connect your bank account</Link>
  </div>
);

export default Home;
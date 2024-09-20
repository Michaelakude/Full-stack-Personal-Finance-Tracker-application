import React from 'react';
import wallet from './wallet.jpg';
import { Link } from 'react-router-dom';

const Home = ({ logout,isAuthenticated }) => (
  
  <div className="flex items-center justify-center min-h-screen bg-gray-100">
    <div className="card bg-base-100 image-full w-96 shadow-xl">
      <figure>
        <img
          src={wallet}
          alt="Wallet" />
      </figure>
      <div className="card-body">
        <h2 className="card-title">Welcome to PennyRaised!</h2>
        <p>The Best Way to manage your money!</p>
        <div className="card-actions justify-end">
          {isAuthenticated && (
            <a href='/login'>
              <button className="btn btn-primary">Login</button>
            </a>
          )}
        </div>
      </div>
    </div>
  </div>
);

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
});

export default Home;

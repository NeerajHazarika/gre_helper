import React, {useState} from "react";
import {useNavigate} from 'react-router-dom';
import axios from 'axios';
import "./Home.css";

const Home = () => {

  const navigate = useNavigate();
  const [testID, setTestID] = useState(0);
  const [attemptID, setAttemptID] = useState(0);

  const StartTest = async () => {
    try {
      const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
  
      // First API request to create a test
      const testResponsePromise = axios.post(`${apiBaseUrl}/api/create_test`);
  
      // Second API request to create an attempt (depends on the testID from the first request)
      const attemptResponsePromise = testResponsePromise.then((testResponse) => {
        const testID = testResponse.data.test_id;
        return axios.post(`${apiBaseUrl}/api/create_attempt/`, { test_id: testID });
      });
  
      // Wait for both API requests to complete
      const [testResponse, attemptResponse] = await Promise.all([
        testResponsePromise,
        attemptResponsePromise,
      ]);
  
      // Update the state with the testID and attemptID
      setTestID(testResponse.data.test_id);
      setAttemptID(attemptResponse.data.attempt_id);
  
      // Redirect to the instruction page with testid and attemptid as query parameters
      navigate(`/instruction/?test_id=${testResponse.data.test_id}&attempt_id=${attemptResponse.data.attempt_id}`);
    } catch (error) {
      console.log(error);
    }
  };
  
  

  return (
    <div className="home-desktop">
      <div className="div">
        <p className="text-wrapper">©GRE Helper 2023. All Rights Reserved.</p>
        <p className="p">
          Our techniques are researched and developed by a team of experts. While we believe in the efficacy of our
          program, the key to success is your dedication and commitment.
        </p>
        <p className="text-wrapper-2">Is it guaranteed to work?</p>
        <div className="text-wrapper-3">It is free</div>
        <p className="text-wrapper-4">How much does it cost?</p>
        <p className="text-wrapper-5">
          It’s time to bid farewell to boring study materials, GRE Helper provides comprehensive and personalized
          approach to your G.R.E exam preparation. With its intelligent assessment, tailored feedback, and valuable
          resources, helps you identify your weaknesses, focus on improving them, and ultimately achieve your best score
          in the exam.
        </p>
        <div className="text-wrapper-6">Why choose GRE Helper?</div>
        <p className="text-wrapper-7">
          GRE Helper is a groundbreaking online platform designed to assess your performance in G.R.E mock tests, gives
          personalized feedback, and offers helpful resources to boost your score and excel in your exam preparation.
        </p>
        <div className="text-wrapper-8">What is GRE Helper?</div>
        <div className="text-wrapper-9">Curious Minds</div>
        <p className="text-wrapper-10">
          Unleash your potential with GRE Helper, your ultimate study buddy. Dive headfirst into our mock tests to ace
          your exam!
        </p>
        <div className="text-wrapper-11">Let’s Go!</div>
        <div className="start-test-button" onClick={StartTest}>
          <div className="overlap-group">
            <div className="text-wrapper-12">Start Test</div>
          </div>
        </div>
        <div className="overlap">
          <div className="text-wrapper-13">HELPER</div>
          <div className="h-1">GRE</div>
          <div className="login-button">
            <div className="div-wrapper">
              <div className="text-wrapper-14">Login / Sign up</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
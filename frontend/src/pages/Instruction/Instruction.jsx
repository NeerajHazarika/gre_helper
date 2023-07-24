import React from "react";
import {useNavigate, useLocation} from "react-router-dom";
import "./Instruction.css";
import checkIcon from "../../assets/icons8-check.svg";
import checkIcon2 from "../../assets/icons8-check(1).svg";

const InstructionPage = () => {
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const testID = queryParams.get("test_id");
  const attemptID = queryParams.get("attempt_id");

  const navigate = useNavigate();

  const redirectToTest = async (test_id, attempt_id) => {
    try {
      const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
  
      // First API request to get question type data
      const questionTypeResponsePromise = fetch(
        `${apiBaseUrl}/api/get_question_type_page/${test_id}/0`
      );
  
      // Second API request to get question image data (depends on the completion of the first request)
      const questionImgResponsePromise = questionTypeResponsePromise.then(() =>
        fetch(`${apiBaseUrl}/api/get_ques_img_src/test/${test_id}/question/0`)
      );
  
      // Wait for both API requests to complete
      const [questionTypeResponse, questionImgResponse] = await Promise.all([
        questionTypeResponsePromise,
        questionImgResponsePromise,
      ]);
  
      // Parse the JSON data from both responses
      const questionTypeData = await questionTypeResponse.json();
      const questionImgData = await questionImgResponse.json();
  
      // Navigate to the test route with the required query parameters
      navigate(
        `/test/${test_id}/attempt/${attempt_id}/question/0?ques_img_src=${questionImgData.ques_img_src}&passage_chart_img_src=${questionImgData.passage_chart_img_src}&question_type_html=${questionTypeData.type_to_templates}`
      );
    } catch (error) {
      console.log("Error occurred during AJAX requests", error);
    }
  };
  

  return (
    <div className="desktop">
      <div className="div">
        <p className="accept-to-continue">
          Accept to continue test. Read Instructions until end and press Accept &amp; Continue:
          <br />
          <br />
          Time Limit: The test has a specified time limit. Make sure to keep track of the time remaining to complete
          each section.
          <br />
          <br />
          Test Sections: The test is divided into multiple sections, including Verbal Reasoning, Quantitative Reasoning,
          and Analytical Writing. Each section assesses different skills and abilities.
          <br />
          <br />
          Navigating Questions: Use the navigation buttons provided to move between questions within a section. You can
          go back and forth to review and revise your answers.
          <br />
          <br />
          Ending the Test: To end the test, click on the &#34;End Test&#34; button. Make sure you have answered all the
          questions before submitting your test.
          <br />
          <br />
          Saving Selected Options: Select your answer choice for each question by clicking on the appropriate option.
          Your selection will be automatically saved as you move to the next question.
          <br />
          <br />
          Cheating Warning: Maintaining the integrity of the test is crucial. Any form of cheating or unauthorized
          assistance during the test is strictly prohibited. Violation of these rules may result in test
          disqualification.
          <br />
          <br />
          Standard Test Rules: Adhere to the standard rules and instructions of the GRE and computer-based testing (CBT)
          format. This includes following the test administrator&#39;s guidelines and adhering to the specified rules of
          conduct.
          <br />
          <br />
          Time Management: Manage your time effectively to ensure you complete all the sections within the given time
          limit. Pace yourself accordingly to allocate sufficient time to each question.
          <br />
          <br />
          Review Your Answers: Before submitting your test, review your answers and make any necessary changes. Ensure
          that you have answered all questions to the best of your ability.
          <br />
          <br />
          Stay Focused: Maintain concentration throughout the test duration. Avoid distractions and create a quiet and
          conducive environment for optimal performance.
        </p>
        <div className="verbal-circle">
          <div className="overlap-4">
            <div className="text-wrapper-11">Verbal</div>
            <div className="overlap-group-3">
              <img className="line-2" alt="Line" src={checkIcon} />
            </div>
          </div>
        </div>
        <div className="math-circle">
          <div className="overlap-4">
            <div className="text-wrapper-11">Math</div>
            <div className="overlap-group-3">
              <img className="line-2" alt="Line" src={checkIcon} />
            </div>
          </div>
        </div>
        <div className="analytical-writing">
          <div className="overlap-4">
            <div className="text-wrapper-10">Analytical Writing</div>
            <div className="overlap-group-3">
              <img className="line-2" alt="Line" src={checkIcon} />
            </div>
          </div>
        </div>
        <div className="stats">
          <div className="text-wrapper-3">questions</div>
          <div className="overlap-3">
            <div className="text-wrapper-4">attempt</div>
            <div className="text-wrapper-5">8</div>
          </div>
          <div className="text-wrapper-6">minutes</div>
          <div className="text-wrapper-7">sections</div>
          <div className="h-1">30 + 20 + 2</div>
          <div className="text-wrapper-8">3</div>
          <div className="text-wrapper-9">90</div>
        </div>
        <div className="accept-continue" onClick={() => redirectToTest(testID, attemptID)}>
          <div className="overlap-2">
            <div className="overlap-group-2">
              <img className="line" alt="Line" src={checkIcon} />
            </div>
            <div className="accept-continue-2">Accept &amp; Continue</div>
          </div>
        </div>
        <div className="go-back-button">
          <div className="overlap">
            <div className="overlap-group">
              <img className="line" alt="Line" src={checkIcon2} />
            </div>
            <div className="text-wrapper-2">Go Back</div>
          </div>
        </div>
        <p className="text-wrapper">© 2023 MasterGRE – All rights reserved</p>
      </div>
    </div>
  );
};

export default InstructionPage;
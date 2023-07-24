import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import "./Test.css";

const TestPage = () => {

  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const ques_img_src = queryParams.get("ques_img_src");

  const [imageSrc, setImageSrc] = useState(null);

  useEffect(() => {
    const fetchImage = async () => {
      try {
        const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
        const response = await fetch(`${apiBaseUrl}/api/filestore/${ques_img_src}`);
        const blob = await response.blob();
        const imageUrl = URL.createObjectURL(blob);
        setImageSrc(imageUrl);
      } catch (error) {
        console.log("Error occurred while fetching the image", error);
      }
    };

    if (ques_img_src) {
      fetchImage();
    }
  }, [ques_img_src]);

  return (
    <div className="instruction-page">
      <div className="div">
        <div className="overlap">
          <div className="question-navigation">
            <div className="element-button">
              <div className="overlap-group">
                <div className="text-wrapper">1</div>
              </div>
            </div>
            <div className="overlap-wrapper">
              <div className="overlap-group">
                <div className="text-wrapper-2">2</div>
              </div>
            </div>
            <div className="overlap-group-wrapper">
              <div className="overlap-group">
                <div className="text-wrapper-3">3</div>
              </div>
            </div>
            <div className="div-wrapper">
              <div className="overlap-group">
                <div className="text-wrapper-4">4</div>
              </div>
            </div>
            <div className="element-button-2">
              <div className="overlap-group">
                <div className="text-wrapper-5">5</div>
              </div>
            </div>
            <div className="element-button-3">
              <div className="overlap-group">
                <div className="text-wrapper-6">6</div>
              </div>
            </div>
            <div className="element-button-4">
              <div className="overlap-group">
                <div className="text-wrapper-5">7</div>
              </div>
            </div>
            <div className="element-button-5">
              <div className="overlap-group">
                <div className="text-wrapper-5">8</div>
              </div>
            </div>
            <div className="element-button-6">
              <div className="overlap-group">
                <div className="text-wrapper-6">9</div>
              </div>
            </div>
            <div className="element-button-7">
              <div className="overlap-group">
                <div className="element-bg" />
                <div className="text-wrapper-7">10</div>
              </div>
            </div>
            <div className="element-button-8">
              <div className="overlap-group">
                <div className="text-wrapper-8">11</div>
              </div>
            </div>
            <div className="element-button-9">
              <div className="overlap-group">
                <div className="text-wrapper-9">12</div>
              </div>
            </div>
            <div className="element-button-10">
              <div className="overlap-group">
                <div className="text-wrapper-10">13</div>
              </div>
            </div>
            <div className="element-button-11">
              <div className="overlap-group">
                <div className="text-wrapper-11">14</div>
              </div>
            </div>
            <div className="element-button-12">
              <div className="overlap-group">
                <div className="text-wrapper-12">15</div>
              </div>
            </div>
            <div className="element-button-13">
              <div className="overlap-group">
                <div className="text-wrapper-13">16</div>
              </div>
            </div>
            <div className="element-button-14">
              <div className="overlap-group">
                <div className="text-wrapper-14">17</div>
              </div>
            </div>
            <div className="element-button-15">
              <div className="overlap-group">
                <div className="text-wrapper-15">18</div>
              </div>
            </div>
            <div className="element-button-16">
              <div className="overlap-group">
                <div className="text-wrapper-16">19</div>
              </div>
            </div>
            <div className="element-button-17">
              <div className="overlap-group">
                <div className="text-wrapper-17">20</div>
              </div>
            </div>
          </div>
        </div>
        <div className="save-next-button">
          <div className="save-next-wrapper">
            <div className="save-next">Save &amp; Next</div>
          </div>
        </div>
        <div className="blank-ii-input">
          <div className="overlap-6">
            <div className="text-wrapper-18">Blank (ii)</div>
          </div>
        </div>
        <div className="blank-i-input">
          <div className="overlap-6">
            <div className="text-wrapper-19">Blank(i)</div>
          </div>
        </div>
        {imageSrc && <img className="screenshot" alt="Screenshot" src={imageSrc} />}
      </div>
    </div>
  );
};

export default TestPage;

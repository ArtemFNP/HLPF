// src/pages/Weather.jsx
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/App.css";
import "../styles/Weather.css";

import rainImage from "../assets/images/rain.png";
import sunImage from "../assets/images/sun.png";
import snowImage from "../assets/images/snow.png";

const Weather = () => {
  const [forecast, setForecast] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  const API_KEY = "7aaaf0be2e3e80bc24cde96ab824dd8d";

  useEffect(() => {
    fetch(
      `https://api.openweathermap.org/data/2.5/forecast?q=Brussels&units=metric&appid=${API_KEY}`
    )
      .then((res) => res.json())
      .then((data) => {
        const filtered = data.list
          .filter((item) => item.dt_txt.includes("12:00:00"))
          .slice(0, 5);
        setForecast(filtered);
        setLoading(false);
      })
      .catch((err) => console.error("Forecast fetch error:", err));
  }, []);

  const getDayInfo = (dateStr) => {
    const date = new Date(dateStr);
    const day = date.toLocaleDateString("en-GB", { weekday: "long" });
    const shortDate = date.toLocaleDateString("en-GB");
    return `${shortDate} ${day}`;
  };

  const getBackground = (desc = "") => {
    const d = desc.toLowerCase();
    if (d.includes("rain")) return rainImage;
    if (d.includes("snow")) return snowImage;
    return sunImage;
  };

  if (loading) return <p>Loading forecast...</p>;

  return (
    <div className="weather-forecast">
      <button onClick={() => navigate("/")} className="weather-back-btn">
        ← Back
      </button>

      <h2 className="forecast-title">5-Day Forecast</h2>

      <div className="forecast-strip">
        {forecast.map((item, index) => {
          const dateInfo = getDayInfo(item.dt_txt);
          const desc = item.weather[0].description;
          const img = getBackground(desc);

          return (
            <div
              key={index}
              className="forecast-day"
              style={{ backgroundImage: `url(${img})` }}
            >
              <h3>{dateInfo}</h3>
              <p>🌡 {item.main.temp.toFixed(1)}°C</p>
              <p>📝 {desc}</p>
              <p>💧 {item.main.humidity}%</p>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Weather;

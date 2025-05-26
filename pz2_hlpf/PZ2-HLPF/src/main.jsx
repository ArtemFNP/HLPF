import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import App from "./App.jsx";
import Weather from "./pages/Weather.jsx";
import JsonFilter from "./pages/JsonFilter.jsx";
import MovieTracker from "./pages/MovieTracker.jsx";
import "./styles/index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
    <Routes>
  <Route path="/" element={<App />} />
  <Route path="/weather" element={<Weather />} />
  <Route path="/filter" element={<JsonFilter />} />
  <Route path="/movies" element={<MovieTracker />} />
</Routes>
    </BrowserRouter>
  </React.StrictMode>
);
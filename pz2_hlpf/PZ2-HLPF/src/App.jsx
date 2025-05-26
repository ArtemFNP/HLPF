import { Link } from "react-router-dom";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./styles/App.css";

const App = () => {
  return (
    <div className="home-container"> 
      <div>
        <a href="https://vitejs.dev" target="_blank" rel="noopener noreferrer">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank" rel="noopener noreferrer">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>

      <h1>Vite + React + SWC</h1>

      <nav style={{ marginBottom: "2rem" }}>
        <Link to="/weather">Forecast</Link> |{" "}
        <Link to="/filter">JSON Filter</Link> |{" "}
        <Link to="/movies">Movie Tracker</Link>
      </nav>

      <div className="card">
        <p>This is the home page. Pick an option above ⬆</p>
      </div>
    </div>
  );
};


export default App;

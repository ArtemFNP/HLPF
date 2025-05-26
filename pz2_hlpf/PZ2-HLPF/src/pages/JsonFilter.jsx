import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/JsonFilter.css";

const JsonFilter = () => {
  const [query, setQuery] = useState("");
  const [people, setPeople] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("/people.json")
      .then((res) => res.json())
      .then((data) => setPeople(data))
      .catch((err) => console.error("Failed to fetch JSON:", err));
  }, []);

  const filteredData = people.filter((item) =>
    item.name.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div className="json-container">
      <button className="json-back-btn" onClick={() => navigate("/")}>
        ← Back
      </button>

      <h2>JSON Filter</h2>
      <input
        type="text"
        placeholder="Insert a name"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <ul>
        {filteredData.map((item) => (
          <li key={item.id}>
            <span className="name">{item.name}</span>
            <span className="dash">—</span>
            <span className="age">{item.age} y.o.</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default JsonFilter;

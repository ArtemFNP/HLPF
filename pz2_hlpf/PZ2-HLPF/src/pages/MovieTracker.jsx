
// src/pages/MovieTracker.jsx
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/MovieTracker.css"; // ✅ Use this for all styles here

const MovieTracker = () => {
  const [movies, setMovies] = useState([]);
  const [newMovie, setNewMovie] = useState("");
  const [selectedMovieId, setSelectedMovieId] = useState(null);
  const [review, setReview] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const storedMovies = JSON.parse(localStorage.getItem("movies"));
    if (storedMovies) setMovies(storedMovies);
  }, []);

  useEffect(() => {
    localStorage.setItem("movies", JSON.stringify(movies));
  }, [movies]);

  const handleAddMovie = () => {
    if (!newMovie.trim()) return;
    const newEntry = {
      id: Date.now(),
      title: newMovie.trim(),
      review: "",
    };
    setMovies([...movies, newEntry]);
    setNewMovie("");
  };

  const handleDelete = (id) => {
    setMovies(movies.filter((m) => m.id !== id));
  };

  const handleReviewSave = (id) => {
    const updated = movies.map((m) =>
      m.id === id ? { ...m, review } : m
    );
    setMovies(updated);
    setSelectedMovieId(null);
    setReview("");
  };

  return (
    <div className="container">
      <h2>🎬 Movie Tracker</h2>

      <button onClick={() => navigate(-1)} style={{ marginBottom: "1rem" }}>
        🔙 Back
      </button>

      <div className="card">
        <input
          type="text"
          placeholder="Movie title"
          value={newMovie}
          onChange={(e) => setNewMovie(e.target.value)}
        />
        <button onClick={handleAddMovie}>Add</button>
      </div>

      <ul style={{ listStyle: "none", padding: 0 }}>
        {movies.map((movie) => (
          <li key={movie.id} className="card" style={{ margin: "1rem auto", maxWidth: "600px", textAlign: "left" }}>
            <strong onClick={() => {
              setSelectedMovieId(movie.id);
              setReview(movie.review || "");
            }}
              style={{ cursor: "pointer", display: "block", marginBottom: "0.5rem" }}>
              🎞 {movie.title}
            </strong>

            {selectedMovieId === movie.id && (
              <div className="review-section" style={{ marginTop: "1rem" }}>
                <textarea
                  placeholder="Write a review..."
                  value={review}
                  onChange={(e) => setReview(e.target.value)}
                  rows={3}
                  style={{ width: "100%", padding: "0.5rem" }}
                ></textarea>
                <button onClick={() => handleReviewSave(movie.id)} style={{ marginTop: "0.5rem" }}>
                  Save Review
                </button>
              </div>
            )}

            {movie.review && selectedMovieId !== movie.id && (
              <p style={{ fontStyle: "italic", color: "#555" }}>
                📌 Review: {movie.review}
              </p>
            )}

            <button onClick={() => handleDelete(movie.id)} style={{ marginTop: "0.5rem", backgroundColor: "#ffdddd" }}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MovieTracker;
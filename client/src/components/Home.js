import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Home() {
  const [restaurants, setRestaurants] = useState([]);

  // Use the useEffect hook to fetch data when the component mounts
  useEffect(() => {
    fetch("/restaurants") // Make a GET request to your Flask endpoint
      .then((response) => response.json())
      .then((data) => setRestaurants(data)); // Update the state with the fetched data
  }, []);

  return (
    <section className="container">
      {restaurants.map((restaurant) => (
        <div key={restaurant.id} className="card">
          <h2>
            <Link to={`/restaurants/${restaurant.id}`}>{restaurant.name}</Link>
          </h2>
          <p>Address: {restaurant.address}</p>
        </div>
      ))}
    </section>
  );
}

export default Home;

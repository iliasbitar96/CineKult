import axios from 'axios';
import '../styles/HomePage.css'
import '../styles/Theme.css'
import { useState, useEffect } from 'react';
import Searchbar from '../components/Searchbar';
import DropDown from '../components/DropDown';
import MovieCard from '../components/MovieCard';
import ButtonTheme from '../components/ButtonTheme';

function HomePage() {
  const [movie, setMovie] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8069/cm_cast/search_movies/');
        setMovie(response.data);
        console.log(response.data)
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className='homePage'>
      <h1 className='title'>La liste </h1>
      <div className="intro">
        Voilà la fameuse liste, vous pouvez scroll jusqu’à trouver la 
        perle rare ou vous pouvez chercher directement un film en tapant 
        des mots clés ou chercher en fonction des catégories. 
        <br/> 
        <br/> 
        Bonne recherche !
      </div>
      <Searchbar 
        placeholder='Recherche par mots clés'
      />
      <div className="search-by">
        <p>Rechercher par</p>
        <DropDown />
        <Searchbar placeholder="Ecrivez le nom d'un acteur" /> 
      </div>
      <ButtonTheme 
        name='Test'
        state='secondary'
      />
      <div className="movie-list">
        <ul>
          <li>{movie.map(m => (
            <MovieCard 
              key={m.id} 
              title={m.name} 
              voteCount={m.votes}
              date={m.year}
              director={m.director}
              actors={m.actors}
              />
          ))}</li>
        </ul>
      </div>
      <br />
      <br />
      <br />
    </div>
  );
}

export default HomePage;

import React, { useEffect } from 'react'
import axios from 'axios';
import '../styles/SearchBar.css'
import Searchicon from '../static/img/search-normal.svg'

const Searchbar = props => {
  let keyword = props.keyword

  const filter_movies = async () => {
    if (keyword){
      console.log('search by keyword')
      const params = new URLSearchParams();
      params.append('param1', 'test');
      axios({ 
        method: 'post',
        url: 'http://127.0.0.1:8069/cm_cast/filter_movies',
        data: keyword
      }).then(function (response) {
        console.log('IDDD', props);
      }, [props]);
    }
  }

  return (
    <div className='searchBar'>
        <input type="text" name="movie" onSubmit={filter_movies}
        placeholder={props.placeholder}/>
        <div className="search-img" onClick={filter_movies}>
            <img src={Searchicon}/>
        </div>
    </div>
  )
}

export default Searchbar
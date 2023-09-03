import React from 'react'
import '../styles/SearchBar.css'
import Searchicon from '../static/img/search-normal.svg'

const Searchbar = props => {
  return (
    <div className='searchBar'>
        <input type="text" name="movie" 
        placeholder={props.placeholder}/>
        <div className="search-img">
            <img src={Searchicon} />
        </div>
    </div>
  )
}

export default Searchbar
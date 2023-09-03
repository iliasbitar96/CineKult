import React from 'react'
import '../styles/MovieCard.css'
import Incr from '../static/img/add-circle.svg'
import Decr from '../static/img/minus-cirlce.svg'

const MovieCard = props => {
  return (
    <div className='movieCard'>
        <div className="top-card">
            <div className="cardCreator">
                <p>Ajouté par</p>
                <p><b>@Eleonor Guetatra{props.creator}</b></p>
            </div>
            <div className="vote-counter">
                <img src={Incr} />
                <span className='vote-count-number'>{props.voteCount}</span>
                <img src={Decr} />
            </div>
        </div>
        <div className="card-body">
            <div className="card-title">
                {props.title}
            </div>
            <div className="card-info">
                <p><span className='info-title'>Sorti en </span><span className='info'>{props.date}</span></p>
                <p><span className='info-title'>De </span><span className='info'>{props.director}</span></p>
                <p><span className='info-title'>Par </span><span className='info'>A24{props.production}</span></p>
                <p><span className='info-title'>Avec </span><span className='info'>{props.actors}</span></p>
            </div>
        </div>
        <div className="card-bottom">
        </div>
    </div>
  )
}

export default MovieCard
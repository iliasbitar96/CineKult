import React, { useEffect, useState } from 'react'
import axios from 'axios';
import '../styles/MovieCard.css'
import Incr from '../static/img/add-circle.svg'
import Decr from '../static/img/minus-cirlce.svg'

const MovieCard = props => {
    const [count, setCount] = useState()
    const set_votes = (e) => {
        const params = new URLSearchParams();
        console.log('ID', props.id)
        params.append('id', props.id);
        params.append('up_vote', 1);
        axios({ 
            method: 'post',
            url: 'http://127.0.0.1:8069/cm_cast/set_vote',
            data: params
          }).then(function (response) {
            setCount(response.data['vote']);
            console.log('IDDD', props.id);
          }, [props.id]);
    }
    const remove_votes = (e) => {
        const params = new URLSearchParams();
        params.append('id', 4);
        params.append('down_vote', -1);
        axios({ 
            method: 'post',
            url: 'http://127.0.0.1:8069/cm_cast/set_vote',
            data: params
          }).then(function (response) {
            setCount(response.data['vote']);
            console.log(props.id);
          }, [props.id]);
    }
    

  return (
    <div className='movieCard'>
        <div className="top-card">
            <div className="cardCreator">
                <p>Ajouté par</p>
                <p><b>@Eleonor Guetatra{props.creator}</b></p>
            </div>
            <div className="vote-counter">
                <img src={Incr} onClick={set_votes}/>
                <span className='vote-count-number'>{count}</span>
                <img src={Decr} onClick={remove_votes}/>
            </div>
        </div>
        <div className="card-body">
            <div className="card-title">
                {props.title}
            </div>
            <div className="card-info">
                <p><span className='info-title'>Sorti en </span><span className='info'>{props.date}</span></p>
                <p><span className='info-title'>De </span><span className='info'>{props.director}</span></p>
                <p><span className='info-title'>Par </span><span className='info'>{props.production}</span></p>
                <p><span className='info-title'>Avec </span><span className='info'>{props.actors}</span></p>
            </div>
        </div>
        <div className="card-bottom">
        </div>
    </div>
  )
}

export default MovieCard
import React from 'react'
import '../styles/ButtonTheme.css'

const ButtonTheme = props => {
  return (
    <button className={`btn-mv ${props.state}`}>
      {props.name}
    </button>
  )
}

export default ButtonTheme
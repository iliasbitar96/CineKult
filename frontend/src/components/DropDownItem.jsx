import React from 'react'
import '../styles/DropDown.css'

const DropDownItem = props => {
  return (
    <li key={props.id} className='dropDownItem'>
        {props.item}
    </li>
  )
}

export default DropDownItem
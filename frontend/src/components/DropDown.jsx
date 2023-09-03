import {React, useState} from 'react'
import '../styles/DropDown.css'
import ArrowDown from '../static/img/arrow-down.svg'
import DropDownItem from './DropDownItem'

const Searchbar = props => {

  const [open, setOpen] = useState(false);
  const [selectedWord, setSelectedWord] = useState([])

  const setChoice = e => {
    console.log(e.item)
  }

  return (
    <div className='dropDown'>
      <div className="dropTop">
          <span>Genre</span>
          <img className={`drop-img ${open? 'active' : 'inactive'}`} src={ArrowDown} onClick={() => {setOpen(!open)}}/>
      </div>
      <div className={`dropBottom ${open? 'active' : 'inactive'}`}>
        <ul>
          <DropDownItem item="Action" onClick={setChoice}/>
          <DropDownItem item="Comedie"/>
          <DropDownItem item="Thriller"/>
        </ul>
      </div>
    </div>
  )
}

export default Searchbar
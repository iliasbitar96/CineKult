import {React, useState, useEffect} from 'react'
import '../styles/DropDown.css'
import ArrowDown from '../static/img/arrow-down.svg'
import DropDownItem from './DropDownItem'

const DropDown = props => {

  const [open, setOpen] = useState(false);
  const [selectedWord, setSelectedWord] = useState()
  const items = props.items 

  const setChoice = word => {
    console.log(word)
    setOpen(!open)
    setSelectedWord(word)
  }

  useEffect(() => {
    const set_first_item = async () => {
      setChoice(items[0])
      setOpen(false)
    };

    set_first_item();
  }, []);

  return (
    <div className='dropDown'>
      <div className="dropTop">
          <DropDownItem item={selectedWord} onClick={setChoice}/>
          <img className={`drop-img ${open? 'active' : 'inactive'}`} src={ArrowDown} onClick={() => {setOpen(!open)}}/>
      </div>
      <div className={`dropBottom ${open? 'active' : 'inactive'}`}>
        <ul>
          {items.map((item, index) => (
            <div onClick={() => {setChoice(item)}}>
              <DropDownItem id={index} item={item} />
            </div>
          ))}
        </ul>
      </div>
    </div>
  )
}

export default DropDown
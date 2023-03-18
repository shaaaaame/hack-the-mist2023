import React from 'react'
import { Link } from 'react-router-dom'
import './Hero.css'

import heart from '../../images/heart.png';
import beat from '../../images/beat.png';
import des from '../../images/des.png';

function Hero() {
  

  return (
    <div className='hero'>
      <img className='hero-heart' src={heart} alt='heart'/>
      <div className='hero-container'>
        <div className='hero-title-container'>
          <div>
            <h1 className='hero-title'>diagnos</h1>
            <h3 className='hero-description'>your healthcare diagnosis app.</h3>
          </div>
          <img className='hero-beat' src={beat} alt='beat'/>
        </div>
        <Link className='hero-link' to='/input'>
          <div className='hero-start'>
            <h3 className='hero-start-text'>get started.</h3>
          </div>
        </Link>
      </div>
      <img className='hero-des' src={des} alt='des'/>
    </div>
  )
}

export default Hero
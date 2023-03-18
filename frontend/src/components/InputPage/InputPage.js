import React, { useState, useEffect } from 'react'

import beat from '../../images/beat.png';
import './InputPage.css'

function InputPage() {
    const [image, setImage] = useState();    
    function onImageChange(e){
        setImage(URL.createObjectURL(e.target.files[0]));
    }

    return (
        <div className='i'>
            <div className='hero-container'>
                <div className='hero-title-container'>
                    <div>
                        <h1 className='hero-title'>diagnos</h1>
                        <h3 className='hero-description'>your healthcare diagnosis app.</h3>
                    </div>
                    <img className='hero-beat' src={beat} alt='beat'/>
                </div>
            </div>
            <div className='i-container'> 
                <div className='i-form-container'>
                    <h3 className='i-form-title'>upload image</h3>
                    <input className='i-form-input' type='file' accept="image/*" onChange={onImageChange} />
                    <div className='i-form-image'><img src={image} alt='input'/></div>
                </div>
                <div className='i-predicted'>
                    <div>
                        <h3>predicted: </h3>
                        <div className='i-predicted-values'>
                            <ul>
                                <li className='i-value'>one</li>
                                <li className='i-value'>two</li>
                                <li className='i-value'>three</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default InputPage
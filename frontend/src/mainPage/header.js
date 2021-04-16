import React from 'react'

/*  Local Components */
import Navbar from './navbar'
import UserPresentation from './userPresentation'


const Header = ({ name }) => (
    <React.Fragment>
        <Navbar />
        <UserPresentation 
            name={name}
        />
    </React.Fragment>
)


export default Header
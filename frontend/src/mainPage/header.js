import React from 'react'

/*  Local Components */
import Navbar from './navbar'
import UserPresentation from './userPresentation'


const Header = ({ user }) => (
    <React.Fragment>
        <Navbar />
        <UserPresentation user={ user } />
    </React.Fragment>
)


export default Header
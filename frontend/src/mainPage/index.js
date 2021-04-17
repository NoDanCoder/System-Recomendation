import React from 'react'
import { useParams } from 'react-router-dom'

/* Local Components */
import Header from './header'
import BodyLists from './bodyLists'


const IndexUser = () => {

    const { id } = useParams()
    return (
        <React.Fragment>
            <Header user={ id } />
            <BodyLists user={ id } />
        </React.Fragment>
    )
}

export default IndexUser
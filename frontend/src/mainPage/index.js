import React from 'react'
import { useParams } from 'react-router-dom'

/* Local Components */
import Header from './header'
import BodyLists from './bodyLists'
import Footer from './footer'
import Loading from '../loading/index'
import Error500 from '../500ServerError/index'
import Error404 from '../404NotFound/index'
import useFetch from '../hooks/useFetch'

/* Settings */
import API_HOST from '../settings'

/* CSS */
import './index.css'


const IndexUser = () => {

    const { id } = useParams()
    const { data, loading, error } = useFetch(`${API_HOST}/user/${id}?prop=name`)

    if (loading)
        return <div className="loading-state"><Loading /></div>
    if (error)
        return <Error500 />
    if ('error' in data)
        return <Error404 />
    
    return (
        <React.Fragment>
            <Header name={ data[0].name } />
            <div className="pb-5 mx-3">
                <BodyLists user={ id } />
            </div>
            <Footer />
        </React.Fragment>
    )
}

export default IndexUser
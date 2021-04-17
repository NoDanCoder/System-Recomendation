/* Local Components */
import Loading from '../loading/index'
import Error500 from '../500ServerError/index'
import useFetch from '../hooks/useFetch'

/* Settings */
import API_HOST from '../settings'

/* CSS */
import './userPresentation.css'


const UserPresentation = ({ user }) => {

    const { data, loading, error } = useFetch(`${API_HOST}/user/${user}?prop=name`)
    const { name } = (data?.length) ? data[0] : "NN"

    if (loading)
        return <Loading />
    if (error)
        return <Error500 />

    return (
        <div className="jumbotron bg-dark">
            <div className="header__main">
                <div className="header__main-img">
                    <img src="https://cdn.shopify.com/s/files/1/0167/4484/files/review-sam_300x300_crop_center.png?v=1605305573" alt="avatar user icon" className="user-icon" />
                </div>
                <div class="header__main-text">
                    <h1 className="display-3 text-light">Welcome, { name }!</h1>
                    <p className="lead text-light"> We have been working too hard to make a bit easier your local business every day.</p>
                    <hr className="my-4 border-light" />
                    <p className="text-light">Check our recomendations for you among a great variety of high quality products.</p>
                </div>
            </div>
        </div>
    )
}


export default UserPresentation
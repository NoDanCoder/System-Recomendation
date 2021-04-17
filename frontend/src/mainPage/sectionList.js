/* Local Components */
import useFetch from '../hooks/useFetch'
import ProductCard from './productCard'
import Loading from '../loading/index'
import Error500 from '../500ServerError/index'

/* CSS */
import './sectionList.css'


const SectionListRender = ( title, products ) => {

    if (!products?.length)
        return ""
    return (
        <div className="body__main">
            <h2 className="body__main-title">{ title }</h2>
            <div className="body__main-list">
                {products.map( elem => {
                    if ("product" in elem)
                        return <ProductCard {...elem.product} />
                    return<ProductCard {...elem.category.product} />
                })}
            </div>
        </div>
    )
}


const SectionList = ({ api, title }) => {

    const { data, loading, error } = useFetch(api)

    if (loading)
        return <Loading />
    if (error)
        return <Error500 />
    
    return SectionListRender(title, data)
}


export default SectionList
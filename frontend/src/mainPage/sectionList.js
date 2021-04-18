/* Local Components */
import useFetch from '../hooks/useFetch'
import ProductCard from './productCard'
import Loading from '../loading/index'
import Error500 from '../500ServerError/index'

/* CSS */
import './sectionList.css'


const SectionListRender = ( title, products ) => {

    return (
        <div className="body__main">
            <h2 className="body__main-title pl-3">{ title }</h2>
            <div className="body__main-list">
                {
                    products?.length ? (
                        products.map( elem => {
                            if ("product" in elem)
                                return <ProductCard key={elem.product.uuid} {...elem.product} />
                            return<ProductCard key={elem.category.product.uuid} {...elem.category.product} />
                        })
                    ) : (
                        <div className="empty-box px-5">
                            <p>Nothing here :(, check our recomendtion categories section :D</p>
                        </div>
                    )
                }
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
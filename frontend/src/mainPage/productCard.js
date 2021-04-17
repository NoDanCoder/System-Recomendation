import React from 'react'
import './productCard.css'


const ProductCard = ({ name, description, image }) => (
    <React.Fragment>
        <div className="container product-card">
            <div className="card mb-3">
                <h3 className="card-header">{ name }</h3>
                        
                <div width="100%" height={200}>
                    <img className="card-image" src={`https://picsum.photos/id/${ image }/500`} alt={`${ name }`} />
                </div>
                
                <div className="card-body">
                    <p className="card-text">{ description }</p>
                </div>
            </div>
        </div>
    </React.Fragment>
)

export default ProductCard
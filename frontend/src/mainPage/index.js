import React from 'react'

/* Local Components */
import ProductCard from './productCard'
import Header from './header'


const IndexUser = () => (
    <React.Fragment>
        <Header 
            name="Daniel"
        />
        <ProductCard 
            key="13"
            name="Product 1"
            description="Description product 1"
            image="1072"
        />
    </React.Fragment>
)

export default IndexUser
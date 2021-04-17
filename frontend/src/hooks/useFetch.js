import { useState, useEffect } from 'react'


async function fetchData(url, setData, setLoading, setError)
{
    try {
        const response = await fetch(url)
        const data = await response.json()
    
        setData(data)
        setLoading(false)
    } catch (error) {
        setError(error)
        setLoading(false)
    }
}

function useFetch(url)
{
    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => 
        fetchData(url, setData, setLoading, setError)
    , [url])

    return { data, loading, error }
}

export default useFetch
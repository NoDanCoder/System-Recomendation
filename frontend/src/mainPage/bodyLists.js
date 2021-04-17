/* Local Components */
import SectionList from './sectionList'

/* Settings */
import API_HOST from '../settings'


const BodyLists = ({ user }) => {

    let infoToFetch = [
        {
            api: 'user',
            title: 'Your most bought products:'
        },{
            api: 'user/reco-category',
            title: 'Popular in your market:'
        },{
            api: 'user/reco-users',
            title: 'Why dont give a try?...'
        }
    ]

    infoToFetch = infoToFetch.map( obj => ({
        api: `${API_HOST}/${obj.api}/${user}`,
        title: obj.title
    }))

    return (
        infoToFetch.map( infoToFetch =>
            <SectionList 
                {...infoToFetch}
            />
        )
    )
}


export default BodyLists
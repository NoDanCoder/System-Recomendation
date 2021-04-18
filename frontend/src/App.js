import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import IndexUser from './mainPage/index'
import Index404 from './404NotFound/index'

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/user/:id" component={IndexUser} />
        <Route component={Index404} />
      </Switch>
    </Router>
  )
}

export default App

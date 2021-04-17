import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import IndexUser from './mainPage/index'

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/user/:id" component={IndexUser} />
      </Switch>
    </Router>
  )
}

export default App

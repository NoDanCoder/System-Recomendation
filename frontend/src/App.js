import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import IndexUser from './mainPage/index'

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" component={IndexUser} />
      </Switch>
    </Router>
  )
}

export default App;

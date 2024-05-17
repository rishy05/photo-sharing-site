import UserUp from "./User";
import PhotoUp from "./Photo";
import { BrowserRouter, Routes, Route, useNavigate} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      
      <Routes>

      {/* <Route path ='user' element={<UserUp/>}/> */}
      <Route path ='photographer' element={<PhotoUp/>}/>
      <Route path = '/' element = {<UserUp/>}/>



      </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;

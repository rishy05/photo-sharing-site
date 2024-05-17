import { useState } from "react";
import axios from "axios";


const FileUpload = () => {

    const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFile = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post('http://localhost:8080/upload', formData, {
        headers: {

          'Content-Type': 'multipart/form-data',
        },
      });
      let dataa = (response.data)
      
      console.log(dataa)
      setMessage(response.data.message);
    } catch (error) {
      console.error('Error uploading file:', error);
      setMessage('Error uploading file');
    }}

    return ( 
        <div>FileUpload
            <form onSubmit={handleUpload}>
                <input type="file" name = 'file' onChange={handleFile}/>
                <button type="submit">Upload</button>
            </form>
        </div>
     );
}
 
export default FileUpload;
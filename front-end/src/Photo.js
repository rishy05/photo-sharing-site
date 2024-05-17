import { useState } from "react";
import axios from "axios";
import './Photo.css'; // Import your CSS file for styling

const PhotoUp = () => {
  const [files, setFiles] = useState([]);
  const [message, setMessage] = useState('');

  const handleFileChange = (event) => {
    setFiles(event.target.files);
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append('file', files[i]);
    }

    try {
      const response = await axios.post('http://127.0.0.1:8080/photographer', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setMessage('Files uploaded successfully!');
    } catch (error) {
      console.error(error);
      setMessage('Error uploading files!');
    }
  };

  const handlePurge = async (e) => {
    try {
      const response = await axios.get('http://127.0.0.1:8080/purge')
    } catch(error){
      console.error(error)
    }
  };

  const handleSub = async (e) => {
    try {
      const response = await axios.get('http://127.0.0.1:8080/submit')
    } catch(error){
      console.error(error)
    }
  };
  return (
    <div className="dark-theme"> {/* Apply dark theme class */}
      <h1>File Upload</h1>
      <form onSubmit={handleUpload}>
        <input type="file" multiple onChange={handleFileChange} />
        <button type="submit">Upload</button>
        <label>{message}</label>
      </form>
      <div>
      
      <button onClick={handlePurge}>Purge</button>
      </div>
      <div>
      <button onClick={handleSub}>Submit</button>
      </div>
    </div>
  );
}

export default PhotoUp;

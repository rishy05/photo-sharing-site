import { useState } from "react";
import axios from "axios";

const UserUp = () => {
  const [file, setFile] = useState(null);
  const [email, setEmail] = useState("");
  const [namee, setName] = useState("")
  const [message, setMessage] = useState("");

  const handleFile = (event) => {
    setFile(event.target.files[0]);
    //file = event.target.files[0]
    console.log(event.target.files[0]);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage("Please select a file to upload.");
      return;
    }

    try {
      const formData = new FormData();
      console.log(file)
      formData.append("file", file);
      formData.append("email", email);
      formData.append("name", namee);
      const response = await axios.post("http://127.0.0.1:8080/user", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setMessage("Files and email uploaded successfully!");
    } catch (error) {
      console.error(error);
      setMessage("Error uploading files and email. Please try again.");
    } finally {
      console.log(email, namee);
      setFile(null);
      setEmail(""); // Clear email field after upload
      setName("");
    }
  };

  return (
    <div>
      <h2>File Upload</h2>
      <form onSubmit={handleUpload}>
        <input type="file" name="file" onChange={handleFile} />
        <br />
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={email}
          onChange={handleEmailChange}
        />
        <br />
        <label htmlFor="name">Name:</label>
        <input
          type="name"
          id="name"
          name="name"
          value={namee}
          onChange={handleNameChange}
        />
        <br/>
        <button type="submit">Upload</button>
        <br />
        <label>{message}</label>
      </form>
    </div>
  );
};

export default UserUp;

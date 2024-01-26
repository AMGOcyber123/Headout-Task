# Getting Started

1. Clone this repository to your local machine:

   ```
   git clone <repository-url>
   cd <repository-name>
## Build the Docker image. Run the following command from the project root directory:
  ```
  docker build -t http-server-app .
  ```


## Run the Docker container:
  ```
  docker run -d -p 8080:8080 --memory=1500m --cpus=2 http-server-app
  ```

#### Your Flask application will now be running inside a Docker container. 
## Container Details:
- **Container ID:** 58e0e5fca9f0
- **Image:** http-server-app
- **Command:** python app.py
- **Created:** 7 minutes ago
- **Status:** Up 7 minutes
- **Ports:** 0.0.0.0:8080->8080/tcp
- **Container Name:** stoic_mayer
 

## Usage
You can access the HTTP server at http://localhost:8080.

### Retrieving Content from a Text File

#### Retrieve Entire Content
- Endpoint: `/data?n=<file_name>`
- Description: Retrieves the entire content of the specified text file.

#### Retrieve Specific Line
- Endpoint: `/data?n=<file_name>&m=<line_number>`
- Description: Retrieves a specific line from the text file.
- Parameters:
  - Replace `<file_name>` with the name of the file you want to access.
  - Replace `<line_number>` with the line number you want to retrieve (optional).


## Optimizations

The Flask application is optimized to efficiently serve large text files:

- It streams file content in chunks to minimize memory usage.
- It can serve text files of approximately 100MB each without loading the entire file into memory.

### Challenges Faced and Optimization Attempts

While working on optimizing this project, I encountered several challenges due to the large file sizes (approximately 100MB each). Although I may not have achieved a perfect solution, I made efforts to address these challenges:

**1. Memory Usage:** Serving such large files efficiently without consuming excessive memory was a significant challenge. Loading an entire 100MB file into memory could strain the system resources.

**2. Line-Based Retrieval:** Retrieving a specific line from a large text file efficiently required careful handling. Reading line by line could be slow for very large files.

**3. Large Number of Files:** Handling more than 30 different 100MB files added complexity to the project. Ensuring that each file could be accessed and retrieved efficiently posed a challenge.

In summary, optimizing this project for serving large files was a challenging task. While the optimizations attempted may not be perfect, they represent efforts to strike a balance between efficiency and resource usage. Further refinements and improvements can always make the project even more robust.

Project Overview
This project is a Flask web application that allows users to convert currencies. It provides a simple user interface where users can enter an amount, select the source currency, and select the target currency. The application then uses the convert function from the conv module to perform the currency conversion and displays the result on the results page.

Technologies Used
Flask: A web framework for Python that allows us to build web applications.
HTML: Used for creating the structure and content of the web pages.
CSS: Used for styling the web pages.
Jinja2: A templating engine used in Flask to dynamically generate HTML pages.
Code Explanation
The Flask application is created and an instance of the Flask class is created with the name app.
The / route is defined using the @app.route decorator. It simply renders the index.html template, which serves as the homepage of the application.
The /results route is defined with the methods=['GET', 'POST'] parameter, indicating that it can handle both GET and POST requests. This route is responsible for processing the currency conversion form.
Inside the /results route, we first check if the request method is POST.
If the method is POST, we retrieve the amount, source currency, and target currency from the form submitted by the user.
The convert function is called from the conv module, passing in the amount, source currency (converted to lowercase), and target currency.
The result, along with other relevant information, is stored in the info list.
The info list is passed to the result.html template, where the result and other information are displayed.
If the method is not POST (i.e., a GET request), the function simply renders the result.html template without any information.
The if __name__ == '__main__': block ensures that the Flask application is only run if the script is executed directly and not imported as a module.
Instructions to Run and Test the Website
To run and test the website, follow these steps:

Install Flask if you haven't already. You can install it by running the command pip install flask in your command prompt or terminal.
Save the provided code into a Python file, for example, currency_converter.py.
Create a new Python file named conv.py and implement the convert function that performs the currency conversion. Make sure to import any necessary libraries or APIs for currency conversion.
Create an index.html file that serves as the homepage and a result.html file to display the conversion results. Customize these files as per your requirements, including form elements, styling, and result display.
In the same directory where you saved the Python files and HTML templates, open a command prompt or terminal.
Run the Flask application by executing the command python currency_converter.py.
You will see some output indicating that the Flask application is running.
Open a web browser and enter the URL http://localhost:5000 to access the homepage of the currency converter application.
Enter the required details in the form, submit it, and verify that the conversion result is displayed correctly on the results page.
Test the application with different inputs to ensure its accuracy and functionality.

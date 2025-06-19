# ClearRoute-x-Le-Mans-24h-Hackathon-2025

*My primary contributions involved implementing the artificial intelligence (AI) components, particularly the anomaly 
detection algorithm, and developing the backend infrastructure to support data processing and API interactions.*

*The project utilizes synthetic data to simulate real-time monitoring of various data during racing scenarios, as actual
data was not available. The system is designed to detect anomalies that could indicate potential issues, thereby enhancing safety and performance in high-stakes environments. Overall, my role in this project was pivotal in establishing the AI-driven backend that powers the anomaly detection 
capabilities, contributing to a robust solution for monitoring coolant temperature data effectively.*

## Getting started

### Running locally

1. Clone the **ClearRoute-x-Le-Mans-24h-Hackathon-2025** repository in your desired directory:
    ```bash
   $> git clone https://github.com/iccaka/ClearRoute-x-Le-Mans-24h-Hackathon-2025.git
   ```
2. Run these commands in order:
    ```bash
   # create a new virtual environment
   $> python3 -m venv venv

   # start the virtual environment
   $> source /venv/bin/activate
   
   # install project dependencies
   $> pip3 install -r requirements.txt
    ```
3. Before starting the project, fastapi needs to be running:
   ```bash
   # start the fastapi entrypoint
   $> fastapi dev app.py
   
   # finally run main.py
   $> python3 main.py
    ```

## Dependencies

Please refer to [requirements.txt](requirements.txt) for a list of the python module dependencies.

## Authors

* **Hristo Mitsev** - *AI and backend work* - [iccaka](https://github.com/iccaka)

See also the list of [contributors]() who participated in this project.

## Built Wit

* [PyCharm](https://www.jetbrains.com/pycharm/) - *The IDE used*

## License

This project is licensed under the MIT License - *see the* 
[LICENSE](https://github.com/iccaka/Metasim-task/blob/master/LICENSE.md) *file for details.*


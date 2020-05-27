# Ambient Weather Monitor

A simple ambient indoor weather statistics measuring and logging system written completely in python consisting of a InfluxDB integeration, a HTTP server, and an MQTT client. Designed to work on raspberry pi's with a senseHAT(Feature to allow using any kind of sensor may arrive in future).

Most settings can be customized using the config.props file.

The InfluxDG/HTTP/MQTT bindings can be further used to integrate the project into further projects.

##### Examples: 

- Using InfluxDB and Grafana to build a dashboard.
![](https://i.imgur.com/CtzEbXf.png)

- Using the HTTP server and iOS shortcuts to build an on-demand notification system.
![](https://i.imgur.com/b6Ru3ci.png)

- Using MQTT on node-red to build a dashboard.
![](https://i.imgur.com/vmE74Pm.png)



[Link to the iOS Shortcut](https://www.icloud.com/shortcuts/a520a8f9ea1e4cdba8ed9ebe7df9d44c)
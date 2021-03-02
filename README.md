

-   **Office Teams Relay - EASY: via Azure Relay**

    -   [OfficeDev/microsoft-teams-tunnelrelay: Tunnel relay allows you to expose local services to the outside world over HTTPS (github.com)](https://github.com/OfficeDev/microsoft-teams-tunnelrelay)

    -   ngrok - [Azure Functions Event Grid local debugging \| Microsoft Docs](https://docs.microsoft.com/en-us/azure/azure-functions/functions-debug-event-grid-trigger-local#allow-azure-to-call-your-local-function)

    -   Azure Relay from scratch

        -   [Azure-Samples/event-grid-relay-listener: Use Service Bus Relay to receive events from Event Grid and print them directly to the console (github.com)](https://github.com/Azure-Samples/event-grid-relay-listener/)

        -   [sfeldman.NET - Azure EventGrid testing with Azure Relay (asp.net)](https://weblogs.asp.net/sfeldman/azure-eventgrid-testing-with-azure-relay)

        -   [Writing tests for Azure Event Grid \| Codit](https://www.codit.eu/blog/writing-tests-for-azure-event-grid/?country_sel=be)

        -   [Locally Debugging an Event Grid Triggered Azure Function with Postman \| Blogilreavy (mcilreavy.com)](https://blog.mcilreavy.com/articles/2018-12/debug-eventgrid-triggered-azure-function)

Creating and Event Grid Viewer: 

[Azure Event Grid trigger for Azure Functions \| Microsoft Docs](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-trigger?tabs=csharp%2cbash#create-a-viewer-web-app)

General Local experience

[Azure Functions Event Grid local debugging \| Microsoft Docs](https://docs.microsoft.com/en-us/azure/azure-functions/functions-debug-event-grid-trigger-local)


# Runing Azurite Storage Emulator

From the `./projects/event_routing/src` folder - as this 
```bash
#!/usr/bin/env bash
# Note replaced by task.json task.
mkdir -p ./.azurite/data

docker run -it --rm -p 10000:10000 -v $(pwd)/.azurite/data:/data \
    mcr.microsoft.com/azure-storage/azurite

```


# Deploying a function pack 

```
az functionapp deployment source config-zip -g scicoriafunctest -n scicoriafunctest --src az-functions-py-play.zip
```
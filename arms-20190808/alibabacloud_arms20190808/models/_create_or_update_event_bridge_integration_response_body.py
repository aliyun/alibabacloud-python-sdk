# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateEventBridgeIntegrationResponseBody(DaraModel):
    def __init__(
        self,
        event_bridge_integration: main_models.CreateOrUpdateEventBridgeIntegrationResponseBodyEventBridgeIntegration = None,
        request_id: str = None,
    ):
        # The information about the EventBridge integration.
        self.event_bridge_integration = event_bridge_integration
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.event_bridge_integration:
            self.event_bridge_integration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bridge_integration is not None:
            result['EventBridgeIntegration'] = self.event_bridge_integration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBridgeIntegration') is not None:
            temp_model = main_models.CreateOrUpdateEventBridgeIntegrationResponseBodyEventBridgeIntegration()
            self.event_bridge_integration = temp_model.from_map(m.get('EventBridgeIntegration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateOrUpdateEventBridgeIntegrationResponseBodyEventBridgeIntegration(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        description: str = None,
        endpoint: str = None,
        event_bus_name: str = None,
        event_bus_region_id: str = None,
        id: int = None,
        name: str = None,
        source: str = None,
    ):
        # The AccessKey ID that is used to connect to EventBridge.
        self.access_key = access_key
        # The AccessKey secret that is used to connect to EventBridge.
        self.access_secret = access_secret
        # The description of the EventBridge integration.
        self.description = description
        # The public endpoint of EventBridge.
        self.endpoint = endpoint
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The region ID of the event bus.
        self.event_bus_region_id = event_bus_region_id
        # The ID of the EventBridge integration.
        self.id = id
        # The name of the EventBridge integration.
        self.name = name
        # The event source.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret

        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.event_bus_region_id is not None:
            result['EventBusRegionId'] = self.event_bus_region_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('EventBusRegionId') is not None:
            self.event_bus_region_id = m.get('EventBusRegionId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self


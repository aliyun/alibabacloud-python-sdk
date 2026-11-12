# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListEventBusesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListEventBusesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code:
        # - Success: indicates that the request is successful.                                 
        # - Other values: indicate error codes. For more information, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. A value of true indicates that the operation is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListEventBusesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEventBusesResponseBodyData(DaraModel):
    def __init__(
        self,
        event_buses: List[main_models.ListEventBusesResponseBodyDataEventBuses] = None,
        next_token: str = None,
        total: int = None,
    ):
        # The list of queried event buses.
        self.event_buses = event_buses
        # The pagination token. This token is returned if more results are available.
        self.next_token = next_token
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.event_buses:
            for v1 in self.event_buses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventBuses'] = []
        if self.event_buses is not None:
            for k1 in self.event_buses:
                result['EventBuses'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_buses = []
        if m.get('EventBuses') is not None:
            for k1 in m.get('EventBuses'):
                temp_model = main_models.ListEventBusesResponseBodyDataEventBuses()
                self.event_buses.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListEventBusesResponseBodyDataEventBuses(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        description: str = None,
        event_bus_arn: str = None,
        event_bus_name: str = None,
        resource_group_id: str = None,
        tags: List[main_models.ListEventBusesResponseBodyDataEventBusesTags] = None,
    ):
        # The creation timestamp.
        self.create_timestamp = create_timestamp
        # The description.
        self.description = description
        # The Alibaba Cloud Resource Name (ARN) of the event bus.
        self.event_bus_arn = event_bus_arn
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The ID of the resource group to which the event bus belongs.
        self.resource_group_id = resource_group_id
        # The tag information of the event bus.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.description is not None:
            result['Description'] = self.description

        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListEventBusesResponseBodyDataEventBusesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListEventBusesResponseBodyDataEventBusesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the event bus tag.
        self.key = key
        # The value of the event bus tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


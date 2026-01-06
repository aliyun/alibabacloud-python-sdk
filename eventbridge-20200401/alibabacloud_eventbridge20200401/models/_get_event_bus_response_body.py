# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class GetEventBusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetEventBusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value Success indicates that the request was successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # The data returned.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. If the operation was successful, the value true is returned.
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
            temp_model = main_models.GetEventBusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetEventBusResponseBodyData(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        description: str = None,
        event_bus_arn: str = None,
        event_bus_name: str = None,
    ):
        # The timestamp that indicates when the event bus was created.
        self.create_timestamp = create_timestamp
        # The description of the event bus.
        self.description = description
        # The Alibaba Cloud Resource Name (ARN) of the event bus.
        self.event_bus_arn = event_bus_arn
        # The name of the event bus.
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

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

        return self


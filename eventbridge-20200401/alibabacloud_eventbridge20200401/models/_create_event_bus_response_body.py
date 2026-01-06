# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateEventBusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateEventBusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. The value true indicates that the request is successful.
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
            temp_model = main_models.CreateEventBusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateEventBusResponseBodyData(DaraModel):
    def __init__(
        self,
        event_bus_arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the event bus.
        self.event_bus_arn = event_bus_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateEventSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateEventSourceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        # 
        # - `Success`: The request was successful.
        # 
        # - Other values indicate errors. For more information, see the "Error codes" section.
        self.code = code
        # The data returned by the request.
        self.data = data
        # The error message returned if the request is unsuccessful.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. A value of `true` indicates that the request was successful.
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
            temp_model = main_models.CreateEventSourceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateEventSourceResponseBodyData(DaraModel):
    def __init__(
        self,
        event_source_arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the event source.
        self.event_source_arn = event_source_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_source_arn is not None:
            result['EventSourceARN'] = self.event_source_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSourceARN') is not None:
            self.event_source_arn = m.get('EventSourceARN')

        return self


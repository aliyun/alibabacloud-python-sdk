# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class MultiModalAgentSSEResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MultiModalAgentSSEResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # Id of the request
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.MultiModalAgentSSEResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class MultiModalAgentSSEResponseBodyData(DaraModel):
    def __init__(
        self,
        created: int = None,
        data_id: str = None,
        finish_reason: str = None,
        output: str = None,
        usage: main_models.MultiModalAgentSSEResponseBodyDataUsage = None,
    ):
        # The timestamp when the session was created.
        self.created = created
        # The value of dataId passed in the API request. This field is not returned if dataId is not specified in the request.
        self.data_id = data_id
        # If streaming output is used, this field is null during generation. When generation ends, this field is set to stop if the generation stopped due to a stop token.
        self.finish_reason = finish_reason
        # The output result.
        self.output = output
        # The credits usage.
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['Created'] = self.created

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.finish_reason is not None:
            result['FinishReason'] = self.finish_reason

        if self.output is not None:
            result['Output'] = self.output

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Usage') is not None:
            temp_model = main_models.MultiModalAgentSSEResponseBodyDataUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class MultiModalAgentSSEResponseBodyDataUsage(DaraModel):
    def __init__(
        self,
        credits: float = None,
    ):
        # The number of credits consumed.
        self.credits = credits

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credits is not None:
            result['Credits'] = self.credits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credits') is not None:
            self.credits = m.get('Credits')

        return self


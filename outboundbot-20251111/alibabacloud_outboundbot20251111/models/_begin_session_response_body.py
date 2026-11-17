# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class BeginSessionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BeginSessionResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # The business status code.
        self.code = code
        # The text conversation reply.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The business message.
        self.message = message
        # The list of error message parameters.
        self.params = params
        # The request ID.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.BeginSessionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BeginSessionResponseBodyData(DaraModel):
    def __init__(
        self,
        answer: str = None,
        control_params_list: List[main_models.BeginSessionResponseBodyDataControlParamsList] = None,
        end_time: int = None,
        extras: main_models.BeginSessionResponseBodyDataExtras = None,
        session_id: str = None,
        start_time: int = None,
        stream_end: bool = None,
        stream_id: str = None,
    ):
        # The reply content from the robot.
        self.answer = answer
        # The list of robot control instructions.
        self.control_params_list = control_params_list
        # The time when the current reply event is sent.
        self.end_time = end_time
        # The extended information of the reply.
        self.extras = extras
        # The session ID.
        self.session_id = session_id
        # The time of the first reply event in the current round.
        self.start_time = start_time
        # Indicates whether the response stream for the current round has ended.
        self.stream_end = stream_end
        # The reply round ID.
        self.stream_id = stream_id

    def validate(self):
        if self.control_params_list:
            for v1 in self.control_params_list:
                 if v1:
                    v1.validate()
        if self.extras:
            self.extras.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        result['ControlParamsList'] = []
        if self.control_params_list is not None:
            for k1 in self.control_params_list:
                result['ControlParamsList'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.extras is not None:
            result['Extras'] = self.extras.to_map()

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_end is not None:
            result['StreamEnd'] = self.stream_end

        if self.stream_id is not None:
            result['StreamId'] = self.stream_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        self.control_params_list = []
        if m.get('ControlParamsList') is not None:
            for k1 in m.get('ControlParamsList'):
                temp_model = main_models.BeginSessionResponseBodyDataControlParamsList()
                self.control_params_list.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Extras') is not None:
            temp_model = main_models.BeginSessionResponseBodyDataExtras()
            self.extras = temp_model.from_map(m.get('Extras'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamEnd') is not None:
            self.stream_end = m.get('StreamEnd')

        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')

        return self

class BeginSessionResponseBodyDataExtras(DaraModel):
    def __init__(
        self,
        debug_info: str = None,
    ):
        # The debug information of the conversation.
        self.debug_info = debug_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')

        return self

class BeginSessionResponseBodyDataControlParamsList(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The type of the control instruction.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


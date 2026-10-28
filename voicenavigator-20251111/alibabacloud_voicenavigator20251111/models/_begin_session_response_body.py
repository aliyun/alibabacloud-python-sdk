# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
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
        # The business status code. A value of OK indicates that the request is successful.
        self.code = code
        # The business data.
        self.data = data
        # The HTTP status code. A value of 200 indicates that the HTTP request is successful.
        self.http_status_code = http_status_code
        # The HTTP response message.
        self.message = message
        # The dynamic error parameters.
        self.params = params
        # The POP request ID.
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
        session_id: str = None,
        start_time: int = None,
        stream_end: bool = None,
        stream_id: str = None,
    ):
        # The chatbot reply content.
        self.answer = answer
        # The list of control parameters.
        self.control_params_list = control_params_list
        # The end time.
        self.end_time = end_time
        # The session ID.
        self.session_id = session_id
        # The start time.
        self.start_time = start_time
        # Specifies whether the streaming response has ended.
        self.stream_end = stream_end
        # The turn ID of the conversation.
        self.stream_id = stream_id

    def validate(self):
        if self.control_params_list:
            for v1 in self.control_params_list:
                 if v1:
                    v1.validate()

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

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamEnd') is not None:
            self.stream_end = m.get('StreamEnd')

        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')

        return self



class BeginSessionResponseBodyDataControlParamsList(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The control parameter type. Valid values:
        # >- HangUp: Hang up.
        # >- Transfer: Transfer.
        # >- GatherDtmf: Gather DTMF.
        # >- Voice: Voice.
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


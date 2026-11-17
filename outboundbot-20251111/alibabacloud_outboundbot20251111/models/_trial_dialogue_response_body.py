# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class TrialDialogueResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.TrialDialogueResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # The business processing status code. OK indicates success. When an exception occurs, the corresponding business error code is returned. The error types and mapping rules follow the current API configuration, and no error codes are added or modified in this update.
        self.code = code
        # The robot reply, turn ID, time, and control commands carried by the current SSE event. A single turn may have multiple events.
        self.data = data
        # The HTTP status code recorded in the business response body. A normal return is 200. To determine whether the business is successful, you should also check Code. You cannot determine that the call is successful solely based on the presence of this field.
        self.http_status_code = http_status_code
        # The business response or error description. It is usually empty or not returned upon success, and you cannot require a fixed text to be returned upon success. Upon failure, it is an error description used to assist troubleshooting, and should be combined with Code and Params to understand the cause of the error. The example is an error message when the experience link visitor token expires (corresponding to Code Expired.VisitorToken), and is for format reference only.
        self.message = message
        # The list of parameters used for the localized display of error messages, which are not scenario variables or business results. A normal successful response is usually an empty array. When an error occurs, parameters corresponding to the error template may be returned.
        self.params = params
        # The ID used to associate and troubleshoot this POP request. The value in the response corresponds to this request. System request parameters are injected by the gateway, and the caller does not need to fill in system fields.
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
            temp_model = main_models.TrialDialogueResponseBodyData()
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

class TrialDialogueResponseBodyData(DaraModel):
    def __init__(
        self,
        answer: str = None,
        control_params_list: List[main_models.TrialDialogueResponseBodyDataControlParamsList] = None,
        end_time: int = None,
        extras: main_models.TrialDialogueResponseBodyDataExtras = None,
        session_id: str = None,
        start_time: int = None,
        stream_end: bool = None,
        stream_id: str = None,
    ):
        # The robot reply text in the current streaming event. It may be returned across multiple SSE events, or it may be empty in the end event or debug event. Do not equate missing text with session failure. Whether the content is incremental or cumulative is determined by the output convention of the dialogue engine. The current general callback directly forwards the engine content.
        self.answer = answer
        # The robot control commands attached to this reply. The current POP structure only expands the command Type and does not add other command fields in this document. When no control commands are generated, the text service supplements a Voice type command.
        self.control_params_list = control_params_list
        # The UNIX timestamp of the current streaming reply callback event, in milliseconds. It is generated based on the current callback time. It may also be returned when StreamEnd=false, and should not be directly interpreted as the end time of the entire conversation or call.
        self.end_time = end_time
        # The extended information object attached to the robot reply, which is different from the JSON event array of the request parameter Extras. The current POP expands the DebugInfo field. Whether it is actually returned depends on the engine used and the current turn of reply.
        self.extras = extras
        # The session ID used to uniquely associate this interaction. For a text conversation, it is the text- identifier returned when the conversation is started. For web voice, it is the ws- identifier. For real number outbound call tests, it is the test- identifier. Subsequent calls must use the actual return value.
        self.session_id = session_id
        # The UNIX timestamp recorded when the streaming reply callback is entered for the first time in this turn, in milliseconds. Subsequent events in this turn use this time. It is not the session creation time, nor is it an update time in the general sense.
        self.start_time = start_time
        # Indicates whether the streaming output for the current reply turn has ended. A value of true indicates that the streaming output has ended and the service has completed the corresponding SSE response. A value of false indicates that there may still be subsequent events in this turn. This field does not indicate that the entire conversation or voice call has ended.
        self.stream_end = stream_end
        # The ID of the conversation turn to which this robot reply belongs. The same turn of reply can contain multiple streaming events. The text conversation context starts from 0 and increments during subsequent Dialogue calls. The actual return value of the engine shall prevail.
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
                temp_model = main_models.TrialDialogueResponseBodyDataControlParamsList()
                self.control_params_list.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Extras') is not None:
            temp_model = main_models.TrialDialogueResponseBodyDataExtras()
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

class TrialDialogueResponseBodyDataExtras(DaraModel):
    def __init__(
        self,
        debug_info: str = None,
    ):
        # The debug information returned by the dialogue engine as a JSON string. It is returned only when the engine provides the debug information, and may be returned with supplementary events after the reply ends. The internal structure is determined by the engine. The example empty object string does not declare any fixed debug fields.
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

class TrialDialogueResponseBodyDataControlParamsList(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The values declared in the control command type include Voice (voice reply), HangUp (hang up), Transfer (transfer), GatherDtmf (collect key presses), and SendSms (send SMS). This update supplements SendSms, which was omitted in the original description, without changing the backend structure or runtime enumeration constraints.
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QueryConversationDetailInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QueryConversationDetailInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The status code.
        self.code = code
        # The response data.
        self.data = data
        # The status code message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryConversationDetailInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryConversationDetailInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        call_result: str = None,
        called_phone: str = None,
        caller_phone: str = None,
        conversation_record: str = None,
        duration: int = None,
        encryption_type: str = None,
        failed_reason: str = None,
        hangup_direction: str = None,
        major_intent: str = None,
        out_id: str = None,
        output_tags: List[main_models.QueryConversationDetailInfoResponseBodyDataOutputTags] = None,
        pick_up_time: int = None,
        recording_file_download_url: str = None,
        release_time: int = None,
        start_call_time: int = None,
        status_code: str = None,
        status_msg: str = None,
        variables: List[main_models.QueryConversationDetailInfoResponseBodyDataVariables] = None,
    ):
        # The unique call ID.
        self.call_id = call_id
        # The call result. Valid values:
        # 
        # - `CALL_FORWARDING`: Call forwarding.
        # 
        # - `INCOMING_CALL_BARRED`: Incoming call barred.
        # 
        # - `CALL_REJECTED`: Call rejected.
        # 
        # - `ANSWERED`: Answered by user.
        # 
        # - `USER_BUSY`: Called party busy.
        # 
        # - `POWERED_OFF`: Powered off.
        # 
        # - `NO_USER_RESPONSE`: Out of service area.
        # 
        # - `OPERATOR_BLOCK`: Blocked by carrier.
        # 
        # - `OTHERS`: Other.
        # 
        # - `SUSPEND`: Suspended.
        # 
        # - `CANCEL`: Canceled by caller.
        # 
        # - `INVALID_NUMBER`: Invalid number.
        # 
        # - `UNAVAILABLE`: Temporarily unavailable.
        # 
        # - `NETWORK_BUSY`: Network busy.
        # 
        # - `NO_ANSWER`: No answer.
        self.call_result = call_result
        # The called number.
        self.called_phone = called_phone
        # The caller number.
        self.caller_phone = caller_phone
        # The conversation record. The structure is a JSON array in which entries are sorted by time. Example:
        # 
        # ```json
        # [
        #     {
        #         "content":"Conversation content",
        #         "role":"Role", // Valid values: user, assistant
        #     }
        # ]
        # ```
        self.conversation_record = conversation_record
        # The duration of the call, in seconds. If the call was not connected, the value is 0.
        self.duration = duration
        self.encryption_type = encryption_type
        # The failure reason.
        self.failed_reason = failed_reason
        # The party that hung up. Valid values:
        # 
        # - **0**: user.
        # 
        # - **1**: assistant.
        self.hangup_direction = hangup_direction
        # The primary intent.
        self.major_intent = major_intent
        # The business-specific ID that is passed in. You can use this unique ID to associate the call with your business.
        self.out_id = out_id
        # A list of output tags.
        self.output_tags = output_tags
        # The timestamp when the call was answered, in milliseconds.
        self.pick_up_time = pick_up_time
        # The download URL for the recording file. This parameter is returned only after the recording file is generated.
        self.recording_file_download_url = recording_file_download_url
        # The timestamp when the call ended, in milliseconds.
        self.release_time = release_time
        # The timestamp when the call was initiated, in milliseconds.
        self.start_call_time = start_call_time
        # The call status code. For more information, see [Call status codes](https://help.aliyun.com/document_detail/112804.html) for the voice service.
        self.status_code = status_code
        # The status message returned by the carrier.
        self.status_msg = status_msg
        # A list of variables associated with the call task.
        self.variables = variables

    def validate(self):
        if self.output_tags:
            for v1 in self.output_tags:
                 if v1:
                    v1.validate()
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_result is not None:
            result['CallResult'] = self.call_result

        if self.called_phone is not None:
            result['CalledPhone'] = self.called_phone

        if self.caller_phone is not None:
            result['CallerPhone'] = self.caller_phone

        if self.conversation_record is not None:
            result['ConversationRecord'] = self.conversation_record

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type

        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason

        if self.hangup_direction is not None:
            result['HangupDirection'] = self.hangup_direction

        if self.major_intent is not None:
            result['MajorIntent'] = self.major_intent

        if self.out_id is not None:
            result['OutId'] = self.out_id

        result['OutputTags'] = []
        if self.output_tags is not None:
            for k1 in self.output_tags:
                result['OutputTags'].append(k1.to_map() if k1 else None)

        if self.pick_up_time is not None:
            result['PickUpTime'] = self.pick_up_time

        if self.recording_file_download_url is not None:
            result['RecordingFileDownloadUrl'] = self.recording_file_download_url

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.start_call_time is not None:
            result['StartCallTime'] = self.start_call_time

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.status_msg is not None:
            result['StatusMsg'] = self.status_msg

        result['Variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['Variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')

        if m.get('CalledPhone') is not None:
            self.called_phone = m.get('CalledPhone')

        if m.get('CallerPhone') is not None:
            self.caller_phone = m.get('CallerPhone')

        if m.get('ConversationRecord') is not None:
            self.conversation_record = m.get('ConversationRecord')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')

        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')

        if m.get('HangupDirection') is not None:
            self.hangup_direction = m.get('HangupDirection')

        if m.get('MajorIntent') is not None:
            self.major_intent = m.get('MajorIntent')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        self.output_tags = []
        if m.get('OutputTags') is not None:
            for k1 in m.get('OutputTags'):
                temp_model = main_models.QueryConversationDetailInfoResponseBodyDataOutputTags()
                self.output_tags.append(temp_model.from_map(k1))

        if m.get('PickUpTime') is not None:
            self.pick_up_time = m.get('PickUpTime')

        if m.get('RecordingFileDownloadUrl') is not None:
            self.recording_file_download_url = m.get('RecordingFileDownloadUrl')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('StartCallTime') is not None:
            self.start_call_time = m.get('StartCallTime')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('StatusMsg') is not None:
            self.status_msg = m.get('StatusMsg')

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.QueryConversationDetailInfoResponseBodyDataVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class QueryConversationDetailInfoResponseBodyDataVariables(DaraModel):
    def __init__(
        self,
        id: str = None,
        key: str = None,
        name: str = None,
        required: bool = None,
        source: str = None,
        value: str = None,
    ):
        # The variable ID.
        self.id = id
        # The variable key.
        self.key = key
        # The variable name.
        self.name = name
        # Indicates whether the variable is required. Valid values:
        # 
        # - `true`: The variable is required.
        # 
        # - `false`: The variable is optional.
        self.required = required
        self.source = source
        # The variable value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        if self.required is not None:
            result['Required'] = self.required

        if self.source is not None:
            result['Source'] = self.source

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class QueryConversationDetailInfoResponseBodyDataOutputTags(DaraModel):
    def __init__(
        self,
        id: str = None,
        output_tag_description: str = None,
        output_tag_name: str = None,
        output_tag_value: str = None,
    ):
        # The tag ID.
        self.id = id
        # The tag description.
        self.output_tag_description = output_tag_description
        # The tag name.
        self.output_tag_name = output_tag_name
        # The tag value.
        self.output_tag_value = output_tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.output_tag_description is not None:
            result['OutputTagDescription'] = self.output_tag_description

        if self.output_tag_name is not None:
            result['OutputTagName'] = self.output_tag_name

        if self.output_tag_value is not None:
            result['OutputTagValue'] = self.output_tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OutputTagDescription') is not None:
            self.output_tag_description = m.get('OutputTagDescription')

        if m.get('OutputTagName') is not None:
            self.output_tag_name = m.get('OutputTagName')

        if m.get('OutputTagValue') is not None:
            self.output_tag_value = m.get('OutputTagValue')

        return self


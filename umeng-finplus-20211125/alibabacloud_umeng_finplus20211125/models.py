# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetMessageStatusRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetMessageStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.mobile = mobile
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetMessageStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetMessageStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetMessageStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMessageStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMessageStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMessageStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendBatchMessageRequest(TeaModel):
    def __init__(
        self,
        batch_flag: str = None,
        extend_info: str = None,
        id_type: str = None,
        phone_number_json: str = None,
        sign_name_json: str = None,
        specific_channel: str = None,
        template_code: str = None,
        template_param_json: str = None,
    ):
        self.batch_flag = batch_flag
        self.extend_info = extend_info
        self.id_type = id_type
        self.phone_number_json = phone_number_json
        self.sign_name_json = sign_name_json
        self.specific_channel = specific_channel
        self.template_code = template_code
        self.template_param_json = template_param_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_flag is not None:
            result['BatchFlag'] = self.batch_flag
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json
        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json
        if self.specific_channel is not None:
            result['SpecificChannel'] = self.specific_channel
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param_json is not None:
            result['TemplateParamJson'] = self.template_param_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchFlag') is not None:
            self.batch_flag = m.get('BatchFlag')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')
        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')
        if m.get('SpecificChannel') is not None:
            self.specific_channel = m.get('SpecificChannel')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParamJson') is not None:
            self.template_param_json = m.get('TemplateParamJson')
        return self


class SendBatchMessageResponseBodyData(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        task_id: str = None,
    ):
        self.mobile = mobile
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SendBatchMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[SendBatchMessageResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SendBatchMessageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendBatchMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendBatchMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendBatchMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



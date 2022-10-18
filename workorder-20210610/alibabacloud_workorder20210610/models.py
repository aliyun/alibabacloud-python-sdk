# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CloseTicketRequest(TeaModel):
    def __init__(
        self,
        ticket_id: str = None,
    ):
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class CloseTicketResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CloseTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTicketRequestSecretInfo(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_name_list: List[str] = None,
    ):
        self.content = content
        self.file_name_list = file_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')
        return self


class CreateTicketRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        creator_id: str = None,
        description: str = None,
        email: str = None,
        file_name_list: List[str] = None,
        secret_info: CreateTicketRequestSecretInfo = None,
        severity: int = None,
        title: str = None,
    ):
        self.category_id = category_id
        self.creator_id = creator_id
        self.description = description
        self.email = email
        self.file_name_list = file_name_list
        self.secret_info = secret_info
        self.severity = severity
        self.title = title

    def validate(self):
        if self.secret_info:
            self.secret_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list
        if self.secret_info is not None:
            result['SecretInfo'] = self.secret_info.to_map()
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')
        if m.get('SecretInfo') is not None:
            temp_model = CreateTicketRequestSecretInfo()
            self.secret_info = temp_model.from_map(m['SecretInfo'])
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateTicketShrinkRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        creator_id: str = None,
        description: str = None,
        email: str = None,
        file_name_list_shrink: str = None,
        secret_info_shrink: str = None,
        severity: int = None,
        title: str = None,
    ):
        self.category_id = category_id
        self.creator_id = creator_id
        self.description = description
        self.email = email
        self.file_name_list_shrink = file_name_list_shrink
        self.secret_info_shrink = secret_info_shrink
        self.severity = severity
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.file_name_list_shrink is not None:
            result['FileNameList'] = self.file_name_list_shrink
        if self.secret_info_shrink is not None:
            result['SecretInfo'] = self.secret_info_shrink
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('FileNameList') is not None:
            self.file_name_list_shrink = m.get('FileNameList')
        if m.get('SecretInfo') is not None:
            self.secret_info_shrink = m.get('SecretInfo')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateTicketResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvaluateTicketRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        score: str = None,
        solved: bool = None,
        ticket_id: str = None,
    ):
        self.content = content
        self.score = score
        self.solved = solved
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.score is not None:
            result['Score'] = self.score
        if self.solved is not None:
            result['Solved'] = self.solved
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Solved') is not None:
            self.solved = m.get('Solved')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class EvaluateTicketResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EvaluateTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EvaluateTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = EvaluateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAttachmentUploadUrlRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
    ):
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GetAttachmentUploadUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        get_signed_url: str = None,
        object_key: str = None,
        put_signed_url: str = None,
    ):
        self.get_signed_url = get_signed_url
        self.object_key = object_key
        self.put_signed_url = put_signed_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_signed_url is not None:
            result['GetSignedUrl'] = self.get_signed_url
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.put_signed_url is not None:
            result['PutSignedUrl'] = self.put_signed_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetSignedUrl') is not None:
            self.get_signed_url = m.get('GetSignedUrl')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('PutSignedUrl') is not None:
            self.put_signed_url = m.get('PutSignedUrl')
        return self


class GetAttachmentUploadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAttachmentUploadUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAttachmentUploadUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAttachmentUploadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAttachmentUploadUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetAttachmentUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMqConsumerTagResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMqConsumerTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMqConsumerTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetMqConsumerTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTicketRequest(TeaModel):
    def __init__(
        self,
        ticket_id: str = None,
    ):
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class GetTicketResponseBodyDataSeverity(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTicketResponseBodyDataStatus(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTicketResponseBodyData(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        create_time: int = None,
        creator_id: str = None,
        description: str = None,
        severity: GetTicketResponseBodyDataSeverity = None,
        status: GetTicketResponseBodyDataStatus = None,
        ticket_id: str = None,
        title: str = None,
    ):
        self.category_id = category_id
        self.create_time = create_time
        self.creator_id = creator_id
        self.description = description
        self.severity = severity
        self.status = status
        self.ticket_id = ticket_id
        self.title = title

    def validate(self):
        if self.severity:
            self.severity.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.severity is not None:
            result['Severity'] = self.severity.to_map()
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Severity') is not None:
            temp_model = GetTicketResponseBodyDataSeverity()
            self.severity = temp_model.from_map(m['Severity'])
        if m.get('Status') is not None:
            temp_model = GetTicketResponseBodyDataStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTicketResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTicketResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTicketResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCategoriesRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        name: str = None,
        product_id: int = None,
    ):
        self.language = language
        self.name = name
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class ListCategoriesResponseBodyData(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        category_name: str = None,
    ):
        self.category_id = category_id
        self.category_name = category_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        return self


class ListCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListCategoriesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCategoriesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCategoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        name: str = None,
    ):
        self.language = language
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListProductsResponseBodyDataProductList(TeaModel):
    def __init__(
        self,
        product_id: int = None,
        product_name: str = None,
    ):
        self.product_id = product_id
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class ListProductsResponseBodyData(TeaModel):
    def __init__(
        self,
        directory_id: int = None,
        directory_name: str = None,
        product_list: List[ListProductsResponseBodyDataProductList] = None,
    ):
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.product_list = product_list

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = ListProductsResponseBodyDataProductList()
                self.product_list.append(temp_model.from_map(k))
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListProductsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListProductsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTicketNotesRequest(TeaModel):
    def __init__(
        self,
        ticket_id: str = None,
    ):
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class ListTicketNotesResponseBodyDataAttachments(TeaModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        self.name = name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListTicketNotesResponseBodyDataDialog(TeaModel):
    def __init__(
        self,
        content: str = None,
        schema: str = None,
    ):
        self.content = content
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class ListTicketNotesResponseBodyDataUser(TeaModel):
    def __init__(
        self,
        name: str = None,
        role: int = None,
    ):
        self.name = name
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ListTicketNotesResponseBodyData(TeaModel):
    def __init__(
        self,
        attachments: List[ListTicketNotesResponseBodyDataAttachments] = None,
        create_time: int = None,
        dialog: ListTicketNotesResponseBodyDataDialog = None,
        dialog_id: int = None,
        status: int = None,
        tip: str = None,
        type: int = None,
        user: ListTicketNotesResponseBodyDataUser = None,
    ):
        self.attachments = attachments
        self.create_time = create_time
        self.dialog = dialog
        self.dialog_id = dialog_id
        self.status = status
        self.tip = tip
        self.type = type
        self.user = user

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()
        if self.dialog:
            self.dialog.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['Attachments'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dialog is not None:
            result['Dialog'] = self.dialog.to_map()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tip is not None:
            result['Tip'] = self.tip
        if self.type is not None:
            result['Type'] = self.type
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('Attachments') is not None:
            for k in m.get('Attachments'):
                temp_model = ListTicketNotesResponseBodyDataAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dialog') is not None:
            temp_model = ListTicketNotesResponseBodyDataDialog()
            self.dialog = temp_model.from_map(m['Dialog'])
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tip') is not None:
            self.tip = m.get('Tip')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('User') is not None:
            temp_model = ListTicketNotesResponseBodyDataUser()
            self.user = temp_model.from_map(m['User'])
        return self


class ListTicketNotesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListTicketNotesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTicketNotesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTicketNotesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTicketNotesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTicketNotesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTicketsRequest(TeaModel):
    def __init__(
        self,
        end_date: int = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: int = None,
        status_list: List[str] = None,
        ticket_id: str = None,
        ticket_id_list: List[str] = None,
    ):
        self.end_date = end_date
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.status_list = status_list
        self.ticket_id = ticket_id
        self.ticket_id_list = ticket_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.ticket_id_list is not None:
            result['TicketIdList'] = self.ticket_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('TicketIdList') is not None:
            self.ticket_id_list = m.get('TicketIdList')
        return self


class ListTicketsShrinkRequest(TeaModel):
    def __init__(
        self,
        end_date: int = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: int = None,
        status_list: List[str] = None,
        ticket_id: str = None,
        ticket_id_list_shrink: str = None,
    ):
        self.end_date = end_date
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.status_list = status_list
        self.ticket_id = ticket_id
        self.ticket_id_list_shrink = ticket_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.ticket_id_list_shrink is not None:
            result['TicketIdList'] = self.ticket_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('TicketIdList') is not None:
            self.ticket_id_list_shrink = m.get('TicketIdList')
        return self


class ListTicketsResponseBodyDataStatus(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTicketsResponseBodyData(TeaModel):
    def __init__(
        self,
        status: ListTicketsResponseBodyDataStatus = None,
        ticket_id: str = None,
        title: str = None,
    ):
        self.status = status
        self.ticket_id = ticket_id
        self.title = title

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            temp_model = ListTicketsResponseBodyDataStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListTicketsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListTicketsResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTicketsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTicketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTicketsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReopenTicketRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        ticket_id: str = None,
    ):
        self.content = content
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class ReopenTicketResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReopenTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReopenTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ReopenTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplyTicketRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        encrypt: bool = None,
        file_name_list: List[str] = None,
        ticket_id: str = None,
    ):
        self.content = content
        self.encrypt = encrypt
        self.file_name_list = file_name_list
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class ReplyTicketShrinkRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        encrypt: bool = None,
        file_name_list_shrink: str = None,
        ticket_id: str = None,
    ):
        self.content = content
        self.encrypt = encrypt
        self.file_name_list_shrink = file_name_list_shrink
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.file_name_list_shrink is not None:
            result['FileNameList'] = self.file_name_list_shrink
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('FileNameList') is not None:
            self.file_name_list_shrink = m.get('FileNameList')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class ReplyTicketResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReplyTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReplyTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ReplyTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



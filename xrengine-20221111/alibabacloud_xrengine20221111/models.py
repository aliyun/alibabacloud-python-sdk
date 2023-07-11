# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddWhitelistRequest(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        remark: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class AddWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddWhitelistResponseBody = None,
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
            temp_model = AddWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthUserRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
    ):
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class AuthUserResponseBodyData(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        type: str = None,
    ):
        self.jwt_token = jwt_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AuthUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AuthUserResponseBodyData = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = AuthUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthUserResponseBody = None,
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
            temp_model = AuthUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreateSvcMapBindRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        map_ids: List[int] = None,
        svc_id: int = None,
    ):
        self.jwt_token = jwt_token
        self.map_ids = map_ids
        self.svc_id = svc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.map_ids is not None:
            result['MapIds'] = self.map_ids
        if self.svc_id is not None:
            result['SvcId'] = self.svc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('MapIds') is not None:
            self.map_ids = m.get('MapIds')
        if m.get('SvcId') is not None:
            self.svc_id = m.get('SvcId')
        return self


class BatchCreateSvcMapBindShrinkRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        map_ids_shrink: str = None,
        svc_id: int = None,
    ):
        self.jwt_token = jwt_token
        self.map_ids_shrink = map_ids_shrink
        self.svc_id = svc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.map_ids_shrink is not None:
            result['MapIds'] = self.map_ids_shrink
        if self.svc_id is not None:
            result['SvcId'] = self.svc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('MapIds') is not None:
            self.map_ids_shrink = m.get('MapIds')
        if m.get('SvcId') is not None:
            self.svc_id = m.get('SvcId')
        return self


class BatchCreateSvcMapBindResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchCreateSvcMapBindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCreateSvcMapBindResponseBody = None,
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
            temp_model = BatchCreateSvcMapBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteSvcMapBindRequest(TeaModel):
    def __init__(
        self,
        ids: List[int] = None,
        jwt_token: str = None,
    ):
        self.ids = ids
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class BatchDeleteSvcMapBindShrinkRequest(TeaModel):
    def __init__(
        self,
        ids_shrink: str = None,
        jwt_token: str = None,
    ):
        self.ids_shrink = ids_shrink
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class BatchDeleteSvcMapBindResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchDeleteSvcMapBindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteSvcMapBindResponseBody = None,
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
            temp_model = BatchDeleteSvcMapBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BuildProjectRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        project_id: str = None,
        video_name: str = None,
    ):
        self.jwt_token = jwt_token
        self.project_id = project_id
        self.video_name = video_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        return self


class BuildProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class BuildProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BuildProjectResponseBody = None,
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
            temp_model = BuildProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLocationServiceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        image_id: int = None,
        jwt_token: str = None,
        name: str = None,
        note: str = None,
        qps: int = None,
    ):
        self.app_id = app_id
        self.image_id = image_id
        self.jwt_token = jwt_token
        self.name = name
        self.note = note
        self.qps = qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.name is not None:
            result['Name'] = self.name
        if self.note is not None:
            result['Note'] = self.note
        if self.qps is not None:
            result['Qps'] = self.qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        return self


class CreateLocationServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLocationServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLocationServiceResponseBody = None,
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
            temp_model = CreateLocationServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequestTryOnParamsClothInfos(TeaModel):
    def __init__(
        self,
        id: int = None,
        size: str = None,
        status: str = None,
    ):
        self.id = id
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateProjectRequestTryOnParams(TeaModel):
    def __init__(
        self,
        cloth_ids: List[int] = None,
        cloth_infos: List[CreateProjectRequestTryOnParamsClothInfos] = None,
    ):
        self.cloth_ids = cloth_ids
        self.cloth_infos = cloth_infos

    def validate(self):
        if self.cloth_infos:
            for k in self.cloth_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloth_ids is not None:
            result['ClothIds'] = self.cloth_ids
        result['ClothInfos'] = []
        if self.cloth_infos is not None:
            for k in self.cloth_infos:
                result['ClothInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClothIds') is not None:
            self.cloth_ids = m.get('ClothIds')
        self.cloth_infos = []
        if m.get('ClothInfos') is not None:
            for k in m.get('ClothInfos'):
                temp_model = CreateProjectRequestTryOnParamsClothInfos()
                self.cloth_infos.append(temp_model.from_map(k))
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        auto_build: bool = None,
        dependencies: str = None,
        gender: str = None,
        height: float = None,
        intro: str = None,
        jwt_token: str = None,
        map_uuid: str = None,
        method: str = None,
        mode: str = None,
        title: str = None,
        try_on_params: CreateProjectRequestTryOnParams = None,
        type: str = None,
        weight: float = None,
    ):
        self.auto_build = auto_build
        self.dependencies = dependencies
        self.gender = gender
        self.height = height
        self.intro = intro
        self.jwt_token = jwt_token
        self.map_uuid = map_uuid
        self.method = method
        self.mode = mode
        self.title = title
        self.try_on_params = try_on_params
        self.type = type
        self.weight = weight

    def validate(self):
        if self.try_on_params:
            self.try_on_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.height is not None:
            result['Height'] = self.height
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.map_uuid is not None:
            result['MapUuid'] = self.map_uuid
        if self.method is not None:
            result['Method'] = self.method
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.title is not None:
            result['Title'] = self.title
        if self.try_on_params is not None:
            result['TryOnParams'] = self.try_on_params.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('MapUuid') is not None:
            self.map_uuid = m.get('MapUuid')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TryOnParams') is not None:
            temp_model = CreateProjectRequestTryOnParams()
            self.try_on_params = temp_model.from_map(m['TryOnParams'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_build: bool = None,
        dependencies: str = None,
        gender: str = None,
        height: float = None,
        intro: str = None,
        jwt_token: str = None,
        map_uuid: str = None,
        method: str = None,
        mode: str = None,
        title: str = None,
        try_on_params_shrink: str = None,
        type: str = None,
        weight: float = None,
    ):
        self.auto_build = auto_build
        self.dependencies = dependencies
        self.gender = gender
        self.height = height
        self.intro = intro
        self.jwt_token = jwt_token
        self.map_uuid = map_uuid
        self.method = method
        self.mode = mode
        self.title = title
        self.try_on_params_shrink = try_on_params_shrink
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.height is not None:
            result['Height'] = self.height
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.map_uuid is not None:
            result['MapUuid'] = self.map_uuid
        if self.method is not None:
            result['Method'] = self.method
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.title is not None:
            result['Title'] = self.title
        if self.try_on_params_shrink is not None:
            result['TryOnParams'] = self.try_on_params_shrink
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('MapUuid') is not None:
            self.map_uuid = m.get('MapUuid')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TryOnParams') is not None:
            self.try_on_params_shrink = m.get('TryOnParams')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateProjectResponseBodyDataDatasetPolicy(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.dir = dir
        self.expire = expire
        self.host = host
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class CreateProjectResponseBodyDataDataset(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        modified_time: str = None,
        oss_key: str = None,
        policy: CreateProjectResponseBodyDataDatasetPolicy = None,
    ):
        self.create_time = create_time
        self.id = id
        self.modified_time = modified_time
        self.oss_key = oss_key
        self.policy = policy

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = CreateProjectResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        return self


class CreateProjectResponseBodyDataSourcePolicy(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.dir = dir
        self.expire = expire
        self.host = host
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class CreateProjectResponseBodyDataSource(TeaModel):
    def __init__(
        self,
        oss_key: str = None,
        policy: CreateProjectResponseBodyDataSourcePolicy = None,
    ):
        self.oss_key = oss_key
        self.policy = policy

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = CreateProjectResponseBodyDataSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        return self


class CreateProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        create_mode: str = None,
        create_time: str = None,
        dataset: CreateProjectResponseBodyDataDataset = None,
        id: str = None,
        intro: str = None,
        method: str = None,
        modified_time: str = None,
        source: CreateProjectResponseBodyDataSource = None,
        status: str = None,
        title: str = None,
        type: str = None,
    ):
        self.create_mode = create_mode
        self.create_time = create_time
        self.dataset = dataset
        self.id = id
        self.intro = intro
        self.method = method
        self.modified_time = modified_time
        self.source = source
        self.status = status
        self.title = title
        self.type = type

    def validate(self):
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.method is not None:
            result['Method'] = self.method
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = CreateProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = CreateProjectResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateProjectResponseBodyData = None,
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
            temp_model = CreateProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectResponseBody = None,
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSourcePolicyRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        oss_key: str = None,
    ):
        self.jwt_token = jwt_token
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class CreateSourcePolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.dir = dir
        self.expire = expire
        self.host = host
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class CreateSourcePolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateSourcePolicyResponseBodyData = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = CreateSourcePolicyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSourcePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSourcePolicyResponseBody = None,
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
            temp_model = CreateSourcePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        project_id: str = None,
    ):
        self.jwt_token = jwt_token
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProjectResponseBody = None,
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSourceFileRequest(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        jwt_token: str = None,
    ):
        self.file_id = file_id
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class DeleteSourceFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class DeleteSourceFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSourceFileResponseBody = None,
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
            temp_model = DeleteSourceFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployLocationTreeRequest(TeaModel):
    def __init__(
        self,
        force_update: bool = None,
        jwt_token: str = None,
        svc_id: int = None,
    ):
        self.force_update = force_update
        self.jwt_token = jwt_token
        self.svc_id = svc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_update is not None:
            result['ForceUpdate'] = self.force_update
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.svc_id is not None:
            result['SvcId'] = self.svc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceUpdate') is not None:
            self.force_update = m.get('ForceUpdate')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('SvcId') is not None:
            self.svc_id = m.get('SvcId')
        return self


class DeployLocationTreeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeployLocationTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployLocationTreeResponseBody = None,
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
            temp_model = DeployLocationTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindSvcMapBindRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        jwt_token: str = None,
        size: int = None,
        sort: str = None,
        sort_field: str = None,
        svc_id: int = None,
    ):
        self.current = current
        self.jwt_token = jwt_token
        self.size = size
        self.sort = sort
        self.sort_field = sort_field
        self.svc_id = svc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.svc_id is not None:
            result['SvcId'] = self.svc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SvcId') is not None:
            self.svc_id = m.get('SvcId')
        return self


class FindSvcMapBindResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: Dict[str, Any] = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        pages: int = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
        self.message = message
        self.pages = pages
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        if self.data is not None:
            result['Data'] = self.data
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class FindSvcMapBindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindSvcMapBindResponseBody = None,
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
            temp_model = FindSvcMapBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArEditCommonMaterialRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
    ):
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class GetArEditCommonMaterialResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        expiration: int = None,
        oss_bucket: str = None,
        oss_path: str = None,
        oss_region: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.expiration = expiration
        self.oss_bucket = oss_bucket
        self.oss_path = oss_path
        self.oss_region = oss_region
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.oss_region is not None:
            result['OssRegion'] = self.oss_region
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('OssRegion') is not None:
            self.oss_region = m.get('OssRegion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetArEditCommonMaterialResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetArEditCommonMaterialResponseBodyData = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = GetArEditCommonMaterialResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetArEditCommonMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArEditCommonMaterialResponseBody = None,
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
            temp_model = GetArEditCommonMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArEditStsAuthRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        map_id: int = None,
    ):
        self.jwt_token = jwt_token
        self.map_id = map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.map_id is not None:
            result['MapId'] = self.map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('MapId') is not None:
            self.map_id = m.get('MapId')
        return self


class GetArEditStsAuthResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        edit_path: str = None,
        expiration: int = None,
        map_3dpath: str = None,
        oss_bucket: str = None,
        oss_region: str = None,
        publish_path: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.edit_path = edit_path
        self.expiration = expiration
        self.map_3dpath = map_3dpath
        self.oss_bucket = oss_bucket
        self.oss_region = oss_region
        self.publish_path = publish_path
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.edit_path is not None:
            result['EditPath'] = self.edit_path
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.map_3dpath is not None:
            result['Map3DPath'] = self.map_3dpath
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_region is not None:
            result['OssRegion'] = self.oss_region
        if self.publish_path is not None:
            result['PublishPath'] = self.publish_path
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('EditPath') is not None:
            self.edit_path = m.get('EditPath')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Map3DPath') is not None:
            self.map_3dpath = m.get('Map3DPath')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssRegion') is not None:
            self.oss_region = m.get('OssRegion')
        if m.get('PublishPath') is not None:
            self.publish_path = m.get('PublishPath')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetArEditStsAuthResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetArEditStsAuthResponseBodyData = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = GetArEditStsAuthResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetArEditStsAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArEditStsAuthResponseBody = None,
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
            temp_model = GetArEditStsAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArEditUgcMaterialRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        map_id: int = None,
    ):
        self.jwt_token = jwt_token
        self.map_id = map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.map_id is not None:
            result['MapId'] = self.map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('MapId') is not None:
            self.map_id = m.get('MapId')
        return self


class GetArEditUgcMaterialResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        expiration: int = None,
        oss_bucket: str = None,
        oss_path: str = None,
        oss_region: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.expiration = expiration
        self.oss_bucket = oss_bucket
        self.oss_path = oss_path
        self.oss_region = oss_region
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.oss_region is not None:
            result['OssRegion'] = self.oss_region
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('OssRegion') is not None:
            self.oss_region = m.get('OssRegion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetArEditUgcMaterialResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetArEditUgcMaterialResponseBodyData = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = GetArEditUgcMaterialResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetArEditUgcMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArEditUgcMaterialResponseBody = None,
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
            temp_model = GetArEditUgcMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectDatasetRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        oss_key: str = None,
    ):
        self.jwt_token = jwt_token
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class GetProjectDatasetResponseBodyDataDataset(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        create_time: str = None,
        id: str = None,
        model_url: str = None,
        modified_time: str = None,
        origin_result_url: str = None,
        oss_key: str = None,
        pose_url: str = None,
        preview_url: str = None,
    ):
        self.cover_url = cover_url
        self.create_time = create_time
        self.id = id
        self.model_url = model_url
        self.modified_time = modified_time
        self.origin_result_url = origin_result_url
        self.oss_key = oss_key
        self.pose_url = pose_url
        self.preview_url = preview_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class GetProjectDatasetResponseBodyData(TeaModel):
    def __init__(
        self,
        create_mode: str = None,
        create_time: str = None,
        dataset: GetProjectDatasetResponseBodyDataDataset = None,
        id: str = None,
        intro: str = None,
        modified_time: str = None,
        status: str = None,
        title: str = None,
        type: str = None,
        biz_usage: str = None,
    ):
        self.create_mode = create_mode
        self.create_time = create_time
        self.dataset = dataset
        self.id = id
        self.intro = intro
        self.modified_time = modified_time
        self.status = status
        self.title = title
        self.type = type
        self.biz_usage = biz_usage

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_usage is not None:
            result['bizUsage'] = self.biz_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = GetProjectDatasetResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('bizUsage') is not None:
            self.biz_usage = m.get('bizUsage')
        return self


class GetProjectDatasetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetProjectDatasetResponseBodyData = None,
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
            temp_model = GetProjectDatasetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetProjectDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectDatasetResponseBody = None,
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
            temp_model = GetProjectDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAreaMapRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        jwt_token: str = None,
        size: int = None,
        sort: str = None,
        sort_field: str = None,
    ):
        self.current = current
        self.jwt_token = jwt_token
        self.size = size
        self.sort = sort
        self.sort_field = sort_field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        return self


class ListAreaMapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: Dict[str, Any] = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        pages: int = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
        self.message = message
        self.pages = pages
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        if self.data is not None:
            result['Data'] = self.data
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAreaMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAreaMapResponseBody = None,
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
            temp_model = ListAreaMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClothTypesResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListClothTypesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListClothTypesResponseBodyData] = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
                temp_model = ListClothTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClothTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClothTypesResponseBody = None,
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
            temp_model = ListClothTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClothesRequest(TeaModel):
    def __init__(
        self,
        categories: List[int] = None,
        cloth_size: str = None,
        current: int = None,
        jwt_token: str = None,
        name: str = None,
        size: int = None,
        type: str = None,
    ):
        self.categories = categories
        self.cloth_size = cloth_size
        self.current = current
        self.jwt_token = jwt_token
        self.name = name
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.cloth_size is not None:
            result['ClothSize'] = self.cloth_size
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('ClothSize') is not None:
            self.cloth_size = m.get('ClothSize')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListClothesShrinkRequest(TeaModel):
    def __init__(
        self,
        categories_shrink: str = None,
        cloth_size: str = None,
        current: int = None,
        jwt_token: str = None,
        name: str = None,
        size: int = None,
        type: str = None,
    ):
        self.categories_shrink = categories_shrink
        self.cloth_size = cloth_size
        self.current = current
        self.jwt_token = jwt_token
        self.name = name
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories_shrink is not None:
            result['Categories'] = self.categories_shrink
        if self.cloth_size is not None:
            result['ClothSize'] = self.cloth_size
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories_shrink = m.get('Categories')
        if m.get('ClothSize') is not None:
            self.cloth_size = m.get('ClothSize')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListClothesResponseBodyData(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        create_time: str = None,
        id: str = None,
        modified_time: str = None,
        name: str = None,
        oss_key: str = None,
        part: str = None,
        size: str = None,
        status: Dict[str, str] = None,
        type: str = None,
    ):
        self.cover_url = cover_url
        self.create_time = create_time
        self.id = id
        self.modified_time = modified_time
        self.name = name
        self.oss_key = oss_key
        self.part = part
        self.size = size
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.part is not None:
            result['Part'] = self.part
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Part') is not None:
            self.part = m.get('Part')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListClothesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[ListClothesResponseBodyData] = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        pages: int = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
        self.message = message
        self.pages = pages
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

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
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClothesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListClothesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClothesResponseBody = None,
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
            temp_model = ListClothesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHdrResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
    ):
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListHdrResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListHdrResponseBodyData] = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
                temp_model = ListHdrResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHdrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHdrResponseBody = None,
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
            temp_model = ListHdrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLocationPaiImageRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        jwt_token: str = None,
        size: int = None,
        sort: str = None,
        sort_field: str = None,
    ):
        self.current = current
        self.jwt_token = jwt_token
        self.size = size
        self.sort = sort
        self.sort_field = sort_field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        return self


class ListLocationPaiImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: Dict[str, Any] = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        pages: int = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
        self.message = message
        self.pages = pages
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        if self.data is not None:
            result['Data'] = self.data
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListLocationPaiImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLocationPaiImageResponseBody = None,
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
            temp_model = ListLocationPaiImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLocationServiceRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        jwt_token: str = None,
        size: int = None,
        sort: str = None,
        sort_field: str = None,
    ):
        self.current = current
        self.jwt_token = jwt_token
        self.size = size
        self.sort = sort
        self.sort_field = sort_field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        return self


class ListLocationServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        expire_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        note: str = None,
        qps: int = None,
        start_time: str = None,
        status: str = None,
        svc_state: str = None,
    ):
        self.app_id = app_id
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.note = note
        self.qps = qps
        self.start_time = start_time
        self.status = status
        self.svc_state = svc_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.note is not None:
            result['Note'] = self.note
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.svc_state is not None:
            result['SvcState'] = self.svc_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SvcState') is not None:
            self.svc_state = m.get('SvcState')
        return self


class ListLocationServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[ListLocationServiceResponseBodyData] = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        pages: int = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
        self.message = message
        self.pages = pages
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

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
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListLocationServiceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListLocationServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLocationServiceResponseBody = None,
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
            temp_model = ListLocationServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRequest(TeaModel):
    def __init__(
        self,
        biz_usage: str = None,
        current: int = None,
        jwt_token: str = None,
        size: int = None,
        sort_field: str = None,
        status: str = None,
        title: str = None,
        type: str = None,
        with_source: bool = None,
        with_user: bool = None,
    ):
        self.biz_usage = biz_usage
        self.current = current
        self.jwt_token = jwt_token
        self.size = size
        self.sort_field = sort_field
        self.status = status
        self.title = title
        self.type = type
        self.with_source = with_source
        self.with_user = with_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.with_source is not None:
            result['WithSource'] = self.with_source
        if self.with_user is not None:
            result['WithUser'] = self.with_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WithSource') is not None:
            self.with_source = m.get('WithSource')
        if m.get('WithUser') is not None:
            self.with_user = m.get('WithUser')
        return self


class ListProjectResponseBodyDataDataset(TeaModel):
    def __init__(
        self,
        build_result_url: Dict[str, Any] = None,
        cover_url: str = None,
        glb_model_url: str = None,
        model_url: str = None,
        origin_result_url: str = None,
        oss_key: str = None,
        pose_url: str = None,
        preview_url: str = None,
    ):
        self.build_result_url = build_result_url
        self.cover_url = cover_url
        self.glb_model_url = glb_model_url
        self.model_url = model_url
        self.origin_result_url = origin_result_url
        self.oss_key = oss_key
        self.pose_url = pose_url
        self.preview_url = preview_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class ListProjectResponseBodyDataSourceClothes(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        name: str = None,
        oss_key: str = None,
        type: str = None,
    ):
        self.cover_url = cover_url
        self.name = name
        self.oss_key = oss_key
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListProjectResponseBodyDataSourceFiles(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        file_name: str = None,
        id: str = None,
        size: int = None,
        type: str = None,
        url: str = None,
    ):
        self.cover_url = cover_url
        self.file_name = file_name
        self.id = id
        self.size = size
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListProjectResponseBodyDataSource(TeaModel):
    def __init__(
        self,
        clothes: List[ListProjectResponseBodyDataSourceClothes] = None,
        files: List[ListProjectResponseBodyDataSourceFiles] = None,
        oss_key: str = None,
    ):
        self.clothes = clothes
        self.files = files
        self.oss_key = oss_key

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clothes'] = []
        if self.clothes is not None:
            for k in self.clothes:
                result['Clothes'].append(k.to_map() if k else None)
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = ListProjectResponseBodyDataSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = ListProjectResponseBodyDataSourceFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class ListProjectResponseBodyDataUser(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        create_time: str = None,
        modified_time: str = None,
        nickname: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.create_time = create_time
        self.modified_time = modified_time
        self.nickname = nickname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.nickname is not None:
            result['Nickname'] = self.nickname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')
        return self


class ListProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_usage: str = None,
        create_time: str = None,
        dataset: ListProjectResponseBodyDataDataset = None,
        ext: str = None,
        ext_info: Dict[str, Any] = None,
        id: str = None,
        intro: str = None,
        modified_time: str = None,
        source: ListProjectResponseBodyDataSource = None,
        status: str = None,
        title: str = None,
        type: str = None,
        user: ListProjectResponseBodyDataUser = None,
    ):
        self.biz_usage = biz_usage
        self.create_time = create_time
        self.dataset = dataset
        self.ext = ext
        self.ext_info = ext_info
        self.id = id
        self.intro = intro
        self.modified_time = modified_time
        self.source = source
        self.status = status
        self.title = title
        self.type = type
        self.user = user

    def validate(self):
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = ListProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = ListProjectResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('User') is not None:
            temp_model = ListProjectResponseBodyDataUser()
            self.user = temp_model.from_map(m['User'])
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[ListProjectResponseBodyData] = None,
        message: str = None,
        pages: int = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.message = message
        self.pages = pages
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

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
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectResponseBody = None,
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
            temp_model = ListProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsByDependencyIdRequest(TeaModel):
    def __init__(
        self,
        dependency_project_id: int = None,
        jwt_token: str = None,
        map_uuid: str = None,
        with_dataset: bool = None,
        with_source: bool = None,
    ):
        self.dependency_project_id = dependency_project_id
        self.jwt_token = jwt_token
        self.map_uuid = map_uuid
        self.with_dataset = with_dataset
        self.with_source = with_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dependency_project_id is not None:
            result['DependencyProjectId'] = self.dependency_project_id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.map_uuid is not None:
            result['MapUuid'] = self.map_uuid
        if self.with_dataset is not None:
            result['WithDataset'] = self.with_dataset
        if self.with_source is not None:
            result['WithSource'] = self.with_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependencyProjectId') is not None:
            self.dependency_project_id = m.get('DependencyProjectId')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('MapUuid') is not None:
            self.map_uuid = m.get('MapUuid')
        if m.get('WithDataset') is not None:
            self.with_dataset = m.get('WithDataset')
        if m.get('WithSource') is not None:
            self.with_source = m.get('WithSource')
        return self


class ListProjectsByDependencyIdResponseBodyDataBuildDetail(TeaModel):
    def __init__(
        self,
        completed_time: str = None,
        error_message: str = None,
        estimated_duration: int = None,
        running_time: str = None,
        submit_time: str = None,
    ):
        self.completed_time = completed_time
        self.error_message = error_message
        self.estimated_duration = estimated_duration
        self.running_time = running_time
        self.submit_time = submit_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class ListProjectsByDependencyIdResponseBodyDataDataset(TeaModel):
    def __init__(
        self,
        build_result_url: Dict[str, Any] = None,
        cover_url: str = None,
        glb_model_url: str = None,
        model_url: str = None,
        origin_result_url: str = None,
        oss_key: str = None,
        pose_url: str = None,
        preview_url: str = None,
    ):
        self.build_result_url = build_result_url
        self.cover_url = cover_url
        self.glb_model_url = glb_model_url
        self.model_url = model_url
        self.origin_result_url = origin_result_url
        self.oss_key = oss_key
        self.pose_url = pose_url
        self.preview_url = preview_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class ListProjectsByDependencyIdResponseBodyDataSourceSourceFiles(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        file_name: str = None,
        id: str = None,
        size: int = None,
        type: str = None,
        url: str = None,
    ):
        self.cover_url = cover_url
        self.file_name = file_name
        self.id = id
        self.size = size
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListProjectsByDependencyIdResponseBodyDataSource(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        modified_time: str = None,
        oss_key: str = None,
        project_id: int = None,
        source_files: List[ListProjectsByDependencyIdResponseBodyDataSourceSourceFiles] = None,
    ):
        self.create_time = create_time
        self.id = id
        self.modified_time = modified_time
        self.oss_key = oss_key
        self.project_id = project_id
        self.source_files = source_files

    def validate(self):
        if self.source_files:
            for k in self.source_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = ListProjectsByDependencyIdResponseBodyDataSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        return self


class ListProjectsByDependencyIdResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_usage: str = None,
        build_detail: ListProjectsByDependencyIdResponseBodyDataBuildDetail = None,
        create_time: str = None,
        dataset: ListProjectsByDependencyIdResponseBodyDataDataset = None,
        ext: str = None,
        id: str = None,
        intro: str = None,
        modified_time: str = None,
        source: ListProjectsByDependencyIdResponseBodyDataSource = None,
        status: str = None,
        title: str = None,
        type: str = None,
    ):
        self.biz_usage = biz_usage
        self.build_detail = build_detail
        self.create_time = create_time
        self.dataset = dataset
        self.ext = ext
        self.id = id
        self.intro = intro
        self.modified_time = modified_time
        self.source = source
        self.status = status
        self.title = title
        self.type = type

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = ListProjectsByDependencyIdResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = ListProjectsByDependencyIdResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = ListProjectsByDependencyIdResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListProjectsByDependencyIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListProjectsByDependencyIdResponseBodyData] = None,
        error_name: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
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
                temp_model = ListProjectsByDependencyIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProjectsByDependencyIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectsByDependencyIdResponseBody = None,
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
            temp_model = ListProjectsByDependencyIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSourceFileRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        project_id: str = None,
    ):
        self.jwt_token = jwt_token
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListSourceFileResponseBodyDataPicList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        file_name: str = None,
        id: str = None,
        modified_time: str = None,
        oss_key: str = None,
        type: str = None,
        url: str = None,
    ):
        self.create_time = create_time
        self.file_name = file_name
        self.id = id
        self.modified_time = modified_time
        self.oss_key = oss_key
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListSourceFileResponseBodyDataVideoList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        file_name: str = None,
        id: str = None,
        modified_time: str = None,
        oss_key: str = None,
        type: str = None,
        url: str = None,
    ):
        self.create_time = create_time
        self.file_name = file_name
        self.id = id
        self.modified_time = modified_time
        self.oss_key = oss_key
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListSourceFileResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_list: List[ListSourceFileResponseBodyDataPicList] = None,
        video_list: List[ListSourceFileResponseBodyDataVideoList] = None,
    ):
        self.pic_list = pic_list
        self.video_list = video_list

    def validate(self):
        if self.pic_list:
            for k in self.pic_list:
                if k:
                    k.validate()
        if self.video_list:
            for k in self.video_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PicList'] = []
        if self.pic_list is not None:
            for k in self.pic_list:
                result['PicList'].append(k.to_map() if k else None)
        result['VideoList'] = []
        if self.video_list is not None:
            for k in self.video_list:
                result['VideoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pic_list = []
        if m.get('PicList') is not None:
            for k in m.get('PicList'):
                temp_model = ListSourceFileResponseBodyDataPicList()
                self.pic_list.append(temp_model.from_map(k))
        self.video_list = []
        if m.get('VideoList') is not None:
            for k in m.get('VideoList'):
                temp_model = ListSourceFileResponseBodyDataVideoList()
                self.video_list.append(temp_model.from_map(k))
        return self


class ListSourceFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListSourceFileResponseBodyData = None,
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
            temp_model = ListSourceFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSourceFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSourceFileResponseBody = None,
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
            temp_model = ListSourceFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkflowResponseBodyDataHumanPose(TeaModel):
    def __init__(
        self,
        biz_usage: str = None,
        id: int = None,
        name: str = None,
        object_type: str = None,
        status: int = None,
    ):
        self.biz_usage = biz_usage
        self.id = id
        self.name = name
        self.object_type = object_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListWorkflowResponseBodyDataMannequins(TeaModel):
    def __init__(
        self,
        biz_usage: str = None,
        id: int = None,
        name: str = None,
        object_type: str = None,
        status: int = None,
    ):
        self.biz_usage = biz_usage
        self.id = id
        self.name = name
        self.object_type = object_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListWorkflowResponseBodyDataObject(TeaModel):
    def __init__(
        self,
        biz_usage: str = None,
        id: int = None,
        name: str = None,
        object_type: str = None,
        status: int = None,
    ):
        self.biz_usage = biz_usage
        self.id = id
        self.name = name
        self.object_type = object_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListWorkflowResponseBodyDataScene(TeaModel):
    def __init__(
        self,
        biz_usage: str = None,
        id: int = None,
        name: str = None,
        object_type: str = None,
        status: int = None,
    ):
        self.biz_usage = biz_usage
        self.id = id
        self.name = name
        self.object_type = object_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListWorkflowResponseBodyData(TeaModel):
    def __init__(
        self,
        human_pose: List[ListWorkflowResponseBodyDataHumanPose] = None,
        mannequins: List[ListWorkflowResponseBodyDataMannequins] = None,
        object: List[ListWorkflowResponseBodyDataObject] = None,
        scene: List[ListWorkflowResponseBodyDataScene] = None,
    ):
        self.human_pose = human_pose
        self.mannequins = mannequins
        self.object = object
        self.scene = scene

    def validate(self):
        if self.human_pose:
            for k in self.human_pose:
                if k:
                    k.validate()
        if self.mannequins:
            for k in self.mannequins:
                if k:
                    k.validate()
        if self.object:
            for k in self.object:
                if k:
                    k.validate()
        if self.scene:
            for k in self.scene:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HumanPose'] = []
        if self.human_pose is not None:
            for k in self.human_pose:
                result['HumanPose'].append(k.to_map() if k else None)
        result['Mannequins'] = []
        if self.mannequins is not None:
            for k in self.mannequins:
                result['Mannequins'].append(k.to_map() if k else None)
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        result['Scene'] = []
        if self.scene is not None:
            for k in self.scene:
                result['Scene'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.human_pose = []
        if m.get('HumanPose') is not None:
            for k in m.get('HumanPose'):
                temp_model = ListWorkflowResponseBodyDataHumanPose()
                self.human_pose.append(temp_model.from_map(k))
        self.mannequins = []
        if m.get('Mannequins') is not None:
            for k in m.get('Mannequins'):
                temp_model = ListWorkflowResponseBodyDataMannequins()
                self.mannequins.append(temp_model.from_map(k))
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListWorkflowResponseBodyDataObject()
                self.object.append(temp_model.from_map(k))
        self.scene = []
        if m.get('Scene') is not None:
            for k in m.get('Scene'):
                temp_model = ListWorkflowResponseBodyDataScene()
                self.scene.append(temp_model.from_map(k))
        return self


class ListWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        data: ListWorkflowResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.http_code = http_code
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListWorkflowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkflowResponseBody = None,
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
            temp_model = ListWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoginRequest(TeaModel):
    def __init__(
        self,
        emp_id: str = None,
        emp_name: str = None,
        token: str = None,
        type: str = None,
    ):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.token = token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emp_id is not None:
            result['EmpId'] = self.emp_id
        if self.emp_name is not None:
            result['EmpName'] = self.emp_name
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmpId') is not None:
            self.emp_id = m.get('EmpId')
        if m.get('EmpName') is not None:
            self.emp_name = m.get('EmpName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class LoginResponseBodyData(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        nickname: str = None,
        uid: str = None,
    ):
        self.jwt_token = jwt_token
        self.nickname = nickname
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.nickname is not None:
            result['Nickname'] = self.nickname
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class LoginResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: LoginResponseBodyData = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = LoginResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LoginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LoginResponseBody = None,
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
            temp_model = LoginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishArEditProjectRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        map_id: int = None,
    ):
        self.jwt_token = jwt_token
        self.map_id = map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.map_id is not None:
            result['MapId'] = self.map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('MapId') is not None:
            self.map_id = m.get('MapId')
        return self


class PublishArEditProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PublishArEditProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishArEditProjectResponseBody = None,
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
            temp_model = PublishArEditProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAreaMapRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        jwt_token: str = None,
    ):
        self.id = id
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class QueryAreaMapResponseBodyData(TeaModel):
    def __init__(
        self,
        d_3oss: str = None,
        ext_info: str = None,
        id: int = None,
        location_oss: str = None,
        map_type: str = None,
        name: str = None,
        note: str = None,
        status: str = None,
    ):
        self.d_3oss = d_3oss
        self.ext_info = ext_info
        self.id = id
        self.location_oss = location_oss
        self.map_type = map_type
        self.name = name
        self.note = note
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.d_3oss is not None:
            result['D3Oss'] = self.d_3oss
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.id is not None:
            result['Id'] = self.id
        if self.location_oss is not None:
            result['LocationOss'] = self.location_oss
        if self.map_type is not None:
            result['MapType'] = self.map_type
        if self.name is not None:
            result['Name'] = self.name
        if self.note is not None:
            result['Note'] = self.note
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('D3Oss') is not None:
            self.d_3oss = m.get('D3Oss')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LocationOss') is not None:
            self.location_oss = m.get('LocationOss')
        if m.get('MapType') is not None:
            self.map_type = m.get('MapType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryAreaMapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryAreaMapResponseBodyData = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = QueryAreaMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAreaMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAreaMapResponseBody = None,
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
            temp_model = QueryAreaMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBuildBreakpointRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        project_id: str = None,
    ):
        self.jwt_token = jwt_token
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryBuildBreakpointResponseBodyDataBreakpoints(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        job_id: str = None,
    ):
        self.algorithm = algorithm
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class QueryBuildBreakpointResponseBodyData(TeaModel):
    def __init__(
        self,
        breakpoints: List[QueryBuildBreakpointResponseBodyDataBreakpoints] = None,
        project_id: str = None,
    ):
        self.breakpoints = breakpoints
        self.project_id = project_id

    def validate(self):
        if self.breakpoints:
            for k in self.breakpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Breakpoints'] = []
        if self.breakpoints is not None:
            for k in self.breakpoints:
                result['Breakpoints'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.breakpoints = []
        if m.get('Breakpoints') is not None:
            for k in m.get('Breakpoints'):
                temp_model = QueryBuildBreakpointResponseBodyDataBreakpoints()
                self.breakpoints.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryBuildBreakpointResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryBuildBreakpointResponseBodyData = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = QueryBuildBreakpointResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBuildBreakpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBuildBreakpointResponseBody = None,
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
            temp_model = QueryBuildBreakpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLocationServiceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        jwt_token: str = None,
    ):
        self.id = id
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class QueryLocationServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        expire_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        image_id: int = None,
        image_name: str = None,
        name: str = None,
        note: str = None,
        qps: int = None,
        start_time: str = None,
        svc_deploy_status: str = None,
        svc_state: str = None,
        tree_config: str = None,
        uuid_log_map: str = None,
    ):
        self.app_id = app_id
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.image_id = image_id
        self.image_name = image_name
        self.name = name
        self.note = note
        self.qps = qps
        self.start_time = start_time
        self.svc_deploy_status = svc_deploy_status
        self.svc_state = svc_state
        self.tree_config = tree_config
        self.uuid_log_map = uuid_log_map

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.name is not None:
            result['Name'] = self.name
        if self.note is not None:
            result['Note'] = self.note
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.svc_deploy_status is not None:
            result['SvcDeployStatus'] = self.svc_deploy_status
        if self.svc_state is not None:
            result['SvcState'] = self.svc_state
        if self.tree_config is not None:
            result['TreeConfig'] = self.tree_config
        if self.uuid_log_map is not None:
            result['UuidLogMap'] = self.uuid_log_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SvcDeployStatus') is not None:
            self.svc_deploy_status = m.get('SvcDeployStatus')
        if m.get('SvcState') is not None:
            self.svc_state = m.get('SvcState')
        if m.get('TreeConfig') is not None:
            self.tree_config = m.get('TreeConfig')
        if m.get('UuidLogMap') is not None:
            self.uuid_log_map = m.get('UuidLogMap')
        return self


class QueryLocationServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryLocationServiceResponseBodyData = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = QueryLocationServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryLocationServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryLocationServiceResponseBody = None,
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
            temp_model = QueryLocationServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectBuildDetailRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryProjectBuildDetailResponseBodyDataInstanceDetailResponseList(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        params: str = None,
        status: str = None,
        submit_time: str = None,
        template_id: int = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.params = params
        self.status = status
        self.submit_time = submit_time
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.params is not None:
            result['Params'] = self.params
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryProjectBuildDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_detail_response_list: List[QueryProjectBuildDetailResponseBodyDataInstanceDetailResponseList] = None,
        status: str = None,
        title: str = None,
        user_id: int = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_detail_response_list = instance_detail_response_list
        self.status = status
        self.title = title
        self.user_id = user_id

    def validate(self):
        if self.instance_detail_response_list:
            for k in self.instance_detail_response_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        result['InstanceDetailResponseList'] = []
        if self.instance_detail_response_list is not None:
            for k in self.instance_detail_response_list:
                result['InstanceDetailResponseList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.instance_detail_response_list = []
        if m.get('InstanceDetailResponseList') is not None:
            for k in m.get('InstanceDetailResponseList'):
                temp_model = QueryProjectBuildDetailResponseBodyDataInstanceDetailResponseList()
                self.instance_detail_response_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryProjectBuildDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryProjectBuildDetailResponseBodyData = None,
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
            temp_model = QueryProjectBuildDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryProjectBuildDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryProjectBuildDetailResponseBody = None,
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
            temp_model = QueryProjectBuildDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectDetailRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        project_id: str = None,
    ):
        self.jwt_token = jwt_token
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryProjectDetailResponseBodyDataBuildDetail(TeaModel):
    def __init__(
        self,
        completed_time: str = None,
        error_message: str = None,
        estimated_duration: int = None,
        running_time: str = None,
        submit_time: str = None,
    ):
        self.completed_time = completed_time
        self.error_message = error_message
        self.estimated_duration = estimated_duration
        self.running_time = running_time
        self.submit_time = submit_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class QueryProjectDetailResponseBodyDataDatasetPolicy(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.dir = dir
        self.expire = expire
        self.host = host
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class QueryProjectDetailResponseBodyDataDataset(TeaModel):
    def __init__(
        self,
        build_result_url: Dict[str, Any] = None,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        glb_model_url: str = None,
        id: str = None,
        model_url: str = None,
        modified_time: str = None,
        origin_result_url: str = None,
        oss_key: str = None,
        policy: QueryProjectDetailResponseBodyDataDatasetPolicy = None,
        pose_url: str = None,
        preview_url: str = None,
    ):
        self.build_result_url = build_result_url
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.glb_model_url = glb_model_url
        self.id = id
        self.model_url = model_url
        self.modified_time = modified_time
        self.origin_result_url = origin_result_url
        self.oss_key = oss_key
        self.policy = policy
        self.pose_url = pose_url
        self.preview_url = preview_url

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.id is not None:
            result['Id'] = self.id
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = QueryProjectDetailResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class QueryProjectDetailResponseBodyDataSourceClothes(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        id: str = None,
        name: str = None,
        oss_key: str = None,
        type: str = None,
    ):
        self.cover_url = cover_url
        self.id = id
        self.name = name
        self.oss_key = oss_key
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryProjectDetailResponseBodyDataSourceFiles(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        file_name: str = None,
        id: str = None,
        size: int = None,
        type: str = None,
        url: str = None,
    ):
        self.cover_url = cover_url
        self.file_name = file_name
        self.id = id
        self.size = size
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryProjectDetailResponseBodyDataSourcePolicy(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.dir = dir
        self.expire = expire
        self.host = host
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class QueryProjectDetailResponseBodyDataSource(TeaModel):
    def __init__(
        self,
        clothes: List[QueryProjectDetailResponseBodyDataSourceClothes] = None,
        create_time: str = None,
        deleted: bool = None,
        files: List[QueryProjectDetailResponseBodyDataSourceFiles] = None,
        id: str = None,
        modified_time: str = None,
        oss_key: str = None,
        policy: QueryProjectDetailResponseBodyDataSourcePolicy = None,
    ):
        self.clothes = clothes
        self.create_time = create_time
        self.deleted = deleted
        self.files = files
        self.id = id
        self.modified_time = modified_time
        self.oss_key = oss_key
        self.policy = policy

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clothes'] = []
        if self.clothes is not None:
            for k in self.clothes:
                result['Clothes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = QueryProjectDetailResponseBodyDataSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = QueryProjectDetailResponseBodyDataSourceFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = QueryProjectDetailResponseBodyDataSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        return self


class QueryProjectDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_usage: str = None,
        build_detail: QueryProjectDetailResponseBodyDataBuildDetail = None,
        create_mode: str = None,
        create_time: str = None,
        dataset: QueryProjectDetailResponseBodyDataDataset = None,
        deleted: bool = None,
        dependencies: str = None,
        id: str = None,
        intro: str = None,
        modified_time: str = None,
        source: QueryProjectDetailResponseBodyDataSource = None,
        status: str = None,
        title: str = None,
        type: str = None,
    ):
        self.biz_usage = biz_usage
        self.build_detail = build_detail
        self.create_mode = create_mode
        self.create_time = create_time
        self.dataset = dataset
        self.deleted = deleted
        self.dependencies = dependencies
        self.id = id
        self.intro = intro
        self.modified_time = modified_time
        self.source = source
        self.status = status
        self.title = title
        self.type = type

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = QueryProjectDetailResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = QueryProjectDetailResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = QueryProjectDetailResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryProjectDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryProjectDetailResponseBodyData = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = QueryProjectDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryProjectDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryProjectDetailResponseBody = None,
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
            temp_model = QueryProjectDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeProductRegionsRequest(TeaModel):
    def __init__(
        self,
        category: int = None,
        image_base_64: str = None,
    ):
        self.category = category
        self.image_base_64 = image_base_64

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.image_base_64 is not None:
            result['ImageBase64'] = self.image_base_64
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ImageBase64') is not None:
            self.image_base_64 = m.get('ImageBase64')
        return self


class RecognizeProductRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        result_code: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.result_code = result_code
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
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
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
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecognizeProductRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeProductRegionsResponseBody = None,
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
            temp_model = RecognizeProductRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RegisterUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterUserResponseBody = None,
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
            temp_model = RegisterUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeLocationServiceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        jwt_token: str = None,
    ):
        self.id = id
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class ResumeLocationServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeLocationServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeLocationServiceResponseBody = None,
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
            temp_model = ResumeLocationServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveArEditProjectRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        map_id: int = None,
    ):
        self.jwt_token = jwt_token
        self.map_id = map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.map_id is not None:
            result['MapId'] = self.map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('MapId') is not None:
            self.map_id = m.get('MapId')
        return self


class SaveArEditProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveArEditProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveArEditProjectResponseBody = None,
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
            temp_model = SaveArEditProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSourceRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        project_id: int = None,
    ):
        self.jwt_token = jwt_token
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class SaveSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSourceResponseBody = None,
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
            temp_model = SaveSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchProductsByImageRequestRegion(TeaModel):
    def __init__(
        self,
        height: int = None,
        start_x: int = None,
        start_y: int = None,
        width: int = None,
    ):
        self.height = height
        self.start_x = start_x
        self.start_y = start_y
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.start_x is not None:
            result['StartX'] = self.start_x
        if self.start_y is not None:
            result['StartY'] = self.start_y
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('StartX') is not None:
            self.start_x = m.get('StartX')
        if m.get('StartY') is not None:
            self.start_y = m.get('StartY')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class SearchProductsByImageRequest(TeaModel):
    def __init__(
        self,
        category: int = None,
        image_base_64: str = None,
        region: SearchProductsByImageRequestRegion = None,
    ):
        self.category = category
        self.image_base_64 = image_base_64
        self.region = region

    def validate(self):
        if self.region:
            self.region.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.image_base_64 is not None:
            result['ImageBase64'] = self.image_base_64
        if self.region is not None:
            result['Region'] = self.region.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ImageBase64') is not None:
            self.image_base_64 = m.get('ImageBase64')
        if m.get('Region') is not None:
            temp_model = SearchProductsByImageRequestRegion()
            self.region = temp_model.from_map(m['Region'])
        return self


class SearchProductsByImageShrinkRequest(TeaModel):
    def __init__(
        self,
        category: int = None,
        image_base_64: str = None,
        region_shrink: str = None,
    ):
        self.category = category
        self.image_base_64 = image_base_64
        self.region_shrink = region_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.image_base_64 is not None:
            result['ImageBase64'] = self.image_base_64
        if self.region_shrink is not None:
            result['Region'] = self.region_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ImageBase64') is not None:
            self.image_base_64 = m.get('ImageBase64')
        if m.get('Region') is not None:
            self.region_shrink = m.get('Region')
        return self


class SearchProductsByImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        result_code: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.result_code = result_code
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
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
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
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchProductsByImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchProductsByImageResponseBody = None,
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
            temp_model = SearchProductsByImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendLocationServiceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        jwt_token: str = None,
    ):
        self.id = id
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class SuspendLocationServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendLocationServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SuspendLocationServiceResponseBody = None,
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
            temp_model = SuspendLocationServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLocationServiceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        jwt_token: str = None,
        note: str = None,
        qps: int = None,
        svc_name: str = None,
        svc_state: str = None,
    ):
        self.id = id
        self.jwt_token = jwt_token
        self.note = note
        self.qps = qps
        self.svc_name = svc_name
        self.svc_state = svc_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.note is not None:
            result['Note'] = self.note
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.svc_name is not None:
            result['SvcName'] = self.svc_name
        if self.svc_state is not None:
            result['SvcState'] = self.svc_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('SvcName') is not None:
            self.svc_name = m.get('SvcName')
        if m.get('SvcState') is not None:
            self.svc_state = m.get('SvcState')
        return self


class UpdateLocationServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateLocationServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLocationServiceResponseBody = None,
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
            temp_model = UpdateLocationServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLocationTreeRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        jwt_token: str = None,
        tree_config: str = None,
    ):
        self.id = id
        self.jwt_token = jwt_token
        self.tree_config = tree_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.tree_config is not None:
            result['TreeConfig'] = self.tree_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('TreeConfig') is not None:
            self.tree_config = m.get('TreeConfig')
        return self


class UpdateLocationTreeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateLocationTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLocationTreeResponseBody = None,
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
            temp_model = UpdateLocationTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        auto_build: bool = None,
        ext: Dict[str, Any] = None,
        intro: str = None,
        jwt_token: str = None,
        project_id: str = None,
        title: str = None,
    ):
        self.auto_build = auto_build
        self.ext = ext
        self.intro = intro
        self.jwt_token = jwt_token
        self.project_id = project_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_build: bool = None,
        ext_shrink: str = None,
        intro: str = None,
        jwt_token: str = None,
        project_id: str = None,
        title: str = None,
    ):
        self.auto_build = auto_build
        self.ext_shrink = ext_shrink
        self.intro = intro
        self.jwt_token = jwt_token
        self.project_id = project_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.ext_shrink is not None:
            result['Ext'] = self.ext_shrink
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('Ext') is not None:
            self.ext_shrink = m.get('Ext')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_name: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_name = error_name
        self.http_code = http_code
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
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectResponseBody = None,
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



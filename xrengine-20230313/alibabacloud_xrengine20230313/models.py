# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class GetMapDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        jwt_token: str = None,
    ):
        self.app_id = app_id
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class GetMapDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[Dict[str, Any]] = None,
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


class GetMapDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMapDataResponseBody = None,
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
            temp_model = GetMapDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMapPublishDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        jwt_token: str = None,
    ):
        self.app_id = app_id
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class GetMapPublishDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[Dict[str, Any]] = None,
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


class GetMapPublishDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMapPublishDataResponseBody = None,
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
            temp_model = GetMapPublishDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitLocateRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        params: str = None,
    ):
        self.jwt_token = jwt_token
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class InitLocateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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


class InitLocateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitLocateResponseBody = None,
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
            temp_model = InitLocateResponseBody()
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


class LocateRequest(TeaModel):
    def __init__(
        self,
        image: str = None,
        jwt_token: str = None,
        params: str = None,
    ):
        self.image = image
        self.jwt_token = jwt_token
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class LocateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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


class LocateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LocateResponseBody = None,
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
            temp_model = LocateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBatchQueryObjectProjectStatusRequest(TeaModel):
    def __init__(
        self,
        project_ids: str = None,
    ):
        self.project_ids = project_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class PopBatchQueryObjectProjectStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        id: str = None,
        status: str = None,
    ):
        self.check_status = check_status
        self.id = id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PopBatchQueryObjectProjectStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[PopBatchQueryObjectProjectStatusResponseBodyData] = None,
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
                temp_model = PopBatchQueryObjectProjectStatusResponseBodyData()
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


class PopBatchQueryObjectProjectStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PopBatchQueryObjectProjectStatusResponseBody = None,
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
            temp_model = PopBatchQueryObjectProjectStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBuildFeatureToAvatarProjectRequest(TeaModel):
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


class PopBuildFeatureToAvatarProjectResponseBody(TeaModel):
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


class PopBuildFeatureToAvatarProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PopBuildFeatureToAvatarProjectResponseBody = None,
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
            temp_model = PopBuildFeatureToAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBuildObjectProjectRequest(TeaModel):
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


class PopBuildObjectProjectResponseBody(TeaModel):
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


class PopBuildObjectProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PopBuildObjectProjectResponseBody = None,
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
            temp_model = PopBuildObjectProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopCreateFeatureToAvatarProjectRequest(TeaModel):
    def __init__(
        self,
        ext_info: str = None,
        intro: str = None,
        title: str = None,
    ):
        self.ext_info = ext_info
        self.intro = intro
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopCreateFeatureToAvatarProjectResponseBodyDataBuildDetail(TeaModel):
    def __init__(
        self,
        completed_time: str = None,
        create_time: str = None,
        deleted: bool = None,
        error_message: str = None,
        estimated_duration: int = None,
        id: int = None,
        modified_time: str = None,
        running_time: str = None,
        status: str = None,
        submit_time: str = None,
    ):
        self.completed_time = completed_time
        self.create_time = create_time
        self.deleted = deleted
        self.error_message = error_message
        self.estimated_duration = estimated_duration
        self.id = id
        self.modified_time = modified_time
        self.running_time = running_time
        self.status = status
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopCreateFeatureToAvatarProjectResponseBodyDataDatasetPolicy(TeaModel):
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


class PopCreateFeatureToAvatarProjectResponseBodyDataDataset(TeaModel):
    def __init__(
        self,
        build_result_url: Dict[str, Any] = None,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        error_code: str = None,
        error_message: str = None,
        glb_model_url: str = None,
        id: int = None,
        model_url: str = None,
        modified_time: str = None,
        origin_result_url: str = None,
        oss_key: str = None,
        policy: PopCreateFeatureToAvatarProjectResponseBodyDataDatasetPolicy = None,
        pose_url: str = None,
        preview_url: str = None,
    ):
        self.build_result_url = build_result_url
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.error_code = error_code
        self.error_message = error_message
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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
            temp_model = PopCreateFeatureToAvatarProjectResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopCreateFeatureToAvatarProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_usage: str = None,
        build_detail: PopCreateFeatureToAvatarProjectResponseBodyDataBuildDetail = None,
        check_status: str = None,
        create_mode: str = None,
        create_time: str = None,
        dataset: PopCreateFeatureToAvatarProjectResponseBodyDataDataset = None,
        deleted: bool = None,
        ext: str = None,
        id: str = None,
        intro: str = None,
        material_cover_url: str = None,
        modified_time: str = None,
        status: str = None,
        title: str = None,
        type: str = None,
    ):
        self.biz_usage = biz_usage
        self.build_detail = build_detail
        self.check_status = check_status
        self.create_mode = create_mode
        self.create_time = create_time
        self.dataset = dataset
        self.deleted = deleted
        self.ext = ext
        self.id = id
        self.intro = intro
        self.material_cover_url = material_cover_url
        self.modified_time = modified_time
        self.status = status
        self.title = title
        self.type = type

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
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
            temp_model = PopCreateFeatureToAvatarProjectResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopCreateFeatureToAvatarProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopCreateFeatureToAvatarProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PopCreateFeatureToAvatarProjectResponseBodyData = None,
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
            temp_model = PopCreateFeatureToAvatarProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopCreateFeatureToAvatarProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PopCreateFeatureToAvatarProjectResponseBody = None,
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
            temp_model = PopCreateFeatureToAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopCreateObjectProjectRequest(TeaModel):
    def __init__(
        self,
        auto_build: bool = None,
        biz_usage: str = None,
        dependencies: str = None,
        intro: str = None,
        mode: str = None,
        title: str = None,
    ):
        self.auto_build = auto_build
        self.biz_usage = biz_usage
        self.dependencies = dependencies
        self.intro = intro
        self.mode = mode
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
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopCreateObjectProjectResponseBodyDataBuildDetail(TeaModel):
    def __init__(
        self,
        completed_time: str = None,
        create_time: str = None,
        deleted: bool = None,
        error_message: str = None,
        estimated_duration: int = None,
        modified_time: str = None,
        running_time: str = None,
        submit_time: str = None,
    ):
        self.completed_time = completed_time
        self.create_time = create_time
        self.deleted = deleted
        self.error_message = error_message
        self.estimated_duration = estimated_duration
        self.modified_time = modified_time
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopCreateObjectProjectResponseBodyDataDatasetPolicy(TeaModel):
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


class PopCreateObjectProjectResponseBodyDataDataset(TeaModel):
    def __init__(
        self,
        build_result_url: Dict[str, Any] = None,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        error_message: str = None,
        glb_model_url: str = None,
        model_url: str = None,
        modified_time: str = None,
        origin_result_url: str = None,
        oss_key: str = None,
        policy: PopCreateObjectProjectResponseBodyDataDatasetPolicy = None,
        pose_url: str = None,
        preview_url: str = None,
    ):
        self.build_result_url = build_result_url
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.error_message = error_message
        self.glb_model_url = glb_model_url
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopCreateObjectProjectResponseBodyDataSourceClothes(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        modified_time: str = None,
        name: str = None,
        oss_key: str = None,
        type: str = None,
    ):
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.modified_time = modified_time
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopCreateObjectProjectResponseBodyDataSourcePolicy(TeaModel):
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


class PopCreateObjectProjectResponseBodyDataSourceSourceFiles(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        file_name: str = None,
        filesize: int = None,
        modified_time: str = None,
        oss_key: str = None,
        type: str = None,
        url: str = None,
    ):
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.file_name = file_name
        self.filesize = filesize
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
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
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
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopCreateObjectProjectResponseBodyDataSource(TeaModel):
    def __init__(
        self,
        clothes: List[PopCreateObjectProjectResponseBodyDataSourceClothes] = None,
        create_time: str = None,
        deleted: bool = None,
        modified_time: str = None,
        oss_key: str = None,
        policy: PopCreateObjectProjectResponseBodyDataSourcePolicy = None,
        source_files: List[PopCreateObjectProjectResponseBodyDataSourceSourceFiles] = None,
    ):
        self.clothes = clothes
        self.create_time = create_time
        self.deleted = deleted
        self.modified_time = modified_time
        self.oss_key = oss_key
        self.policy = policy
        self.source_files = source_files

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopCreateObjectProjectResponseBodyDataSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopCreateObjectProjectResponseBodyDataSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        return self


class PopCreateObjectProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_build: bool = None,
        biz_usage: str = None,
        build_detail: PopCreateObjectProjectResponseBodyDataBuildDetail = None,
        check_status: str = None,
        create_mode: str = None,
        create_time: str = None,
        dataset: PopCreateObjectProjectResponseBodyDataDataset = None,
        deleted: bool = None,
        dependencies: str = None,
        ext: str = None,
        id: str = None,
        intro: str = None,
        modified_time: str = None,
        source: PopCreateObjectProjectResponseBodyDataSource = None,
        status: str = None,
        title: str = None,
        type: str = None,
    ):
        self.auto_build = auto_build
        self.biz_usage = biz_usage
        self.build_detail = build_detail
        self.check_status = check_status
        self.create_mode = create_mode
        self.create_time = create_time
        self.dataset = dataset
        self.deleted = deleted
        self.dependencies = dependencies
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
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
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
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopCreateObjectProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PopCreateObjectProjectResponseBodyData = None,
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
            temp_model = PopCreateObjectProjectResponseBodyData()
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


class PopCreateObjectProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PopCreateObjectProjectResponseBody = None,
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
            temp_model = PopCreateObjectProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListFeatureToAvatarMaterialsRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        list_status: str = None,
        size: int = None,
        tags: str = None,
    ):
        self.current = current
        self.list_status = list_status
        self.size = size
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.size is not None:
            result['Size'] = self.size
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class PopListFeatureToAvatarMaterialsResponseBodyData(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        common: bool = None,
        cover_url: str = None,
        deleted: bool = None,
        ext: str = None,
        file_url: str = None,
        id: str = None,
        intro: str = None,
        list_status: str = None,
        name: str = None,
        type: str = None,
    ):
        self.check_status = check_status
        self.common = common
        self.cover_url = cover_url
        self.deleted = deleted
        self.ext = ext
        self.file_url = file_url
        self.id = id
        self.intro = intro
        self.list_status = list_status
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListFeatureToAvatarMaterialsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[PopListFeatureToAvatarMaterialsResponseBodyData] = None,
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
                temp_model = PopListFeatureToAvatarMaterialsResponseBodyData()
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


class PopListFeatureToAvatarMaterialsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PopListFeatureToAvatarMaterialsResponseBody = None,
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
            temp_model = PopListFeatureToAvatarMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListFeatureToAvatarProjectRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        size: int = None,
        sort_field: str = None,
        status: str = None,
        title: str = None,
    ):
        self.current = current
        self.size = size
        self.sort_field = sort_field
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.size is not None:
            result['Size'] = self.size
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopListFeatureToAvatarProjectResponseBodyDataBuildDetail(TeaModel):
    def __init__(
        self,
        completed_time: str = None,
        create_time: str = None,
        deleted: bool = None,
        error_message: str = None,
        estimated_duration: int = None,
        id: int = None,
        modified_time: str = None,
        running_time: str = None,
        status: str = None,
        submit_time: str = None,
    ):
        self.completed_time = completed_time
        self.create_time = create_time
        self.deleted = deleted
        self.error_message = error_message
        self.estimated_duration = estimated_duration
        self.id = id
        self.modified_time = modified_time
        self.running_time = running_time
        self.status = status
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopListFeatureToAvatarProjectResponseBodyDataDatasetPolicy(TeaModel):
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


class PopListFeatureToAvatarProjectResponseBodyDataDataset(TeaModel):
    def __init__(
        self,
        build_result_url: Dict[str, Any] = None,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        error_code: str = None,
        error_message: str = None,
        glb_model_url: str = None,
        id: int = None,
        model_url: str = None,
        modified_time: str = None,
        origin_result_url: str = None,
        oss_key: str = None,
        policy: PopListFeatureToAvatarProjectResponseBodyDataDatasetPolicy = None,
        pose_url: str = None,
        preview_url: str = None,
    ):
        self.build_result_url = build_result_url
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.error_code = error_code
        self.error_message = error_message
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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
            temp_model = PopListFeatureToAvatarProjectResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopListFeatureToAvatarProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_usage: str = None,
        build_detail: PopListFeatureToAvatarProjectResponseBodyDataBuildDetail = None,
        check_status: str = None,
        create_mode: str = None,
        create_time: str = None,
        dataset: PopListFeatureToAvatarProjectResponseBodyDataDataset = None,
        deleted: bool = None,
        ext: str = None,
        id: str = None,
        intro: str = None,
        material_cover_url: str = None,
        modified_time: str = None,
        status: str = None,
        title: str = None,
        type: str = None,
    ):
        self.biz_usage = biz_usage
        self.build_detail = build_detail
        self.check_status = check_status
        self.create_mode = create_mode
        self.create_time = create_time
        self.dataset = dataset
        self.deleted = deleted
        self.ext = ext
        self.id = id
        self.intro = intro
        self.material_cover_url = material_cover_url
        self.modified_time = modified_time
        self.status = status
        self.title = title
        self.type = type

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
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
            temp_model = PopListFeatureToAvatarProjectResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopListFeatureToAvatarProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListFeatureToAvatarProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[PopListFeatureToAvatarProjectResponseBodyData] = None,
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
                temp_model = PopListFeatureToAvatarProjectResponseBodyData()
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


class PopListFeatureToAvatarProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PopListFeatureToAvatarProjectResponseBody = None,
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
            temp_model = PopListFeatureToAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListObjectProjectRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        size: int = None,
        sort_field: str = None,
        status: str = None,
        title: str = None,
        with_source: bool = None,
    ):
        self.current = current
        self.size = size
        self.sort_field = sort_field
        self.status = status
        self.title = title
        self.with_source = with_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.size is not None:
            result['Size'] = self.size
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.with_source is not None:
            result['WithSource'] = self.with_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WithSource') is not None:
            self.with_source = m.get('WithSource')
        return self


class PopListObjectProjectResponseBodyDataBuildDetail(TeaModel):
    def __init__(
        self,
        completed_time: str = None,
        create_time: str = None,
        deleted: bool = None,
        error_message: str = None,
        estimated_duration: int = None,
        modified_time: str = None,
        running_time: str = None,
        submit_time: str = None,
    ):
        self.completed_time = completed_time
        self.create_time = create_time
        self.deleted = deleted
        self.error_message = error_message
        self.estimated_duration = estimated_duration
        self.modified_time = modified_time
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopListObjectProjectResponseBodyDataDatasetPolicy(TeaModel):
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


class PopListObjectProjectResponseBodyDataDataset(TeaModel):
    def __init__(
        self,
        build_result_url: Dict[str, Any] = None,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        error_message: str = None,
        glb_model_url: str = None,
        model_url: str = None,
        modified_time: str = None,
        origin_result_url: str = None,
        oss_key: str = None,
        policy: PopListObjectProjectResponseBodyDataDatasetPolicy = None,
        pose_url: str = None,
        preview_url: str = None,
    ):
        self.build_result_url = build_result_url
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.error_message = error_message
        self.glb_model_url = glb_model_url
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListObjectProjectResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopListObjectProjectResponseBodyDataSourceClothes(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        modified_time: str = None,
        name: str = None,
        oss_key: str = None,
        type: str = None,
    ):
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.modified_time = modified_time
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListObjectProjectResponseBodyDataSourcePolicy(TeaModel):
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


class PopListObjectProjectResponseBodyDataSourceSourceFiles(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        file_name: str = None,
        filesize: int = None,
        modified_time: str = None,
        oss_key: str = None,
        type: str = None,
        url: str = None,
    ):
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.file_name = file_name
        self.filesize = filesize
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
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
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
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopListObjectProjectResponseBodyDataSource(TeaModel):
    def __init__(
        self,
        clothes: List[PopListObjectProjectResponseBodyDataSourceClothes] = None,
        create_time: str = None,
        deleted: bool = None,
        modified_time: str = None,
        oss_key: str = None,
        policy: PopListObjectProjectResponseBodyDataSourcePolicy = None,
        source_files: List[PopListObjectProjectResponseBodyDataSourceSourceFiles] = None,
    ):
        self.clothes = clothes
        self.create_time = create_time
        self.deleted = deleted
        self.modified_time = modified_time
        self.oss_key = oss_key
        self.policy = policy
        self.source_files = source_files

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopListObjectProjectResponseBodyDataSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListObjectProjectResponseBodyDataSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopListObjectProjectResponseBodyDataSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        return self


class PopListObjectProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_build: bool = None,
        biz_usage: str = None,
        build_detail: PopListObjectProjectResponseBodyDataBuildDetail = None,
        check_status: str = None,
        create_mode: str = None,
        create_time: str = None,
        dataset: PopListObjectProjectResponseBodyDataDataset = None,
        deleted: bool = None,
        dependencies: str = None,
        ext: str = None,
        id: str = None,
        intro: str = None,
        modified_time: str = None,
        source: PopListObjectProjectResponseBodyDataSource = None,
        status: str = None,
        title: str = None,
        type: str = None,
    ):
        self.auto_build = auto_build
        self.biz_usage = biz_usage
        self.build_detail = build_detail
        self.check_status = check_status
        self.create_mode = create_mode
        self.create_time = create_time
        self.dataset = dataset
        self.deleted = deleted
        self.dependencies = dependencies
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
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
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
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopListObjectProjectResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopListObjectProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = PopListObjectProjectResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListObjectProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[PopListObjectProjectResponseBodyData] = None,
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
                temp_model = PopListObjectProjectResponseBodyData()
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


class PopListObjectProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PopListObjectProjectResponseBody = None,
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
            temp_model = PopListObjectProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopObjectProjectDetailRequest(TeaModel):
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


class PopObjectProjectDetailResponseBodyDataBuildDetail(TeaModel):
    def __init__(
        self,
        completed_time: str = None,
        create_time: str = None,
        deleted: bool = None,
        error_message: str = None,
        estimated_duration: int = None,
        modified_time: str = None,
        running_time: str = None,
        submit_time: str = None,
    ):
        self.completed_time = completed_time
        self.create_time = create_time
        self.deleted = deleted
        self.error_message = error_message
        self.estimated_duration = estimated_duration
        self.modified_time = modified_time
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopObjectProjectDetailResponseBodyDataDatasetPolicy(TeaModel):
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


class PopObjectProjectDetailResponseBodyDataDataset(TeaModel):
    def __init__(
        self,
        build_result_url: Dict[str, Any] = None,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        error_message: str = None,
        glb_model_url: str = None,
        model_url: str = None,
        modified_time: str = None,
        origin_result_url: str = None,
        oss_key: str = None,
        policy: PopObjectProjectDetailResponseBodyDataDatasetPolicy = None,
        pose_url: str = None,
        preview_url: str = None,
    ):
        self.build_result_url = build_result_url
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.error_message = error_message
        self.glb_model_url = glb_model_url
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopObjectProjectDetailResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopObjectProjectDetailResponseBodyDataSourceClothes(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        modified_time: str = None,
        name: str = None,
        oss_key: str = None,
        type: str = None,
    ):
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.modified_time = modified_time
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopObjectProjectDetailResponseBodyDataSourcePolicy(TeaModel):
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


class PopObjectProjectDetailResponseBodyDataSourceSourceFiles(TeaModel):
    def __init__(
        self,
        cover_url: str = None,
        create_time: str = None,
        deleted: bool = None,
        file_name: str = None,
        filesize: int = None,
        modified_time: str = None,
        oss_key: str = None,
        type: str = None,
        url: str = None,
    ):
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted = deleted
        self.file_name = file_name
        self.filesize = filesize
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
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
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
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopObjectProjectDetailResponseBodyDataSource(TeaModel):
    def __init__(
        self,
        clothes: List[PopObjectProjectDetailResponseBodyDataSourceClothes] = None,
        create_time: str = None,
        deleted: bool = None,
        modified_time: str = None,
        oss_key: str = None,
        policy: PopObjectProjectDetailResponseBodyDataSourcePolicy = None,
        source_files: List[PopObjectProjectDetailResponseBodyDataSourceSourceFiles] = None,
    ):
        self.clothes = clothes
        self.create_time = create_time
        self.deleted = deleted
        self.modified_time = modified_time
        self.oss_key = oss_key
        self.policy = policy
        self.source_files = source_files

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopObjectProjectDetailResponseBodyDataSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopObjectProjectDetailResponseBodyDataSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopObjectProjectDetailResponseBodyDataSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        return self


class PopObjectProjectDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_build: bool = None,
        biz_usage: str = None,
        build_detail: PopObjectProjectDetailResponseBodyDataBuildDetail = None,
        check_status: str = None,
        create_mode: str = None,
        create_time: str = None,
        dataset: PopObjectProjectDetailResponseBodyDataDataset = None,
        deleted: bool = None,
        dependencies: str = None,
        ext: str = None,
        id: str = None,
        intro: str = None,
        modified_time: str = None,
        source: PopObjectProjectDetailResponseBodyDataSource = None,
        status: str = None,
        title: str = None,
        type: str = None,
    ):
        self.auto_build = auto_build
        self.biz_usage = biz_usage
        self.build_detail = build_detail
        self.check_status = check_status
        self.create_mode = create_mode
        self.create_time = create_time
        self.dataset = dataset
        self.deleted = deleted
        self.dependencies = dependencies
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
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
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
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopObjectProjectDetailResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopObjectProjectDetailResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = PopObjectProjectDetailResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopObjectProjectDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PopObjectProjectDetailResponseBodyData = None,
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
            temp_model = PopObjectProjectDetailResponseBodyData()
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


class PopObjectProjectDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PopObjectProjectDetailResponseBody = None,
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
            temp_model = PopObjectProjectDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



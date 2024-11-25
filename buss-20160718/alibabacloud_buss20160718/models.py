# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ApplyRemovingPunishRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        id: str = None,
    ):
        self.ali_uid = ali_uid
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ApplyRemovingPunishResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
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
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApplyRemovingPunishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyRemovingPunishResponseBody = None,
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
            temp_model = ApplyRemovingPunishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddPunishListRequestPunishListRequests(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        data_value: str = None,
        operator: str = None,
        reason: str = None,
        source_code: str = None,
        type: str = None,
    ):
        self.data_type = data_type
        self.data_value = data_value
        self.operator = operator
        self.reason = reason
        self.source_code = source_code
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_value is not None:
            result['DataValue'] = self.data_value
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataValue') is not None:
            self.data_value = m.get('DataValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class BatchAddPunishListRequest(TeaModel):
    def __init__(
        self,
        punish_list_requests: List[BatchAddPunishListRequestPunishListRequests] = None,
    ):
        # This parameter is required.
        self.punish_list_requests = punish_list_requests

    def validate(self):
        if self.punish_list_requests:
            for k in self.punish_list_requests:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PunishListRequests'] = []
        if self.punish_list_requests is not None:
            for k in self.punish_list_requests:
                result['PunishListRequests'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.punish_list_requests = []
        if m.get('PunishListRequests') is not None:
            for k in m.get('PunishListRequests'):
                temp_model = BatchAddPunishListRequestPunishListRequests()
                self.punish_list_requests.append(temp_model.from_map(k))
        return self


class BatchAddPunishListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchAddPunishListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddPunishListResponseBody = None,
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
            temp_model = BatchAddPunishListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDelPunishListRequestPunishListRequests(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        data_value: str = None,
        operator: str = None,
        reason: str = None,
        source_code: str = None,
        type: str = None,
    ):
        self.data_type = data_type
        self.data_value = data_value
        self.operator = operator
        self.reason = reason
        self.source_code = source_code
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_value is not None:
            result['DataValue'] = self.data_value
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataValue') is not None:
            self.data_value = m.get('DataValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class BatchDelPunishListRequest(TeaModel):
    def __init__(
        self,
        punish_list_requests: List[BatchDelPunishListRequestPunishListRequests] = None,
    ):
        # This parameter is required.
        self.punish_list_requests = punish_list_requests

    def validate(self):
        if self.punish_list_requests:
            for k in self.punish_list_requests:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PunishListRequests'] = []
        if self.punish_list_requests is not None:
            for k in self.punish_list_requests:
                result['PunishListRequests'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.punish_list_requests = []
        if m.get('PunishListRequests') is not None:
            for k in m.get('PunishListRequests'):
                temp_model = BatchDelPunishListRequestPunishListRequests()
                self.punish_list_requests.append(temp_model.from_map(k))
        return self


class BatchDelPunishListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDelPunishListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDelPunishListResponseBody = None,
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
            temp_model = BatchDelPunishListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelPunishWhiteForIdcispRequestPunishListRequests(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        data_value: str = None,
        operator: str = None,
        reason: str = None,
        source_code: str = None,
        type: str = None,
    ):
        self.data_type = data_type
        self.data_value = data_value
        self.operator = operator
        self.reason = reason
        self.source_code = source_code
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_value is not None:
            result['DataValue'] = self.data_value
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataValue') is not None:
            self.data_value = m.get('DataValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DelPunishWhiteForIdcispRequest(TeaModel):
    def __init__(
        self,
        punish_list_requests: List[DelPunishWhiteForIdcispRequestPunishListRequests] = None,
    ):
        # This parameter is required.
        self.punish_list_requests = punish_list_requests

    def validate(self):
        if self.punish_list_requests:
            for k in self.punish_list_requests:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PunishListRequests'] = []
        if self.punish_list_requests is not None:
            for k in self.punish_list_requests:
                result['PunishListRequests'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.punish_list_requests = []
        if m.get('PunishListRequests') is not None:
            for k in m.get('PunishListRequests'):
                temp_model = DelPunishWhiteForIdcispRequestPunishListRequests()
                self.punish_list_requests.append(temp_model.from_map(k))
        return self


class DelPunishWhiteForIdcispResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DelPunishWhiteForIdcispResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DelPunishWhiteForIdcispResponseBody = None,
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
            temp_model = DelPunishWhiteForIdcispResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindFullPunishWhiteListRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        source_code: str = None,
    ):
        # This parameter is required.
        self.data_type = data_type
        # This parameter is required.
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class FindFullPunishWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class FindFullPunishWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindFullPunishWhiteListResponseBody = None,
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
            temp_model = FindFullPunishWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindPunishRequestByExtIdRequest(TeaModel):
    def __init__(
        self,
        punish_request_id: str = None,
        source_code: str = None,
    ):
        # This parameter is required.
        self.punish_request_id = punish_request_id
        # This parameter is required.
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.punish_request_id is not None:
            result['PunishRequestId'] = self.punish_request_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PunishRequestId') is not None:
            self.punish_request_id = m.get('PunishRequestId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class FindPunishRequestByExtIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class FindPunishRequestByExtIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindPunishRequestByExtIdResponseBody = None,
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
            temp_model = FindPunishRequestByExtIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindPunishRequestByIdRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class FindPunishRequestByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class FindPunishRequestByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindPunishRequestByIdResponseBody = None,
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
            temp_model = FindPunishRequestByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindPunishWhiteRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        data_values: List[str] = None,
        source_code: str = None,
    ):
        # This parameter is required.
        self.data_type = data_type
        # This parameter is required.
        self.data_values = data_values
        # This parameter is required.
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_values is not None:
            result['DataValues'] = self.data_values
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataValues') is not None:
            self.data_values = m.get('DataValues')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class FindPunishWhiteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class FindPunishWhiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindPunishWhiteResponseBody = None,
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
            temp_model = FindPunishWhiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PunishWhiteListServiceRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        data_values: List[str] = None,
        filter_global: bool = None,
        source_code: str = None,
    ):
        self.data_type = data_type
        self.data_values = data_values
        self.filter_global = filter_global
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_values is not None:
            result['DataValues'] = self.data_values
        if self.filter_global is not None:
            result['FilterGlobal'] = self.filter_global
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataValues') is not None:
            self.data_values = m.get('DataValues')
        if m.get('FilterGlobal') is not None:
            self.filter_global = m.get('FilterGlobal')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class PunishWhiteListServiceShrinkRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        data_values_shrink: str = None,
        filter_global: bool = None,
        source_code: str = None,
    ):
        self.data_type = data_type
        self.data_values_shrink = data_values_shrink
        self.filter_global = filter_global
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_values_shrink is not None:
            result['DataValues'] = self.data_values_shrink
        if self.filter_global is not None:
            result['FilterGlobal'] = self.filter_global
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataValues') is not None:
            self.data_values_shrink = m.get('DataValues')
        if m.get('FilterGlobal') is not None:
            self.filter_global = m.get('FilterGlobal')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class PunishWhiteListServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, str] = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class PunishWhiteListServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PunishWhiteListServiceResponseBody = None,
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
            temp_model = PunishWhiteListServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIppTaskListRequest(TeaModel):
    def __init__(
        self,
        param_0: int = None,
        param_1: int = None,
    ):
        self.param_0 = param_0
        self.param_1 = param_1

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_0 is not None:
            result['Param0'] = self.param_0
        if self.param_1 is not None:
            result['Param1'] = self.param_1
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param0') is not None:
            self.param_0 = m.get('Param0')
        if m.get('Param1') is not None:
            self.param_1 = m.get('Param1')
        return self


class QueryIppTaskListResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        module: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.error_code = error_code
        self.module = module
        self.success = success
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.module is not None:
            result['Module'] = self.module
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryIppTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryIppTaskListResponseBody = None,
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
            temp_model = QueryIppTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOverseaIppTaskListRequest(TeaModel):
    def __init__(
        self,
        param_0: int = None,
        param_1: int = None,
    ):
        self.param_0 = param_0
        self.param_1 = param_1

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_0 is not None:
            result['Param0'] = self.param_0
        if self.param_1 is not None:
            result['Param1'] = self.param_1
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param0') is not None:
            self.param_0 = m.get('Param0')
        if m.get('Param1') is not None:
            self.param_1 = m.get('Param1')
        return self


class QueryOverseaIppTaskListResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        module: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.error_code = error_code
        self.module = module
        self.success = success
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.module is not None:
            result['Module'] = self.module
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryOverseaIppTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOverseaIppTaskListResponseBody = None,
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
            temp_model = QueryOverseaIppTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPunishForRcRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        current_page: int = None,
        date_end: int = None,
        date_start: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        self.current_page = current_page
        self.date_end = date_end
        self.date_start = date_start
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.date_end is not None:
            result['DateEnd'] = self.date_end
        if self.date_start is not None:
            result['DateStart'] = self.date_start
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DateEnd') is not None:
            self.date_end = m.get('DateEnd')
        if m.get('DateStart') is not None:
            self.date_start = m.get('DateStart')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPunishForRcResponseBodyDataPunishRequestDTO(TeaModel):
    def __init__(
        self,
        anti_result: str = None,
        anti_status: str = None,
        bussiness_code: str = None,
        event_code: str = None,
        ext_request_id: str = None,
        gmt_created: int = None,
        id: int = None,
        instance_id: str = None,
        punish_domain: str = None,
        punish_ip: str = None,
        punish_result: str = None,
        punish_status: str = None,
        punish_url: str = None,
        reason: str = None,
        source_code: str = None,
        user_id: str = None,
    ):
        self.anti_result = anti_result
        self.anti_status = anti_status
        self.bussiness_code = bussiness_code
        self.event_code = event_code
        self.ext_request_id = ext_request_id
        self.gmt_created = gmt_created
        self.id = id
        self.instance_id = instance_id
        self.punish_domain = punish_domain
        self.punish_ip = punish_ip
        self.punish_result = punish_result
        self.punish_status = punish_status
        self.punish_url = punish_url
        self.reason = reason
        self.source_code = source_code
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_result is not None:
            result['AntiResult'] = self.anti_result
        if self.anti_status is not None:
            result['AntiStatus'] = self.anti_status
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.ext_request_id is not None:
            result['ExtRequestId'] = self.ext_request_id
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.punish_domain is not None:
            result['PunishDomain'] = self.punish_domain
        if self.punish_ip is not None:
            result['PunishIp'] = self.punish_ip
        if self.punish_result is not None:
            result['PunishResult'] = self.punish_result
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        if self.punish_url is not None:
            result['PunishUrl'] = self.punish_url
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiResult') is not None:
            self.anti_result = m.get('AntiResult')
        if m.get('AntiStatus') is not None:
            self.anti_status = m.get('AntiStatus')
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('ExtRequestId') is not None:
            self.ext_request_id = m.get('ExtRequestId')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PunishDomain') is not None:
            self.punish_domain = m.get('PunishDomain')
        if m.get('PunishIp') is not None:
            self.punish_ip = m.get('PunishIp')
        if m.get('PunishResult') is not None:
            self.punish_result = m.get('PunishResult')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        if m.get('PunishUrl') is not None:
            self.punish_url = m.get('PunishUrl')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryPunishForRcResponseBodyData(TeaModel):
    def __init__(
        self,
        punish_request_dto: List[QueryPunishForRcResponseBodyDataPunishRequestDTO] = None,
    ):
        self.punish_request_dto = punish_request_dto

    def validate(self):
        if self.punish_request_dto:
            for k in self.punish_request_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PunishRequestDTO'] = []
        if self.punish_request_dto is not None:
            for k in self.punish_request_dto:
                result['PunishRequestDTO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.punish_request_dto = []
        if m.get('PunishRequestDTO') is not None:
            for k in m.get('PunishRequestDTO'):
                temp_model = QueryPunishForRcResponseBodyDataPunishRequestDTO()
                self.punish_request_dto.append(temp_model.from_map(k))
        return self


class QueryPunishForRcResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryPunishForRcResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryPunishForRcResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPunishForRcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPunishForRcResponseBody = None,
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
            temp_model = QueryPunishForRcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPunishListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        date_end: int = None,
        date_start: int = None,
        page_size: int = None,
        punish_ip: str = None,
        punish_url: str = None,
    ):
        self.current_page = current_page
        self.date_end = date_end
        self.date_start = date_start
        self.page_size = page_size
        self.punish_ip = punish_ip
        self.punish_url = punish_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.date_end is not None:
            result['DateEnd'] = self.date_end
        if self.date_start is not None:
            result['DateStart'] = self.date_start
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.punish_ip is not None:
            result['PunishIp'] = self.punish_ip
        if self.punish_url is not None:
            result['PunishUrl'] = self.punish_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DateEnd') is not None:
            self.date_end = m.get('DateEnd')
        if m.get('DateStart') is not None:
            self.date_start = m.get('DateStart')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PunishIp') is not None:
            self.punish_ip = m.get('PunishIp')
        if m.get('PunishUrl') is not None:
            self.punish_url = m.get('PunishUrl')
        return self


class QueryPunishListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class QueryPunishListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPunishListResponseBody = None,
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
            temp_model = QueryPunishListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRiskPunishListRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        current_page: int = None,
        date_end: str = None,
        date_start: str = None,
        ip: str = None,
        page_size: int = None,
        url: str = None,
    ):
        self.ali_uid = ali_uid
        self.current_page = current_page
        self.date_end = date_end
        self.date_start = date_start
        self.ip = ip
        self.page_size = page_size
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.date_end is not None:
            result['DateEnd'] = self.date_end
        if self.date_start is not None:
            result['DateStart'] = self.date_start
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DateEnd') is not None:
            self.date_end = m.get('DateEnd')
        if m.get('DateStart') is not None:
            self.date_start = m.get('DateStart')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryRiskPunishListResponseBodyDataListApplyRecords(TeaModel):
    def __init__(
        self,
        apply_status: str = None,
        fail_reason: str = None,
        gmt_apply: str = None,
        gmt_remove_punish: str = None,
    ):
        self.apply_status = apply_status
        self.fail_reason = fail_reason
        self.gmt_apply = gmt_apply
        self.gmt_remove_punish = gmt_remove_punish

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_status is not None:
            result['applyStatus'] = self.apply_status
        if self.fail_reason is not None:
            result['failReason'] = self.fail_reason
        if self.gmt_apply is not None:
            result['gmtApply'] = self.gmt_apply
        if self.gmt_remove_punish is not None:
            result['gmtRemovePunish'] = self.gmt_remove_punish
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyStatus') is not None:
            self.apply_status = m.get('applyStatus')
        if m.get('failReason') is not None:
            self.fail_reason = m.get('failReason')
        if m.get('gmtApply') is not None:
            self.gmt_apply = m.get('gmtApply')
        if m.get('gmtRemovePunish') is not None:
            self.gmt_remove_punish = m.get('gmtRemovePunish')
        return self


class QueryRiskPunishListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        action: str = None,
        apply_records: List[QueryRiskPunishListResponseBodyDataListApplyRecords] = None,
        apply_status: str = None,
        business: str = None,
        domain: str = None,
        gmt_punished: str = None,
        id: int = None,
        ip: str = None,
        is_config_waf: int = None,
        is_domain: int = None,
        port: str = None,
        punish_status: str = None,
        reason: str = None,
        url: str = None,
    ):
        self.action = action
        self.apply_records = apply_records
        self.apply_status = apply_status
        self.business = business
        self.domain = domain
        self.gmt_punished = gmt_punished
        self.id = id
        self.ip = ip
        self.is_config_waf = is_config_waf
        self.is_domain = is_domain
        self.port = port
        self.punish_status = punish_status
        self.reason = reason
        self.url = url

    def validate(self):
        if self.apply_records:
            for k in self.apply_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        result['ApplyRecords'] = []
        if self.apply_records is not None:
            for k in self.apply_records:
                result['ApplyRecords'].append(k.to_map() if k else None)
        if self.apply_status is not None:
            result['ApplyStatus'] = self.apply_status
        if self.business is not None:
            result['Business'] = self.business
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.gmt_punished is not None:
            result['GmtPunished'] = self.gmt_punished
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.is_config_waf is not None:
            result['IsConfigWaf'] = self.is_config_waf
        if self.is_domain is not None:
            result['IsDomain'] = self.is_domain
        if self.port is not None:
            result['Port'] = self.port
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        self.apply_records = []
        if m.get('ApplyRecords') is not None:
            for k in m.get('ApplyRecords'):
                temp_model = QueryRiskPunishListResponseBodyDataListApplyRecords()
                self.apply_records.append(temp_model.from_map(k))
        if m.get('ApplyStatus') is not None:
            self.apply_status = m.get('ApplyStatus')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('GmtPunished') is not None:
            self.gmt_punished = m.get('GmtPunished')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IsConfigWaf') is not None:
            self.is_config_waf = m.get('IsConfigWaf')
        if m.get('IsDomain') is not None:
            self.is_domain = m.get('IsDomain')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryRiskPunishListResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryRiskPunishListResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryRiskPunishListResponseBodyDataList] = None,
        page_info: QueryRiskPunishListResponseBodyDataPageInfo = None,
    ):
        self.list = list
        self.page_info = page_info

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRiskPunishListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = QueryRiskPunishListResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        return self


class QueryRiskPunishListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRiskPunishListResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryRiskPunishListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRiskPunishListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRiskPunishListResponseBody = None,
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
            temp_model = QueryRiskPunishListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRiskPunishRecordRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        business: str = None,
        current_page: int = None,
        ip: str = None,
        page_size: int = None,
        punish_date_end: str = None,
        punish_date_start: str = None,
        punish_status: str = None,
        url: str = None,
        yundun_access_key: str = None,
        yundun_access_key_secret: str = None,
    ):
        self.ali_uid = ali_uid
        self.business = business
        self.current_page = current_page
        self.ip = ip
        self.page_size = page_size
        self.punish_date_end = punish_date_end
        self.punish_date_start = punish_date_start
        self.punish_status = punish_status
        self.url = url
        self.yundun_access_key = yundun_access_key
        self.yundun_access_key_secret = yundun_access_key_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.business is not None:
            result['Business'] = self.business
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.punish_date_end is not None:
            result['PunishDateEnd'] = self.punish_date_end
        if self.punish_date_start is not None:
            result['PunishDateStart'] = self.punish_date_start
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        if self.url is not None:
            result['Url'] = self.url
        if self.yundun_access_key is not None:
            result['YundunAccessKey'] = self.yundun_access_key
        if self.yundun_access_key_secret is not None:
            result['YundunAccessKeySecret'] = self.yundun_access_key_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PunishDateEnd') is not None:
            self.punish_date_end = m.get('PunishDateEnd')
        if m.get('PunishDateStart') is not None:
            self.punish_date_start = m.get('PunishDateStart')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('YundunAccessKey') is not None:
            self.yundun_access_key = m.get('YundunAccessKey')
        if m.get('YundunAccessKeySecret') is not None:
            self.yundun_access_key_secret = m.get('YundunAccessKeySecret')
        return self


class QueryRiskPunishRecordResponseBodyDataListApplyRecords(TeaModel):
    def __init__(
        self,
        apply_status: str = None,
        fail_reason: str = None,
        gmt_apply: str = None,
        gmt_remove_punish: str = None,
    ):
        self.apply_status = apply_status
        self.fail_reason = fail_reason
        self.gmt_apply = gmt_apply
        self.gmt_remove_punish = gmt_remove_punish

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_status is not None:
            result['applyStatus'] = self.apply_status
        if self.fail_reason is not None:
            result['failReason'] = self.fail_reason
        if self.gmt_apply is not None:
            result['gmtApply'] = self.gmt_apply
        if self.gmt_remove_punish is not None:
            result['gmtRemovePunish'] = self.gmt_remove_punish
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyStatus') is not None:
            self.apply_status = m.get('applyStatus')
        if m.get('failReason') is not None:
            self.fail_reason = m.get('failReason')
        if m.get('gmtApply') is not None:
            self.gmt_apply = m.get('gmtApply')
        if m.get('gmtRemovePunish') is not None:
            self.gmt_remove_punish = m.get('gmtRemovePunish')
        return self


class QueryRiskPunishRecordResponseBodyDataList(TeaModel):
    def __init__(
        self,
        action: str = None,
        apply_records: List[QueryRiskPunishRecordResponseBodyDataListApplyRecords] = None,
        apply_status: str = None,
        business: str = None,
        domain: str = None,
        gmt_punished: str = None,
        id: int = None,
        ip: str = None,
        is_config_waf: int = None,
        is_domain: int = None,
        port: str = None,
        punish_status: str = None,
        reason: str = None,
        url: str = None,
    ):
        self.action = action
        self.apply_records = apply_records
        self.apply_status = apply_status
        self.business = business
        self.domain = domain
        self.gmt_punished = gmt_punished
        self.id = id
        self.ip = ip
        self.is_config_waf = is_config_waf
        self.is_domain = is_domain
        self.port = port
        self.punish_status = punish_status
        self.reason = reason
        self.url = url

    def validate(self):
        if self.apply_records:
            for k in self.apply_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        result['ApplyRecords'] = []
        if self.apply_records is not None:
            for k in self.apply_records:
                result['ApplyRecords'].append(k.to_map() if k else None)
        if self.apply_status is not None:
            result['ApplyStatus'] = self.apply_status
        if self.business is not None:
            result['Business'] = self.business
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.gmt_punished is not None:
            result['GmtPunished'] = self.gmt_punished
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.is_config_waf is not None:
            result['IsConfigWaf'] = self.is_config_waf
        if self.is_domain is not None:
            result['IsDomain'] = self.is_domain
        if self.port is not None:
            result['Port'] = self.port
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        self.apply_records = []
        if m.get('ApplyRecords') is not None:
            for k in m.get('ApplyRecords'):
                temp_model = QueryRiskPunishRecordResponseBodyDataListApplyRecords()
                self.apply_records.append(temp_model.from_map(k))
        if m.get('ApplyStatus') is not None:
            self.apply_status = m.get('ApplyStatus')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('GmtPunished') is not None:
            self.gmt_punished = m.get('GmtPunished')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IsConfigWaf') is not None:
            self.is_config_waf = m.get('IsConfigWaf')
        if m.get('IsDomain') is not None:
            self.is_domain = m.get('IsDomain')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryRiskPunishRecordResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryRiskPunishRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryRiskPunishRecordResponseBodyDataList] = None,
        page_info: QueryRiskPunishRecordResponseBodyDataPageInfo = None,
    ):
        self.list = list
        self.page_info = page_info

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRiskPunishRecordResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = QueryRiskPunishRecordResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        return self


class QueryRiskPunishRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRiskPunishRecordResponseBodyData = None,
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
            temp_model = QueryRiskPunishRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRiskPunishRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRiskPunishRecordResponseBody = None,
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
            temp_model = QueryRiskPunishRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReceiveRaiderDataRequest(TeaModel):
    def __init__(
        self,
        raider_data: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.raider_data = raider_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raider_data is not None:
            result['RaiderData'] = self.raider_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RaiderData') is not None:
            self.raider_data = m.get('RaiderData')
        return self


class ReceiveRaiderDataShrinkRequest(TeaModel):
    def __init__(
        self,
        raider_data_shrink: str = None,
    ):
        # This parameter is required.
        self.raider_data_shrink = raider_data_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raider_data_shrink is not None:
            result['RaiderData'] = self.raider_data_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RaiderData') is not None:
            self.raider_data_shrink = m.get('RaiderData')
        return self


class ReceiveRaiderDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class ReceiveRaiderDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReceiveRaiderDataResponseBody = None,
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
            temp_model = ReceiveRaiderDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RiskPunishRequest(TeaModel):
    def __init__(
        self,
        bussiness_code: str = None,
        domain: str = None,
        event_code: str = None,
        expected_remove_time: int = None,
        extras: Dict[str, Any] = None,
        filter_special_account: bool = None,
        filter_white: bool = None,
        instance_id: str = None,
        ip: str = None,
        is_direct_punish: bool = None,
        punish_date: int = None,
        punish_request_id: str = None,
        punish_url: str = None,
        reason: str = None,
        source_code: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.bussiness_code = bussiness_code
        self.domain = domain
        # This parameter is required.
        self.event_code = event_code
        self.expected_remove_time = expected_remove_time
        self.extras = extras
        self.filter_special_account = filter_special_account
        self.filter_white = filter_white
        self.instance_id = instance_id
        self.ip = ip
        self.is_direct_punish = is_direct_punish
        self.punish_date = punish_date
        # This parameter is required.
        self.punish_request_id = punish_request_id
        self.punish_url = punish_url
        # This parameter is required.
        self.reason = reason
        # This parameter is required.
        self.source_code = source_code
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.expected_remove_time is not None:
            result['ExpectedRemoveTime'] = self.expected_remove_time
        if self.extras is not None:
            result['Extras'] = self.extras
        if self.filter_special_account is not None:
            result['FilterSpecialAccount'] = self.filter_special_account
        if self.filter_white is not None:
            result['FilterWhite'] = self.filter_white
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.is_direct_punish is not None:
            result['IsDirectPunish'] = self.is_direct_punish
        if self.punish_date is not None:
            result['PunishDate'] = self.punish_date
        if self.punish_request_id is not None:
            result['PunishRequestId'] = self.punish_request_id
        if self.punish_url is not None:
            result['PunishUrl'] = self.punish_url
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('ExpectedRemoveTime') is not None:
            self.expected_remove_time = m.get('ExpectedRemoveTime')
        if m.get('Extras') is not None:
            self.extras = m.get('Extras')
        if m.get('FilterSpecialAccount') is not None:
            self.filter_special_account = m.get('FilterSpecialAccount')
        if m.get('FilterWhite') is not None:
            self.filter_white = m.get('FilterWhite')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IsDirectPunish') is not None:
            self.is_direct_punish = m.get('IsDirectPunish')
        if m.get('PunishDate') is not None:
            self.punish_date = m.get('PunishDate')
        if m.get('PunishRequestId') is not None:
            self.punish_request_id = m.get('PunishRequestId')
        if m.get('PunishUrl') is not None:
            self.punish_url = m.get('PunishUrl')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RiskPunishShrinkRequest(TeaModel):
    def __init__(
        self,
        bussiness_code: str = None,
        domain: str = None,
        event_code: str = None,
        expected_remove_time: int = None,
        extras_shrink: str = None,
        filter_special_account: bool = None,
        filter_white: bool = None,
        instance_id: str = None,
        ip: str = None,
        is_direct_punish: bool = None,
        punish_date: int = None,
        punish_request_id: str = None,
        punish_url: str = None,
        reason: str = None,
        source_code: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.bussiness_code = bussiness_code
        self.domain = domain
        # This parameter is required.
        self.event_code = event_code
        self.expected_remove_time = expected_remove_time
        self.extras_shrink = extras_shrink
        self.filter_special_account = filter_special_account
        self.filter_white = filter_white
        self.instance_id = instance_id
        self.ip = ip
        self.is_direct_punish = is_direct_punish
        self.punish_date = punish_date
        # This parameter is required.
        self.punish_request_id = punish_request_id
        self.punish_url = punish_url
        # This parameter is required.
        self.reason = reason
        # This parameter is required.
        self.source_code = source_code
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.expected_remove_time is not None:
            result['ExpectedRemoveTime'] = self.expected_remove_time
        if self.extras_shrink is not None:
            result['Extras'] = self.extras_shrink
        if self.filter_special_account is not None:
            result['FilterSpecialAccount'] = self.filter_special_account
        if self.filter_white is not None:
            result['FilterWhite'] = self.filter_white
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.is_direct_punish is not None:
            result['IsDirectPunish'] = self.is_direct_punish
        if self.punish_date is not None:
            result['PunishDate'] = self.punish_date
        if self.punish_request_id is not None:
            result['PunishRequestId'] = self.punish_request_id
        if self.punish_url is not None:
            result['PunishUrl'] = self.punish_url
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('ExpectedRemoveTime') is not None:
            self.expected_remove_time = m.get('ExpectedRemoveTime')
        if m.get('Extras') is not None:
            self.extras_shrink = m.get('Extras')
        if m.get('FilterSpecialAccount') is not None:
            self.filter_special_account = m.get('FilterSpecialAccount')
        if m.get('FilterWhite') is not None:
            self.filter_white = m.get('FilterWhite')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IsDirectPunish') is not None:
            self.is_direct_punish = m.get('IsDirectPunish')
        if m.get('PunishDate') is not None:
            self.punish_date = m.get('PunishDate')
        if m.get('PunishRequestId') is not None:
            self.punish_request_id = m.get('PunishRequestId')
        if m.get('PunishUrl') is not None:
            self.punish_url = m.get('PunishUrl')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RiskPunishResponseBody(TeaModel):
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


class RiskPunishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RiskPunishResponseBody = None,
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
            temp_model = RiskPunishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RiskPunishRemoveRequest(TeaModel):
    def __init__(
        self,
        extras: Dict[str, Any] = None,
        punish_request_id: str = None,
        rm_punish: bool = None,
        source_code: str = None,
    ):
        self.extras = extras
        # This parameter is required.
        self.punish_request_id = punish_request_id
        self.rm_punish = rm_punish
        # This parameter is required.
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extras is not None:
            result['Extras'] = self.extras
        if self.punish_request_id is not None:
            result['PunishRequestId'] = self.punish_request_id
        if self.rm_punish is not None:
            result['RmPunish'] = self.rm_punish
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extras') is not None:
            self.extras = m.get('Extras')
        if m.get('PunishRequestId') is not None:
            self.punish_request_id = m.get('PunishRequestId')
        if m.get('RmPunish') is not None:
            self.rm_punish = m.get('RmPunish')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class RiskPunishRemoveShrinkRequest(TeaModel):
    def __init__(
        self,
        extras_shrink: str = None,
        punish_request_id: str = None,
        rm_punish: bool = None,
        source_code: str = None,
    ):
        self.extras_shrink = extras_shrink
        # This parameter is required.
        self.punish_request_id = punish_request_id
        self.rm_punish = rm_punish
        # This parameter is required.
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extras_shrink is not None:
            result['Extras'] = self.extras_shrink
        if self.punish_request_id is not None:
            result['PunishRequestId'] = self.punish_request_id
        if self.rm_punish is not None:
            result['RmPunish'] = self.rm_punish
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extras') is not None:
            self.extras_shrink = m.get('Extras')
        if m.get('PunishRequestId') is not None:
            self.punish_request_id = m.get('PunishRequestId')
        if m.get('RmPunish') is not None:
            self.rm_punish = m.get('RmPunish')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class RiskPunishRemoveResponseBody(TeaModel):
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


class RiskPunishRemoveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RiskPunishRemoveResponseBody = None,
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
            temp_model = RiskPunishRemoveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



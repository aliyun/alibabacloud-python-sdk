# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CheckReadyFlagRequest(TeaModel):
    def __init__(
        self,
        cycles: int = None,
        data_type: str = None,
        domain_code: str = None,
        end_time: int = None,
        period: str = None,
        start_time: int = None,
    ):
        self.cycles = cycles
        self.data_type = data_type
        self.domain_code = domain_code
        self.end_time = end_time
        self.period = period
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cycles is not None:
            result['Cycles'] = self.cycles
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.period is not None:
            result['Period'] = self.period
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cycles') is not None:
            self.cycles = m.get('Cycles')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CheckReadyFlagResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckReadyFlagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckReadyFlagResponseBody = None,
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
            temp_model = CheckReadyFlagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainPartRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        domain_code: str = None,
        part: str = None,
    ):
        self.data_type = data_type
        self.domain_code = domain_code
        self.part = part

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.part is not None:
            result['Part'] = self.part
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Part') is not None:
            self.part = m.get('Part')
        return self


class DeleteDomainPartResponseBody(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDomainPartResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDomainPartResponseBody = None,
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
            temp_model = DeleteDomainPartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainPartByProxyRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        domain_code: str = None,
        part: str = None,
    ):
        self.data_type = data_type
        self.domain_code = domain_code
        self.part = part

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.part is not None:
            result['Part'] = self.part
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Part') is not None:
            self.part = m.get('Part')
        return self


class DeleteDomainPartByProxyResponseBody(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDomainPartByProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDomainPartByProxyResponseBody = None,
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
            temp_model = DeleteDomainPartByProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMeasureDataRequest(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        filter: str = None,
    ):
        self.api_type = api_type
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        # OMS Domain
        self.domain_code = domain_code
        self.filter = filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.filter is not None:
            result['Filter'] = self.filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        return self


class DeleteMeasureDataResponseBody(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.api_type = api_type
        self.data_type = data_type
        # OMS Domain
        self.domain_code = domain_code
        # Id of the request
        self.request_id = request_id
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DeleteMeasureDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMeasureDataResponseBody = None,
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
            temp_model = DeleteMeasureDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessPolicyConfigRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        compress_enable: bool = None,
    ):
        self.ali_uid = ali_uid
        self.compress_enable = compress_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        return self


class GetAccessPolicyConfigResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        compressed: bool = None,
        data: str = None,
        request_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.compressed = compressed
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessPolicyConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccessPolicyConfigResponseBody = None,
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
            temp_model = GetAccessPolicyConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainConfigRequest(TeaModel):
    def __init__(
        self,
        compress_enable: bool = None,
        domain_code: str = None,
    ):
        self.compress_enable = compress_enable
        self.domain_code = domain_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        return self


class GetDomainConfigResponseBody(TeaModel):
    def __init__(
        self,
        compressed: bool = None,
        data: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.compressed = compressed
        self.data = data
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainConfigResponseBody = None,
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
            temp_model = GetDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainPartRequest(TeaModel):
    def __init__(
        self,
        compress_enable: bool = None,
        data_type: str = None,
        domain_code: str = None,
        part: str = None,
    ):
        self.compress_enable = compress_enable
        self.data_type = data_type
        self.domain_code = domain_code
        self.part = part

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.part is not None:
            result['Part'] = self.part
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Part') is not None:
            self.part = m.get('Part')
        return self


class GetDomainPartResponseBody(TeaModel):
    def __init__(
        self,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainPartResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainPartResponseBody = None,
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
            temp_model = GetDomainPartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainPartByProxyRequest(TeaModel):
    def __init__(
        self,
        compress_enable: bool = None,
        data_type: str = None,
        domain_code: str = None,
        part: str = None,
    ):
        self.compress_enable = compress_enable
        self.data_type = data_type
        self.domain_code = domain_code
        self.part = part

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.part is not None:
            result['Part'] = self.part
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Part') is not None:
            self.part = m.get('Part')
        return self


class GetDomainPartByProxyResponseBody(TeaModel):
    def __init__(
        self,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainPartByProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainPartByProxyResponseBody = None,
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
            temp_model = GetDomainPartByProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainPartConfigRequest(TeaModel):
    def __init__(
        self,
        compress_enable: bool = None,
        data_type: str = None,
        domain_code: str = None,
        part: str = None,
    ):
        self.compress_enable = compress_enable
        self.data_type = data_type
        self.domain_code = domain_code
        self.part = part

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.part is not None:
            result['Part'] = self.part
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Part') is not None:
            self.part = m.get('Part')
        return self


class GetDomainPartConfigResponseBody(TeaModel):
    def __init__(
        self,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainPartConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainPartConfigResponseBody = None,
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
            temp_model = GetDomainPartConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileConfigRequest(TeaModel):
    def __init__(
        self,
        dimension_type: str = None,
        domain_code: str = None,
    ):
        self.dimension_type = dimension_type
        self.domain_code = domain_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension_type is not None:
            result['DimensionType'] = self.dimension_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionType') is not None:
            self.dimension_type = m.get('DimensionType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        return self


class GetFileConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFileConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFileConfigResponseBody = None,
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
            temp_model = GetFileConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIncrementMeasureDataByProxyRequest(TeaModel):
    def __init__(
        self,
        compress_enable: bool = None,
        data_type: str = None,
        domain_code: str = None,
        modify_end_time: int = None,
        modify_start_time: int = None,
        row_key_map_str: str = None,
    ):
        self.compress_enable = compress_enable
        self.data_type = data_type
        self.domain_code = domain_code
        self.modify_end_time = modify_end_time
        self.modify_start_time = modify_start_time
        self.row_key_map_str = row_key_map_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.modify_end_time is not None:
            result['ModifyEndTime'] = self.modify_end_time
        if self.modify_start_time is not None:
            result['ModifyStartTime'] = self.modify_start_time
        if self.row_key_map_str is not None:
            result['RowKeyMapStr'] = self.row_key_map_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('ModifyEndTime') is not None:
            self.modify_end_time = m.get('ModifyEndTime')
        if m.get('ModifyStartTime') is not None:
            self.modify_start_time = m.get('ModifyStartTime')
        if m.get('RowKeyMapStr') is not None:
            self.row_key_map_str = m.get('RowKeyMapStr')
        return self


class GetIncrementMeasureDataByProxyResponseBody(TeaModel):
    def __init__(
        self,
        compressed: str = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIncrementMeasureDataByProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIncrementMeasureDataByProxyResponseBody = None,
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
            temp_model = GetIncrementMeasureDataByProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMeasureDataRequest(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compress_enable: bool = None,
        data_type: str = None,
        domain_code: str = None,
        filter: str = None,
        max_result: int = None,
        next_token: str = None,
        query_field: str = None,
    ):
        self.api_type = api_type
        self.compress_enable = compress_enable
        self.data_type = data_type
        self.domain_code = domain_code
        self.filter = filter
        self.max_result = max_result
        self.next_token = next_token
        self.query_field = query_field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.query_field is not None:
            result['QueryField'] = self.query_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('QueryField') is not None:
            self.query_field = m.get('QueryField')
        return self


class GetMeasureDataResponseBody(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.api_type = api_type
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMeasureDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMeasureDataResponseBody = None,
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
            temp_model = GetMeasureDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenApiConfigRequest(TeaModel):
    def __init__(
        self,
        compress_enable: bool = None,
        data_type: str = None,
        product_name: str = None,
        table_name: str = None,
        site_bid: str = None,
    ):
        self.compress_enable = compress_enable
        self.data_type = data_type
        self.product_name = product_name
        self.table_name = table_name
        self.site_bid = site_bid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.site_bid is not None:
            result['siteBid'] = self.site_bid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('siteBid') is not None:
            self.site_bid = m.get('siteBid')
        return self


class GetOpenApiConfigResponseBody(TeaModel):
    def __init__(
        self,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        product_name: str = None,
        request_id: str = None,
        site_bid: str = None,
        table_name: str = None,
    ):
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.product_name = product_name
        self.request_id = request_id
        self.site_bid = site_bid
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_bid is not None:
            result['SiteBid'] = self.site_bid
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteBid') is not None:
            self.site_bid = m.get('SiteBid')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetOpenApiConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOpenApiConfigResponseBody = None,
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
            temp_model = GetOpenApiConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReadyFlagRequest(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compress_enable: bool = None,
        data_type: str = None,
        domain_code: str = None,
        filter: str = None,
        max_result: int = None,
        next_token: str = None,
    ):
        self.api_type = api_type
        self.compress_enable = compress_enable
        self.data_type = data_type
        self.domain_code = domain_code
        self.filter = filter
        self.max_result = max_result
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetReadyFlagResponseBody(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.api_type = api_type
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetReadyFlagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetReadyFlagResponseBody = None,
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
            temp_model = GetReadyFlagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReadyFlagAlertConfigRequest(TeaModel):
    def __init__(
        self,
        compress_enable: bool = None,
        data_type: str = None,
        domain_code: str = None,
    ):
        self.compress_enable = compress_enable
        self.data_type = data_type
        self.domain_code = domain_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        return self


class GetReadyFlagAlertConfigResponseBody(TeaModel):
    def __init__(
        self,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetReadyFlagAlertConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetReadyFlagAlertConfigResponseBody = None,
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
            temp_model = GetReadyFlagAlertConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReadyFlagByProxyRequest(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compress_enable: bool = None,
        data_type: str = None,
        domain_code: str = None,
        filter: str = None,
        max_result: int = None,
        next_token: str = None,
    ):
        self.api_type = api_type
        self.compress_enable = compress_enable
        self.data_type = data_type
        self.domain_code = domain_code
        self.filter = filter
        self.max_result = max_result
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compress_enable is not None:
            result['CompressEnable'] = self.compress_enable
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('CompressEnable') is not None:
            self.compress_enable = m.get('CompressEnable')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetReadyFlagByProxyResponseBody(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.api_type = api_type
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetReadyFlagByProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetReadyFlagByProxyResponseBody = None,
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
            temp_model = GetReadyFlagByProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutDomainPartRequest(TeaModel):
    def __init__(
        self,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
    ):
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        return self


class PutDomainPartResponseBody(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutDomainPartResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutDomainPartResponseBody = None,
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
            temp_model = PutDomainPartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutDomainPartByProxyRequest(TeaModel):
    def __init__(
        self,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
    ):
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        return self


class PutDomainPartByProxyResponseBody(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutDomainPartByProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutDomainPartByProxyResponseBody = None,
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
            temp_model = PutDomainPartByProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutMeasureDataRequest(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        filter: str = None,
        source_request_id: str = None,
    ):
        self.api_type = api_type
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        self.filter = filter
        self.source_request_id = source_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.source_request_id is not None:
            result['SourceRequestId'] = self.source_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('SourceRequestId') is not None:
            self.source_request_id = m.get('SourceRequestId')
        return self


class PutMeasureDataResponseBody(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
        source_request_id: str = None,
    ):
        self.api_type = api_type
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id
        self.source_request_id = source_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_request_id is not None:
            result['SourceRequestId'] = self.source_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceRequestId') is not None:
            self.source_request_id = m.get('SourceRequestId')
        return self


class PutMeasureDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutMeasureDataResponseBody = None,
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
            temp_model = PutMeasureDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutMeasureDataByProxyRequest(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        filter: str = None,
    ):
        self.api_type = api_type
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        self.filter = filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.filter is not None:
            result['Filter'] = self.filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        return self


class PutMeasureDataByProxyResponseBody(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.api_type = api_type
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutMeasureDataByProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutMeasureDataByProxyResponseBody = None,
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
            temp_model = PutMeasureDataByProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutReadyFlagRequest(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
        source_request_id: str = None,
    ):
        self.api_type = api_type
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code
        self.source_request_id = source_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.source_request_id is not None:
            result['SourceRequestId'] = self.source_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('SourceRequestId') is not None:
            self.source_request_id = m.get('SourceRequestId')
        return self


class PutReadyFlagResponseBody(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
        source_request_id: str = None,
    ):
        self.api_type = api_type
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id
        self.source_request_id = source_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_request_id is not None:
            result['SourceRequestId'] = self.source_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceRequestId') is not None:
            self.source_request_id = m.get('SourceRequestId')
        return self


class PutReadyFlagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutReadyFlagResponseBody = None,
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
            temp_model = PutReadyFlagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutReadyFlagByProxyRequest(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        compressed: bool = None,
        data: str = None,
        data_type: str = None,
        domain_code: str = None,
    ):
        self.api_type = api_type
        self.compressed = compressed
        self.data = data
        self.data_type = data_type
        self.domain_code = domain_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        return self


class PutReadyFlagByProxyResponseBody(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        data_type: str = None,
        domain_code: str = None,
        request_id: str = None,
    ):
        self.api_type = api_type
        self.data_type = data_type
        self.domain_code = domain_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutReadyFlagByProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutReadyFlagByProxyResponseBody = None,
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
            temp_model = PutReadyFlagByProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



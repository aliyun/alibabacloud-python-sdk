# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class GetOpenStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
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


class GetOpenStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOpenStatusResponseBody = None,
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
            temp_model = GetOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderInfoRequest(TeaModel):
    def __init__(
        self,
        list_released: bool = None,
        rel_service: str = None,
        resource_type: int = None,
    ):
        self.list_released = list_released
        # This parameter is required.
        self.rel_service = rel_service
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_released is not None:
            result['ListReleased'] = self.list_released
        if self.rel_service is not None:
            result['RelService'] = self.rel_service
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListReleased') is not None:
            self.list_released = m.get('ListReleased')
        if m.get('RelService') is not None:
            self.rel_service = m.get('RelService')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetOrderInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        current_concurrency: int = None,
        current_days: int = None,
        instance_id: str = None,
        is_released: bool = None,
        license_key: str = None,
        remark: str = None,
        total_days: int = None,
    ):
        self.biz_type = biz_type
        self.current_concurrency = current_concurrency
        self.current_days = current_days
        self.instance_id = instance_id
        self.is_released = is_released
        self.license_key = license_key
        self.remark = remark
        self.total_days = total_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.current_concurrency is not None:
            result['currentConcurrency'] = self.current_concurrency
        if self.current_days is not None:
            result['currentDays'] = self.current_days
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_released is not None:
            result['isReleased'] = self.is_released
        if self.license_key is not None:
            result['licenseKey'] = self.license_key
        if self.remark is not None:
            result['remark'] = self.remark
        if self.total_days is not None:
            result['totalDays'] = self.total_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('currentConcurrency') is not None:
            self.current_concurrency = m.get('currentConcurrency')
        if m.get('currentDays') is not None:
            self.current_days = m.get('currentDays')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isReleased') is not None:
            self.is_released = m.get('isReleased')
        if m.get('licenseKey') is not None:
            self.license_key = m.get('licenseKey')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('totalDays') is not None:
            self.total_days = m.get('totalDays')
        return self


class GetOrderInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOrderInfoResponseBodyData] = None,
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
                temp_model = GetOrderInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrderInfoResponseBody = None,
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
            temp_model = GetOrderInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderUsageRequest(TeaModel):
    def __init__(
        self,
        license_key: str = None,
        rel_service: str = None,
        resource_type: int = None,
        time_range: int = None,
    ):
        # This parameter is required.
        self.license_key = license_key
        # This parameter is required.
        self.rel_service = rel_service
        # This parameter is required.
        self.resource_type = resource_type
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.rel_service is not None:
            result['RelService'] = self.rel_service
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('RelService') is not None:
            self.rel_service = m.get('RelService')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        return self


class GetOrderUsageResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrderUsageResponseBody = None,
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
            temp_model = GetOrderUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



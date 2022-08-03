# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class GetStatTrendRequest(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        data_source_id: str = None,
        end_date: str = None,
        start_date: str = None,
        type: int = None,
    ):
        self.app_version = app_version
        self.data_source_id = data_source_id
        self.end_date = end_date
        self.start_date = start_date
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetStatTrendResponseBodyData(TeaModel):
    def __init__(
        self,
        affected_user_count: int = None,
        affected_user_rate: int = None,
        error_count: int = None,
        error_rate: int = None,
        time_point: str = None,
    ):
        self.affected_user_count = affected_user_count
        self.affected_user_rate = affected_user_rate
        self.error_count = error_count
        self.error_rate = error_rate
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_user_count is not None:
            result['affectedUserCount'] = self.affected_user_count
        if self.affected_user_rate is not None:
            result['affectedUserRate'] = self.affected_user_rate
        if self.error_count is not None:
            result['errorCount'] = self.error_count
        if self.error_rate is not None:
            result['errorRate'] = self.error_rate
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('affectedUserCount') is not None:
            self.affected_user_count = m.get('affectedUserCount')
        if m.get('affectedUserRate') is not None:
            self.affected_user_rate = m.get('affectedUserRate')
        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')
        if m.get('errorRate') is not None:
            self.error_rate = m.get('errorRate')
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        return self


class GetStatTrendResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetStatTrendResponseBodyData] = None,
        msg: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetStatTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetStatTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStatTrendResponseBody = None,
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
            temp_model = GetStatTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSymUploadParamRequest(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        data_source_id: str = None,
        file_name: str = None,
        file_type: int = None,
    ):
        self.app_version = app_version
        self.data_source_id = data_source_id
        self.file_name = file_name
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        return self


class GetSymUploadParamResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        callback: str = None,
        key: str = None,
        policy: str = None,
        signature: str = None,
        upload_address: str = None,
    ):
        self.access_key_id = access_key_id
        self.callback = callback
        self.key = key
        self.policy = policy
        self.signature = signature
        self.upload_address = upload_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.callback is not None:
            result['callback'] = self.callback
        if self.key is not None:
            result['key'] = self.key
        if self.policy is not None:
            result['policy'] = self.policy
        if self.signature is not None:
            result['signature'] = self.signature
        if self.upload_address is not None:
            result['uploadAddress'] = self.upload_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('callback') is not None:
            self.callback = m.get('callback')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('uploadAddress') is not None:
            self.upload_address = m.get('uploadAddress')
        return self


class GetSymUploadParamResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetSymUploadParamResponseBodyData = None,
        msg: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetSymUploadParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class GetSymUploadParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSymUploadParamResponseBody = None,
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
            temp_model = GetSymUploadParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTodayStatTrendRequest(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        data_source_id: str = None,
        type: int = None,
    ):
        self.app_version = app_version
        self.data_source_id = data_source_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTodayStatTrendResponseBodyData(TeaModel):
    def __init__(
        self,
        affected_user_count: int = None,
        affected_user_rate: int = None,
        error_count: int = None,
        error_rate: int = None,
        time_point: str = None,
    ):
        self.affected_user_count = affected_user_count
        self.affected_user_rate = affected_user_rate
        self.error_count = error_count
        self.error_rate = error_rate
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_user_count is not None:
            result['affectedUserCount'] = self.affected_user_count
        if self.affected_user_rate is not None:
            result['affectedUserRate'] = self.affected_user_rate
        if self.error_count is not None:
            result['errorCount'] = self.error_count
        if self.error_rate is not None:
            result['errorRate'] = self.error_rate
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('affectedUserCount') is not None:
            self.affected_user_count = m.get('affectedUserCount')
        if m.get('affectedUserRate') is not None:
            self.affected_user_rate = m.get('affectedUserRate')
        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')
        if m.get('errorRate') is not None:
            self.error_rate = m.get('errorRate')
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        return self


class GetTodayStatTrendResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetTodayStatTrendResponseBodyData] = None,
        msg: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetTodayStatTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTodayStatTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTodayStatTrendResponseBody = None,
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
            temp_model = GetTodayStatTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class BatchCheckSessionRequestRecords(TeaModel):
    def __init__(
        self,
        custom_session_id: str = None,
        platform_session_id: str = None,
        reference_info: Dict[str, Any] = None,
        type: str = None,
    ):
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id
        self.reference_info = reference_info
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.reference_info is not None:
            result['ReferenceInfo'] = self.reference_info
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('ReferenceInfo') is not None:
            self.reference_info = m.get('ReferenceInfo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class BatchCheckSessionRequest(TeaModel):
    def __init__(
        self,
        records: List[BatchCheckSessionRequestRecords] = None,
    ):
        # This parameter is required.
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = BatchCheckSessionRequestRecords()
                self.records.append(temp_model.from_map(k))
        return self


class BatchCheckSessionShrinkRequest(TeaModel):
    def __init__(
        self,
        records_shrink: str = None,
    ):
        # This parameter is required.
        self.records_shrink = records_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.records_shrink is not None:
            result['Records'] = self.records_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Records') is not None:
            self.records_shrink = m.get('Records')
        return self


class BatchCheckSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchCheckSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCheckSessionResponseBody = None,
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
            temp_model = BatchCheckSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelReserveTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelReserveTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelReserveTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelReserveTaskResponseBody = None,
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
            temp_model = CancelReserveTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAdaptationRequestAdaptTarget(TeaModel):
    def __init__(
        self,
        bit_rate: int = None,
        frame_rate: int = None,
        resolution: str = None,
        start_program: str = None,
    ):
        self.bit_rate = bit_rate
        self.frame_rate = frame_rate
        self.resolution = resolution
        self.start_program = start_program

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.start_program is not None:
            result['StartProgram'] = self.start_program
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('StartProgram') is not None:
            self.start_program = m.get('StartProgram')
        return self


class CreateAdaptationRequest(TeaModel):
    def __init__(
        self,
        adapt_target: CreateAdaptationRequestAdaptTarget = None,
        app_version_id: str = None,
    ):
        self.adapt_target = adapt_target
        # This parameter is required.
        self.app_version_id = app_version_id

    def validate(self):
        if self.adapt_target:
            self.adapt_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_target is not None:
            result['AdaptTarget'] = self.adapt_target.to_map()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptTarget') is not None:
            temp_model = CreateAdaptationRequestAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class CreateAdaptationShrinkRequest(TeaModel):
    def __init__(
        self,
        adapt_target_shrink: str = None,
        app_version_id: str = None,
    ):
        self.adapt_target_shrink = adapt_target_shrink
        # This parameter is required.
        self.app_version_id = app_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_target_shrink is not None:
            result['AdaptTarget'] = self.adapt_target_shrink
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptTarget') is not None:
            self.adapt_target_shrink = m.get('AdaptTarget')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class CreateAdaptationResponseBody(TeaModel):
    def __init__(
        self,
        adapt_apply_id: int = None,
        request_id: str = None,
    ):
        self.adapt_apply_id = adapt_apply_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAdaptationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAdaptationResponseBody = None,
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
            temp_model = CreateAdaptationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        streaming_app_id: str = None,
        streaming_solution: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.app_type = app_type
        self.streaming_app_id = streaming_app_id
        self.streaming_solution = streaming_solution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.streaming_app_id is not None:
            result['StreamingAppId'] = self.streaming_app_id
        if self.streaming_solution is not None:
            result['StreamingSolution'] = self.streaming_solution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('StreamingAppId') is not None:
            self.streaming_app_id = m.get('StreamingAppId')
        if m.get('StreamingSolution') is not None:
            self.streaming_solution = m.get('StreamingSolution')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionRequestStartParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionRequestSystemInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionRequest(TeaModel):
    def __init__(
        self,
        adapter_file_id: str = None,
        app_id: str = None,
        app_version: str = None,
        client_ip: str = None,
        custom_session_id: str = None,
        custom_user_id: str = None,
        district_id: str = None,
        enable_postpaid: bool = None,
        project_id: str = None,
        start_parameters: List[CreateAppSessionRequestStartParameters] = None,
        system_info: List[CreateAppSessionRequestSystemInfo] = None,
        timeout: int = None,
    ):
        # 适配文件ID。此功能灰度开放，如未约定使用请勿传入。
        self.adapter_file_id = adapter_file_id
        # This parameter is required.
        self.app_id = app_id
        self.app_version = app_version
        self.client_ip = client_ip
        # This parameter is required.
        self.custom_session_id = custom_session_id
        self.custom_user_id = custom_user_id
        self.district_id = district_id
        self.enable_postpaid = enable_postpaid
        # 项目ID。如果已将应用关联到项目，创建会话时需填写正确的项目ID。
        self.project_id = project_id
        self.start_parameters = start_parameters
        self.system_info = system_info
        self.timeout = timeout

    def validate(self):
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.system_info:
            for k in self.system_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapter_file_id is not None:
            result['AdapterFileId'] = self.adapter_file_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.enable_postpaid is not None:
            result['EnablePostpaid'] = self.enable_postpaid
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdapterFileId') is not None:
            self.adapter_file_id = m.get('AdapterFileId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('EnablePostpaid') is not None:
            self.enable_postpaid = m.get('EnablePostpaid')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionRequestStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionRequestSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateAppSessionResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppSessionResponseBody = None,
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
            temp_model = CreateAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionBatchRequestAppInfosResultStoreStoreInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionBatchRequestAppInfosResultStore(TeaModel):
    def __init__(
        self,
        need: bool = None,
        store_info: List[CreateAppSessionBatchRequestAppInfosResultStoreStoreInfo] = None,
        type: str = None,
    ):
        self.need = need
        self.store_info = store_info
        self.type = type

    def validate(self):
        if self.store_info:
            for k in self.store_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need is not None:
            result['Need'] = self.need
        result['StoreInfo'] = []
        if self.store_info is not None:
            for k in self.store_info:
                result['StoreInfo'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Need') is not None:
            self.need = m.get('Need')
        self.store_info = []
        if m.get('StoreInfo') is not None:
            for k in m.get('StoreInfo'):
                temp_model = CreateAppSessionBatchRequestAppInfosResultStoreStoreInfo()
                self.store_info.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppSessionBatchRequestAppInfosStartParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionBatchRequestAppInfosSystemInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionBatchRequestAppInfos(TeaModel):
    def __init__(
        self,
        adapter_file_id: str = None,
        app_id: str = None,
        app_version: str = None,
        client_ip: str = None,
        custom_user_id: str = None,
        customer_session_id: str = None,
        dataset_id: str = None,
        district_id: str = None,
        project_id: str = None,
        result_store: CreateAppSessionBatchRequestAppInfosResultStore = None,
        start_parameters: List[CreateAppSessionBatchRequestAppInfosStartParameters] = None,
        system_info: List[CreateAppSessionBatchRequestAppInfosSystemInfo] = None,
    ):
        self.adapter_file_id = adapter_file_id
        # This parameter is required.
        self.app_id = app_id
        self.app_version = app_version
        self.client_ip = client_ip
        self.custom_user_id = custom_user_id
        # This parameter is required.
        self.customer_session_id = customer_session_id
        self.dataset_id = dataset_id
        self.district_id = district_id
        self.project_id = project_id
        self.result_store = result_store
        self.start_parameters = start_parameters
        self.system_info = system_info

    def validate(self):
        if self.result_store:
            self.result_store.validate()
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.system_info:
            for k in self.system_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapter_file_id is not None:
            result['AdapterFileId'] = self.adapter_file_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.customer_session_id is not None:
            result['CustomerSessionId'] = self.customer_session_id
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.result_store is not None:
            result['ResultStore'] = self.result_store.to_map()
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdapterFileId') is not None:
            self.adapter_file_id = m.get('AdapterFileId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('CustomerSessionId') is not None:
            self.customer_session_id = m.get('CustomerSessionId')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResultStore') is not None:
            temp_model = CreateAppSessionBatchRequestAppInfosResultStore()
            self.result_store = temp_model.from_map(m['ResultStore'])
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionBatchRequestAppInfosStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionBatchRequestAppInfosSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        return self


class CreateAppSessionBatchRequest(TeaModel):
    def __init__(
        self,
        app_infos: List[CreateAppSessionBatchRequestAppInfos] = None,
        custom_task_id: str = None,
        timeout: int = None,
    ):
        # This parameter is required.
        self.app_infos = app_infos
        # This parameter is required.
        self.custom_task_id = custom_task_id
        # This parameter is required.
        self.timeout = timeout

    def validate(self):
        if self.app_infos:
            for k in self.app_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfos'] = []
        if self.app_infos is not None:
            for k in self.app_infos:
                result['AppInfos'].append(k.to_map() if k else None)
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_infos = []
        if m.get('AppInfos') is not None:
            for k in m.get('AppInfos'):
                temp_model = CreateAppSessionBatchRequestAppInfos()
                self.app_infos.append(temp_model.from_map(k))
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateAppSessionBatchShrinkRequest(TeaModel):
    def __init__(
        self,
        app_infos_shrink: str = None,
        custom_task_id: str = None,
        timeout: int = None,
    ):
        # This parameter is required.
        self.app_infos_shrink = app_infos_shrink
        # This parameter is required.
        self.custom_task_id = custom_task_id
        # This parameter is required.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_infos_shrink is not None:
            result['AppInfos'] = self.app_infos_shrink
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfos') is not None:
            self.app_infos_shrink = m.get('AppInfos')
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateAppSessionBatchResponseBody(TeaModel):
    def __init__(
        self,
        custom_task_id: str = None,
        platform_task_id: str = None,
        request_id: str = None,
    ):
        self.custom_task_id = custom_task_id
        self.platform_task_id = platform_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.platform_task_id is not None:
            result['PlatformTaskId'] = self.platform_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('PlatformTaskId') is not None:
            self.platform_task_id = m.get('PlatformTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppSessionBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppSessionBatchResponseBody = None,
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
            temp_model = CreateAppSessionBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionBatchSyncRequestAppInfosMatchRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.type = type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateAppSessionBatchSyncRequestAppInfosStartParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionBatchSyncRequestAppInfosSystemInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionBatchSyncRequestAppInfosTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionBatchSyncRequestAppInfos(TeaModel):
    def __init__(
        self,
        adapter_file_id: str = None,
        app_id: str = None,
        app_version: str = None,
        client_ip: str = None,
        custom_user_id: str = None,
        customer_session_id: str = None,
        district_id: str = None,
        match_rules: List[CreateAppSessionBatchSyncRequestAppInfosMatchRules] = None,
        project_id: str = None,
        start_parameters: List[CreateAppSessionBatchSyncRequestAppInfosStartParameters] = None,
        system_info: List[CreateAppSessionBatchSyncRequestAppInfosSystemInfo] = None,
        tags: List[CreateAppSessionBatchSyncRequestAppInfosTags] = None,
    ):
        self.adapter_file_id = adapter_file_id
        # This parameter is required.
        self.app_id = app_id
        self.app_version = app_version
        self.client_ip = client_ip
        self.custom_user_id = custom_user_id
        # This parameter is required.
        self.customer_session_id = customer_session_id
        self.district_id = district_id
        self.match_rules = match_rules
        self.project_id = project_id
        self.start_parameters = start_parameters
        self.system_info = system_info
        self.tags = tags

    def validate(self):
        if self.match_rules:
            for k in self.match_rules:
                if k:
                    k.validate()
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.system_info:
            for k in self.system_info:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapter_file_id is not None:
            result['AdapterFileId'] = self.adapter_file_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.customer_session_id is not None:
            result['CustomerSessionId'] = self.customer_session_id
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        result['MatchRules'] = []
        if self.match_rules is not None:
            for k in self.match_rules:
                result['MatchRules'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdapterFileId') is not None:
            self.adapter_file_id = m.get('AdapterFileId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('CustomerSessionId') is not None:
            self.customer_session_id = m.get('CustomerSessionId')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        self.match_rules = []
        if m.get('MatchRules') is not None:
            for k in m.get('MatchRules'):
                temp_model = CreateAppSessionBatchSyncRequestAppInfosMatchRules()
                self.match_rules.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionBatchSyncRequestAppInfosStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionBatchSyncRequestAppInfosSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateAppSessionBatchSyncRequestAppInfosTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateAppSessionBatchSyncRequest(TeaModel):
    def __init__(
        self,
        app_infos: List[CreateAppSessionBatchSyncRequestAppInfos] = None,
        batch_id: str = None,
    ):
        # This parameter is required.
        self.app_infos = app_infos
        # This parameter is required.
        self.batch_id = batch_id

    def validate(self):
        if self.app_infos:
            for k in self.app_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfos'] = []
        if self.app_infos is not None:
            for k in self.app_infos:
                result['AppInfos'].append(k.to_map() if k else None)
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_infos = []
        if m.get('AppInfos') is not None:
            for k in m.get('AppInfos'):
                temp_model = CreateAppSessionBatchSyncRequestAppInfos()
                self.app_infos.append(temp_model.from_map(k))
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class CreateAppSessionBatchSyncShrinkRequest(TeaModel):
    def __init__(
        self,
        app_infos_shrink: str = None,
        batch_id: str = None,
    ):
        # This parameter is required.
        self.app_infos_shrink = app_infos_shrink
        # This parameter is required.
        self.batch_id = batch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_infos_shrink is not None:
            result['AppInfos'] = self.app_infos_shrink
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfos') is not None:
            self.app_infos_shrink = m.get('AppInfos')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class CreateAppSessionBatchSyncResponseBodyFailedListFailedInfo(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class CreateAppSessionBatchSyncResponseBodyFailedList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        custom_session_id: str = None,
        failed_info: CreateAppSessionBatchSyncResponseBodyFailedListFailedInfo = None,
    ):
        self.app_id = app_id
        self.custom_session_id = custom_session_id
        self.failed_info = failed_info

    def validate(self):
        if self.failed_info:
            self.failed_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.failed_info is not None:
            result['FailedInfo'] = self.failed_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('FailedInfo') is not None:
            temp_model = CreateAppSessionBatchSyncResponseBodyFailedListFailedInfo()
            self.failed_info = temp_model.from_map(m['FailedInfo'])
        return self


class CreateAppSessionBatchSyncResponseBodyResultListBizInfoEndpoints(TeaModel):
    def __init__(
        self,
        access_host: str = None,
        access_port: str = None,
        district_id: str = None,
        isp: str = None,
        name: str = None,
        type: str = None,
    ):
        self.access_host = access_host
        self.access_port = access_port
        self.district_id = district_id
        self.isp = isp
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_host is not None:
            result['AccessHost'] = self.access_host
        if self.access_port is not None:
            result['AccessPort'] = self.access_port
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessHost') is not None:
            self.access_host = m.get('AccessHost')
        if m.get('AccessPort') is not None:
            self.access_port = m.get('AccessPort')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppSessionBatchSyncResponseBodyResultListBizInfo(TeaModel):
    def __init__(
        self,
        biz: Dict[str, Any] = None,
        endpoints: List[CreateAppSessionBatchSyncResponseBodyResultListBizInfoEndpoints] = None,
    ):
        self.biz = biz
        self.endpoints = endpoints

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz is not None:
            result['Biz'] = self.biz
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = CreateAppSessionBatchSyncResponseBodyResultListBizInfoEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        return self


class CreateAppSessionBatchSyncResponseBodyResultList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        biz_info: CreateAppSessionBatchSyncResponseBodyResultListBizInfo = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.biz_info = biz_info
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id

    def validate(self):
        if self.biz_info:
            self.biz_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_info is not None:
            result['BizInfo'] = self.biz_info.to_map()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BizInfo') is not None:
            temp_model = CreateAppSessionBatchSyncResponseBodyResultListBizInfo()
            self.biz_info = temp_model.from_map(m['BizInfo'])
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        return self


class CreateAppSessionBatchSyncResponseBody(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        failed_list: List[CreateAppSessionBatchSyncResponseBodyFailedList] = None,
        request_id: str = None,
        result_list: List[CreateAppSessionBatchSyncResponseBodyResultList] = None,
    ):
        self.batch_id = batch_id
        self.failed_list = failed_list
        self.request_id = request_id
        self.result_list = result_list

    def validate(self):
        if self.failed_list:
            for k in self.failed_list:
                if k:
                    k.validate()
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        result['FailedList'] = []
        if self.failed_list is not None:
            for k in self.failed_list:
                result['FailedList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        self.failed_list = []
        if m.get('FailedList') is not None:
            for k in m.get('FailedList'):
                temp_model = CreateAppSessionBatchSyncResponseBodyFailedList()
                self.failed_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = CreateAppSessionBatchSyncResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class CreateAppSessionBatchSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppSessionBatchSyncResponseBody = None,
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
            temp_model = CreateAppSessionBatchSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionSyncRequestMatchRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.type = type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateAppSessionSyncRequestStartParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionSyncRequestSystemInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionSyncRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionSyncRequest(TeaModel):
    def __init__(
        self,
        adapter_file_id: str = None,
        app_id: str = None,
        app_version: str = None,
        client_ip: str = None,
        custom_session_id: str = None,
        custom_user_id: str = None,
        district_id: str = None,
        match_rules: List[CreateAppSessionSyncRequestMatchRules] = None,
        project_id: str = None,
        start_parameters: List[CreateAppSessionSyncRequestStartParameters] = None,
        system_info: List[CreateAppSessionSyncRequestSystemInfo] = None,
        tags: List[CreateAppSessionSyncRequestTags] = None,
    ):
        self.adapter_file_id = adapter_file_id
        # This parameter is required.
        self.app_id = app_id
        self.app_version = app_version
        self.client_ip = client_ip
        # This parameter is required.
        self.custom_session_id = custom_session_id
        self.custom_user_id = custom_user_id
        self.district_id = district_id
        self.match_rules = match_rules
        self.project_id = project_id
        self.start_parameters = start_parameters
        self.system_info = system_info
        self.tags = tags

    def validate(self):
        if self.match_rules:
            for k in self.match_rules:
                if k:
                    k.validate()
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.system_info:
            for k in self.system_info:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapter_file_id is not None:
            result['AdapterFileId'] = self.adapter_file_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        result['MatchRules'] = []
        if self.match_rules is not None:
            for k in self.match_rules:
                result['MatchRules'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdapterFileId') is not None:
            self.adapter_file_id = m.get('AdapterFileId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        self.match_rules = []
        if m.get('MatchRules') is not None:
            for k in m.get('MatchRules'):
                temp_model = CreateAppSessionSyncRequestMatchRules()
                self.match_rules.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionSyncRequestStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionSyncRequestSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateAppSessionSyncRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateAppSessionSyncResponseBodyBizInfoEndpoints(TeaModel):
    def __init__(
        self,
        access_host: str = None,
        access_port: str = None,
        district_id: str = None,
        isp: str = None,
        name: str = None,
        type: str = None,
    ):
        self.access_host = access_host
        self.access_port = access_port
        self.district_id = district_id
        self.isp = isp
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_host is not None:
            result['AccessHost'] = self.access_host
        if self.access_port is not None:
            result['AccessPort'] = self.access_port
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessHost') is not None:
            self.access_host = m.get('AccessHost')
        if m.get('AccessPort') is not None:
            self.access_port = m.get('AccessPort')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppSessionSyncResponseBodyBizInfo(TeaModel):
    def __init__(
        self,
        biz: Dict[str, Any] = None,
        endpoints: List[CreateAppSessionSyncResponseBodyBizInfoEndpoints] = None,
    ):
        self.biz = biz
        self.endpoints = endpoints

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz is not None:
            result['Biz'] = self.biz
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = CreateAppSessionSyncResponseBodyBizInfoEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        return self


class CreateAppSessionSyncResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        biz_info: CreateAppSessionSyncResponseBodyBizInfo = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.biz_info = biz_info
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id
        self.request_id = request_id

    def validate(self):
        if self.biz_info:
            self.biz_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_info is not None:
            result['BizInfo'] = self.biz_info.to_map()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BizInfo') is not None:
            temp_model = CreateAppSessionSyncResponseBodyBizInfo()
            self.biz_info = temp_model.from_map(m['BizInfo'])
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppSessionSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppSessionSyncResponseBody = None,
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
            temp_model = CreateAppSessionSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppVersionRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_name: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.app_version_name = app_version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        return self


class CreateAppVersionResponseBody(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
        request_id: str = None,
    ):
        self.app_version_id = app_version_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppVersionResponseBody = None,
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
            temp_model = CreateAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCapacityReservationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        client_token: str = None,
        district_id: str = None,
        expect_resource_ready_time: str = None,
        expect_session_capacity: int = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.app_version = app_version
        self.client_token = client_token
        # This parameter is required.
        self.district_id = district_id
        self.expect_resource_ready_time = expect_resource_ready_time
        # This parameter is required.
        self.expect_session_capacity = expect_session_capacity
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.expect_resource_ready_time is not None:
            result['ExpectResourceReadyTime'] = self.expect_resource_ready_time
        if self.expect_session_capacity is not None:
            result['ExpectSessionCapacity'] = self.expect_session_capacity
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ExpectResourceReadyTime') is not None:
            self.expect_resource_ready_time = m.get('ExpectResourceReadyTime')
        if m.get('ExpectSessionCapacity') is not None:
            self.expect_session_capacity = m.get('ExpectSessionCapacity')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateCapacityReservationResponseBody(TeaModel):
    def __init__(
        self,
        curr_max_allocatable_session_capacity: int = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.curr_max_allocatable_session_capacity = curr_max_allocatable_session_capacity
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_max_allocatable_session_capacity is not None:
            result['CurrMaxAllocatableSessionCapacity'] = self.curr_max_allocatable_session_capacity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrMaxAllocatableSessionCapacity') is not None:
            self.curr_max_allocatable_session_capacity = m.get('CurrMaxAllocatableSessionCapacity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateCapacityReservationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCapacityReservationResponseBody = None,
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
            temp_model = CreateCapacityReservationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppResponseBody = None,
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppVersionRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
    ):
        # This parameter is required.
        self.app_version_id = app_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class DeleteAppVersionResponseBody(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
        request_id: str = None,
    ):
        self.app_version_id = app_version_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppVersionResponseBody = None,
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
            temp_model = DeleteAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAdaptationRequest(TeaModel):
    def __init__(
        self,
        adapt_apply_id: int = None,
        app_version_id: str = None,
    ):
        self.adapt_apply_id = adapt_apply_id
        self.app_version_id = app_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class GetAdaptationResponseBodyAdaptTarget(TeaModel):
    def __init__(
        self,
        bit_rate: int = None,
        frame_rate: int = None,
        resolution: str = None,
        start_program: str = None,
    ):
        self.bit_rate = bit_rate
        self.frame_rate = frame_rate
        self.resolution = resolution
        self.start_program = start_program

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.start_program is not None:
            result['StartProgram'] = self.start_program
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('StartProgram') is not None:
            self.start_program = m.get('StartProgram')
        return self


class GetAdaptationResponseBody(TeaModel):
    def __init__(
        self,
        adapt_apply_id: int = None,
        adapt_target: GetAdaptationResponseBodyAdaptTarget = None,
        app_id: str = None,
        app_version_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        request_id: str = None,
    ):
        self.adapt_apply_id = adapt_apply_id
        self.adapt_target = adapt_target
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.request_id = request_id

    def validate(self):
        if self.adapt_target:
            self.adapt_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        if self.adapt_target is not None:
            result['AdaptTarget'] = self.adapt_target.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        if m.get('AdaptTarget') is not None:
            temp_model = GetAdaptationResponseBodyAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAdaptationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAdaptationResponseBody = None,
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
            temp_model = GetAdaptationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        request_id: str = None,
        streaming_app_id: str = None,
        streaming_solution: str = None,
        version_adapt_num: int = None,
        version_total_num: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_type = app_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.request_id = request_id
        self.streaming_app_id = streaming_app_id
        self.streaming_solution = streaming_solution
        self.version_adapt_num = version_adapt_num
        self.version_total_num = version_total_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.streaming_app_id is not None:
            result['StreamingAppId'] = self.streaming_app_id
        if self.streaming_solution is not None:
            result['StreamingSolution'] = self.streaming_solution
        if self.version_adapt_num is not None:
            result['VersionAdaptNum'] = self.version_adapt_num
        if self.version_total_num is not None:
            result['VersionTotalNum'] = self.version_total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StreamingAppId') is not None:
            self.streaming_app_id = m.get('StreamingAppId')
        if m.get('StreamingSolution') is not None:
            self.streaming_solution = m.get('StreamingSolution')
        if m.get('VersionAdaptNum') is not None:
            self.version_adapt_num = m.get('VersionAdaptNum')
        if m.get('VersionTotalNum') is not None:
            self.version_total_num = m.get('VersionTotalNum')
        return self


class GetAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppResponseBody = None,
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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppCcuRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        project_id: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetAppCcuResponseBodyDetailList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        ccu: str = None,
        district_id: str = None,
        project_id: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.ccu = ccu
        self.district_id = district_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.ccu is not None:
            result['Ccu'] = self.ccu
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Ccu') is not None:
            self.ccu = m.get('Ccu')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetAppCcuResponseBody(TeaModel):
    def __init__(
        self,
        detail_list: List[GetAppCcuResponseBodyDetailList] = None,
        request_id: str = None,
        timestamp: str = None,
    ):
        self.detail_list = detail_list
        self.request_id = request_id
        self.timestamp = timestamp

    def validate(self):
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetailList'] = []
        if self.detail_list is not None:
            for k in self.detail_list:
                result['DetailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_list = []
        if m.get('DetailList') is not None:
            for k in m.get('DetailList'):
                temp_model = GetAppCcuResponseBodyDetailList()
                self.detail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetAppCcuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppCcuResponseBody = None,
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
            temp_model = GetAppCcuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppSessionRequest(TeaModel):
    def __init__(
        self,
        custom_session_id: str = None,
        platform_session_id: str = None,
    ):
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        return self


class GetAppSessionResponseBodyBizInfo(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        stop_time: str = None,
    ):
        # 会话启动时间
        self.start_time = start_time
        # 会话停止时间
        self.stop_time = stop_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        return self


class GetAppSessionResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        biz_info: GetAppSessionResponseBodyBizInfo = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        # 业务特定的信息，如会话启动/停止时间。
        self.biz_info = biz_info
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.biz_info:
            self.biz_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_info is not None:
            result['BizInfo'] = self.biz_info.to_map()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BizInfo') is not None:
            temp_model = GetAppSessionResponseBodyBizInfo()
            self.biz_info = temp_model.from_map(m['BizInfo'])
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAppSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppSessionResponseBody = None,
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
            temp_model = GetAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppVersionRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
    ):
        # This parameter is required.
        self.app_version_id = app_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class GetAppVersionResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
        app_version_name: str = None,
        app_version_status: str = None,
        app_version_status_memo: str = None,
        consume_cu: float = None,
        file_address: str = None,
        file_size: int = None,
        file_upload_finish_time: str = None,
        file_upload_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.app_version_name = app_version_name
        self.app_version_status = app_version_status
        self.app_version_status_memo = app_version_status_memo
        self.consume_cu = consume_cu
        self.file_address = file_address
        self.file_size = file_size
        self.file_upload_finish_time = file_upload_finish_time
        self.file_upload_type = file_upload_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.app_version_status is not None:
            result['AppVersionStatus'] = self.app_version_status
        if self.app_version_status_memo is not None:
            result['AppVersionStatusMemo'] = self.app_version_status_memo
        if self.consume_cu is not None:
            result['ConsumeCu'] = self.consume_cu
        if self.file_address is not None:
            result['FileAddress'] = self.file_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_upload_finish_time is not None:
            result['FileUploadFinishTime'] = self.file_upload_finish_time
        if self.file_upload_type is not None:
            result['FileUploadType'] = self.file_upload_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('AppVersionStatus') is not None:
            self.app_version_status = m.get('AppVersionStatus')
        if m.get('AppVersionStatusMemo') is not None:
            self.app_version_status_memo = m.get('AppVersionStatusMemo')
        if m.get('ConsumeCu') is not None:
            self.consume_cu = m.get('ConsumeCu')
        if m.get('FileAddress') is not None:
            self.file_address = m.get('FileAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUploadFinishTime') is not None:
            self.file_upload_finish_time = m.get('FileUploadFinishTime')
        if m.get('FileUploadType') is not None:
            self.file_upload_type = m.get('FileUploadType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppVersionResponseBody = None,
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
            temp_model = GetAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCapacityRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        district_id: str = None,
        page_num: int = None,
        page_size: int = None,
        project_id: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.district_id = district_id
        self.page_num = page_num
        self.page_size = page_size
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetCapacityResponseBodyCapacities(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        district_id: str = None,
        project_id: str = None,
        session_capacity: int = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.district_id = district_id
        self.project_id = project_id
        self.session_capacity = session_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.session_capacity is not None:
            result['SessionCapacity'] = self.session_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SessionCapacity') is not None:
            self.session_capacity = m.get('SessionCapacity')
        return self


class GetCapacityResponseBody(TeaModel):
    def __init__(
        self,
        capacities: List[GetCapacityResponseBodyCapacities] = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.capacities = capacities
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.capacities:
            for k in self.capacities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Capacities'] = []
        if self.capacities is not None:
            for k in self.capacities:
                result['Capacities'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.capacities = []
        if m.get('Capacities') is not None:
            for k in m.get('Capacities'):
                temp_model = GetCapacityResponseBodyCapacities()
                self.capacities.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetCapacityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCapacityResponseBody = None,
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
            temp_model = GetCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReserveTaskDetailRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
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


class GetReserveTaskDetailResponseBodyResBatchList(TeaModel):
    def __init__(
        self,
        res_batch_id: str = None,
        res_batch_tag_name: str = None,
    ):
        self.res_batch_id = res_batch_id
        self.res_batch_tag_name = res_batch_tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_batch_id is not None:
            result['ResBatchId'] = self.res_batch_id
        if self.res_batch_tag_name is not None:
            result['ResBatchTagName'] = self.res_batch_tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResBatchId') is not None:
            self.res_batch_id = m.get('ResBatchId')
        if m.get('ResBatchTagName') is not None:
            self.res_batch_tag_name = m.get('ResBatchTagName')
        return self


class GetReserveTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        curr_completed_session_capacity: int = None,
        district_id: str = None,
        expect_resource_ready_time: str = None,
        expect_session_capacity: int = None,
        project_id: str = None,
        request_id: str = None,
        res_batch_list: List[GetReserveTaskDetailResponseBodyResBatchList] = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.curr_completed_session_capacity = curr_completed_session_capacity
        self.district_id = district_id
        self.expect_resource_ready_time = expect_resource_ready_time
        self.expect_session_capacity = expect_session_capacity
        self.project_id = project_id
        self.request_id = request_id
        self.res_batch_list = res_batch_list
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        if self.res_batch_list:
            for k in self.res_batch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.curr_completed_session_capacity is not None:
            result['CurrCompletedSessionCapacity'] = self.curr_completed_session_capacity
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.expect_resource_ready_time is not None:
            result['ExpectResourceReadyTime'] = self.expect_resource_ready_time
        if self.expect_session_capacity is not None:
            result['ExpectSessionCapacity'] = self.expect_session_capacity
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResBatchList'] = []
        if self.res_batch_list is not None:
            for k in self.res_batch_list:
                result['ResBatchList'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CurrCompletedSessionCapacity') is not None:
            self.curr_completed_session_capacity = m.get('CurrCompletedSessionCapacity')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ExpectResourceReadyTime') is not None:
            self.expect_resource_ready_time = m.get('ExpectResourceReadyTime')
        if m.get('ExpectSessionCapacity') is not None:
            self.expect_session_capacity = m.get('ExpectSessionCapacity')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.res_batch_list = []
        if m.get('ResBatchList') is not None:
            for k in m.get('ResBatchList'):
                temp_model = GetReserveTaskDetailResponseBodyResBatchList()
                self.res_batch_list.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetReserveTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetReserveTaskDetailResponseBody = None,
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
            temp_model = GetReserveTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcePublicIPsRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        project_id: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetResourcePublicIPsResponseBodyIpList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        project_id: str = None,
    ):
        self.ip = ip
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetResourcePublicIPsResponseBody(TeaModel):
    def __init__(
        self,
        ip_list: List[GetResourcePublicIPsResponseBodyIpList] = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.ip_list = ip_list
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_list = []
        if m.get('IpList') is not None:
            for k in m.get('IpList'):
                temp_model = GetResourcePublicIPsResponseBodyIpList()
                self.ip_list.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetResourcePublicIPsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourcePublicIPsResponseBody = None,
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
            temp_model = GetResourcePublicIPsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppRequest(TeaModel):
    def __init__(
        self,
        key_search: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.key_search = key_search
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_search is not None:
            result['KeySearch'] = self.key_search
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeySearch') is not None:
            self.key_search = m.get('KeySearch')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppResponseBodyApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        version_adapt_num: int = None,
        version_total_num: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_type = app_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.version_adapt_num = version_adapt_num
        self.version_total_num = version_total_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.version_adapt_num is not None:
            result['VersionAdaptNum'] = self.version_adapt_num
        if self.version_total_num is not None:
            result['VersionTotalNum'] = self.version_total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('VersionAdaptNum') is not None:
            self.version_adapt_num = m.get('VersionAdaptNum')
        if m.get('VersionTotalNum') is not None:
            self.version_total_num = m.get('VersionTotalNum')
        return self


class ListAppResponseBody(TeaModel):
    def __init__(
        self,
        apps: List[ListAppResponseBodyApps] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.apps = apps
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListAppResponseBodyApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppResponseBody = None,
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
            temp_model = ListAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppSessionsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        custom_session_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        platform_session_ids: List[str] = None,
        project_id: str = None,
    ):
        self.app_id = app_id
        self.custom_session_ids = custom_session_ids
        self.page_number = page_number
        self.page_size = page_size
        self.platform_session_ids = platform_session_ids
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.custom_session_ids is not None:
            result['CustomSessionIds'] = self.custom_session_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform_session_ids is not None:
            result['PlatformSessionIds'] = self.platform_session_ids
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CustomSessionIds') is not None:
            self.custom_session_ids = m.get('CustomSessionIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlatformSessionIds') is not None:
            self.platform_session_ids = m.get('PlatformSessionIds')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListAppSessionsResponseBodyAppSessionsBizInfo(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        stop_time: str = None,
    ):
        # 会话启动时间
        self.start_time = start_time
        # 会话停止时间
        self.stop_time = stop_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        return self


class ListAppSessionsResponseBodyAppSessions(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        biz_info: ListAppSessionsResponseBodyAppSessionsBizInfo = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        project_id: str = None,
        status: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        # 业务特定的信息，如会话启动/停止时间。
        self.biz_info = biz_info
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id
        self.project_id = project_id
        self.status = status

    def validate(self):
        if self.biz_info:
            self.biz_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_info is not None:
            result['BizInfo'] = self.biz_info.to_map()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BizInfo') is not None:
            temp_model = ListAppSessionsResponseBodyAppSessionsBizInfo()
            self.biz_info = temp_model.from_map(m['BizInfo'])
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppSessionsResponseBody(TeaModel):
    def __init__(
        self,
        app_sessions: List[ListAppSessionsResponseBodyAppSessions] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.app_sessions = app_sessions
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.app_sessions:
            for k in self.app_sessions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppSessions'] = []
        if self.app_sessions is not None:
            for k in self.app_sessions:
                result['AppSessions'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_sessions = []
        if m.get('AppSessions') is not None:
            for k in m.get('AppSessions'):
                temp_model = ListAppSessionsResponseBodyAppSessions()
                self.app_sessions.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppSessionsResponseBody = None,
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
            temp_model = ListAppSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppVersionRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppVersionResponseBodyVersions(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
        app_version_name: str = None,
        app_version_status: str = None,
        app_version_status_memo: str = None,
        consume_cu: float = None,
        file_address: str = None,
        file_size: int = None,
        file_upload_finish_time: str = None,
        file_upload_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
    ):
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.app_version_name = app_version_name
        self.app_version_status = app_version_status
        self.app_version_status_memo = app_version_status_memo
        self.consume_cu = consume_cu
        self.file_address = file_address
        self.file_size = file_size
        self.file_upload_finish_time = file_upload_finish_time
        self.file_upload_type = file_upload_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.app_version_status is not None:
            result['AppVersionStatus'] = self.app_version_status
        if self.app_version_status_memo is not None:
            result['AppVersionStatusMemo'] = self.app_version_status_memo
        if self.consume_cu is not None:
            result['ConsumeCu'] = self.consume_cu
        if self.file_address is not None:
            result['FileAddress'] = self.file_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_upload_finish_time is not None:
            result['FileUploadFinishTime'] = self.file_upload_finish_time
        if self.file_upload_type is not None:
            result['FileUploadType'] = self.file_upload_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('AppVersionStatus') is not None:
            self.app_version_status = m.get('AppVersionStatus')
        if m.get('AppVersionStatusMemo') is not None:
            self.app_version_status_memo = m.get('AppVersionStatusMemo')
        if m.get('ConsumeCu') is not None:
            self.consume_cu = m.get('ConsumeCu')
        if m.get('FileAddress') is not None:
            self.file_address = m.get('FileAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUploadFinishTime') is not None:
            self.file_upload_finish_time = m.get('FileUploadFinishTime')
        if m.get('FileUploadType') is not None:
            self.file_upload_type = m.get('FileUploadType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class ListAppVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        versions: List[ListAppVersionResponseBodyVersions] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListAppVersionResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListAppVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppVersionResponseBody = None,
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
            temp_model = ListAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        district_id: str = None,
        instance_id: List[str] = None,
        instance_type: str = None,
        max_results: int = None,
        next_token: str = None,
        project_id: str = None,
        status: str = None,
    ):
        self.district_id = district_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.max_results = max_results
        self.next_token = next_token
        self.project_id = project_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        district_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        project_id: str = None,
        status: str = None,
    ):
        self.creation_time = creation_time
        self.district_id = district_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.project_id = project_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyInstances] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.instances = instances
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ModifyAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppResponseBody = None,
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
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppVersionRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
        app_version_name: str = None,
    ):
        # This parameter is required.
        self.app_version_id = app_version_id
        # This parameter is required.
        self.app_version_name = app_version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        return self


class ModifyAppVersionResponseBody(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
        request_id: str = None,
    ):
        self.app_version_id = app_version_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppVersionResponseBody = None,
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
            temp_model = ModifyAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseCapacityRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        district_id: str = None,
        expect_release_session_capacity: int = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.app_version = app_version
        # This parameter is required.
        self.district_id = district_id
        # This parameter is required.
        self.expect_release_session_capacity = expect_release_session_capacity
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.expect_release_session_capacity is not None:
            result['ExpectReleaseSessionCapacity'] = self.expect_release_session_capacity
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ExpectReleaseSessionCapacity') is not None:
            self.expect_release_session_capacity = m.get('ExpectReleaseSessionCapacity')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ReleaseCapacityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ReleaseCapacityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseCapacityResponseBody = None,
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
            temp_model = ReleaseCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseCapacityByBatchRequest(TeaModel):
    def __init__(
        self,
        res_batch_id: str = None,
    ):
        # This parameter is required.
        self.res_batch_id = res_batch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_batch_id is not None:
            result['ResBatchId'] = self.res_batch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResBatchId') is not None:
            self.res_batch_id = m.get('ResBatchId')
        return self


class ReleaseCapacityByBatchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseCapacityByBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseCapacityByBatchResponseBody = None,
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
            temp_model = ReleaseCapacityByBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancesRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        district_id: str = None,
        instance_type: str = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.amount = amount
        # This parameter is required.
        self.district_id = district_id
        # This parameter is required.
        self.instance_type = instance_type
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ReleaseInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        request_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseInstancesResponseBody = None,
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
            temp_model = ReleaseInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReserveInstancesRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        district_id: str = None,
        instance_type: str = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.amount = amount
        # This parameter is required.
        self.district_id = district_id
        # This parameter is required.
        self.instance_type = instance_type
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ReserveInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        request_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReserveInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReserveInstancesResponseBody = None,
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
            temp_model = ReserveInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendBizCocChangeCallbackRequest(TeaModel):
    def __init__(
        self,
        platform_session_id: str = None,
        result: bool = None,
    ):
        self.platform_session_id = platform_session_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SendBizCocChangeCallbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendBizCocChangeCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendBizCocChangeCallbackResponseBody = None,
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
            temp_model = SendBizCocChangeCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppSessionRequestStopParam(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: Any = None,
    ):
        # 目前支持的枚举值包括：
        # - reason：停止原因。
        self.key = key
        # key对应的取值。
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class StopAppSessionRequest(TeaModel):
    def __init__(
        self,
        custom_session_id: str = None,
        platform_session_id: str = None,
        stop_param: List[StopAppSessionRequestStopParam] = None,
    ):
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id
        # 停止容器参数。此参数将透传到Agent。
        self.stop_param = stop_param

    def validate(self):
        if self.stop_param:
            for k in self.stop_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        result['StopParam'] = []
        if self.stop_param is not None:
            for k in self.stop_param:
                result['StopParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        self.stop_param = []
        if m.get('StopParam') is not None:
            for k in m.get('StopParam'):
                temp_model = StopAppSessionRequestStopParam()
                self.stop_param.append(temp_model.from_map(k))
        return self


class StopAppSessionShrinkRequest(TeaModel):
    def __init__(
        self,
        custom_session_id: str = None,
        platform_session_id: str = None,
        stop_param_shrink: str = None,
    ):
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id
        # 停止容器参数。此参数将透传到Agent。
        self.stop_param_shrink = stop_param_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.stop_param_shrink is not None:
            result['StopParam'] = self.stop_param_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('StopParam') is not None:
            self.stop_param_shrink = m.get('StopParam')
        return self


class StopAppSessionResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAppSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopAppSessionResponseBody = None,
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
            temp_model = StopAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppSessionBatchRequestStopParam(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: Any = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class StopAppSessionBatchRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class StopAppSessionBatchRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        batch_id: str = None,
        project_id: str = None,
        stop_param: List[StopAppSessionBatchRequestStopParam] = None,
        tags: List[StopAppSessionBatchRequestTags] = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        # This parameter is required.
        self.batch_id = batch_id
        self.project_id = project_id
        self.stop_param = stop_param
        self.tags = tags

    def validate(self):
        if self.stop_param:
            for k in self.stop_param:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['StopParam'] = []
        if self.stop_param is not None:
            for k in self.stop_param:
                result['StopParam'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.stop_param = []
        if m.get('StopParam') is not None:
            for k in m.get('StopParam'):
                temp_model = StopAppSessionBatchRequestStopParam()
                self.stop_param.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = StopAppSessionBatchRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class StopAppSessionBatchShrinkRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class StopAppSessionBatchShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        batch_id: str = None,
        project_id: str = None,
        stop_param_shrink: str = None,
        tags: List[StopAppSessionBatchShrinkRequestTags] = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        # This parameter is required.
        self.batch_id = batch_id
        self.project_id = project_id
        self.stop_param_shrink = stop_param_shrink
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.stop_param_shrink is not None:
            result['StopParam'] = self.stop_param_shrink
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StopParam') is not None:
            self.stop_param_shrink = m.get('StopParam')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = StopAppSessionBatchShrinkRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class StopAppSessionBatchResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        batch_id: str = None,
        project_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.batch_id = batch_id
        self.project_id = project_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAppSessionBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopAppSessionBatchResponseBody = None,
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
            temp_model = StopAppSessionBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSessionBizStatusRequest(TeaModel):
    def __init__(
        self,
        biz_status: str = None,
        platform_session_id: str = None,
    ):
        self.biz_status = biz_status
        # This parameter is required.
        self.platform_session_id = platform_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        return self


class UpdateSessionBizStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        custom_session_id: str = None,
        platform_session_id: str = None,
    ):
        self.custom_session_id = custom_session_id
        self.platform_session_id = platform_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        return self


class UpdateSessionBizStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateSessionBizStatusResponseBodyData = None,
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
            temp_model = UpdateSessionBizStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSessionBizStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSessionBizStatusResponseBody = None,
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
            temp_model = UpdateSessionBizStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



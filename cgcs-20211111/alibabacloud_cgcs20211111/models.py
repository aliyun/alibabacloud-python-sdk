# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


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
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.adapt_apply_id = adapt_apply_id
        self.code = code
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
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = CreateAdaptationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_id = app_id
        self.code = code
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionRequestResultStoreStoreInfo(TeaModel):
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


class CreateAppSessionRequestResultStore(TeaModel):
    def __init__(
        self,
        need: bool = None,
        store_info: List[CreateAppSessionRequestResultStoreStoreInfo] = None,
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
                temp_model = CreateAppSessionRequestResultStoreStoreInfo()
                self.store_info.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppSessionRequestStartParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # key
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


class CreateAppSessionRequestStartParametersV2(TeaModel):
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
        app_id: str = None,
        app_version: str = None,
        client_ip: str = None,
        custom_session_id: str = None,
        custom_user_id: str = None,
        dataset_id: str = None,
        enable_postpaid: bool = None,
        result_store: CreateAppSessionRequestResultStore = None,
        start_parameters: List[CreateAppSessionRequestStartParameters] = None,
        start_parameters_v2: List[CreateAppSessionRequestStartParametersV2] = None,
        system_info: List[CreateAppSessionRequestSystemInfo] = None,
        timeout: int = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        # 客户端ip
        self.client_ip = client_ip
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 自定义用户id
        self.custom_user_id = custom_user_id
        self.dataset_id = dataset_id
        self.enable_postpaid = enable_postpaid
        self.result_store = result_store
        # 启动参数
        self.start_parameters = start_parameters
        self.start_parameters_v2 = start_parameters_v2
        # 系统信息：如端侧机型等信息
        self.system_info = system_info
        self.timeout = timeout

    def validate(self):
        if self.result_store:
            self.result_store.validate()
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.start_parameters_v2:
            for k in self.start_parameters_v2:
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
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.enable_postpaid is not None:
            result['EnablePostpaid'] = self.enable_postpaid
        if self.result_store is not None:
            result['ResultStore'] = self.result_store.to_map()
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['StartParametersV2'] = []
        if self.start_parameters_v2 is not None:
            for k in self.start_parameters_v2:
                result['StartParametersV2'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('EnablePostpaid') is not None:
            self.enable_postpaid = m.get('EnablePostpaid')
        if m.get('ResultStore') is not None:
            temp_model = CreateAppSessionRequestResultStore()
            self.result_store = temp_model.from_map(m['ResultStore'])
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionRequestStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.start_parameters_v2 = []
        if m.get('StartParametersV2') is not None:
            for k in m.get('StartParametersV2'):
                temp_model = CreateAppSessionRequestStartParametersV2()
                self.start_parameters_v2.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionRequestSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateAppSessionShrinkRequestStartParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # key
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


class CreateAppSessionShrinkRequestSystemInfo(TeaModel):
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


class CreateAppSessionShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        client_ip: str = None,
        custom_session_id: str = None,
        custom_user_id: str = None,
        dataset_id: str = None,
        enable_postpaid: bool = None,
        result_store_shrink: str = None,
        start_parameters: List[CreateAppSessionShrinkRequestStartParameters] = None,
        start_parameters_v2shrink: str = None,
        system_info: List[CreateAppSessionShrinkRequestSystemInfo] = None,
        timeout: int = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        # 客户端ip
        self.client_ip = client_ip
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 自定义用户id
        self.custom_user_id = custom_user_id
        self.dataset_id = dataset_id
        self.enable_postpaid = enable_postpaid
        self.result_store_shrink = result_store_shrink
        # 启动参数
        self.start_parameters = start_parameters
        self.start_parameters_v2shrink = start_parameters_v2shrink
        # 系统信息：如端侧机型等信息
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
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.enable_postpaid is not None:
            result['EnablePostpaid'] = self.enable_postpaid
        if self.result_store_shrink is not None:
            result['ResultStore'] = self.result_store_shrink
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        if self.start_parameters_v2shrink is not None:
            result['StartParametersV2'] = self.start_parameters_v2shrink
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('EnablePostpaid') is not None:
            self.enable_postpaid = m.get('EnablePostpaid')
        if m.get('ResultStore') is not None:
            self.result_store_shrink = m.get('ResultStore')
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionShrinkRequestStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        if m.get('StartParametersV2') is not None:
            self.start_parameters_v2shrink = m.get('StartParametersV2')
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionShrinkRequestSystemInfo()
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
        # 应用id
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
        self.platform_session_id = platform_session_id
        # 请求id
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
            temp_model = CreateAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionSyncRequestSpeedInfo(TeaModel):
    def __init__(
        self,
        endpoint_id: int = None,
        rtt: int = None,
    ):
        self.endpoint_id = endpoint_id
        self.rtt = rtt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id
        if self.rtt is not None:
            result['rtt'] = self.rtt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        if m.get('rtt') is not None:
            self.rtt = m.get('rtt')
        return self


class CreateAppSessionSyncRequestStartParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # key
        self.key = key
        # value
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateAppSessionSyncRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        client_ip: str = None,
        custom_session_id: str = None,
        custom_user_id: str = None,
        district_id: str = None,
        project_id: str = None,
        speed_info: List[CreateAppSessionSyncRequestSpeedInfo] = None,
        start_parameters: List[CreateAppSessionSyncRequestStartParameters] = None,
        system_info: List[CreateAppSessionSyncRequestSystemInfo] = None,
        tags: List[CreateAppSessionSyncRequestTags] = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        # 客户端ip
        self.client_ip = client_ip
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 自定义用户id
        self.custom_user_id = custom_user_id
        self.district_id = district_id
        self.project_id = project_id
        self.speed_info = speed_info
        # 启动参数
        self.start_parameters = start_parameters
        # 系统信息：如端侧机型等信息
        self.system_info = system_info
        self.tags = tags

    def validate(self):
        if self.speed_info:
            for k in self.speed_info:
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
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['SpeedInfo'] = []
        if self.speed_info is not None:
            for k in self.speed_info:
                result['SpeedInfo'].append(k.to_map() if k else None)
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.speed_info = []
        if m.get('SpeedInfo') is not None:
            for k in m.get('SpeedInfo'):
                temp_model = CreateAppSessionSyncRequestSpeedInfo()
                self.speed_info.append(temp_model.from_map(k))
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
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = CreateAppSessionSyncRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateAppSessionSyncResponseBodyBizInfoBiz(TeaModel):
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
        biz: List[CreateAppSessionSyncResponseBodyBizInfoBiz] = None,
        endpoints: List[CreateAppSessionSyncResponseBodyBizInfoEndpoints] = None,
    ):
        self.biz = biz
        self.endpoints = endpoints

    def validate(self):
        if self.biz:
            for k in self.biz:
                if k:
                    k.validate()
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Biz'] = []
        if self.biz is not None:
            for k in self.biz:
                result['Biz'].append(k.to_map() if k else None)
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz = []
        if m.get('Biz') is not None:
            for k in m.get('Biz'):
                temp_model = CreateAppSessionSyncResponseBodyBizInfoBiz()
                self.biz.append(temp_model.from_map(k))
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
        # 应用id
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        self.biz_info = biz_info
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
        self.platform_session_id = platform_session_id
        # 请求id
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
            temp_model = CreateAppSessionSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppVersionRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_name: str = None,
    ):
        self.app_id = app_id
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
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_version_id = app_version_id
        self.code = code
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
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        # 自定义会话id
        self.app_id = app_id
        self.app_version = app_version
        self.client_token = client_token
        self.district_id = district_id
        self.expect_resource_ready_time = expect_resource_ready_time
        self.expect_session_capacity = expect_session_capacity
        # 平台会话id
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
        # 请求id
        self.request_id = request_id
        # 自定义会话id
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
            temp_model = CreateCapacityReservationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetDeployTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        custom_param: str = None,
        need_unzip: bool = None,
        oss_bucket: str = None,
        oss_file_path: str = None,
        oss_region_id: str = None,
        source_type: str = None,
    ):
        self.client_token = client_token
        self.custom_param = custom_param
        self.need_unzip = need_unzip
        self.oss_bucket = oss_bucket
        self.oss_file_path = oss_file_path
        self.oss_region_id = oss_region_id
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.custom_param is not None:
            result['CustomParam'] = self.custom_param
        if self.need_unzip is not None:
            result['NeedUnzip'] = self.need_unzip
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_file_path is not None:
            result['OssFilePath'] = self.oss_file_path
        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CustomParam') is not None:
            self.custom_param = m.get('CustomParam')
        if m.get('NeedUnzip') is not None:
            self.need_unzip = m.get('NeedUnzip')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssFilePath') is not None:
            self.oss_file_path = m.get('OssFilePath')
        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class CreateDatasetDeployTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # 请求id
        self.request_id = request_id
        # 应用版本
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


class CreateDatasetDeployTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetDeployTaskResponseBody = None,
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
            temp_model = CreateDatasetDeployTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProjectQuotaLimitDistrictLimitMapValue(TeaModel):
    def __init__(
        self,
        district_id: str = None,
        district_name: str = None,
        max_limit: int = None,
    ):
        # 大区ID
        self.district_id = district_id
        # 大区名称
        self.district_name = district_name
        # 上限
        self.max_limit = max_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.district_name is not None:
            result['DistrictName'] = self.district_name
        if self.max_limit is not None:
            result['MaxLimit'] = self.max_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('DistrictName') is not None:
            self.district_name = m.get('DistrictName')
        if m.get('MaxLimit') is not None:
            self.max_limit = m.get('MaxLimit')
        return self


class CreateProjectRequestProjectQuotaLimit(TeaModel):
    def __init__(
        self,
        district_limit_map: Dict[str, ProjectQuotaLimitDistrictLimitMapValue] = None,
        limit_type: str = None,
    ):
        # key - districtId
        self.district_limit_map = district_limit_map
        # 限制类型 ：目前默认 - ReserveContainer
        self.limit_type = limit_type

    def validate(self):
        if self.district_limit_map:
            for v in self.district_limit_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistrictLimitMap'] = {}
        if self.district_limit_map is not None:
            for k, v in self.district_limit_map.items():
                result['DistrictLimitMap'][k] = v.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.district_limit_map = {}
        if m.get('DistrictLimitMap') is not None:
            for k, v in m.get('DistrictLimitMap').items():
                temp_model = ProjectQuotaLimitDistrictLimitMapValue()
                self.district_limit_map[k] = temp_model.from_map(v)
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        bound_app_id_list: List[str] = None,
        operator_id: str = None,
        operator_type: str = None,
        project_memo: str = None,
        project_name: str = None,
        project_quota_limit: CreateProjectRequestProjectQuotaLimit = None,
    ):
        self.bound_app_id_list = bound_app_id_list
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        self.project_memo = project_memo
        # project name
        self.project_name = project_name
        # key : districtId
        self.project_quota_limit = project_quota_limit

    def validate(self):
        if self.project_quota_limit:
            self.project_quota_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_id_list is not None:
            result['BoundAppIdList'] = self.bound_app_id_list
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundAppIdList') is not None:
            self.bound_app_id_list = m.get('BoundAppIdList')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            temp_model = CreateProjectRequestProjectQuotaLimit()
            self.project_quota_limit = temp_model.from_map(m['ProjectQuotaLimit'])
        return self


class CreateProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        bound_app_id_list_shrink: str = None,
        operator_id: str = None,
        operator_type: str = None,
        project_memo: str = None,
        project_name: str = None,
        project_quota_limit_shrink: str = None,
    ):
        self.bound_app_id_list_shrink = bound_app_id_list_shrink
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        self.project_memo = project_memo
        # project name
        self.project_name = project_name
        # key : districtId
        self.project_quota_limit_shrink = project_quota_limit_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_id_list_shrink is not None:
            result['BoundAppIdList'] = self.bound_app_id_list_shrink
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit_shrink is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundAppIdList') is not None:
            self.bound_app_id_list_shrink = m.get('BoundAppIdList')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            self.project_quota_limit_shrink = m.get('ProjectQuotaLimit')
        return self


class CreateProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        project_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        self.project_id = project_id
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
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
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
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
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_id = app_id
        self.code = code
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppVersionRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
    ):
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
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_version_id = app_version_id
        self.code = code
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
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = DeleteAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        operator_id: str = None,
        operator_type: str = None,
        project_id: str = None,
    ):
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # project Id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteProjectResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = DeleteProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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
        code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.adapt_apply_id = adapt_apply_id
        self.adapt_target = adapt_target
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.code = code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
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
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        if m.get('AdaptTarget') is not None:
            temp_model = GetAdaptationResponseBodyAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetAdaptationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
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
        code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        version_adapt_num: int = None,
        version_total_num: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_type = app_type
        self.code = code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success
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
        if self.code is not None:
            result['Code'] = self.code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppSessionRequest(TeaModel):
    def __init__(
        self,
        custom_session_id: str = None,
        platform_session_id: str = None,
    ):
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetAppSessionResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        biz_info: List[GetAppSessionResponseBodyBizInfo] = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # 应用id
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        self.biz_info = biz_info
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
        self.platform_session_id = platform_session_id
        # 请求id
        self.request_id = request_id
        # 状态
        self.status = status

    def validate(self):
        if self.biz_info:
            for k in self.biz_info:
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
        result['BizInfo'] = []
        if self.biz_info is not None:
            for k in self.biz_info:
                result['BizInfo'].append(k.to_map() if k else None)
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
        self.biz_info = []
        if m.get('BizInfo') is not None:
            for k in m.get('BizInfo'):
                temp_model = GetAppSessionResponseBodyBizInfo()
                self.biz_info.append(temp_model.from_map(k))
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
            temp_model = GetAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppVersionRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
    ):
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
        code: str = None,
        consume_cu: float = None,
        file_address: str = None,
        file_size: int = None,
        file_upload_finish_time: str = None,
        file_upload_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.app_version_name = app_version_name
        self.app_version_status = app_version_status
        self.app_version_status_memo = app_version_status_memo
        self.code = code
        self.consume_cu = consume_cu
        self.file_address = file_address
        self.file_size = file_size
        self.file_upload_finish_time = file_upload_finish_time
        self.file_upload_type = file_upload_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
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
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
    ):
        self.dataset_id = dataset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        return self


class GetDatasetResponseBody(TeaModel):
    def __init__(
        self,
        custom_param: str = None,
        dataset_id: str = None,
        dataset_size: int = None,
        request_id: str = None,
    ):
        # 应用id
        self.custom_param = custom_param
        # 自定义会话id
        self.dataset_id = dataset_id
        self.dataset_size = dataset_size
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_param is not None:
            result['CustomParam'] = self.custom_param
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_size is not None:
            result['DatasetSize'] = self.dataset_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomParam') is not None:
            self.custom_param = m.get('CustomParam')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetSize') is not None:
            self.dataset_size = m.get('DatasetSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasetResponseBody = None,
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
            temp_model = GetDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(
        self,
        operator_id: str = None,
        operator_type: str = None,
        project_id: str = None,
    ):
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # project id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DataProjectQuotaLimitDistrictLimitMapValue(TeaModel):
    def __init__(
        self,
        district_id: str = None,
        district_name: str = None,
        max_limit: int = None,
    ):
        # 大区ID
        self.district_id = district_id
        # 大区名称
        self.district_name = district_name
        # 上限
        self.max_limit = max_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.district_name is not None:
            result['DistrictName'] = self.district_name
        if self.max_limit is not None:
            result['MaxLimit'] = self.max_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('DistrictName') is not None:
            self.district_name = m.get('DistrictName')
        if m.get('MaxLimit') is not None:
            self.max_limit = m.get('MaxLimit')
        return self


class GetProjectResponseBodyDataProjectQuotaLimit(TeaModel):
    def __init__(
        self,
        district_limit_map: Dict[str, DataProjectQuotaLimitDistrictLimitMapValue] = None,
        limit_type: str = None,
    ):
        # key - districtId
        self.district_limit_map = district_limit_map
        # 限制类型 ：目前默认 - ReserveContainer
        self.limit_type = limit_type

    def validate(self):
        if self.district_limit_map:
            for v in self.district_limit_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistrictLimitMap'] = {}
        if self.district_limit_map is not None:
            for k, v in self.district_limit_map.items():
                result['DistrictLimitMap'][k] = v.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.district_limit_map = {}
        if m.get('DistrictLimitMap') is not None:
            for k, v in m.get('DistrictLimitMap').items():
                temp_model = DataProjectQuotaLimitDistrictLimitMapValue()
                self.district_limit_map[k] = temp_model.from_map(v)
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class GetProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        bound_app_nums: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        project_id: str = None,
        project_memo: str = None,
        project_name: str = None,
        project_quota_limit: GetProjectResponseBodyDataProjectQuotaLimit = None,
    ):
        # 项目关联的应用数量
        self.bound_app_nums = bound_app_nums
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.project_id = project_id
        self.project_memo = project_memo
        self.project_name = project_name
        # key : districtId
        self.project_quota_limit = project_quota_limit

    def validate(self):
        if self.project_quota_limit:
            self.project_quota_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_nums is not None:
            result['BoundAppNums'] = self.bound_app_nums
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundAppNums') is not None:
            self.bound_app_nums = m.get('BoundAppNums')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            temp_model = GetProjectResponseBodyDataProjectQuotaLimit()
            self.project_quota_limit = temp_model.from_map(m['ProjectQuotaLimit'])
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetProjectResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = GetProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectResponseBody = None,
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
            temp_model = GetProjectResponseBody()
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
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.apps = apps
        self.code = code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListAppResponseBodyApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
    ):
        self.app_id = app_id
        # 自定义会话id
        self.custom_session_ids = custom_session_ids
        # 页码
        self.page_number = page_number
        # 分页大小
        self.page_size = page_size
        # 自定义用户id
        self.platform_session_ids = platform_session_ids

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
        return self


class ListAppSessionsResponseBodyAppSessionsBizInfo(TeaModel):
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListAppSessionsResponseBodyAppSessions(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        biz_info: List[ListAppSessionsResponseBodyAppSessionsBizInfo] = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        status: str = None,
    ):
        # 应用id
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        self.biz_info = biz_info
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
        self.platform_session_id = platform_session_id
        # 状态
        self.status = status

    def validate(self):
        if self.biz_info:
            for k in self.biz_info:
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
        result['BizInfo'] = []
        if self.biz_info is not None:
            for k in self.biz_info:
                result['BizInfo'].append(k.to_map() if k else None)
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        self.biz_info = []
        if m.get('BizInfo') is not None:
            for k in m.get('BizInfo'):
                temp_model = ListAppSessionsResponseBodyAppSessionsBizInfo()
                self.biz_info.append(temp_model.from_map(k))
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
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
        # 请求id
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
        tenant_id: int = None,
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
        self.tenant_id = tenant_id

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
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
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
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListAppVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
        versions: List[ListAppVersionResponseBodyVersions] = None,
    ):
        self.code = code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = ListAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        self.app_id = app_id
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
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_id = app_id
        self.code = code
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppVersionRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
        app_version_name: str = None,
    ):
        self.app_version_id = app_version_id
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
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_version_id = app_version_id
        self.code = code
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
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = ModifyAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProjectRequestProjectQuotaLimit(TeaModel):
    def __init__(
        self,
        district_limit_map: Dict[str, ProjectQuotaLimitDistrictLimitMapValue] = None,
        limit_type: str = None,
    ):
        # key - districtId
        self.district_limit_map = district_limit_map
        # 限制类型 ：目前默认 - ReserveContainer
        self.limit_type = limit_type

    def validate(self):
        if self.district_limit_map:
            for v in self.district_limit_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistrictLimitMap'] = {}
        if self.district_limit_map is not None:
            for k, v in self.district_limit_map.items():
                result['DistrictLimitMap'][k] = v.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.district_limit_map = {}
        if m.get('DistrictLimitMap') is not None:
            for k, v in m.get('DistrictLimitMap').items():
                temp_model = ProjectQuotaLimitDistrictLimitMapValue()
                self.district_limit_map[k] = temp_model.from_map(v)
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class ModifyProjectRequest(TeaModel):
    def __init__(
        self,
        bound_app_id_list: List[str] = None,
        operator_id: str = None,
        operator_type: str = None,
        project_id: str = None,
        project_memo: str = None,
        project_name: str = None,
        project_quota_limit: ModifyProjectRequestProjectQuotaLimit = None,
    ):
        self.bound_app_id_list = bound_app_id_list
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # project Id
        self.project_id = project_id
        self.project_memo = project_memo
        # project name
        self.project_name = project_name
        # key : districtId
        self.project_quota_limit = project_quota_limit

    def validate(self):
        if self.project_quota_limit:
            self.project_quota_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_id_list is not None:
            result['BoundAppIdList'] = self.bound_app_id_list
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundAppIdList') is not None:
            self.bound_app_id_list = m.get('BoundAppIdList')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            temp_model = ModifyProjectRequestProjectQuotaLimit()
            self.project_quota_limit = temp_model.from_map(m['ProjectQuotaLimit'])
        return self


class ModifyProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        bound_app_id_list_shrink: str = None,
        operator_id: str = None,
        operator_type: str = None,
        project_id: str = None,
        project_memo: str = None,
        project_name: str = None,
        project_quota_limit_shrink: str = None,
    ):
        self.bound_app_id_list_shrink = bound_app_id_list_shrink
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # project Id
        self.project_id = project_id
        self.project_memo = project_memo
        # project name
        self.project_name = project_name
        # key : districtId
        self.project_quota_limit_shrink = project_quota_limit_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_id_list_shrink is not None:
            result['BoundAppIdList'] = self.bound_app_id_list_shrink
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit_shrink is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundAppIdList') is not None:
            self.bound_app_id_list_shrink = m.get('BoundAppIdList')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            self.project_quota_limit_shrink = m.get('ProjectQuotaLimit')
        return self


class ModifyProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ModifyProjectResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = ModifyProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyProjectResponseBody = None,
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
            temp_model = ModifyProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageQueryProjectRequest(TeaModel):
    def __init__(
        self,
        key_search: str = None,
        operator_id: str = None,
        operator_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # projectId or projectName like
        self.key_search = key_search
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 当前页码，默认1
        self.page_number = page_number
        # 每页项数，默认20,最大100
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
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeySearch') is not None:
            self.key_search = m.get('KeySearch')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DataRecordsProjectQuotaLimitDistrictLimitMapValue(TeaModel):
    def __init__(
        self,
        district_id: str = None,
        district_name: str = None,
        max_limit: int = None,
    ):
        # 大区ID
        self.district_id = district_id
        # 大区名称
        self.district_name = district_name
        # 上限
        self.max_limit = max_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.district_name is not None:
            result['DistrictName'] = self.district_name
        if self.max_limit is not None:
            result['MaxLimit'] = self.max_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('DistrictName') is not None:
            self.district_name = m.get('DistrictName')
        if m.get('MaxLimit') is not None:
            self.max_limit = m.get('MaxLimit')
        return self


class PageQueryProjectResponseBodyDataRecordsProjectQuotaLimit(TeaModel):
    def __init__(
        self,
        district_limit_map: Dict[str, DataRecordsProjectQuotaLimitDistrictLimitMapValue] = None,
        limit_type: str = None,
    ):
        # key - districtId
        self.district_limit_map = district_limit_map
        # 限制类型 ：目前默认 - ReserveContainer
        self.limit_type = limit_type

    def validate(self):
        if self.district_limit_map:
            for v in self.district_limit_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistrictLimitMap'] = {}
        if self.district_limit_map is not None:
            for k, v in self.district_limit_map.items():
                result['DistrictLimitMap'][k] = v.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.district_limit_map = {}
        if m.get('DistrictLimitMap') is not None:
            for k, v in m.get('DistrictLimitMap').items():
                temp_model = DataRecordsProjectQuotaLimitDistrictLimitMapValue()
                self.district_limit_map[k] = temp_model.from_map(v)
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class PageQueryProjectResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        bound_app_nums: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        project_id: str = None,
        project_memo: str = None,
        project_name: str = None,
        project_quota_limit: PageQueryProjectResponseBodyDataRecordsProjectQuotaLimit = None,
    ):
        # 项目关联的应用数量
        self.bound_app_nums = bound_app_nums
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.project_id = project_id
        self.project_memo = project_memo
        self.project_name = project_name
        # key : districtId
        self.project_quota_limit = project_quota_limit

    def validate(self):
        if self.project_quota_limit:
            self.project_quota_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_nums is not None:
            result['BoundAppNums'] = self.bound_app_nums
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundAppNums') is not None:
            self.bound_app_nums = m.get('BoundAppNums')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            temp_model = PageQueryProjectResponseBodyDataRecordsProjectQuotaLimit()
            self.project_quota_limit = temp_model.from_map(m['ProjectQuotaLimit'])
        return self


class PageQueryProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pages: int = None,
        records: List[PageQueryProjectResponseBodyDataRecords] = None,
        total_count: int = None,
    ):
        # 当前页码，默认1
        self.page_number = page_number
        # 每页项数，默认20,最大100
        self.page_size = page_size
        # 总页数
        self.pages = pages
        # 结果集
        self.records = records
        # 总共项数
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = PageQueryProjectResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PageQueryProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PageQueryProjectResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = PageQueryProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PageQueryProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageQueryProjectResponseBody = None,
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
            temp_model = PageQueryProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageQueryProjectAppsRequest(TeaModel):
    def __init__(
        self,
        operator_id: str = None,
        operator_type: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
    ):
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 当前页码，默认1
        self.page_number = page_number
        # 每页项数，默认20,最大100
        self.page_size = page_size
        # projectId
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PageQueryProjectAppsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        gmt_create: str = None,
        project_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.gmt_create = gmt_create
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
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PageQueryProjectAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pages: int = None,
        records: List[PageQueryProjectAppsResponseBodyDataRecords] = None,
        total_count: int = None,
    ):
        # 当前页码，默认1
        self.page_number = page_number
        # 每页项数，默认20,最大100
        self.page_size = page_size
        # 总页数
        self.pages = pages
        # 结果集
        self.records = records
        # 总共项数
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = PageQueryProjectAppsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PageQueryProjectAppsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PageQueryProjectAppsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = PageQueryProjectAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PageQueryProjectAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageQueryProjectAppsResponseBody = None,
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
            temp_model = PageQueryProjectAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOfflineTaskProgressRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        version_id: str = None,
    ):
        self.app_id = app_id
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class QueryOfflineTaskProgressResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        progress: float = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.progress = progress
        self.status = status

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
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryOfflineTaskProgressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryOfflineTaskProgressResponseBodyData = None,
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
            temp_model = QueryOfflineTaskProgressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryOfflineTaskProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOfflineTaskProgressResponseBody = None,
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
            temp_model = QueryOfflineTaskProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshDistrictMetaResponseBodyDataProjectQuotaLimit(TeaModel):
    def __init__(
        self,
        district_limit_map: Dict[str, DataProjectQuotaLimitDistrictLimitMapValue] = None,
        limit_type: str = None,
    ):
        # key - districtId
        self.district_limit_map = district_limit_map
        # 限制类型 ：目前默认 - ReserveContainer
        self.limit_type = limit_type

    def validate(self):
        if self.district_limit_map:
            for v in self.district_limit_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistrictLimitMap'] = {}
        if self.district_limit_map is not None:
            for k, v in self.district_limit_map.items():
                result['DistrictLimitMap'][k] = v.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.district_limit_map = {}
        if m.get('DistrictLimitMap') is not None:
            for k, v in m.get('DistrictLimitMap').items():
                temp_model = DataProjectQuotaLimitDistrictLimitMapValue()
                self.district_limit_map[k] = temp_model.from_map(v)
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class RefreshDistrictMetaResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        project_quota_limit: RefreshDistrictMetaResponseBodyDataProjectQuotaLimit = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        self.project_quota_limit = project_quota_limit
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
        self.success = success

    def validate(self):
        if self.project_quota_limit:
            self.project_quota_limit.validate()

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
        if self.project_quota_limit is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit.to_map()
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
        if m.get('ProjectQuotaLimit') is not None:
            temp_model = RefreshDistrictMetaResponseBodyDataProjectQuotaLimit()
            self.project_quota_limit = temp_model.from_map(m['ProjectQuotaLimit'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshDistrictMetaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RefreshDistrictMetaResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = RefreshDistrictMetaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshDistrictMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshDistrictMetaResponseBody = None,
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
            temp_model = RefreshDistrictMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppSessionRequestStopParam(TeaModel):
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


class StopAppSessionRequest(TeaModel):
    def __init__(
        self,
        custom_session_id: str = None,
        platform_session_id: str = None,
        stop_param: List[StopAppSessionRequestStopParam] = None,
    ):
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 自定义用户id
        self.platform_session_id = platform_session_id
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


class StopAppSessionResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        request_id: str = None,
    ):
        # 应用id
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
        self.platform_session_id = platform_session_id
        # 请求id
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
            temp_model = StopAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitOfflineTaskRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        env: str = None,
        uri: str = None,
        version_id: str = None,
        version_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_type = app_type
        self.env = env
        self.uri = uri
        self.version_id = version_id
        self.version_name = version_name

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
        if self.env is not None:
            result['Env'] = self.env
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class SubmitOfflineTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitOfflineTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitOfflineTaskResponseBody = None,
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
            temp_model = SubmitOfflineTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class ApplyDataModelConfigInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        configuration: str = None,
        data_model_code: str = None,
        product_key: str = None,
    ):
        self.api_version = api_version
        self.configuration = configuration
        self.data_model_code = data_model_code
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.data_model_code is not None:
            result['DataModelCode'] = self.data_model_code
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('DataModelCode') is not None:
            self.data_model_code = m.get('DataModelCode')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ApplyDataModelConfigInfoResponseBody(TeaModel):
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


class ApplyDataModelConfigInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyDataModelConfigInfoResponseBody = None,
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
            temp_model = ApplyDataModelConfigInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDataRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        business_id: str = None,
        key: str = None,
        product_key: str = None,
        value: str = None,
    ):
        self.api_version = api_version
        self.business_id = business_id
        self.key = key
        self.product_key = product_key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.key is not None:
            result['Key'] = self.key
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AttachDataResponseBody(TeaModel):
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


class AttachDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachDataResponseBody = None,
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
            temp_model = AttachDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDataWithSignatureRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        business_id: str = None,
        iot_auth_type: str = None,
        iot_data_digest: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        iot_signature: str = None,
        key: str = None,
        product_key: str = None,
        value: str = None,
    ):
        self.api_version = api_version
        self.business_id = business_id
        self.iot_auth_type = iot_auth_type
        self.iot_data_digest = iot_data_digest
        self.iot_id = iot_id
        self.iot_id_service_provider = iot_id_service_provider
        self.iot_id_source = iot_id_source
        self.iot_signature = iot_signature
        self.key = key
        self.product_key = product_key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.iot_signature is not None:
            result['IotSignature'] = self.iot_signature
        if self.key is not None:
            result['Key'] = self.key
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('IotSignature') is not None:
            self.iot_signature = m.get('IotSignature')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AttachDataWithSignatureResponseBody(TeaModel):
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


class AttachDataWithSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachDataWithSignatureResponseBody = None,
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
            temp_model = AttachDataWithSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeDeviceRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        device_group_id: str = None,
        device_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.device_group_id = device_group_id
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class AuthorizeDeviceResponseBody(TeaModel):
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


class AuthorizeDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeDeviceResponseBody = None,
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
            temp_model = AuthorizeDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        device_group_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.device_group_id = device_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        return self


class AuthorizeDeviceGroupResponseBody(TeaModel):
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


class AuthorizeDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeDeviceGroupResponseBody = None,
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
            temp_model = AuthorizeDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUploadMPCoSPhaseDigestInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        phase_data_list: Dict[str, Any] = None,
        phase_group_id: str = None,
        phase_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.phase_data_list = phase_data_list
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.phase_data_list is not None:
            result['PhaseDataList'] = self.phase_data_list
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('PhaseDataList') is not None:
            self.phase_data_list = m.get('PhaseDataList')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        return self


class BatchUploadMPCoSPhaseDigestInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        phase_data_list_shrink: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.phase_data_list_shrink = phase_data_list_shrink
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.phase_data_list_shrink is not None:
            result['PhaseDataList'] = self.phase_data_list_shrink
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('PhaseDataList') is not None:
            self.phase_data_list_shrink = m.get('PhaseDataList')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        return self


class BatchUploadMPCoSPhaseDigestInfoResponseBody(TeaModel):
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


class BatchUploadMPCoSPhaseDigestInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUploadMPCoSPhaseDigestInfoResponseBody = None,
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
            temp_model = BatchUploadMPCoSPhaseDigestInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUploadMPCoSPhaseDigestInfoByDeviceRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        iot_auth_type: str = None,
        iot_data_digest: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        iot_signature: str = None,
        phase_data_list: Dict[str, Any] = None,
        phase_group_id: str = None,
        phase_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.iot_auth_type = iot_auth_type
        self.iot_data_digest = iot_data_digest
        self.iot_id = iot_id
        self.iot_id_service_provider = iot_id_service_provider
        self.iot_id_source = iot_id_source
        self.iot_signature = iot_signature
        self.phase_data_list = phase_data_list
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.iot_signature is not None:
            result['IotSignature'] = self.iot_signature
        if self.phase_data_list is not None:
            result['PhaseDataList'] = self.phase_data_list
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('IotSignature') is not None:
            self.iot_signature = m.get('IotSignature')
        if m.get('PhaseDataList') is not None:
            self.phase_data_list = m.get('PhaseDataList')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        return self


class BatchUploadMPCoSPhaseDigestInfoByDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        iot_auth_type: str = None,
        iot_data_digest: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        iot_signature: str = None,
        phase_data_list_shrink: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.iot_auth_type = iot_auth_type
        self.iot_data_digest = iot_data_digest
        self.iot_id = iot_id
        self.iot_id_service_provider = iot_id_service_provider
        self.iot_id_source = iot_id_source
        self.iot_signature = iot_signature
        self.phase_data_list_shrink = phase_data_list_shrink
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.iot_signature is not None:
            result['IotSignature'] = self.iot_signature
        if self.phase_data_list_shrink is not None:
            result['PhaseDataList'] = self.phase_data_list_shrink
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('IotSignature') is not None:
            self.iot_signature = m.get('IotSignature')
        if m.get('PhaseDataList') is not None:
            self.phase_data_list_shrink = m.get('PhaseDataList')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        return self


class BatchUploadMPCoSPhaseDigestInfoByDeviceResponseBody(TeaModel):
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


class BatchUploadMPCoSPhaseDigestInfoByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUploadMPCoSPhaseDigestInfoByDeviceResponseBody = None,
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
            temp_model = BatchUploadMPCoSPhaseDigestInfoByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUploadMPCoSPhaseTextInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        phase_data_list: Dict[str, Any] = None,
        phase_group_id: str = None,
        phase_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.phase_data_list = phase_data_list
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.phase_data_list is not None:
            result['PhaseDataList'] = self.phase_data_list
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('PhaseDataList') is not None:
            self.phase_data_list = m.get('PhaseDataList')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        return self


class BatchUploadMPCoSPhaseTextInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        phase_data_list_shrink: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.phase_data_list_shrink = phase_data_list_shrink
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.phase_data_list_shrink is not None:
            result['PhaseDataList'] = self.phase_data_list_shrink
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('PhaseDataList') is not None:
            self.phase_data_list_shrink = m.get('PhaseDataList')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        return self


class BatchUploadMPCoSPhaseTextInfoResponseBody(TeaModel):
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


class BatchUploadMPCoSPhaseTextInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUploadMPCoSPhaseTextInfoResponseBody = None,
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
            temp_model = BatchUploadMPCoSPhaseTextInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUploadMPCoSPhaseTextInfoByDeviceRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        iot_auth_type: str = None,
        iot_data_digest: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        iot_signature: str = None,
        phase_data_list: Dict[str, Any] = None,
        phase_group_id: str = None,
        phase_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.iot_auth_type = iot_auth_type
        self.iot_data_digest = iot_data_digest
        self.iot_id = iot_id
        self.iot_id_service_provider = iot_id_service_provider
        self.iot_id_source = iot_id_source
        self.iot_signature = iot_signature
        self.phase_data_list = phase_data_list
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.iot_signature is not None:
            result['IotSignature'] = self.iot_signature
        if self.phase_data_list is not None:
            result['PhaseDataList'] = self.phase_data_list
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('IotSignature') is not None:
            self.iot_signature = m.get('IotSignature')
        if m.get('PhaseDataList') is not None:
            self.phase_data_list = m.get('PhaseDataList')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        return self


class BatchUploadMPCoSPhaseTextInfoByDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        iot_auth_type: str = None,
        iot_data_digest: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        iot_signature: str = None,
        phase_data_list_shrink: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.iot_auth_type = iot_auth_type
        self.iot_data_digest = iot_data_digest
        self.iot_id = iot_id
        self.iot_id_service_provider = iot_id_service_provider
        self.iot_id_source = iot_id_source
        self.iot_signature = iot_signature
        self.phase_data_list_shrink = phase_data_list_shrink
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.iot_signature is not None:
            result['IotSignature'] = self.iot_signature
        if self.phase_data_list_shrink is not None:
            result['PhaseDataList'] = self.phase_data_list_shrink
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('IotSignature') is not None:
            self.iot_signature = m.get('IotSignature')
        if m.get('PhaseDataList') is not None:
            self.phase_data_list_shrink = m.get('PhaseDataList')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        return self


class BatchUploadMPCoSPhaseTextInfoByDeviceResponseBody(TeaModel):
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


class BatchUploadMPCoSPhaseTextInfoByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUploadMPCoSPhaseTextInfoByDeviceResponseBody = None,
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
            temp_model = BatchUploadMPCoSPhaseTextInfoByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMPCoSPhaseRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        name: str = None,
        phase_group_id: str = None,
        remark: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.name = name
        self.phase_group_id = phase_group_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreateMPCoSPhaseResponseBody(TeaModel):
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


class CreateMPCoSPhaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMPCoSPhaseResponseBody = None,
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
            temp_model = CreateMPCoSPhaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMPCoSPhaseGroupRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        name: str = None,
        remark: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.name = name
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreateMPCoSPhaseGroupResponseBody(TeaModel):
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


class CreateMPCoSPhaseGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMPCoSPhaseGroupResponseBody = None,
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
            temp_model = CreateMPCoSPhaseGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMemberRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        member_contact: str = None,
        member_name: str = None,
        member_phone: str = None,
        member_uid: str = None,
        remark: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.member_contact = member_contact
        self.member_name = member_name
        self.member_phone = member_phone
        self.member_uid = member_uid
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.member_contact is not None:
            result['MemberContact'] = self.member_contact
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.member_phone is not None:
            result['MemberPhone'] = self.member_phone
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('MemberContact') is not None:
            self.member_contact = m.get('MemberContact')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('MemberPhone') is not None:
            self.member_phone = m.get('MemberPhone')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreateMemberResponseBody(TeaModel):
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


class CreateMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMemberResponseBody = None,
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
            temp_model = CreateMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCapacityInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        return self


class DescribeCapacityInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        capacity_quota: int = None,
        count_quota: int = None,
        member_used_capacity: int = None,
        member_used_count: int = None,
        used_capacity: int = None,
        used_count: int = None,
    ):
        self.capacity_quota = capacity_quota
        self.count_quota = count_quota
        self.member_used_capacity = member_used_capacity
        self.member_used_count = member_used_count
        self.used_capacity = used_capacity
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity_quota is not None:
            result['CapacityQuota'] = self.capacity_quota
        if self.count_quota is not None:
            result['CountQuota'] = self.count_quota
        if self.member_used_capacity is not None:
            result['MemberUsedCapacity'] = self.member_used_capacity
        if self.member_used_count is not None:
            result['MemberUsedCount'] = self.member_used_count
        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityQuota') is not None:
            self.capacity_quota = m.get('CapacityQuota')
        if m.get('CountQuota') is not None:
            self.count_quota = m.get('CountQuota')
        if m.get('MemberUsedCapacity') is not None:
            self.member_used_capacity = m.get('MemberUsedCapacity')
        if m.get('MemberUsedCount') is not None:
            self.member_used_count = m.get('MemberUsedCount')
        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribeCapacityInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeCapacityInfoResponseBodyData = None,
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
            temp_model = DescribeCapacityInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCapacityInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCapacityInfoResponseBody = None,
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
            temp_model = DescribeCapacityInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMPCoSAuthorizedInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        member_id: str = None,
        phase_group_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.member_id = member_id
        self.phase_group_id = phase_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        return self


class DescribeMPCoSAuthorizedInfoResponseBodyDataAuthorizedPhaseList(TeaModel):
    def __init__(
        self,
        phase_id: str = None,
        phase_name: str = None,
    ):
        self.phase_id = phase_id
        self.phase_name = phase_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.phase_name is not None:
            result['PhaseName'] = self.phase_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('PhaseName') is not None:
            self.phase_name = m.get('PhaseName')
        return self


class DescribeMPCoSAuthorizedInfoResponseBodyDataUnAuthorizedPhaseList(TeaModel):
    def __init__(
        self,
        phase_id: str = None,
        phase_name: str = None,
    ):
        self.phase_id = phase_id
        self.phase_name = phase_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.phase_name is not None:
            result['PhaseName'] = self.phase_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('PhaseName') is not None:
            self.phase_name = m.get('PhaseName')
        return self


class DescribeMPCoSAuthorizedInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_phase_list: List[DescribeMPCoSAuthorizedInfoResponseBodyDataAuthorizedPhaseList] = None,
        un_authorized_phase_list: List[DescribeMPCoSAuthorizedInfoResponseBodyDataUnAuthorizedPhaseList] = None,
    ):
        self.authorized_phase_list = authorized_phase_list
        self.un_authorized_phase_list = un_authorized_phase_list

    def validate(self):
        if self.authorized_phase_list:
            for k in self.authorized_phase_list:
                if k:
                    k.validate()
        if self.un_authorized_phase_list:
            for k in self.un_authorized_phase_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthorizedPhaseList'] = []
        if self.authorized_phase_list is not None:
            for k in self.authorized_phase_list:
                result['AuthorizedPhaseList'].append(k.to_map() if k else None)
        result['UnAuthorizedPhaseList'] = []
        if self.un_authorized_phase_list is not None:
            for k in self.un_authorized_phase_list:
                result['UnAuthorizedPhaseList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorized_phase_list = []
        if m.get('AuthorizedPhaseList') is not None:
            for k in m.get('AuthorizedPhaseList'):
                temp_model = DescribeMPCoSAuthorizedInfoResponseBodyDataAuthorizedPhaseList()
                self.authorized_phase_list.append(temp_model.from_map(k))
        self.un_authorized_phase_list = []
        if m.get('UnAuthorizedPhaseList') is not None:
            for k in m.get('UnAuthorizedPhaseList'):
                temp_model = DescribeMPCoSAuthorizedInfoResponseBodyDataUnAuthorizedPhaseList()
                self.un_authorized_phase_list.append(temp_model.from_map(k))
        return self


class DescribeMPCoSAuthorizedInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeMPCoSAuthorizedInfoResponseBodyData = None,
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
            temp_model = DescribeMPCoSAuthorizedInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMPCoSAuthorizedInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMPCoSAuthorizedInfoResponseBody = None,
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
            temp_model = DescribeMPCoSAuthorizedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMPCoSPhaseInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        data_key: str = None,
        data_seq: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.data_key = data_key
        self.data_seq = data_seq
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_key is not None:
            result['DataKey'] = self.data_key
        if self.data_seq is not None:
            result['DataSeq'] = self.data_seq
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataKey') is not None:
            self.data_key = m.get('DataKey')
        if m.get('DataSeq') is not None:
            self.data_seq = m.get('DataSeq')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        return self


class DescribeMPCoSPhaseInfoResponseBodyDataRelatedDataList(TeaModel):
    def __init__(
        self,
        related_data_key: str = None,
        related_data_seq: str = None,
        related_phase_data_hash: str = None,
        related_phase_id: str = None,
        related_phase_name: str = None,
    ):
        self.related_data_key = related_data_key
        self.related_data_seq = related_data_seq
        self.related_phase_data_hash = related_phase_data_hash
        self.related_phase_id = related_phase_id
        self.related_phase_name = related_phase_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.related_data_key is not None:
            result['RelatedDataKey'] = self.related_data_key
        if self.related_data_seq is not None:
            result['RelatedDataSeq'] = self.related_data_seq
        if self.related_phase_data_hash is not None:
            result['RelatedPhaseDataHash'] = self.related_phase_data_hash
        if self.related_phase_id is not None:
            result['RelatedPhaseId'] = self.related_phase_id
        if self.related_phase_name is not None:
            result['RelatedPhaseName'] = self.related_phase_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelatedDataKey') is not None:
            self.related_data_key = m.get('RelatedDataKey')
        if m.get('RelatedDataSeq') is not None:
            self.related_data_seq = m.get('RelatedDataSeq')
        if m.get('RelatedPhaseDataHash') is not None:
            self.related_phase_data_hash = m.get('RelatedPhaseDataHash')
        if m.get('RelatedPhaseId') is not None:
            self.related_phase_id = m.get('RelatedPhaseId')
        if m.get('RelatedPhaseName') is not None:
            self.related_phase_name = m.get('RelatedPhaseName')
        return self


class DescribeMPCoSPhaseInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        block_hash: str = None,
        block_number: int = None,
        data_hash: str = None,
        data_value: str = None,
        iot_id: str = None,
        previous_hash: str = None,
        product_key: str = None,
        related_data_list: List[DescribeMPCoSPhaseInfoResponseBodyDataRelatedDataList] = None,
        timestamp: int = None,
        transaction_hash: str = None,
    ):
        self.block_hash = block_hash
        self.block_number = block_number
        self.data_hash = data_hash
        self.data_value = data_value
        self.iot_id = iot_id
        self.previous_hash = previous_hash
        self.product_key = product_key
        self.related_data_list = related_data_list
        self.timestamp = timestamp
        self.transaction_hash = transaction_hash

    def validate(self):
        if self.related_data_list:
            for k in self.related_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.block_number is not None:
            result['BlockNumber'] = self.block_number
        if self.data_hash is not None:
            result['DataHash'] = self.data_hash
        if self.data_value is not None:
            result['DataValue'] = self.data_value
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.previous_hash is not None:
            result['PreviousHash'] = self.previous_hash
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        result['RelatedDataList'] = []
        if self.related_data_list is not None:
            for k in self.related_data_list:
                result['RelatedDataList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.transaction_hash is not None:
            result['TransactionHash'] = self.transaction_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('BlockNumber') is not None:
            self.block_number = m.get('BlockNumber')
        if m.get('DataHash') is not None:
            self.data_hash = m.get('DataHash')
        if m.get('DataValue') is not None:
            self.data_value = m.get('DataValue')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PreviousHash') is not None:
            self.previous_hash = m.get('PreviousHash')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        self.related_data_list = []
        if m.get('RelatedDataList') is not None:
            for k in m.get('RelatedDataList'):
                temp_model = DescribeMPCoSPhaseInfoResponseBodyDataRelatedDataList()
                self.related_data_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TransactionHash') is not None:
            self.transaction_hash = m.get('TransactionHash')
        return self


class DescribeMPCoSPhaseInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeMPCoSPhaseInfoResponseBodyData = None,
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
            temp_model = DescribeMPCoSPhaseInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMPCoSPhaseInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMPCoSPhaseInfoResponseBody = None,
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
            temp_model = DescribeMPCoSPhaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMPCoSResourceInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        return self


class DescribeMPCoSResourceInfoResponseBodyDataPhaseQuotaInfoList(TeaModel):
    def __init__(
        self,
        phase_group_id: str = None,
        phase_group_name: str = None,
        phase_quota: int = None,
        used_phase: int = None,
    ):
        self.phase_group_id = phase_group_id
        self.phase_group_name = phase_group_name
        self.phase_quota = phase_quota
        self.used_phase = used_phase

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_group_name is not None:
            result['PhaseGroupName'] = self.phase_group_name
        if self.phase_quota is not None:
            result['PhaseQuota'] = self.phase_quota
        if self.used_phase is not None:
            result['UsedPhase'] = self.used_phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseGroupName') is not None:
            self.phase_group_name = m.get('PhaseGroupName')
        if m.get('PhaseQuota') is not None:
            self.phase_quota = m.get('PhaseQuota')
        if m.get('UsedPhase') is not None:
            self.used_phase = m.get('UsedPhase')
        return self


class DescribeMPCoSResourceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        member_quota: int = None,
        phase_group_quota: int = None,
        phase_quota_info_list: List[DescribeMPCoSResourceInfoResponseBodyDataPhaseQuotaInfoList] = None,
        used_member: int = None,
        used_phase_group: int = None,
    ):
        self.member_quota = member_quota
        self.phase_group_quota = phase_group_quota
        self.phase_quota_info_list = phase_quota_info_list
        self.used_member = used_member
        self.used_phase_group = used_phase_group

    def validate(self):
        if self.phase_quota_info_list:
            for k in self.phase_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_quota is not None:
            result['MemberQuota'] = self.member_quota
        if self.phase_group_quota is not None:
            result['PhaseGroupQuota'] = self.phase_group_quota
        result['PhaseQuotaInfoList'] = []
        if self.phase_quota_info_list is not None:
            for k in self.phase_quota_info_list:
                result['PhaseQuotaInfoList'].append(k.to_map() if k else None)
        if self.used_member is not None:
            result['UsedMember'] = self.used_member
        if self.used_phase_group is not None:
            result['UsedPhaseGroup'] = self.used_phase_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberQuota') is not None:
            self.member_quota = m.get('MemberQuota')
        if m.get('PhaseGroupQuota') is not None:
            self.phase_group_quota = m.get('PhaseGroupQuota')
        self.phase_quota_info_list = []
        if m.get('PhaseQuotaInfoList') is not None:
            for k in m.get('PhaseQuotaInfoList'):
                temp_model = DescribeMPCoSResourceInfoResponseBodyDataPhaseQuotaInfoList()
                self.phase_quota_info_list.append(temp_model.from_map(k))
        if m.get('UsedMember') is not None:
            self.used_member = m.get('UsedMember')
        if m.get('UsedPhaseGroup') is not None:
            self.used_phase_group = m.get('UsedPhaseGroup')
        return self


class DescribeMPCoSResourceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeMPCoSResourceInfoResponseBodyData = None,
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
            temp_model = DescribeMPCoSResourceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMPCoSResourceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMPCoSResourceInfoResponseBody = None,
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
            temp_model = DescribeMPCoSResourceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMemberCapacityInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        return self


class DescribeMemberCapacityInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_name: str = None,
        member_uid: str = None,
        used_capacity: str = None,
        used_count: str = None,
    ):
        self.member_id = member_id
        self.member_name = member_name
        self.member_uid = member_uid
        self.used_capacity = used_capacity
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribeMemberCapacityInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeMemberCapacityInfoResponseBodyData] = None,
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
                temp_model = DescribeMemberCapacityInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMemberCapacityInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMemberCapacityInfoResponseBody = None,
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
            temp_model = DescribeMemberCapacityInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        return self


class DescribeResourceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        authorize_type: str = None,
        effective_time: int = None,
        expired_time: int = None,
        region: str = None,
        status: str = None,
    ):
        self.authorize_type = authorize_type
        self.effective_time = effective_time
        self.expired_time = expired_time
        self.region = region
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize_type is not None:
            result['AuthorizeType'] = self.authorize_type
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizeType') is not None:
            self.authorize_type = m.get('AuthorizeType')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeResourceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeResourceInfoResponseBodyData = None,
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
            temp_model = DescribeResourceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeResourceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourceInfoResponseBody = None,
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
            temp_model = DescribeResourceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBlockChainInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        business_id: str = None,
        key: str = None,
        product_key: str = None,
    ):
        self.api_version = api_version
        self.business_id = business_id
        self.key = key
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.key is not None:
            result['Key'] = self.key
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetBlockChainInfoResponseBody(TeaModel):
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


class GetBlockChainInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBlockChainInfoResponseBody = None,
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
            temp_model = GetBlockChainInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        business_id: str = None,
        key: str = None,
        product_key: str = None,
    ):
        self.api_version = api_version
        self.business_id = business_id
        self.key = key
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.key is not None:
            result['Key'] = self.key
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetDataResponseBody(TeaModel):
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


class GetDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataResponseBody = None,
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
            temp_model = GetDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataModelConfigInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        data_model_code: str = None,
        product_key: str = None,
    ):
        self.api_version = api_version
        self.data_model_code = data_model_code
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.data_model_code is not None:
            result['DataModelCode'] = self.data_model_code
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('DataModelCode') is not None:
            self.data_model_code = m.get('DataModelCode')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetDataModelConfigInfoResponseBody(TeaModel):
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


class GetDataModelConfigInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataModelConfigInfoResponseBody = None,
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
            temp_model = GetDataModelConfigInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistoryDataCountRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        end_time: int = None,
        key: str = None,
        product_key: str = None,
        start_time: int = None,
    ):
        self.api_version = api_version
        self.end_time = end_time
        self.key = key
        self.product_key = product_key
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetHistoryDataCountResponseBody(TeaModel):
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


class GetHistoryDataCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHistoryDataCountResponseBody = None,
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
            temp_model = GetHistoryDataCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistoryDataListRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        current_page: int = None,
        end_time: int = None,
        key: str = None,
        page_size: int = None,
        product_key: str = None,
        start_time: int = None,
    ):
        self.api_version = api_version
        self.current_page = current_page
        self.end_time = end_time
        self.key = key
        self.page_size = page_size
        self.product_key = product_key
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetHistoryDataListResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetHistoryDataListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetHistoryDataListResponseBodyData = None,
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
            temp_model = GetHistoryDataListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHistoryDataListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHistoryDataListResponseBody = None,
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
            temp_model = GetHistoryDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDependentDataModelsRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        product_key: str = None,
    ):
        self.api_version = api_version
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ListDependentDataModelsResponseBodyDataDataModelInfo(TeaModel):
    def __init__(
        self,
        data_model_code: str = None,
        data_model_name: str = None,
    ):
        self.data_model_code = data_model_code
        self.data_model_name = data_model_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_model_code is not None:
            result['DataModelCode'] = self.data_model_code
        if self.data_model_name is not None:
            result['DataModelName'] = self.data_model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataModelCode') is not None:
            self.data_model_code = m.get('DataModelCode')
        if m.get('DataModelName') is not None:
            self.data_model_name = m.get('DataModelName')
        return self


class ListDependentDataModelsResponseBodyData(TeaModel):
    def __init__(
        self,
        data_model_info: List[ListDependentDataModelsResponseBodyDataDataModelInfo] = None,
    ):
        self.data_model_info = data_model_info

    def validate(self):
        if self.data_model_info:
            for k in self.data_model_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModelInfo'] = []
        if self.data_model_info is not None:
            for k in self.data_model_info:
                result['DataModelInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_model_info = []
        if m.get('DataModelInfo') is not None:
            for k in m.get('DataModelInfo'):
                temp_model = ListDependentDataModelsResponseBodyDataDataModelInfo()
                self.data_model_info.append(temp_model.from_map(k))
        return self


class ListDependentDataModelsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListDependentDataModelsResponseBodyData = None,
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
            temp_model = ListDependentDataModelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDependentDataModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDependentDataModelsResponseBody = None,
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
            temp_model = ListDependentDataModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        device_group_id: str = None,
        iot_id: str = None,
        num: int = None,
        size: int = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.device_group_id = device_group_id
        self.iot_id = iot_id
        self.num = num
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.num is not None:
            result['Num'] = self.num
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListDeviceResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        iot_id: str = None,
        last_save_time: int = None,
        status: str = None,
    ):
        self.device_id = device_id
        self.iot_id = iot_id
        self.last_save_time = last_save_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.last_save_time is not None:
            result['LastSaveTime'] = self.last_save_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('LastSaveTime') is not None:
            self.last_save_time = m.get('LastSaveTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListDeviceResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListDeviceResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListDeviceResponseBodyData = None,
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
            temp_model = ListDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceResponseBody = None,
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
            temp_model = ListDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        num: int = None,
        product_key: str = None,
        size: int = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.num = num
        self.product_key = product_key
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.num is not None:
            result['Num'] = self.num
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListDeviceGroupResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        authorize_type: str = None,
        device_group_id: str = None,
        owner_name: str = None,
        owner_uid: str = None,
        product_key: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.authorize_type = authorize_type
        self.device_group_id = device_group_id
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.product_key = product_key
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize_type is not None:
            result['AuthorizeType'] = self.authorize_type
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizeType') is not None:
            self.authorize_type = m.get('AuthorizeType')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDeviceGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListDeviceGroupResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListDeviceGroupResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListDeviceGroupResponseBodyData = None,
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
            temp_model = ListDeviceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceGroupResponseBody = None,
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
            temp_model = ListDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMPCoSPhaseRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        name: str = None,
        num: int = None,
        phase_group_id: str = None,
        size: int = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.name = name
        self.num = num
        self.phase_group_id = phase_group_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListMPCoSPhaseResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        access_permission: int = None,
        name: str = None,
        phase_id: str = None,
        remark: str = None,
    ):
        self.access_permission = access_permission
        self.name = name
        self.phase_id = phase_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_permission is not None:
            result['AccessPermission'] = self.access_permission
        if self.name is not None:
            result['Name'] = self.name
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPermission') is not None:
            self.access_permission = m.get('AccessPermission')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ListMPCoSPhaseResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListMPCoSPhaseResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListMPCoSPhaseResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMPCoSPhaseResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListMPCoSPhaseResponseBodyData = None,
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
            temp_model = ListMPCoSPhaseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMPCoSPhaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMPCoSPhaseResponseBody = None,
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
            temp_model = ListMPCoSPhaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMPCoSPhaseGroupRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        name: str = None,
        num: int = None,
        size: int = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.name = name
        self.num = num
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListMPCoSPhaseGroupResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        name: str = None,
        phase_group_id: str = None,
        remark: str = None,
    ):
        self.name = name
        self.phase_group_id = phase_group_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ListMPCoSPhaseGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListMPCoSPhaseGroupResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListMPCoSPhaseGroupResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMPCoSPhaseGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListMPCoSPhaseGroupResponseBodyData = None,
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
            temp_model = ListMPCoSPhaseGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMPCoSPhaseGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMPCoSPhaseGroupResponseBody = None,
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
            temp_model = ListMPCoSPhaseGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMPCoSPhaseHistoryRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        data_key: str = None,
        end_time: int = None,
        num: int = None,
        phase_group_id: str = None,
        phase_id: str = None,
        size: int = None,
        start_time: int = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.data_key = data_key
        self.end_time = end_time
        self.num = num
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id
        self.size = size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_key is not None:
            result['DataKey'] = self.data_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.num is not None:
            result['Num'] = self.num
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataKey') is not None:
            self.data_key = m.get('DataKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListMPCoSPhaseHistoryResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        block_hash: str = None,
        block_number: int = None,
        data_hash: str = None,
        data_seq: str = None,
        data_value: str = None,
        iot_id: str = None,
        previous_hash: str = None,
        product_key: str = None,
        timestamp: int = None,
        transaction_hash: str = None,
    ):
        self.block_hash = block_hash
        self.block_number = block_number
        self.data_hash = data_hash
        self.data_seq = data_seq
        self.data_value = data_value
        self.iot_id = iot_id
        self.previous_hash = previous_hash
        self.product_key = product_key
        self.timestamp = timestamp
        self.transaction_hash = transaction_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.block_number is not None:
            result['BlockNumber'] = self.block_number
        if self.data_hash is not None:
            result['DataHash'] = self.data_hash
        if self.data_seq is not None:
            result['DataSeq'] = self.data_seq
        if self.data_value is not None:
            result['DataValue'] = self.data_value
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.previous_hash is not None:
            result['PreviousHash'] = self.previous_hash
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.transaction_hash is not None:
            result['TransactionHash'] = self.transaction_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('BlockNumber') is not None:
            self.block_number = m.get('BlockNumber')
        if m.get('DataHash') is not None:
            self.data_hash = m.get('DataHash')
        if m.get('DataSeq') is not None:
            self.data_seq = m.get('DataSeq')
        if m.get('DataValue') is not None:
            self.data_value = m.get('DataValue')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PreviousHash') is not None:
            self.previous_hash = m.get('PreviousHash')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TransactionHash') is not None:
            self.transaction_hash = m.get('TransactionHash')
        return self


class ListMPCoSPhaseHistoryResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListMPCoSPhaseHistoryResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListMPCoSPhaseHistoryResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMPCoSPhaseHistoryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListMPCoSPhaseHistoryResponseBodyData = None,
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
            temp_model = ListMPCoSPhaseHistoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMPCoSPhaseHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMPCoSPhaseHistoryResponseBody = None,
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
            temp_model = ListMPCoSPhaseHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMemberRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        member_uid: str = None,
        num: int = None,
        size: int = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.member_uid = member_uid
        self.num = num
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.num is not None:
            result['Num'] = self.num
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListMemberResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        member_contact: str = None,
        member_id: str = None,
        member_name: str = None,
        member_phone: str = None,
        member_uid: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.member_contact = member_contact
        self.member_id = member_id
        self.member_name = member_name
        self.member_phone = member_phone
        self.member_uid = member_uid
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_contact is not None:
            result['MemberContact'] = self.member_contact
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.member_phone is not None:
            result['MemberPhone'] = self.member_phone
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberContact') is not None:
            self.member_contact = m.get('MemberContact')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('MemberPhone') is not None:
            self.member_phone = m.get('MemberPhone')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListMemberResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListMemberResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListMemberResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListMemberResponseBodyData = None,
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
            temp_model = ListMemberResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMemberResponseBody = None,
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
            temp_model = ListMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMultiPartyCollaborationChainRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        name: str = None,
        num: int = None,
        size: int = None,
    ):
        self.api_version = api_version
        self.name = name
        self.num = num
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListMultiPartyCollaborationChainResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        name: str = None,
        remark: str = None,
        role_type: str = None,
    ):
        self.biz_chain_id = biz_chain_id
        self.name = name
        self.remark = remark
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class ListMultiPartyCollaborationChainResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListMultiPartyCollaborationChainResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListMultiPartyCollaborationChainResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMultiPartyCollaborationChainResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListMultiPartyCollaborationChainResponseBodyData = None,
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
            temp_model = ListMultiPartyCollaborationChainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMultiPartyCollaborationChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMultiPartyCollaborationChainResponseBody = None,
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
            temp_model = ListMultiPartyCollaborationChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPSMemberDataTypeCodeRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        member_uid: str = None,
        num: int = None,
        size: int = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.member_uid = member_uid
        self.num = num
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.num is not None:
            result['Num'] = self.num
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListPSMemberDataTypeCodeResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        data_type_code: str = None,
        member_id: str = None,
        member_name: str = None,
        member_uid: str = None,
    ):
        self.data_type_code = data_type_code
        self.member_id = member_id
        self.member_name = member_name
        self.member_uid = member_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type_code is not None:
            result['DataTypeCode'] = self.data_type_code
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTypeCode') is not None:
            self.data_type_code = m.get('DataTypeCode')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        return self


class ListPSMemberDataTypeCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListPSMemberDataTypeCodeResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListPSMemberDataTypeCodeResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListPSMemberDataTypeCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListPSMemberDataTypeCodeResponseBodyData = None,
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
            temp_model = ListPSMemberDataTypeCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPSMemberDataTypeCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPSMemberDataTypeCodeResponseBody = None,
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
            temp_model = ListPSMemberDataTypeCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProofChainRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        name: str = None,
        num: int = None,
        size: int = None,
    ):
        self.api_version = api_version
        self.name = name
        self.num = num
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListProofChainResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        biz_chain_code: str = None,
        biz_chain_id: str = None,
        data_type_code: str = None,
        name: str = None,
        remark: str = None,
        role_type: str = None,
    ):
        self.biz_chain_code = biz_chain_code
        self.biz_chain_id = biz_chain_id
        self.data_type_code = data_type_code
        self.name = name
        self.remark = remark
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_code is not None:
            result['BizChainCode'] = self.biz_chain_code
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_type_code is not None:
            result['DataTypeCode'] = self.data_type_code
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainCode') is not None:
            self.biz_chain_code = m.get('BizChainCode')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataTypeCode') is not None:
            self.data_type_code = m.get('DataTypeCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class ListProofChainResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListProofChainResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListProofChainResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListProofChainResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListProofChainResponseBodyData = None,
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
            temp_model = ListProofChainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProofChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProofChainResponseBody = None,
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
            temp_model = ListProofChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockMemberRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        member_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class LockMemberResponseBody(TeaModel):
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


class LockMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LockMemberResponseBody = None,
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
            temp_model = LockMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMPCoSPhaseRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        name: str = None,
        phase_id: str = None,
        remark: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.name = name
        self.phase_id = phase_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ModifyMPCoSPhaseResponseBody(TeaModel):
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


class ModifyMPCoSPhaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyMPCoSPhaseResponseBody = None,
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
            temp_model = ModifyMPCoSPhaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMPCoSPhaseGroupRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        name: str = None,
        phase_group_id: str = None,
        remark: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.name = name
        self.phase_group_id = phase_group_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ModifyMPCoSPhaseGroupResponseBody(TeaModel):
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


class ModifyMPCoSPhaseGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyMPCoSPhaseGroupResponseBody = None,
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
            temp_model = ModifyMPCoSPhaseGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMemberRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        member_contact: str = None,
        member_id: str = None,
        member_name: str = None,
        member_phone: str = None,
        member_uid: str = None,
        remark: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.member_contact = member_contact
        self.member_id = member_id
        self.member_name = member_name
        self.member_phone = member_phone
        self.member_uid = member_uid
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.member_contact is not None:
            result['MemberContact'] = self.member_contact
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.member_phone is not None:
            result['MemberPhone'] = self.member_phone
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('MemberContact') is not None:
            self.member_contact = m.get('MemberContact')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('MemberPhone') is not None:
            self.member_phone = m.get('MemberPhone')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ModifyMemberResponseBody(TeaModel):
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


class ModifyMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyMemberResponseBody = None,
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
            temp_model = ModifyMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        authorize_type: str = None,
        biz_chain_id: str = None,
        device_group_name: str = None,
        product_key: str = None,
        remark: str = None,
    ):
        self.api_version = api_version
        self.authorize_type = authorize_type
        self.biz_chain_id = biz_chain_id
        self.device_group_name = device_group_name
        self.product_key = product_key
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.authorize_type is not None:
            result['AuthorizeType'] = self.authorize_type
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('AuthorizeType') is not None:
            self.authorize_type = m.get('AuthorizeType')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class RegisterDeviceGroupResponseBody(TeaModel):
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


class RegisterDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterDeviceGroupResponseBody = None,
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
            temp_model = RegisterDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDataRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        key: str = None,
        product_key: str = None,
        value: str = None,
    ):
        self.api_version = api_version
        self.key = key
        self.product_key = product_key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.key is not None:
            result['Key'] = self.key
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetDataResponseBody(TeaModel):
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


class SetDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDataResponseBody = None,
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
            temp_model = SetDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDataWithSignatureRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        iot_auth_type: str = None,
        iot_data_digest: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        iot_signature: str = None,
        key: str = None,
        product_key: str = None,
        value: str = None,
    ):
        self.api_version = api_version
        self.iot_auth_type = iot_auth_type
        self.iot_data_digest = iot_data_digest
        self.iot_id = iot_id
        self.iot_id_service_provider = iot_id_service_provider
        self.iot_id_source = iot_id_source
        self.iot_signature = iot_signature
        self.key = key
        self.product_key = product_key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.iot_signature is not None:
            result['IotSignature'] = self.iot_signature
        if self.key is not None:
            result['Key'] = self.key
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('IotSignature') is not None:
            self.iot_signature = m.get('IotSignature')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetDataWithSignatureResponseBody(TeaModel):
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


class SetDataWithSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDataWithSignatureResponseBody = None,
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
            temp_model = SetDataWithSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnAuthorizeDeviceRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        device_group_id: str = None,
        device_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.device_group_id = device_group_id
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class UnAuthorizeDeviceResponseBody(TeaModel):
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


class UnAuthorizeDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnAuthorizeDeviceResponseBody = None,
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
            temp_model = UnAuthorizeDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnAuthorizeDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        device_group_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.device_group_id = device_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        return self


class UnAuthorizeDeviceGroupResponseBody(TeaModel):
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


class UnAuthorizeDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnAuthorizeDeviceGroupResponseBody = None,
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
            temp_model = UnAuthorizeDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnLockMemberRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        member_id: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class UnLockMemberResponseBody(TeaModel):
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


class UnLockMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnLockMemberResponseBody = None,
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
            temp_model = UnLockMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMPCoSAuthorizedInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        authorized_phase_list: Dict[str, Any] = None,
        biz_chain_id: str = None,
        member_id: str = None,
        phase_group_id: str = None,
    ):
        self.api_version = api_version
        self.authorized_phase_list = authorized_phase_list
        self.biz_chain_id = biz_chain_id
        self.member_id = member_id
        self.phase_group_id = phase_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.authorized_phase_list is not None:
            result['AuthorizedPhaseList'] = self.authorized_phase_list
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('AuthorizedPhaseList') is not None:
            self.authorized_phase_list = m.get('AuthorizedPhaseList')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        return self


class UpdateMPCoSAuthorizedInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        authorized_phase_list_shrink: str = None,
        biz_chain_id: str = None,
        member_id: str = None,
        phase_group_id: str = None,
    ):
        self.api_version = api_version
        self.authorized_phase_list_shrink = authorized_phase_list_shrink
        self.biz_chain_id = biz_chain_id
        self.member_id = member_id
        self.phase_group_id = phase_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.authorized_phase_list_shrink is not None:
            result['AuthorizedPhaseList'] = self.authorized_phase_list_shrink
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('AuthorizedPhaseList') is not None:
            self.authorized_phase_list_shrink = m.get('AuthorizedPhaseList')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        return self


class UpdateMPCoSAuthorizedInfoResponseBody(TeaModel):
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


class UpdateMPCoSAuthorizedInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMPCoSAuthorizedInfoResponseBody = None,
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
            temp_model = UpdateMPCoSAuthorizedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadMPCoSPhaseDigestInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        data_key: str = None,
        data_seq: str = None,
        phase_data: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
        related_data_list: Dict[str, Any] = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.data_key = data_key
        self.data_seq = data_seq
        self.phase_data = phase_data
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id
        self.related_data_list = related_data_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_key is not None:
            result['DataKey'] = self.data_key
        if self.data_seq is not None:
            result['DataSeq'] = self.data_seq
        if self.phase_data is not None:
            result['PhaseData'] = self.phase_data
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.related_data_list is not None:
            result['RelatedDataList'] = self.related_data_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataKey') is not None:
            self.data_key = m.get('DataKey')
        if m.get('DataSeq') is not None:
            self.data_seq = m.get('DataSeq')
        if m.get('PhaseData') is not None:
            self.phase_data = m.get('PhaseData')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('RelatedDataList') is not None:
            self.related_data_list = m.get('RelatedDataList')
        return self


class UploadMPCoSPhaseDigestInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        data_key: str = None,
        data_seq: str = None,
        phase_data: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
        related_data_list_shrink: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.data_key = data_key
        self.data_seq = data_seq
        self.phase_data = phase_data
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id
        self.related_data_list_shrink = related_data_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_key is not None:
            result['DataKey'] = self.data_key
        if self.data_seq is not None:
            result['DataSeq'] = self.data_seq
        if self.phase_data is not None:
            result['PhaseData'] = self.phase_data
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.related_data_list_shrink is not None:
            result['RelatedDataList'] = self.related_data_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataKey') is not None:
            self.data_key = m.get('DataKey')
        if m.get('DataSeq') is not None:
            self.data_seq = m.get('DataSeq')
        if m.get('PhaseData') is not None:
            self.phase_data = m.get('PhaseData')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('RelatedDataList') is not None:
            self.related_data_list_shrink = m.get('RelatedDataList')
        return self


class UploadMPCoSPhaseDigestInfoResponseBody(TeaModel):
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


class UploadMPCoSPhaseDigestInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadMPCoSPhaseDigestInfoResponseBody = None,
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
            temp_model = UploadMPCoSPhaseDigestInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadMPCoSPhaseDigestInfoByDeviceRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        data_key: str = None,
        data_seq: str = None,
        iot_auth_type: str = None,
        iot_data_digest: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        iot_signature: str = None,
        phase_data: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
        related_data_list: Dict[str, Any] = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.data_key = data_key
        self.data_seq = data_seq
        self.iot_auth_type = iot_auth_type
        self.iot_data_digest = iot_data_digest
        self.iot_id = iot_id
        self.iot_id_service_provider = iot_id_service_provider
        self.iot_id_source = iot_id_source
        self.iot_signature = iot_signature
        self.phase_data = phase_data
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id
        self.related_data_list = related_data_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_key is not None:
            result['DataKey'] = self.data_key
        if self.data_seq is not None:
            result['DataSeq'] = self.data_seq
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.iot_signature is not None:
            result['IotSignature'] = self.iot_signature
        if self.phase_data is not None:
            result['PhaseData'] = self.phase_data
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.related_data_list is not None:
            result['RelatedDataList'] = self.related_data_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataKey') is not None:
            self.data_key = m.get('DataKey')
        if m.get('DataSeq') is not None:
            self.data_seq = m.get('DataSeq')
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('IotSignature') is not None:
            self.iot_signature = m.get('IotSignature')
        if m.get('PhaseData') is not None:
            self.phase_data = m.get('PhaseData')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('RelatedDataList') is not None:
            self.related_data_list = m.get('RelatedDataList')
        return self


class UploadMPCoSPhaseDigestInfoByDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        data_key: str = None,
        data_seq: str = None,
        iot_auth_type: str = None,
        iot_data_digest: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        iot_signature: str = None,
        phase_data: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
        related_data_list_shrink: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.data_key = data_key
        self.data_seq = data_seq
        self.iot_auth_type = iot_auth_type
        self.iot_data_digest = iot_data_digest
        self.iot_id = iot_id
        self.iot_id_service_provider = iot_id_service_provider
        self.iot_id_source = iot_id_source
        self.iot_signature = iot_signature
        self.phase_data = phase_data
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id
        self.related_data_list_shrink = related_data_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_key is not None:
            result['DataKey'] = self.data_key
        if self.data_seq is not None:
            result['DataSeq'] = self.data_seq
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.iot_signature is not None:
            result['IotSignature'] = self.iot_signature
        if self.phase_data is not None:
            result['PhaseData'] = self.phase_data
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.related_data_list_shrink is not None:
            result['RelatedDataList'] = self.related_data_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataKey') is not None:
            self.data_key = m.get('DataKey')
        if m.get('DataSeq') is not None:
            self.data_seq = m.get('DataSeq')
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('IotSignature') is not None:
            self.iot_signature = m.get('IotSignature')
        if m.get('PhaseData') is not None:
            self.phase_data = m.get('PhaseData')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('RelatedDataList') is not None:
            self.related_data_list_shrink = m.get('RelatedDataList')
        return self


class UploadMPCoSPhaseDigestInfoByDeviceResponseBody(TeaModel):
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


class UploadMPCoSPhaseDigestInfoByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadMPCoSPhaseDigestInfoByDeviceResponseBody = None,
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
            temp_model = UploadMPCoSPhaseDigestInfoByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadMPCoSPhaseTextInfoRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        data_key: str = None,
        data_seq: str = None,
        phase_data: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
        related_data_list: Dict[str, Any] = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.data_key = data_key
        self.data_seq = data_seq
        self.phase_data = phase_data
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id
        self.related_data_list = related_data_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_key is not None:
            result['DataKey'] = self.data_key
        if self.data_seq is not None:
            result['DataSeq'] = self.data_seq
        if self.phase_data is not None:
            result['PhaseData'] = self.phase_data
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.related_data_list is not None:
            result['RelatedDataList'] = self.related_data_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataKey') is not None:
            self.data_key = m.get('DataKey')
        if m.get('DataSeq') is not None:
            self.data_seq = m.get('DataSeq')
        if m.get('PhaseData') is not None:
            self.phase_data = m.get('PhaseData')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('RelatedDataList') is not None:
            self.related_data_list = m.get('RelatedDataList')
        return self


class UploadMPCoSPhaseTextInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        data_key: str = None,
        data_seq: str = None,
        phase_data: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
        related_data_list_shrink: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.data_key = data_key
        self.data_seq = data_seq
        self.phase_data = phase_data
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id
        self.related_data_list_shrink = related_data_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_key is not None:
            result['DataKey'] = self.data_key
        if self.data_seq is not None:
            result['DataSeq'] = self.data_seq
        if self.phase_data is not None:
            result['PhaseData'] = self.phase_data
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.related_data_list_shrink is not None:
            result['RelatedDataList'] = self.related_data_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataKey') is not None:
            self.data_key = m.get('DataKey')
        if m.get('DataSeq') is not None:
            self.data_seq = m.get('DataSeq')
        if m.get('PhaseData') is not None:
            self.phase_data = m.get('PhaseData')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('RelatedDataList') is not None:
            self.related_data_list_shrink = m.get('RelatedDataList')
        return self


class UploadMPCoSPhaseTextInfoResponseBody(TeaModel):
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


class UploadMPCoSPhaseTextInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadMPCoSPhaseTextInfoResponseBody = None,
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
            temp_model = UploadMPCoSPhaseTextInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadMPCoSPhaseTextInfoByDeviceRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        data_key: str = None,
        data_seq: str = None,
        iot_auth_type: str = None,
        iot_data_digest: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        iot_signature: str = None,
        phase_data: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
        related_data_list: Dict[str, Any] = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.data_key = data_key
        self.data_seq = data_seq
        self.iot_auth_type = iot_auth_type
        self.iot_data_digest = iot_data_digest
        self.iot_id = iot_id
        self.iot_id_service_provider = iot_id_service_provider
        self.iot_id_source = iot_id_source
        self.iot_signature = iot_signature
        self.phase_data = phase_data
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id
        self.related_data_list = related_data_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_key is not None:
            result['DataKey'] = self.data_key
        if self.data_seq is not None:
            result['DataSeq'] = self.data_seq
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.iot_signature is not None:
            result['IotSignature'] = self.iot_signature
        if self.phase_data is not None:
            result['PhaseData'] = self.phase_data
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.related_data_list is not None:
            result['RelatedDataList'] = self.related_data_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataKey') is not None:
            self.data_key = m.get('DataKey')
        if m.get('DataSeq') is not None:
            self.data_seq = m.get('DataSeq')
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('IotSignature') is not None:
            self.iot_signature = m.get('IotSignature')
        if m.get('PhaseData') is not None:
            self.phase_data = m.get('PhaseData')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('RelatedDataList') is not None:
            self.related_data_list = m.get('RelatedDataList')
        return self


class UploadMPCoSPhaseTextInfoByDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        biz_chain_id: str = None,
        data_key: str = None,
        data_seq: str = None,
        iot_auth_type: str = None,
        iot_data_digest: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        iot_signature: str = None,
        phase_data: str = None,
        phase_group_id: str = None,
        phase_id: str = None,
        related_data_list_shrink: str = None,
    ):
        self.api_version = api_version
        self.biz_chain_id = biz_chain_id
        self.data_key = data_key
        self.data_seq = data_seq
        self.iot_auth_type = iot_auth_type
        self.iot_data_digest = iot_data_digest
        self.iot_id = iot_id
        self.iot_id_service_provider = iot_id_service_provider
        self.iot_id_source = iot_id_source
        self.iot_signature = iot_signature
        self.phase_data = phase_data
        self.phase_group_id = phase_group_id
        self.phase_id = phase_id
        self.related_data_list_shrink = related_data_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.data_key is not None:
            result['DataKey'] = self.data_key
        if self.data_seq is not None:
            result['DataSeq'] = self.data_seq
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.iot_signature is not None:
            result['IotSignature'] = self.iot_signature
        if self.phase_data is not None:
            result['PhaseData'] = self.phase_data
        if self.phase_group_id is not None:
            result['PhaseGroupId'] = self.phase_group_id
        if self.phase_id is not None:
            result['PhaseId'] = self.phase_id
        if self.related_data_list_shrink is not None:
            result['RelatedDataList'] = self.related_data_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('DataKey') is not None:
            self.data_key = m.get('DataKey')
        if m.get('DataSeq') is not None:
            self.data_seq = m.get('DataSeq')
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('IotSignature') is not None:
            self.iot_signature = m.get('IotSignature')
        if m.get('PhaseData') is not None:
            self.phase_data = m.get('PhaseData')
        if m.get('PhaseGroupId') is not None:
            self.phase_group_id = m.get('PhaseGroupId')
        if m.get('PhaseId') is not None:
            self.phase_id = m.get('PhaseId')
        if m.get('RelatedDataList') is not None:
            self.related_data_list_shrink = m.get('RelatedDataList')
        return self


class UploadMPCoSPhaseTextInfoByDeviceResponseBody(TeaModel):
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


class UploadMPCoSPhaseTextInfoByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadMPCoSPhaseTextInfoByDeviceResponseBody = None,
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
            temp_model = UploadMPCoSPhaseTextInfoByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



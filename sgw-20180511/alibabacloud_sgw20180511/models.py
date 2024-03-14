# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ActivateAllInOneGatewayRequest(TeaModel):
    def __init__(
        self,
        client_uuid: str = None,
        device_number: str = None,
        gateway_id: str = None,
        model: str = None,
        security_token: str = None,
        serial_number: str = None,
    ):
        self.client_uuid = client_uuid
        self.device_number = device_number
        self.gateway_id = gateway_id
        self.model = model
        self.security_token = security_token
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_uuid is not None:
            result['ClientUUID'] = self.client_uuid
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.model is not None:
            result['Model'] = self.model
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUUID') is not None:
            self.client_uuid = m.get('ClientUUID')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class ActivateAllInOneGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gateway_id: str = None,
        license_content: str = None,
        message: str = None,
        region_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.gateway_id = gateway_id
        self.license_content = license_content
        self.message = message
        self.region_id = region_id
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
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.license_content is not None:
            result['LicenseContent'] = self.license_content
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('LicenseContent') is not None:
            self.license_content = m.get('LicenseContent')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActivateAllInOneGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateAllInOneGatewayResponseBody = None,
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
            temp_model = ActivateAllInOneGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ActivateGatewayRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        client_uuid: str = None,
        model: str = None,
        security_token: str = None,
        serial_number: str = None,
        token: str = None,
        type: str = None,
    ):
        self.category = category
        self.client_uuid = client_uuid
        self.model = model
        self.security_token = security_token
        self.serial_number = serial_number
        self.token = token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_uuid is not None:
            result['ClientUUID'] = self.client_uuid
        if self.model is not None:
            result['Model'] = self.model
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientUUID') is not None:
            self.client_uuid = m.get('ClientUUID')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ActivateGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gateway_id: str = None,
        message: str = None,
        region_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.gateway_id = gateway_id
        self.message = message
        self.region_id = region_id
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
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActivateGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateGatewayResponseBody = None,
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
            temp_model = ActivateGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSharesToExpressSyncRequest(TeaModel):
    def __init__(
        self,
        express_sync_id: str = None,
        gateway_shares: str = None,
        security_token: str = None,
    ):
        self.express_sync_id = express_sync_id
        self.gateway_shares = gateway_shares
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.express_sync_id is not None:
            result['ExpressSyncId'] = self.express_sync_id
        if self.gateway_shares is not None:
            result['GatewayShares'] = self.gateway_shares
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressSyncId') is not None:
            self.express_sync_id = m.get('ExpressSyncId')
        if m.get('GatewayShares') is not None:
            self.gateway_shares = m.get('GatewayShares')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class AddSharesToExpressSyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        mns_full_sync_delay: int = None,
        mns_inner_endpoint: str = None,
        mns_public_endpoint: str = None,
        mns_queues: str = None,
        mns_topic: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.mns_full_sync_delay = mns_full_sync_delay
        self.mns_inner_endpoint = mns_inner_endpoint
        self.mns_public_endpoint = mns_public_endpoint
        self.mns_queues = mns_queues
        self.mns_topic = mns_topic
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.mns_full_sync_delay is not None:
            result['MnsFullSyncDelay'] = self.mns_full_sync_delay
        if self.mns_inner_endpoint is not None:
            result['MnsInnerEndpoint'] = self.mns_inner_endpoint
        if self.mns_public_endpoint is not None:
            result['MnsPublicEndpoint'] = self.mns_public_endpoint
        if self.mns_queues is not None:
            result['MnsQueues'] = self.mns_queues
        if self.mns_topic is not None:
            result['MnsTopic'] = self.mns_topic
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MnsFullSyncDelay') is not None:
            self.mns_full_sync_delay = m.get('MnsFullSyncDelay')
        if m.get('MnsInnerEndpoint') is not None:
            self.mns_inner_endpoint = m.get('MnsInnerEndpoint')
        if m.get('MnsPublicEndpoint') is not None:
            self.mns_public_endpoint = m.get('MnsPublicEndpoint')
        if m.get('MnsQueues') is not None:
            self.mns_queues = m.get('MnsQueues')
        if m.get('MnsTopic') is not None:
            self.mns_topic = m.get('MnsTopic')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddSharesToExpressSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddSharesToExpressSyncResponseBody = None,
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
            temp_model = AddSharesToExpressSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTagsToGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
        tags: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AddTagsToGatewayResponseBody(TeaModel):
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


class AddTagsToGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddTagsToGatewayResponseBody = None,
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
            temp_model = AddTagsToGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckActivationKeyRequest(TeaModel):
    def __init__(
        self,
        crypt_key: str = None,
        crypt_text: str = None,
        gateway_id: str = None,
        security_token: str = None,
        token: str = None,
    ):
        self.crypt_key = crypt_key
        self.crypt_text = crypt_text
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crypt_key is not None:
            result['CryptKey'] = self.crypt_key
        if self.crypt_text is not None:
            result['CryptText'] = self.crypt_text
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CryptKey') is not None:
            self.crypt_key = m.get('CryptKey')
        if m.get('CryptText') is not None:
            self.crypt_text = m.get('CryptText')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CheckActivationKeyResponseBody(TeaModel):
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


class CheckActivationKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckActivationKeyResponseBody = None,
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
            temp_model = CheckActivationKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckBlockVolumeNameRequest(TeaModel):
    def __init__(
        self,
        bucket_endpoint: str = None,
        bucket_name: str = None,
        security_token: str = None,
        volume_name: str = None,
    ):
        # Bucket Endpoint。
        self.bucket_endpoint = bucket_endpoint
        self.bucket_name = bucket_name
        self.security_token = security_token
        self.volume_name = volume_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_endpoint is not None:
            result['BucketEndpoint'] = self.bucket_endpoint
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.volume_name is not None:
            result['VolumeName'] = self.volume_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketEndpoint') is not None:
            self.bucket_endpoint = m.get('BucketEndpoint')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VolumeName') is not None:
            self.volume_name = m.get('VolumeName')
        return self


class CheckBlockVolumeNameResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_already_exist: bool = None,
        is_require_recovery: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.is_already_exist = is_already_exist
        self.is_require_recovery = is_require_recovery
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
        if self.is_already_exist is not None:
            result['IsAlreadyExist'] = self.is_already_exist
        if self.is_require_recovery is not None:
            result['IsRequireRecovery'] = self.is_require_recovery
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
        if m.get('IsAlreadyExist') is not None:
            self.is_already_exist = m.get('IsAlreadyExist')
        if m.get('IsRequireRecovery') is not None:
            self.is_require_recovery = m.get('IsRequireRecovery')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckBlockVolumeNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckBlockVolumeNameResponseBody = None,
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
            temp_model = CheckBlockVolumeNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckGatewayEssdSupportRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CheckGatewayEssdSupportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_service_affect: bool = None,
        is_support_essd: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.is_service_affect = is_service_affect
        self.is_support_essd = is_support_essd
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
        if self.is_service_affect is not None:
            result['IsServiceAffect'] = self.is_service_affect
        if self.is_support_essd is not None:
            result['IsSupportEssd'] = self.is_support_essd
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
        if m.get('IsServiceAffect') is not None:
            self.is_service_affect = m.get('IsServiceAffect')
        if m.get('IsSupportEssd') is not None:
            self.is_support_essd = m.get('IsSupportEssd')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckGatewayEssdSupportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckGatewayEssdSupportResponseBody = None,
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
            temp_model = CheckGatewayEssdSupportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMnsServiceRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
    ):
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CheckMnsServiceResponseBody(TeaModel):
    def __init__(
        self,
        check_message: str = None,
        code: str = None,
        is_enabled: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.check_message = check_message
        self.code = code
        self.is_enabled = is_enabled
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
        if self.check_message is not None:
            result['CheckMessage'] = self.check_message
        if self.code is not None:
            result['Code'] = self.code
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckMessage') is not None:
            self.check_message = m.get('CheckMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckMnsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckMnsServiceResponseBody = None,
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
            temp_model = CheckMnsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckRoleRequest(TeaModel):
    def __init__(
        self,
        role_type: str = None,
        security_token: str = None,
    ):
        self.role_type = role_type
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CheckRoleResponseBody(TeaModel):
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


class CheckRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckRoleResponseBody = None,
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
            temp_model = CheckRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckSlrRoleRequest(TeaModel):
    def __init__(
        self,
        create_if_not_exist: bool = None,
        role_name: str = None,
        security_token: str = None,
    ):
        self.create_if_not_exist = create_if_not_exist
        self.role_name = role_name
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_if_not_exist is not None:
            result['CreateIfNotExist'] = self.create_if_not_exist
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateIfNotExist') is not None:
            self.create_if_not_exist = m.get('CreateIfNotExist')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CheckSlrRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        exist: bool = None,
        message: str = None,
        request_id: str = None,
        require_old_way_check: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.exist = exist
        self.message = message
        self.request_id = request_id
        self.require_old_way_check = require_old_way_check
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
        if self.exist is not None:
            result['Exist'] = self.exist
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.require_old_way_check is not None:
            result['RequireOldWayCheck'] = self.require_old_way_check
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequireOldWayCheck') is not None:
            self.require_old_way_check = m.get('RequireOldWayCheck')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckSlrRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckSlrRoleResponseBody = None,
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
            temp_model = CheckSlrRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUpgradeVersionRequest(TeaModel):
    def __init__(
        self,
        client_uuid: str = None,
        gateway_id: str = None,
        gateway_version: str = None,
        security_token: str = None,
    ):
        self.client_uuid = client_uuid
        self.gateway_id = gateway_id
        self.gateway_version = gateway_version
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_uuid is not None:
            result['ClientUUID'] = self.client_uuid
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_version is not None:
            result['GatewayVersion'] = self.gateway_version
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUUID') is not None:
            self.client_uuid = m.get('ClientUUID')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayVersion') is not None:
            self.gateway_version = m.get('GatewayVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CheckUpgradeVersionResponseBodyPatchesPatch(TeaModel):
    def __init__(
        self,
        internal_url: str = None,
        md5: str = None,
        name: str = None,
        url: str = None,
    ):
        self.internal_url = internal_url
        self.md5 = md5
        self.name = name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internal_url is not None:
            result['InternalUrl'] = self.internal_url
        if self.md5 is not None:
            result['MD5'] = self.md5
        if self.name is not None:
            result['Name'] = self.name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternalUrl') is not None:
            self.internal_url = m.get('InternalUrl')
        if m.get('MD5') is not None:
            self.md5 = m.get('MD5')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CheckUpgradeVersionResponseBodyPatches(TeaModel):
    def __init__(
        self,
        patch: List[CheckUpgradeVersionResponseBodyPatchesPatch] = None,
    ):
        self.patch = patch

    def validate(self):
        if self.patch:
            for k in self.patch:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Patch'] = []
        if self.patch is not None:
            for k in self.patch:
                result['Patch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.patch = []
        if m.get('Patch') is not None:
            for k in m.get('Patch'):
                temp_model = CheckUpgradeVersionResponseBodyPatchesPatch()
                self.patch.append(temp_model.from_map(k))
        return self


class CheckUpgradeVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        latest_version: str = None,
        message: str = None,
        option: str = None,
        patches: CheckUpgradeVersionResponseBodyPatches = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.latest_version = latest_version
        self.message = message
        self.option = option
        self.patches = patches
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.patches:
            self.patches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.message is not None:
            result['Message'] = self.message
        if self.option is not None:
            result['Option'] = self.option
        if self.patches is not None:
            result['Patches'] = self.patches.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('Patches') is not None:
            temp_model = CheckUpgradeVersionResponseBodyPatches()
            self.patches = temp_model.from_map(m['Patches'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckUpgradeVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckUpgradeVersionResponseBody = None,
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
            temp_model = CheckUpgradeVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCacheRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        gateway_id: str = None,
        security_token: str = None,
        size_in_gb: int = None,
    ):
        self.category = category
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.size_in_gb = size_in_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.size_in_gb is not None:
            result['SizeInGB'] = self.size_in_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SizeInGB') is not None:
            self.size_in_gb = m.get('SizeInGB')
        return self


class CreateCacheResponseBody(TeaModel):
    def __init__(
        self,
        buy_url: str = None,
        cache_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.buy_url = buy_url
        self.cache_id = cache_id
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
        if self.buy_url is not None:
            result['BuyURL'] = self.buy_url
        if self.cache_id is not None:
            result['CacheId'] = self.cache_id
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
        if m.get('BuyURL') is not None:
            self.buy_url = m.get('BuyURL')
        if m.get('CacheId') is not None:
            self.cache_id = m.get('CacheId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCacheResponseBody = None,
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
            temp_model = CreateCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateElasticGatewayPrivateZoneRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateElasticGatewayPrivateZoneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateElasticGatewayPrivateZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateElasticGatewayPrivateZoneResponseBody = None,
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
            temp_model = CreateElasticGatewayPrivateZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExpressSyncRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_prefix: str = None,
        bucket_region: str = None,
        description: str = None,
        name: str = None,
        security_token: str = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_prefix = bucket_prefix
        self.bucket_region = bucket_region
        self.description = description
        self.name = name
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_prefix is not None:
            result['BucketPrefix'] = self.bucket_prefix
        if self.bucket_region is not None:
            result['BucketRegion'] = self.bucket_region
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketPrefix') is not None:
            self.bucket_prefix = m.get('BucketPrefix')
        if m.get('BucketRegion') is not None:
            self.bucket_region = m.get('BucketRegion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateExpressSyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        express_sync_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.express_sync_id = express_sync_id
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
        if self.express_sync_id is not None:
            result['ExpressSyncId'] = self.express_sync_id
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
        if m.get('ExpressSyncId') is not None:
            self.express_sync_id = m.get('ExpressSyncId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateExpressSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExpressSyncResponseBody = None,
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
            temp_model = CreateExpressSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        gateway_class: str = None,
        location: str = None,
        name: str = None,
        post_paid: bool = None,
        public_network_bandwidth: int = None,
        release_after_expiration: bool = None,
        resource_region_id: str = None,
        secondary_vswitch_id: str = None,
        security_token: str = None,
        storage_bundle_id: str = None,
        type: str = None,
        untrusted_env_id: str = None,
        untrusted_env_instance_type: str = None,
        v_switch_id: str = None,
    ):
        self.description = description
        self.gateway_class = gateway_class
        self.location = location
        self.name = name
        self.post_paid = post_paid
        self.public_network_bandwidth = public_network_bandwidth
        self.release_after_expiration = release_after_expiration
        self.resource_region_id = resource_region_id
        self.secondary_vswitch_id = secondary_vswitch_id
        self.security_token = security_token
        self.storage_bundle_id = storage_bundle_id
        self.type = type
        self.untrusted_env_id = untrusted_env_id
        self.untrusted_env_instance_type = untrusted_env_instance_type
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gateway_class is not None:
            result['GatewayClass'] = self.gateway_class
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.post_paid is not None:
            result['PostPaid'] = self.post_paid
        if self.public_network_bandwidth is not None:
            result['PublicNetworkBandwidth'] = self.public_network_bandwidth
        if self.release_after_expiration is not None:
            result['ReleaseAfterExpiration'] = self.release_after_expiration
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.secondary_vswitch_id is not None:
            result['SecondaryVSwitchId'] = self.secondary_vswitch_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        if self.type is not None:
            result['Type'] = self.type
        if self.untrusted_env_id is not None:
            result['UntrustedEnvId'] = self.untrusted_env_id
        if self.untrusted_env_instance_type is not None:
            result['UntrustedEnvInstanceType'] = self.untrusted_env_instance_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GatewayClass') is not None:
            self.gateway_class = m.get('GatewayClass')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PostPaid') is not None:
            self.post_paid = m.get('PostPaid')
        if m.get('PublicNetworkBandwidth') is not None:
            self.public_network_bandwidth = m.get('PublicNetworkBandwidth')
        if m.get('ReleaseAfterExpiration') is not None:
            self.release_after_expiration = m.get('ReleaseAfterExpiration')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('SecondaryVSwitchId') is not None:
            self.secondary_vswitch_id = m.get('SecondaryVSwitchId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UntrustedEnvId') is not None:
            self.untrusted_env_id = m.get('UntrustedEnvId')
        if m.get('UntrustedEnvInstanceType') is not None:
            self.untrusted_env_instance_type = m.get('UntrustedEnvInstanceType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateGatewayResponseBody(TeaModel):
    def __init__(
        self,
        buy_url: str = None,
        code: str = None,
        gateway_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.buy_url = buy_url
        self.code = code
        self.gateway_id = gateway_id
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
        if self.buy_url is not None:
            result['BuyURL'] = self.buy_url
        if self.code is not None:
            result['Code'] = self.code
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyURL') is not None:
            self.buy_url = m.get('BuyURL')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayResponseBody = None,
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
            temp_model = CreateGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayBlockVolumeRequest(TeaModel):
    def __init__(
        self,
        cache_mode: str = None,
        chap_enabled: bool = None,
        chap_in_password: str = None,
        chap_in_user: str = None,
        chunk_size: int = None,
        gateway_id: str = None,
        local_file_path: str = None,
        name: str = None,
        oss_bucket_name: str = None,
        oss_bucket_ssl: bool = None,
        oss_endpoint: str = None,
        recovery: bool = None,
        security_token: str = None,
        size: int = None,
        volume_protocol: str = None,
    ):
        self.cache_mode = cache_mode
        self.chap_enabled = chap_enabled
        self.chap_in_password = chap_in_password
        self.chap_in_user = chap_in_user
        self.chunk_size = chunk_size
        self.gateway_id = gateway_id
        self.local_file_path = local_file_path
        self.name = name
        self.oss_bucket_name = oss_bucket_name
        self.oss_bucket_ssl = oss_bucket_ssl
        self.oss_endpoint = oss_endpoint
        self.recovery = recovery
        self.security_token = security_token
        self.size = size
        self.volume_protocol = volume_protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_mode is not None:
            result['CacheMode'] = self.cache_mode
        if self.chap_enabled is not None:
            result['ChapEnabled'] = self.chap_enabled
        if self.chap_in_password is not None:
            result['ChapInPassword'] = self.chap_in_password
        if self.chap_in_user is not None:
            result['ChapInUser'] = self.chap_in_user
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.local_file_path is not None:
            result['LocalFilePath'] = self.local_file_path
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_bucket_ssl is not None:
            result['OssBucketSsl'] = self.oss_bucket_ssl
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.recovery is not None:
            result['Recovery'] = self.recovery
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.size is not None:
            result['Size'] = self.size
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheMode') is not None:
            self.cache_mode = m.get('CacheMode')
        if m.get('ChapEnabled') is not None:
            self.chap_enabled = m.get('ChapEnabled')
        if m.get('ChapInPassword') is not None:
            self.chap_in_password = m.get('ChapInPassword')
        if m.get('ChapInUser') is not None:
            self.chap_in_user = m.get('ChapInUser')
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('LocalFilePath') is not None:
            self.local_file_path = m.get('LocalFilePath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssBucketSsl') is not None:
            self.oss_bucket_ssl = m.get('OssBucketSsl')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('Recovery') is not None:
            self.recovery = m.get('Recovery')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        return self


class CreateGatewayBlockVolumeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateGatewayBlockVolumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayBlockVolumeResponseBody = None,
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
            temp_model = CreateGatewayBlockVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayCacheDiskRequest(TeaModel):
    def __init__(
        self,
        cache_disk_category: str = None,
        cache_disk_size_in_gb: int = None,
        gateway_id: str = None,
        performance_level: str = None,
        security_token: str = None,
    ):
        self.cache_disk_category = cache_disk_category
        self.cache_disk_size_in_gb = cache_disk_size_in_gb
        self.gateway_id = gateway_id
        self.performance_level = performance_level
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_disk_category is not None:
            result['CacheDiskCategory'] = self.cache_disk_category
        if self.cache_disk_size_in_gb is not None:
            result['CacheDiskSizeInGB'] = self.cache_disk_size_in_gb
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheDiskCategory') is not None:
            self.cache_disk_category = m.get('CacheDiskCategory')
        if m.get('CacheDiskSizeInGB') is not None:
            self.cache_disk_size_in_gb = m.get('CacheDiskSizeInGB')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateGatewayCacheDiskResponseBody(TeaModel):
    def __init__(
        self,
        buy_url: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.buy_url = buy_url
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_url is not None:
            result['BuyURL'] = self.buy_url
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyURL') is not None:
            self.buy_url = m.get('BuyURL')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateGatewayCacheDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayCacheDiskResponseBody = None,
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
            temp_model = CreateGatewayCacheDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayFileShareRequest(TeaModel):
    def __init__(
        self,
        access_based_enumeration: bool = None,
        backend_limit: int = None,
        browsable: bool = None,
        bypass_cache_read: bool = None,
        cache_mode: str = None,
        client_side_cmk: str = None,
        client_side_encryption: bool = None,
        direct_io: bool = None,
        download_limit: int = None,
        fast_reclaim: bool = None,
        frontend_limit: int = None,
        gateway_id: str = None,
        ignore_delete: bool = None,
        in_place: bool = None,
        kms_rotate_period: int = None,
        lag_period: int = None,
        local_file_path: str = None,
        name: str = None,
        nfs_v4optimization: bool = None,
        oss_bucket_name: str = None,
        oss_bucket_ssl: bool = None,
        oss_endpoint: str = None,
        partial_sync_paths: str = None,
        path_prefix: str = None,
        polling_interval: int = None,
        read_only_client_list: str = None,
        read_only_user_list: str = None,
        read_write_client_list: str = None,
        read_write_user_list: str = None,
        remote_sync: bool = None,
        remote_sync_download: bool = None,
        security_token: str = None,
        server_side_algorithm: str = None,
        server_side_cmk: str = None,
        server_side_encryption: bool = None,
        share_protocol: str = None,
        squash: str = None,
        support_archive: bool = None,
        transfer_acceleration: bool = None,
        windows_acl: bool = None,
    ):
        self.access_based_enumeration = access_based_enumeration
        self.backend_limit = backend_limit
        self.browsable = browsable
        self.bypass_cache_read = bypass_cache_read
        self.cache_mode = cache_mode
        self.client_side_cmk = client_side_cmk
        self.client_side_encryption = client_side_encryption
        self.direct_io = direct_io
        self.download_limit = download_limit
        self.fast_reclaim = fast_reclaim
        self.frontend_limit = frontend_limit
        self.gateway_id = gateway_id
        self.ignore_delete = ignore_delete
        self.in_place = in_place
        self.kms_rotate_period = kms_rotate_period
        self.lag_period = lag_period
        self.local_file_path = local_file_path
        self.name = name
        self.nfs_v4optimization = nfs_v4optimization
        self.oss_bucket_name = oss_bucket_name
        self.oss_bucket_ssl = oss_bucket_ssl
        self.oss_endpoint = oss_endpoint
        self.partial_sync_paths = partial_sync_paths
        self.path_prefix = path_prefix
        self.polling_interval = polling_interval
        self.read_only_client_list = read_only_client_list
        self.read_only_user_list = read_only_user_list
        self.read_write_client_list = read_write_client_list
        self.read_write_user_list = read_write_user_list
        self.remote_sync = remote_sync
        self.remote_sync_download = remote_sync_download
        self.security_token = security_token
        self.server_side_algorithm = server_side_algorithm
        self.server_side_cmk = server_side_cmk
        self.server_side_encryption = server_side_encryption
        self.share_protocol = share_protocol
        self.squash = squash
        self.support_archive = support_archive
        self.transfer_acceleration = transfer_acceleration
        self.windows_acl = windows_acl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_based_enumeration is not None:
            result['AccessBasedEnumeration'] = self.access_based_enumeration
        if self.backend_limit is not None:
            result['BackendLimit'] = self.backend_limit
        if self.browsable is not None:
            result['Browsable'] = self.browsable
        if self.bypass_cache_read is not None:
            result['BypassCacheRead'] = self.bypass_cache_read
        if self.cache_mode is not None:
            result['CacheMode'] = self.cache_mode
        if self.client_side_cmk is not None:
            result['ClientSideCmk'] = self.client_side_cmk
        if self.client_side_encryption is not None:
            result['ClientSideEncryption'] = self.client_side_encryption
        if self.direct_io is not None:
            result['DirectIO'] = self.direct_io
        if self.download_limit is not None:
            result['DownloadLimit'] = self.download_limit
        if self.fast_reclaim is not None:
            result['FastReclaim'] = self.fast_reclaim
        if self.frontend_limit is not None:
            result['FrontendLimit'] = self.frontend_limit
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.ignore_delete is not None:
            result['IgnoreDelete'] = self.ignore_delete
        if self.in_place is not None:
            result['InPlace'] = self.in_place
        if self.kms_rotate_period is not None:
            result['KmsRotatePeriod'] = self.kms_rotate_period
        if self.lag_period is not None:
            result['LagPeriod'] = self.lag_period
        if self.local_file_path is not None:
            result['LocalFilePath'] = self.local_file_path
        if self.name is not None:
            result['Name'] = self.name
        if self.nfs_v4optimization is not None:
            result['NfsV4Optimization'] = self.nfs_v4optimization
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_bucket_ssl is not None:
            result['OssBucketSsl'] = self.oss_bucket_ssl
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.partial_sync_paths is not None:
            result['PartialSyncPaths'] = self.partial_sync_paths
        if self.path_prefix is not None:
            result['PathPrefix'] = self.path_prefix
        if self.polling_interval is not None:
            result['PollingInterval'] = self.polling_interval
        if self.read_only_client_list is not None:
            result['ReadOnlyClientList'] = self.read_only_client_list
        if self.read_only_user_list is not None:
            result['ReadOnlyUserList'] = self.read_only_user_list
        if self.read_write_client_list is not None:
            result['ReadWriteClientList'] = self.read_write_client_list
        if self.read_write_user_list is not None:
            result['ReadWriteUserList'] = self.read_write_user_list
        if self.remote_sync is not None:
            result['RemoteSync'] = self.remote_sync
        if self.remote_sync_download is not None:
            result['RemoteSyncDownload'] = self.remote_sync_download
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_side_algorithm is not None:
            result['ServerSideAlgorithm'] = self.server_side_algorithm
        if self.server_side_cmk is not None:
            result['ServerSideCmk'] = self.server_side_cmk
        if self.server_side_encryption is not None:
            result['ServerSideEncryption'] = self.server_side_encryption
        if self.share_protocol is not None:
            result['ShareProtocol'] = self.share_protocol
        if self.squash is not None:
            result['Squash'] = self.squash
        if self.support_archive is not None:
            result['SupportArchive'] = self.support_archive
        if self.transfer_acceleration is not None:
            result['TransferAcceleration'] = self.transfer_acceleration
        if self.windows_acl is not None:
            result['WindowsAcl'] = self.windows_acl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessBasedEnumeration') is not None:
            self.access_based_enumeration = m.get('AccessBasedEnumeration')
        if m.get('BackendLimit') is not None:
            self.backend_limit = m.get('BackendLimit')
        if m.get('Browsable') is not None:
            self.browsable = m.get('Browsable')
        if m.get('BypassCacheRead') is not None:
            self.bypass_cache_read = m.get('BypassCacheRead')
        if m.get('CacheMode') is not None:
            self.cache_mode = m.get('CacheMode')
        if m.get('ClientSideCmk') is not None:
            self.client_side_cmk = m.get('ClientSideCmk')
        if m.get('ClientSideEncryption') is not None:
            self.client_side_encryption = m.get('ClientSideEncryption')
        if m.get('DirectIO') is not None:
            self.direct_io = m.get('DirectIO')
        if m.get('DownloadLimit') is not None:
            self.download_limit = m.get('DownloadLimit')
        if m.get('FastReclaim') is not None:
            self.fast_reclaim = m.get('FastReclaim')
        if m.get('FrontendLimit') is not None:
            self.frontend_limit = m.get('FrontendLimit')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IgnoreDelete') is not None:
            self.ignore_delete = m.get('IgnoreDelete')
        if m.get('InPlace') is not None:
            self.in_place = m.get('InPlace')
        if m.get('KmsRotatePeriod') is not None:
            self.kms_rotate_period = m.get('KmsRotatePeriod')
        if m.get('LagPeriod') is not None:
            self.lag_period = m.get('LagPeriod')
        if m.get('LocalFilePath') is not None:
            self.local_file_path = m.get('LocalFilePath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NfsV4Optimization') is not None:
            self.nfs_v4optimization = m.get('NfsV4Optimization')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssBucketSsl') is not None:
            self.oss_bucket_ssl = m.get('OssBucketSsl')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('PartialSyncPaths') is not None:
            self.partial_sync_paths = m.get('PartialSyncPaths')
        if m.get('PathPrefix') is not None:
            self.path_prefix = m.get('PathPrefix')
        if m.get('PollingInterval') is not None:
            self.polling_interval = m.get('PollingInterval')
        if m.get('ReadOnlyClientList') is not None:
            self.read_only_client_list = m.get('ReadOnlyClientList')
        if m.get('ReadOnlyUserList') is not None:
            self.read_only_user_list = m.get('ReadOnlyUserList')
        if m.get('ReadWriteClientList') is not None:
            self.read_write_client_list = m.get('ReadWriteClientList')
        if m.get('ReadWriteUserList') is not None:
            self.read_write_user_list = m.get('ReadWriteUserList')
        if m.get('RemoteSync') is not None:
            self.remote_sync = m.get('RemoteSync')
        if m.get('RemoteSyncDownload') is not None:
            self.remote_sync_download = m.get('RemoteSyncDownload')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerSideAlgorithm') is not None:
            self.server_side_algorithm = m.get('ServerSideAlgorithm')
        if m.get('ServerSideCmk') is not None:
            self.server_side_cmk = m.get('ServerSideCmk')
        if m.get('ServerSideEncryption') is not None:
            self.server_side_encryption = m.get('ServerSideEncryption')
        if m.get('ShareProtocol') is not None:
            self.share_protocol = m.get('ShareProtocol')
        if m.get('Squash') is not None:
            self.squash = m.get('Squash')
        if m.get('SupportArchive') is not None:
            self.support_archive = m.get('SupportArchive')
        if m.get('TransferAcceleration') is not None:
            self.transfer_acceleration = m.get('TransferAcceleration')
        if m.get('WindowsAcl') is not None:
            self.windows_acl = m.get('WindowsAcl')
        return self


class CreateGatewayFileShareResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateGatewayFileShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayFileShareResponseBody = None,
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
            temp_model = CreateGatewayFileShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayLoggingRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
        sls_logstore: str = None,
        sls_project: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.sls_logstore = sls_logstore
        self.sls_project = sls_project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        return self


class CreateGatewayLoggingResponseBody(TeaModel):
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


class CreateGatewayLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayLoggingResponseBody = None,
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
            temp_model = CreateGatewayLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewaySMBUserRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        password: str = None,
        security_token: str = None,
        username: str = None,
    ):
        self.gateway_id = gateway_id
        self.password = password
        self.security_token = security_token
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.password is not None:
            result['Password'] = self.password
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateGatewaySMBUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateGatewaySMBUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewaySMBUserResponseBody = None,
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
            temp_model = CreateGatewaySMBUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStorageBundleRequest(TeaModel):
    def __init__(
        self,
        backend_bucket_region_id: str = None,
        description: str = None,
        name: str = None,
        security_token: str = None,
    ):
        self.backend_bucket_region_id = backend_bucket_region_id
        self.description = description
        self.name = name
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_bucket_region_id is not None:
            result['BackendBucketRegionId'] = self.backend_bucket_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendBucketRegionId') is not None:
            self.backend_bucket_region_id = m.get('BackendBucketRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateStorageBundleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        storage_bundle_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.storage_bundle_id = storage_bundle_id
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
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
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
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateStorageBundleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStorageBundleResponseBody = None,
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
            temp_model = CreateStorageBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCSGClientsRequest(TeaModel):
    def __init__(
        self,
        client_ids: List[str] = None,
        client_region_id: str = None,
        security_token: str = None,
    ):
        self.client_ids = client_ids
        self.client_region_id = client_region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.client_region_id is not None:
            result['ClientRegionId'] = self.client_region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('ClientRegionId') is not None:
            self.client_region_id = m.get('ClientRegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteCSGClientsShrinkRequest(TeaModel):
    def __init__(
        self,
        client_ids_shrink: str = None,
        client_region_id: str = None,
        security_token: str = None,
    ):
        self.client_ids_shrink = client_ids_shrink
        self.client_region_id = client_region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink
        if self.client_region_id is not None:
            result['ClientRegionId'] = self.client_region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')
        if m.get('ClientRegionId') is not None:
            self.client_region_id = m.get('ClientRegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteCSGClientsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteCSGClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCSGClientsResponseBody = None,
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
            temp_model = DeleteCSGClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteElasticGatewayPrivateZoneRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteElasticGatewayPrivateZoneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteElasticGatewayPrivateZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteElasticGatewayPrivateZoneResponseBody = None,
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
            temp_model = DeleteElasticGatewayPrivateZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExpressSyncRequest(TeaModel):
    def __init__(
        self,
        express_sync_id: str = None,
        security_token: str = None,
    ):
        self.express_sync_id = express_sync_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.express_sync_id is not None:
            result['ExpressSyncId'] = self.express_sync_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressSyncId') is not None:
            self.express_sync_id = m.get('ExpressSyncId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteExpressSyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteExpressSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExpressSyncResponseBody = None,
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
            temp_model = DeleteExpressSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        reason_detail: str = None,
        reason_type: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.reason_detail = reason_detail
        self.reason_type = reason_type
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.reason_detail is not None:
            result['ReasonDetail'] = self.reason_detail
        if self.reason_type is not None:
            result['ReasonType'] = self.reason_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('ReasonDetail') is not None:
            self.reason_detail = m.get('ReasonDetail')
        if m.get('ReasonType') is not None:
            self.reason_type = m.get('ReasonType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayResponseBody = None,
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
            temp_model = DeleteGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayBlockVolumesRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        index_id: str = None,
        is_source_deletion: bool = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.is_source_deletion = is_source_deletion
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.is_source_deletion is not None:
            result['IsSourceDeletion'] = self.is_source_deletion
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('IsSourceDeletion') is not None:
            self.is_source_deletion = m.get('IsSourceDeletion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteGatewayBlockVolumesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteGatewayBlockVolumesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayBlockVolumesResponseBody = None,
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
            temp_model = DeleteGatewayBlockVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayCacheDiskRequest(TeaModel):
    def __init__(
        self,
        cache_id: str = None,
        gateway_id: str = None,
        local_file_path: str = None,
        security_token: str = None,
    ):
        self.cache_id = cache_id
        self.gateway_id = gateway_id
        self.local_file_path = local_file_path
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_id is not None:
            result['CacheId'] = self.cache_id
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.local_file_path is not None:
            result['LocalFilePath'] = self.local_file_path
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheId') is not None:
            self.cache_id = m.get('CacheId')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('LocalFilePath') is not None:
            self.local_file_path = m.get('LocalFilePath')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteGatewayCacheDiskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteGatewayCacheDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayCacheDiskResponseBody = None,
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
            temp_model = DeleteGatewayCacheDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayFileSharesRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        gateway_id: str = None,
        index_id: str = None,
        security_token: str = None,
    ):
        self.force = force
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteGatewayFileSharesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteGatewayFileSharesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayFileSharesResponseBody = None,
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
            temp_model = DeleteGatewayFileSharesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayLoggingRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteGatewayLoggingResponseBody(TeaModel):
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


class DeleteGatewayLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayLoggingResponseBody = None,
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
            temp_model = DeleteGatewayLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewaySMBUserRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
        username: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DeleteGatewaySMBUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteGatewaySMBUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewaySMBUserResponseBody = None,
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
            temp_model = DeleteGatewaySMBUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStorageBundleRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        storage_bundle_id: str = None,
    ):
        self.security_token = security_token
        self.storage_bundle_id = storage_bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        return self


class DeleteStorageBundleResponseBody(TeaModel):
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


class DeleteStorageBundleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStorageBundleResponseBody = None,
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
            temp_model = DeleteStorageBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployCSGClientsRequest(TeaModel):
    def __init__(
        self,
        client_region_id: str = None,
        ecs_instance_ids: List[str] = None,
        security_token: str = None,
        vpc_id: str = None,
    ):
        self.client_region_id = client_region_id
        self.ecs_instance_ids = ecs_instance_ids
        self.security_token = security_token
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_region_id is not None:
            result['ClientRegionId'] = self.client_region_id
        if self.ecs_instance_ids is not None:
            result['EcsInstanceIds'] = self.ecs_instance_ids
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientRegionId') is not None:
            self.client_region_id = m.get('ClientRegionId')
        if m.get('EcsInstanceIds') is not None:
            self.ecs_instance_ids = m.get('EcsInstanceIds')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DeployCSGClientsShrinkRequest(TeaModel):
    def __init__(
        self,
        client_region_id: str = None,
        ecs_instance_ids_shrink: str = None,
        security_token: str = None,
        vpc_id: str = None,
    ):
        self.client_region_id = client_region_id
        self.ecs_instance_ids_shrink = ecs_instance_ids_shrink
        self.security_token = security_token
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_region_id is not None:
            result['ClientRegionId'] = self.client_region_id
        if self.ecs_instance_ids_shrink is not None:
            result['EcsInstanceIds'] = self.ecs_instance_ids_shrink
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientRegionId') is not None:
            self.client_region_id = m.get('ClientRegionId')
        if m.get('EcsInstanceIds') is not None:
            self.ecs_instance_ids_shrink = m.get('EcsInstanceIds')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DeployCSGClientsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeployCSGClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployCSGClientsResponseBody = None,
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
            temp_model = DeployCSGClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployCacheDiskRequest(TeaModel):
    def __init__(
        self,
        cache_config: str = None,
        disk_category: str = None,
        gateway_id: str = None,
        security_token: str = None,
        size_in_gb: int = None,
    ):
        self.cache_config = cache_config
        self.disk_category = disk_category
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.size_in_gb = size_in_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_config is not None:
            result['CacheConfig'] = self.cache_config
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.size_in_gb is not None:
            result['SizeInGB'] = self.size_in_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheConfig') is not None:
            self.cache_config = m.get('CacheConfig')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SizeInGB') is not None:
            self.size_in_gb = m.get('SizeInGB')
        return self


class DeployCacheDiskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeployCacheDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployCacheDiskResponseBody = None,
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
            temp_model = DeployCacheDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_class: str = None,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_class = gateway_class
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_class is not None:
            result['GatewayClass'] = self.gateway_class
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayClass') is not None:
            self.gateway_class = m.get('GatewayClass')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeployGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeployGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployGatewayResponseBody = None,
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
            temp_model = DeployGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountConfigRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAccountConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_support_client_side_encryption: bool = None,
        is_support_elastic_gateway_beta: bool = None,
        is_support_gateway_logging: bool = None,
        is_support_server_side_encryption: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.is_support_client_side_encryption = is_support_client_side_encryption
        self.is_support_elastic_gateway_beta = is_support_elastic_gateway_beta
        self.is_support_gateway_logging = is_support_gateway_logging
        self.is_support_server_side_encryption = is_support_server_side_encryption
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
        if self.is_support_client_side_encryption is not None:
            result['IsSupportClientSideEncryption'] = self.is_support_client_side_encryption
        if self.is_support_elastic_gateway_beta is not None:
            result['IsSupportElasticGatewayBeta'] = self.is_support_elastic_gateway_beta
        if self.is_support_gateway_logging is not None:
            result['IsSupportGatewayLogging'] = self.is_support_gateway_logging
        if self.is_support_server_side_encryption is not None:
            result['IsSupportServerSideEncryption'] = self.is_support_server_side_encryption
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
        if m.get('IsSupportClientSideEncryption') is not None:
            self.is_support_client_side_encryption = m.get('IsSupportClientSideEncryption')
        if m.get('IsSupportElasticGatewayBeta') is not None:
            self.is_support_elastic_gateway_beta = m.get('IsSupportElasticGatewayBeta')
        if m.get('IsSupportGatewayLogging') is not None:
            self.is_support_gateway_logging = m.get('IsSupportGatewayLogging')
        if m.get('IsSupportServerSideEncryption') is not None:
            self.is_support_server_side_encryption = m.get('IsSupportServerSideEncryption')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAccountConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountConfigResponseBody = None,
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
            temp_model = DescribeAccountConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlockVolumeSnapshotsRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        index_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeBlockVolumeSnapshotsResponseBodySnapshotsSnapshot(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        size: int = None,
        snapshot_name: str = None,
    ):
        self.create_time = create_time
        self.size = size
        self.snapshot_name = snapshot_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class DescribeBlockVolumeSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        snapshot: List[DescribeBlockVolumeSnapshotsResponseBodySnapshotsSnapshot] = None,
    ):
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            for k in self.snapshot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Snapshot'] = []
        if self.snapshot is not None:
            for k in self.snapshot:
                result['Snapshot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot = []
        if m.get('Snapshot') is not None:
            for k in m.get('Snapshot'):
                temp_model = DescribeBlockVolumeSnapshotsResponseBodySnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k))
        return self


class DescribeBlockVolumeSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshots: DescribeBlockVolumeSnapshotsResponseBodySnapshots = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.snapshots = snapshots
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Snapshots') is not None:
            temp_model = DescribeBlockVolumeSnapshotsResponseBodySnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBlockVolumeSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBlockVolumeSnapshotsResponseBody = None,
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
            temp_model = DescribeBlockVolumeSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCSGClientTasksRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.client_id = client_id
        self.client_region_id = client_region_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_region_id is not None:
            result['ClientRegionId'] = self.client_region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientRegionId') is not None:
            self.client_region_id = m.get('ClientRegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCSGClientTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        created_time: int = None,
        message_key: str = None,
        message_params: str = None,
        name: str = None,
        progress: int = None,
        state_code: str = None,
        task_id: str = None,
        updated_time: int = None,
    ):
        self.created_time = created_time
        self.message_key = message_key
        self.message_params = message_params
        self.name = name
        self.progress = progress
        self.state_code = state_code
        self.task_id = task_id
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.message_key is not None:
            result['MessageKey'] = self.message_key
        if self.message_params is not None:
            result['MessageParams'] = self.message_params
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.state_code is not None:
            result['StateCode'] = self.state_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('MessageKey') is not None:
            self.message_key = m.get('MessageKey')
        if m.get('MessageParams') is not None:
            self.message_params = m.get('MessageParams')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StateCode') is not None:
            self.state_code = m.get('StateCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribeCSGClientTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        tasks: List[DescribeCSGClientTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DescribeCSGClientTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCSGClientTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCSGClientTasksResponseBody = None,
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
            temp_model = DescribeCSGClientTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCSGClientsRequest(TeaModel):
    def __init__(
        self,
        client_region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.client_region_id = client_region_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_region_id is not None:
            result['ClientRegionId'] = self.client_region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientRegionId') is not None:
            self.client_region_id = m.get('ClientRegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCSGClientsResponseBodyClients(TeaModel):
    def __init__(
        self,
        client_deletion_command: str = None,
        client_id: str = None,
        client_installation_command: str = None,
        client_version: str = None,
        ecs_instance_id: str = None,
        host_instance_id: str = None,
        last_heartbeat_time: int = None,
        status: str = None,
        vpc_id: str = None,
        work_directory: str = None,
    ):
        self.client_deletion_command = client_deletion_command
        self.client_id = client_id
        self.client_installation_command = client_installation_command
        self.client_version = client_version
        self.ecs_instance_id = ecs_instance_id
        self.host_instance_id = host_instance_id
        self.last_heartbeat_time = last_heartbeat_time
        self.status = status
        self.vpc_id = vpc_id
        self.work_directory = work_directory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_deletion_command is not None:
            result['ClientDeletionCommand'] = self.client_deletion_command
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_installation_command is not None:
            result['ClientInstallationCommand'] = self.client_installation_command
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.host_instance_id is not None:
            result['HostInstanceId'] = self.host_instance_id
        if self.last_heartbeat_time is not None:
            result['LastHeartbeatTime'] = self.last_heartbeat_time
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.work_directory is not None:
            result['WorkDirectory'] = self.work_directory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientDeletionCommand') is not None:
            self.client_deletion_command = m.get('ClientDeletionCommand')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientInstallationCommand') is not None:
            self.client_installation_command = m.get('ClientInstallationCommand')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('HostInstanceId') is not None:
            self.host_instance_id = m.get('HostInstanceId')
        if m.get('LastHeartbeatTime') is not None:
            self.last_heartbeat_time = m.get('LastHeartbeatTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WorkDirectory') is not None:
            self.work_directory = m.get('WorkDirectory')
        return self


class DescribeCSGClientsResponseBody(TeaModel):
    def __init__(
        self,
        clients: List[DescribeCSGClientsResponseBodyClients] = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.clients = clients
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.clients:
            for k in self.clients:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clients'] = []
        if self.clients is not None:
            for k in self.clients:
                result['Clients'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
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
        self.clients = []
        if m.get('Clients') is not None:
            for k in m.get('Clients'):
                temp_model = DescribeCSGClientsResponseBodyClients()
                self.clients.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
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


class DescribeCSGClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCSGClientsResponseBody = None,
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
            temp_model = DescribeCSGClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDashboardRequest(TeaModel):
    def __init__(
        self,
        backend_bucket_region_id: str = None,
        resource_group_id: str = None,
        security_token: str = None,
    ):
        self.backend_bucket_region_id = backend_bucket_region_id
        self.resource_group_id = resource_group_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_bucket_region_id is not None:
            result['BackendBucketRegionId'] = self.backend_bucket_region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendBucketRegionId') is not None:
            self.backend_bucket_region_id = m.get('BackendBucketRegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDashboardResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        overview: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.overview = overview
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
        if self.overview is not None:
            result['Overview'] = self.overview
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
        if m.get('Overview') is not None:
            self.overview = m.get('Overview')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDashboardResponseBody = None,
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
            temp_model = DescribeDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpireCachesRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeExpireCachesResponseBody(TeaModel):
    def __init__(
        self,
        cache_file_paths: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.cache_file_paths = cache_file_paths
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
        if self.cache_file_paths is not None:
            result['CacheFilePaths'] = self.cache_file_paths
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
        if m.get('CacheFilePaths') is not None:
            self.cache_file_paths = m.get('CacheFilePaths')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExpireCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExpireCachesResponseBody = None,
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
            temp_model = DescribeExpireCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressSyncSharesRequest(TeaModel):
    def __init__(
        self,
        express_sync_ids: str = None,
        is_external: bool = None,
        security_token: str = None,
    ):
        self.express_sync_ids = express_sync_ids
        self.is_external = is_external
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.express_sync_ids is not None:
            result['ExpressSyncIds'] = self.express_sync_ids
        if self.is_external is not None:
            result['IsExternal'] = self.is_external
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressSyncIds') is not None:
            self.express_sync_ids = m.get('ExpressSyncIds')
        if m.get('IsExternal') is not None:
            self.is_external = m.get('IsExternal')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeExpressSyncSharesResponseBodySharesShare(TeaModel):
    def __init__(
        self,
        express_sync_id: str = None,
        express_sync_state: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        gateway_region: str = None,
        mns_queue: str = None,
        share_name: str = None,
        storage_bundle_id: str = None,
        sync_progress: int = None,
    ):
        self.express_sync_id = express_sync_id
        self.express_sync_state = express_sync_state
        self.gateway_id = gateway_id
        self.gateway_name = gateway_name
        self.gateway_region = gateway_region
        self.mns_queue = mns_queue
        self.share_name = share_name
        self.storage_bundle_id = storage_bundle_id
        self.sync_progress = sync_progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.express_sync_id is not None:
            result['ExpressSyncId'] = self.express_sync_id
        if self.express_sync_state is not None:
            result['ExpressSyncState'] = self.express_sync_state
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.gateway_region is not None:
            result['GatewayRegion'] = self.gateway_region
        if self.mns_queue is not None:
            result['MnsQueue'] = self.mns_queue
        if self.share_name is not None:
            result['ShareName'] = self.share_name
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        if self.sync_progress is not None:
            result['SyncProgress'] = self.sync_progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressSyncId') is not None:
            self.express_sync_id = m.get('ExpressSyncId')
        if m.get('ExpressSyncState') is not None:
            self.express_sync_state = m.get('ExpressSyncState')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('GatewayRegion') is not None:
            self.gateway_region = m.get('GatewayRegion')
        if m.get('MnsQueue') is not None:
            self.mns_queue = m.get('MnsQueue')
        if m.get('ShareName') is not None:
            self.share_name = m.get('ShareName')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        if m.get('SyncProgress') is not None:
            self.sync_progress = m.get('SyncProgress')
        return self


class DescribeExpressSyncSharesResponseBodyShares(TeaModel):
    def __init__(
        self,
        share: List[DescribeExpressSyncSharesResponseBodySharesShare] = None,
    ):
        self.share = share

    def validate(self):
        if self.share:
            for k in self.share:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Share'] = []
        if self.share is not None:
            for k in self.share:
                result['Share'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.share = []
        if m.get('Share') is not None:
            for k in m.get('Share'):
                temp_model = DescribeExpressSyncSharesResponseBodySharesShare()
                self.share.append(temp_model.from_map(k))
        return self


class DescribeExpressSyncSharesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        shares: DescribeExpressSyncSharesResponseBodyShares = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.shares = shares
        self.success = success

    def validate(self):
        if self.shares:
            self.shares.validate()

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
        if self.shares is not None:
            result['Shares'] = self.shares.to_map()
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
        if m.get('Shares') is not None:
            temp_model = DescribeExpressSyncSharesResponseBodyShares()
            self.shares = temp_model.from_map(m['Shares'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExpressSyncSharesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExpressSyncSharesResponseBody = None,
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
            temp_model = DescribeExpressSyncSharesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressSyncsRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_prefix: str = None,
        security_token: str = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_prefix = bucket_prefix
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_prefix is not None:
            result['BucketPrefix'] = self.bucket_prefix
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketPrefix') is not None:
            self.bucket_prefix = m.get('BucketPrefix')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeExpressSyncsResponseBodyExpressSyncsExpressSync(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_prefix: str = None,
        bucket_region: str = None,
        description: str = None,
        express_sync_id: str = None,
        mns_topic: str = None,
        name: str = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_prefix = bucket_prefix
        self.bucket_region = bucket_region
        self.description = description
        self.express_sync_id = express_sync_id
        self.mns_topic = mns_topic
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_prefix is not None:
            result['BucketPrefix'] = self.bucket_prefix
        if self.bucket_region is not None:
            result['BucketRegion'] = self.bucket_region
        if self.description is not None:
            result['Description'] = self.description
        if self.express_sync_id is not None:
            result['ExpressSyncId'] = self.express_sync_id
        if self.mns_topic is not None:
            result['MnsTopic'] = self.mns_topic
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketPrefix') is not None:
            self.bucket_prefix = m.get('BucketPrefix')
        if m.get('BucketRegion') is not None:
            self.bucket_region = m.get('BucketRegion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpressSyncId') is not None:
            self.express_sync_id = m.get('ExpressSyncId')
        if m.get('MnsTopic') is not None:
            self.mns_topic = m.get('MnsTopic')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeExpressSyncsResponseBodyExpressSyncs(TeaModel):
    def __init__(
        self,
        express_sync: List[DescribeExpressSyncsResponseBodyExpressSyncsExpressSync] = None,
    ):
        self.express_sync = express_sync

    def validate(self):
        if self.express_sync:
            for k in self.express_sync:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExpressSync'] = []
        if self.express_sync is not None:
            for k in self.express_sync:
                result['ExpressSync'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.express_sync = []
        if m.get('ExpressSync') is not None:
            for k in m.get('ExpressSync'):
                temp_model = DescribeExpressSyncsResponseBodyExpressSyncsExpressSync()
                self.express_sync.append(temp_model.from_map(k))
        return self


class DescribeExpressSyncsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        express_syncs: DescribeExpressSyncsResponseBodyExpressSyncs = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.express_syncs = express_syncs
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.express_syncs:
            self.express_syncs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.express_syncs is not None:
            result['ExpressSyncs'] = self.express_syncs.to_map()
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
        if m.get('ExpressSyncs') is not None:
            temp_model = DescribeExpressSyncsResponseBodyExpressSyncs()
            self.express_syncs = temp_model.from_map(m['ExpressSyncs'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExpressSyncsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExpressSyncsResponseBody = None,
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
            temp_model = DescribeExpressSyncsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayResponseBodyElasticNodes(TeaModel):
    def __init__(
        self,
        elastic_node: List[str] = None,
    ):
        self.elastic_node = elastic_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_node is not None:
            result['ElasticNode'] = self.elastic_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNode') is not None:
            self.elastic_node = m.get('ElasticNode')
        return self


class DescribeGatewayResponseBody(TeaModel):
    def __init__(
        self,
        activated_time: int = None,
        buy_url: str = None,
        capacity: int = None,
        category: str = None,
        code: str = None,
        common_buy_instance_id: str = None,
        created_time: int = None,
        data_load_interval: int = None,
        data_load_type: str = None,
        description: str = None,
        ecs_instance_id: str = None,
        elastic_gateway: bool = None,
        elastic_nodes: DescribeGatewayResponseBodyElasticNodes = None,
        expire_status: int = None,
        expired_time: int = None,
        gateway_class: str = None,
        gateway_id: str = None,
        gateway_region_id: str = None,
        gateway_type: str = None,
        gateway_version: str = None,
        high_availability: bool = None,
        inner_ip: str = None,
        inner_ipv_6ip: str = None,
        ip: str = None,
        is_post_paid: bool = None,
        is_release_after_expiration: bool = None,
        last_error_key: str = None,
        location: str = None,
        max_throughput: int = None,
        message: str = None,
        name: str = None,
        public_network_bandwidth: int = None,
        renew_url: str = None,
        request_id: str = None,
        status: str = None,
        storage_bundle_id: str = None,
        success: bool = None,
        task_id: str = None,
        type: str = None,
        untrusted_env_instance_type: str = None,
        untrusted_env_oss_endpoint: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.activated_time = activated_time
        self.buy_url = buy_url
        self.capacity = capacity
        self.category = category
        self.code = code
        self.common_buy_instance_id = common_buy_instance_id
        self.created_time = created_time
        self.data_load_interval = data_load_interval
        self.data_load_type = data_load_type
        self.description = description
        self.ecs_instance_id = ecs_instance_id
        self.elastic_gateway = elastic_gateway
        self.elastic_nodes = elastic_nodes
        self.expire_status = expire_status
        self.expired_time = expired_time
        self.gateway_class = gateway_class
        self.gateway_id = gateway_id
        self.gateway_region_id = gateway_region_id
        self.gateway_type = gateway_type
        self.gateway_version = gateway_version
        self.high_availability = high_availability
        self.inner_ip = inner_ip
        self.inner_ipv_6ip = inner_ipv_6ip
        self.ip = ip
        self.is_post_paid = is_post_paid
        self.is_release_after_expiration = is_release_after_expiration
        self.last_error_key = last_error_key
        self.location = location
        self.max_throughput = max_throughput
        self.message = message
        self.name = name
        self.public_network_bandwidth = public_network_bandwidth
        self.renew_url = renew_url
        self.request_id = request_id
        self.status = status
        self.storage_bundle_id = storage_bundle_id
        self.success = success
        self.task_id = task_id
        self.type = type
        self.untrusted_env_instance_type = untrusted_env_instance_type
        self.untrusted_env_oss_endpoint = untrusted_env_oss_endpoint
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        if self.elastic_nodes:
            self.elastic_nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activated_time is not None:
            result['ActivatedTime'] = self.activated_time
        if self.buy_url is not None:
            result['BuyURL'] = self.buy_url
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.category is not None:
            result['Category'] = self.category
        if self.code is not None:
            result['Code'] = self.code
        if self.common_buy_instance_id is not None:
            result['CommonBuyInstanceId'] = self.common_buy_instance_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_load_interval is not None:
            result['DataLoadInterval'] = self.data_load_interval
        if self.data_load_type is not None:
            result['DataLoadType'] = self.data_load_type
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.elastic_gateway is not None:
            result['ElasticGateway'] = self.elastic_gateway
        if self.elastic_nodes is not None:
            result['ElasticNodes'] = self.elastic_nodes.to_map()
        if self.expire_status is not None:
            result['ExpireStatus'] = self.expire_status
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gateway_class is not None:
            result['GatewayClass'] = self.gateway_class
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_region_id is not None:
            result['GatewayRegionId'] = self.gateway_region_id
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.gateway_version is not None:
            result['GatewayVersion'] = self.gateway_version
        if self.high_availability is not None:
            result['HighAvailability'] = self.high_availability
        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip
        if self.inner_ipv_6ip is not None:
            result['InnerIpv6Ip'] = self.inner_ipv_6ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.is_post_paid is not None:
            result['IsPostPaid'] = self.is_post_paid
        if self.is_release_after_expiration is not None:
            result['IsReleaseAfterExpiration'] = self.is_release_after_expiration
        if self.last_error_key is not None:
            result['LastErrorKey'] = self.last_error_key
        if self.location is not None:
            result['Location'] = self.location
        if self.max_throughput is not None:
            result['MaxThroughput'] = self.max_throughput
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.public_network_bandwidth is not None:
            result['PublicNetworkBandwidth'] = self.public_network_bandwidth
        if self.renew_url is not None:
            result['RenewURL'] = self.renew_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        if self.untrusted_env_instance_type is not None:
            result['UntrustedEnvInstanceType'] = self.untrusted_env_instance_type
        if self.untrusted_env_oss_endpoint is not None:
            result['UntrustedEnvOssEndpoint'] = self.untrusted_env_oss_endpoint
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivatedTime') is not None:
            self.activated_time = m.get('ActivatedTime')
        if m.get('BuyURL') is not None:
            self.buy_url = m.get('BuyURL')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CommonBuyInstanceId') is not None:
            self.common_buy_instance_id = m.get('CommonBuyInstanceId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataLoadInterval') is not None:
            self.data_load_interval = m.get('DataLoadInterval')
        if m.get('DataLoadType') is not None:
            self.data_load_type = m.get('DataLoadType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('ElasticGateway') is not None:
            self.elastic_gateway = m.get('ElasticGateway')
        if m.get('ElasticNodes') is not None:
            temp_model = DescribeGatewayResponseBodyElasticNodes()
            self.elastic_nodes = temp_model.from_map(m['ElasticNodes'])
        if m.get('ExpireStatus') is not None:
            self.expire_status = m.get('ExpireStatus')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GatewayClass') is not None:
            self.gateway_class = m.get('GatewayClass')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayRegionId') is not None:
            self.gateway_region_id = m.get('GatewayRegionId')
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')
        if m.get('GatewayVersion') is not None:
            self.gateway_version = m.get('GatewayVersion')
        if m.get('HighAvailability') is not None:
            self.high_availability = m.get('HighAvailability')
        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')
        if m.get('InnerIpv6Ip') is not None:
            self.inner_ipv_6ip = m.get('InnerIpv6Ip')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IsPostPaid') is not None:
            self.is_post_paid = m.get('IsPostPaid')
        if m.get('IsReleaseAfterExpiration') is not None:
            self.is_release_after_expiration = m.get('IsReleaseAfterExpiration')
        if m.get('LastErrorKey') is not None:
            self.last_error_key = m.get('LastErrorKey')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxThroughput') is not None:
            self.max_throughput = m.get('MaxThroughput')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PublicNetworkBandwidth') is not None:
            self.public_network_bandwidth = m.get('PublicNetworkBandwidth')
        if m.get('RenewURL') is not None:
            self.renew_url = m.get('RenewURL')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UntrustedEnvInstanceType') is not None:
            self.untrusted_env_instance_type = m.get('UntrustedEnvInstanceType')
        if m.get('UntrustedEnvOssEndpoint') is not None:
            self.untrusted_env_oss_endpoint = m.get('UntrustedEnvOssEndpoint')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayResponseBody = None,
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
            temp_model = DescribeGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayADInfoRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayADInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        domain_name: str = None,
        is_enabled: bool = None,
        message: str = None,
        request_id: str = None,
        server_ip: str = None,
        success: bool = None,
        username: str = None,
    ):
        self.code = code
        self.domain_name = domain_name
        self.is_enabled = is_enabled
        self.message = message
        self.request_id = request_id
        self.server_ip = server_ip
        self.success = success
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.success is not None:
            result['Success'] = self.success
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeGatewayADInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayADInfoResponseBody = None,
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
            temp_model = DescribeGatewayADInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayActionsRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayActionsResponseBodyActionsAction(TeaModel):
    def __init__(
        self,
        ad_ldap: str = None,
        cache: str = None,
        disk: str = None,
        gateway_id: str = None,
        monitor: str = None,
        self_: str = None,
        smb_user: str = None,
        target: str = None,
    ):
        self.ad_ldap = ad_ldap
        self.cache = cache
        self.disk = disk
        self.gateway_id = gateway_id
        self.monitor = monitor
        self.self_ = self_
        self.smb_user = smb_user
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_ldap is not None:
            result['AdLdap'] = self.ad_ldap
        if self.cache is not None:
            result['Cache'] = self.cache
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.monitor is not None:
            result['Monitor'] = self.monitor
        if self.self_ is not None:
            result['Self'] = self.self_
        if self.smb_user is not None:
            result['SmbUser'] = self.smb_user
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdLdap') is not None:
            self.ad_ldap = m.get('AdLdap')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Monitor') is not None:
            self.monitor = m.get('Monitor')
        if m.get('Self') is not None:
            self.self_ = m.get('Self')
        if m.get('SmbUser') is not None:
            self.smb_user = m.get('SmbUser')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class DescribeGatewayActionsResponseBodyActions(TeaModel):
    def __init__(
        self,
        action: List[DescribeGatewayActionsResponseBodyActionsAction] = None,
    ):
        self.action = action

    def validate(self):
        if self.action:
            for k in self.action:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Action'] = []
        if self.action is not None:
            for k in self.action:
                result['Action'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action = []
        if m.get('Action') is not None:
            for k in m.get('Action'):
                temp_model = DescribeGatewayActionsResponseBodyActionsAction()
                self.action.append(temp_model.from_map(k))
        return self


class DescribeGatewayActionsResponseBody(TeaModel):
    def __init__(
        self,
        actions: DescribeGatewayActionsResponseBodyActions = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.actions = actions
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.actions:
            self.actions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['Actions'] = self.actions.to_map()
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
        if m.get('Actions') is not None:
            temp_model = DescribeGatewayActionsResponseBodyActions()
            self.actions = temp_model.from_map(m['Actions'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayActionsResponseBody = None,
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
            temp_model = DescribeGatewayActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayAuthInfoRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayAuthInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        password: str = None,
        public_ip: str = None,
        request_id: str = None,
        success: bool = None,
        username: str = None,
    ):
        self.code = code
        self.message = message
        self.password = password
        self.public_ip = public_ip
        self.request_id = request_id
        self.success = success
        self.username = username

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
        if self.password is not None:
            result['Password'] = self.password
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeGatewayAuthInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayAuthInfoResponseBody = None,
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
            temp_model = DescribeGatewayAuthInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayAutoPlansRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayAutoPlansResponseBodyAutoPlans(TeaModel):
    def __init__(
        self,
        detail: str = None,
        end_time: int = None,
        event: str = None,
        plan_id: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.detail = detail
        self.end_time = end_time
        self.event = event
        self.plan_id = plan_id
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeGatewayAutoPlansResponseBody(TeaModel):
    def __init__(
        self,
        auto_plans: List[DescribeGatewayAutoPlansResponseBodyAutoPlans] = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.auto_plans = auto_plans
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.auto_plans:
            for k in self.auto_plans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoPlans'] = []
        if self.auto_plans is not None:
            for k in self.auto_plans:
                result['AutoPlans'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
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
        self.auto_plans = []
        if m.get('AutoPlans') is not None:
            for k in m.get('AutoPlans'):
                temp_model = DescribeGatewayAutoPlansResponseBodyAutoPlans()
                self.auto_plans.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
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


class DescribeGatewayAutoPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayAutoPlansResponseBody = None,
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
            temp_model = DescribeGatewayAutoPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayAutoUpgradeConfigurationRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayAutoUpgradeConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        auto_upgrade_end_hour: int = None,
        auto_upgrade_start_hour: int = None,
        code: str = None,
        is_auto_upgrade: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.auto_upgrade_end_hour = auto_upgrade_end_hour
        self.auto_upgrade_start_hour = auto_upgrade_start_hour
        self.code = code
        self.is_auto_upgrade = is_auto_upgrade
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
        if self.auto_upgrade_end_hour is not None:
            result['AutoUpgradeEndHour'] = self.auto_upgrade_end_hour
        if self.auto_upgrade_start_hour is not None:
            result['AutoUpgradeStartHour'] = self.auto_upgrade_start_hour
        if self.code is not None:
            result['Code'] = self.code
        if self.is_auto_upgrade is not None:
            result['IsAutoUpgrade'] = self.is_auto_upgrade
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpgradeEndHour') is not None:
            self.auto_upgrade_end_hour = m.get('AutoUpgradeEndHour')
        if m.get('AutoUpgradeStartHour') is not None:
            self.auto_upgrade_start_hour = m.get('AutoUpgradeStartHour')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsAutoUpgrade') is not None:
            self.is_auto_upgrade = m.get('IsAutoUpgrade')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayAutoUpgradeConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayAutoUpgradeConfigurationResponseBody = None,
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
            temp_model = DescribeGatewayAutoUpgradeConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayBlockVolumesRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        index_id: str = None,
        refresh: bool = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.refresh = refresh
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.refresh is not None:
            result['Refresh'] = self.refresh
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('Refresh') is not None:
            self.refresh = m.get('Refresh')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayBlockVolumesResponseBodyBlockVolumesBlockVolume(TeaModel):
    def __init__(
        self,
        address: str = None,
        cache_mode: str = None,
        chap_enabled: bool = None,
        chap_in_user: str = None,
        chunk_size: int = None,
        disk_id: str = None,
        disk_type: str = None,
        enabled: bool = None,
        index_id: str = None,
        local_path: str = None,
        lun_id: int = None,
        name: str = None,
        oss_bucket_name: str = None,
        oss_bucket_ssl: bool = None,
        oss_endpoint: str = None,
        port: int = None,
        protocol: str = None,
        size: int = None,
        state: str = None,
        status: int = None,
        target: str = None,
        total_download: int = None,
        total_upload: int = None,
        volume_state: int = None,
    ):
        self.address = address
        self.cache_mode = cache_mode
        self.chap_enabled = chap_enabled
        self.chap_in_user = chap_in_user
        self.chunk_size = chunk_size
        self.disk_id = disk_id
        self.disk_type = disk_type
        self.enabled = enabled
        self.index_id = index_id
        self.local_path = local_path
        # LUN ID。
        self.lun_id = lun_id
        self.name = name
        self.oss_bucket_name = oss_bucket_name
        self.oss_bucket_ssl = oss_bucket_ssl
        self.oss_endpoint = oss_endpoint
        self.port = port
        self.protocol = protocol
        self.size = size
        self.state = state
        self.status = status
        self.target = target
        self.total_download = total_download
        self.total_upload = total_upload
        self.volume_state = volume_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.cache_mode is not None:
            result['CacheMode'] = self.cache_mode
        if self.chap_enabled is not None:
            result['ChapEnabled'] = self.chap_enabled
        if self.chap_in_user is not None:
            result['ChapInUser'] = self.chap_in_user
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.local_path is not None:
            result['LocalPath'] = self.local_path
        if self.lun_id is not None:
            result['LunId'] = self.lun_id
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_bucket_ssl is not None:
            result['OssBucketSsl'] = self.oss_bucket_ssl
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.size is not None:
            result['Size'] = self.size
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.target is not None:
            result['Target'] = self.target
        if self.total_download is not None:
            result['TotalDownload'] = self.total_download
        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload
        if self.volume_state is not None:
            result['VolumeState'] = self.volume_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CacheMode') is not None:
            self.cache_mode = m.get('CacheMode')
        if m.get('ChapEnabled') is not None:
            self.chap_enabled = m.get('ChapEnabled')
        if m.get('ChapInUser') is not None:
            self.chap_in_user = m.get('ChapInUser')
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('LocalPath') is not None:
            self.local_path = m.get('LocalPath')
        if m.get('LunId') is not None:
            self.lun_id = m.get('LunId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssBucketSsl') is not None:
            self.oss_bucket_ssl = m.get('OssBucketSsl')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')
        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')
        if m.get('VolumeState') is not None:
            self.volume_state = m.get('VolumeState')
        return self


class DescribeGatewayBlockVolumesResponseBodyBlockVolumes(TeaModel):
    def __init__(
        self,
        block_volume: List[DescribeGatewayBlockVolumesResponseBodyBlockVolumesBlockVolume] = None,
    ):
        self.block_volume = block_volume

    def validate(self):
        if self.block_volume:
            for k in self.block_volume:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockVolume'] = []
        if self.block_volume is not None:
            for k in self.block_volume:
                result['BlockVolume'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_volume = []
        if m.get('BlockVolume') is not None:
            for k in m.get('BlockVolume'):
                temp_model = DescribeGatewayBlockVolumesResponseBodyBlockVolumesBlockVolume()
                self.block_volume.append(temp_model.from_map(k))
        return self


class DescribeGatewayBlockVolumesResponseBody(TeaModel):
    def __init__(
        self,
        block_volumes: DescribeGatewayBlockVolumesResponseBodyBlockVolumes = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.block_volumes = block_volumes
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.block_volumes:
            self.block_volumes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_volumes is not None:
            result['BlockVolumes'] = self.block_volumes.to_map()
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
        if m.get('BlockVolumes') is not None:
            temp_model = DescribeGatewayBlockVolumesResponseBodyBlockVolumes()
            self.block_volumes = temp_model.from_map(m['BlockVolumes'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayBlockVolumesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayBlockVolumesResponseBody = None,
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
            temp_model = DescribeGatewayBlockVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayBucketCachesRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.bucket_name = bucket_name
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayBucketCachesResponseBodyBucketCachesBucketCache(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        cache_mode: str = None,
        cache_stats: str = None,
        category: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        location: str = None,
        mount_point: str = None,
        protocol: str = None,
        region_id: str = None,
        share_name: str = None,
        type: str = None,
        vpc_cidr: str = None,
        vpc_id: str = None,
    ):
        self.bucket_name = bucket_name
        self.cache_mode = cache_mode
        self.cache_stats = cache_stats
        self.category = category
        self.gateway_id = gateway_id
        self.gateway_name = gateway_name
        self.location = location
        self.mount_point = mount_point
        self.protocol = protocol
        self.region_id = region_id
        self.share_name = share_name
        self.type = type
        self.vpc_cidr = vpc_cidr
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.cache_mode is not None:
            result['CacheMode'] = self.cache_mode
        if self.cache_stats is not None:
            result['CacheStats'] = self.cache_stats
        if self.category is not None:
            result['Category'] = self.category
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.location is not None:
            result['Location'] = self.location
        if self.mount_point is not None:
            result['MountPoint'] = self.mount_point
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_name is not None:
            result['ShareName'] = self.share_name
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_cidr is not None:
            result['VpcCidr'] = self.vpc_cidr
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CacheMode') is not None:
            self.cache_mode = m.get('CacheMode')
        if m.get('CacheStats') is not None:
            self.cache_stats = m.get('CacheStats')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MountPoint') is not None:
            self.mount_point = m.get('MountPoint')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareName') is not None:
            self.share_name = m.get('ShareName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcCidr') is not None:
            self.vpc_cidr = m.get('VpcCidr')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeGatewayBucketCachesResponseBodyBucketCaches(TeaModel):
    def __init__(
        self,
        bucket_cache: List[DescribeGatewayBucketCachesResponseBodyBucketCachesBucketCache] = None,
    ):
        self.bucket_cache = bucket_cache

    def validate(self):
        if self.bucket_cache:
            for k in self.bucket_cache:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BucketCache'] = []
        if self.bucket_cache is not None:
            for k in self.bucket_cache:
                result['BucketCache'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bucket_cache = []
        if m.get('BucketCache') is not None:
            for k in m.get('BucketCache'):
                temp_model = DescribeGatewayBucketCachesResponseBodyBucketCachesBucketCache()
                self.bucket_cache.append(temp_model.from_map(k))
        return self


class DescribeGatewayBucketCachesResponseBody(TeaModel):
    def __init__(
        self,
        bucket_caches: DescribeGatewayBucketCachesResponseBodyBucketCaches = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.bucket_caches = bucket_caches
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.bucket_caches:
            self.bucket_caches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_caches is not None:
            result['BucketCaches'] = self.bucket_caches.to_map()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('BucketCaches') is not None:
            temp_model = DescribeGatewayBucketCachesResponseBodyBucketCaches()
            self.bucket_caches = temp_model.from_map(m['BucketCaches'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
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


class DescribeGatewayBucketCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayBucketCachesResponseBody = None,
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
            temp_model = DescribeGatewayBucketCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayCachesRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayCachesResponseBodyCachesCache(TeaModel):
    def __init__(
        self,
        buy_url: str = None,
        cache_id: str = None,
        cache_type: str = None,
        expire_status: int = None,
        expired_time: int = None,
        iops: int = None,
        is_direct_expand: str = None,
        is_no_partition: bool = None,
        is_used: bool = None,
        local_file_path: str = None,
        performance_level: str = None,
        renew_url: str = None,
        size_in_gb: int = None,
        subscription_instance_id: str = None,
    ):
        self.buy_url = buy_url
        self.cache_id = cache_id
        self.cache_type = cache_type
        self.expire_status = expire_status
        self.expired_time = expired_time
        # IOPS。
        self.iops = iops
        self.is_direct_expand = is_direct_expand
        self.is_no_partition = is_no_partition
        self.is_used = is_used
        self.local_file_path = local_file_path
        self.performance_level = performance_level
        self.renew_url = renew_url
        self.size_in_gb = size_in_gb
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_url is not None:
            result['BuyURL'] = self.buy_url
        if self.cache_id is not None:
            result['CacheId'] = self.cache_id
        if self.cache_type is not None:
            result['CacheType'] = self.cache_type
        if self.expire_status is not None:
            result['ExpireStatus'] = self.expire_status
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.iops is not None:
            result['Iops'] = self.iops
        if self.is_direct_expand is not None:
            result['IsDirectExpand'] = self.is_direct_expand
        if self.is_no_partition is not None:
            result['IsNoPartition'] = self.is_no_partition
        if self.is_used is not None:
            result['IsUsed'] = self.is_used
        if self.local_file_path is not None:
            result['LocalFilePath'] = self.local_file_path
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.renew_url is not None:
            result['RenewURL'] = self.renew_url
        if self.size_in_gb is not None:
            result['SizeInGB'] = self.size_in_gb
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyURL') is not None:
            self.buy_url = m.get('BuyURL')
        if m.get('CacheId') is not None:
            self.cache_id = m.get('CacheId')
        if m.get('CacheType') is not None:
            self.cache_type = m.get('CacheType')
        if m.get('ExpireStatus') is not None:
            self.expire_status = m.get('ExpireStatus')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Iops') is not None:
            self.iops = m.get('Iops')
        if m.get('IsDirectExpand') is not None:
            self.is_direct_expand = m.get('IsDirectExpand')
        if m.get('IsNoPartition') is not None:
            self.is_no_partition = m.get('IsNoPartition')
        if m.get('IsUsed') is not None:
            self.is_used = m.get('IsUsed')
        if m.get('LocalFilePath') is not None:
            self.local_file_path = m.get('LocalFilePath')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('RenewURL') is not None:
            self.renew_url = m.get('RenewURL')
        if m.get('SizeInGB') is not None:
            self.size_in_gb = m.get('SizeInGB')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class DescribeGatewayCachesResponseBodyCaches(TeaModel):
    def __init__(
        self,
        cache: List[DescribeGatewayCachesResponseBodyCachesCache] = None,
    ):
        self.cache = cache

    def validate(self):
        if self.cache:
            for k in self.cache:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cache'] = []
        if self.cache is not None:
            for k in self.cache:
                result['Cache'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cache = []
        if m.get('Cache') is not None:
            for k in m.get('Cache'):
                temp_model = DescribeGatewayCachesResponseBodyCachesCache()
                self.cache.append(temp_model.from_map(k))
        return self


class DescribeGatewayCachesResponseBody(TeaModel):
    def __init__(
        self,
        caches: DescribeGatewayCachesResponseBodyCaches = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.caches = caches
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.caches:
            self.caches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caches is not None:
            result['Caches'] = self.caches.to_map()
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
        if m.get('Caches') is not None:
            temp_model = DescribeGatewayCachesResponseBodyCaches()
            self.caches = temp_model.from_map(m['Caches'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayCachesResponseBody = None,
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
            temp_model = DescribeGatewayCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayCapacityLimitRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
        size_in_gb: int = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.size_in_gb = size_in_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.size_in_gb is not None:
            result['SizeInGB'] = self.size_in_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SizeInGB') is not None:
            self.size_in_gb = m.get('SizeInGB')
        return self


class DescribeGatewayCapacityLimitResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        file_number: int = None,
        file_system_size_in_tb: int = None,
        is_metadata_separate: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.file_number = file_number
        self.file_system_size_in_tb = file_system_size_in_tb
        self.is_metadata_separate = is_metadata_separate
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
        if self.file_number is not None:
            result['FileNumber'] = self.file_number
        if self.file_system_size_in_tb is not None:
            result['FileSystemSizeInTB'] = self.file_system_size_in_tb
        if self.is_metadata_separate is not None:
            result['IsMetadataSeparate'] = self.is_metadata_separate
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
        if m.get('FileNumber') is not None:
            self.file_number = m.get('FileNumber')
        if m.get('FileSystemSizeInTB') is not None:
            self.file_system_size_in_tb = m.get('FileSystemSizeInTB')
        if m.get('IsMetadataSeparate') is not None:
            self.is_metadata_separate = m.get('IsMetadataSeparate')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayCapacityLimitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayCapacityLimitResponseBody = None,
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
            temp_model = DescribeGatewayCapacityLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayCategoriesRequest(TeaModel):
    def __init__(
        self,
        gateway_location: str = None,
        security_token: str = None,
    ):
        self.gateway_location = gateway_location
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_location is not None:
            result['GatewayLocation'] = self.gateway_location
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayLocation') is not None:
            self.gateway_location = m.get('GatewayLocation')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        categories: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.categories = categories
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
        if self.categories is not None:
            result['Categories'] = self.categories
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
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayCategoriesResponseBody = None,
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
            temp_model = DescribeGatewayCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayClassesRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
    ):
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayClassesResponseBody(TeaModel):
    def __init__(
        self,
        classes: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.classes = classes
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
        if self.classes is not None:
            result['Classes'] = self.classes
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
        if m.get('Classes') is not None:
            self.classes = m.get('Classes')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayClassesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayClassesResponseBody = None,
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
            temp_model = DescribeGatewayClassesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayCredentialRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayCredentialResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        console_password: str = None,
        console_username: str = None,
        ecs_ip: str = None,
        ecs_password: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.code = code
        self.console_password = console_password
        self.console_username = console_username
        self.ecs_ip = ecs_ip
        self.ecs_password = ecs_password
        self.message = message
        self.request_id = request_id
        self.success = success
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.console_password is not None:
            result['ConsolePassword'] = self.console_password
        if self.console_username is not None:
            result['ConsoleUsername'] = self.console_username
        if self.ecs_ip is not None:
            result['EcsIp'] = self.ecs_ip
        if self.ecs_password is not None:
            result['EcsPassword'] = self.ecs_password
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConsolePassword') is not None:
            self.console_password = m.get('ConsolePassword')
        if m.get('ConsoleUsername') is not None:
            self.console_username = m.get('ConsoleUsername')
        if m.get('EcsIp') is not None:
            self.ecs_ip = m.get('EcsIp')
        if m.get('EcsPassword') is not None:
            self.ecs_password = m.get('EcsPassword')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeGatewayCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayCredentialResponseBody = None,
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
            temp_model = DescribeGatewayCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayDNSRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayDNSResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dns_server: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dns_server = dns_server
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
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server
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
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayDNSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayDNSResponseBody = None,
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
            temp_model = DescribeGatewayDNSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayFileSharesRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        index_id: str = None,
        refresh: bool = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.refresh = refresh
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.refresh is not None:
            result['Refresh'] = self.refresh
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('Refresh') is not None:
            self.refresh = m.get('Refresh')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayFileSharesResponseBodyFileSharesFileShare(TeaModel):
    def __init__(
        self,
        access_based_enumeration: bool = None,
        active_messages: int = None,
        address: str = None,
        be_limit: int = None,
        browsable: bool = None,
        bucket_infos: str = None,
        buckets_stub: bool = None,
        bypass_cache_read: bool = None,
        cache_mode: str = None,
        client_side_cmk: str = None,
        client_side_encryption: bool = None,
        direct_io: bool = None,
        disk_id: str = None,
        disk_type: str = None,
        download_limit: int = None,
        download_queue: int = None,
        download_rate: int = None,
        enabled: bool = None,
        express_sync_id: str = None,
        fast_reclaim: bool = None,
        fe_limit: int = None,
        file_num_limit: int = None,
        fs_size_limit: int = None,
        high_watermark: int = None,
        ignore_delete: bool = None,
        in_place: bool = None,
        in_rate: int = None,
        index_id: str = None,
        kms_rotate_period: str = None,
        lag_period: int = None,
        local_path: str = None,
        low_watermark: int = None,
        mns_health: str = None,
        name: str = None,
        nfs_v4optimization: bool = None,
        no_partition: bool = None,
        obsolete_buckets: str = None,
        oss_bucket_name: str = None,
        oss_bucket_ssl: bool = None,
        oss_endpoint: str = None,
        oss_health: str = None,
        oss_used: int = None,
        out_rate: int = None,
        partial_sync_paths: str = None,
        path_prefix: str = None,
        polling_interval: int = None,
        protocol: str = None,
        remaining_meta_space: int = None,
        remote_sync: bool = None,
        remote_sync_download: bool = None,
        ro_client_list: str = None,
        ro_user_list: str = None,
        rw_client_list: str = None,
        rw_user_list: str = None,
        server_side_algorithm: str = None,
        server_side_cmk: str = None,
        server_side_encryption: bool = None,
        size: int = None,
        squash: str = None,
        state: str = None,
        status: str = None,
        support_archive: bool = None,
        sync_progress: int = None,
        throttling: bool = None,
        total_download: int = None,
        total_upload: int = None,
        transfer_acceleration: bool = None,
        upload_queue: int = None,
        used: int = None,
        windows_acl: bool = None,
    ):
        self.access_based_enumeration = access_based_enumeration
        self.active_messages = active_messages
        self.address = address
        self.be_limit = be_limit
        self.browsable = browsable
        self.bucket_infos = bucket_infos
        self.buckets_stub = buckets_stub
        self.bypass_cache_read = bypass_cache_read
        self.cache_mode = cache_mode
        self.client_side_cmk = client_side_cmk
        self.client_side_encryption = client_side_encryption
        self.direct_io = direct_io
        self.disk_id = disk_id
        self.disk_type = disk_type
        self.download_limit = download_limit
        self.download_queue = download_queue
        self.download_rate = download_rate
        self.enabled = enabled
        self.express_sync_id = express_sync_id
        self.fast_reclaim = fast_reclaim
        self.fe_limit = fe_limit
        self.file_num_limit = file_num_limit
        self.fs_size_limit = fs_size_limit
        self.high_watermark = high_watermark
        self.ignore_delete = ignore_delete
        self.in_place = in_place
        self.in_rate = in_rate
        self.index_id = index_id
        self.kms_rotate_period = kms_rotate_period
        self.lag_period = lag_period
        self.local_path = local_path
        self.low_watermark = low_watermark
        self.mns_health = mns_health
        self.name = name
        self.nfs_v4optimization = nfs_v4optimization
        self.no_partition = no_partition
        self.obsolete_buckets = obsolete_buckets
        self.oss_bucket_name = oss_bucket_name
        self.oss_bucket_ssl = oss_bucket_ssl
        self.oss_endpoint = oss_endpoint
        self.oss_health = oss_health
        self.oss_used = oss_used
        self.out_rate = out_rate
        self.partial_sync_paths = partial_sync_paths
        # OSS Prefix。
        self.path_prefix = path_prefix
        self.polling_interval = polling_interval
        self.protocol = protocol
        self.remaining_meta_space = remaining_meta_space
        self.remote_sync = remote_sync
        self.remote_sync_download = remote_sync_download
        self.ro_client_list = ro_client_list
        self.ro_user_list = ro_user_list
        self.rw_client_list = rw_client_list
        self.rw_user_list = rw_user_list
        self.server_side_algorithm = server_side_algorithm
        self.server_side_cmk = server_side_cmk
        self.server_side_encryption = server_side_encryption
        self.size = size
        self.squash = squash
        self.state = state
        self.status = status
        self.support_archive = support_archive
        self.sync_progress = sync_progress
        self.throttling = throttling
        self.total_download = total_download
        self.total_upload = total_upload
        self.transfer_acceleration = transfer_acceleration
        self.upload_queue = upload_queue
        self.used = used
        self.windows_acl = windows_acl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_based_enumeration is not None:
            result['AccessBasedEnumeration'] = self.access_based_enumeration
        if self.active_messages is not None:
            result['ActiveMessages'] = self.active_messages
        if self.address is not None:
            result['Address'] = self.address
        if self.be_limit is not None:
            result['BeLimit'] = self.be_limit
        if self.browsable is not None:
            result['Browsable'] = self.browsable
        if self.bucket_infos is not None:
            result['BucketInfos'] = self.bucket_infos
        if self.buckets_stub is not None:
            result['BucketsStub'] = self.buckets_stub
        if self.bypass_cache_read is not None:
            result['BypassCacheRead'] = self.bypass_cache_read
        if self.cache_mode is not None:
            result['CacheMode'] = self.cache_mode
        if self.client_side_cmk is not None:
            result['ClientSideCmk'] = self.client_side_cmk
        if self.client_side_encryption is not None:
            result['ClientSideEncryption'] = self.client_side_encryption
        if self.direct_io is not None:
            result['DirectIO'] = self.direct_io
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.download_limit is not None:
            result['DownloadLimit'] = self.download_limit
        if self.download_queue is not None:
            result['DownloadQueue'] = self.download_queue
        if self.download_rate is not None:
            result['DownloadRate'] = self.download_rate
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.express_sync_id is not None:
            result['ExpressSyncId'] = self.express_sync_id
        if self.fast_reclaim is not None:
            result['FastReclaim'] = self.fast_reclaim
        if self.fe_limit is not None:
            result['FeLimit'] = self.fe_limit
        if self.file_num_limit is not None:
            result['FileNumLimit'] = self.file_num_limit
        if self.fs_size_limit is not None:
            result['FsSizeLimit'] = self.fs_size_limit
        if self.high_watermark is not None:
            result['HighWatermark'] = self.high_watermark
        if self.ignore_delete is not None:
            result['IgnoreDelete'] = self.ignore_delete
        if self.in_place is not None:
            result['InPlace'] = self.in_place
        if self.in_rate is not None:
            result['InRate'] = self.in_rate
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.kms_rotate_period is not None:
            result['KmsRotatePeriod'] = self.kms_rotate_period
        if self.lag_period is not None:
            result['LagPeriod'] = self.lag_period
        if self.local_path is not None:
            result['LocalPath'] = self.local_path
        if self.low_watermark is not None:
            result['LowWatermark'] = self.low_watermark
        if self.mns_health is not None:
            result['MnsHealth'] = self.mns_health
        if self.name is not None:
            result['Name'] = self.name
        if self.nfs_v4optimization is not None:
            result['NfsV4Optimization'] = self.nfs_v4optimization
        if self.no_partition is not None:
            result['NoPartition'] = self.no_partition
        if self.obsolete_buckets is not None:
            result['ObsoleteBuckets'] = self.obsolete_buckets
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_bucket_ssl is not None:
            result['OssBucketSsl'] = self.oss_bucket_ssl
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_health is not None:
            result['OssHealth'] = self.oss_health
        if self.oss_used is not None:
            result['OssUsed'] = self.oss_used
        if self.out_rate is not None:
            result['OutRate'] = self.out_rate
        if self.partial_sync_paths is not None:
            result['PartialSyncPaths'] = self.partial_sync_paths
        if self.path_prefix is not None:
            result['PathPrefix'] = self.path_prefix
        if self.polling_interval is not None:
            result['PollingInterval'] = self.polling_interval
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.remaining_meta_space is not None:
            result['RemainingMetaSpace'] = self.remaining_meta_space
        if self.remote_sync is not None:
            result['RemoteSync'] = self.remote_sync
        if self.remote_sync_download is not None:
            result['RemoteSyncDownload'] = self.remote_sync_download
        if self.ro_client_list is not None:
            result['RoClientList'] = self.ro_client_list
        if self.ro_user_list is not None:
            result['RoUserList'] = self.ro_user_list
        if self.rw_client_list is not None:
            result['RwClientList'] = self.rw_client_list
        if self.rw_user_list is not None:
            result['RwUserList'] = self.rw_user_list
        if self.server_side_algorithm is not None:
            result['ServerSideAlgorithm'] = self.server_side_algorithm
        if self.server_side_cmk is not None:
            result['ServerSideCmk'] = self.server_side_cmk
        if self.server_side_encryption is not None:
            result['ServerSideEncryption'] = self.server_side_encryption
        if self.size is not None:
            result['Size'] = self.size
        if self.squash is not None:
            result['Squash'] = self.squash
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.support_archive is not None:
            result['SupportArchive'] = self.support_archive
        if self.sync_progress is not None:
            result['SyncProgress'] = self.sync_progress
        if self.throttling is not None:
            result['Throttling'] = self.throttling
        if self.total_download is not None:
            result['TotalDownload'] = self.total_download
        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload
        if self.transfer_acceleration is not None:
            result['TransferAcceleration'] = self.transfer_acceleration
        if self.upload_queue is not None:
            result['UploadQueue'] = self.upload_queue
        if self.used is not None:
            result['Used'] = self.used
        if self.windows_acl is not None:
            result['WindowsAcl'] = self.windows_acl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessBasedEnumeration') is not None:
            self.access_based_enumeration = m.get('AccessBasedEnumeration')
        if m.get('ActiveMessages') is not None:
            self.active_messages = m.get('ActiveMessages')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BeLimit') is not None:
            self.be_limit = m.get('BeLimit')
        if m.get('Browsable') is not None:
            self.browsable = m.get('Browsable')
        if m.get('BucketInfos') is not None:
            self.bucket_infos = m.get('BucketInfos')
        if m.get('BucketsStub') is not None:
            self.buckets_stub = m.get('BucketsStub')
        if m.get('BypassCacheRead') is not None:
            self.bypass_cache_read = m.get('BypassCacheRead')
        if m.get('CacheMode') is not None:
            self.cache_mode = m.get('CacheMode')
        if m.get('ClientSideCmk') is not None:
            self.client_side_cmk = m.get('ClientSideCmk')
        if m.get('ClientSideEncryption') is not None:
            self.client_side_encryption = m.get('ClientSideEncryption')
        if m.get('DirectIO') is not None:
            self.direct_io = m.get('DirectIO')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DownloadLimit') is not None:
            self.download_limit = m.get('DownloadLimit')
        if m.get('DownloadQueue') is not None:
            self.download_queue = m.get('DownloadQueue')
        if m.get('DownloadRate') is not None:
            self.download_rate = m.get('DownloadRate')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExpressSyncId') is not None:
            self.express_sync_id = m.get('ExpressSyncId')
        if m.get('FastReclaim') is not None:
            self.fast_reclaim = m.get('FastReclaim')
        if m.get('FeLimit') is not None:
            self.fe_limit = m.get('FeLimit')
        if m.get('FileNumLimit') is not None:
            self.file_num_limit = m.get('FileNumLimit')
        if m.get('FsSizeLimit') is not None:
            self.fs_size_limit = m.get('FsSizeLimit')
        if m.get('HighWatermark') is not None:
            self.high_watermark = m.get('HighWatermark')
        if m.get('IgnoreDelete') is not None:
            self.ignore_delete = m.get('IgnoreDelete')
        if m.get('InPlace') is not None:
            self.in_place = m.get('InPlace')
        if m.get('InRate') is not None:
            self.in_rate = m.get('InRate')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('KmsRotatePeriod') is not None:
            self.kms_rotate_period = m.get('KmsRotatePeriod')
        if m.get('LagPeriod') is not None:
            self.lag_period = m.get('LagPeriod')
        if m.get('LocalPath') is not None:
            self.local_path = m.get('LocalPath')
        if m.get('LowWatermark') is not None:
            self.low_watermark = m.get('LowWatermark')
        if m.get('MnsHealth') is not None:
            self.mns_health = m.get('MnsHealth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NfsV4Optimization') is not None:
            self.nfs_v4optimization = m.get('NfsV4Optimization')
        if m.get('NoPartition') is not None:
            self.no_partition = m.get('NoPartition')
        if m.get('ObsoleteBuckets') is not None:
            self.obsolete_buckets = m.get('ObsoleteBuckets')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssBucketSsl') is not None:
            self.oss_bucket_ssl = m.get('OssBucketSsl')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssHealth') is not None:
            self.oss_health = m.get('OssHealth')
        if m.get('OssUsed') is not None:
            self.oss_used = m.get('OssUsed')
        if m.get('OutRate') is not None:
            self.out_rate = m.get('OutRate')
        if m.get('PartialSyncPaths') is not None:
            self.partial_sync_paths = m.get('PartialSyncPaths')
        if m.get('PathPrefix') is not None:
            self.path_prefix = m.get('PathPrefix')
        if m.get('PollingInterval') is not None:
            self.polling_interval = m.get('PollingInterval')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RemainingMetaSpace') is not None:
            self.remaining_meta_space = m.get('RemainingMetaSpace')
        if m.get('RemoteSync') is not None:
            self.remote_sync = m.get('RemoteSync')
        if m.get('RemoteSyncDownload') is not None:
            self.remote_sync_download = m.get('RemoteSyncDownload')
        if m.get('RoClientList') is not None:
            self.ro_client_list = m.get('RoClientList')
        if m.get('RoUserList') is not None:
            self.ro_user_list = m.get('RoUserList')
        if m.get('RwClientList') is not None:
            self.rw_client_list = m.get('RwClientList')
        if m.get('RwUserList') is not None:
            self.rw_user_list = m.get('RwUserList')
        if m.get('ServerSideAlgorithm') is not None:
            self.server_side_algorithm = m.get('ServerSideAlgorithm')
        if m.get('ServerSideCmk') is not None:
            self.server_side_cmk = m.get('ServerSideCmk')
        if m.get('ServerSideEncryption') is not None:
            self.server_side_encryption = m.get('ServerSideEncryption')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Squash') is not None:
            self.squash = m.get('Squash')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportArchive') is not None:
            self.support_archive = m.get('SupportArchive')
        if m.get('SyncProgress') is not None:
            self.sync_progress = m.get('SyncProgress')
        if m.get('Throttling') is not None:
            self.throttling = m.get('Throttling')
        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')
        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')
        if m.get('TransferAcceleration') is not None:
            self.transfer_acceleration = m.get('TransferAcceleration')
        if m.get('UploadQueue') is not None:
            self.upload_queue = m.get('UploadQueue')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        if m.get('WindowsAcl') is not None:
            self.windows_acl = m.get('WindowsAcl')
        return self


class DescribeGatewayFileSharesResponseBodyFileShares(TeaModel):
    def __init__(
        self,
        file_share: List[DescribeGatewayFileSharesResponseBodyFileSharesFileShare] = None,
    ):
        self.file_share = file_share

    def validate(self):
        if self.file_share:
            for k in self.file_share:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileShare'] = []
        if self.file_share is not None:
            for k in self.file_share:
                result['FileShare'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_share = []
        if m.get('FileShare') is not None:
            for k in m.get('FileShare'):
                temp_model = DescribeGatewayFileSharesResponseBodyFileSharesFileShare()
                self.file_share.append(temp_model.from_map(k))
        return self


class DescribeGatewayFileSharesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        file_shares: DescribeGatewayFileSharesResponseBodyFileShares = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.file_shares = file_shares
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.file_shares:
            self.file_shares.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.file_shares is not None:
            result['FileShares'] = self.file_shares.to_map()
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
        if m.get('FileShares') is not None:
            temp_model = DescribeGatewayFileSharesResponseBodyFileShares()
            self.file_shares = temp_model.from_map(m['FileShares'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayFileSharesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayFileSharesResponseBody = None,
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
            temp_model = DescribeGatewayFileSharesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayFileStatusRequest(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        gateway_id: str = None,
        index_id: str = None,
        security_token: str = None,
    ):
        self.file_path = file_path
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayFileStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.status = status
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
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayFileStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayFileStatusResponseBody = None,
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
            temp_model = DescribeGatewayFileStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayImagesRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        type: str = None,
    ):
        self.security_token = security_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeGatewayImagesResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        description: str = None,
        md5: str = None,
        modified_date: str = None,
        name: str = None,
        size: int = None,
        title: str = None,
        type: str = None,
        url: str = None,
        version: str = None,
    ):
        self.description = description
        self.md5 = md5
        self.modified_date = modified_date
        self.name = name
        self.size = size
        self.title = title
        self.type = type
        self.url = url
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.md5 is not None:
            result['MD5'] = self.md5
        if self.modified_date is not None:
            result['ModifiedDate'] = self.modified_date
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MD5') is not None:
            self.md5 = m.get('MD5')
        if m.get('ModifiedDate') is not None:
            self.modified_date = m.get('ModifiedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeGatewayImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeGatewayImagesResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeGatewayImagesResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeGatewayImagesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        images: DescribeGatewayImagesResponseBodyImages = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.images = images
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
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
        if m.get('Images') is not None:
            temp_model = DescribeGatewayImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayImagesResponseBody = None,
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
            temp_model = DescribeGatewayImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayInfoRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayInfoResponseBodyGatewayInfosGatewayInfo(TeaModel):
    def __init__(
        self,
        info: str = None,
        time: int = None,
    ):
        self.info = info
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeGatewayInfoResponseBodyGatewayInfos(TeaModel):
    def __init__(
        self,
        gateway_info: List[DescribeGatewayInfoResponseBodyGatewayInfosGatewayInfo] = None,
    ):
        self.gateway_info = gateway_info

    def validate(self):
        if self.gateway_info:
            for k in self.gateway_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GatewayInfo'] = []
        if self.gateway_info is not None:
            for k in self.gateway_info:
                result['GatewayInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway_info = []
        if m.get('GatewayInfo') is not None:
            for k in m.get('GatewayInfo'):
                temp_model = DescribeGatewayInfoResponseBodyGatewayInfosGatewayInfo()
                self.gateway_info.append(temp_model.from_map(k))
        return self


class DescribeGatewayInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gateway_infos: DescribeGatewayInfoResponseBodyGatewayInfos = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.gateway_infos = gateway_infos
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.gateway_infos:
            self.gateway_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.gateway_infos is not None:
            result['GatewayInfos'] = self.gateway_infos.to_map()
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
        if m.get('GatewayInfos') is not None:
            temp_model = DescribeGatewayInfoResponseBodyGatewayInfos()
            self.gateway_infos = temp_model.from_map(m['GatewayInfos'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayInfoResponseBody = None,
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
            temp_model = DescribeGatewayInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayLDAPInfoRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayLDAPInfoResponseBody(TeaModel):
    def __init__(
        self,
        base_dn: str = None,
        code: str = None,
        is_enabled: bool = None,
        is_tls: bool = None,
        message: str = None,
        request_id: str = None,
        root_dn: str = None,
        server_ip: str = None,
        success: bool = None,
    ):
        self.base_dn = base_dn
        self.code = code
        self.is_enabled = is_enabled
        self.is_tls = is_tls
        self.message = message
        self.request_id = request_id
        self.root_dn = root_dn
        self.server_ip = server_ip
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.code is not None:
            result['Code'] = self.code
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.is_tls is not None:
            result['IsTls'] = self.is_tls
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_dn is not None:
            result['RootDN'] = self.root_dn
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('IsTls') is not None:
            self.is_tls = m.get('IsTls')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootDN') is not None:
            self.root_dn = m.get('RootDN')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayLDAPInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayLDAPInfoResponseBody = None,
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
            temp_model = DescribeGatewayLDAPInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayLocationsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
    ):
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayLocationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        locations: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.locations = locations
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
        if self.locations is not None:
            result['Locations'] = self.locations
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
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayLocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayLocationsResponseBody = None,
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
            temp_model = DescribeGatewayLocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayLoggingRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayLoggingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gateway_logging_status: str = None,
        message: str = None,
        request_id: str = None,
        sls_logstore: str = None,
        sls_project: str = None,
        success: bool = None,
    ):
        self.code = code
        self.gateway_logging_status = gateway_logging_status
        self.message = message
        self.request_id = request_id
        self.sls_logstore = sls_logstore
        self.sls_project = sls_project
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
        if self.gateway_logging_status is not None:
            result['GatewayLoggingStatus'] = self.gateway_logging_status
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GatewayLoggingStatus') is not None:
            self.gateway_logging_status = m.get('GatewayLoggingStatus')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayLoggingResponseBody = None,
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
            temp_model = DescribeGatewayLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayLogsRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        log_file_path: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.log_file_path = log_file_path
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.log_file_path is not None:
            result['LogFilePath'] = self.log_file_path
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('LogFilePath') is not None:
            self.log_file_path = m.get('LogFilePath')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayLogsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        log_file_paths: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.log_file_paths = log_file_paths
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
        if self.log_file_paths is not None:
            result['LogFilePaths'] = self.log_file_paths
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
        if m.get('LogFilePaths') is not None:
            self.log_file_paths = m.get('LogFilePaths')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayLogsResponseBody = None,
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
            temp_model = DescribeGatewayLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayModificationClassesRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayModificationClassesResponseBodyTargetGatewayClassesTargetGatewayClass(TeaModel):
    def __init__(
        self,
        gateway_class: str = None,
        is_available: bool = None,
    ):
        self.gateway_class = gateway_class
        self.is_available = is_available

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_class is not None:
            result['GatewayClass'] = self.gateway_class
        if self.is_available is not None:
            result['IsAvailable'] = self.is_available
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayClass') is not None:
            self.gateway_class = m.get('GatewayClass')
        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')
        return self


class DescribeGatewayModificationClassesResponseBodyTargetGatewayClasses(TeaModel):
    def __init__(
        self,
        target_gateway_class: List[DescribeGatewayModificationClassesResponseBodyTargetGatewayClassesTargetGatewayClass] = None,
    ):
        self.target_gateway_class = target_gateway_class

    def validate(self):
        if self.target_gateway_class:
            for k in self.target_gateway_class:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TargetGatewayClass'] = []
        if self.target_gateway_class is not None:
            for k in self.target_gateway_class:
                result['TargetGatewayClass'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target_gateway_class = []
        if m.get('TargetGatewayClass') is not None:
            for k in m.get('TargetGatewayClass'):
                temp_model = DescribeGatewayModificationClassesResponseBodyTargetGatewayClassesTargetGatewayClass()
                self.target_gateway_class.append(temp_model.from_map(k))
        return self


class DescribeGatewayModificationClassesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        target_gateway_classes: DescribeGatewayModificationClassesResponseBodyTargetGatewayClasses = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.target_gateway_classes = target_gateway_classes

    def validate(self):
        if self.target_gateway_classes:
            self.target_gateway_classes.validate()

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
        if self.target_gateway_classes is not None:
            result['TargetGatewayClasses'] = self.target_gateway_classes.to_map()
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
        if m.get('TargetGatewayClasses') is not None:
            temp_model = DescribeGatewayModificationClassesResponseBodyTargetGatewayClasses()
            self.target_gateway_classes = temp_model.from_map(m['TargetGatewayClasses'])
        return self


class DescribeGatewayModificationClassesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayModificationClassesResponseBody = None,
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
            temp_model = DescribeGatewayModificationClassesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayNFSClientsRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayNFSClientsResponseBodyClientInfoListClientInfo(TeaModel):
    def __init__(
        self,
        client_ip_addr: str = None,
        has_nfsv_3: bool = None,
        has_nfsv_40: bool = None,
        has_nfsv_41: bool = None,
    ):
        self.client_ip_addr = client_ip_addr
        self.has_nfsv_3 = has_nfsv_3
        self.has_nfsv_40 = has_nfsv_40
        self.has_nfsv_41 = has_nfsv_41

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip_addr is not None:
            result['ClientIpAddr'] = self.client_ip_addr
        if self.has_nfsv_3 is not None:
            result['HasNFSv3'] = self.has_nfsv_3
        if self.has_nfsv_40 is not None:
            result['HasNFSv40'] = self.has_nfsv_40
        if self.has_nfsv_41 is not None:
            result['HasNFSv41'] = self.has_nfsv_41
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIpAddr') is not None:
            self.client_ip_addr = m.get('ClientIpAddr')
        if m.get('HasNFSv3') is not None:
            self.has_nfsv_3 = m.get('HasNFSv3')
        if m.get('HasNFSv40') is not None:
            self.has_nfsv_40 = m.get('HasNFSv40')
        if m.get('HasNFSv41') is not None:
            self.has_nfsv_41 = m.get('HasNFSv41')
        return self


class DescribeGatewayNFSClientsResponseBodyClientInfoList(TeaModel):
    def __init__(
        self,
        client_info: List[DescribeGatewayNFSClientsResponseBodyClientInfoListClientInfo] = None,
    ):
        self.client_info = client_info

    def validate(self):
        if self.client_info:
            for k in self.client_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientInfo'] = []
        if self.client_info is not None:
            for k in self.client_info:
                result['ClientInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_info = []
        if m.get('ClientInfo') is not None:
            for k in m.get('ClientInfo'):
                temp_model = DescribeGatewayNFSClientsResponseBodyClientInfoListClientInfo()
                self.client_info.append(temp_model.from_map(k))
        return self


class DescribeGatewayNFSClientsResponseBody(TeaModel):
    def __init__(
        self,
        client_info_list: DescribeGatewayNFSClientsResponseBodyClientInfoList = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        version_3enabled: bool = None,
        version_40enabled: bool = None,
        version_41enabled: bool = None,
    ):
        self.client_info_list = client_info_list
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.version_3enabled = version_3enabled
        self.version_40enabled = version_40enabled
        self.version_41enabled = version_41enabled

    def validate(self):
        if self.client_info_list:
            self.client_info_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_info_list is not None:
            result['ClientInfoList'] = self.client_info_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
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
        if self.version_3enabled is not None:
            result['Version3Enabled'] = self.version_3enabled
        if self.version_40enabled is not None:
            result['Version40Enabled'] = self.version_40enabled
        if self.version_41enabled is not None:
            result['Version41Enabled'] = self.version_41enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfoList') is not None:
            temp_model = DescribeGatewayNFSClientsResponseBodyClientInfoList()
            self.client_info_list = temp_model.from_map(m['ClientInfoList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        if m.get('Version3Enabled') is not None:
            self.version_3enabled = m.get('Version3Enabled')
        if m.get('Version40Enabled') is not None:
            self.version_40enabled = m.get('Version40Enabled')
        if m.get('Version41Enabled') is not None:
            self.version_41enabled = m.get('Version41Enabled')
        return self


class DescribeGatewayNFSClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayNFSClientsResponseBody = None,
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
            temp_model = DescribeGatewayNFSClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewaySMBUsersRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewaySMBUsersResponseBodyUsersUser(TeaModel):
    def __init__(
        self,
        username: str = None,
    ):
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeGatewaySMBUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user: List[DescribeGatewaySMBUsersResponseBodyUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = DescribeGatewaySMBUsersResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class DescribeGatewaySMBUsersResponseBody(TeaModel):
    def __init__(
        self,
        active_directory: bool = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        users: DescribeGatewaySMBUsersResponseBodyUsers = None,
    ):
        self.active_directory = active_directory
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_directory is not None:
            result['ActiveDirectory'] = self.active_directory
        if self.code is not None:
            result['Code'] = self.code
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
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveDirectory') is not None:
            self.active_directory = m.get('ActiveDirectory')
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        if m.get('Users') is not None:
            temp_model = DescribeGatewaySMBUsersResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class DescribeGatewaySMBUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewaySMBUsersResponseBody = None,
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
            temp_model = DescribeGatewaySMBUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayStatisticsRequest(TeaModel):
    def __init__(
        self,
        end_timestamp: int = None,
        gateway_category: str = None,
        gateway_location: str = None,
        security_token: str = None,
        start_timestamp: int = None,
        target_account_id: str = None,
    ):
        self.end_timestamp = end_timestamp
        self.gateway_category = gateway_category
        self.gateway_location = gateway_location
        self.security_token = security_token
        self.start_timestamp = start_timestamp
        self.target_account_id = target_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.gateway_category is not None:
            result['GatewayCategory'] = self.gateway_category
        if self.gateway_location is not None:
            result['GatewayLocation'] = self.gateway_location
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.target_account_id is not None:
            result['TargetAccountId'] = self.target_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('GatewayCategory') is not None:
            self.gateway_category = m.get('GatewayCategory')
        if m.get('GatewayLocation') is not None:
            self.gateway_location = m.get('GatewayLocation')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('TargetAccountId') is not None:
            self.target_account_id = m.get('TargetAccountId')
        return self


class DescribeGatewayStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
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
        if self.result is not None:
            result['Result'] = self.result
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
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayStatisticsResponseBody = None,
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
            temp_model = DescribeGatewayStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayStockRequest(TeaModel):
    def __init__(
        self,
        gateway_region_id: str = None,
        security_token: str = None,
    ):
        self.gateway_region_id = gateway_region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_region_id is not None:
            result['GatewayRegionId'] = self.gateway_region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayRegionId') is not None:
            self.gateway_region_id = m.get('GatewayRegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayStockResponseBodyStocksStock(TeaModel):
    def __init__(
        self,
        stock_info: str = None,
        zone_id: str = None,
    ):
        self.stock_info = stock_info
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stock_info is not None:
            result['StockInfo'] = self.stock_info
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StockInfo') is not None:
            self.stock_info = m.get('StockInfo')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeGatewayStockResponseBodyStocks(TeaModel):
    def __init__(
        self,
        stock: List[DescribeGatewayStockResponseBodyStocksStock] = None,
    ):
        self.stock = stock

    def validate(self):
        if self.stock:
            for k in self.stock:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Stock'] = []
        if self.stock is not None:
            for k in self.stock:
                result['Stock'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stock = []
        if m.get('Stock') is not None:
            for k in m.get('Stock'):
                temp_model = DescribeGatewayStockResponseBodyStocksStock()
                self.stock.append(temp_model.from_map(k))
        return self


class DescribeGatewayStockResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        stocks: DescribeGatewayStockResponseBodyStocks = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.stocks = stocks
        self.success = success

    def validate(self):
        if self.stocks:
            self.stocks.validate()

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
        if self.stocks is not None:
            result['Stocks'] = self.stocks.to_map()
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
        if m.get('Stocks') is not None:
            temp_model = DescribeGatewayStockResponseBodyStocks()
            self.stocks = temp_model.from_map(m['Stocks'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewayStockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayStockResponseBody = None,
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
            temp_model = DescribeGatewayStockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayTypesRequest(TeaModel):
    def __init__(
        self,
        gateway_location: str = None,
        security_token: str = None,
    ):
        self.gateway_location = gateway_location
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_location is not None:
            result['GatewayLocation'] = self.gateway_location
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayLocation') is not None:
            self.gateway_location = m.get('GatewayLocation')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewayTypesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        types: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.types = types

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
        if self.types is not None:
            result['Types'] = self.types
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
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class DescribeGatewayTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayTypesResponseBody = None,
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
            temp_model = DescribeGatewayTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewaysRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        storage_bundle_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.storage_bundle_id = storage_bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        return self


class DescribeGatewaysResponseBodyGatewaysGatewayElasticNodes(TeaModel):
    def __init__(
        self,
        elastic_node: List[str] = None,
    ):
        self.elastic_node = elastic_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_node is not None:
            result['ElasticNode'] = self.elastic_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNode') is not None:
            self.elastic_node = m.get('ElasticNode')
        return self


class DescribeGatewaysResponseBodyGatewaysGateway(TeaModel):
    def __init__(
        self,
        activated_time: int = None,
        buy_url: str = None,
        capacity: int = None,
        category: str = None,
        common_buy_instance_id: str = None,
        created_time: int = None,
        data_load_interval: int = None,
        data_load_type: str = None,
        description: str = None,
        ecs_instance_id: str = None,
        elastic_gateway: bool = None,
        elastic_nodes: DescribeGatewaysResponseBodyGatewaysGatewayElasticNodes = None,
        expire_status: int = None,
        expired_time: int = None,
        gateway_class: str = None,
        gateway_id: str = None,
        gateway_region_id: str = None,
        gateway_type: str = None,
        gateway_version: str = None,
        high_availability: bool = None,
        inner_ip: str = None,
        inner_ipv_6ip: str = None,
        ip: str = None,
        is_post_paid: bool = None,
        is_release_after_expiration: bool = None,
        last_error_key: str = None,
        location: str = None,
        max_throughput: int = None,
        name: str = None,
        public_network_bandwidth: int = None,
        renew_url: str = None,
        status: str = None,
        storage_bundle_id: str = None,
        task_id: str = None,
        type: str = None,
        untrusted_env_instance_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.activated_time = activated_time
        self.buy_url = buy_url
        self.capacity = capacity
        self.category = category
        self.common_buy_instance_id = common_buy_instance_id
        self.created_time = created_time
        self.data_load_interval = data_load_interval
        self.data_load_type = data_load_type
        self.description = description
        self.ecs_instance_id = ecs_instance_id
        self.elastic_gateway = elastic_gateway
        self.elastic_nodes = elastic_nodes
        self.expire_status = expire_status
        self.expired_time = expired_time
        self.gateway_class = gateway_class
        self.gateway_id = gateway_id
        self.gateway_region_id = gateway_region_id
        self.gateway_type = gateway_type
        self.gateway_version = gateway_version
        self.high_availability = high_availability
        self.inner_ip = inner_ip
        self.inner_ipv_6ip = inner_ipv_6ip
        self.ip = ip
        self.is_post_paid = is_post_paid
        self.is_release_after_expiration = is_release_after_expiration
        self.last_error_key = last_error_key
        self.location = location
        self.max_throughput = max_throughput
        self.name = name
        self.public_network_bandwidth = public_network_bandwidth
        self.renew_url = renew_url
        self.status = status
        self.storage_bundle_id = storage_bundle_id
        self.task_id = task_id
        self.type = type
        self.untrusted_env_instance_type = untrusted_env_instance_type
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        if self.elastic_nodes:
            self.elastic_nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activated_time is not None:
            result['ActivatedTime'] = self.activated_time
        if self.buy_url is not None:
            result['BuyURL'] = self.buy_url
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.category is not None:
            result['Category'] = self.category
        if self.common_buy_instance_id is not None:
            result['CommonBuyInstanceId'] = self.common_buy_instance_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_load_interval is not None:
            result['DataLoadInterval'] = self.data_load_interval
        if self.data_load_type is not None:
            result['DataLoadType'] = self.data_load_type
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.elastic_gateway is not None:
            result['ElasticGateway'] = self.elastic_gateway
        if self.elastic_nodes is not None:
            result['ElasticNodes'] = self.elastic_nodes.to_map()
        if self.expire_status is not None:
            result['ExpireStatus'] = self.expire_status
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gateway_class is not None:
            result['GatewayClass'] = self.gateway_class
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_region_id is not None:
            result['GatewayRegionId'] = self.gateway_region_id
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.gateway_version is not None:
            result['GatewayVersion'] = self.gateway_version
        if self.high_availability is not None:
            result['HighAvailability'] = self.high_availability
        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip
        if self.inner_ipv_6ip is not None:
            result['InnerIpv6Ip'] = self.inner_ipv_6ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.is_post_paid is not None:
            result['IsPostPaid'] = self.is_post_paid
        if self.is_release_after_expiration is not None:
            result['IsReleaseAfterExpiration'] = self.is_release_after_expiration
        if self.last_error_key is not None:
            result['LastErrorKey'] = self.last_error_key
        if self.location is not None:
            result['Location'] = self.location
        if self.max_throughput is not None:
            result['MaxThroughput'] = self.max_throughput
        if self.name is not None:
            result['Name'] = self.name
        if self.public_network_bandwidth is not None:
            result['PublicNetworkBandwidth'] = self.public_network_bandwidth
        if self.renew_url is not None:
            result['RenewURL'] = self.renew_url
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        if self.untrusted_env_instance_type is not None:
            result['UntrustedEnvInstanceType'] = self.untrusted_env_instance_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivatedTime') is not None:
            self.activated_time = m.get('ActivatedTime')
        if m.get('BuyURL') is not None:
            self.buy_url = m.get('BuyURL')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CommonBuyInstanceId') is not None:
            self.common_buy_instance_id = m.get('CommonBuyInstanceId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataLoadInterval') is not None:
            self.data_load_interval = m.get('DataLoadInterval')
        if m.get('DataLoadType') is not None:
            self.data_load_type = m.get('DataLoadType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('ElasticGateway') is not None:
            self.elastic_gateway = m.get('ElasticGateway')
        if m.get('ElasticNodes') is not None:
            temp_model = DescribeGatewaysResponseBodyGatewaysGatewayElasticNodes()
            self.elastic_nodes = temp_model.from_map(m['ElasticNodes'])
        if m.get('ExpireStatus') is not None:
            self.expire_status = m.get('ExpireStatus')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GatewayClass') is not None:
            self.gateway_class = m.get('GatewayClass')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayRegionId') is not None:
            self.gateway_region_id = m.get('GatewayRegionId')
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')
        if m.get('GatewayVersion') is not None:
            self.gateway_version = m.get('GatewayVersion')
        if m.get('HighAvailability') is not None:
            self.high_availability = m.get('HighAvailability')
        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')
        if m.get('InnerIpv6Ip') is not None:
            self.inner_ipv_6ip = m.get('InnerIpv6Ip')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IsPostPaid') is not None:
            self.is_post_paid = m.get('IsPostPaid')
        if m.get('IsReleaseAfterExpiration') is not None:
            self.is_release_after_expiration = m.get('IsReleaseAfterExpiration')
        if m.get('LastErrorKey') is not None:
            self.last_error_key = m.get('LastErrorKey')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxThroughput') is not None:
            self.max_throughput = m.get('MaxThroughput')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PublicNetworkBandwidth') is not None:
            self.public_network_bandwidth = m.get('PublicNetworkBandwidth')
        if m.get('RenewURL') is not None:
            self.renew_url = m.get('RenewURL')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UntrustedEnvInstanceType') is not None:
            self.untrusted_env_instance_type = m.get('UntrustedEnvInstanceType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeGatewaysResponseBodyGateways(TeaModel):
    def __init__(
        self,
        gateway: List[DescribeGatewaysResponseBodyGatewaysGateway] = None,
    ):
        self.gateway = gateway

    def validate(self):
        if self.gateway:
            for k in self.gateway:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Gateway'] = []
        if self.gateway is not None:
            for k in self.gateway:
                result['Gateway'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway = []
        if m.get('Gateway') is not None:
            for k in m.get('Gateway'):
                temp_model = DescribeGatewaysResponseBodyGatewaysGateway()
                self.gateway.append(temp_model.from_map(k))
        return self


class DescribeGatewaysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gateways: DescribeGatewaysResponseBodyGateways = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.gateways = gateways
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.gateways:
            self.gateways.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.gateways is not None:
            result['Gateways'] = self.gateways.to_map()
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
        if m.get('Gateways') is not None:
            temp_model = DescribeGatewaysResponseBodyGateways()
            self.gateways = temp_model.from_map(m['Gateways'])
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


class DescribeGatewaysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewaysResponseBody = None,
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
            temp_model = DescribeGatewaysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewaysForCmsRequest(TeaModel):
    def __init__(
        self,
        gateway_region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.gateway_region_id = gateway_region_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_region_id is not None:
            result['GatewayRegionId'] = self.gateway_region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayRegionId') is not None:
            self.gateway_region_id = m.get('GatewayRegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGatewaysForCmsResponseBodyGatewaysGateway(TeaModel):
    def __init__(
        self,
        description: str = None,
        gateway_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.gateway_id = gateway_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeGatewaysForCmsResponseBodyGateways(TeaModel):
    def __init__(
        self,
        gateway: List[DescribeGatewaysForCmsResponseBodyGatewaysGateway] = None,
    ):
        self.gateway = gateway

    def validate(self):
        if self.gateway:
            for k in self.gateway:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Gateway'] = []
        if self.gateway is not None:
            for k in self.gateway:
                result['Gateway'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway = []
        if m.get('Gateway') is not None:
            for k in m.get('Gateway'):
                temp_model = DescribeGatewaysForCmsResponseBodyGatewaysGateway()
                self.gateway.append(temp_model.from_map(k))
        return self


class DescribeGatewaysForCmsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gateways: DescribeGatewaysForCmsResponseBodyGateways = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.gateways = gateways
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.gateways:
            self.gateways.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.gateways is not None:
            result['Gateways'] = self.gateways.to_map()
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
        if m.get('Gateways') is not None:
            temp_model = DescribeGatewaysForCmsResponseBodyGateways()
            self.gateways = temp_model.from_map(m['Gateways'])
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


class DescribeGatewaysForCmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewaysForCmsResponseBody = None,
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
            temp_model = DescribeGatewaysForCmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewaysTagsRequest(TeaModel):
    def __init__(
        self,
        gateway_ids: str = None,
        security_token: str = None,
        storage_bundle_id: str = None,
        tag_category: str = None,
    ):
        self.gateway_ids = gateway_ids
        self.security_token = security_token
        self.storage_bundle_id = storage_bundle_id
        self.tag_category = tag_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_ids is not None:
            result['GatewayIds'] = self.gateway_ids
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        if self.tag_category is not None:
            result['TagCategory'] = self.tag_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayIds') is not None:
            self.gateway_ids = m.get('GatewayIds')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        if m.get('TagCategory') is not None:
            self.tag_category = m.get('TagCategory')
        return self


class DescribeGatewaysTagsResponseBodyGatewayTagsGatewayTagTagsTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeGatewaysTagsResponseBodyGatewayTagsGatewayTagTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeGatewaysTagsResponseBodyGatewayTagsGatewayTagTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeGatewaysTagsResponseBodyGatewayTagsGatewayTagTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeGatewaysTagsResponseBodyGatewayTagsGatewayTag(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        tags: DescribeGatewaysTagsResponseBodyGatewayTagsGatewayTagTags = None,
    ):
        self.gateway_id = gateway_id
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Tags') is not None:
            temp_model = DescribeGatewaysTagsResponseBodyGatewayTagsGatewayTagTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeGatewaysTagsResponseBodyGatewayTags(TeaModel):
    def __init__(
        self,
        gateway_tag: List[DescribeGatewaysTagsResponseBodyGatewayTagsGatewayTag] = None,
    ):
        self.gateway_tag = gateway_tag

    def validate(self):
        if self.gateway_tag:
            for k in self.gateway_tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GatewayTag'] = []
        if self.gateway_tag is not None:
            for k in self.gateway_tag:
                result['GatewayTag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway_tag = []
        if m.get('GatewayTag') is not None:
            for k in m.get('GatewayTag'):
                temp_model = DescribeGatewaysTagsResponseBodyGatewayTagsGatewayTag()
                self.gateway_tag.append(temp_model.from_map(k))
        return self


class DescribeGatewaysTagsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gateway_tags: DescribeGatewaysTagsResponseBodyGatewayTags = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.gateway_tags = gateway_tags
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.gateway_tags:
            self.gateway_tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.gateway_tags is not None:
            result['GatewayTags'] = self.gateway_tags.to_map()
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
        if m.get('GatewayTags') is not None:
            temp_model = DescribeGatewaysTagsResponseBodyGatewayTags()
            self.gateway_tags = temp_model.from_map(m['GatewayTags'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGatewaysTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewaysTagsResponseBody = None,
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
            temp_model = DescribeGatewaysTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKmsKeyRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        kms_key: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.kms_key = kms_key
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.kms_key is not None:
            result['KmsKey'] = self.kms_key
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('KmsKey') is not None:
            self.kms_key = m.get('KmsKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeKmsKeyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_valid: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.is_valid = is_valid
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
        if self.is_valid is not None:
            result['IsValid'] = self.is_valid
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
        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeKmsKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeKmsKeyResponseBody = None,
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
            temp_model = DescribeKmsKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMqttConfigRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeMqttConfigResponseBody(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        broker_url: str = None,
        code: str = None,
        group_id: str = None,
        internal_broker_url: str = None,
        is_enabled: bool = None,
        message: str = None,
        mqtt_instance_id: str = None,
        password: str = None,
        publish_topic: str = None,
        request_id: str = None,
        subscribe_topic: str = None,
        success: bool = None,
        username: str = None,
    ):
        self.auth_type = auth_type
        self.broker_url = broker_url
        self.code = code
        self.group_id = group_id
        self.internal_broker_url = internal_broker_url
        self.is_enabled = is_enabled
        self.message = message
        self.mqtt_instance_id = mqtt_instance_id
        self.password = password
        self.publish_topic = publish_topic
        self.request_id = request_id
        self.subscribe_topic = subscribe_topic
        self.success = success
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.code is not None:
            result['Code'] = self.code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.internal_broker_url is not None:
            result['InternalBrokerUrl'] = self.internal_broker_url
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.message is not None:
            result['Message'] = self.message
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.publish_topic is not None:
            result['PublishTopic'] = self.publish_topic
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscribe_topic is not None:
            result['SubscribeTopic'] = self.subscribe_topic
        if self.success is not None:
            result['Success'] = self.success
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InternalBrokerUrl') is not None:
            self.internal_broker_url = m.get('InternalBrokerUrl')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PublishTopic') is not None:
            self.publish_topic = m.get('PublishTopic')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscribeTopic') is not None:
            self.subscribe_topic = m.get('SubscribeTopic')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeMqttConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMqttConfigResponseBody = None,
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
            temp_model = DescribeMqttConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssBucketInfoRequest(TeaModel):
    def __init__(
        self,
        bucket_endpoint: str = None,
        bucket_name: str = None,
        gateway_id: str = None,
        security_token: str = None,
        type: str = None,
    ):
        self.bucket_endpoint = bucket_endpoint
        self.bucket_name = bucket_name
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_endpoint is not None:
            result['BucketEndpoint'] = self.bucket_endpoint
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketEndpoint') is not None:
            self.bucket_endpoint = m.get('BucketEndpoint')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeOssBucketInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_archive: bool = None,
        is_back_to_resource: bool = None,
        is_cold_archive: bool = None,
        is_fresh: bool = None,
        is_support_server_side_encryption: bool = None,
        is_versioning: bool = None,
        message: str = None,
        polling_interval: int = None,
        request_id: str = None,
        storage_size: int = None,
        success: bool = None,
    ):
        self.code = code
        self.is_archive = is_archive
        self.is_back_to_resource = is_back_to_resource
        self.is_cold_archive = is_cold_archive
        self.is_fresh = is_fresh
        self.is_support_server_side_encryption = is_support_server_side_encryption
        self.is_versioning = is_versioning
        self.message = message
        self.polling_interval = polling_interval
        self.request_id = request_id
        self.storage_size = storage_size
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
        if self.is_archive is not None:
            result['IsArchive'] = self.is_archive
        if self.is_back_to_resource is not None:
            result['IsBackToResource'] = self.is_back_to_resource
        if self.is_cold_archive is not None:
            result['IsColdArchive'] = self.is_cold_archive
        if self.is_fresh is not None:
            result['IsFresh'] = self.is_fresh
        if self.is_support_server_side_encryption is not None:
            result['IsSupportServerSideEncryption'] = self.is_support_server_side_encryption
        if self.is_versioning is not None:
            result['IsVersioning'] = self.is_versioning
        if self.message is not None:
            result['Message'] = self.message
        if self.polling_interval is not None:
            result['PollingInterval'] = self.polling_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsArchive') is not None:
            self.is_archive = m.get('IsArchive')
        if m.get('IsBackToResource') is not None:
            self.is_back_to_resource = m.get('IsBackToResource')
        if m.get('IsColdArchive') is not None:
            self.is_cold_archive = m.get('IsColdArchive')
        if m.get('IsFresh') is not None:
            self.is_fresh = m.get('IsFresh')
        if m.get('IsSupportServerSideEncryption') is not None:
            self.is_support_server_side_encryption = m.get('IsSupportServerSideEncryption')
        if m.get('IsVersioning') is not None:
            self.is_versioning = m.get('IsVersioning')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PollingInterval') is not None:
            self.polling_interval = m.get('PollingInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeOssBucketInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssBucketInfoResponseBody = None,
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
            temp_model = DescribeOssBucketInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssBucketsRequest(TeaModel):
    def __init__(
        self,
        bucket_endpoint: str = None,
        security_token: str = None,
    ):
        self.bucket_endpoint = bucket_endpoint
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_endpoint is not None:
            result['BucketEndpoint'] = self.bucket_endpoint
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketEndpoint') is not None:
            self.bucket_endpoint = m.get('BucketEndpoint')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeOssBucketsResponseBodyBucketsBucket(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeOssBucketsResponseBodyBuckets(TeaModel):
    def __init__(
        self,
        bucket: List[DescribeOssBucketsResponseBodyBucketsBucket] = None,
    ):
        self.bucket = bucket

    def validate(self):
        if self.bucket:
            for k in self.bucket:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bucket'] = []
        if self.bucket is not None:
            for k in self.bucket:
                result['Bucket'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bucket = []
        if m.get('Bucket') is not None:
            for k in m.get('Bucket'):
                temp_model = DescribeOssBucketsResponseBodyBucketsBucket()
                self.bucket.append(temp_model.from_map(k))
        return self


class DescribeOssBucketsResponseBody(TeaModel):
    def __init__(
        self,
        buckets: DescribeOssBucketsResponseBodyBuckets = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.buckets = buckets
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.buckets:
            self.buckets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buckets is not None:
            result['Buckets'] = self.buckets.to_map()
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
        if m.get('Buckets') is not None:
            temp_model = DescribeOssBucketsResponseBodyBuckets()
            self.buckets = temp_model.from_map(m['Buckets'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeOssBucketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssBucketsResponseBody = None,
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
            temp_model = DescribeOssBucketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePayAsYouGoPriceRequest(TeaModel):
    def __init__(
        self,
        gateway_class: str = None,
        region_id: str = None,
        security_token: str = None,
    ):
        self.gateway_class = gateway_class
        self.region_id = region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_class is not None:
            result['GatewayClass'] = self.gateway_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayClass') is not None:
            self.gateway_class = m.get('GatewayClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribePayAsYouGoPriceResponseBody(TeaModel):
    def __init__(
        self,
        cache_cloud_efficiency_size_price: float = None,
        cache_cloud_ssdsize_price: float = None,
        cache_essdpl_1size_price: float = None,
        code: str = None,
        currency: str = None,
        gateway_class_price: float = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.cache_cloud_efficiency_size_price = cache_cloud_efficiency_size_price
        self.cache_cloud_ssdsize_price = cache_cloud_ssdsize_price
        self.cache_essdpl_1size_price = cache_essdpl_1size_price
        self.code = code
        self.currency = currency
        self.gateway_class_price = gateway_class_price
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
        if self.cache_cloud_efficiency_size_price is not None:
            result['CacheCloudEfficiencySizePrice'] = self.cache_cloud_efficiency_size_price
        if self.cache_cloud_ssdsize_price is not None:
            result['CacheCloudSSDSizePrice'] = self.cache_cloud_ssdsize_price
        if self.cache_essdpl_1size_price is not None:
            result['CacheESSDPl1SizePrice'] = self.cache_essdpl_1size_price
        if self.code is not None:
            result['Code'] = self.code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.gateway_class_price is not None:
            result['GatewayClassPrice'] = self.gateway_class_price
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheCloudEfficiencySizePrice') is not None:
            self.cache_cloud_efficiency_size_price = m.get('CacheCloudEfficiencySizePrice')
        if m.get('CacheCloudSSDSizePrice') is not None:
            self.cache_cloud_ssdsize_price = m.get('CacheCloudSSDSizePrice')
        if m.get('CacheESSDPl1SizePrice') is not None:
            self.cache_essdpl_1size_price = m.get('CacheESSDPl1SizePrice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('GatewayClassPrice') is not None:
            self.gateway_class_price = m.get('GatewayClassPrice')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribePayAsYouGoPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePayAsYouGoPriceResponseBody = None,
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
            temp_model = DescribePayAsYouGoPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
    ):
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.regions = regions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
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
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSharesBucketInfoForExpressSyncRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_region: str = None,
        security_token: str = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_region = bucket_region
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_region is not None:
            result['BucketRegion'] = self.bucket_region
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketRegion') is not None:
            self.bucket_region = m.get('BucketRegion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSharesBucketInfoForExpressSyncResponseBodyBucketInfosBucketInfo(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_prefix: str = None,
        bucket_region: str = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_prefix = bucket_prefix
        self.bucket_region = bucket_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_prefix is not None:
            result['BucketPrefix'] = self.bucket_prefix
        if self.bucket_region is not None:
            result['BucketRegion'] = self.bucket_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketPrefix') is not None:
            self.bucket_prefix = m.get('BucketPrefix')
        if m.get('BucketRegion') is not None:
            self.bucket_region = m.get('BucketRegion')
        return self


class DescribeSharesBucketInfoForExpressSyncResponseBodyBucketInfos(TeaModel):
    def __init__(
        self,
        bucket_info: List[DescribeSharesBucketInfoForExpressSyncResponseBodyBucketInfosBucketInfo] = None,
    ):
        self.bucket_info = bucket_info

    def validate(self):
        if self.bucket_info:
            for k in self.bucket_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BucketInfo'] = []
        if self.bucket_info is not None:
            for k in self.bucket_info:
                result['BucketInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bucket_info = []
        if m.get('BucketInfo') is not None:
            for k in m.get('BucketInfo'):
                temp_model = DescribeSharesBucketInfoForExpressSyncResponseBodyBucketInfosBucketInfo()
                self.bucket_info.append(temp_model.from_map(k))
        return self


class DescribeSharesBucketInfoForExpressSyncResponseBody(TeaModel):
    def __init__(
        self,
        bucket_infos: DescribeSharesBucketInfoForExpressSyncResponseBodyBucketInfos = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.bucket_infos = bucket_infos
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.bucket_infos:
            self.bucket_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_infos is not None:
            result['BucketInfos'] = self.bucket_infos.to_map()
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
        if m.get('BucketInfos') is not None:
            temp_model = DescribeSharesBucketInfoForExpressSyncResponseBodyBucketInfos()
            self.bucket_infos = temp_model.from_map(m['BucketInfos'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSharesBucketInfoForExpressSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSharesBucketInfoForExpressSyncResponseBody = None,
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
            temp_model = DescribeSharesBucketInfoForExpressSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStorageBundleRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        storage_bundle_id: str = None,
    ):
        self.security_token = security_token
        self.storage_bundle_id = storage_bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        return self


class DescribeStorageBundleResponseBody(TeaModel):
    def __init__(
        self,
        backend_bucket_region_id: str = None,
        code: str = None,
        created_time: int = None,
        description: str = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        storage_bundle_id: str = None,
        success: bool = None,
    ):
        self.backend_bucket_region_id = backend_bucket_region_id
        self.code = code
        self.created_time = created_time
        self.description = description
        self.message = message
        self.name = name
        self.request_id = request_id
        self.storage_bundle_id = storage_bundle_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_bucket_region_id is not None:
            result['BackendBucketRegionId'] = self.backend_bucket_region_id
        if self.code is not None:
            result['Code'] = self.code
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendBucketRegionId') is not None:
            self.backend_bucket_region_id = m.get('BackendBucketRegionId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeStorageBundleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStorageBundleResponseBody = None,
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
            temp_model = DescribeStorageBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStorageBundlesRequest(TeaModel):
    def __init__(
        self,
        backend_bucket_region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.backend_bucket_region_id = backend_bucket_region_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_bucket_region_id is not None:
            result['BackendBucketRegionId'] = self.backend_bucket_region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendBucketRegionId') is not None:
            self.backend_bucket_region_id = m.get('BackendBucketRegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeStorageBundlesResponseBodyStorageBundlesStorageBundle(TeaModel):
    def __init__(
        self,
        backend_bucket_region_id: str = None,
        created_time: int = None,
        description: str = None,
        name: str = None,
        storage_bundle_id: str = None,
    ):
        self.backend_bucket_region_id = backend_bucket_region_id
        self.created_time = created_time
        self.description = description
        self.name = name
        self.storage_bundle_id = storage_bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_bucket_region_id is not None:
            result['BackendBucketRegionId'] = self.backend_bucket_region_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendBucketRegionId') is not None:
            self.backend_bucket_region_id = m.get('BackendBucketRegionId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        return self


class DescribeStorageBundlesResponseBodyStorageBundles(TeaModel):
    def __init__(
        self,
        storage_bundle: List[DescribeStorageBundlesResponseBodyStorageBundlesStorageBundle] = None,
    ):
        self.storage_bundle = storage_bundle

    def validate(self):
        if self.storage_bundle:
            for k in self.storage_bundle:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StorageBundle'] = []
        if self.storage_bundle is not None:
            for k in self.storage_bundle:
                result['StorageBundle'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.storage_bundle = []
        if m.get('StorageBundle') is not None:
            for k in m.get('StorageBundle'):
                temp_model = DescribeStorageBundlesResponseBodyStorageBundlesStorageBundle()
                self.storage_bundle.append(temp_model.from_map(k))
        return self


class DescribeStorageBundlesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        storage_bundles: DescribeStorageBundlesResponseBodyStorageBundles = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.storage_bundles = storage_bundles
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.storage_bundles:
            self.storage_bundles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_bundles is not None:
            result['StorageBundles'] = self.storage_bundles.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageBundles') is not None:
            temp_model = DescribeStorageBundlesResponseBodyStorageBundles()
            self.storage_bundles = temp_model.from_map(m['StorageBundles'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeStorageBundlesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStorageBundlesResponseBody = None,
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
            temp_model = DescribeStorageBundlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionPriceRequest(TeaModel):
    def __init__(
        self,
        cache_cloud_efficiency_size: int = None,
        cache_essdpl_1size: int = None,
        cache_ssdsize: int = None,
        gateway_class: str = None,
        period_quantity: int = None,
        period_unit: str = None,
        region_id: str = None,
        security_token: str = None,
    ):
        self.cache_cloud_efficiency_size = cache_cloud_efficiency_size
        self.cache_essdpl_1size = cache_essdpl_1size
        self.cache_ssdsize = cache_ssdsize
        self.gateway_class = gateway_class
        self.period_quantity = period_quantity
        self.period_unit = period_unit
        self.region_id = region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_cloud_efficiency_size is not None:
            result['CacheCloudEfficiencySize'] = self.cache_cloud_efficiency_size
        if self.cache_essdpl_1size is not None:
            result['CacheESSDPl1Size'] = self.cache_essdpl_1size
        if self.cache_ssdsize is not None:
            result['CacheSSDSize'] = self.cache_ssdsize
        if self.gateway_class is not None:
            result['GatewayClass'] = self.gateway_class
        if self.period_quantity is not None:
            result['PeriodQuantity'] = self.period_quantity
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheCloudEfficiencySize') is not None:
            self.cache_cloud_efficiency_size = m.get('CacheCloudEfficiencySize')
        if m.get('CacheESSDPl1Size') is not None:
            self.cache_essdpl_1size = m.get('CacheESSDPl1Size')
        if m.get('CacheSSDSize') is not None:
            self.cache_ssdsize = m.get('CacheSSDSize')
        if m.get('GatewayClass') is not None:
            self.gateway_class = m.get('GatewayClass')
        if m.get('PeriodQuantity') is not None:
            self.period_quantity = m.get('PeriodQuantity')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSubscriptionPriceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        currency: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trade_price: float = None,
    ):
        self.code = code
        self.currency = currency
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribeSubscriptionPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSubscriptionPriceResponseBody = None,
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
            temp_model = DescribeSubscriptionPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        target_id: str = None,
        task_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.target_id = target_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTasksResponseBodyTasksSimpleTask(TeaModel):
    def __init__(
        self,
        created_time: int = None,
        message_key: str = None,
        name: str = None,
        progress: int = None,
        related_resource_id: str = None,
        state_code: str = None,
        task_id: str = None,
        updated_time: int = None,
    ):
        self.created_time = created_time
        self.message_key = message_key
        self.name = name
        self.progress = progress
        self.related_resource_id = related_resource_id
        self.state_code = state_code
        self.task_id = task_id
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.message_key is not None:
            result['MessageKey'] = self.message_key
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.related_resource_id is not None:
            result['RelatedResourceId'] = self.related_resource_id
        if self.state_code is not None:
            result['StateCode'] = self.state_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('MessageKey') is not None:
            self.message_key = m.get('MessageKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RelatedResourceId') is not None:
            self.related_resource_id = m.get('RelatedResourceId')
        if m.get('StateCode') is not None:
            self.state_code = m.get('StateCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribeTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        simple_task: List[DescribeTasksResponseBodyTasksSimpleTask] = None,
    ):
        self.simple_task = simple_task

    def validate(self):
        if self.simple_task:
            for k in self.simple_task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SimpleTask'] = []
        if self.simple_task is not None:
            for k in self.simple_task:
                result['SimpleTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.simple_task = []
        if m.get('SimpleTask') is not None:
            for k in m.get('SimpleTask'):
                temp_model = DescribeTasksResponseBodyTasksSimpleTask()
                self.simple_task.append(temp_model.from_map(k))
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        tasks: DescribeTasksResponseBodyTasks = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        if m.get('Tasks') is not None:
            temp_model = DescribeTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTasksResponseBody = None,
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
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBusinessStatusRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
    ):
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUserBusinessStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_enabled: bool = None,
        is_indebted: bool = None,
        is_indebted_overdue: bool = None,
        is_risk_control: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.is_enabled = is_enabled
        self.is_indebted = is_indebted
        self.is_indebted_overdue = is_indebted_overdue
        self.is_risk_control = is_risk_control
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
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.is_indebted is not None:
            result['IsIndebted'] = self.is_indebted
        if self.is_indebted_overdue is not None:
            result['IsIndebtedOverdue'] = self.is_indebted_overdue
        if self.is_risk_control is not None:
            result['IsRiskControl'] = self.is_risk_control
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
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('IsIndebted') is not None:
            self.is_indebted = m.get('IsIndebted')
        if m.get('IsIndebtedOverdue') is not None:
            self.is_indebted_overdue = m.get('IsIndebtedOverdue')
        if m.get('IsRiskControl') is not None:
            self.is_risk_control = m.get('IsRiskControl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeUserBusinessStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserBusinessStatusResponseBody = None,
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
            temp_model = DescribeUserBusinessStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVSwitchesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_region_id: str = None,
        security_token: str = None,
        storage_bundle_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.resource_region_id = resource_region_id
        self.security_token = security_token
        self.storage_bundle_id = storage_bundle_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVSwitchesResponseBodyVSwitchesVSwitch(TeaModel):
    def __init__(
        self,
        available_selection_info: str = None,
        id: str = None,
        is_default: bool = None,
        name: str = None,
        zone_id: str = None,
    ):
        self.available_selection_info = available_selection_info
        self.id = id
        self.is_default = is_default
        self.name = name
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_selection_info is not None:
            result['AvailableSelectionInfo'] = self.available_selection_info
        if self.id is not None:
            result['Id'] = self.id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableSelectionInfo') is not None:
            self.available_selection_info = m.get('AvailableSelectionInfo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeVSwitchesResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        v_switch: List[DescribeVSwitchesResponseBodyVSwitchesVSwitch] = None,
    ):
        self.v_switch = v_switch

    def validate(self):
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k in m.get('VSwitch'):
                temp_model = DescribeVSwitchesResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        return self


class DescribeVSwitchesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        v_switches: DescribeVSwitchesResponseBodyVSwitches = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        if m.get('VSwitches') is not None:
            temp_model = DescribeVSwitchesResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m['VSwitches'])
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVSwitchesResponseBody = None,
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
            temp_model = DescribeVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_region_id: str = None,
        security_token: str = None,
        storage_bundle_id: str = None,
        vpc_id: str = None,
    ):
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.resource_region_id = resource_region_id
        self.security_token = security_token
        self.storage_bundle_id = storage_bundle_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVpcsResponseBodyVpcsVpc(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        id: str = None,
        is_default: bool = None,
        name: str = None,
    ):
        self.cidr_block = cidr_block
        self.id = id
        self.is_default = is_default
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.id is not None:
            result['Id'] = self.id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeVpcsResponseBodyVpcs(TeaModel):
    def __init__(
        self,
        vpc: List[DescribeVpcsResponseBodyVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = DescribeVpcsResponseBodyVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class DescribeVpcsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        vpcs: DescribeVpcsResponseBodyVpcs = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.vpcs = vpcs

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        if m.get('Vpcs') is not None:
            temp_model = DescribeVpcsResponseBodyVpcs()
            self.vpcs = temp_model.from_map(m['Vpcs'])
        return self


class DescribeVpcsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcsResponseBody = None,
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
            temp_model = DescribeVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        security_token: str = None,
    ):
        self.region_id = region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        zones: DescribeZonesResponseBodyZones = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

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
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
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
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZonesResponseBody = None,
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableGatewayLoggingRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DisableGatewayLoggingResponseBody(TeaModel):
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


class DisableGatewayLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableGatewayLoggingResponseBody = None,
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
            temp_model = DisableGatewayLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableGatewayNFSVersionRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        nfsversion: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.nfsversion = nfsversion
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.nfsversion is not None:
            result['NFSVersion'] = self.nfsversion
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('NFSVersion') is not None:
            self.nfsversion = m.get('NFSVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DisableGatewayNFSVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DisableGatewayNFSVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableGatewayNFSVersionResponseBody = None,
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
            temp_model = DisableGatewayNFSVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableGatewayIpv6Request(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class EnableGatewayIpv6ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class EnableGatewayIpv6Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableGatewayIpv6ResponseBody = None,
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
            temp_model = EnableGatewayIpv6ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableGatewayLoggingRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class EnableGatewayLoggingResponseBody(TeaModel):
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


class EnableGatewayLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableGatewayLoggingResponseBody = None,
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
            temp_model = EnableGatewayLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExpandCacheDiskRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        local_file_path: str = None,
        new_size_in_gb: int = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.local_file_path = local_file_path
        self.new_size_in_gb = new_size_in_gb
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.local_file_path is not None:
            result['LocalFilePath'] = self.local_file_path
        if self.new_size_in_gb is not None:
            result['NewSizeInGB'] = self.new_size_in_gb
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('LocalFilePath') is not None:
            self.local_file_path = m.get('LocalFilePath')
        if m.get('NewSizeInGB') is not None:
            self.new_size_in_gb = m.get('NewSizeInGB')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ExpandCacheDiskResponseBody(TeaModel):
    def __init__(
        self,
        buy_url: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.buy_url = buy_url
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_url is not None:
            result['BuyURL'] = self.buy_url
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyURL') is not None:
            self.buy_url = m.get('BuyURL')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ExpandCacheDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExpandCacheDiskResponseBody = None,
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
            temp_model = ExpandCacheDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExpandGatewayFileShareRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        index_id: str = None,
    ):
        self.gateway_id = gateway_id
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        return self


class ExpandGatewayFileShareResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ExpandGatewayFileShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExpandGatewayFileShareResponseBody = None,
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
            temp_model = ExpandGatewayFileShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExpandGatewayNetworkBandwidthRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        new_network_bandwidth: int = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.new_network_bandwidth = new_network_bandwidth
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.new_network_bandwidth is not None:
            result['NewNetworkBandwidth'] = self.new_network_bandwidth
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('NewNetworkBandwidth') is not None:
            self.new_network_bandwidth = m.get('NewNetworkBandwidth')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ExpandGatewayNetworkBandwidthResponseBody(TeaModel):
    def __init__(
        self,
        buy_url: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.buy_url = buy_url
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_url is not None:
            result['BuyURL'] = self.buy_url
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyURL') is not None:
            self.buy_url = m.get('BuyURL')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ExpandGatewayNetworkBandwidthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExpandGatewayNetworkBandwidthResponseBody = None,
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
            temp_model = ExpandGatewayNetworkBandwidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateGatewayTokenRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GenerateGatewayTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        token: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.token = token

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
        if self.token is not None:
            result['Token'] = self.token
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
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GenerateGatewayTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateGatewayTokenResponseBody = None,
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
            temp_model = GenerateGatewayTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateMqttTokenRequest(TeaModel):
    def __init__(
        self,
        client_uuid: str = None,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.client_uuid = client_uuid
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_uuid is not None:
            result['ClientUUID'] = self.client_uuid
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUUID') is not None:
            self.client_uuid = m.get('ClientUUID')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GenerateMqttTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        mqtt_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.mqtt_token = mqtt_token
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
        if self.mqtt_token is not None:
            result['MqttToken'] = self.mqtt_token
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
        if m.get('MqttToken') is not None:
            self.mqtt_token = m.get('MqttToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateMqttTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateMqttTokenResponseBody = None,
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
            temp_model = GenerateMqttTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateStsTokenRequest(TeaModel):
    def __init__(
        self,
        expire_in_seconds: int = None,
        gateway_id: str = None,
        security_token: str = None,
        token_type: str = None,
    ):
        self.expire_in_seconds = expire_in_seconds
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_in_seconds is not None:
            result['ExpireInSeconds'] = self.expire_in_seconds
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.token_type is not None:
            result['TokenType'] = self.token_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireInSeconds') is not None:
            self.expire_in_seconds = m.get('ExpireInSeconds')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TokenType') is not None:
            self.token_type = m.get('TokenType')
        return self


class GenerateStsTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        code: str = None,
        environment: str = None,
        expiration: str = None,
        message: str = None,
        request_id: str = None,
        security_token: str = None,
        success: bool = None,
        support_bundle_target: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.code = code
        self.environment = environment
        self.expiration = expiration
        self.message = message
        self.request_id = request_id
        self.security_token = security_token
        self.success = success
        self.support_bundle_target = support_bundle_target

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
        if self.code is not None:
            result['Code'] = self.code
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.success is not None:
            result['Success'] = self.success
        if self.support_bundle_target is not None:
            result['SupportBundleTarget'] = self.support_bundle_target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SupportBundleTarget') is not None:
            self.support_bundle_target = m.get('SupportBundleTarget')
        return self


class GenerateStsTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateStsTokenResponseBody = None,
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
            temp_model = GenerateStsTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HandleGatewayAutoPlanRequest(TeaModel):
    def __init__(
        self,
        cancel: bool = None,
        delay_hours: int = None,
        gateway_id: str = None,
        plan_id: str = None,
        security_token: str = None,
    ):
        self.cancel = cancel
        self.delay_hours = delay_hours
        self.gateway_id = gateway_id
        self.plan_id = plan_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancel is not None:
            result['Cancel'] = self.cancel
        if self.delay_hours is not None:
            result['DelayHours'] = self.delay_hours
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cancel') is not None:
            self.cancel = m.get('Cancel')
        if m.get('DelayHours') is not None:
            self.delay_hours = m.get('DelayHours')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class HandleGatewayAutoPlanResponseBody(TeaModel):
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


class HandleGatewayAutoPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HandleGatewayAutoPlanResponseBody = None,
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
            temp_model = HandleGatewayAutoPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_region_id: str = None,
        resource_type: str = None,
        security_token: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_region_id = resource_region_id
        self.resource_type = resource_type
        self.security_token = security_token
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGatewayRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        gateway_id: str = None,
        name: str = None,
        security_token: str = None,
    ):
        self.description = description
        self.gateway_id = gateway_id
        self.name = name
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.name is not None:
            result['Name'] = self.name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gateway_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.gateway_id = gateway_id
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
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
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
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyGatewayResponseBody = None,
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
            temp_model = ModifyGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGatewayBlockVolumeRequest(TeaModel):
    def __init__(
        self,
        cache_config: str = None,
        gateway_id: str = None,
        index_id: str = None,
        security_token: str = None,
    ):
        self.cache_config = cache_config
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_config is not None:
            result['CacheConfig'] = self.cache_config
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheConfig') is not None:
            self.cache_config = m.get('CacheConfig')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyGatewayBlockVolumeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyGatewayBlockVolumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyGatewayBlockVolumeResponseBody = None,
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
            temp_model = ModifyGatewayBlockVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGatewayClassRequest(TeaModel):
    def __init__(
        self,
        gateway_class: str = None,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_class = gateway_class
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_class is not None:
            result['GatewayClass'] = self.gateway_class
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayClass') is not None:
            self.gateway_class = m.get('GatewayClass')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyGatewayClassResponseBody(TeaModel):
    def __init__(
        self,
        buy_url: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.buy_url = buy_url
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_url is not None:
            result['BuyURL'] = self.buy_url
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyURL') is not None:
            self.buy_url = m.get('BuyURL')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyGatewayClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyGatewayClassResponseBody = None,
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
            temp_model = ModifyGatewayClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGatewayFileShareRequest(TeaModel):
    def __init__(
        self,
        cache_config: str = None,
        gateway_id: str = None,
        index_id: str = None,
        security_token: str = None,
    ):
        self.cache_config = cache_config
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_config is not None:
            result['CacheConfig'] = self.cache_config
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheConfig') is not None:
            self.cache_config = m.get('CacheConfig')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyGatewayFileShareResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyGatewayFileShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyGatewayFileShareResponseBody = None,
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
            temp_model = ModifyGatewayFileShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGatewayFileShareWatermarkRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        index_id: str = None,
        security_token: str = None,
        watermark: int = None,
    ):
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.security_token = security_token
        self.watermark = watermark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        return self


class ModifyGatewayFileShareWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyGatewayFileShareWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyGatewayFileShareWatermarkResponseBody = None,
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
            temp_model = ModifyGatewayFileShareWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyStorageBundleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        security_token: str = None,
        storage_bundle_id: str = None,
    ):
        self.description = description
        self.name = name
        self.security_token = security_token
        self.storage_bundle_id = storage_bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        return self


class ModifyStorageBundleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        storage_bundle_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.storage_bundle_id = storage_bundle_id
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
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
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
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyStorageBundleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyStorageBundleResponseBody = None,
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
            temp_model = ModifyStorageBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenSgwServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenSgwServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenSgwServiceResponseBody = None,
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
            temp_model = OpenSgwServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        operate_action: str = None,
        params: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.operate_action = operate_action
        self.params = params
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.operate_action is not None:
            result['OperateAction'] = self.operate_action
        if self.params is not None:
            result['Params'] = self.params
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('OperateAction') is not None:
            self.operate_action = m.get('OperateAction')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class OperateGatewayResponseBody(TeaModel):
    def __init__(
        self,
        buy_url: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.buy_url = buy_url
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_url is not None:
            result['BuyURL'] = self.buy_url
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyURL') is not None:
            self.buy_url = m.get('BuyURL')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class OperateGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateGatewayResponseBody = None,
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
            temp_model = OperateGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseServiceRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
    ):
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ReleaseServiceResponseBody(TeaModel):
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


class ReleaseServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseServiceResponseBody = None,
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
            temp_model = ReleaseServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSharesFromExpressSyncRequest(TeaModel):
    def __init__(
        self,
        express_sync_id: str = None,
        gateway_shares: str = None,
        security_token: str = None,
    ):
        self.express_sync_id = express_sync_id
        self.gateway_shares = gateway_shares
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.express_sync_id is not None:
            result['ExpressSyncId'] = self.express_sync_id
        if self.gateway_shares is not None:
            result['GatewayShares'] = self.gateway_shares
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressSyncId') is not None:
            self.express_sync_id = m.get('ExpressSyncId')
        if m.get('GatewayShares') is not None:
            self.gateway_shares = m.get('GatewayShares')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RemoveSharesFromExpressSyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RemoveSharesFromExpressSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveSharesFromExpressSyncResponseBody = None,
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
            temp_model = RemoveSharesFromExpressSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTagsFromGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
        tags: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class RemoveTagsFromGatewayResponseBody(TeaModel):
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


class RemoveTagsFromGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveTagsFromGatewayResponseBody = None,
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
            temp_model = RemoveTagsFromGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportBlockVolumesRequest(TeaModel):
    def __init__(
        self,
        client_uuid: str = None,
        gateway_id: str = None,
        info: str = None,
        security_token: str = None,
    ):
        self.client_uuid = client_uuid
        self.gateway_id = gateway_id
        self.info = info
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_uuid is not None:
            result['ClientUUID'] = self.client_uuid
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.info is not None:
            result['Info'] = self.info
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUUID') is not None:
            self.client_uuid = m.get('ClientUUID')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ReportBlockVolumesResponseBody(TeaModel):
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


class ReportBlockVolumesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportBlockVolumesResponseBody = None,
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
            temp_model = ReportBlockVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportFileSharesRequest(TeaModel):
    def __init__(
        self,
        client_uuid: str = None,
        gateway_id: str = None,
        info: str = None,
        security_token: str = None,
    ):
        self.client_uuid = client_uuid
        self.gateway_id = gateway_id
        self.info = info
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_uuid is not None:
            result['ClientUUID'] = self.client_uuid
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.info is not None:
            result['Info'] = self.info
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUUID') is not None:
            self.client_uuid = m.get('ClientUUID')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ReportFileSharesResponseBody(TeaModel):
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


class ReportFileSharesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportFileSharesResponseBody = None,
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
            temp_model = ReportFileSharesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportGatewayInfoRequest(TeaModel):
    def __init__(
        self,
        client_uuid: str = None,
        gateway_id: str = None,
        gateway_status: str = None,
        info: str = None,
        security_token: str = None,
        time: int = None,
    ):
        self.client_uuid = client_uuid
        self.gateway_id = gateway_id
        self.gateway_status = gateway_status
        self.info = info
        self.security_token = security_token
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_uuid is not None:
            result['ClientUUID'] = self.client_uuid
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_status is not None:
            result['GatewayStatus'] = self.gateway_status
        if self.info is not None:
            result['Info'] = self.info
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUUID') is not None:
            self.client_uuid = m.get('ClientUUID')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayStatus') is not None:
            self.gateway_status = m.get('GatewayStatus')
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class ReportGatewayInfoResponseBody(TeaModel):
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


class ReportGatewayInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportGatewayInfoResponseBody = None,
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
            temp_model = ReportGatewayInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportGatewayUsageRequest(TeaModel):
    def __init__(
        self,
        client_uuid: str = None,
        gateway_id: str = None,
        security_token: str = None,
        usage: str = None,
    ):
        self.client_uuid = client_uuid
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_uuid is not None:
            result['ClientUUID'] = self.client_uuid
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUUID') is not None:
            self.client_uuid = m.get('ClientUUID')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class ReportGatewayUsageResponseBody(TeaModel):
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


class ReportGatewayUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportGatewayUsageResponseBody = None,
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
            temp_model = ReportGatewayUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetGatewayPasswordRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        password: str = None,
        security_token: str = None,
        username: str = None,
    ):
        self.gateway_id = gateway_id
        self.password = password
        self.security_token = security_token
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.password is not None:
            result['Password'] = self.password
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ResetGatewayPasswordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ResetGatewayPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetGatewayPasswordResponseBody = None,
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
            temp_model = ResetGatewayPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartFileSharesRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
        share_protocol: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token
        self.share_protocol = share_protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.share_protocol is not None:
            result['ShareProtocol'] = self.share_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ShareProtocol') is not None:
            self.share_protocol = m.get('ShareProtocol')
        return self


class RestartFileSharesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RestartFileSharesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartFileSharesResponseBody = None,
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
            temp_model = RestartFileSharesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGatewayADInfoRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        is_enabled: bool = None,
        password: str = None,
        security_token: str = None,
        server_ip: str = None,
        username: str = None,
    ):
        self.gateway_id = gateway_id
        self.is_enabled = is_enabled
        self.password = password
        self.security_token = security_token
        self.server_ip = server_ip
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.password is not None:
            result['Password'] = self.password
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class SetGatewayADInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SetGatewayADInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGatewayADInfoResponseBody = None,
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
            temp_model = SetGatewayADInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGatewayAutoUpgradeConfigurationRequest(TeaModel):
    def __init__(
        self,
        auto_upgrade_end_hour: int = None,
        auto_upgrade_start_hour: int = None,
        gateway_id: str = None,
        is_auto_upgrade: bool = None,
        security_token: str = None,
    ):
        self.auto_upgrade_end_hour = auto_upgrade_end_hour
        self.auto_upgrade_start_hour = auto_upgrade_start_hour
        self.gateway_id = gateway_id
        self.is_auto_upgrade = is_auto_upgrade
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_upgrade_end_hour is not None:
            result['AutoUpgradeEndHour'] = self.auto_upgrade_end_hour
        if self.auto_upgrade_start_hour is not None:
            result['AutoUpgradeStartHour'] = self.auto_upgrade_start_hour
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.is_auto_upgrade is not None:
            result['IsAutoUpgrade'] = self.is_auto_upgrade
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpgradeEndHour') is not None:
            self.auto_upgrade_end_hour = m.get('AutoUpgradeEndHour')
        if m.get('AutoUpgradeStartHour') is not None:
            self.auto_upgrade_start_hour = m.get('AutoUpgradeStartHour')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IsAutoUpgrade') is not None:
            self.is_auto_upgrade = m.get('IsAutoUpgrade')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetGatewayAutoUpgradeConfigurationResponseBody(TeaModel):
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


class SetGatewayAutoUpgradeConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGatewayAutoUpgradeConfigurationResponseBody = None,
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
            temp_model = SetGatewayAutoUpgradeConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGatewayDNSRequest(TeaModel):
    def __init__(
        self,
        dns_server: str = None,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.dns_server = dns_server
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetGatewayDNSResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SetGatewayDNSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGatewayDNSResponseBody = None,
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
            temp_model = SetGatewayDNSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGatewayLDAPInfoRequest(TeaModel):
    def __init__(
        self,
        base_dn: str = None,
        gateway_id: str = None,
        is_enabled: bool = None,
        is_tls: bool = None,
        password: str = None,
        root_dn: str = None,
        security_token: str = None,
        server_ip: str = None,
    ):
        self.base_dn = base_dn
        self.gateway_id = gateway_id
        self.is_enabled = is_enabled
        self.is_tls = is_tls
        self.password = password
        self.root_dn = root_dn
        self.security_token = security_token
        self.server_ip = server_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.is_tls is not None:
            result['IsTls'] = self.is_tls
        if self.password is not None:
            result['Password'] = self.password
        if self.root_dn is not None:
            result['RootDN'] = self.root_dn
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('IsTls') is not None:
            self.is_tls = m.get('IsTls')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RootDN') is not None:
            self.root_dn = m.get('RootDN')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        return self


class SetGatewayLDAPInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SetGatewayLDAPInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGatewayLDAPInfoResponseBody = None,
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
            temp_model = SetGatewayLDAPInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchCSGClientsReverseSyncConfigurationRequest(TeaModel):
    def __init__(
        self,
        client_ids: List[str] = None,
        client_region_id: str = None,
        is_reverse_sync: bool = None,
        reverse_sync_internal_second: int = None,
        security_token: str = None,
    ):
        self.client_ids = client_ids
        self.client_region_id = client_region_id
        self.is_reverse_sync = is_reverse_sync
        self.reverse_sync_internal_second = reverse_sync_internal_second
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.client_region_id is not None:
            result['ClientRegionId'] = self.client_region_id
        if self.is_reverse_sync is not None:
            result['IsReverseSync'] = self.is_reverse_sync
        if self.reverse_sync_internal_second is not None:
            result['ReverseSyncInternalSecond'] = self.reverse_sync_internal_second
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('ClientRegionId') is not None:
            self.client_region_id = m.get('ClientRegionId')
        if m.get('IsReverseSync') is not None:
            self.is_reverse_sync = m.get('IsReverseSync')
        if m.get('ReverseSyncInternalSecond') is not None:
            self.reverse_sync_internal_second = m.get('ReverseSyncInternalSecond')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SwitchCSGClientsReverseSyncConfigurationShrinkRequest(TeaModel):
    def __init__(
        self,
        client_ids_shrink: str = None,
        client_region_id: str = None,
        is_reverse_sync: bool = None,
        reverse_sync_internal_second: int = None,
        security_token: str = None,
    ):
        self.client_ids_shrink = client_ids_shrink
        self.client_region_id = client_region_id
        self.is_reverse_sync = is_reverse_sync
        self.reverse_sync_internal_second = reverse_sync_internal_second
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink
        if self.client_region_id is not None:
            result['ClientRegionId'] = self.client_region_id
        if self.is_reverse_sync is not None:
            result['IsReverseSync'] = self.is_reverse_sync
        if self.reverse_sync_internal_second is not None:
            result['ReverseSyncInternalSecond'] = self.reverse_sync_internal_second
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')
        if m.get('ClientRegionId') is not None:
            self.client_region_id = m.get('ClientRegionId')
        if m.get('IsReverseSync') is not None:
            self.is_reverse_sync = m.get('IsReverseSync')
        if m.get('ReverseSyncInternalSecond') is not None:
            self.reverse_sync_internal_second = m.get('ReverseSyncInternalSecond')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SwitchCSGClientsReverseSyncConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SwitchCSGClientsReverseSyncConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchCSGClientsReverseSyncConfigurationResponseBody = None,
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
            temp_model = SwitchCSGClientsReverseSyncConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchGatewayExpirationPolicyRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SwitchGatewayExpirationPolicyResponseBody(TeaModel):
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


class SwitchGatewayExpirationPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchGatewayExpirationPolicyResponseBody = None,
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
            temp_model = SwitchGatewayExpirationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchToSubscriptionRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SwitchToSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        subscription_url: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.subscription_url = subscription_url
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
        if self.subscription_url is not None:
            result['SubscriptionURL'] = self.subscription_url
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
        if m.get('SubscriptionURL') is not None:
            self.subscription_url = m.get('SubscriptionURL')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SwitchToSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchToSubscriptionResponseBody = None,
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
            temp_model = SwitchToSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_region_id: str = None,
        resource_type: str = None,
        security_token: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_region_id = resource_region_id
        self.resource_type = resource_type
        self.security_token = security_token
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerGatewayRemoteSyncRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        index_id: str = None,
        path: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.path = path
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.path is not None:
            result['Path'] = self.path
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class TriggerGatewayRemoteSyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TriggerGatewayRemoteSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerGatewayRemoteSyncResponseBody = None,
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
            temp_model = TriggerGatewayRemoteSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_region_id: str = None,
        resource_type: str = None,
        security_token: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_region_id = resource_region_id
        self.resource_type = resource_type
        self.security_token = security_token
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayBlockVolumeRequest(TeaModel):
    def __init__(
        self,
        chap_enabled: bool = None,
        chap_in_password: str = None,
        chap_in_user: str = None,
        gateway_id: str = None,
        index_id: str = None,
        security_token: str = None,
        size: int = None,
    ):
        self.chap_enabled = chap_enabled
        self.chap_in_password = chap_in_password
        self.chap_in_user = chap_in_user
        self.gateway_id = gateway_id
        self.index_id = index_id
        self.security_token = security_token
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chap_enabled is not None:
            result['ChapEnabled'] = self.chap_enabled
        if self.chap_in_password is not None:
            result['ChapInPassword'] = self.chap_in_password
        if self.chap_in_user is not None:
            result['ChapInUser'] = self.chap_in_user
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChapEnabled') is not None:
            self.chap_enabled = m.get('ChapEnabled')
        if m.get('ChapInPassword') is not None:
            self.chap_in_password = m.get('ChapInPassword')
        if m.get('ChapInUser') is not None:
            self.chap_in_user = m.get('ChapInUser')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class UpdateGatewayBlockVolumeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateGatewayBlockVolumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGatewayBlockVolumeResponseBody = None,
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
            temp_model = UpdateGatewayBlockVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayFileShareRequest(TeaModel):
    def __init__(
        self,
        access_based_enumeration: bool = None,
        backend_limit: int = None,
        browsable: bool = None,
        bypass_cache_read: bool = None,
        cache_mode: str = None,
        client_side_cmk: str = None,
        client_side_encryption: bool = None,
        direct_io: bool = None,
        download_limit: int = None,
        fast_reclaim: bool = None,
        frontend_limit: int = None,
        gateway_id: str = None,
        ignore_delete: bool = None,
        in_place: bool = None,
        index_id: str = None,
        kms_rotate_period: int = None,
        lag_period: int = None,
        name: str = None,
        nfs_v4optimization: bool = None,
        polling_interval: int = None,
        read_only_client_list: str = None,
        read_only_user_list: str = None,
        read_write_client_list: str = None,
        read_write_user_list: str = None,
        remote_sync: bool = None,
        remote_sync_download: bool = None,
        security_token: str = None,
        server_side_cmk: str = None,
        server_side_encryption: bool = None,
        squash: str = None,
        transfer_acceleration: bool = None,
        windows_acl: bool = None,
    ):
        self.access_based_enumeration = access_based_enumeration
        self.backend_limit = backend_limit
        self.browsable = browsable
        self.bypass_cache_read = bypass_cache_read
        self.cache_mode = cache_mode
        self.client_side_cmk = client_side_cmk
        self.client_side_encryption = client_side_encryption
        self.direct_io = direct_io
        self.download_limit = download_limit
        self.fast_reclaim = fast_reclaim
        self.frontend_limit = frontend_limit
        self.gateway_id = gateway_id
        self.ignore_delete = ignore_delete
        self.in_place = in_place
        self.index_id = index_id
        self.kms_rotate_period = kms_rotate_period
        self.lag_period = lag_period
        self.name = name
        self.nfs_v4optimization = nfs_v4optimization
        self.polling_interval = polling_interval
        self.read_only_client_list = read_only_client_list
        self.read_only_user_list = read_only_user_list
        self.read_write_client_list = read_write_client_list
        self.read_write_user_list = read_write_user_list
        self.remote_sync = remote_sync
        self.remote_sync_download = remote_sync_download
        self.security_token = security_token
        self.server_side_cmk = server_side_cmk
        self.server_side_encryption = server_side_encryption
        self.squash = squash
        self.transfer_acceleration = transfer_acceleration
        self.windows_acl = windows_acl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_based_enumeration is not None:
            result['AccessBasedEnumeration'] = self.access_based_enumeration
        if self.backend_limit is not None:
            result['BackendLimit'] = self.backend_limit
        if self.browsable is not None:
            result['Browsable'] = self.browsable
        if self.bypass_cache_read is not None:
            result['BypassCacheRead'] = self.bypass_cache_read
        if self.cache_mode is not None:
            result['CacheMode'] = self.cache_mode
        if self.client_side_cmk is not None:
            result['ClientSideCmk'] = self.client_side_cmk
        if self.client_side_encryption is not None:
            result['ClientSideEncryption'] = self.client_side_encryption
        if self.direct_io is not None:
            result['DirectIO'] = self.direct_io
        if self.download_limit is not None:
            result['DownloadLimit'] = self.download_limit
        if self.fast_reclaim is not None:
            result['FastReclaim'] = self.fast_reclaim
        if self.frontend_limit is not None:
            result['FrontendLimit'] = self.frontend_limit
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.ignore_delete is not None:
            result['IgnoreDelete'] = self.ignore_delete
        if self.in_place is not None:
            result['InPlace'] = self.in_place
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.kms_rotate_period is not None:
            result['KmsRotatePeriod'] = self.kms_rotate_period
        if self.lag_period is not None:
            result['LagPeriod'] = self.lag_period
        if self.name is not None:
            result['Name'] = self.name
        if self.nfs_v4optimization is not None:
            result['NfsV4Optimization'] = self.nfs_v4optimization
        if self.polling_interval is not None:
            result['PollingInterval'] = self.polling_interval
        if self.read_only_client_list is not None:
            result['ReadOnlyClientList'] = self.read_only_client_list
        if self.read_only_user_list is not None:
            result['ReadOnlyUserList'] = self.read_only_user_list
        if self.read_write_client_list is not None:
            result['ReadWriteClientList'] = self.read_write_client_list
        if self.read_write_user_list is not None:
            result['ReadWriteUserList'] = self.read_write_user_list
        if self.remote_sync is not None:
            result['RemoteSync'] = self.remote_sync
        if self.remote_sync_download is not None:
            result['RemoteSyncDownload'] = self.remote_sync_download
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_side_cmk is not None:
            result['ServerSideCmk'] = self.server_side_cmk
        if self.server_side_encryption is not None:
            result['ServerSideEncryption'] = self.server_side_encryption
        if self.squash is not None:
            result['Squash'] = self.squash
        if self.transfer_acceleration is not None:
            result['TransferAcceleration'] = self.transfer_acceleration
        if self.windows_acl is not None:
            result['WindowsAcl'] = self.windows_acl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessBasedEnumeration') is not None:
            self.access_based_enumeration = m.get('AccessBasedEnumeration')
        if m.get('BackendLimit') is not None:
            self.backend_limit = m.get('BackendLimit')
        if m.get('Browsable') is not None:
            self.browsable = m.get('Browsable')
        if m.get('BypassCacheRead') is not None:
            self.bypass_cache_read = m.get('BypassCacheRead')
        if m.get('CacheMode') is not None:
            self.cache_mode = m.get('CacheMode')
        if m.get('ClientSideCmk') is not None:
            self.client_side_cmk = m.get('ClientSideCmk')
        if m.get('ClientSideEncryption') is not None:
            self.client_side_encryption = m.get('ClientSideEncryption')
        if m.get('DirectIO') is not None:
            self.direct_io = m.get('DirectIO')
        if m.get('DownloadLimit') is not None:
            self.download_limit = m.get('DownloadLimit')
        if m.get('FastReclaim') is not None:
            self.fast_reclaim = m.get('FastReclaim')
        if m.get('FrontendLimit') is not None:
            self.frontend_limit = m.get('FrontendLimit')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('IgnoreDelete') is not None:
            self.ignore_delete = m.get('IgnoreDelete')
        if m.get('InPlace') is not None:
            self.in_place = m.get('InPlace')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('KmsRotatePeriod') is not None:
            self.kms_rotate_period = m.get('KmsRotatePeriod')
        if m.get('LagPeriod') is not None:
            self.lag_period = m.get('LagPeriod')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NfsV4Optimization') is not None:
            self.nfs_v4optimization = m.get('NfsV4Optimization')
        if m.get('PollingInterval') is not None:
            self.polling_interval = m.get('PollingInterval')
        if m.get('ReadOnlyClientList') is not None:
            self.read_only_client_list = m.get('ReadOnlyClientList')
        if m.get('ReadOnlyUserList') is not None:
            self.read_only_user_list = m.get('ReadOnlyUserList')
        if m.get('ReadWriteClientList') is not None:
            self.read_write_client_list = m.get('ReadWriteClientList')
        if m.get('ReadWriteUserList') is not None:
            self.read_write_user_list = m.get('ReadWriteUserList')
        if m.get('RemoteSync') is not None:
            self.remote_sync = m.get('RemoteSync')
        if m.get('RemoteSyncDownload') is not None:
            self.remote_sync_download = m.get('RemoteSyncDownload')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerSideCmk') is not None:
            self.server_side_cmk = m.get('ServerSideCmk')
        if m.get('ServerSideEncryption') is not None:
            self.server_side_encryption = m.get('ServerSideEncryption')
        if m.get('Squash') is not None:
            self.squash = m.get('Squash')
        if m.get('TransferAcceleration') is not None:
            self.transfer_acceleration = m.get('TransferAcceleration')
        if m.get('WindowsAcl') is not None:
            self.windows_acl = m.get('WindowsAcl')
        return self


class UpdateGatewayFileShareResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateGatewayFileShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGatewayFileShareResponseBody = None,
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
            temp_model = UpdateGatewayFileShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_token: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class UpgradeGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpgradeGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeGatewayResponseBody = None,
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
            temp_model = UpgradeGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadCSGClientLogRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_region_id: str = None,
        security_token: str = None,
    ):
        self.client_id = client_id
        self.client_region_id = client_region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_region_id is not None:
            result['ClientRegionId'] = self.client_region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientRegionId') is not None:
            self.client_region_id = m.get('ClientRegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class UploadCSGClientLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UploadCSGClientLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadCSGClientLogResponseBody = None,
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
            temp_model = UploadCSGClientLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadGatewayLogRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
    ):
        self.gateway_id = gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        return self


class UploadGatewayLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UploadGatewayLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadGatewayLogResponseBody = None,
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
            temp_model = UploadGatewayLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateExpressSyncConfigRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_prefix: str = None,
        bucket_region: str = None,
        name: str = None,
        security_token: str = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_prefix = bucket_prefix
        self.bucket_region = bucket_region
        self.name = name
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_prefix is not None:
            result['BucketPrefix'] = self.bucket_prefix
        if self.bucket_region is not None:
            result['BucketRegion'] = self.bucket_region
        if self.name is not None:
            result['Name'] = self.name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketPrefix') is not None:
            self.bucket_prefix = m.get('BucketPrefix')
        if m.get('BucketRegion') is not None:
            self.bucket_region = m.get('BucketRegion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ValidateExpressSyncConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_valid: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        validate_message: str = None,
    ):
        self.code = code
        self.is_valid = is_valid
        self.message = message
        self.request_id = request_id
        self.success = success
        self.validate_message = validate_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_valid is not None:
            result['IsValid'] = self.is_valid
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.validate_message is not None:
            result['ValidateMessage'] = self.validate_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ValidateMessage') is not None:
            self.validate_message = m.get('ValidateMessage')
        return self


class ValidateExpressSyncConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateExpressSyncConfigResponseBody = None,
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
            temp_model = ValidateExpressSyncConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateGatewayNameRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        storage_bundle_id: str = None,
    ):
        self.name = name
        self.storage_bundle_id = storage_bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.storage_bundle_id is not None:
            result['StorageBundleId'] = self.storage_bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StorageBundleId') is not None:
            self.storage_bundle_id = m.get('StorageBundleId')
        return self


class ValidateGatewayNameResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_valid: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.is_valid = is_valid
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
        if self.is_valid is not None:
            result['IsValid'] = self.is_valid
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
        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidateGatewayNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateGatewayNameResponseBody = None,
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
            temp_model = ValidateGatewayNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



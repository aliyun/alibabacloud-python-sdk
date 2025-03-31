# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ActiveCaCertificateRequest(TeaModel):
    def __init__(
        self,
        mqtt_instance_id: str = None,
        sn: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance to which the CA certificate is bound.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # The serial number of the CA certificate that you want to reactivate. The serial number is the unique identifier of a CA certificate.
        # 
        # The serial number of a CA certificate cannot exceed 128 bytes in size.
        # 
        # This parameter is required.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class ActiveCaCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sn: str = None,
    ):
        # Public parameters, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # The SN serial number of the activated CA certificate, used to uniquely identify a CA certificate.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class ActiveCaCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActiveCaCertificateResponseBody = None,
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
            temp_model = ActiveCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ActiveDeviceCertificateRequest(TeaModel):
    def __init__(
        self,
        ca_sn: str = None,
        device_sn: str = None,
        mqtt_instance_id: str = None,
    ):
        # The serial number of the CA certificate to which the device certificate belongs. The serial number is the unique identifier of a CA certificate.
        # 
        # The serial number of a CA certificate cannot exceed 128 bytes in size.
        # 
        # This parameter is required.
        self.ca_sn = ca_sn
        # The serial number of the device certificate that you want to reactivate. The serial number is the unique identifier of a device.
        # 
        # This parameter is required.
        self.device_sn = device_sn
        # The ID of the ApsaraMQ for MQTT instance to which the device certificate is bound.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        return self


class ActiveDeviceCertificateResponseBody(TeaModel):
    def __init__(
        self,
        device_sn: str = None,
        request_id: str = None,
    ):
        # The serial number of the device certificate that you reactivated. The serial number is the unique identifier of a device certificate.
        self.device_sn = device_sn
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ActiveDeviceCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActiveDeviceCertificateResponseBody = None,
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
            temp_model = ActiveDeviceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCustomAuthConnectBlackRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
    ):
        # The client ID of the device whose connections you want to disable.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AddCustomAuthConnectBlackResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The value 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
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


class AddCustomAuthConnectBlackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCustomAuthConnectBlackResponseBody = None,
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
            temp_model = AddCustomAuthConnectBlackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCustomAuthIdentityRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        identity_type: str = None,
        instance_id: str = None,
        secret: str = None,
        sign_mode: str = None,
        username: str = None,
    ):
        # The client ID if you set IdentityType to CLIENT.
        self.client_id = client_id
        # The identity type. Valid values:
        # 
        # *   USER
        # *   CLIENT
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The ID of the Message Queue for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The AccessKey secret.
        # 
        # This parameter is required.
        self.secret = secret
        # The signature verification mode. ORIGIN: compares the password and the AccessKey secret. SIGNED: uses the HMAC_SHA1 algorithm to sign the client ID to obtain a password and then compares the password.
        # 
        # This parameter is required.
        self.sign_mode = sign_mode
        # The username.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class AddCustomAuthIdentityResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
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


class AddCustomAuthIdentityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCustomAuthIdentityResponseBody = None,
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
            temp_model = AddCustomAuthIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCustomAuthPermissionRequest(TeaModel):
    def __init__(
        self,
        effect: str = None,
        identity: str = None,
        identity_type: str = None,
        instance_id: str = None,
        permit_action: str = None,
        topic: str = None,
    ):
        # Specifies whether to allow or deny access.
        # 
        # This parameter is required.
        self.effect = effect
        # The username or client ID.
        # 
        # This parameter is required.
        self.identity = identity
        # The identity type. Valid values: USER and CLIENT.
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The permissions that you want to grant.
        # 
        # This parameter is required.
        self.permit_action = permit_action
        # The topics on which you want to grant permissions. Multi-level topics and wildcard characters are supported.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.permit_action is not None:
            result['PermitAction'] = self.permit_action
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PermitAction') is not None:
            self.permit_action = m.get('PermitAction')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class AddCustomAuthPermissionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
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


class AddCustomAuthPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCustomAuthPermissionResponseBody = None,
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
            temp_model = AddCustomAuthPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyTokenRequest(TeaModel):
    def __init__(
        self,
        actions: str = None,
        expire_time: int = None,
        instance_id: str = None,
        resources: str = None,
    ):
        # The permission type of the token. Valid values:
        # 
        # *   **R**: read-only. You can only subscribe to the specified topics.
        # *   **W**: write-only. You can only send messages to the specified topics.
        # *   **R,W**: read and write. You can send messages to and subscribe to the specified topics. Separate **R** and **W** with a comma (,).
        # 
        # This parameter is required.
        self.actions = actions
        # The timestamp that indicates the point in time when the token expires. Unit: milliseconds. The minimum validity period of a token is 60 seconds, and the maximum validity period of a token is 30 days. If you specify a validity period of more than 30 days for a token, no errors are returned. However, the token is valid only for 30 days.
        # 
        # For example, you want to specify a validity period of 60 seconds for a token. If the current system timestamp is 1609434061000, you must set this parameter to **1609434121000**. The value is calculated by using the following formula: 1609434061000 + 60 x 1000 = 1609434121000.
        # 
        # This parameter is required.
        self.expire_time = expire_time
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com/).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The topics on the ApsaraMQ for MQTT instance. Separate multiple topics with commas (,). Each token can be used to access up to 100 topics. Multiple topics are sorted in alphabetic order. MQTT wildcards, including single-level wildcards represented by plus signs (+) and multi-level wildcards represented by number signs (#), can be used for the Resources parameter that you register to apply for a token.
        # 
        # For example, if you set the **Resources** parameter to Topic1/+ when you apply for a token, the ApsaraMQ for MQTT client can manage the topics in Topic1/xxx. If you set the **Resources** parameter to Topic1/# when you apply for a token, the ApsaraMQ for MQTT client can manage topics of any level in Topic1/xxx/xxx/xxx.
        # 
        # >  ApsaraMQ for MQTT supports subtopics. You can specify subtopics in the code for messaging instead of configuring them in the ApsaraMQ for MQTT console. Forward slashes (/) are used to separate topics of different levels. For more information, see [Terms](https://help.aliyun.com/document_detail/42420.html).
        # 
        # This parameter is required.
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['Actions'] = self.actions
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions = m.get('Actions')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class ApplyTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token: str = None,
    ):
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id
        # The token that is returned by the ApsaraMQ for MQTT broker.
        # 
        # >  Do not assume the length, format, or rule of the token to return. The actual returned token shall prevail.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ApplyTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyTokenResponseBody = None,
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
            temp_model = ApplyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchQuerySessionByClientIdsRequest(TeaModel):
    def __init__(
        self,
        client_id_list: List[str] = None,
        instance_id: str = None,
    ):
        # The ApsaraMQ for MQTT clients.
        # 
        # This parameter is required.
        self.client_id_list = client_id_list
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com).
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id_list is not None:
            result['ClientIdList'] = self.client_id_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIdList') is not None:
            self.client_id_list = m.get('ClientIdList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class BatchQuerySessionByClientIdsResponseBodyOnlineStatusList(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        online_status: bool = None,
    ):
        # The ID of the ApsaraMQ for MQTT client. For more information about client IDs, see [Terms](https://help.aliyun.com/document_detail/42420.html).
        self.client_id = client_id
        # Indicates whether the ApsaraMQ for MQTT client is online. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.online_status = online_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        return self


class BatchQuerySessionByClientIdsResponseBody(TeaModel):
    def __init__(
        self,
        online_status_list: List[BatchQuerySessionByClientIdsResponseBodyOnlineStatusList] = None,
        request_id: str = None,
    ):
        # The status list of all queried ApsaraMQ for MQTT clients.
        self.online_status_list = online_status_list
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        if self.online_status_list:
            for k in self.online_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OnlineStatusList'] = []
        if self.online_status_list is not None:
            for k in self.online_status_list:
                result['OnlineStatusList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.online_status_list = []
        if m.get('OnlineStatusList') is not None:
            for k in m.get('OnlineStatusList'):
                temp_model = BatchQuerySessionByClientIdsResponseBodyOnlineStatusList()
                self.online_status_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchQuerySessionByClientIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchQuerySessionByClientIdsResponseBody = None,
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
            temp_model = BatchQuerySessionByClientIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseConnectionRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
    ):
        # Client ID of the device
        # 
        # This parameter is required.
        self.client_id = client_id
        # ID of the Micro Message Queue MQTT version instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CloseConnectionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Return code of the interface: 200 indicates success. Other values indicate error codes. For details about the error codes, see Error Codes.
        self.code = code
        # Call result information
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the operation was successful. true means success, false means failure.
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


class CloseConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseConnectionResponseBody = None,
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
            temp_model = CloseConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupIdRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        tags: str = None,
    ):
        # The ID of the group that you want to create. The group ID must meet the following conventions:
        # 
        # *   The ID must be 7 to 64 characters in length. It must start with GID_ or GID- and can contain only letters, digits, hyphens (-), and underscores (_).
        # *   The ID cannot be changed after the group is created. For more information, see [Terms](https://help.aliyun.com/document_detail/42420.html).
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the ApsaraMQ for MQTT instance to which the group belongs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID. This parameter is a common parameter.
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


class CreateGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGroupIdResponseBody = None,
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
            temp_model = CreateGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCaCertificateRequest(TeaModel):
    def __init__(
        self,
        mqtt_instance_id: str = None,
        sn: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance to which the CA certificate is bound.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # The serial number of the CA certificate that you want to delete. The serial number is the unique identifier of a CA certificate.
        # 
        # The serial number of a CA certificate cannot exceed 128 bytes in size.
        # 
        # This parameter is required.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class DeleteCaCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sn: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The serial number of the CA certificate that you deleted. The serial number is the unique identifier of a CA certificate.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class DeleteCaCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCaCertificateResponseBody = None,
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
            temp_model = DeleteCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomAuthConnectBlackRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteCustomAuthConnectBlackResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values: true and false.
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


class DeleteCustomAuthConnectBlackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomAuthConnectBlackResponseBody = None,
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
            temp_model = DeleteCustomAuthConnectBlackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomAuthIdentityRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        identity_type: str = None,
        instance_id: str = None,
        username: str = None,
    ):
        # The client ID if you set IdentityType to CLIENT.
        self.client_id = client_id
        # The identity type. Valid values:
        # 
        # *   USER
        # *   CLIENT
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The username.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DeleteCustomAuthIdentityResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful. Other status codes indicate that the request failed.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
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


class DeleteCustomAuthIdentityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomAuthIdentityResponseBody = None,
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
            temp_model = DeleteCustomAuthIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomAuthPermissionRequest(TeaModel):
    def __init__(
        self,
        identity: str = None,
        identity_type: str = None,
        instance_id: str = None,
        topic: str = None,
    ):
        # The username or client ID.
        # 
        # This parameter is required.
        self.identity = identity
        # The identity type. Valid values:
        # 
        # *   USER
        # *   CLIENT
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The topic on which you want to grant permissions. Multi-level topics and Wildcard characters are supported.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class DeleteCustomAuthPermissionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
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


class DeleteCustomAuthPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomAuthPermissionResponseBody = None,
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
            temp_model = DeleteCustomAuthPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceCertificateRequest(TeaModel):
    def __init__(
        self,
        ca_sn: str = None,
        device_sn: str = None,
        mqtt_instance_id: str = None,
    ):
        # The serial number of the CA certificate to which the device certificate belongs. The serial number is the unique identifier of a CA certificate. CA certificates are used to validate device certificates.
        # 
        # The serial number of a CA certificate cannot exceed 128 bytes in size.
        # 
        # This parameter is required.
        self.ca_sn = ca_sn
        # The serial number of the device certificate whose registration information you want to delete. The serial number is the unique identifier of a device.
        # 
        # The serial number of a device certificate cannot exceed 128 bytes in size.
        # 
        # This parameter is required.
        self.device_sn = device_sn
        # The ID of the ApsaraMQ for MQTT instance to which the device certificate is bound.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        return self


class DeleteDeviceCertificateResponseBody(TeaModel):
    def __init__(
        self,
        device_sn: str = None,
        request_id: str = None,
    ):
        # The serial number of the device certificate whose registration information is deleted. The serial number is the unique identifier of a device certificate.
        self.device_sn = device_sn
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDeviceCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDeviceCertificateResponseBody = None,
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
            temp_model = DeleteDeviceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupIdRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the group that you want to delete.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the ApsaraMQ for MQTT instance from which you want to delete a group.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID. This parameter is a common parameter.
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


class DeleteGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGroupIdResponseBody = None,
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
            temp_model = DeleteGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisasterDowngradeRequest(TeaModel):
    def __init__(
        self,
        downgrade_instance_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance for which you want to downgrade the VIP access.
        # 
        # This parameter is required.
        self.downgrade_instance_id = downgrade_instance_id
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.downgrade_instance_id is not None:
            result['DowngradeInstanceId'] = self.downgrade_instance_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DowngradeInstanceId') is not None:
            self.downgrade_instance_id = m.get('DowngradeInstanceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisasterDowngradeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For information about error codes, see Error codes.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisasterDowngradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisasterDowngradeResponseBody = None,
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
            temp_model = DisasterDowngradeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisasterRecoveryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        recovery_instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.recovery_instance_id = recovery_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.recovery_instance_id is not None:
            result['RecoveryInstanceId'] = self.recovery_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RecoveryInstanceId') is not None:
            self.recovery_instance_id = m.get('RecoveryInstanceId')
        return self


class DisasterRecoveryResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisasterRecoveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisasterRecoveryResponseBody = None,
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
            temp_model = DisasterRecoveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCaCertificateRequest(TeaModel):
    def __init__(
        self,
        mqtt_instance_id: str = None,
        sn: str = None,
    ):
        # The instance ID bound to the CA certificate, which is the instance ID of the MQTT version of the cloud message queue.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # The SN serial number of the CA certificate to be queried, used to uniquely identify a CA certificate.
        # 
        # This parameter is required.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class GetCaCertificateResponseBodyData(TeaModel):
    def __init__(
        self,
        ca_content: str = None,
        ca_name: str = None,
        registration_code: str = None,
        sn: str = None,
        status: str = None,
        valid_begin: str = None,
        valid_end: str = None,
        verification_content: str = None,
    ):
        # Content of the CA certificate.
        # > \\n represents a new line.
        self.ca_content = ca_content
        # Name of the CA certificate
        self.ca_name = ca_name
        # Registration code of the CA certificate
        self.registration_code = registration_code
        # The SN serial number of the CA certificate, used to uniquely identify a CA certificate. Value range: no more than 128 bytes.
        self.sn = sn
        # The status of the CA certificate. The values are as follows:
        # - **0**: Indicates that the certificate is in an inactive state. - **1**: Indicates that the certificate is in an active state.
        # > After the CA certificate is registered, it is in an active state by default.
        self.status = status
        # The start time when the CA certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_begin = valid_begin
        # The end time when the CA certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_end = valid_end
        # Content of the Verification certificate.
        # > \\n represents a new line.
        self.verification_content = verification_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_content is not None:
            result['CaContent'] = self.ca_content
        if self.ca_name is not None:
            result['CaName'] = self.ca_name
        if self.registration_code is not None:
            result['RegistrationCode'] = self.registration_code
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin
        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end
        if self.verification_content is not None:
            result['VerificationContent'] = self.verification_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaContent') is not None:
            self.ca_content = m.get('CaContent')
        if m.get('CaName') is not None:
            self.ca_name = m.get('CaName')
        if m.get('RegistrationCode') is not None:
            self.registration_code = m.get('RegistrationCode')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')
        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')
        if m.get('VerificationContent') is not None:
            self.verification_content = m.get('VerificationContent')
        return self


class GetCaCertificateResponseBody(TeaModel):
    def __init__(
        self,
        data: GetCaCertificateResponseBodyData = None,
        request_id: str = None,
    ):
        # Certificate details.
        self.data = data
        # Public parameters, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetCaCertificateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCaCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCaCertificateResponseBody = None,
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
            temp_model = GetCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceCertificateRequest(TeaModel):
    def __init__(
        self,
        ca_sn: str = None,
        device_sn: str = None,
        mqtt_instance_id: str = None,
    ):
        # The SN serial number of the CA certificate to which the device certificate to be queried belongs, used to uniquely identify a CA certificate. Value range: no more than 128 bytes.
        # 
        # This parameter is required.
        self.ca_sn = ca_sn
        # The SN serial number of the device certificate to be queried, used to uniquely identify a device certificate. Value range: no more than 128 bytes.
        # 
        # This parameter is required.
        self.device_sn = device_sn
        # The instance ID to which the device certificate is bound, i.e., the instance ID of the Cloud Message Queue MQTT version.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        return self


class GetDeviceCertificateResponseBodyData(TeaModel):
    def __init__(
        self,
        ca_sn: str = None,
        device_content: str = None,
        device_name: str = None,
        device_sn: str = None,
        status: str = None,
        valid_begin: str = None,
        valid_end: str = None,
    ):
        # The SN serial number of the CA certificate to which the device certificate belongs, used to uniquely identify a CA certificate.
        self.ca_sn = ca_sn
        # Content of the device certificate.
        # 
        #  represents a new line.
        self.device_content = device_content
        # Name of the device certificate.
        self.device_name = device_name
        # The SN serial number of the device certificate, used to uniquely identify a device certificate.
        self.device_sn = device_sn
        # The status of the device certificate. The values are as follows:
        # - **0**: Indicates that the certificate is in an inactive state. - **1**: Indicates that the certificate is in an active state.
        # > After the device certificate is registered, it is in an active state by default.
        self.status = status
        # The start time when the device certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_begin = valid_begin
        # The end time when the device certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_end = valid_end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_content is not None:
            result['DeviceContent'] = self.device_content
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin
        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceContent') is not None:
            self.device_content = m.get('DeviceContent')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')
        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')
        return self


class GetDeviceCertificateResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDeviceCertificateResponseBodyData = None,
        request_id: str = None,
    ):
        # Certificate details.
        self.data = data
        # Public parameters, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDeviceCertificateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceCertificateResponseBody = None,
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
            temp_model = GetDeviceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceCredentialRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
    ):
        # The client ID of the device whose access credential you want to query.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDeviceCredentialResponseBodyDeviceCredential(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        create_time: int = None,
        device_access_key_id: str = None,
        device_access_key_secret: str = None,
        instance_id: str = None,
        update_time: int = None,
    ):
        # The client ID of the device.
        self.client_id = client_id
        # The timestamp that indicates when the access credential of the device was created. Unit: milliseconds.
        self.create_time = create_time
        # The AccessKey ID of the device.
        self.device_access_key_id = device_access_key_id
        # The AccessKey secret of the device.
        self.device_access_key_secret = device_access_key_secret
        # The ID of the ApsaraMQ for MQTT instance.
        self.instance_id = instance_id
        # The timestamp that indicates when the access credential of the device was last updated. The value of this parameter is a UNIX timestamp in milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.device_access_key_id is not None:
            result['DeviceAccessKeyId'] = self.device_access_key_id
        if self.device_access_key_secret is not None:
            result['DeviceAccessKeySecret'] = self.device_access_key_secret
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeviceAccessKeyId') is not None:
            self.device_access_key_id = m.get('DeviceAccessKeyId')
        if m.get('DeviceAccessKeySecret') is not None:
            self.device_access_key_secret = m.get('DeviceAccessKeySecret')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetDeviceCredentialResponseBody(TeaModel):
    def __init__(
        self,
        device_credential: GetDeviceCredentialResponseBodyDeviceCredential = None,
        request_id: str = None,
    ):
        # The information about the access credential of the device.
        self.device_credential = device_credential
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_credential is not None:
            result['DeviceCredential'] = self.device_credential.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCredential') is not None:
            temp_model = GetDeviceCredentialResponseBodyDeviceCredential()
            self.device_credential = temp_model.from_map(m['DeviceCredential'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceCredentialResponseBody = None,
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
            temp_model = GetDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisterCodeRequest(TeaModel):
    def __init__(
        self,
        mqtt_instance_id: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        return self


class GetRegisterCodeResponseBody(TeaModel):
    def __init__(
        self,
        register_code: str = None,
        request_id: str = None,
    ):
        # The registration code of the CA certificate.
        self.register_code = register_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRegisterCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRegisterCodeResponseBody = None,
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
            temp_model = GetRegisterCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InactivateCaCertificateRequest(TeaModel):
    def __init__(
        self,
        mqtt_instance_id: str = None,
        sn: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance to which the CA certificate is bound.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # The serial number of the CA certificate that you want to deregister. The serial number is the unique identifier of a CA certificate.
        # 
        # The serial number of a CA certificate cannot exceed 128 bytes in size.
        # 
        # This parameter is required.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class InactivateCaCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sn: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The serial number of the CA certificate that is deregistered. The serial number is the unique identifier of a CA certificate.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class InactivateCaCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InactivateCaCertificateResponseBody = None,
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
            temp_model = InactivateCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InactivateDeviceCertificateRequest(TeaModel):
    def __init__(
        self,
        ca_sn: str = None,
        device_sn: str = None,
        mqtt_instance_id: str = None,
    ):
        # The serial number of the CA certificate to which the device certificate that you want to deregister belongs. The serial number is the unique identifier of a CA certificate.
        # 
        # The serial number of a CA certificate cannot exceed 128 bytes in size.
        # 
        # This parameter is required.
        self.ca_sn = ca_sn
        # The serial number of the device certificate that you want to deregister. The serial number is the unique identifier of a device.
        # 
        # This parameter is required.
        self.device_sn = device_sn
        # The ID of the ApsaraMQ for MQTT instance to which the device certificate that you want to deregister is bound.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        return self


class InactivateDeviceCertificateResponseBody(TeaModel):
    def __init__(
        self,
        device_sn: str = None,
        request_id: str = None,
    ):
        # The serial number of the device certificate that is deregistered. The serial number is the unique identifier of a device certificate.
        self.device_sn = device_sn
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InactivateDeviceCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InactivateDeviceCertificateResponseBody = None,
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
            temp_model = InactivateDeviceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCaCertificateRequest(TeaModel):
    def __init__(
        self,
        mqtt_instance_id: str = None,
        page_no: str = None,
        page_size: str = None,
    ):
        # The instance ID of the Cloud Message Queue MQTT version, indicating which instance\\"s CA certificates need to be viewed.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # Indicates the page number of the returned results. The starting page is counted from 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The maximum number of query records to display per page. Value range: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCaCertificateResponseBodyDataCaCertificateVOS(TeaModel):
    def __init__(
        self,
        ca_content: str = None,
        ca_name: str = None,
        registration_code: str = None,
        sn: str = None,
        status: str = None,
        valid_begin: str = None,
        valid_end: str = None,
        verification_content: str = None,
    ):
        # Content of the CA certificate. 
        # > \\n represents a new line.
        self.ca_content = ca_content
        # Name of the CA certificate
        self.ca_name = ca_name
        # Registration code of the CA certificate
        self.registration_code = registration_code
        # SN serial number of the CA certificate
        self.sn = sn
        # The status of the CA certificate. The values are as follows:
        # - **0**: Indicates that the certificate is in an inactive state. - **1**: Indicates that the certificate is in an active state.
        # > After the CA certificate is registered, it is in an active state by default.
        self.status = status
        # The start time when the CA certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_begin = valid_begin
        # The end time when the CA certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_end = valid_end
        # Verify the content of the certificate. 
        # > \\n represents a new line.
        self.verification_content = verification_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_content is not None:
            result['CaContent'] = self.ca_content
        if self.ca_name is not None:
            result['CaName'] = self.ca_name
        if self.registration_code is not None:
            result['RegistrationCode'] = self.registration_code
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin
        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end
        if self.verification_content is not None:
            result['VerificationContent'] = self.verification_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaContent') is not None:
            self.ca_content = m.get('CaContent')
        if m.get('CaName') is not None:
            self.ca_name = m.get('CaName')
        if m.get('RegistrationCode') is not None:
            self.registration_code = m.get('RegistrationCode')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')
        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')
        if m.get('VerificationContent') is not None:
            self.verification_content = m.get('VerificationContent')
        return self


class ListCaCertificateResponseBodyData(TeaModel):
    def __init__(
        self,
        ca_certificate_vos: List[ListCaCertificateResponseBodyDataCaCertificateVOS] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # Details of the CA certificate
        self.ca_certificate_vos = ca_certificate_vos
        # The current page number of the returned query records.
        self.page_no = page_no
        # The maximum number of results to display per page.
        self.page_size = page_size
        # Maximum number of pages in the query result.
        self.total = total

    def validate(self):
        if self.ca_certificate_vos:
            for k in self.ca_certificate_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CaCertificateVOS'] = []
        if self.ca_certificate_vos is not None:
            for k in self.ca_certificate_vos:
                result['CaCertificateVOS'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ca_certificate_vos = []
        if m.get('CaCertificateVOS') is not None:
            for k in m.get('CaCertificateVOS'):
                temp_model = ListCaCertificateResponseBodyDataCaCertificateVOS()
                self.ca_certificate_vos.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListCaCertificateResponseBody(TeaModel):
    def __init__(
        self,
        data: ListCaCertificateResponseBodyData = None,
        request_id: str = None,
    ):
        # Query result.
        self.data = data
        # Public parameters, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListCaCertificateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCaCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCaCertificateResponseBody = None,
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
            temp_model = ListCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceCertificateRequest(TeaModel):
    def __init__(
        self,
        mqtt_instance_id: str = None,
        page_no: str = None,
        page_size: str = None,
    ):
        # The instance ID of the Cloud Message Queue MQTT version, indicating which instance\\"s device certificates need to be viewed.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # Indicates which page of the results to return. The starting page is counted from 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The maximum number of query records to display per page. Value range: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDeviceCertificateResponseBodyDataDeviceCertificateVOS(TeaModel):
    def __init__(
        self,
        ca_sn: str = None,
        device_content: str = None,
        device_name: str = None,
        device_sn: str = None,
        status: str = None,
        valid_begin: str = None,
        valid_end: str = None,
    ):
        # The SN serial number of the CA certificate to which the device certificate belongs, used to uniquely identify a CA certificate.
        self.ca_sn = ca_sn
        # Content of the device certificate.
        # 
        #  represents a new line.
        self.device_content = device_content
        # Name of the device certificate.
        self.device_name = device_name
        # The SN serial number of the device certificate, used to uniquely identify a device certificate.
        self.device_sn = device_sn
        # The status of the device certificate. The values are as follows:
        # - 0: indicates that the certificate is in an inactive state. - 1: indicates that the certificate is in an active state.
        # After the device certificate is registered, it defaults to the active state.
        self.status = status
        # The start time when the device certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_begin = valid_begin
        # The end time when the device certificate becomes effective. Formatted as a Unix timestamp in milliseconds.
        self.valid_end = valid_end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_content is not None:
            result['DeviceContent'] = self.device_content
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin
        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceContent') is not None:
            self.device_content = m.get('DeviceContent')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')
        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')
        return self


class ListDeviceCertificateResponseBodyData(TeaModel):
    def __init__(
        self,
        device_certificate_vos: List[ListDeviceCertificateResponseBodyDataDeviceCertificateVOS] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # Details of the device certificate.
        self.device_certificate_vos = device_certificate_vos
        # The current page number of the returned query records.
        self.page_no = page_no
        # The maximum number of results to display per page.
        self.page_size = page_size
        # Maximum number of pages in the query result.
        self.total = total

    def validate(self):
        if self.device_certificate_vos:
            for k in self.device_certificate_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceCertificateVOS'] = []
        if self.device_certificate_vos is not None:
            for k in self.device_certificate_vos:
                result['DeviceCertificateVOS'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_certificate_vos = []
        if m.get('DeviceCertificateVOS') is not None:
            for k in m.get('DeviceCertificateVOS'):
                temp_model = ListDeviceCertificateResponseBodyDataDeviceCertificateVOS()
                self.device_certificate_vos.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeviceCertificateResponseBody(TeaModel):
    def __init__(
        self,
        data: ListDeviceCertificateResponseBodyData = None,
        request_id: str = None,
    ):
        # Query result.
        self.data = data
        # Public parameters, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDeviceCertificateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeviceCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceCertificateResponseBody = None,
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
            temp_model = ListDeviceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceCertificateByCaSnRequest(TeaModel):
    def __init__(
        self,
        ca_sn: str = None,
        mqtt_instance_id: str = None,
        page_no: str = None,
        page_size: str = None,
    ):
        # The SN serial number of the CA certificate to be queried, indicating which CA certificate\\"s registered device certificates are to be retrieved.
        # 
        # This parameter is required.
        self.ca_sn = ca_sn
        # The instance ID bound to the CA certificate, which is the instance ID of the MQTT version of the cloud message queue.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # Indicates the page number of the returned results. The starting page is counted from 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The maximum number of query records to display per page. Value range: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDeviceCertificateByCaSnResponseBodyDataDeviceCertificateVOS(TeaModel):
    def __init__(
        self,
        ca_sn: str = None,
        device_content: str = None,
        device_name: str = None,
        device_sn: str = None,
        status: str = None,
        valid_begin: str = None,
        valid_end: str = None,
    ):
        # The SN serial number of the CA certificate to which the device certificate belongs, used to uniquely identify a CA certificate.
        self.ca_sn = ca_sn
        # Content of the device certificate.
        # 
        #  represents a new line.
        self.device_content = device_content
        # Name of the device certificate.
        self.device_name = device_name
        # The SN serial number of the device certificate, used to uniquely identify a device certificate.
        self.device_sn = device_sn
        # The status of the device certificate. The values are as follows:
        # - 0: indicates that the certificate is in an inactive state. 
        # - 1: indicates that the certificate is in an active state.
        # 
        # After the device certificate is registered, it is in an active state by default.
        self.status = status
        # The start time when the device certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_begin = valid_begin
        # The end time when the device certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_end = valid_end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_content is not None:
            result['DeviceContent'] = self.device_content
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin
        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceContent') is not None:
            self.device_content = m.get('DeviceContent')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')
        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')
        return self


class ListDeviceCertificateByCaSnResponseBodyData(TeaModel):
    def __init__(
        self,
        device_certificate_vos: List[ListDeviceCertificateByCaSnResponseBodyDataDeviceCertificateVOS] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # Details of the device certificate.
        self.device_certificate_vos = device_certificate_vos
        # The current page number of the returned query records.
        self.page_no = page_no
        # The maximum number of results to display per page.
        self.page_size = page_size
        # Total number of query results.
        self.total = total

    def validate(self):
        if self.device_certificate_vos:
            for k in self.device_certificate_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceCertificateVOS'] = []
        if self.device_certificate_vos is not None:
            for k in self.device_certificate_vos:
                result['DeviceCertificateVOS'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_certificate_vos = []
        if m.get('DeviceCertificateVOS') is not None:
            for k in m.get('DeviceCertificateVOS'):
                temp_model = ListDeviceCertificateByCaSnResponseBodyDataDeviceCertificateVOS()
                self.device_certificate_vos.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeviceCertificateByCaSnResponseBody(TeaModel):
    def __init__(
        self,
        data: ListDeviceCertificateByCaSnResponseBodyData = None,
        request_id: str = None,
    ):
        # Query result.
        self.data = data
        # Public parameters, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDeviceCertificateByCaSnResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeviceCertificateByCaSnResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceCertificateByCaSnResponseBody = None,
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
            temp_model = ListDeviceCertificateByCaSnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceCredentialClientIdRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        next_token: str = None,
        page_no: str = None,
        page_size: str = None,
    ):
        # Group ID of the MQTT version of the micro message queue.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the Cloud Message Queue MQTT version instance, which must match the actual instance ID used by the client. You can obtain this ID from the **Instance Details** page in the console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Token for starting the next page query.
        self.next_token = next_token
        # Indicates the page number of the returned results. The starting page is counted from 1.
        self.page_no = page_no
        # The maximum number of query records to display per page. 
        # Value range: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDeviceCredentialClientIdResponseBodyDeviceCredentialClientIdList(TeaModel):
    def __init__(
        self,
        client_id_list: List[str] = None,
        next_token: str = None,
        page_no: str = None,
        page_size: str = None,
        total: str = None,
    ):
        # Client list.
        self.client_id_list = client_id_list
        # Indicates whether there is a token (Token) for the next query. Values: 
        # - For the first query and when there is no next query, this field does not need to be filled. 
        # - If there is a next query, the value should be the NextToken returned from the previous API call.
        self.next_token = next_token
        # The current page number of the returned query records.
        self.page_no = page_no
        # The maximum number of results to display per page.
        self.page_size = page_size
        # Total number of query results.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id_list is not None:
            result['ClientIdList'] = self.client_id_list
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIdList') is not None:
            self.client_id_list = m.get('ClientIdList')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeviceCredentialClientIdResponseBody(TeaModel):
    def __init__(
        self,
        device_credential_client_id_list: ListDeviceCredentialClientIdResponseBodyDeviceCredentialClientIdList = None,
        request_id: str = None,
    ):
        # Returns the information list.
        self.device_credential_client_id_list = device_credential_client_id_list
        # Public parameters, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id

    def validate(self):
        if self.device_credential_client_id_list:
            self.device_credential_client_id_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_credential_client_id_list is not None:
            result['DeviceCredentialClientIdList'] = self.device_credential_client_id_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCredentialClientIdList') is not None:
            temp_model = ListDeviceCredentialClientIdResponseBodyDeviceCredentialClientIdList()
            self.device_credential_client_id_list = temp_model.from_map(m['DeviceCredentialClientIdList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeviceCredentialClientIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceCredentialClientIdResponseBody = None,
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
            temp_model = ListDeviceCredentialClientIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupIdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tags: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance whose groups you want to query.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListGroupIdResponseBodyDataTags(TeaModel):
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


class ListGroupIdResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        group_id: str = None,
        independent_naming: bool = None,
        instance_id: str = None,
        tags: List[ListGroupIdResponseBodyDataTags] = None,
        update_time: int = None,
    ):
        # The time when the group was created.
        self.create_time = create_time
        # The queried group that belongs to the ApsaraMQ for MQTT instance.
        self.group_id = group_id
        # Indicates whether a separate namespace is configured for the ApsaraMQ for MQTT instance. Valid values:
        # 
        # *   **true**: A separate namespace is configured for the ApsaraMQ for MQTT instance. Resource names must be unique within an ApsaraMQ for MQTT instance but can be the same across ApsaraMQ for MQTT instances.
        # *   **false**: No separate namespace is configured for the ApsaraMQ for MQTT instance. Resource names must be globally unique within an ApsaraMQ for MQTT instance and across ApsaraMQ for MQTT instances.
        self.independent_naming = independent_naming
        # The ID of the ApsaraMQ for MQTT instance to which the group belongs.
        self.instance_id = instance_id
        self.tags = tags
        # The time when the group was last updated.
        self.update_time = update_time

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListGroupIdResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListGroupIdResponseBodyData] = None,
        request_id: str = None,
    ):
        # The details of a queried group.
        self.data = data
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListGroupIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupIdResponseBody = None,
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
            temp_model = ListGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        tags: str = None,
    ):
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListInstancesResponseBodyInstancesMqttTags(TeaModel):
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


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: int = None,
        instance_type: int = None,
        kernel_version: str = None,
        mqtt_tags: List[ListInstancesResponseBodyInstancesMqttTags] = None,
        order_id: str = None,
        region_id: str = None,
        specific: str = None,
    ):
        self.create_time = create_time
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.kernel_version = kernel_version
        self.mqtt_tags = mqtt_tags
        self.order_id = order_id
        self.region_id = region_id
        self.specific = specific

    def validate(self):
        if self.mqtt_tags:
            for k in self.mqtt_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version
        result['MqttTags'] = []
        if self.mqtt_tags is not None:
            for k in self.mqtt_tags:
                result['MqttTags'].append(k.to_map() if k else None)
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.specific is not None:
            result['Specific'] = self.specific
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')
        self.mqtt_tags = []
        if m.get('MqttTags') is not None:
            for k in m.get('MqttTags'):
                temp_model = ListInstancesResponseBodyInstancesMqttTags()
                self.mqtt_tags.append(temp_model.from_map(k))
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Specific') is not None:
            self.specific = m.get('Specific')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instances: List[ListInstancesResponseBodyInstances] = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.instances = instances
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
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
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.code = code
        self.message = message
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
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


class QueryCustomAuthConnectBlackRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
        next_token: str = None,
        size: int = None,
    ):
        # The ID of the client to be queried.
        self.client_id = client_id
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token
        # The number of clients to be queried. Maximum value: 100.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class QueryCustomAuthConnectBlackResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        effect: str = None,
        permit_action: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # Indicates whether to allow or deny access.
        self.effect = effect
        # The authorized permissions.
        self.permit_action = permit_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.permit_action is not None:
            result['PermitAction'] = self.permit_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('PermitAction') is not None:
            self.permit_action = m.get('PermitAction')
        return self


class QueryCustomAuthConnectBlackResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        results: List[QueryCustomAuthConnectBlackResponseBodyDataResults] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The returned results.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = QueryCustomAuthConnectBlackResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        return self


class QueryCustomAuthConnectBlackResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryCustomAuthConnectBlackResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful. Other status codes indicate that the request failed. For a list of error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
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
            temp_model = QueryCustomAuthConnectBlackResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCustomAuthConnectBlackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCustomAuthConnectBlackResponseBody = None,
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
            temp_model = QueryCustomAuthConnectBlackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCustomAuthIdentityRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        identity_type: str = None,
        instance_id: str = None,
        next_token: str = None,
        size: int = None,
        username: str = None,
    ):
        # The client ID if you set IdentityType to CLIENT.
        self.client_id = client_id
        # The identity type.
        self.identity_type = identity_type
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token
        # The number of identities to be queried. Maximum value: 100.
        # 
        # This parameter is required.
        self.size = size
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.size is not None:
            result['Size'] = self.size
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class QueryCustomAuthIdentityResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        identity_type: str = None,
        secret: str = None,
        sign_mode: str = None,
        username: str = None,
    ):
        # The client ID if IdentityType is set to CLIENT.
        self.client_id = client_id
        # The identity type. Valid values:
        # 
        # *   USER
        # *   CLIENT
        self.identity_type = identity_type
        # The AccessKey secret.
        self.secret = secret
        # The signature verification mode. ORIGIN: compares the password and the AccessKey secret. SIGNED: uses the HMAC_SHA1 algorithm to sign the client ID to obtain a password and then compares the password.
        self.sign_mode = sign_mode
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class QueryCustomAuthIdentityResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        results: List[QueryCustomAuthIdentityResponseBodyDataResults] = None,
    ):
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The returned results.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = QueryCustomAuthIdentityResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        return self


class QueryCustomAuthIdentityResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryCustomAuthIdentityResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful. Other status codes indicate that the request failed. For a list of error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
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
            temp_model = QueryCustomAuthIdentityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCustomAuthIdentityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCustomAuthIdentityResponseBody = None,
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
            temp_model = QueryCustomAuthIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCustomAuthPermissionRequest(TeaModel):
    def __init__(
        self,
        identity: str = None,
        identity_type: str = None,
        instance_id: str = None,
        next_token: str = None,
        size: int = None,
        topic: str = None,
    ):
        # The username or client ID.
        self.identity = identity
        # The identity type.
        self.identity_type = identity_type
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token
        # The number of queries to be returned. Maximum value: 100.
        # 
        # This parameter is required.
        self.size = size
        # The topic whose authorization information you want to query. Multi-level topics and wildcard characters are supported.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.size is not None:
            result['Size'] = self.size
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class QueryCustomAuthPermissionResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        effect: str = None,
        identity: str = None,
        identity_type: str = None,
        permit_action: str = None,
        topic: str = None,
    ):
        # Indicates whether to allow or deny access.
        self.effect = effect
        # The username or client ID.
        self.identity = identity
        # The identity type. Valid values:
        # 
        # *   USER
        # *   CLIENT
        self.identity_type = identity_type
        # The authorized permissions.
        self.permit_action = permit_action
        # The topic name. Multi-level topics and wildcard characters are supported.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.permit_action is not None:
            result['PermitAction'] = self.permit_action
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('PermitAction') is not None:
            self.permit_action = m.get('PermitAction')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class QueryCustomAuthPermissionResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        results: List[QueryCustomAuthPermissionResponseBodyDataResults] = None,
    ):
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token
        # The response results.
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = QueryCustomAuthPermissionResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        return self


class QueryCustomAuthPermissionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryCustomAuthPermissionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
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
            temp_model = QueryCustomAuthPermissionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCustomAuthPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCustomAuthPermissionResponseBody = None,
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
            temp_model = QueryCustomAuthPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceDeviceRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        client_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        mqtt_region_id: str = None,
        page_size: int = None,
        reverse: bool = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The client ID of the device whose trace you want to query.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The number of the page to return. Pages start from page 1. If the input parameter value is greater than the total number of pages, the returned result is empty.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the ApsaraMQ for MQTT instance resides. For more information, see [Endpoints](https://help.aliyun.com/document_detail/181438.html).
        # 
        # This parameter is required.
        self.mqtt_region_id = mqtt_region_id
        # The number of entries to return on each page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Specifies whether the returned results are displayed in reverse chronological order. Valid values:
        # 
        # *   **true**: The returned results are displayed in reverse time order of actions on the device. This means that the information about the latest action on the device is displayed as the first entry and the information about the earliest action on the device is displayed as the last entry.
        # *   **false**: The returned results are displayed in time order of actions on the device. This means that the information about the earliest action on the device is displayed as the first entry and the information about the latest action on the device is displayed as the last entry.
        # 
        # If you do not specify this parameter, the returned results are displayed in time order of actions on the device by default.
        self.reverse = reverse

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class QueryMqttTraceDeviceResponseBodyDeviceInfoList(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_code: str = None,
        action_info: str = None,
        channel_id: str = None,
        time: str = None,
    ):
        # The action on the device. Valid values:
        # 
        # *   **connect**: The ApsaraMQ for MQTT client requests a connection to the ApsaraMQ for MQTT broker.
        # *   **close**: The TCP connection is closed.
        # *   **disconnect**: The ApsaraMQ for MQTT client requests a disconnection from the ApsaraMQ for MQTT broker.
        self.action = action
        # The returned code for the action on the device. Valid values:
        # 
        # *   **mqtt.trace.action.connect**: This value is returned if the value of Action is **connect**.
        # *   **mqtt.trace.action.close**: This value is returned if the value of Action is **close**.
        # *   **mqtt.trace.action.disconnect**: This value is returned if the value of Action is **disconnect**.
        self.action_code = action_code
        # The returned information for the action on the device. Valid values:
        # 
        # *   **accepted**: The ApsaraMQ for MQTT broker accepts the connection request from the ApsaraMQ for MQTT client.
        # *   **not authorized**: The TCP connection is closed because the permission verification of the client to access the instance fails.
        # *   **clientId conflict**: The TCP connection is closed due to a conflict in the ID of the ApsaraMQ for MQTT client.
        # *   **resource auth failed**: The TCP connection is closed because the permission verification for the ApsaraMQ for MQTT client to access the topic or group fails.
        # *   **no heart**: The TCP connection is closed because no heartbeat is detected on the client.
        # *   **closed by client**: The TCP connection is closed because an exception occurs on the client.
        # *   **disconnected by client**: The client requests a disconnection.
        # *   **invalid param**: The TCP connection is closed due to invalid request parameters.
        # *   **Socket IOException**: The TCP connection is closed due to network jitter or packet loss.
        self.action_info = action_info
        # The connection ID.
        self.channel_id = channel_id
        # The time when the action occurred on the device.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryMqttTraceDeviceResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        device_info_list: List[QueryMqttTraceDeviceResponseBodyDeviceInfoList] = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The details of the action on the device.
        self.device_info_list = device_info_list
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID. You can use the ID to troubleshoot issues. This parameter is a common parameter.
        self.request_id = request_id
        # The total number of returned actions on the device.
        self.total = total

    def validate(self):
        if self.device_info_list:
            for k in self.device_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['DeviceInfoList'] = []
        if self.device_info_list is not None:
            for k in self.device_info_list:
                result['DeviceInfoList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.device_info_list = []
        if m.get('DeviceInfoList') is not None:
            for k in m.get('DeviceInfoList'):
                temp_model = QueryMqttTraceDeviceResponseBodyDeviceInfoList()
                self.device_info_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryMqttTraceDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMqttTraceDeviceResponseBody = None,
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
            temp_model = QueryMqttTraceDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceMessageOfClientRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        client_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        mqtt_region_id: str = None,
        page_size: int = None,
        reverse: bool = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The client ID of the device whose messages you want to query.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The number of the page to return. Pages start from page 1. If the input parameter value is greater than the total number of pages, the returned result is empty.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section of the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the ApsaraMQ for MQTT instance resides. For more information, see [Endpoints](https://help.aliyun.com/document_detail/181438.html).
        # 
        # This parameter is required.
        self.mqtt_region_id = mqtt_region_id
        # The number of entries to return on each page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Specifies whether the returned results are displayed in reverse chronological order. Valid values:
        # 
        # *   **true**: The returned results are displayed in reverse order of the time when messages are sent or received. This means that the latest sent or received message is displayed as the first entry and the earliest sent or received message is displayed as the last entry.
        # *   **false**: The returned results are displayed in order of the time when messages are sent or received. This means that the earliest sent or received message is displayed as the first entry and the latest sent or received message is displayed as the last entry.
        # 
        # If this parameter is not specified, the returned results are displayed in order of the time when messages are sent or received.
        self.reverse = reverse

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_code: str = None,
        action_info: str = None,
        client_id: str = None,
        msg_id: str = None,
        time: str = None,
    ):
        # The action on the message. Valid values:
        # 
        # *   **pub_mqtt**: The ApsaraMQ for MQTT client sends the message.
        # *   **sub**: The ApsaraMQ for MQTT client subscribes to the message.
        # *   **push_offline**: The ApsaraMQ for MQTT broker pushes the offline message to the ApsaraMQ for MQTT client.
        self.action = action
        # The returned code for the action on the message. Valid values:
        # 
        # *   **mqtt.trace.action.msg.pub.mqtt**: This value is returned if the value of Action is **pub_mqtt**.
        # *   **mqtt.trace.action.msg.sub**: This value is returned if the value of Action is **sub**.
        # *   **mqtt.trace.action.msg.push.offline**: This value is returned if the value of Action is **push_offline**.
        self.action_code = action_code
        # The information returned for the action on the message. Valid values:
        # 
        # *   **Pub From Mqtt Client**: This value is returned if the value of Action is **pub_mqtt**.
        # *   **Push To Mqtt Client**: This value is returned if the value of Action is **sub**.
        # *   **Push Offline Msg To Mqtt Client**: This value is returned if the value of Action is **push_offline**.
        self.action_info = action_info
        # The client ID of the device.
        self.client_id = client_id
        # The message ID.
        self.msg_id = msg_id
        # The time when the message was sent or received.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryMqttTraceMessageOfClientResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        message_of_client_list: List[QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList] = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The returned messages.
        self.message_of_client_list = message_of_client_list
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID. You can use the ID to troubleshoot issues. This parameter is a common parameter.
        self.request_id = request_id
        # The total number of messages returned.
        self.total = total

    def validate(self):
        if self.message_of_client_list:
            for k in self.message_of_client_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['MessageOfClientList'] = []
        if self.message_of_client_list is not None:
            for k in self.message_of_client_list:
                result['MessageOfClientList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.message_of_client_list = []
        if m.get('MessageOfClientList') is not None:
            for k in m.get('MessageOfClientList'):
                temp_model = QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList()
                self.message_of_client_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryMqttTraceMessageOfClientResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMqttTraceMessageOfClientResponseBody = None,
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
            temp_model = QueryMqttTraceMessageOfClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceMessagePublishRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        instance_id: str = None,
        mqtt_region_id: str = None,
        msg_id: str = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the ApsaraMQ for MQTT instance resides. For more information, see [Endpoints](https://help.aliyun.com/document_detail/181438.html).
        # 
        # This parameter is required.
        self.mqtt_region_id = mqtt_region_id
        # The message ID.
        # 
        # This parameter is required.
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class QueryMqttTraceMessagePublishResponseBodyMessageTraceLists(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_code: str = None,
        action_info: str = None,
        client_id: str = None,
        msg_id: str = None,
        time: str = None,
    ):
        # The action on the message. Valid values:
        # 
        # *   **pub_mqtt**: indicates that the message was sent by an ApsaraMQ for MQTT client.
        # *   **pub_mq**: indicates that the message was sent by an ApsaraMQ for RocketMQ client.
        self.action = action
        # The returned code for the action on the message. Valid values:
        # 
        # *   **mqtt.trace.action.msg.pub.mqtt**: This value is returned if the value of Action is **pub_mqtt**.
        # *   **mqtt.trace.action.msg.pub.mq**: This value is returned if the value of Action is **pub_mq**.
        self.action_code = action_code
        # The returned information for the action on the message. Valid values:
        # 
        # *   **Pub From Mqtt Client**: This value is returned if the value of Action is **pub_mqtt**.
        # *   **Pub From MQ**: This value is returned if the value of Action is **pub_mq**.
        self.action_info = action_info
        # The ID of the client that sends the message.
        self.client_id = client_id
        # The message ID.
        self.msg_id = msg_id
        # The time when the message was sent.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryMqttTraceMessagePublishResponseBody(TeaModel):
    def __init__(
        self,
        message_trace_lists: List[QueryMqttTraceMessagePublishResponseBodyMessageTraceLists] = None,
        request_id: str = None,
    ):
        # The message traces.
        self.message_trace_lists = message_trace_lists
        # The request ID. You can use the ID to troubleshoot issues. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        if self.message_trace_lists:
            for k in self.message_trace_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MessageTraceLists'] = []
        if self.message_trace_lists is not None:
            for k in self.message_trace_lists:
                result['MessageTraceLists'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_trace_lists = []
        if m.get('MessageTraceLists') is not None:
            for k in m.get('MessageTraceLists'):
                temp_model = QueryMqttTraceMessagePublishResponseBodyMessageTraceLists()
                self.message_trace_lists.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryMqttTraceMessagePublishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMqttTraceMessagePublishResponseBody = None,
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
            temp_model = QueryMqttTraceMessagePublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceMessageSubscribeRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        client_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        mqtt_region_id: str = None,
        msg_id: str = None,
        page_size: int = None,
        reverse: bool = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The ID of the client that subscribes to the message. If you do not specify this parameter, the IDs of all clients that subscribe to the message are returned.
        self.client_id = client_id
        # The number of the page to return. Pages start from page 1. If the input parameter value is greater than the total number of pages, the returned result is empty.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section of the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the ApsaraMQ for MQTT instance resides. For more information, see [Endpoints](https://help.aliyun.com/document_detail/181438.html).
        # 
        # This parameter is required.
        self.mqtt_region_id = mqtt_region_id
        # The message ID.
        # 
        # This parameter is required.
        self.msg_id = msg_id
        # The number of entries to return on each page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Specifies whether the returned results are displayed in reverse chronological order. Valid values:
        # 
        # *   **true**: The returned results are displayed in reverse order of the time when messages are delivered. This means that the latest consumed message is displayed as the first entry and the earliest consumed message is displayed as the last entry.
        # *   **false**: The returned results are displayed in order of the time when messages are delivered. This means that the earliest consumed message is displayed as the first entry and the latest consumed message is displayed as the last entry.
        # 
        # If you do not specify this parameter, the returned results are displayed in order of time when messages are delivered.
        self.reverse = reverse

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_code: str = None,
        action_info: str = None,
        client_id: str = None,
        msg_id: str = None,
        time: str = None,
    ):
        # The action on the message. Valid values:
        # 
        # *   **sub**: The ApsaraMQ for MQTT client subscribes to the message.
        # *   **push_offline**: The ApsaraMQ for MQTT broker pushes the offline message to the ApsaraMQ for MQTT client.
        self.action = action
        # The code returned for the action on the message. Valid values:
        # 
        # *   **mqtt.trace.action.msg.sub**: The value that is returned if the value of Action is **sub**.
        # *   **mqtt.trace.action.msg.push.offline**: The value that is returned if the value of Action is **push_offline**.
        self.action_code = action_code
        # The returned information for the action on the message. Valid values:
        # 
        # *   **Push To Mqtt Client**: The value that is returned if the value of Action is **sub**.
        # *   **Push Offline Msg To Mqtt Client**: The value that is returned if the value of Action is **push_offline**.
        self.action_info = action_info
        # The ID of the client that subscribes to the message.
        self.client_id = client_id
        # The message ID.
        self.msg_id = msg_id
        # The time when the message was delivered.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryMqttTraceMessageSubscribeResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        message_trace_lists: List[QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists] = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The delivery trace of the queried message.
        self.message_trace_lists = message_trace_lists
        # The number of entries returned per page.
        self.page_size = page_size
        # The unique ID that the system generates for the request. You can use the ID to troubleshoot issues. This parameter is a common parameter.
        self.request_id = request_id
        # The returned delivery traces.
        self.total = total

    def validate(self):
        if self.message_trace_lists:
            for k in self.message_trace_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['MessageTraceLists'] = []
        if self.message_trace_lists is not None:
            for k in self.message_trace_lists:
                result['MessageTraceLists'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.message_trace_lists = []
        if m.get('MessageTraceLists') is not None:
            for k in m.get('MessageTraceLists'):
                temp_model = QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists()
                self.message_trace_lists.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryMqttTraceMessageSubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMqttTraceMessageSubscribeResponseBody = None,
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
            temp_model = QueryMqttTraceMessageSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySessionByClientIdRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT client that you want to query.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com).
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QuerySessionByClientIdResponseBody(TeaModel):
    def __init__(
        self,
        online_status: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the ApsaraMQ for MQTT client is connected to the ApsaraMQ for MQTT broker. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.online_status = online_status
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QuerySessionByClientIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySessionByClientIdResponseBody = None,
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
            temp_model = QuerySessionByClientIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTokenRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        token: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com/).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token that you want to query.
        # 
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class QueryTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token_status: bool = None,
    ):
        # The unique ID that the system generates for the request. This parameter is a common parameter.
        self.request_id = request_id
        # The status of the queried token. Valid values:
        # 
        # *   **true**: indicates the token is valid.
        # *   **false**: indicates the token is invalid.
        self.token_status = token_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token_status is not None:
            result['TokenStatus'] = self.token_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TokenStatus') is not None:
            self.token_status = m.get('TokenStatus')
        return self


class QueryTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTokenResponseBody = None,
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
            temp_model = QueryTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshDeviceCredentialRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
    ):
        # The client ID of the device whose access credential you want to update.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RefreshDeviceCredentialResponseBodyDeviceCredential(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        create_time: int = None,
        device_access_key_id: str = None,
        device_access_key_secret: str = None,
        instance_id: str = None,
        update_time: int = None,
    ):
        # The client ID of the device.
        self.client_id = client_id
        # The timestamp that indicates when the access credential of the device was created. The value of this parameter is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The AccessKey ID of the device.
        self.device_access_key_id = device_access_key_id
        # The AccessKey secret of the device.
        self.device_access_key_secret = device_access_key_secret
        # The ID of the ApsaraMQ for MQTT instance.
        self.instance_id = instance_id
        # The timestamp that indicates when the access credential of the device was last updated. The value of this parameter is a UNIX timestamp in milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.device_access_key_id is not None:
            result['DeviceAccessKeyId'] = self.device_access_key_id
        if self.device_access_key_secret is not None:
            result['DeviceAccessKeySecret'] = self.device_access_key_secret
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeviceAccessKeyId') is not None:
            self.device_access_key_id = m.get('DeviceAccessKeyId')
        if m.get('DeviceAccessKeySecret') is not None:
            self.device_access_key_secret = m.get('DeviceAccessKeySecret')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class RefreshDeviceCredentialResponseBody(TeaModel):
    def __init__(
        self,
        device_credential: RefreshDeviceCredentialResponseBodyDeviceCredential = None,
        request_id: str = None,
    ):
        # The access credential of the device.
        self.device_credential = device_credential
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_credential is not None:
            result['DeviceCredential'] = self.device_credential.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCredential') is not None:
            temp_model = RefreshDeviceCredentialResponseBodyDeviceCredential()
            self.device_credential = temp_model.from_map(m['DeviceCredential'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshDeviceCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshDeviceCredentialResponseBody = None,
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
            temp_model = RefreshDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterCaCertificateRequest(TeaModel):
    def __init__(
        self,
        ca_content: str = None,
        ca_name: str = None,
        mqtt_instance_id: str = None,
        verification_content: str = None,
    ):
        # The content of the CA certificate that you want to register with an ApsaraMQ for MQTT broker.
        # 
        # 
        # > In the example, \\n indicates a line feed.
        # 
        # This parameter is required.
        self.ca_content = ca_content
        # The name of the CA certificate that you want to register with an ApsaraMQ for MQTT broker.
        # 
        # This parameter is required.
        self.ca_name = ca_name
        # The ID of the ApsaraMQ for MQTT instance to which you want to bind the CA certificate.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # The content of the validation certificate issued by the CA certificate that you want to register with an ApsaraMQ for MQTT broker. The validation certificate must be used together with the registration code of the CA certificate to verify the private key of the CA certificate.
        # > In the example, \\n indicates a line feed.
        # 
        # This parameter is required.
        self.verification_content = verification_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_content is not None:
            result['CaContent'] = self.ca_content
        if self.ca_name is not None:
            result['CaName'] = self.ca_name
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.verification_content is not None:
            result['VerificationContent'] = self.verification_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaContent') is not None:
            self.ca_content = m.get('CaContent')
        if m.get('CaName') is not None:
            self.ca_name = m.get('CaName')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('VerificationContent') is not None:
            self.verification_content = m.get('VerificationContent')
        return self


class RegisterCaCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sn: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The serial number of the registered CA certificate. The serial number is the unique identifier of a CA certificate.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class RegisterCaCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterCaCertificateResponseBody = None,
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
            temp_model = RegisterCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDeviceCredentialRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
    ):
        # The client ID of the device for which you want to create an access credential.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RegisterDeviceCredentialResponseBodyDeviceCredential(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        create_time: int = None,
        device_access_key_id: str = None,
        device_access_key_secret: str = None,
        instance_id: str = None,
        update_time: int = None,
    ):
        # The client ID of the device.
        self.client_id = client_id
        # The timestamp that indicates when the access credential of the device was created. Unit: milliseconds.
        self.create_time = create_time
        # The AccessKey ID of the device.
        self.device_access_key_id = device_access_key_id
        # The AccessKey secret of the device.
        self.device_access_key_secret = device_access_key_secret
        # The ID of the ApsaraMQ for MQTT instance.
        self.instance_id = instance_id
        # The timestamp that indicates when the access credential of the device was last updated. Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.device_access_key_id is not None:
            result['DeviceAccessKeyId'] = self.device_access_key_id
        if self.device_access_key_secret is not None:
            result['DeviceAccessKeySecret'] = self.device_access_key_secret
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeviceAccessKeyId') is not None:
            self.device_access_key_id = m.get('DeviceAccessKeyId')
        if m.get('DeviceAccessKeySecret') is not None:
            self.device_access_key_secret = m.get('DeviceAccessKeySecret')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class RegisterDeviceCredentialResponseBody(TeaModel):
    def __init__(
        self,
        device_credential: RegisterDeviceCredentialResponseBodyDeviceCredential = None,
        request_id: str = None,
    ):
        # The access credential of the device.
        self.device_credential = device_credential
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_credential is not None:
            result['DeviceCredential'] = self.device_credential.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCredential') is not None:
            temp_model = RegisterDeviceCredentialResponseBodyDeviceCredential()
            self.device_credential = temp_model.from_map(m['DeviceCredential'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterDeviceCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterDeviceCredentialResponseBody = None,
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
            temp_model = RegisterDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeTokenRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        token: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com/).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token that you want to revoke.
        # 
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class RevokeTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID. This parameter is a common parameter.
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


class RevokeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeTokenResponseBody = None,
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
            temp_model = RevokeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        mqtt_topic: str = None,
        payload: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The topic to which you want to send a message on the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.mqtt_topic = mqtt_topic
        # The message content, which is the payload of the message. We recommend that you encode the content in Base64 to prevent non-printable characters from being transmitted.
        # 
        # This parameter is required.
        self.payload = payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mqtt_topic is not None:
            result['MqttTopic'] = self.mqtt_topic
        if self.payload is not None:
            result['Payload'] = self.payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MqttTopic') is not None:
            self.mqtt_topic = m.get('MqttTopic')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
        request_id: str = None,
    ):
        # The unique message ID that is returned by the ApsaraMQ for MQTT broker after the message is sent.
        self.msg_id = msg_id
        # The unique ID that the system generates for the request. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageResponseBody = None,
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSniConfigRequest(TeaModel):
    def __init__(
        self,
        default_certificate: str = None,
        mqtt_instance_id: str = None,
        sni_config: str = None,
    ):
        # The default certificate. If the domain name that you access cannot match the certificates of the broker, the default certificate is returned.
        # 
        # This parameter is required.
        self.default_certificate = default_certificate
        # The instance ID.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # The Server Name Indication (SNI) configuration. This parameter is used to map domain names and certificates. Format: Domain name#Certificate ID#Password (if available);Domain name#Certificate ID#Password (if available).
        self.sni_config = sni_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_certificate is not None:
            result['DefaultCertificate'] = self.default_certificate
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.sni_config is not None:
            result['SniConfig'] = self.sni_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCertificate') is not None:
            self.default_certificate = m.get('DefaultCertificate')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('SniConfig') is not None:
            self.sni_config = m.get('SniConfig')
        return self


class SetSniConfigResponseBodyAccessDeniedDetail(TeaModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        self.auth_action = auth_action
        self.auth_principal_display_name = auth_principal_display_name
        self.auth_principal_owner_id = auth_principal_owner_id
        self.auth_principal_type = auth_principal_type
        self.encoded_diagnostic_message = encoded_diagnostic_message
        self.no_permission_type = no_permission_type
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action
        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name
        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id
        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type
        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message
        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')
        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')
        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')
        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')
        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')
        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class SetSniConfigResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: SetSniConfigResponseBodyAccessDeniedDetail = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The request ID.
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = SetSniConfigResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetSniConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSniConfigResponseBody = None,
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
            temp_model = SetSniConfigResponseBody()
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
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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
        # Id of the request
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


class UnRegisterDeviceCredentialRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
    ):
        # The client ID of the device whose access credential you want to deregister.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UnRegisterDeviceCredentialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The unique ID that the system generates for the request. This parameter is a common parameter.
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


class UnRegisterDeviceCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnRegisterDeviceCredentialResponseBody = None,
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
            temp_model = UnRegisterDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
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
        # Id of the request
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


class UpdateCustomAuthIdentityRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        identity_type: str = None,
        instance_id: str = None,
        secret: str = None,
        sign_mode: str = None,
        username: str = None,
    ):
        # The client ID if you set IdentityType to CLIENT.
        self.client_id = client_id
        # The identity type. Valid values:
        # 
        # *   USER
        # *   CLIENT
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The AccessKey secret.
        # 
        # This parameter is required.
        self.secret = secret
        # The signature verification mode. ORIGIN: compares the password and the AccessKey secret. SIGNED: uses the HMAC_SHA1 algorithm to sign the client ID to obtain a password and then compares the password.
        # 
        # This parameter is required.
        self.sign_mode = sign_mode
        # The username. The value cannot exceed 64 characters in length.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateCustomAuthIdentityResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
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


class UpdateCustomAuthIdentityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomAuthIdentityResponseBody = None,
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
            temp_model = UpdateCustomAuthIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomAuthPermissionRequest(TeaModel):
    def __init__(
        self,
        effect: str = None,
        identity: str = None,
        identity_type: str = None,
        instance_id: str = None,
        permit_action: str = None,
        topic: str = None,
    ):
        # Specifies whether to allow or deny access.
        # 
        # This parameter is required.
        self.effect = effect
        # Username or Client ID.
        # 
        # This parameter is required.
        self.identity = identity
        # The identity type. Valid values:
        # 
        # *   USER
        # *   CLIENT
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # ID of the Cloud Message Queue MQTT version instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The permissions that you want to grant.
        # 
        # This parameter is required.
        self.permit_action = permit_action
        # Authorized Topic, supporting multi-level MQTT topics and wildcards.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.permit_action is not None:
            result['PermitAction'] = self.permit_action
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PermitAction') is not None:
            self.permit_action = m.get('PermitAction')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateCustomAuthPermissionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code returned upon failed invocation. For more information, see Error Codes.
        self.code = code
        # Information
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful. true: Call succeeded. false: Call failed.
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


class UpdateCustomAuthPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomAuthPermissionResponseBody = None,
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
            temp_model = UpdateCustomAuthPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



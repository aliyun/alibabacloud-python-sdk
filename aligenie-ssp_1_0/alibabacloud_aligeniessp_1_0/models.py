# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetDeviceBasicInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetDeviceBasicInfoRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，此处填写天猫精灵AI平台中，该产品ProductKey所在项目的Project ID。
        self.encode_key = encode_key
        # 编码类型，此处填写“PROJECT_ID”
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型  - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetDeviceBasicInfoRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceBasicInfoRequestDeviceInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceBasicInfoRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetDeviceBasicInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetDeviceBasicInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        firmware_version: str = None,
        name: str = None,
    ):
        # 固件版本
        self.firmware_version = firmware_version
        # 设备名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetDeviceBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetDeviceBasicInfoResponseBodyResult = None,
    ):
        # 返回的错误码
        self.code = code
        # 返回的错误信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 返回result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
            result['Result'] = self.result.to_map()
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
            temp_model = GetDeviceBasicInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceBasicInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceIdByIdentityHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetDeviceIdByIdentityRequest(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        identity_id: str = None,
        identity_type: str = None,
        product_key: str = None,
    ):
        # 编码类型对应的值，此处填写天猫精灵AI平台中，该产品ProductKey所在项目的Project ID。
        self.encode_key = encode_key
        # 编码类型，此处填写“PROJECT_ID”
        self.encode_type = encode_type
        # 认证标识，填写MAC地址或者SN的值。
        self.identity_id = identity_id
        # 填写设备认证类型，“MAC”或者“SN”
        self.identity_type = identity_type
        # 产品唯一标志符productKey，在天猫精灵AI平台中创建产品时，平台颁发的全局唯一标识。
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds(TeaModel):
    def __init__(
        self,
        device_union_id: str = None,
        organization_id: str = None,
    ):
        # 组织id对应的归一id
        self.device_union_id = device_union_id
        # 组织id
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetDeviceIdByIdentityResponseBodyResult(TeaModel):
    def __init__(
        self,
        device_open_id: str = None,
        device_union_ids: List[GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds] = None,
    ):
        # 设备信息对应的openId
        self.device_open_id = device_open_id
        # 组织id及归一id列表
        self.device_union_ids = device_union_ids

    def validate(self):
        if self.device_union_ids:
            for k in self.device_union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        return self


class GetDeviceIdByIdentityResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetDeviceIdByIdentityResponseBodyResult = None,
    ):
        # 返回的错误码
        self.code = code
        # 返回的错误信息
        self.message = message
        # 请求ID，用于排查问题，如果没有这个参数，可以在responseHeader里进行排查。
        self.request_id = request_id
        # 返回result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
            result['Result'] = self.result.to_map()
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
            temp_model = GetDeviceIdByIdentityResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceIdByIdentityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceIdByIdentityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceIdByIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceStatusInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetDeviceStatusInfoRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，此处填写天猫精灵AI平台中，该产品ProductKey所在项目的Project ID。
        self.encode_key = encode_key
        # 编码类型，此处填写“PROJECT_ID”
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型  - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetDeviceStatusInfoRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceStatusInfoRequestDeviceInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceStatusInfoRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetDeviceStatusInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetDeviceStatusInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        online: int = None,
    ):
        # 是否在线，0为不在线，1为在线
        self.online = online

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online is not None:
            result['Online'] = self.online
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Online') is not None:
            self.online = m.get('Online')
        return self


class GetDeviceStatusInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetDeviceStatusInfoResponseBodyResult = None,
    ):
        # 返回的错误码
        self.code = code
        # 返回的错误信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 返回result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
            result['Result'] = self.result.to_map()
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
            temp_model = GetDeviceStatusInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceStatusInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceStatusInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceStatusInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserByDeviceIdHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetUserByDeviceIdRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，此处填写天猫精灵AI平台中，该产品ProductKey所在项目的Project ID。
        self.encode_key = encode_key
        # 编码类型，此处填写“PROJECT_ID”
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型  - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetUserByDeviceIdRequest(TeaModel):
    def __init__(
        self,
        device_info: GetUserByDeviceIdRequestDeviceInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetUserByDeviceIdRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetUserByDeviceIdShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetUserByDeviceIdResponseBodyResultUserUnionIds(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        user_union_id: str = None,
    ):
        # 组织id
        self.organization_id = organization_id
        # 组织id对应的归一id
        self.user_union_id = user_union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.user_union_id is not None:
            result['UserUnionId'] = self.user_union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('UserUnionId') is not None:
            self.user_union_id = m.get('UserUnionId')
        return self


class GetUserByDeviceIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        user_open_id: str = None,
        user_union_ids: List[GetUserByDeviceIdResponseBodyResultUserUnionIds] = None,
    ):
        # 用户信息对应的openId
        self.user_open_id = user_open_id
        # 组织id及归一id列表
        self.user_union_ids = user_union_ids

    def validate(self):
        if self.user_union_ids:
            for k in self.user_union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        result['UserUnionIds'] = []
        if self.user_union_ids is not None:
            for k in self.user_union_ids:
                result['UserUnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        self.user_union_ids = []
        if m.get('UserUnionIds') is not None:
            for k in m.get('UserUnionIds'):
                temp_model = GetUserByDeviceIdResponseBodyResultUserUnionIds()
                self.user_union_ids.append(temp_model.from_map(k))
        return self


class GetUserByDeviceIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetUserByDeviceIdResponseBodyResult = None,
    ):
        # 返回的错误码
        self.code = code
        # 返回的错误信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 用户open信息
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
            result['Result'] = self.result.to_map()
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
            temp_model = GetUserByDeviceIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetUserByDeviceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserByDeviceIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserByDeviceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceBasicInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListDeviceBasicInfoRequestDeviceInfos(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id_type: str = None,
        ids: List[str] = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，此处填写天猫精灵AI平台中，该产品ProductKey所在项目的Project ID。
        self.encode_key = encode_key
        # 编码类型，此处填写“PROJECT_ID”
        self.encode_type = encode_type
        # 设备Id的类型  - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在开放平台申请过组织后才会有
        self.id_type = id_type
        # 设备标识列表（deviceOpenId或deviceUnionId）
        self.ids = ids
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListDeviceBasicInfoRequest(TeaModel):
    def __init__(
        self,
        device_infos: ListDeviceBasicInfoRequestDeviceInfos = None,
    ):
        # 设备标识信息
        self.device_infos = device_infos

    def validate(self):
        if self.device_infos:
            self.device_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_infos is not None:
            result['DeviceInfos'] = self.device_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfos') is not None:
            temp_model = ListDeviceBasicInfoRequestDeviceInfos()
            self.device_infos = temp_model.from_map(m['DeviceInfos'])
        return self


class ListDeviceBasicInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        device_infos_shrink: str = None,
    ):
        # 设备标识信息
        self.device_infos_shrink = device_infos_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_infos_shrink is not None:
            result['DeviceInfos'] = self.device_infos_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfos') is not None:
            self.device_infos_shrink = m.get('DeviceInfos')
        return self


class ResultValueDeviceUnionIds(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        device_union_id: str = None,
    ):
        # 组织id，
        self.organization_id = organization_id
        # 组织id对应的归一id
        self.device_union_id = device_union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')
        return self


class ResultValue(TeaModel):
    def __init__(
        self,
        device_open_id: str = None,
        device_union_ids: List[ResultValueDeviceUnionIds] = None,
        name: str = None,
        firmware_version: str = None,
    ):
        # 设备信息对应的openId
        self.device_open_id = device_open_id
        # 组织id及归一id列表
        self.device_union_ids = device_union_ids
        # 设备名称
        self.name = name
        # 固件版本
        self.firmware_version = firmware_version

    def validate(self):
        if self.device_union_ids:
            for k in self.device_union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = ResultValueDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        return self


class ListDeviceBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, ResultValue] = None,
    ):
        # 返回的错误码
        self.code = code
        # 返回的错误信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 返回result，key为deviceOpenId或deviceUnionId，value为对应的设备信息
        self.result = result

    def validate(self):
        if self.result:
            for v in self.result.values():
                if v:
                    v.validate()

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
        result['Result'] = {}
        if self.result is not None:
            for k, v in self.result.items():
                result['Result'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = {}
        if m.get('Result') is not None:
            for k, v in m.get('Result').items():
                temp_model = ResultValue()
                self.result[k] = temp_model.from_map(v)
        return self


class ListDeviceBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceBasicInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeviceBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceByUserIdHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListDeviceByUserIdRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，此处填写天猫精灵AI平台中，该产品ProductKey所在项目的Project ID。
        self.encode_key = encode_key
        # 编码类型，此处填写“PROJECT_ID”
        self.encode_type = encode_type
        # 用户标识（userOpenId或userUnionId）
        self.id = id
        # 用户Id的类型  - OPEN_ID：默认的用户ID标识 - UNION_ID: 组织维度的用户ID标识，在开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListDeviceByUserIdRequest(TeaModel):
    def __init__(
        self,
        user_info: ListDeviceByUserIdRequestUserInfo = None,
    ):
        # 用户标识信息
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = ListDeviceByUserIdRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListDeviceByUserIdShrinkRequest(TeaModel):
    def __init__(
        self,
        user_info_shrink: str = None,
    ):
        # 用户标识信息
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListDeviceByUserIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, ResultValue] = None,
    ):
        # 返回的错误码
        self.code = code
        # 返回的错误信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 返回result
        self.result = result

    def validate(self):
        if self.result:
            for v in self.result.values():
                if v:
                    v.validate()

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
        result['Result'] = {}
        if self.result is not None:
            for k, v in self.result.items():
                result['Result'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = {}
        if m.get('Result') is not None:
            for k, v in m.get('Result').items():
                temp_model = ResultValue()
                self.result[k] = temp_model.from_map(v)
        return self


class ListDeviceByUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceByUserIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeviceByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceIdByIdentitysHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListDeviceIdByIdentitysRequest(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        identity_ids: List[str] = None,
        identity_type: str = None,
        product_key: str = None,
    ):
        # 编码类型对应的值，此处填写天猫精灵AI平台中，该产品ProductKey所在项目的Project ID。
        self.encode_key = encode_key
        # 编码类型，此处填写“PROJECT_ID”
        self.encode_type = encode_type
        self.identity_ids = identity_ids
        # 填写设备认证类型，“MAC”或者“SN”
        self.identity_type = identity_type
        # 产品唯一标志符productKey，在天猫精灵AI平台中创建产品时，平台颁发的全局唯一标识。
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.identity_ids is not None:
            result['IdentityIds'] = self.identity_ids
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdentityIds') is not None:
            self.identity_ids = m.get('IdentityIds')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ListDeviceIdByIdentitysShrinkRequest(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        identity_ids_shrink: str = None,
        identity_type: str = None,
        product_key: str = None,
    ):
        # 编码类型对应的值，此处填写天猫精灵AI平台中，该产品ProductKey所在项目的Project ID。
        self.encode_key = encode_key
        # 编码类型，此处填写“PROJECT_ID”
        self.encode_type = encode_type
        self.identity_ids_shrink = identity_ids_shrink
        # 填写设备认证类型，“MAC”或者“SN”
        self.identity_type = identity_type
        # 产品唯一标志符productKey，在天猫精灵AI平台中创建产品时，平台颁发的全局唯一标识。
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.identity_ids_shrink is not None:
            result['IdentityIds'] = self.identity_ids_shrink
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdentityIds') is not None:
            self.identity_ids_shrink = m.get('IdentityIds')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ListDeviceIdByIdentitysResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, ResultValue] = None,
    ):
        # 返回的错误码
        self.code = code
        # 返回的错误信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 返回result
        self.result = result

    def validate(self):
        if self.result:
            for v in self.result.values():
                if v:
                    v.validate()

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
        result['Result'] = {}
        if self.result is not None:
            for k, v in self.result.items():
                result['Result'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = {}
        if m.get('Result') is not None:
            for k, v in m.get('Result').items():
                temp_model = ResultValue()
                self.result[k] = temp_model.from_map(v)
        return self


class ListDeviceIdByIdentitysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceIdByIdentitysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeviceIdByIdentitysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDeviceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UnbindDeviceRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，此处填写天猫精灵AI平台中，该产品ProductKey所在项目的Project ID。
        self.encode_key = encode_key
        # 编码类型，此处填写“PROJECT_ID”
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型  - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UnbindDeviceRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，此处填写天猫精灵AI平台中，该产品ProductKey所在项目的Project ID。
        self.encode_key = encode_key
        # 编码类型，此处填写“PROJECT_ID”
        self.encode_type = encode_type
        # 用户标识（userOpenId或userUnionId）
        self.id = id
        # 用户Id的类型  - OPEN_ID：默认的用户ID标识 - UNION_ID: 组织维度的用户ID标识，在开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UnbindDeviceRequest(TeaModel):
    def __init__(
        self,
        device_info: UnbindDeviceRequestDeviceInfo = None,
        user_info: UnbindDeviceRequestUserInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info
        # 用户标识信息
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = UnbindDeviceRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = UnbindDeviceRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class UnbindDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink
        # 用户标识信息
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class UnbindDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        # 返回的错误码
        self.code = code
        # 返回的错误信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 是否解绑成功
        self.result = result

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
        return self


class UnbindDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



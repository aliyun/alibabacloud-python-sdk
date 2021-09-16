# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


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
        identity_type: str = None,
        encode_type: str = None,
        identity_id: str = None,
        product_key: str = None,
        encode_key: str = None,
    ):
        # 认证类型，MAC/SN
        self.identity_type = identity_type
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型： PACKAGE_NAME：apk包名 SKILL_ID：技能id
        self.encode_type = encode_type
        # 认证标识，具体的MAC地址或者SN号
        self.identity_id = identity_id
        # 产品唯一标志符productKey，从AI开放平台中获取
        self.product_key = product_key
        # 编码类型对应的值，例如：编码类型是SKILLID，其值就为webhook服务中得到的skillId；编码类似是PACKAGENAME，其值就为对应客户端app的packageName。
        self.encode_key = encode_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        return self


class GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds(TeaModel):
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
        message: str = None,
        code: int = None,
        result: GetDeviceIdByIdentityResponseBodyResult = None,
        request_id: str = None,
    ):
        # 返回的错误信息
        self.message = message
        # 返回的错误码
        self.code = code
        # 返回result
        self.result = result
        # 请求id
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Result') is not None:
            temp_model = GetDeviceIdByIdentityResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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



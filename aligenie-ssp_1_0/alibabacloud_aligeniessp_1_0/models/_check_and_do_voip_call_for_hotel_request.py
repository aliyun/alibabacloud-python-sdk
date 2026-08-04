# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class CheckAndDoVoipCallForHotelRequest(DaraModel):
    def __init__(
        self,
        biz_data: str = None,
        callee_nick: str = None,
        callee_phone_num: str = None,
        device_info: main_models.CheckAndDoVoipCallForHotelRequestDeviceInfo = None,
        user_info: main_models.CheckAndDoVoipCallForHotelRequestUserInfo = None,
    ):
        self.biz_data = biz_data
        self.callee_nick = callee_nick
        self.callee_phone_num = callee_phone_num
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_data is not None:
            result['BizData'] = self.biz_data

        if self.callee_nick is not None:
            result['CalleeNick'] = self.callee_nick

        if self.callee_phone_num is not None:
            result['CalleePhoneNum'] = self.callee_phone_num

        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')

        if m.get('CalleeNick') is not None:
            self.callee_nick = m.get('CalleeNick')

        if m.get('CalleePhoneNum') is not None:
            self.callee_phone_num = m.get('CalleePhoneNum')

        if m.get('DeviceInfo') is not None:
            temp_model = main_models.CheckAndDoVoipCallForHotelRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.CheckAndDoVoipCallForHotelRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class CheckAndDoVoipCallForHotelRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CheckAndDoVoipCallForHotelRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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


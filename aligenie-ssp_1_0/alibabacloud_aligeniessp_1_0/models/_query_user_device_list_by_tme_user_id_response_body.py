# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class QueryUserDeviceListByTmeUserIdResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.QueryUserDeviceListByTmeUserIdResponseBodyResult = None,
        success: bool = None,
    ):
        # Response code
        self.code = code
        # Response message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Response Result
        self.result = result
        # Flag indicating whether the invocation succeeded
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

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
            temp_model = main_models.QueryUserDeviceListByTmeUserIdResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryUserDeviceListByTmeUserIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        aligenie_user_info_list: List[main_models.QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoList] = None,
        encode_key: str = None,
        encode_type: str = None,
        sp: str = None,
    ):
        # Tmall Genie User List
        self.aligenie_user_info_list = aligenie_user_info_list
        # entity key (pass-through by third party)
        self.encode_key = encode_key
        # entity Type (pass-through by third party)
        self.encode_type = encode_type
        # "KG": KuGou  
        # "KW": Kuwo  
        # "QM": QQ Music
        self.sp = sp

    def validate(self):
        if self.aligenie_user_info_list:
            for v1 in self.aligenie_user_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AligenieUserInfoList'] = []
        if self.aligenie_user_info_list is not None:
            for k1 in self.aligenie_user_info_list:
                result['AligenieUserInfoList'].append(k1.to_map() if k1 else None)

        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.sp is not None:
            result['Sp'] = self.sp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aligenie_user_info_list = []
        if m.get('AligenieUserInfoList') is not None:
            for k1 in m.get('AligenieUserInfoList'):
                temp_model = main_models.QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoList()
                self.aligenie_user_info_list.append(temp_model.from_map(k1))

        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('Sp') is not None:
            self.sp = m.get('Sp')

        return self

class QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoList(DaraModel):
    def __init__(
        self,
        authorized_device_list: List[main_models.QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoListAuthorizedDeviceList] = None,
        open_user_id: str = None,
        user_nickname: str = None,
    ):
        # User Authorization device List
        self.authorized_device_list = authorized_device_list
        # User ID
        self.open_user_id = open_user_id
        # User nickname
        self.user_nickname = user_nickname

    def validate(self):
        if self.authorized_device_list:
            for v1 in self.authorized_device_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizedDeviceList'] = []
        if self.authorized_device_list is not None:
            for k1 in self.authorized_device_list:
                result['AuthorizedDeviceList'].append(k1.to_map() if k1 else None)

        if self.open_user_id is not None:
            result['OpenUserId'] = self.open_user_id

        if self.user_nickname is not None:
            result['UserNickname'] = self.user_nickname

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorized_device_list = []
        if m.get('AuthorizedDeviceList') is not None:
            for k1 in m.get('AuthorizedDeviceList'):
                temp_model = main_models.QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoListAuthorizedDeviceList()
                self.authorized_device_list.append(temp_model.from_map(k1))

        if m.get('OpenUserId') is not None:
            self.open_user_id = m.get('OpenUserId')

        if m.get('UserNickname') is not None:
            self.user_nickname = m.get('UserNickname')

        return self

class QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoListAuthorizedDeviceList(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        online: bool = None,
        open_device_id: str = None,
        tme_device_id: str = None,
        tme_product_id: str = None,
    ):
        # device name
        self.device_name = device_name
        # Indicates whether the device is online
        self.online = online
        # Device ID
        self.open_device_id = open_device_id
        # Device ID exposed to TME
        self.tme_device_id = tme_device_id
        # TME product ID
        self.tme_product_id = tme_product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.online is not None:
            result['Online'] = self.online

        if self.open_device_id is not None:
            result['OpenDeviceId'] = self.open_device_id

        if self.tme_device_id is not None:
            result['TmeDeviceId'] = self.tme_device_id

        if self.tme_product_id is not None:
            result['TmeProductId'] = self.tme_product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('OpenDeviceId') is not None:
            self.open_device_id = m.get('OpenDeviceId')

        if m.get('TmeDeviceId') is not None:
            self.tme_device_id = m.get('TmeDeviceId')

        if m.get('TmeProductId') is not None:
            self.tme_product_id = m.get('TmeProductId')

        return self


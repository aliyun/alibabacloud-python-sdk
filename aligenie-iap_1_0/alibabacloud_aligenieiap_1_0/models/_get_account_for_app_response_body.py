# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class GetAccountForAppResponseBody(DaraModel):
    def __init__(
        self,
        ret_code: int = None,
        ret_msg: str = None,
        ret_value: main_models.GetAccountForAppResponseBodyRetValue = None,
    ):
        # Error code returned. A value of `0` indicates success.
        self.ret_code = ret_code
        # Error message returned. No message is returned upon success.
        self.ret_msg = ret_msg
        # List of result objects returned.
        self.ret_value = ret_value

    def validate(self):
        if self.ret_value:
            self.ret_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg

        if self.ret_value is not None:
            result['RetValue'] = self.ret_value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')

        if m.get('RetValue') is not None:
            temp_model = main_models.GetAccountForAppResponseBodyRetValue()
            self.ret_value = temp_model.from_map(m.get('RetValue'))

        return self

class GetAccountForAppResponseBodyRetValue(DaraModel):
    def __init__(
        self,
        is_vip: bool = None,
        str_vip_expire: str = None,
        vip_expire_at: int = None,
    ):
        # Indicates whether the user is an authorized member.
        self.is_vip = is_vip
        # Membership expiration time.
        self.str_vip_expire = str_vip_expire
        # Millisecond-level UNIX timestamp.
        # 
        # - If the user has activated membership, returns the membership expiration time.
        # - If the user has never activated membership, the value is always `0`.
        self.vip_expire_at = vip_expire_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_vip is not None:
            result['IsVip'] = self.is_vip

        if self.str_vip_expire is not None:
            result['StrVipExpire'] = self.str_vip_expire

        if self.vip_expire_at is not None:
            result['VipExpireAt'] = self.vip_expire_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsVip') is not None:
            self.is_vip = m.get('IsVip')

        if m.get('StrVipExpire') is not None:
            self.str_vip_expire = m.get('StrVipExpire')

        if m.get('VipExpireAt') is not None:
            self.vip_expire_at = m.get('VipExpireAt')

        return self


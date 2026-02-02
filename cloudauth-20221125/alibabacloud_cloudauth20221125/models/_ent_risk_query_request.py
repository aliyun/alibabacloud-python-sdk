# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EntRiskQueryRequest(DaraModel):
    def __init__(
        self,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        param_type: str = None,
        param_value: str = None,
        scene_code: str = None,
        user_authorization: str = None,
    ):
        # A unique business identifier defined by the merchant side, used for subsequent problem localization and troubleshooting. Supports a combination of 32 alphanumeric characters, please ensure uniqueness.
        self.merchant_biz_id = merchant_biz_id
        # A custom user ID in your business, used for subsequent problem localization and troubleshooting.
        self.merchant_user_id = merchant_user_id
        # Parameter type.
        # 00: Company name;
        # 01: Business registration number;
        # 02: Unified Social Credit Code;
        # 03: Organization code;
        self.param_type = param_type
        # Enter one of the following based on the ParamType: company name, business registration number, unified social credit code, or organization code.
        self.param_value = param_value
        # Custom scene code, used to distinguish business scenarios, a 10-digit number.
        self.scene_code = scene_code
        # Whether user authorization is obtained.
        # 1: Authorized
        # 0: Not authorized
        self.user_authorization = user_authorization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.param_value is not None:
            result['ParamValue'] = self.param_value

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.user_authorization is not None:
            result['UserAuthorization'] = self.user_authorization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('UserAuthorization') is not None:
            self.user_authorization = m.get('UserAuthorization')

        return self


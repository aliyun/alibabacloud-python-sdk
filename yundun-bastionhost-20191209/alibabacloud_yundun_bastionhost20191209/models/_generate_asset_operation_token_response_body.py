# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GenerateAssetOperationTokenResponseBody(DaraModel):
    def __init__(
        self,
        asset_operation_token: main_models.GenerateAssetOperationTokenResponseBodyAssetOperationToken = None,
        request_id: str = None,
    ):
        # The data returned.
        self.asset_operation_token = asset_operation_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.asset_operation_token:
            self.asset_operation_token.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_operation_token is not None:
            result['AssetOperationToken'] = self.asset_operation_token.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetOperationToken') is not None:
            temp_model = main_models.GenerateAssetOperationTokenResponseBodyAssetOperationToken()
            self.asset_operation_token = temp_model.from_map(m.get('AssetOperationToken'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GenerateAssetOperationTokenResponseBodyAssetOperationToken(DaraModel):
    def __init__(
        self,
        count_left: int = None,
        expire_time: int = None,
        has_count_limit: bool = None,
        max_renew_count: int = None,
        renew_count: int = None,
        sso_url: str = None,
        token: str = None,
        token_id: str = None,
    ):
        # The remaining number of times that you can use the O\\&M token.
        self.count_left = count_left
        # The time when the O\\&M token expires. The value is a UNIX timestamp.
        self.expire_time = expire_time
        # Indicates whether the number of times that you can use the O\\&M token is limited.
        self.has_count_limit = has_count_limit
        # The maximum number of renewals. A value of 0 indicates that renewal is not supported.
        self.max_renew_count = max_renew_count
        # The number of times the O\\&M token is renewed.
        self.renew_count = renew_count
        # The single sign-on (SSO) URL.
        self.sso_url = sso_url
        # The O\\&M token that you apply for.
        self.token = token
        # The ID of the O\\&M token.
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count_left is not None:
            result['CountLeft'] = self.count_left

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.has_count_limit is not None:
            result['HasCountLimit'] = self.has_count_limit

        if self.max_renew_count is not None:
            result['MaxRenewCount'] = self.max_renew_count

        if self.renew_count is not None:
            result['RenewCount'] = self.renew_count

        if self.sso_url is not None:
            result['SsoUrl'] = self.sso_url

        if self.token is not None:
            result['Token'] = self.token

        if self.token_id is not None:
            result['TokenId'] = self.token_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountLeft') is not None:
            self.count_left = m.get('CountLeft')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HasCountLimit') is not None:
            self.has_count_limit = m.get('HasCountLimit')

        if m.get('MaxRenewCount') is not None:
            self.max_renew_count = m.get('MaxRenewCount')

        if m.get('RenewCount') is not None:
            self.renew_count = m.get('RenewCount')

        if m.get('SsoUrl') is not None:
            self.sso_url = m.get('SsoUrl')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')

        return self


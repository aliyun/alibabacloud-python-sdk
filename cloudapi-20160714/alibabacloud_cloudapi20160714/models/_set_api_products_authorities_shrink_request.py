# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetApiProductsAuthoritiesShrinkRequest(DaraModel):
    def __init__(
        self,
        api_product_ids_shrink: str = None,
        app_id: int = None,
        auth_valid_time: str = None,
        description: str = None,
        security_token: str = None,
    ):
        # The API products.
        # 
        # This parameter is required.
        self.api_product_ids_shrink = api_product_ids_shrink
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # 授权有效时间的截止时间，请设置格林尼治标准时间(GMT), 如果为空，即为授权永久有效。
        self.auth_valid_time = auth_valid_time
        # The authorization description.
        self.description = description
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_product_ids_shrink is not None:
            result['ApiProductIds'] = self.api_product_ids_shrink

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auth_valid_time is not None:
            result['AuthValidTime'] = self.auth_valid_time

        if self.description is not None:
            result['Description'] = self.description

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProductIds') is not None:
            self.api_product_ids_shrink = m.get('ApiProductIds')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AuthValidTime') is not None:
            self.auth_valid_time = m.get('AuthValidTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self


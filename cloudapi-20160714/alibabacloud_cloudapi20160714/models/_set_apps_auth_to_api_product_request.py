# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetAppsAuthToApiProductRequest(DaraModel):
    def __init__(
        self,
        api_product_id: str = None,
        app_ids: List[int] = None,
        auth_valid_time: str = None,
        description: str = None,
        security_token: str = None,
    ):
        # The ID of the API product.
        # 
        # This parameter is required.
        self.api_product_id = api_product_id
        # The IDs of the applications that you want to authorize.
        # 
        # This parameter is required.
        self.app_ids = app_ids
        # The time (UTC) when the authorization expires. If this parameter is empty, the authorization does not expire.
        self.auth_valid_time = auth_valid_time
        # The description of the authorization.
        self.description = description
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_product_id is not None:
            result['ApiProductId'] = self.api_product_id

        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.auth_valid_time is not None:
            result['AuthValidTime'] = self.auth_valid_time

        if self.description is not None:
            result['Description'] = self.description

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProductId') is not None:
            self.api_product_id = m.get('ApiProductId')

        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('AuthValidTime') is not None:
            self.auth_valid_time = m.get('AuthValidTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self


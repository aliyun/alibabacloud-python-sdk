# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataMaskingUsersShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_role: str = None,
        expire_time: int = None,
        expire_time_operation: str = None,
        lang: str = None,
        product_code: str = None,
        product_id: int = None,
        user_list_shrink: str = None,
    ):
        self.auth_role = auth_role
        self.expire_time = expire_time
        self.expire_time_operation = expire_time_operation
        self.lang = lang
        self.product_code = product_code
        self.product_id = product_id
        self.user_list_shrink = user_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_role is not None:
            result['AuthRole'] = self.auth_role

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expire_time_operation is not None:
            result['ExpireTimeOperation'] = self.expire_time_operation

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.user_list_shrink is not None:
            result['UserList'] = self.user_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthRole') is not None:
            self.auth_role = m.get('AuthRole')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpireTimeOperation') is not None:
            self.expire_time_operation = m.get('ExpireTimeOperation')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('UserList') is not None:
            self.user_list_shrink = m.get('UserList')

        return self


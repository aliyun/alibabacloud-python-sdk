# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class UpdateDataMaskingUsersRequest(DaraModel):
    def __init__(
        self,
        auth_role: str = None,
        expire_time: int = None,
        expire_time_operation: str = None,
        lang: str = None,
        product_code: str = None,
        product_id: int = None,
        user_list: List[main_models.UpdateDataMaskingUsersRequestUserList] = None,
    ):
        self.auth_role = auth_role
        self.expire_time = expire_time
        self.expire_time_operation = expire_time_operation
        self.lang = lang
        self.product_code = product_code
        self.product_id = product_id
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for v1 in self.user_list:
                 if v1:
                    v1.validate()

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

        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

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

        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.UpdateDataMaskingUsersRequestUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class UpdateDataMaskingUsersRequestUserList(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        instance_id: str = None,
    ):
        self.account_id = account_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self


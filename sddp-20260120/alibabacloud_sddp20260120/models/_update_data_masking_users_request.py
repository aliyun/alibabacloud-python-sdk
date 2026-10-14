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
        # The column encryption access permissions. Valid values:
        # 
        # - fullAccess: plaintext access.
        # - restrictedAccess: restricted access.
        # - noneAccess: decryption denied.
        # 
        # noneAccess applies only to ApsaraDB RDS for MySQL instances whose active key pattern is client_key.
        self.auth_role = auth_role
        # The expiration time of the plaintext access permissions. Specify a UNIX timestamp in milliseconds since 1970-01-01 00:00:00 UTC. This parameter is required only when ExpireTimeOperation is set to SET. The value must be later than the current time and no later than 2145953410000. The server stores the value with second-level precision. Do not specify this parameter when ExpireTimeOperation is set to PRESERVE or CLEAR.
        self.expire_time = expire_time
        # The action to take on the permission expiration time. Valid values:
        # 
        # - PRESERVE: Retains the existing expiration time.
        # - CLEAR: Clears the expiration time.
        # - SET: Sets the expiration time to the value specified by ExpireTime.
        # 
        # Default value: PRESERVE. Only fullAccess supports configuring a validity period.
        self.expire_time_operation = expire_time_operation
        # The language of the response description. Valid values:
        # 
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # The cloud product code. Column encryption supports RDS, POLARDB, and PolarDBX2. If ProductId is also specified, the two parameters must correspond to each other.
        self.product_code = product_code
        # The cloud product type identifier. Valid values:
        # 
        # - 5: RDS.
        # - 8: POLARDB.
        # - 27: PolarDBX2.
        # 
        # If both ProductId and ProductCode are specified, they must correspond to each other.
        self.product_id = product_id
        # The list of database accounts for which to set permissions.
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
        # The database account identifier. Obtain this value from Items[].Id in the response of ListDataAssetAccounts and pass it as a string.
        self.account_id = account_id
        # The database instance identity. Obtain this value from Items[].InstanceId in the response of ListDataMaskingInstances.
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


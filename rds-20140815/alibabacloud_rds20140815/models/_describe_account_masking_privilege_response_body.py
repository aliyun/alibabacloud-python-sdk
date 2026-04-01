# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountMaskingPrivilegeResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeAccountMaskingPrivilegeResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeAccountMaskingPrivilegeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccountMaskingPrivilegeResponseBodyData(DaraModel):
    def __init__(
        self,
        user_privilege: List[main_models.DescribeAccountMaskingPrivilegeResponseBodyDataUserPrivilege] = None,
    ):
        self.user_privilege = user_privilege

    def validate(self):
        if self.user_privilege:
            for v1 in self.user_privilege:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserPrivilege'] = []
        if self.user_privilege is not None:
            for k1 in self.user_privilege:
                result['UserPrivilege'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_privilege = []
        if m.get('UserPrivilege') is not None:
            for k1 in m.get('UserPrivilege'):
                temp_model = main_models.DescribeAccountMaskingPrivilegeResponseBodyDataUserPrivilege()
                self.user_privilege.append(temp_model.from_map(k1))

        return self

class DescribeAccountMaskingPrivilegeResponseBodyDataUserPrivilege(DaraModel):
    def __init__(
        self,
        expire_time: str = None,
        privilege: str = None,
        user_name: str = None,
    ):
        self.expire_time = expire_time
        self.privilege = privilege
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.privilege is not None:
            result['Privilege'] = self.privilege

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self


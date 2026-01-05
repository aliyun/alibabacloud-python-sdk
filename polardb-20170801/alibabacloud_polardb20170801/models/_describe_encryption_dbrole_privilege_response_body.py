# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeEncryptionDBRolePrivilegeResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        data: main_models.DescribeEncryptionDBRolePrivilegeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeEncryptionDBRolePrivilegeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeEncryptionDBRolePrivilegeResponseBodyData(DaraModel):
    def __init__(
        self,
        role_privilege_list: List[main_models.DescribeEncryptionDBRolePrivilegeResponseBodyDataRolePrivilegeList] = None,
    ):
        self.role_privilege_list = role_privilege_list

    def validate(self):
        if self.role_privilege_list:
            for v1 in self.role_privilege_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RolePrivilegeList'] = []
        if self.role_privilege_list is not None:
            for k1 in self.role_privilege_list:
                result['RolePrivilegeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_privilege_list = []
        if m.get('RolePrivilegeList') is not None:
            for k1 in m.get('RolePrivilegeList'):
                temp_model = main_models.DescribeEncryptionDBRolePrivilegeResponseBodyDataRolePrivilegeList()
                self.role_privilege_list.append(temp_model.from_map(k1))

        return self

class DescribeEncryptionDBRolePrivilegeResponseBodyDataRolePrivilegeList(DaraModel):
    def __init__(
        self,
        encryption: str = None,
        negation: str = None,
        not_encryption: str = None,
        role_privilege_name: str = None,
    ):
        self.encryption = encryption
        self.negation = negation
        self.not_encryption = not_encryption
        self.role_privilege_name = role_privilege_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encryption is not None:
            result['Encryption'] = self.encryption

        if self.negation is not None:
            result['Negation'] = self.negation

        if self.not_encryption is not None:
            result['NotEncryption'] = self.not_encryption

        if self.role_privilege_name is not None:
            result['RolePrivilegeName'] = self.role_privilege_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')

        if m.get('Negation') is not None:
            self.negation = m.get('Negation')

        if m.get('NotEncryption') is not None:
            self.not_encryption = m.get('NotEncryption')

        if m.get('RolePrivilegeName') is not None:
            self.role_privilege_name = m.get('RolePrivilegeName')

        return self


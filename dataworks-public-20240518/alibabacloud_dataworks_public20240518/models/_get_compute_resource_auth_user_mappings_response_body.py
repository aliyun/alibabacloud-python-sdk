# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetComputeResourceAuthUserMappingsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetComputeResourceAuthUserMappingsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.data = data
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetComputeResourceAuthUserMappingsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetComputeResourceAuthUserMappingsResponseBodyData(DaraModel):
    def __init__(
        self,
        accounts: List[main_models.GetComputeResourceAuthUserMappingsResponseBodyDataAccounts] = None,
        hadoop_auth_type: str = None,
    ):
        # The list of mapped account information.
        self.accounts = accounts
        # The authentication type, such as LDAP.
        self.hadoop_auth_type = hadoop_auth_type

    def validate(self):
        if self.accounts:
            for v1 in self.accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Accounts'] = []
        if self.accounts is not None:
            for k1 in self.accounts:
                result['Accounts'].append(k1.to_map() if k1 else None)

        if self.hadoop_auth_type is not None:
            result['HadoopAuthType'] = self.hadoop_auth_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.GetComputeResourceAuthUserMappingsResponseBodyDataAccounts()
                self.accounts.append(temp_model.from_map(k1))

        if m.get('HadoopAuthType') is not None:
            self.hadoop_auth_type = m.get('HadoopAuthType')

        return self

class GetComputeResourceAuthUserMappingsResponseBodyDataAccounts(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        username: str = None,
    ):
        # The Alibaba Cloud UID.
        self.user_id = user_id
        # The username in the target system, such as an LDAP account.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeEnabledPrivilegesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeEnabledPrivilegesResponseBodyData] = None,
        request_id: str = None,
    ):
        # The queried permission level and permissions.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeEnabledPrivilegesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnabledPrivilegesResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        privileges: List[main_models.DescribeEnabledPrivilegesResponseBodyDataPrivileges] = None,
        scope: str = None,
    ):
        # The description of the permission level.
        # 
        # This parameter is required.
        self.description = description
        # The queried permissions.
        # 
        # This parameter is required.
        self.privileges = privileges
        # The permission level.
        # 
        # This parameter is required.
        self.scope = scope

    def validate(self):
        if self.privileges:
            for v1 in self.privileges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['Privileges'] = []
        if self.privileges is not None:
            for k1 in self.privileges:
                result['Privileges'].append(k1.to_map() if k1 else None)

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.privileges = []
        if m.get('Privileges') is not None:
            for k1 in m.get('Privileges'):
                temp_model = main_models.DescribeEnabledPrivilegesResponseBodyDataPrivileges()
                self.privileges.append(temp_model.from_map(k1))

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

class DescribeEnabledPrivilegesResponseBodyDataPrivileges(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
    ):
        # The description of the permission.
        self.description = description
        # The name of the permission.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class CreateLakeStorageRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbcluster_id: str = None,
        description: str = None,
        permissions: List[main_models.CreateLakeStorageRequestPermissions] = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the AnalyticDB for MySQL cluster with which you want to associate the lake storage.
        self.dbcluster_id = dbcluster_id
        # The description of the lake storage.
        self.description = description
        # The permissions that you want to grant on the lake storage to the Alibaba Cloud account besides the permissions that are automatically granted to the Resource Access Management (RAM) user or the Alibaba Cloud account.
        self.permissions = permissions
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        result['Permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['Permissions'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.permissions = []
        if m.get('Permissions') is not None:
            for k1 in m.get('Permissions'):
                temp_model = main_models.CreateLakeStorageRequestPermissions()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateLakeStorageRequestPermissions(DaraModel):
    def __init__(
        self,
        account: str = None,
        read: bool = None,
        type: str = None,
        write: bool = None,
    ):
        # The account ID.
        self.account = account
        # The read permissions.
        self.read = read
        # The account type.
        self.type = type
        # The write permissions.
        self.write = write

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.read is not None:
            result['Read'] = self.read

        if self.type is not None:
            result['Type'] = self.type

        if self.write is not None:
            result['Write'] = self.write

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Read') is not None:
            self.read = m.get('Read')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Write') is not None:
            self.write = m.get('Write')

        return self


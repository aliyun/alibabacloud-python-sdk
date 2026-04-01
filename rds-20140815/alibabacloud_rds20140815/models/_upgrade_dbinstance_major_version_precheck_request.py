# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeDBInstanceMajorVersionPrecheckRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        resource_owner_id: int = None,
        target_major_version: str = None,
        upgrade_mode: str = None,
    ):
        # The ID of the instance. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) operation to query the ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.resource_owner_id = resource_owner_id
        # The new major engine version of the instance. The new major engine version must be later than the original major engine version.
        # 
        # This parameter is required.
        self.target_major_version = target_major_version
        self.upgrade_mode = upgrade_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.target_major_version is not None:
            result['TargetMajorVersion'] = self.target_major_version

        if self.upgrade_mode is not None:
            result['UpgradeMode'] = self.upgrade_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TargetMajorVersion') is not None:
            self.target_major_version = m.get('TargetMajorVersion')

        if m.get('UpgradeMode') is not None:
            self.upgrade_mode = m.get('UpgradeMode')

        return self


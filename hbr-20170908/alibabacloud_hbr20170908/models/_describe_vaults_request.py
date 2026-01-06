# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeVaultsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        replication: bool = None,
        resource_group_id: str = None,
        status: str = None,
        tag: List[main_models.DescribeVaultsRequestTag] = None,
        vault_id: str = None,
        vault_name: str = None,
        vault_owner_id: int = None,
        vault_region_id: str = None,
        vault_type: str = None,
    ):
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        self.replication = replication
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the backup vault. Valid values:
        # 
        # *   **UNKNOWN**: The backup vault is in an unknown state.
        # *   **INITIALIZING**: The backup vault is being initialized.
        # *   **CREATED**: The backup vault is created.
        # *   **ERROR**: An error occurs on the backup vault.
        self.status = status
        # Tag information. Supports up to 20 tags.
        self.tag = tag
        # Backup vault ID.
        self.vault_id = vault_id
        # The name of the backup vault. The name must be 1 to 64 characters in length.
        self.vault_name = vault_name
        self.vault_owner_id = vault_owner_id
        # The region ID to which the backup vault belongs.
        self.vault_region_id = vault_region_id
        # Backup repository type. The values are as follows: 
        # - **STANDARD**: Represents a standard repository, which can be used for ECS file backups, OSS backups, NAS backups, etc. 
        # - **OTS_BACKUP**: Represents a TableStore repository, which is only used for TableStore backups, and TableStore must use this type of repository.
        self.vault_type = vault_type

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.replication is not None:
            result['Replication'] = self.replication

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        if self.vault_name is not None:
            result['VaultName'] = self.vault_name

        if self.vault_owner_id is not None:
            result['VaultOwnerId'] = self.vault_owner_id

        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id

        if self.vault_type is not None:
            result['VaultType'] = self.vault_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Replication') is not None:
            self.replication = m.get('Replication')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeVaultsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')

        if m.get('VaultOwnerId') is not None:
            self.vault_owner_id = m.get('VaultOwnerId')

        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')

        if m.get('VaultType') is not None:
            self.vault_type = m.get('VaultType')

        return self

class DescribeVaultsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The Value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


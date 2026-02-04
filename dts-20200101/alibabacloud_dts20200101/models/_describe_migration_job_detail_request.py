# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeMigrationJobDetailRequest(DaraModel):
    def __init__(
        self,
        migration_mode: main_models.DescribeMigrationJobDetailRequestMigrationMode = None,
        account_id: str = None,
        client_token: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.migration_mode = migration_mode
        # The ID of the data migration instance. You can call the **DescribeMigrationJobs** operation to query the instance ID.
        self.account_id = account_id
        # The number of the page to return. The value must be an integer that is greater than **0** and does not exceed the maximum value of the Integer data type. Default value: **1**.
        self.client_token = client_token
        # The ID of the data migration instance. You can call the **DescribeMigrationJobs** operation to query the instance ID.
        # 
        # This parameter is required.
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        # The number of the page to return. The value must be an integer that is greater than **0** and does not exceed the maximum value of the Integer data type. Default value: **1**.
        self.page_num = page_num
        # The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30.
        self.page_size = page_size
        # The ID of the region where the data migration instance resides. For more information, see List of supported regions.
        self.region_id = region_id
        # Specifies whether to query the details of schema migration. Valid values:
        # 
        # *   **true**: yes
        # 
        # *   **false**: no
        # 
        # > Default value: **false**
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.migration_mode:
            self.migration_mode.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationMode') is not None:
            temp_model = main_models.DescribeMigrationJobDetailRequestMigrationMode()
            self.migration_mode = temp_model.from_map(m.get('MigrationMode'))

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class DescribeMigrationJobDetailRequestMigrationMode(DaraModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        # The ID of the region where the data migration instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.data_initialization = data_initialization
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**. Default value: **30**.
        self.data_synchronization = data_synchronization
        # When you call this operation, the data migration task must be in the Migrating, Failed, Paused, or Finished state.
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization

        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization

        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')

        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')

        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')

        return self


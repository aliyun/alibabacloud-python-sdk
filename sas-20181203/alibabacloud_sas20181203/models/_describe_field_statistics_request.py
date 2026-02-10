# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFieldStatisticsRequest(DaraModel):
    def __init__(
        self,
        machine_types: str = None,
        region_id: str = None,
        resource_directory_account_id: int = None,
    ):
        # The type of the asset to query. If no asset types are specified, all types of assets are returned. Valid values:
        # 
        # *   **ecs**: server
        # *   **cloud_product**: Alibaba Cloud service
        self.machine_types = machine_types
        # The ID of the region in which the asset resides.
        self.region_id = region_id
        # The ID of the primary account of the Resource Directory member account.
        # > call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) interface to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self


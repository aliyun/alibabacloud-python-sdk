# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupPlanListRequest(DaraModel):
    def __init__(
        self,
        backup_method: str = None,
        backup_plan_id: str = None,
        backup_plan_name: str = None,
        backup_plan_status: str = None,
        client_token: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region: str = None,
        resource_group_id: str = None,
        show_backup_strategy_info: bool = None,
        show_recover_time_range: bool = None,
        show_storage_strategy_info: bool = None,
    ):
        self.backup_method = backup_method
        # Backup plan ID. To list multiple backup plans, separate IDs with commas.
        self.backup_plan_id = backup_plan_id
        # Backup plan name.
        self.backup_plan_name = backup_plan_name
        # Backup plan status. Valid values:
        # 
        # - **wait**: Not configured.
        # 
        # - **init**: Not started (precheck failed).
        # 
        # - **running**: Running.
        # 
        # - **stop**: Failed.
        # 
        # - **pause**: Paused.
        # 
        # - **locked**: Locked.
        # 
        # - **check_pass**: Precheck passed.
        self.backup_plan_status = backup_plan_status
        # A client token used to ensure idempotence and prevent duplicate requests.
        self.client_token = client_token
        self.owner_id = owner_id
        # Page number. Valid values: integers greater than or equal to 0 and less than or equal to the maximum integer value. Default value: 0.
        self.page_num = page_num
        # Number of records per page. Valid values: 1 to 100.
        # 
        # > Default value: **30**.
        self.page_size = page_size
        # DBS region. Call [DescribeRegions](https://help.aliyun.com/document_detail/2869853.html) to view supported regions.
        self.region = region
        # Resource group ID.
        self.resource_group_id = resource_group_id
        self.show_backup_strategy_info = show_backup_strategy_info
        self.show_recover_time_range = show_recover_time_range
        self.show_storage_strategy_info = show_storage_strategy_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name

        if self.backup_plan_status is not None:
            result['BackupPlanStatus'] = self.backup_plan_status

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.show_backup_strategy_info is not None:
            result['ShowBackupStrategyInfo'] = self.show_backup_strategy_info

        if self.show_recover_time_range is not None:
            result['ShowRecoverTimeRange'] = self.show_recover_time_range

        if self.show_storage_strategy_info is not None:
            result['ShowStorageStrategyInfo'] = self.show_storage_strategy_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')

        if m.get('BackupPlanStatus') is not None:
            self.backup_plan_status = m.get('BackupPlanStatus')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShowBackupStrategyInfo') is not None:
            self.show_backup_strategy_info = m.get('ShowBackupStrategyInfo')

        if m.get('ShowRecoverTimeRange') is not None:
            self.show_recover_time_range = m.get('ShowRecoverTimeRange')

        if m.get('ShowStorageStrategyInfo') is not None:
            self.show_storage_strategy_info = m.get('ShowStorageStrategyInfo')

        return self


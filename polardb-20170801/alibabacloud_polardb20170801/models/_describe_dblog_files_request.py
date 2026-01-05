# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBLogFilesRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbnode_id: str = None,
        describe_simulate_switch_mode: str = None,
        end_time: str = None,
        log_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        simulate_list_id: str = None,
        simulate_mode_list: str = None,
        simulate_status_list: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.dbnode_id = dbnode_id
        self.describe_simulate_switch_mode = describe_simulate_switch_mode
        self.end_time = end_time
        # The log type. Valid values:
        # 
        # *   **HaSwitchLogList**: failover logs.
        # 
        # This parameter is required.
        self.log_type = log_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.simulate_list_id = simulate_list_id
        self.simulate_mode_list = simulate_mode_list
        self.simulate_status_list = simulate_status_list
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.describe_simulate_switch_mode is not None:
            result['DescribeSimulateSwitchMode'] = self.describe_simulate_switch_mode

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.simulate_list_id is not None:
            result['SimulateListId'] = self.simulate_list_id

        if self.simulate_mode_list is not None:
            result['SimulateModeList'] = self.simulate_mode_list

        if self.simulate_status_list is not None:
            result['SimulateStatusList'] = self.simulate_status_list

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('DescribeSimulateSwitchMode') is not None:
            self.describe_simulate_switch_mode = m.get('DescribeSimulateSwitchMode')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SimulateListId') is not None:
            self.simulate_list_id = m.get('SimulateListId')

        if m.get('SimulateModeList') is not None:
            self.simulate_mode_list = m.get('SimulateModeList')

        if m.get('SimulateStatusList') is not None:
            self.simulate_status_list = m.get('SimulateStatusList')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self


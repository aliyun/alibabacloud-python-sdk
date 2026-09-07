# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccountPrivilegesShrinkRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privileges_shrink: str = None,
        dbcluster_id: str = None,
        promql_insert_privileges_shrink: str = None,
        promql_select_node_percentage: float = None,
        promql_select_privileges_shrink: str = None,
        region_id: str = None,
        resource_group_name: str = None,
    ):
        # The name of the database account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The list of granted permissions.
        self.account_privileges_shrink = account_privileges_shrink
        # <props="china">The cluster ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The cluster ID of the Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.promql_insert_privileges_shrink = promql_insert_privileges_shrink
        self.promql_select_node_percentage = promql_select_node_percentage
        self.promql_select_privileges_shrink = promql_select_privileges_shrink
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_privileges_shrink is not None:
            result['AccountPrivileges'] = self.account_privileges_shrink

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.promql_insert_privileges_shrink is not None:
            result['PromqlInsertPrivileges'] = self.promql_insert_privileges_shrink

        if self.promql_select_node_percentage is not None:
            result['PromqlSelectNodePercentage'] = self.promql_select_node_percentage

        if self.promql_select_privileges_shrink is not None:
            result['PromqlSelectPrivileges'] = self.promql_select_privileges_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPrivileges') is not None:
            self.account_privileges_shrink = m.get('AccountPrivileges')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PromqlInsertPrivileges') is not None:
            self.promql_insert_privileges_shrink = m.get('PromqlInsertPrivileges')

        if m.get('PromqlSelectNodePercentage') is not None:
            self.promql_select_node_percentage = m.get('PromqlSelectNodePercentage')

        if m.get('PromqlSelectPrivileges') is not None:
            self.promql_select_privileges_shrink = m.get('PromqlSelectPrivileges')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMaterializedViewRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        db_name: str = None,
        enable_delay_alert: bool = None,
        enable_failure_alert: bool = None,
        group_name: str = None,
        latency_tolerance: int = None,
        owner_account: str = None,
        owner_id: int = None,
        query_write: bool = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        view_name: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database where the materialized view resides.
        # 
        # This parameter is required.
        self.db_name = db_name
        # Enable the refresh delay alert. Valid values:
        # 
        # *   true: Enables alert.
        # *   false: Disables alert.
        self.enable_delay_alert = enable_delay_alert
        # Specifies whether to send alerts when the refresh task fails. Valid values:
        # 
        # *   true: Send alerts.
        # *   false: Alerts disabled.
        self.enable_failure_alert = enable_failure_alert
        # The name of the resource group to which the materialized view is bound.
        self.group_name = group_name
        # Refresh delay tolerance (in minutes).
        self.latency_tolerance = latency_tolerance
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to enable query rewrite. Valid values:
        # 
        # *   true: Enables query rewrite.
        # *   false: Disables query rewrite.
        self.query_write = query_write
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the materialized view.
        # 
        # This parameter is required.
        self.view_name = view_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.enable_delay_alert is not None:
            result['EnableDelayAlert'] = self.enable_delay_alert

        if self.enable_failure_alert is not None:
            result['EnableFailureAlert'] = self.enable_failure_alert

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.latency_tolerance is not None:
            result['LatencyTolerance'] = self.latency_tolerance

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.query_write is not None:
            result['QueryWrite'] = self.query_write

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.view_name is not None:
            result['ViewName'] = self.view_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('EnableDelayAlert') is not None:
            self.enable_delay_alert = m.get('EnableDelayAlert')

        if m.get('EnableFailureAlert') is not None:
            self.enable_failure_alert = m.get('EnableFailureAlert')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('LatencyTolerance') is not None:
            self.latency_tolerance = m.get('LatencyTolerance')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QueryWrite') is not None:
            self.query_write = m.get('QueryWrite')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ViewName') is not None:
            self.view_name = m.get('ViewName')

        return self


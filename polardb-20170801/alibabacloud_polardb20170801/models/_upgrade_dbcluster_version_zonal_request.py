# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeDBClusterVersionZonalRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbcluster_id: str = None,
        from_time_service: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        planned_end_time: str = None,
        planned_start_time: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        target_dbrevision_version_code: str = None,
        target_proxy_revision_version_code: str = None,
        upgrade_label: str = None,
        upgrade_policy: str = None,
        upgrade_type: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.from_time_service = from_time_service
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.planned_end_time = planned_end_time
        self.planned_start_time = planned_start_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.target_dbrevision_version_code = target_dbrevision_version_code
        self.target_proxy_revision_version_code = target_proxy_revision_version_code
        self.upgrade_label = upgrade_label
        self.upgrade_policy = upgrade_policy
        self.upgrade_type = upgrade_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.from_time_service is not None:
            result['FromTimeService'] = self.from_time_service

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.target_dbrevision_version_code is not None:
            result['TargetDBRevisionVersionCode'] = self.target_dbrevision_version_code

        if self.target_proxy_revision_version_code is not None:
            result['TargetProxyRevisionVersionCode'] = self.target_proxy_revision_version_code

        if self.upgrade_label is not None:
            result['UpgradeLabel'] = self.upgrade_label

        if self.upgrade_policy is not None:
            result['UpgradePolicy'] = self.upgrade_policy

        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FromTimeService') is not None:
            self.from_time_service = m.get('FromTimeService')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TargetDBRevisionVersionCode') is not None:
            self.target_dbrevision_version_code = m.get('TargetDBRevisionVersionCode')

        if m.get('TargetProxyRevisionVersionCode') is not None:
            self.target_proxy_revision_version_code = m.get('TargetProxyRevisionVersionCode')

        if m.get('UpgradeLabel') is not None:
            self.upgrade_label = m.get('UpgradeLabel')

        if m.get('UpgradePolicy') is not None:
            self.upgrade_policy = m.get('UpgradePolicy')

        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')

        return self


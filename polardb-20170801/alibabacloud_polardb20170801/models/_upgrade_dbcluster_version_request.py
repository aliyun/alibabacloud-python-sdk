# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeDBClusterVersionRequest(DaraModel):
    def __init__(
        self,
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
        # The ID of cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to immediately run the kernel upgrade task. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        # 
        # >  This parameter is not required when you call the operation.
        self.from_time_service = from_time_service
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest start time to run the task that updates the kernel version of the cluster. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # > *   The value of this parameter must be at least 30 minutes later than the value of PlannedStartTime.
        # >*   If you specify `PlannedStartTime` but do not specify PlannedEndTime, the latest start time of the task is `PlannedEndTime + 30 minutes`. For example, if you set `PlannedStartTime` to `2021-01-14T09:00:00Z` and do not specify PlannedEndTime, the latest start time of the task is set to `2021-01-14T09:30:00Z`.
        self.planned_end_time = planned_end_time
        # The earliest start time to run the task that updates the kernel version of the cluster. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # > 
        # 
        # *   The earliest start time of the task can be a point in time within the next 72 hours. For example, if the current time is `2021-01-14T09:00:00Z`, you can specify a point in time from `2021-01-14T09:00:00Z` to `2021-01-17T09:00:00Z`.
        # 
        # *   If you do not specify this parameter, the kernel update task runs immediately after you submit the request.
        self.planned_start_time = planned_start_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The code of the db version to which you want to upgrade the cluster. You can call the [DescribeDBClusterVersion](https://help.aliyun.com/document_detail/2319145.html) operation to query the version code.
        self.target_dbrevision_version_code = target_dbrevision_version_code
        # The code of the proxy version to which you want to upgrade the cluster. You can call the [DescribeDBClusterVersion](https://help.aliyun.com/document_detail/2319145.html) operation to query the version code.
        self.target_proxy_revision_version_code = target_proxy_revision_version_code
        # The upgrade tag. The value is fixed as **INNOVATE**.
        # 
        # > *   This parameter is applicable only when you upgrade PolarDB for MySQL 8.0.1 to PolarDB for MySQL 8.0.2.
        # >*   If you specify this parameter, you must set `UpgradePolicy` to **COLD**.
        self.upgrade_label = upgrade_label
        # The engine version upgrade policy. Valid values:
        # 
        # *   **HOT**: hot upgrade.
        # *   **COLD**: cold upgrade. Only PolarDB for MySQL 8.0 Cluster Edition supports this upgrade method.
        self.upgrade_policy = upgrade_policy
        # The update type. Valid values:
        # 
        # *   **PROXY**: specifies to upgrade PloarProxy.
        # *   **DB**: specifies to upgrade the kernel version.
        # *   **ALL**: specifies to upgrade both PloarProxy and kernel version.
        self.upgrade_type = upgrade_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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


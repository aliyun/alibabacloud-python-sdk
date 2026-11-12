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
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can generate the value on the client side. The value must be unique across different requests and is case-sensitive. It can contain up to 64 ASCII characters.
        self.client_token = client_token
        # The ID of the PolarDB on ENS cluster. Only cluster IDs returned by the DescribeDBClustersZonal operation are supported. Before you call this operation, you must create an edge cluster by using ENS infrastructure. Standard PolarDB cluster IDs are not supported. Note: Only edge cluster IDs returned by DescribeDBClustersZonal are accepted, and the edge cluster must be created based on ENS.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to immediately execute or schedule the kernel version upgrade. Valid values:
        # 
        # - **false** (default): Scheduled execution.
        # 
        # - **true**: Immediate execution.
        # 
        # > You do not need to specify this parameter when you invoke this operation.
        self.from_time_service = from_time_service
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest time to start the scheduled task. The time must be in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # > * The latest time must be at least 30 minutes later than the start time.
        # > * If you specify `PlannedStartTime` but do not specify this parameter, the latest time to start the task defaults to 30 minutes after the start time. For example, if you set `PlannedStartTime` to `2021-01-14T09:00:00Z` and leave this parameter empty, the task starts at `2021-01-14T09:30:00Z` at the latest.
        self.planned_end_time = planned_end_time
        # The earliest time to start the scheduled Milvus version upgrade task. The time must be in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # > * The start time must be within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, the allowed start time ranges from `2021-01-14T09:00:00Z` to `2021-01-15T09:00:00Z`.
        # > * If you leave this parameter empty, the Milvus version upgrade task is immediately executed by default.
        self.planned_start_time = planned_start_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The version code of the target database engine version. You can obtain the value from the [DescribeDBClusterVersion](https://help.aliyun.com/document_detail/2319145.html) operation.
        self.target_dbrevision_version_code = target_dbrevision_version_code
        # The version code of the target PolarProxy version. You can obtain the value from the [DescribeDBClusterVersion](https://help.aliyun.com/document_detail/2319145.html) operation.
        self.target_proxy_revision_version_code = target_proxy_revision_version_code
        # The kernel version upgrade label. Set the value to **INNOVATE**.
        # 
        # > - This parameter applies only to upgrades from PolarDB for MySQL 8.0.1 to PolarDB for MySQL 8.0.2.
        # > - If you specify this parameter, you must set `UpgradePolicy` to **COLD**.
        self.upgrade_label = upgrade_label
        # The kernel version upgrade policy. Valid values:
        # 
        # - **HOT**: Hot upgrade.
        # 
        # - **COLD**: Cold upgrade. Only PolarDB for MySQL 8.0 Cluster Edition supports this upgrade method.
        self.upgrade_policy = upgrade_policy
        # The upgrade type. Valid values:
        # 
        # - **PROXY**: Upgrades only PolarProxy.
        # 
        # - **DB**: Upgrades only the database engine.
        # 
        # - **ALL** (default): Upgrades both PolarProxy and the database engine.
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


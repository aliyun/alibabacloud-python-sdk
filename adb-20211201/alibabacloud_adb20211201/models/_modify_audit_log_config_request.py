# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAuditLogConfigRequest(DaraModel):
    def __init__(
        self,
        audit_log_status: str = None,
        dbcluster_id: str = None,
        engine_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The status of SQL audit logging. Valid values:
        # - **on**: Enables SQL audit logging.
        # - **off**: Disables SQL audit logging.
        # 
        # > After SQL audit logging is disabled, all SQL audit logs are deleted. Query and export the SQL audit logs before disabling SQL audit logging. For more information, see [DescribeAuditLogRecords](https://help.aliyun.com/document_detail/612426.html). When SQL audit logging is enabled again, audit logs are displayed starting from the most recent time that audit logging was enabled.
        # 
        # This parameter is required.
        self.audit_log_status = audit_log_status
        # <props="china">The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # > You can call [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) to query the IDs of all clusters in a specified region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The type of the compute engine. Valid values:
        # 
        # - XIHE (**default**): Xihe compute engine.
        # - SPARK: Spark compute engine.
        self.engine_type = engine_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # > You can call [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) to query the region ID of a specified cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_log_status is not None:
            result['AuditLogStatus'] = self.audit_log_status

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditLogStatus') is not None:
            self.audit_log_status = m.get('AuditLogStatus')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self


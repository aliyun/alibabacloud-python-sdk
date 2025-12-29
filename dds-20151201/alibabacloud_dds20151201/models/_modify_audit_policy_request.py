# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAuditPolicyRequest(DaraModel):
    def __init__(
        self,
        audit_log_switch_source: str = None,
        audit_status: str = None,
        dbinstance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        service_type: str = None,
        storage_period: int = None,
    ):
        # The request source for the audit log feature. Set the value to **Console**.
        self.audit_log_switch_source = audit_log_switch_source
        # Specifies whether to enable the audit log feature. Valid values:
        # 
        # *   **enable**
        # *   **disabled**
        # 
        # This parameter is required.
        self.audit_status = audit_status
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the audit log feature. Valid values:
        # 
        # *   **Trail**: free trial edition.
        # *   **Standard**: official edition.
        # 
        # > The default value is **Trail**. Starting from January 6, 2022, the official edition of the audit log feature has been launched in all regions, and the free trial edition of the feature can no longer be applied for. We recommend that you set this parameter to **Standard**.
        self.service_type = service_type
        # The log retention period. Valid values: 1 to 365 days. Default value: 30 days.
        self.storage_period = storage_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_log_switch_source is not None:
            result['AuditLogSwitchSource'] = self.audit_log_switch_source

        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.storage_period is not None:
            result['StoragePeriod'] = self.storage_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditLogSwitchSource') is not None:
            self.audit_log_switch_source = m.get('AuditLogSwitchSource')

        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('StoragePeriod') is not None:
            self.storage_period = m.get('StoragePeriod')

        return self


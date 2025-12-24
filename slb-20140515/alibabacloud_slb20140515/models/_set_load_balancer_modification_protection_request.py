# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLoadBalancerModificationProtectionRequest(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        modification_protection_reason: str = None,
        modification_protection_status: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The reason why the configuration read-only mode is enabled. The value must be 1 to 80 characters in length. It must start with a letter and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # >  This parameter is valid only if the **ModificationProtectionStatus** parameter is set to **ConsoleProtection**.
        self.modification_protection_reason = modification_protection_reason
        # Specifies whether to enable the configuration read-only mode. Valid values:
        # 
        # *   **NonProtection**: disables the configuration read-only mode. After you disable the configuration read-only mode, the value of **ModificationProtectionReason** is cleared.
        # *   **ConsoleProtection**: enables the configuration read-only mode.
        # 
        # >  If you set this parameter to **ConsoleProtection**, you cannot use the CLB console to modify instance configurations. However, you can call API operations to modify instance configurations.
        # 
        # This parameter is required.
        self.modification_protection_status = modification_protection_status
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the CLB instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation to query the most recent region list.
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
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason

        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status

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
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')

        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')

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


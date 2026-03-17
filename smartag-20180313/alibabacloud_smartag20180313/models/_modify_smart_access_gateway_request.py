# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySmartAccessGatewayRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        enable_software_connection_audit: bool = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        position: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        routing_strategy: str = None,
        security_lock_threshold: int = None,
        smart_agid: str = None,
    ):
        # The CIDR blocks of terminals in the private network. Make sure that the CIDR blocks do not overlap with each other.
        # 
        # If the LAN ports of the terminals use dynamic routing, the IP addresses within the first private CIDR block are allocated to the terminals that have Dynamic Host Configuration Protocol (DHCP) enabled.
        self.cidr_block = cidr_block
        # The description of the SAG instance.
        # 
        # The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to audit the network connection logs of the SAS app instance.
        # 
        # *   **true**: yes
        # *   **false**: no
        self.enable_software_connection_audit = enable_software_connection_audit
        # The name of the SAG instance.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The location where the SAG instance is deployed.
        self.position = position
        # The ID of the region where the SAG instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The policy that is used to advertise routes to Alibaba Cloud. Valid values:
        # 
        # *   **static**: static routing
        # *   **dynamic**: dynamic routing
        self.routing_strategy = routing_strategy
        # The time during which the disconnected SAG instance remains locked. Valid values: an integer that is greater than or equal to 0.
        # 
        # Unit: seconds.
        self.security_lock_threshold = security_lock_threshold
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_software_connection_audit is not None:
            result['EnableSoftwareConnectionAudit'] = self.enable_software_connection_audit

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.position is not None:
            result['Position'] = self.position

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.routing_strategy is not None:
            result['RoutingStrategy'] = self.routing_strategy

        if self.security_lock_threshold is not None:
            result['SecurityLockThreshold'] = self.security_lock_threshold

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableSoftwareConnectionAudit') is not None:
            self.enable_software_connection_audit = m.get('EnableSoftwareConnectionAudit')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoutingStrategy') is not None:
            self.routing_strategy = m.get('RoutingStrategy')

        if m.get('SecurityLockThreshold') is not None:
            self.security_lock_threshold = m.get('SecurityLockThreshold')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self


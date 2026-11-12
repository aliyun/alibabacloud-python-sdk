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
        # The private CIDR block used by clients at the on-premises site for communication. Make sure that private CIDR blocks do not conflict with each other. 
        # 
        # If the LAN port of the Smart Access Gateway device is configured in dynamic mode, the IP addresses used by on-premises clients with DHCP enabled are allocated from the first private CIDR block that you specify.
        self.cidr_block = cidr_block
        # The description of the Smart Access Gateway instance. 
        # 
        # The description must be 2 to 256 characters in length, and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable connection log auditing for the SAG app. Valid values:
        # 
        # - **true**: enables connection log auditing for the SAG app.
        # 
        # - **false**: disables connection log auditing for the SAG app.
        self.enable_software_connection_audit = enable_software_connection_audit
        # The name of the Smart Access Gateway instance. 
        # 
        # The name must be 2 to 128 characters in length, and must start with a letter or a Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The location where the Smart Access Gateway instance is deployed.
        self.position = position
        # The region ID of the Smart Access Gateway instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The route synchronization mode for the on-premises network. Valid values:
        # 
        # - **static**: static routing.
        # 
        # - **dynamic**: dynamic routing.
        self.routing_strategy = routing_strategy
        # The threshold configured by the user for the offline lock feature. The value must be greater than or equal to 0.
        # 
        # Unit: seconds.
        self.security_lock_threshold = security_lock_threshold
        # The instance ID of the Smart Access Gateway.
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


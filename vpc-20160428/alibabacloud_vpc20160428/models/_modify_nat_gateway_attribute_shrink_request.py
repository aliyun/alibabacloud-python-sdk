# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNatGatewayAttributeShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        eip_bind_mode: str = None,
        enable_session_log: bool = None,
        icmp_reply_enabled: bool = None,
        log_delivery_shrink: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The description of the NAT gateway.
        # 
        # The description must be 1 to 128 characters in length, and cannot start with `http://` or `https://`.
        self.description = description
        # Modifies the mode in which the EIP is associated with the NAT gateway. The value can be empty or **NAT**, which specifies the NAT mode.
        # 
        # > 
        # 
        # *   You can only change **MULTI_BINDED** to **NAT**. You cannot change **NAT** to **MULTI_BINDED**. For more information about the **MULTI_BINDED** mode, see [CreateNatGateway](https://help.aliyun.com/document_detail/120219.html).
        # 
        # *   When you change the association mode, your network may be interrupted for seconds. The duration increases with the number of EIPs. You can change the association mode for at most 5 EIPs at the same time. We recommend changing the association mode during off-peak hours.
        # *   After the association mode is changed to **NAT**, the Internet NAT gateway is compatible with an IPv4 gateway. If an EIP is associated with a NAT gateway in NAT mode, the EIP occupies a private IP address of the vSwitch to which the NAT gateway belongs. Ensure the vSwitch has sufficient private IP addresses for EIPs to be associated with the NAT gateway.
        self.eip_bind_mode = eip_bind_mode
        # Whether to enable session logging, with values:
        # - **true**: Session logging is enabled. 
        # - **false**: Session logging is disabled.
        self.enable_session_log = enable_session_log
        # Specifies whether to enable the Internet Control Message Protocol (ICMP) non-retrieval feature. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        self.icmp_reply_enabled = icmp_reply_enabled
        # Session log configuration information.
        self.log_delivery_shrink = log_delivery_shrink
        # The name of the NAT gateway.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the NAT gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.description is not None:
            result['Description'] = self.description

        if self.eip_bind_mode is not None:
            result['EipBindMode'] = self.eip_bind_mode

        if self.enable_session_log is not None:
            result['EnableSessionLog'] = self.enable_session_log

        if self.icmp_reply_enabled is not None:
            result['IcmpReplyEnabled'] = self.icmp_reply_enabled

        if self.log_delivery_shrink is not None:
            result['LogDelivery'] = self.log_delivery_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

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
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EipBindMode') is not None:
            self.eip_bind_mode = m.get('EipBindMode')

        if m.get('EnableSessionLog') is not None:
            self.enable_session_log = m.get('EnableSessionLog')

        if m.get('IcmpReplyEnabled') is not None:
            self.icmp_reply_enabled = m.get('IcmpReplyEnabled')

        if m.get('LogDelivery') is not None:
            self.log_delivery_shrink = m.get('LogDelivery')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

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


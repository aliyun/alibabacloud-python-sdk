# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAllowedIpRequest(DaraModel):
    def __init__(
        self,
        allowed_list_ip: str = None,
        allowed_list_type: str = None,
        description: str = None,
        instance_id: str = None,
        port_range: str = None,
        region_id: str = None,
        update_type: str = None,
    ):
        # The IP addresses that you want to manage. You can specify a CIDR block. Example: **192.168.0.0/16**.
        # 
        # *   If the **UpdateType** parameter is set to **add**, specify one or more IP addresses for this parameter. Separate multiple IP addresses with commas (,).
        # *   If the **UpdateType** parameter is set to **delete**, specify only one IP address.
        # *   Exercise caution when you delete IP addresses.
        # 
        # This parameter is required.
        self.allowed_list_ip = allowed_list_ip
        # The type of the whitelist. Valid values:
        # 
        # *   **vpc**: a whitelist for access from a VPC.
        # *   **internet**: a whitelist for access from the Internet.
        # 
        # This parameter is required.
        self.allowed_list_type = allowed_list_type
        # The description of the whitelist.
        self.description = description
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The port range. Valid values:
        # 
        # *   **9092/9092**: Messages are transmitted in a virtual private cloud (VPC) by using the PLAINTEXT protocol.
        # *   **9093/9093**: Messages are transmitted over the Internet by using the SASL_SSL protocol.
        # *   **9094/9094**: Messages are transmitted in a VPC by using the SASL_PLAINTEXT protocol.
        # *   **9095/9095**: Messages are transmitted in a VPC by using the SASL_SSL protocol.
        # 
        # This parameter must correspond to **AllowdedListType**.
        # 
        # This parameter is required.
        self.port_range = port_range
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of configuration change. Valid values:
        # 
        # *   **add**
        # *   **delete**
        # 
        # This parameter is required.
        self.update_type = update_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_list_ip is not None:
            result['AllowedListIp'] = self.allowed_list_ip

        if self.allowed_list_type is not None:
            result['AllowedListType'] = self.allowed_list_type

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.update_type is not None:
            result['UpdateType'] = self.update_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedListIp') is not None:
            self.allowed_list_ip = m.get('AllowedListIp')

        if m.get('AllowedListType') is not None:
            self.allowed_list_type = m.get('AllowedListType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')

        return self


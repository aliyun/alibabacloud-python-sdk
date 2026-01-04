# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigUdpReflectRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The configuration of the filtering policy for UDP reflection attacks.
        # 
        # The value is a string that consists of a JSON struct. The JSON struct contains the following field:
        # 
        # *   **UdpSports**: the source ports of the UDP traffic that you want to block. This field is required and must be of the ARRAY type. Example: `[17,19]`.
        # 
        #     We recommend that you block the following source ports of UDP traffic:
        # 
        #     *   UDP 17: QOTD reflection attacks
        #     *   UDP 19: CharGEN reflection attacks
        #     *   UDP 69: TFTP reflection attacks
        #     *   UDP 111: Portmap reflection attacks
        #     *   UDP 123: NTP reflection attacks
        #     *   UDP 137: NetBIOS reflection attacks
        #     *   UDP 161: SNMPv2 reflection attacks
        #     *   UDP 389: CLDAP reflection attacks
        #     *   UDP 1194: OpenVPN reflection attacks
        #     *   UDP 1900: SSDP reflection attacks
        #     *   UDP 3389: RDP reflection attacks
        #     *   UDP 11211: memcached reflection attacks
        # 
        # This parameter is required.
        self.config = config
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the Anti-DDoS Proxy instance. Valid values:
        # 
        # *   **cn-hangzhou**: indicates an Anti-DDoS Proxy (Chinese Mainland) instance. This is the default value.
        # *   **ap-southeast-1**: indicates an Anti-DDoS Proxy (Outside Chinese Mainland) instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


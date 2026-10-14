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
        # The configuration of the UDP reflection attack attack prevention protection policy to add.
        # 
        # This parameter is a string that represents a JSON structure transformed into a character string. The JSON structure contains the following field:
        # 
        # - **UdpSports**: Array type. Required. The UDP reflection source ports to block. Example: `[17,19]`.
        # 
        #     Block the following source ports that are commonly used in UDP reflection attacks:
        # 
        #     - UDP 17: QOTD reflection attacks
        #     - UDP 19: CharGEN reflection attacks
        #     - UDP 69: TFTP reflection attacks
        #     - UDP 111: Portmap reflection attacks
        #     - UDP 123: NTP reflection attacks
        #     - UDP 137: NetBIOS reflection attacks
        #     - UDP 161: SNMPv2 reflection attacks
        #     - UDP 389: CLDAP reflection attacks
        #     - UDP 1194: OpenVPN reflection attacks
        #     - UDP 1900: SSDP reflection attacks
        #     - UDP 3389: RDP reflection attacks
        #     - UDP 11211: Memcached reflection attacks
        # 
        # This parameter is required.
        self.config = config
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance to manage.
        # 
        # > You can invoke [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) to query the IDs of all Anti-DDoS Pro or Anti-DDoS Premium instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the Anti-DDoS Pro or Anti-DDoS Premium instance. Valid values:
        # 
        # - **cn-hangzhou** (default): the Chinese mainland, which indicates an Anti-DDoS Pro instance.
        # - **ap-southeast-1**: outside the Chinese mainland, which indicates an Anti-DDoS Premium instance.
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


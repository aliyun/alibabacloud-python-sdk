# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHostsPortRequest(DaraModel):
    def __init__(
        self,
        host_ids: str = None,
        instance_id: str = None,
        port: str = None,
        protocol_name: str = None,
        region_id: str = None,
    ):
        # The ID of the host for which you want to change the port. The value is a JSON string. You can add up to 100 host IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # >  You can call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to query the IDs of hosts.
        # 
        # This parameter is required.
        self.host_ids = host_ids
        # The ID of the bastion host for which you want to change the port of the host.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new port of the host. The port number must be an integer. Valid values: 22 to 65535.
        # 
        # This parameter is required.
        self.port = port
        # The protocol that is used to connect to the host. Valid values:
        # 
        # *   **SSH**
        # *   **RDP**
        # 
        # This parameter is required.
        self.protocol_name = protocol_name
        # The region ID of the bastion host for which you want to change the port of the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


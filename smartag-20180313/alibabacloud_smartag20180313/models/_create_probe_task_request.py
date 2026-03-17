# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProbeTaskRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        enable: bool = None,
        packet_number: int = None,
        port: int = None,
        probe_task_source_address: str = None,
        protocol: str = None,
        region_id: str = None,
        sag_id: str = None,
        sn: str = None,
        task_name: str = None,
        type: str = None,
    ):
        # The domain name that is probed by the task. If the protocol of the probe task is ICMP or TCP, set the value to the IP address or domain name of the service that you want to probe. If the protocol of the probe task is HTTP, set the value to the URL of the service that you want to probe.
        # 
        # This parameter is required.
        self.domain = domain
        # Specifies whether to enable the probe task. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # This parameter is required.
        self.enable = enable
        # The number of probe packets transmitted by the probe task per minute.
        # 
        # Valid values: **1** to **60**.
        # 
        # > This parameter is required if the protocol of the probe task is ICMP. Ignore this parameter if the protocol of the probe task is not ICMP.
        self.packet_number = packet_number
        # The port that is probed by the task.
        # 
        # > This parameter is required if the protocol of the probe task is TCP. Ignore this parameter if the protocol of the probe task is not TCP.
        self.port = port
        # The source address of the probe task.
        # 
        # > This parameter is required if the task probes private networks.
        self.probe_task_source_address = probe_task_source_address
        # The protocol of the probe task. Valid values:
        # 
        # *   **ICMP**
        # *   **TCP**
        # *   **HTTP**
        # 
        # > Tasks that probe private networks support only ICMP and TCP.
        # 
        # This parameter is required.
        self.protocol = protocol
        # The region ID of the SAG instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.sag_id = sag_id
        # The serial number of the SAG device.
        # 
        # This parameter is required.
        self.sn = sn
        # The name of the probe task.
        self.task_name = task_name
        # The type of the probe task. Valid values:
        # 
        # *   **Internet**: probes a public network.
        # *   **Intranet**: probes a private network.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.packet_number is not None:
            result['PacketNumber'] = self.packet_number

        if self.port is not None:
            result['Port'] = self.port

        if self.probe_task_source_address is not None:
            result['ProbeTaskSourceAddress'] = self.probe_task_source_address

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sag_id is not None:
            result['SagId'] = self.sag_id

        if self.sn is not None:
            result['Sn'] = self.sn

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('PacketNumber') is not None:
            self.packet_number = m.get('PacketNumber')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProbeTaskSourceAddress') is not None:
            self.probe_task_source_address = m.get('ProbeTaskSourceAddress')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SagId') is not None:
            self.sag_id = m.get('SagId')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


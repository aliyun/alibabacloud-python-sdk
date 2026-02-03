# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class GetNisNetworkRankingResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetNisNetworkRankingResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetNisNetworkRankingResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNisNetworkRankingResponseBodyData(DaraModel):
    def __init__(
        self,
        active_session_count: float = None,
        asn: str = None,
        attachment_id: str = None,
        bandwidth_package_id: str = None,
        byte_count: float = None,
        city: str = None,
        country: str = None,
        destination_ip: str = None,
        destination_isp: str = None,
        destination_port: str = None,
        destination_region_no: str = None,
        destination_zone: str = None,
        ip: str = None,
        in_bps: float = None,
        in_pps: float = None,
        instance_id: str = None,
        isp: str = None,
        new_session_per_second: float = None,
        out_bps: float = None,
        out_pps: float = None,
        packet_count: float = None,
        protocol: str = None,
        province: str = None,
        rtt: float = None,
        region_no: str = None,
        retransmit_rate: float = None,
        source_ip: str = None,
        source_isp: str = None,
        source_port: str = None,
        source_zone: str = None,
        vbr_id: str = None,
    ):
        self.active_session_count = active_session_count
        self.asn = asn
        self.attachment_id = attachment_id
        self.bandwidth_package_id = bandwidth_package_id
        self.byte_count = byte_count
        self.city = city
        self.country = country
        self.destination_ip = destination_ip
        self.destination_isp = destination_isp
        self.destination_port = destination_port
        self.destination_region_no = destination_region_no
        self.destination_zone = destination_zone
        self.ip = ip
        self.in_bps = in_bps
        self.in_pps = in_pps
        self.instance_id = instance_id
        self.isp = isp
        self.new_session_per_second = new_session_per_second
        self.out_bps = out_bps
        self.out_pps = out_pps
        self.packet_count = packet_count
        self.protocol = protocol
        self.province = province
        self.rtt = rtt
        self.region_no = region_no
        self.retransmit_rate = retransmit_rate
        self.source_ip = source_ip
        self.source_isp = source_isp
        self.source_port = source_port
        self.source_zone = source_zone
        self.vbr_id = vbr_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_session_count is not None:
            result['ActiveSessionCount'] = self.active_session_count

        if self.asn is not None:
            result['Asn'] = self.asn

        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.byte_count is not None:
            result['ByteCount'] = self.byte_count

        if self.city is not None:
            result['City'] = self.city

        if self.country is not None:
            result['Country'] = self.country

        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip

        if self.destination_isp is not None:
            result['DestinationIsp'] = self.destination_isp

        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port

        if self.destination_region_no is not None:
            result['DestinationRegionNo'] = self.destination_region_no

        if self.destination_zone is not None:
            result['DestinationZone'] = self.destination_zone

        if self.ip is not None:
            result['IP'] = self.ip

        if self.in_bps is not None:
            result['InBps'] = self.in_bps

        if self.in_pps is not None:
            result['InPps'] = self.in_pps

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.new_session_per_second is not None:
            result['NewSessionPerSecond'] = self.new_session_per_second

        if self.out_bps is not None:
            result['OutBps'] = self.out_bps

        if self.out_pps is not None:
            result['OutPps'] = self.out_pps

        if self.packet_count is not None:
            result['PacketCount'] = self.packet_count

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.province is not None:
            result['Province'] = self.province

        if self.rtt is not None:
            result['RTT'] = self.rtt

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.retransmit_rate is not None:
            result['RetransmitRate'] = self.retransmit_rate

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.source_isp is not None:
            result['SourceIsp'] = self.source_isp

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.source_zone is not None:
            result['SourceZone'] = self.source_zone

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveSessionCount') is not None:
            self.active_session_count = m.get('ActiveSessionCount')

        if m.get('Asn') is not None:
            self.asn = m.get('Asn')

        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('ByteCount') is not None:
            self.byte_count = m.get('ByteCount')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')

        if m.get('DestinationIsp') is not None:
            self.destination_isp = m.get('DestinationIsp')

        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')

        if m.get('DestinationRegionNo') is not None:
            self.destination_region_no = m.get('DestinationRegionNo')

        if m.get('DestinationZone') is not None:
            self.destination_zone = m.get('DestinationZone')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')

        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('NewSessionPerSecond') is not None:
            self.new_session_per_second = m.get('NewSessionPerSecond')

        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')

        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')

        if m.get('PacketCount') is not None:
            self.packet_count = m.get('PacketCount')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RTT') is not None:
            self.rtt = m.get('RTT')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RetransmitRate') is not None:
            self.retransmit_rate = m.get('RetransmitRate')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SourceIsp') is not None:
            self.source_isp = m.get('SourceIsp')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('SourceZone') is not None:
            self.source_zone = m.get('SourceZone')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        return self


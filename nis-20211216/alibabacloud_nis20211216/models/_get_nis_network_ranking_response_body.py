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
        # The collection of cloud network metric ranking data.
        self.data = data
        # The request ID.
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
        global_country_code: str = None,
        global_province_code: str = None,
        ip: str = None,
        in_bps: float = None,
        in_pps: float = None,
        instance_id: str = None,
        isp: str = None,
        line_type: str = None,
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
        source_region: str = None,
        source_zone: str = None,
        vbr_id: str = None,
    ):
        # The number of concurrent connections.
        self.active_session_count = active_session_count
        # The autonomous system number (ASN) of the client ISP.
        self.asn = asn
        # The transit router attachment ID.
        self.attachment_id = attachment_id
        # The bandwidth package instance ID.
        self.bandwidth_package_id = bandwidth_package_id
        # The traffic volume in bytes.
        self.byte_count = byte_count
        # The city where the client is located.
        self.city = city
        # The country where the client is located.
        self.country = country
        # The destination IP address.
        self.destination_ip = destination_ip
        # The destination ISP.
        self.destination_isp = destination_isp
        # The destination port.
        self.destination_port = destination_port
        # The destination region ID.
        self.destination_region_no = destination_region_no
        # The destination zone for probing.
        self.destination_zone = destination_zone
        self.global_country_code = global_country_code
        self.global_province_code = global_province_code
        # The IP address.
        self.ip = ip
        # The inbound bandwidth. Unit: bit/s.
        self.in_bps = in_bps
        # The inbound packet rate. Unit: packets per second.
        self.in_pps = in_pps
        # The cloud resource instance ID corresponding to each scenario. For example, in the cross-region network traffic analysis scenario, this represents the CEN ID. In the public network scenario, this represents the EIP ID, ECS instance ID, or CLB ID.
        self.instance_id = instance_id
        # The ISP of the client.
        self.isp = isp
        self.line_type = line_type
        # The number of new connections per second.
        self.new_session_per_second = new_session_per_second
        # The outbound bandwidth. Unit: bit/s.
        self.out_bps = out_bps
        # The outbound packet rate. Unit: packets per second.
        self.out_pps = out_pps
        # The number of traffic packets.
        self.packet_count = packet_count
        # The network protocol.
        self.protocol = protocol
        # The province or state where the client is located.
        self.province = province
        # The latency. Unit: ms.
        self.rtt = rtt
        # The Alibaba Cloud region ID.
        self.region_no = region_no
        # The retransmission rate of TCP packets.
        self.retransmit_rate = retransmit_rate
        # The source IP address.
        self.source_ip = source_ip
        # The source Internet Service Provider (ISP).
        self.source_isp = source_isp
        # The source port.
        self.source_port = source_port
        self.source_region = source_region
        # The source zone for probing.
        self.source_zone = source_zone
        # The instance ID of the virtual border router (VBR).
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

        if self.global_country_code is not None:
            result['GlobalCountryCode'] = self.global_country_code

        if self.global_province_code is not None:
            result['GlobalProvinceCode'] = self.global_province_code

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

        if self.line_type is not None:
            result['LineType'] = self.line_type

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

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

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

        if m.get('GlobalCountryCode') is not None:
            self.global_country_code = m.get('GlobalCountryCode')

        if m.get('GlobalProvinceCode') is not None:
            self.global_province_code = m.get('GlobalProvinceCode')

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

        if m.get('LineType') is not None:
            self.line_type = m.get('LineType')

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

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('SourceZone') is not None:
            self.source_zone = m.get('SourceZone')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        return self


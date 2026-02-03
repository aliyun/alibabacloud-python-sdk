# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class GetInternetTupleResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetInternetTupleResponseBodyData] = None,
        request_id: str = None,
    ):
        # The ranking result of Internet traffic data.
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
                temp_model = main_models.GetInternetTupleResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInternetTupleResponseBodyData(DaraModel):
    def __init__(
        self,
        access_region: str = None,
        begin_time: str = None,
        byte_count: float = None,
        cloud_city: str = None,
        cloud_country: str = None,
        cloud_ip: str = None,
        cloud_isp: str = None,
        cloud_port: str = None,
        cloud_product: str = None,
        cloud_province: str = None,
        direction: str = None,
        in_byte_count: float = None,
        in_out_order_count: float = None,
        in_packet_count: float = None,
        in_retran_count: float = None,
        instance_id: str = None,
        other_city: str = None,
        other_country: str = None,
        other_ip: str = None,
        other_isp: str = None,
        other_port: str = None,
        other_product: str = None,
        other_province: str = None,
        out_byte_count: float = None,
        out_order_count: float = None,
        out_out_order_count: float = None,
        out_packet_count: float = None,
        out_retran_count: float = None,
        packet_count: float = None,
        protocol: str = None,
        retransmit_rate: float = None,
        rtt: float = None,
    ):
        # The access point of Alibaba Cloud.
        # 
        # >  This parameter is valid only if you set **InstanceId** to the instance ID of an Anycast elastic IP address (EIP).
        self.access_region = access_region
        # The beginning of the time range that you queried. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.begin_time = begin_time
        # The traffic volume. Unit: bytes.
        self.byte_count = byte_count
        # The local city.
        self.cloud_city = cloud_city
        # The local country or region.
        self.cloud_country = cloud_country
        # The local IP address.
        self.cloud_ip = cloud_ip
        # The local ISP.
        self.cloud_isp = cloud_isp
        # The local port.
        self.cloud_port = cloud_port
        # The service code of the instance to which the local IP address belongs.
        self.cloud_product = cloud_product
        # The local province.
        self.cloud_province = cloud_province
        # The direction of Internet traffic. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        self.direction = direction
        # The inbound traffic volume. Unit: bytes.
        self.in_byte_count = in_byte_count
        # The number of inbound disordered packets.
        self.in_out_order_count = in_out_order_count
        # The number of inbound packets.
        self.in_packet_count = in_packet_count
        # The number of inbound repeated packets.
        self.in_retran_count = in_retran_count
        # The ID of the instance to which the local IP address belongs.
        self.instance_id = instance_id
        # The remote city. In most cases, this parameter is empty if you set **OtherCountry** to a country except China.
        self.other_city = other_city
        # The remote country or region.
        self.other_country = other_country
        # The remote IP address.
        self.other_ip = other_ip
        # The remote ISP.
        self.other_isp = other_isp
        # The remote port.
        self.other_port = other_port
        # The service code of the instance to which the remote IP address belongs. If the IP address is not on the cloud, this parameter is empty.
        self.other_product = other_product
        # The remote province. In most cases, this parameter is empty if you set **OtherCountry** to a country except China.
        self.other_province = other_province
        # The outbound traffic volume. Unit: bytes.
        self.out_byte_count = out_byte_count
        # The number of disordered packets.
        self.out_order_count = out_order_count
        # The number of outbound disordered packets.
        self.out_out_order_count = out_out_order_count
        # The number of outbound packets.
        self.out_packet_count = out_packet_count
        # The number of outbound repeated packets.
        self.out_retran_count = out_retran_count
        # The number of packets.
        self.packet_count = packet_count
        # The protocol number.
        self.protocol = protocol
        # The retransmission rate of TCP packets.
        self.retransmit_rate = retransmit_rate
        # The round-trip time (RTT). Unit: milliseconds.
        self.rtt = rtt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_region is not None:
            result['AccessRegion'] = self.access_region

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.byte_count is not None:
            result['ByteCount'] = self.byte_count

        if self.cloud_city is not None:
            result['CloudCity'] = self.cloud_city

        if self.cloud_country is not None:
            result['CloudCountry'] = self.cloud_country

        if self.cloud_ip is not None:
            result['CloudIp'] = self.cloud_ip

        if self.cloud_isp is not None:
            result['CloudIsp'] = self.cloud_isp

        if self.cloud_port is not None:
            result['CloudPort'] = self.cloud_port

        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product

        if self.cloud_province is not None:
            result['CloudProvince'] = self.cloud_province

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.in_byte_count is not None:
            result['InByteCount'] = self.in_byte_count

        if self.in_out_order_count is not None:
            result['InOutOrderCount'] = self.in_out_order_count

        if self.in_packet_count is not None:
            result['InPacketCount'] = self.in_packet_count

        if self.in_retran_count is not None:
            result['InRetranCount'] = self.in_retran_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.other_city is not None:
            result['OtherCity'] = self.other_city

        if self.other_country is not None:
            result['OtherCountry'] = self.other_country

        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip

        if self.other_isp is not None:
            result['OtherIsp'] = self.other_isp

        if self.other_port is not None:
            result['OtherPort'] = self.other_port

        if self.other_product is not None:
            result['OtherProduct'] = self.other_product

        if self.other_province is not None:
            result['OtherProvince'] = self.other_province

        if self.out_byte_count is not None:
            result['OutByteCount'] = self.out_byte_count

        if self.out_order_count is not None:
            result['OutOrderCount'] = self.out_order_count

        if self.out_out_order_count is not None:
            result['OutOutOrderCount'] = self.out_out_order_count

        if self.out_packet_count is not None:
            result['OutPacketCount'] = self.out_packet_count

        if self.out_retran_count is not None:
            result['OutRetranCount'] = self.out_retran_count

        if self.packet_count is not None:
            result['PacketCount'] = self.packet_count

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.retransmit_rate is not None:
            result['RetransmitRate'] = self.retransmit_rate

        if self.rtt is not None:
            result['Rtt'] = self.rtt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRegion') is not None:
            self.access_region = m.get('AccessRegion')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('ByteCount') is not None:
            self.byte_count = m.get('ByteCount')

        if m.get('CloudCity') is not None:
            self.cloud_city = m.get('CloudCity')

        if m.get('CloudCountry') is not None:
            self.cloud_country = m.get('CloudCountry')

        if m.get('CloudIp') is not None:
            self.cloud_ip = m.get('CloudIp')

        if m.get('CloudIsp') is not None:
            self.cloud_isp = m.get('CloudIsp')

        if m.get('CloudPort') is not None:
            self.cloud_port = m.get('CloudPort')

        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')

        if m.get('CloudProvince') is not None:
            self.cloud_province = m.get('CloudProvince')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('InByteCount') is not None:
            self.in_byte_count = m.get('InByteCount')

        if m.get('InOutOrderCount') is not None:
            self.in_out_order_count = m.get('InOutOrderCount')

        if m.get('InPacketCount') is not None:
            self.in_packet_count = m.get('InPacketCount')

        if m.get('InRetranCount') is not None:
            self.in_retran_count = m.get('InRetranCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OtherCity') is not None:
            self.other_city = m.get('OtherCity')

        if m.get('OtherCountry') is not None:
            self.other_country = m.get('OtherCountry')

        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')

        if m.get('OtherIsp') is not None:
            self.other_isp = m.get('OtherIsp')

        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')

        if m.get('OtherProduct') is not None:
            self.other_product = m.get('OtherProduct')

        if m.get('OtherProvince') is not None:
            self.other_province = m.get('OtherProvince')

        if m.get('OutByteCount') is not None:
            self.out_byte_count = m.get('OutByteCount')

        if m.get('OutOrderCount') is not None:
            self.out_order_count = m.get('OutOrderCount')

        if m.get('OutOutOrderCount') is not None:
            self.out_out_order_count = m.get('OutOutOrderCount')

        if m.get('OutPacketCount') is not None:
            self.out_packet_count = m.get('OutPacketCount')

        if m.get('OutRetranCount') is not None:
            self.out_retran_count = m.get('OutRetranCount')

        if m.get('PacketCount') is not None:
            self.packet_count = m.get('PacketCount')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RetransmitRate') is not None:
            self.retransmit_rate = m.get('RetransmitRate')

        if m.get('Rtt') is not None:
            self.rtt = m.get('Rtt')

        return self


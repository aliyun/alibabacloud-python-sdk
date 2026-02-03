# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class DescribeNisTrafficRankingResponseBody(DaraModel):
    def __init__(
        self,
        flow_ranking_list: List[main_models.DescribeNisTrafficRankingResponseBodyFlowRankingList] = None,
        max_results: int = None,
        next_token: str = None,
        nis_traffic_ranking_id: str = None,
        request_id: str = None,
        status: str = None,
        total_count: int = None,
    ):
        self.flow_ranking_list = flow_ranking_list
        self.max_results = max_results
        self.next_token = next_token
        self.nis_traffic_ranking_id = nis_traffic_ranking_id
        self.request_id = request_id
        self.status = status
        self.total_count = total_count

    def validate(self):
        if self.flow_ranking_list:
            for v1 in self.flow_ranking_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FlowRankingList'] = []
        if self.flow_ranking_list is not None:
            for k1 in self.flow_ranking_list:
                result['FlowRankingList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.nis_traffic_ranking_id is not None:
            result['NisTrafficRankingId'] = self.nis_traffic_ranking_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_ranking_list = []
        if m.get('FlowRankingList') is not None:
            for k1 in m.get('FlowRankingList'):
                temp_model = main_models.DescribeNisTrafficRankingResponseBodyFlowRankingList()
                self.flow_ranking_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NisTrafficRankingId') is not None:
            self.nis_traffic_ranking_id = m.get('NisTrafficRankingId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNisTrafficRankingResponseBodyFlowRankingList(DaraModel):
    def __init__(
        self,
        binding_resource_id: str = None,
        binding_resource_type: str = None,
        bytes: float = None,
        bytes_rate: float = None,
        client_asn: str = None,
        client_city: str = None,
        client_country: str = None,
        client_isp: str = None,
        client_province: str = None,
        destination_ip: str = None,
        destination_port: str = None,
        destination_region_no: str = None,
        direction: str = None,
        dscp: str = None,
        ecs_id: str = None,
        instance_id: str = None,
        network_interface_id: str = None,
        packets: float = None,
        packets_lost_blackhole: float = None,
        packets_lost_no_route: float = None,
        packets_lost_ttlexpired: float = None,
        protocol: str = None,
        public_ip_address: str = None,
        region_id: str = None,
        round_trip_time: float = None,
        source_ip: str = None,
        source_port: str = None,
        source_region_no: str = None,
        traffic_path: str = None,
        transit_router_attachment_id: str = None,
        transit_router_destination_account_id: str = None,
        transit_router_destination_available_zone: str = None,
        transit_router_destination_network_interface: str = None,
        transit_router_destination_resource_id: str = None,
        transit_router_destination_vswitch_id: str = None,
        transit_router_id: str = None,
        transit_router_pair_attachment_id: str = None,
        transit_router_source_account_id: str = None,
        transit_router_source_available_zone: str = None,
        transit_router_source_network_interface: str = None,
        transit_router_source_resource_id: str = None,
        transit_router_source_vswitch_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.binding_resource_id = binding_resource_id
        self.binding_resource_type = binding_resource_type
        self.bytes = bytes
        self.bytes_rate = bytes_rate
        self.client_asn = client_asn
        self.client_city = client_city
        self.client_country = client_country
        self.client_isp = client_isp
        self.client_province = client_province
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.destination_region_no = destination_region_no
        self.direction = direction
        self.dscp = dscp
        self.ecs_id = ecs_id
        self.instance_id = instance_id
        self.network_interface_id = network_interface_id
        self.packets = packets
        self.packets_lost_blackhole = packets_lost_blackhole
        self.packets_lost_no_route = packets_lost_no_route
        self.packets_lost_ttlexpired = packets_lost_ttlexpired
        self.protocol = protocol
        self.public_ip_address = public_ip_address
        self.region_id = region_id
        self.round_trip_time = round_trip_time
        self.source_ip = source_ip
        self.source_port = source_port
        self.source_region_no = source_region_no
        self.traffic_path = traffic_path
        self.transit_router_attachment_id = transit_router_attachment_id
        self.transit_router_destination_account_id = transit_router_destination_account_id
        self.transit_router_destination_available_zone = transit_router_destination_available_zone
        self.transit_router_destination_network_interface = transit_router_destination_network_interface
        self.transit_router_destination_resource_id = transit_router_destination_resource_id
        self.transit_router_destination_vswitch_id = transit_router_destination_vswitch_id
        self.transit_router_id = transit_router_id
        self.transit_router_pair_attachment_id = transit_router_pair_attachment_id
        self.transit_router_source_account_id = transit_router_source_account_id
        self.transit_router_source_available_zone = transit_router_source_available_zone
        self.transit_router_source_network_interface = transit_router_source_network_interface
        self.transit_router_source_resource_id = transit_router_source_resource_id
        self.transit_router_source_vswitch_id = transit_router_source_vswitch_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_resource_id is not None:
            result['BindingResourceId'] = self.binding_resource_id

        if self.binding_resource_type is not None:
            result['BindingResourceType'] = self.binding_resource_type

        if self.bytes is not None:
            result['Bytes'] = self.bytes

        if self.bytes_rate is not None:
            result['BytesRate'] = self.bytes_rate

        if self.client_asn is not None:
            result['ClientAsn'] = self.client_asn

        if self.client_city is not None:
            result['ClientCity'] = self.client_city

        if self.client_country is not None:
            result['ClientCountry'] = self.client_country

        if self.client_isp is not None:
            result['ClientIsp'] = self.client_isp

        if self.client_province is not None:
            result['ClientProvince'] = self.client_province

        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip

        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port

        if self.destination_region_no is not None:
            result['DestinationRegionNo'] = self.destination_region_no

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dscp is not None:
            result['Dscp'] = self.dscp

        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.packets is not None:
            result['Packets'] = self.packets

        if self.packets_lost_blackhole is not None:
            result['PacketsLostBlackhole'] = self.packets_lost_blackhole

        if self.packets_lost_no_route is not None:
            result['PacketsLostNoRoute'] = self.packets_lost_no_route

        if self.packets_lost_ttlexpired is not None:
            result['PacketsLostTTLExpired'] = self.packets_lost_ttlexpired

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.round_trip_time is not None:
            result['RoundTripTime'] = self.round_trip_time

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.source_region_no is not None:
            result['SourceRegionNo'] = self.source_region_no

        if self.traffic_path is not None:
            result['TrafficPath'] = self.traffic_path

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_destination_account_id is not None:
            result['TransitRouterDestinationAccountId'] = self.transit_router_destination_account_id

        if self.transit_router_destination_available_zone is not None:
            result['TransitRouterDestinationAvailableZone'] = self.transit_router_destination_available_zone

        if self.transit_router_destination_network_interface is not None:
            result['TransitRouterDestinationNetworkInterface'] = self.transit_router_destination_network_interface

        if self.transit_router_destination_resource_id is not None:
            result['TransitRouterDestinationResourceId'] = self.transit_router_destination_resource_id

        if self.transit_router_destination_vswitch_id is not None:
            result['TransitRouterDestinationVSwitchId'] = self.transit_router_destination_vswitch_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_pair_attachment_id is not None:
            result['TransitRouterPairAttachmentId'] = self.transit_router_pair_attachment_id

        if self.transit_router_source_account_id is not None:
            result['TransitRouterSourceAccountId'] = self.transit_router_source_account_id

        if self.transit_router_source_available_zone is not None:
            result['TransitRouterSourceAvailableZone'] = self.transit_router_source_available_zone

        if self.transit_router_source_network_interface is not None:
            result['TransitRouterSourceNetworkInterface'] = self.transit_router_source_network_interface

        if self.transit_router_source_resource_id is not None:
            result['TransitRouterSourceResourceId'] = self.transit_router_source_resource_id

        if self.transit_router_source_vswitch_id is not None:
            result['TransitRouterSourceVSwitchId'] = self.transit_router_source_vswitch_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingResourceId') is not None:
            self.binding_resource_id = m.get('BindingResourceId')

        if m.get('BindingResourceType') is not None:
            self.binding_resource_type = m.get('BindingResourceType')

        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')

        if m.get('BytesRate') is not None:
            self.bytes_rate = m.get('BytesRate')

        if m.get('ClientAsn') is not None:
            self.client_asn = m.get('ClientAsn')

        if m.get('ClientCity') is not None:
            self.client_city = m.get('ClientCity')

        if m.get('ClientCountry') is not None:
            self.client_country = m.get('ClientCountry')

        if m.get('ClientIsp') is not None:
            self.client_isp = m.get('ClientIsp')

        if m.get('ClientProvince') is not None:
            self.client_province = m.get('ClientProvince')

        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')

        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')

        if m.get('DestinationRegionNo') is not None:
            self.destination_region_no = m.get('DestinationRegionNo')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('Dscp') is not None:
            self.dscp = m.get('Dscp')

        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('Packets') is not None:
            self.packets = m.get('Packets')

        if m.get('PacketsLostBlackhole') is not None:
            self.packets_lost_blackhole = m.get('PacketsLostBlackhole')

        if m.get('PacketsLostNoRoute') is not None:
            self.packets_lost_no_route = m.get('PacketsLostNoRoute')

        if m.get('PacketsLostTTLExpired') is not None:
            self.packets_lost_ttlexpired = m.get('PacketsLostTTLExpired')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoundTripTime') is not None:
            self.round_trip_time = m.get('RoundTripTime')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('SourceRegionNo') is not None:
            self.source_region_no = m.get('SourceRegionNo')

        if m.get('TrafficPath') is not None:
            self.traffic_path = m.get('TrafficPath')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterDestinationAccountId') is not None:
            self.transit_router_destination_account_id = m.get('TransitRouterDestinationAccountId')

        if m.get('TransitRouterDestinationAvailableZone') is not None:
            self.transit_router_destination_available_zone = m.get('TransitRouterDestinationAvailableZone')

        if m.get('TransitRouterDestinationNetworkInterface') is not None:
            self.transit_router_destination_network_interface = m.get('TransitRouterDestinationNetworkInterface')

        if m.get('TransitRouterDestinationResourceId') is not None:
            self.transit_router_destination_resource_id = m.get('TransitRouterDestinationResourceId')

        if m.get('TransitRouterDestinationVSwitchId') is not None:
            self.transit_router_destination_vswitch_id = m.get('TransitRouterDestinationVSwitchId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterPairAttachmentId') is not None:
            self.transit_router_pair_attachment_id = m.get('TransitRouterPairAttachmentId')

        if m.get('TransitRouterSourceAccountId') is not None:
            self.transit_router_source_account_id = m.get('TransitRouterSourceAccountId')

        if m.get('TransitRouterSourceAvailableZone') is not None:
            self.transit_router_source_available_zone = m.get('TransitRouterSourceAvailableZone')

        if m.get('TransitRouterSourceNetworkInterface') is not None:
            self.transit_router_source_network_interface = m.get('TransitRouterSourceNetworkInterface')

        if m.get('TransitRouterSourceResourceId') is not None:
            self.transit_router_source_resource_id = m.get('TransitRouterSourceResourceId')

        if m.get('TransitRouterSourceVSwitchId') is not None:
            self.transit_router_source_vswitch_id = m.get('TransitRouterSourceVSwitchId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self


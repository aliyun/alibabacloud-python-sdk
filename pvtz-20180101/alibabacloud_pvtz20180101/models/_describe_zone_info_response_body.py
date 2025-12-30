# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeZoneInfoResponseBody(DaraModel):
    def __init__(
        self,
        bind_edge_dns_clusters: main_models.DescribeZoneInfoResponseBodyBindEdgeDnsClusters = None,
        bind_vpcs: main_models.DescribeZoneInfoResponseBodyBindVpcs = None,
        create_time: str = None,
        create_timestamp: int = None,
        creator: str = None,
        creator_type: str = None,
        dns_group: str = None,
        dns_group_changing: bool = None,
        is_ptr: bool = None,
        proxy_pattern: str = None,
        record_count: int = None,
        remark: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        slave_dns: bool = None,
        update_time: str = None,
        update_timestamp: int = None,
        zone_id: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        zone_type: str = None,
    ):
        self.bind_edge_dns_clusters = bind_edge_dns_clusters
        # The VPCs associated with the zone.
        self.bind_vpcs = bind_vpcs
        # The time when the zone was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the zone was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The creator of the zone.
        self.creator = creator
        # The type of the creator.
        self.creator_type = creator_type
        # The logical location type of the built-in authoritative module in which the zone is added. Valid values:
        # 
        # *   **NORMAL_ZONE**: regular module
        # *   **FAST_ZONE**: acceleration module
        self.dns_group = dns_group
        # Indicates whether the zone is being removed to another logical location. Valid values:
        # 
        # *   true
        # *   false
        self.dns_group_changing = dns_group_changing
        # Indicates whether the zone is a reverse lookup zone. Valid values:
        # 
        # *   true
        # *   false
        self.is_ptr = is_ptr
        # Indicates whether the recursive resolution proxy for subdomain names is enabled. Valid values:
        # 
        # *   ZONE: The recursive resolution proxy for subdomain names is disabled. In this case, NXDOMAIN is returned if the queried domain name does not exist in the zone.
        # *   RECORD: The recursive resolution proxy for subdomain names is enabled. In this case, if the queried domain name does not exist in the zone, DNS requests are recursively forwarded to the forward module and then to the recursion module until DNS results are returned.
        self.proxy_pattern = proxy_pattern
        # The total number of DNS records added in the zone.
        self.record_count = record_count
        # The description of the zone.
        self.remark = remark
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the zone belongs.
        self.resource_group_id = resource_group_id
        # Indicates whether the secondary Domain Name System (DNS) feature is enabled for the zone. Valid values:
        # 
        # *   **true**: The secondary DNS feature is enabled.
        # *   **false**: The secondary DNS feature is disabled.
        self.slave_dns = slave_dns
        # The time when the zone was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the zone was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The zone ID. This ID uniquely identifies the zone.
        self.zone_id = zone_id
        # The zone name.
        self.zone_name = zone_name
        # The tag added to the zone.
        self.zone_tag = zone_tag
        # The zone type. Valid values:
        # 
        # *   **AUTH_ZONE**: authoritative zone
        # *   **CLOUD_PRODUCT_ZONE**: authoritative zone for cloud services
        self.zone_type = zone_type

    def validate(self):
        if self.bind_edge_dns_clusters:
            self.bind_edge_dns_clusters.validate()
        if self.bind_vpcs:
            self.bind_vpcs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_edge_dns_clusters is not None:
            result['BindEdgeDnsClusters'] = self.bind_edge_dns_clusters.to_map()

        if self.bind_vpcs is not None:
            result['BindVpcs'] = self.bind_vpcs.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type

        if self.dns_group is not None:
            result['DnsGroup'] = self.dns_group

        if self.dns_group_changing is not None:
            result['DnsGroupChanging'] = self.dns_group_changing

        if self.is_ptr is not None:
            result['IsPtr'] = self.is_ptr

        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slave_dns is not None:
            result['SlaveDns'] = self.slave_dns

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag

        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindEdgeDnsClusters') is not None:
            temp_model = main_models.DescribeZoneInfoResponseBodyBindEdgeDnsClusters()
            self.bind_edge_dns_clusters = temp_model.from_map(m.get('BindEdgeDnsClusters'))

        if m.get('BindVpcs') is not None:
            temp_model = main_models.DescribeZoneInfoResponseBodyBindVpcs()
            self.bind_vpcs = temp_model.from_map(m.get('BindVpcs'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')

        if m.get('DnsGroup') is not None:
            self.dns_group = m.get('DnsGroup')

        if m.get('DnsGroupChanging') is not None:
            self.dns_group_changing = m.get('DnsGroupChanging')

        if m.get('IsPtr') is not None:
            self.is_ptr = m.get('IsPtr')

        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlaveDns') is not None:
            self.slave_dns = m.get('SlaveDns')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

class DescribeZoneInfoResponseBodyBindVpcs(DaraModel):
    def __init__(
        self,
        vpc: List[main_models.DescribeZoneInfoResponseBodyBindVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for v1 in self.vpc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Vpc'] = []
        if self.vpc is not None:
            for k1 in self.vpc:
                result['Vpc'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k1 in m.get('Vpc'):
                temp_model = main_models.DescribeZoneInfoResponseBodyBindVpcsVpc()
                self.vpc.append(temp_model.from_map(k1))

        return self

class DescribeZoneInfoResponseBodyBindVpcsVpc(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_type: str = None,
        vpc_user_id: int = None,
    ):
        # The region ID of the VPC.
        self.region_id = region_id
        # The name of the region where the VPC resides.
        self.region_name = region_name
        # The VPC ID. This ID uniquely identifies the VPC.
        self.vpc_id = vpc_id
        # The VPC name.
        self.vpc_name = vpc_name
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
        self.vpc_type = vpc_type
        # The user ID to which the VPC belongs. If null is returned, the VPC belongs to the current user.
        self.vpc_user_id = vpc_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        if self.vpc_user_id is not None:
            result['VpcUserId'] = self.vpc_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        if m.get('VpcUserId') is not None:
            self.vpc_user_id = m.get('VpcUserId')

        return self

class DescribeZoneInfoResponseBodyBindEdgeDnsClusters(DaraModel):
    def __init__(
        self,
        edge_dns_cluster: List[main_models.DescribeZoneInfoResponseBodyBindEdgeDnsClustersEdgeDnsCluster] = None,
    ):
        self.edge_dns_cluster = edge_dns_cluster

    def validate(self):
        if self.edge_dns_cluster:
            for v1 in self.edge_dns_cluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EdgeDnsCluster'] = []
        if self.edge_dns_cluster is not None:
            for k1 in self.edge_dns_cluster:
                result['EdgeDnsCluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge_dns_cluster = []
        if m.get('EdgeDnsCluster') is not None:
            for k1 in m.get('EdgeDnsCluster'):
                temp_model = main_models.DescribeZoneInfoResponseBodyBindEdgeDnsClustersEdgeDnsCluster()
                self.edge_dns_cluster.append(temp_model.from_map(k1))

        return self

class DescribeZoneInfoResponseBodyBindEdgeDnsClustersEdgeDnsCluster(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_user_id: int = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_user_id = cluster_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_user_id is not None:
            result['ClusterUserId'] = self.cluster_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterUserId') is not None:
            self.cluster_user_id = m.get('ClusterUserId')

        return self


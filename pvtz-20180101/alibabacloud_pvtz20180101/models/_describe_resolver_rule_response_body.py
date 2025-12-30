# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeResolverRuleResponseBody(DaraModel):
    def __init__(
        self,
        bind_edge_dns_clusters: List[main_models.DescribeResolverRuleResponseBodyBindEdgeDnsClusters] = None,
        bind_vpcs: List[main_models.DescribeResolverRuleResponseBodyBindVpcs] = None,
        create_time: str = None,
        create_timestamp: int = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        forward_ips: List[main_models.DescribeResolverRuleResponseBodyForwardIps] = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        zone_name: str = None,
    ):
        self.bind_edge_dns_clusters = bind_edge_dns_clusters
        # The virtual private clouds (VPCs) that are associated with the forwarding rule.
        self.bind_vpcs = bind_vpcs
        # The time when the forwarding rule was created.
        self.create_time = create_time
        # The time when the forwarding rule was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The endpoint name.
        self.endpoint_name = endpoint_name
        # The destination IP addresses.
        self.forward_ips = forward_ips
        # The ID of the forwarding rule.
        self.id = id
        # The name of the forwarding rule.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The type of the forwarding rule. Valid value:
        # 
        # OUTBOUND: outbound forwarding rule. This type of rule forwards Domain Name System (DNS) requests to one or more external IP addresses.
        self.type = type
        # The time when the forwarding rule was updated.
        self.update_time = update_time
        # The time when the forwarding rule was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The name of the forward zone.
        self.zone_name = zone_name

    def validate(self):
        if self.bind_edge_dns_clusters:
            for v1 in self.bind_edge_dns_clusters:
                 if v1:
                    v1.validate()
        if self.bind_vpcs:
            for v1 in self.bind_vpcs:
                 if v1:
                    v1.validate()
        if self.forward_ips:
            for v1 in self.forward_ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BindEdgeDnsClusters'] = []
        if self.bind_edge_dns_clusters is not None:
            for k1 in self.bind_edge_dns_clusters:
                result['BindEdgeDnsClusters'].append(k1.to_map() if k1 else None)

        result['BindVpcs'] = []
        if self.bind_vpcs is not None:
            for k1 in self.bind_vpcs:
                result['BindVpcs'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        result['ForwardIps'] = []
        if self.forward_ips is not None:
            for k1 in self.forward_ips:
                result['ForwardIps'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bind_edge_dns_clusters = []
        if m.get('BindEdgeDnsClusters') is not None:
            for k1 in m.get('BindEdgeDnsClusters'):
                temp_model = main_models.DescribeResolverRuleResponseBodyBindEdgeDnsClusters()
                self.bind_edge_dns_clusters.append(temp_model.from_map(k1))

        self.bind_vpcs = []
        if m.get('BindVpcs') is not None:
            for k1 in m.get('BindVpcs'):
                temp_model = main_models.DescribeResolverRuleResponseBodyBindVpcs()
                self.bind_vpcs.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        self.forward_ips = []
        if m.get('ForwardIps') is not None:
            for k1 in m.get('ForwardIps'):
                temp_model = main_models.DescribeResolverRuleResponseBodyForwardIps()
                self.forward_ips.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

class DescribeResolverRuleResponseBodyForwardIps(DaraModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
    ):
        # The destination IP address.
        self.ip = ip
        # The port number.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class DescribeResolverRuleResponseBodyBindVpcs(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_type: str = None,
        vpc_user_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The region name.
        self.region_name = region_name
        # The VPC ID.
        self.vpc_id = vpc_id
        # The VPC name.
        self.vpc_name = vpc_name
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
        self.vpc_type = vpc_type
        # The ID of the user to which the VPC belongs.
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

class DescribeResolverRuleResponseBodyBindEdgeDnsClusters(DaraModel):
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


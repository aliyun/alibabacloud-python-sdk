# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListTrafficMirrorFiltersResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
        traffic_mirror_filters: List[main_models.ListTrafficMirrorFiltersResponseBodyTrafficMirrorFilters] = None,
    ):
        # The number of entries returned.
        self.count = count
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count
        # The information about the filters.
        self.traffic_mirror_filters = traffic_mirror_filters

    def validate(self):
        if self.traffic_mirror_filters:
            for v1 in self.traffic_mirror_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TrafficMirrorFilters'] = []
        if self.traffic_mirror_filters is not None:
            for k1 in self.traffic_mirror_filters:
                result['TrafficMirrorFilters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.traffic_mirror_filters = []
        if m.get('TrafficMirrorFilters') is not None:
            for k1 in m.get('TrafficMirrorFilters'):
                temp_model = main_models.ListTrafficMirrorFiltersResponseBodyTrafficMirrorFilters()
                self.traffic_mirror_filters.append(temp_model.from_map(k1))

        return self

class ListTrafficMirrorFiltersResponseBodyTrafficMirrorFilters(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        egress_rules: List[main_models.ListTrafficMirrorFiltersResponseBodyTrafficMirrorFiltersEgressRules] = None,
        ingress_rules: List[main_models.ListTrafficMirrorFiltersResponseBodyTrafficMirrorFiltersIngressRules] = None,
        resource_group_id: str = None,
        tags: List[main_models.ListTrafficMirrorFiltersResponseBodyTrafficMirrorFiltersTags] = None,
        traffic_mirror_filter_description: str = None,
        traffic_mirror_filter_id: str = None,
        traffic_mirror_filter_name: str = None,
        traffic_mirror_filter_status: str = None,
    ):
        # The time when the filter is created.
        self.creation_time = creation_time
        # The information about the outbound rules.
        self.egress_rules = egress_rules
        # The information about the inbound rules.
        self.ingress_rules = ingress_rules
        # The ID of the resource group to which the traffic mirror session belongs.
        self.resource_group_id = resource_group_id
        # The tag list.
        self.tags = tags
        # The description of the filter.
        self.traffic_mirror_filter_description = traffic_mirror_filter_description
        # The ID of the filter.
        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        # The filter name.
        self.traffic_mirror_filter_name = traffic_mirror_filter_name
        # The status of the filter. Valid values:
        # 
        # *   **Creating**
        # *   **Created**
        # *   **Modifying**
        # *   **Deleting**
        self.traffic_mirror_filter_status = traffic_mirror_filter_status

    def validate(self):
        if self.egress_rules:
            for v1 in self.egress_rules:
                 if v1:
                    v1.validate()
        if self.ingress_rules:
            for v1 in self.ingress_rules:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        result['EgressRules'] = []
        if self.egress_rules is not None:
            for k1 in self.egress_rules:
                result['EgressRules'].append(k1.to_map() if k1 else None)

        result['IngressRules'] = []
        if self.ingress_rules is not None:
            for k1 in self.ingress_rules:
                result['IngressRules'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.traffic_mirror_filter_description is not None:
            result['TrafficMirrorFilterDescription'] = self.traffic_mirror_filter_description

        if self.traffic_mirror_filter_id is not None:
            result['TrafficMirrorFilterId'] = self.traffic_mirror_filter_id

        if self.traffic_mirror_filter_name is not None:
            result['TrafficMirrorFilterName'] = self.traffic_mirror_filter_name

        if self.traffic_mirror_filter_status is not None:
            result['TrafficMirrorFilterStatus'] = self.traffic_mirror_filter_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        self.egress_rules = []
        if m.get('EgressRules') is not None:
            for k1 in m.get('EgressRules'):
                temp_model = main_models.ListTrafficMirrorFiltersResponseBodyTrafficMirrorFiltersEgressRules()
                self.egress_rules.append(temp_model.from_map(k1))

        self.ingress_rules = []
        if m.get('IngressRules') is not None:
            for k1 in m.get('IngressRules'):
                temp_model = main_models.ListTrafficMirrorFiltersResponseBodyTrafficMirrorFiltersIngressRules()
                self.ingress_rules.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTrafficMirrorFiltersResponseBodyTrafficMirrorFiltersTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TrafficMirrorFilterDescription') is not None:
            self.traffic_mirror_filter_description = m.get('TrafficMirrorFilterDescription')

        if m.get('TrafficMirrorFilterId') is not None:
            self.traffic_mirror_filter_id = m.get('TrafficMirrorFilterId')

        if m.get('TrafficMirrorFilterName') is not None:
            self.traffic_mirror_filter_name = m.get('TrafficMirrorFilterName')

        if m.get('TrafficMirrorFilterStatus') is not None:
            self.traffic_mirror_filter_status = m.get('TrafficMirrorFilterStatus')

        return self

class ListTrafficMirrorFiltersResponseBodyTrafficMirrorFiltersTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListTrafficMirrorFiltersResponseBodyTrafficMirrorFiltersIngressRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        destination_cidr_block: str = None,
        destination_port_range: str = None,
        ip_version: str = None,
        priority: int = None,
        protocol: str = None,
        source_cidr_block: str = None,
        source_port_range: str = None,
        traffic_direction: str = None,
        traffic_mirror_filter_id: str = None,
        traffic_mirror_filter_rule_id: str = None,
        traffic_mirror_filter_rule_status: str = None,
    ):
        # The action of the inbound rule. Valid values:
        # 
        # *   **accept**
        # *   **drop**
        self.action = action
        # The destination CIDR block of the inbound traffic.
        self.destination_cidr_block = destination_cidr_block
        # The destination port range of the inbound traffic.
        self.destination_port_range = destination_port_range
        # The version of IP protocol.
        self.ip_version = ip_version
        # The priority of the inbound rule. A smaller value indicates a higher priority.
        self.priority = priority
        # The protocol that is used by the inbound traffic to be mirrored. Valid values:
        # 
        # *   **ALL**
        # *   **ICMP**
        # *   **TCP**
        # *   **UDP**
        self.protocol = protocol
        # The source CIDR block of the inbound traffic.
        self.source_cidr_block = source_cidr_block
        # The destination port range of the inbound traffic.
        self.source_port_range = source_port_range
        # The direction of the network traffic. Valid values:
        # 
        # *   **egress**
        # *   **ingress**
        self.traffic_direction = traffic_direction
        # The ID of the filter associated with the inbound rule.
        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        # The ID of the inbound rule.
        self.traffic_mirror_filter_rule_id = traffic_mirror_filter_rule_id
        # The status of the inbound rule. Valid values:
        # 
        # *   **Creating**
        # *   **Created**
        # *   **Modifying**
        # *   **Deleting**
        self.traffic_mirror_filter_rule_status = traffic_mirror_filter_rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.destination_port_range is not None:
            result['DestinationPortRange'] = self.destination_port_range

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.source_cidr_block is not None:
            result['SourceCidrBlock'] = self.source_cidr_block

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.traffic_direction is not None:
            result['TrafficDirection'] = self.traffic_direction

        if self.traffic_mirror_filter_id is not None:
            result['TrafficMirrorFilterId'] = self.traffic_mirror_filter_id

        if self.traffic_mirror_filter_rule_id is not None:
            result['TrafficMirrorFilterRuleId'] = self.traffic_mirror_filter_rule_id

        if self.traffic_mirror_filter_rule_status is not None:
            result['TrafficMirrorFilterRuleStatus'] = self.traffic_mirror_filter_rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('DestinationPortRange') is not None:
            self.destination_port_range = m.get('DestinationPortRange')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SourceCidrBlock') is not None:
            self.source_cidr_block = m.get('SourceCidrBlock')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('TrafficDirection') is not None:
            self.traffic_direction = m.get('TrafficDirection')

        if m.get('TrafficMirrorFilterId') is not None:
            self.traffic_mirror_filter_id = m.get('TrafficMirrorFilterId')

        if m.get('TrafficMirrorFilterRuleId') is not None:
            self.traffic_mirror_filter_rule_id = m.get('TrafficMirrorFilterRuleId')

        if m.get('TrafficMirrorFilterRuleStatus') is not None:
            self.traffic_mirror_filter_rule_status = m.get('TrafficMirrorFilterRuleStatus')

        return self

class ListTrafficMirrorFiltersResponseBodyTrafficMirrorFiltersEgressRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        destination_cidr_block: str = None,
        destination_port_range: str = None,
        ip_version: str = None,
        priority: int = None,
        protocol: str = None,
        source_cidr_block: str = None,
        source_port_range: str = None,
        traffic_direction: str = None,
        traffic_mirror_filter_id: str = None,
        traffic_mirror_filter_rule_id: str = None,
        traffic_mirror_filter_rule_status: str = None,
    ):
        # The action of the outbound rule. Valid values:
        # 
        # *   **accept**
        # *   **drop**
        self.action = action
        # The destination CIDR block of the outbound traffic.
        self.destination_cidr_block = destination_cidr_block
        # The destination port range of the outbound traffic.
        self.destination_port_range = destination_port_range
        # The version of IP protocol.
        self.ip_version = ip_version
        # The priority of the outbound rule. A smaller value indicates a higher priority.
        self.priority = priority
        # The protocol that is used by the outbound traffic to be mirrored. Valid values:
        # 
        # *   **ALL**
        # *   **ICMP**
        # *   **TCP**
        # *   **UDP**
        self.protocol = protocol
        # The source CIDR block of the outbound traffic.
        self.source_cidr_block = source_cidr_block
        # The source port range of the outbound traffic.
        self.source_port_range = source_port_range
        # The direction of the network traffic. Valid values:
        # 
        # *   **egress**
        # *   **ingress**
        self.traffic_direction = traffic_direction
        # The ID of the filter associated with the outbound rule.
        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        # The ID of the outbound rule.
        self.traffic_mirror_filter_rule_id = traffic_mirror_filter_rule_id
        # The status of the outbound rule. Valid values:
        # 
        # *   **Creating**
        # *   **Created**
        # *   **Modifying**
        # *   **Deleting**
        self.traffic_mirror_filter_rule_status = traffic_mirror_filter_rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.destination_port_range is not None:
            result['DestinationPortRange'] = self.destination_port_range

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.source_cidr_block is not None:
            result['SourceCidrBlock'] = self.source_cidr_block

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.traffic_direction is not None:
            result['TrafficDirection'] = self.traffic_direction

        if self.traffic_mirror_filter_id is not None:
            result['TrafficMirrorFilterId'] = self.traffic_mirror_filter_id

        if self.traffic_mirror_filter_rule_id is not None:
            result['TrafficMirrorFilterRuleId'] = self.traffic_mirror_filter_rule_id

        if self.traffic_mirror_filter_rule_status is not None:
            result['TrafficMirrorFilterRuleStatus'] = self.traffic_mirror_filter_rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('DestinationPortRange') is not None:
            self.destination_port_range = m.get('DestinationPortRange')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SourceCidrBlock') is not None:
            self.source_cidr_block = m.get('SourceCidrBlock')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('TrafficDirection') is not None:
            self.traffic_direction = m.get('TrafficDirection')

        if m.get('TrafficMirrorFilterId') is not None:
            self.traffic_mirror_filter_id = m.get('TrafficMirrorFilterId')

        if m.get('TrafficMirrorFilterRuleId') is not None:
            self.traffic_mirror_filter_rule_id = m.get('TrafficMirrorFilterRuleId')

        if m.get('TrafficMirrorFilterRuleStatus') is not None:
            self.traffic_mirror_filter_rule_status = m.get('TrafficMirrorFilterRuleStatus')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class ModifyFullLogTtlRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, ttl=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.ttl = ttl                  # type: int
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.ttl, 'ttl')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('Ttl') is not None:
            self.ttl = map.get('Ttl')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        return self


class ModifyFullLogTtlResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ReleaseValueAddedRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None):
        self.source_ip = source_ip      # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        return self


class ReleaseValueAddedResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ListValueAddedRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        return self


class ListValueAddedResponse(TeaModel):
    def __init__(self, request_id=None, value_added_list=None):
        self.request_id = request_id    # type: str
        self.value_added_list = value_added_list  # type: List[ListValueAddedResponseValueAddedList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.value_added_list, 'value_added_list')
        if self.value_added_list:
            for k in self.value_added_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ValueAddedList'] = []
        if self.value_added_list is not None:
            for k in self.value_added_list:
                result['ValueAddedList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.value_added_list = []
        if map.get('ValueAddedList') is not None:
            for k in map.get('ValueAddedList'):
                temp_model = ListValueAddedResponseValueAddedList()
                self.value_added_list.append(temp_model.from_map(k))
        return self


class ListValueAddedResponseValueAddedList(TeaModel):
    def __init__(self, instance_id=None, status=None, expire_time=None, gmt_create=None, log_size=None):
        self.instance_id = instance_id  # type: str
        self.status = status            # type: int
        self.expire_time = expire_time  # type: int
        self.gmt_create = gmt_create    # type: int
        self.log_size = log_size        # type: int

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.log_size, 'log_size')

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('ExpireTime') is not None:
            self.expire_time = map.get('ExpireTime')
        if map.get('GmtCreate') is not None:
            self.gmt_create = map.get('GmtCreate')
        if map.get('LogSize') is not None:
            self.log_size = map.get('LogSize')
        return self


class ListLayer7CustomPortsRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        return self


class ListLayer7CustomPortsResponse(TeaModel):
    def __init__(self, request_id=None, layer_7custom_ports=None):
        self.request_id = request_id    # type: str
        self.layer_7custom_ports = layer_7custom_ports  # type: List[ListLayer7CustomPortsResponseLayer7CustomPorts]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.layer_7custom_ports, 'layer_7custom_ports')
        if self.layer_7custom_ports:
            for k in self.layer_7custom_ports:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Layer7CustomPorts'] = []
        if self.layer_7custom_ports is not None:
            for k in self.layer_7custom_ports:
                result['Layer7CustomPorts'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.layer_7custom_ports = []
        if map.get('Layer7CustomPorts') is not None:
            for k in map.get('Layer7CustomPorts'):
                temp_model = ListLayer7CustomPortsResponseLayer7CustomPorts()
                self.layer_7custom_ports.append(temp_model.from_map(k))
        return self


class ListLayer7CustomPortsResponseLayer7CustomPorts(TeaModel):
    def __init__(self, proxy_type=None, proxy_ports=None):
        self.proxy_type = proxy_type    # type: str
        self.proxy_ports = proxy_ports  # type: List[str]

    def validate(self):
        self.validate_required(self.proxy_type, 'proxy_type')
        self.validate_required(self.proxy_ports, 'proxy_ports')

    def to_map(self):
        result = {}
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports
        return result

    def from_map(self, map={}):
        if map.get('ProxyType') is not None:
            self.proxy_type = map.get('ProxyType')
        if map.get('ProxyPorts') is not None:
            self.proxy_ports = map.get('ProxyPorts')
        return self


class DescribeSimpleDomainsRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, instance_ids=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.instance_ids = instance_ids  # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('InstanceIds') is not None:
            self.instance_ids = map.get('InstanceIds')
        return self


class DescribeSimpleDomainsResponse(TeaModel):
    def __init__(self, request_id=None, domain_list=None):
        self.request_id = request_id    # type: str
        self.domain_list = domain_list  # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('DomainList') is not None:
            self.domain_list = map.get('DomainList')
        return self


class DescribeDefenseCountStatisticsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeDefenseCountStatisticsResponse(TeaModel):
    def __init__(self, request_id=None, defense_count_statistics=None):
        self.request_id = request_id    # type: str
        self.defense_count_statistics = defense_count_statistics  # type: DescribeDefenseCountStatisticsResponseDefenseCountStatistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.defense_count_statistics, 'defense_count_statistics')
        if self.defense_count_statistics:
            self.defense_count_statistics.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.defense_count_statistics is not None:
            result['DefenseCountStatistics'] = self.defense_count_statistics.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('DefenseCountStatistics') is not None:
            temp_model = DescribeDefenseCountStatisticsResponseDefenseCountStatistics()
            self.defense_count_statistics = temp_model.from_map(map['DefenseCountStatistics'])
        return self


class DescribeDefenseCountStatisticsResponseDefenseCountStatistics(TeaModel):
    def __init__(self, defense_count_total_usage_of_current_month=None, flow_pack_count_remain=None,
                 max_usable_defense_count_current_month=None):
        self.defense_count_total_usage_of_current_month = defense_count_total_usage_of_current_month  # type: int
        self.flow_pack_count_remain = flow_pack_count_remain  # type: int
        self.max_usable_defense_count_current_month = max_usable_defense_count_current_month  # type: int

    def validate(self):
        self.validate_required(self.defense_count_total_usage_of_current_month, 'defense_count_total_usage_of_current_month')
        self.validate_required(self.flow_pack_count_remain, 'flow_pack_count_remain')
        self.validate_required(self.max_usable_defense_count_current_month, 'max_usable_defense_count_current_month')

    def to_map(self):
        result = {}
        if self.defense_count_total_usage_of_current_month is not None:
            result['DefenseCountTotalUsageOfCurrentMonth'] = self.defense_count_total_usage_of_current_month
        if self.flow_pack_count_remain is not None:
            result['FlowPackCountRemain'] = self.flow_pack_count_remain
        if self.max_usable_defense_count_current_month is not None:
            result['MaxUsableDefenseCountCurrentMonth'] = self.max_usable_defense_count_current_month
        return result

    def from_map(self, map={}):
        if map.get('DefenseCountTotalUsageOfCurrentMonth') is not None:
            self.defense_count_total_usage_of_current_month = map.get('DefenseCountTotalUsageOfCurrentMonth')
        if map.get('FlowPackCountRemain') is not None:
            self.flow_pack_count_remain = map.get('FlowPackCountRemain')
        if map.get('MaxUsableDefenseCountCurrentMonth') is not None:
            self.max_usable_defense_count_current_month = map.get('MaxUsableDefenseCountCurrentMonth')
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_type=None, resource_id=None, tag_key=None,
                 all=None):
        self.region_id = region_id      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag_key = tag_key          # type: List[str]
        self.all = all                  # type: bool

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('ResourceId') is not None:
            self.resource_id = map.get('ResourceId')
        if map.get('TagKey') is not None:
            self.tag_key = map.get('TagKey')
        if map.get('All') is not None:
            self.all = map.get('All')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_type=None, resource_id=None, tag=None):
        self.region_id = region_id      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag = tag                  # type: List[TagResourcesRequestTag]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('ResourceId') is not None:
            self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('Key') is not None:
            self.key = map.get('Key')
        if map.get('Value') is not None:
            self.value = map.get('Value')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_type=None, resource_id=None, tag=None,
                 next_token=None):
        self.region_id = region_id      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag = tag                  # type: List[ListTagResourcesRequestTag]
        self.next_token = next_token    # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('ResourceId') is not None:
            self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('Key') is not None:
            self.key = map.get('Key')
        if map.get('Value') is not None:
            self.value = map.get('Value')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, tag_resources=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseTagResources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        if map.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseTagResources()
            self.tag_resources = temp_model.from_map(map['TagResources'])
        return self


class ListTagResourcesResponseTagResourcesTagResource(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, tag_key=None, tag_value=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str
        self.tag_key = tag_key          # type: str
        self.tag_value = tag_value      # type: str

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = {}
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, map={}):
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('ResourceId') is not None:
            self.resource_id = map.get('ResourceId')
        if map.get('TagKey') is not None:
            self.tag_key = map.get('TagKey')
        if map.get('TagValue') is not None:
            self.tag_value = map.get('TagValue')
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: List[ListTagResourcesResponseTagResourcesTagResource]

    def validate(self):
        self.validate_required(self.tag_resource, 'tag_resource')
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.tag_resource = []
        if map.get('TagResource') is not None:
            for k in map.get('TagResource'):
                temp_model = ListTagResourcesResponseTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_type=None, page_size=None,
                 current_page=None):
        self.region_id = region_id      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_type = resource_type  # type: str
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('CurrentPage') is not None:
            self.current_page = map.get('CurrentPage')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, request_id=None, current_page=None, page_size=None, total_count=None, tag_keys=None):
        self.request_id = request_id    # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.tag_keys = tag_keys        # type: List[ListTagKeysResponseTagKeys]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.tag_keys, 'tag_keys')
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('CurrentPage') is not None:
            self.current_page = map.get('CurrentPage')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.tag_keys = []
        if map.get('TagKeys') is not None:
            for k in map.get('TagKeys'):
                temp_model = ListTagKeysResponseTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        return self


class ListTagKeysResponseTagKeys(TeaModel):
    def __init__(self, tag_key=None, tag_count=None):
        self.tag_key = tag_key          # type: str
        self.tag_count = tag_count      # type: int

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_count, 'tag_count')

    def to_map(self):
        result = {}
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        return result

    def from_map(self, map={}):
        if map.get('TagKey') is not None:
            self.tag_key = map.get('TagKey')
        if map.get('TagCount') is not None:
            self.tag_count = map.get('TagCount')
        return self


class DescribeDomainQpsWithCacheRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, start_time=None, end_time=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        return self


class DescribeDomainQpsWithCacheResponse(TeaModel):
    def __init__(self, request_id=None, interval=None, start_time=None, totals=None, blocks=None, cache_hits=None,
                 precise_blocks=None, region_blocks=None, ip_block_qps=None, cc_js_qps=None, precise_js_qps=None,
                 cc_block_qps=None):
        self.request_id = request_id    # type: str
        self.interval = interval        # type: int
        self.start_time = start_time    # type: int
        self.totals = totals            # type: List[str]
        self.blocks = blocks            # type: List[str]
        self.cache_hits = cache_hits    # type: List[str]
        self.precise_blocks = precise_blocks  # type: List[str]
        self.region_blocks = region_blocks  # type: List[str]
        self.ip_block_qps = ip_block_qps  # type: List[str]
        self.cc_js_qps = cc_js_qps      # type: List[str]
        self.precise_js_qps = precise_js_qps  # type: List[str]
        self.cc_block_qps = cc_block_qps  # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.totals, 'totals')
        self.validate_required(self.blocks, 'blocks')
        self.validate_required(self.cache_hits, 'cache_hits')
        self.validate_required(self.precise_blocks, 'precise_blocks')
        self.validate_required(self.region_blocks, 'region_blocks')
        self.validate_required(self.ip_block_qps, 'ip_block_qps')
        self.validate_required(self.cc_js_qps, 'cc_js_qps')
        self.validate_required(self.precise_js_qps, 'precise_js_qps')
        self.validate_required(self.cc_block_qps, 'cc_block_qps')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.totals is not None:
            result['Totals'] = self.totals
        if self.blocks is not None:
            result['Blocks'] = self.blocks
        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits
        if self.precise_blocks is not None:
            result['PreciseBlocks'] = self.precise_blocks
        if self.region_blocks is not None:
            result['RegionBlocks'] = self.region_blocks
        if self.ip_block_qps is not None:
            result['IpBlockQps'] = self.ip_block_qps
        if self.cc_js_qps is not None:
            result['CcJsQps'] = self.cc_js_qps
        if self.precise_js_qps is not None:
            result['PreciseJsQps'] = self.precise_js_qps
        if self.cc_block_qps is not None:
            result['CcBlockQps'] = self.cc_block_qps
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('Totals') is not None:
            self.totals = map.get('Totals')
        if map.get('Blocks') is not None:
            self.blocks = map.get('Blocks')
        if map.get('CacheHits') is not None:
            self.cache_hits = map.get('CacheHits')
        if map.get('PreciseBlocks') is not None:
            self.precise_blocks = map.get('PreciseBlocks')
        if map.get('RegionBlocks') is not None:
            self.region_blocks = map.get('RegionBlocks')
        if map.get('IpBlockQps') is not None:
            self.ip_block_qps = map.get('IpBlockQps')
        if map.get('CcJsQps') is not None:
            self.cc_js_qps = map.get('CcJsQps')
        if map.get('PreciseJsQps') is not None:
            self.precise_js_qps = map.get('PreciseJsQps')
        if map.get('CcBlockQps') is not None:
            self.cc_block_qps = map.get('CcBlockQps')
        return self


class DescribeLogStoreExistStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeLogStoreExistStatusResponse(TeaModel):
    def __init__(self, request_id=None, exist_status=None):
        self.request_id = request_id    # type: str
        self.exist_status = exist_status  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.exist_status, 'exist_status')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('ExistStatus') is not None:
            self.exist_status = map.get('ExistStatus')
        return self


class DescribeBatchSlsDispatchStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, page_no=None, page_size=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        return self


class DescribeBatchSlsDispatchStatusResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, sls_config_status_list=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.sls_config_status_list = sls_config_status_list  # type: List[DescribeBatchSlsDispatchStatusResponseSlsConfigStatusList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.sls_config_status_list, 'sls_config_status_list')
        if self.sls_config_status_list:
            for k in self.sls_config_status_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['SlsConfigStatusList'] = []
        if self.sls_config_status_list is not None:
            for k in self.sls_config_status_list:
                result['SlsConfigStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.sls_config_status_list = []
        if map.get('SlsConfigStatusList') is not None:
            for k in map.get('SlsConfigStatusList'):
                temp_model = DescribeBatchSlsDispatchStatusResponseSlsConfigStatusList()
                self.sls_config_status_list.append(temp_model.from_map(k))
        return self


class DescribeBatchSlsDispatchStatusResponseSlsConfigStatusList(TeaModel):
    def __init__(self, enable=None, domain=None):
        self.enable = enable            # type: bool
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.enable, 'enable')
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        if map.get('Enable') is not None:
            self.enable = map.get('Enable')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        return self


class DescribeSlsEmptyCountRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeSlsEmptyCountResponse(TeaModel):
    def __init__(self, request_id=None, available_count=None):
        self.request_id = request_id    # type: str
        self.available_count = available_count  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.available_count, 'available_count')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_count is not None:
            result['AvailableCount'] = self.available_count
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('AvailableCount') is not None:
            self.available_count = map.get('AvailableCount')
        return self


class EmptySlsLogstoreRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        return self


class EmptySlsLogstoreResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class CloseDomainSlsConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, domain=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        return self


class CloseDomainSlsConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class OpenDomainSlsConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, domain=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        return self


class OpenDomainSlsConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DescribeSlsLogstoreInfoRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeSlsLogstoreInfoResponse(TeaModel):
    def __init__(self, request_id=None, quota=None, log_store=None, used=None, project=None, ttl=None):
        self.request_id = request_id    # type: str
        self.quota = quota              # type: int
        self.log_store = log_store      # type: str
        self.used = used                # type: int
        self.project = project          # type: str
        self.ttl = ttl                  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.quota, 'quota')
        self.validate_required(self.log_store, 'log_store')
        self.validate_required(self.used, 'used')
        self.validate_required(self.project, 'project')
        self.validate_required(self.ttl, 'ttl')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.used is not None:
            result['Used'] = self.used
        if self.project is not None:
            result['Project'] = self.project
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Quota') is not None:
            self.quota = map.get('Quota')
        if map.get('LogStore') is not None:
            self.log_store = map.get('LogStore')
        if map.get('Used') is not None:
            self.used = map.get('Used')
        if map.get('Project') is not None:
            self.project = map.get('Project')
        if map.get('Ttl') is not None:
            self.ttl = map.get('Ttl')
        return self


class DescribeSlsAuthStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeSlsAuthStatusResponse(TeaModel):
    def __init__(self, request_id=None, sls_auth_status=None):
        self.request_id = request_id    # type: str
        self.sls_auth_status = sls_auth_status  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sls_auth_status, 'sls_auth_status')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_auth_status is not None:
            result['SlsAuthStatus'] = self.sls_auth_status
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('SlsAuthStatus') is not None:
            self.sls_auth_status = map.get('SlsAuthStatus')
        return self


class DescribeSlsOpenStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeSlsOpenStatusResponse(TeaModel):
    def __init__(self, request_id=None, sls_open_status=None):
        self.request_id = request_id    # type: str
        self.sls_open_status = sls_open_status  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sls_open_status, 'sls_open_status')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_open_status is not None:
            result['SlsOpenStatus'] = self.sls_open_status
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('SlsOpenStatus') is not None:
            self.sls_open_status = map.get('SlsOpenStatus')
        return self


class DescribeDomainSlsStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, domain=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        return self


class DescribeDomainSlsStatusResponse(TeaModel):
    def __init__(self, request_id=None, sls_status=None, sls_logstore=None, sls_project=None):
        self.request_id = request_id    # type: str
        self.sls_status = sls_status    # type: bool
        self.sls_logstore = sls_logstore  # type: str
        self.sls_project = sls_project  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sls_status, 'sls_status')
        self.validate_required(self.sls_logstore, 'sls_logstore')
        self.validate_required(self.sls_project, 'sls_project')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_status is not None:
            result['SlsStatus'] = self.sls_status
        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('SlsStatus') is not None:
            self.sls_status = map.get('SlsStatus')
        if map.get('SlsLogstore') is not None:
            self.sls_logstore = map.get('SlsLogstore')
        if map.get('SlsProject') is not None:
            self.sls_project = map.get('SlsProject')
        return self


class ConfigDomainAccessModeRequest(TeaModel):
    def __init__(self, source_ip=None, domain=None, access_mode=None):
        self.source_ip = source_ip      # type: str
        self.domain = domain            # type: str
        self.access_mode = access_mode  # type: int

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.access_mode, 'access_mode')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('AccessMode') is not None:
            self.access_mode = map.get('AccessMode')
        return self


class ConfigDomainAccessModeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DescribeDomainAccessModeRequest(TeaModel):
    def __init__(self, source_ip=None, domain_list=None):
        self.source_ip = source_ip      # type: str
        self.domain_list = domain_list  # type: List[str]

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('DomainList') is not None:
            self.domain_list = map.get('DomainList')
        return self


class DescribeDomainAccessModeResponse(TeaModel):
    def __init__(self, request_id=None, domain_mode_list=None):
        self.request_id = request_id    # type: str
        self.domain_mode_list = domain_mode_list  # type: List[DescribeDomainAccessModeResponseDomainModeList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_mode_list, 'domain_mode_list')
        if self.domain_mode_list:
            for k in self.domain_mode_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainModeList'] = []
        if self.domain_mode_list is not None:
            for k in self.domain_mode_list:
                result['DomainModeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.domain_mode_list = []
        if map.get('DomainModeList') is not None:
            for k in map.get('DomainModeList'):
                temp_model = DescribeDomainAccessModeResponseDomainModeList()
                self.domain_mode_list.append(temp_model.from_map(k))
        return self


class DescribeDomainAccessModeResponseDomainModeList(TeaModel):
    def __init__(self, domain=None, access_mode=None):
        self.domain = domain            # type: str
        self.access_mode = access_mode  # type: int

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.access_mode, 'access_mode')

    def to_map(self):
        result = {}
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, map={}):
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('AccessMode') is not None:
            self.access_mode = map.get('AccessMode')
        return self


class DeleteAsyncTaskRequest(TeaModel):
    def __init__(self, resource_group_id=None, task_id=None):
        self.resource_group_id = resource_group_id  # type: str
        self.task_id = task_id          # type: int

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('TaskId') is not None:
            self.task_id = map.get('TaskId')
        return self


class DeleteAsyncTaskResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class CreateAsyncTaskRequest(TeaModel):
    def __init__(self, resource_group_id=None, task_type=None, task_params=None):
        self.resource_group_id = resource_group_id  # type: str
        self.task_type = task_type      # type: int
        self.task_params = task_params  # type: str

    def validate(self):
        self.validate_required(self.task_type, 'task_type')
        self.validate_required(self.task_params, 'task_params')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('TaskType') is not None:
            self.task_type = map.get('TaskType')
        if map.get('TaskParams') is not None:
            self.task_params = map.get('TaskParams')
        return self


class CreateAsyncTaskResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ListAsyncTaskRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, page_no=None, page_size=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        return self


class ListAsyncTaskResponse(TeaModel):
    def __init__(self, request_id=None, total=None, async_tasks=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.async_tasks = async_tasks  # type: List[ListAsyncTaskResponseAsyncTasks]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.async_tasks, 'async_tasks')
        if self.async_tasks:
            for k in self.async_tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['AsyncTasks'] = []
        if self.async_tasks is not None:
            for k in self.async_tasks:
                result['AsyncTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.async_tasks = []
        if map.get('AsyncTasks') is not None:
            for k in map.get('AsyncTasks'):
                temp_model = ListAsyncTaskResponseAsyncTasks()
                self.async_tasks.append(temp_model.from_map(k))
        return self


class ListAsyncTaskResponseAsyncTasks(TeaModel):
    def __init__(self, task_id=None, end_time=None, start_time=None, task_status=None, task_result=None,
                 task_params=None, task_type=None):
        self.task_id = task_id          # type: int
        self.end_time = end_time        # type: int
        self.start_time = start_time    # type: int
        self.task_status = task_status  # type: int
        self.task_result = task_result  # type: str
        self.task_params = task_params  # type: str
        self.task_type = task_type      # type: int

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.task_status, 'task_status')
        self.validate_required(self.task_result, 'task_result')
        self.validate_required(self.task_params, 'task_params')
        self.validate_required(self.task_type, 'task_type')

    def to_map(self):
        result = {}
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, map={}):
        if map.get('TaskId') is not None:
            self.task_id = map.get('TaskId')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('TaskStatus') is not None:
            self.task_status = map.get('TaskStatus')
        if map.get('TaskResult') is not None:
            self.task_result = map.get('TaskResult')
        if map.get('TaskParams') is not None:
            self.task_params = map.get('TaskParams')
        if map.get('TaskType') is not None:
            self.task_type = map.get('TaskType')
        return self


class EnableLayer7CCRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        return self


class EnableLayer7CCRuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class EnableLayer7CCRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        return self


class EnableLayer7CCResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DisableLayer7CCRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        return self


class DisableLayer7CCRuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DisableLayer7CCRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        return self


class DisableLayer7CCResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DescribleLayer7InstanceRelationsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain_list=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain_list = domain_list  # type: List[str]

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('DomainList') is not None:
            self.domain_list = map.get('DomainList')
        return self


class DescribleLayer7InstanceRelationsResponse(TeaModel):
    def __init__(self, request_id=None, layer_7instance_relations=None):
        self.request_id = request_id    # type: str
        self.layer_7instance_relations = layer_7instance_relations  # type: List[DescribleLayer7InstanceRelationsResponseLayer7InstanceRelations]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.layer_7instance_relations, 'layer_7instance_relations')
        if self.layer_7instance_relations:
            for k in self.layer_7instance_relations:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Layer7InstanceRelations'] = []
        if self.layer_7instance_relations is not None:
            for k in self.layer_7instance_relations:
                result['Layer7InstanceRelations'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.layer_7instance_relations = []
        if map.get('Layer7InstanceRelations') is not None:
            for k in map.get('Layer7InstanceRelations'):
                temp_model = DescribleLayer7InstanceRelationsResponseLayer7InstanceRelations()
                self.layer_7instance_relations.append(temp_model.from_map(k))
        return self


class DescribleLayer7InstanceRelationsResponseLayer7InstanceRelationsInstanceDetails(TeaModel):
    def __init__(self, instance_id=None, function_version=None, eip_list=None):
        self.instance_id = instance_id  # type: str
        self.function_version = function_version  # type: str
        self.eip_list = eip_list        # type: List[str]

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.function_version, 'function_version')
        self.validate_required(self.eip_list, 'eip_list')

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version
        if self.eip_list is not None:
            result['EipList'] = self.eip_list
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('FunctionVersion') is not None:
            self.function_version = map.get('FunctionVersion')
        if map.get('EipList') is not None:
            self.eip_list = map.get('EipList')
        return self


class DescribleLayer7InstanceRelationsResponseLayer7InstanceRelations(TeaModel):
    def __init__(self, domain=None, instance_details=None):
        self.domain = domain            # type: str
        self.instance_details = instance_details  # type: List[DescribleLayer7InstanceRelationsResponseLayer7InstanceRelationsInstanceDetails]

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.instance_details, 'instance_details')
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.domain is not None:
            result['Domain'] = self.domain
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k in self.instance_details:
                result['InstanceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        self.instance_details = []
        if map.get('InstanceDetails') is not None:
            for k in map.get('InstanceDetails'):
                temp_model = DescribleLayer7InstanceRelationsResponseLayer7InstanceRelationsInstanceDetails()
                self.instance_details.append(temp_model.from_map(k))
        return self


class DescribleCertListRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        return self


class DescribleCertListResponse(TeaModel):
    def __init__(self, request_id=None, cert_list=None):
        self.request_id = request_id    # type: str
        self.cert_list = cert_list      # type: List[DescribleCertListResponseCertList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.cert_list, 'cert_list')
        if self.cert_list:
            for k in self.cert_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CertList'] = []
        if self.cert_list is not None:
            for k in self.cert_list:
                result['CertList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.cert_list = []
        if map.get('CertList') is not None:
            for k in map.get('CertList'):
                temp_model = DescribleCertListResponseCertList()
                self.cert_list.append(temp_model.from_map(k))
        return self


class DescribleCertListResponseCertList(TeaModel):
    def __init__(self, id=None, name=None, common=None, issuer=None, start_date=None, end_date=None,
                 domain_related=None):
        self.id = id                    # type: int
        self.name = name                # type: str
        self.common = common            # type: str
        self.issuer = issuer            # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.domain_related = domain_related  # type: bool

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.common, 'common')
        self.validate_required(self.issuer, 'issuer')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.domain_related, 'domain_related')

    def to_map(self):
        result = {}
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.common is not None:
            result['Common'] = self.common
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.domain_related is not None:
            result['DomainRelated'] = self.domain_related
        return result

    def from_map(self, map={}):
        if map.get('Id') is not None:
            self.id = map.get('Id')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Common') is not None:
            self.common = map.get('Common')
        if map.get('Issuer') is not None:
            self.issuer = map.get('Issuer')
        if map.get('StartDate') is not None:
            self.start_date = map.get('StartDate')
        if map.get('EndDate') is not None:
            self.end_date = map.get('EndDate')
        if map.get('DomainRelated') is not None:
            self.domain_related = map.get('DomainRelated')
        return self


class DescribeLayer7CCRulesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, offset=None, page_size=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.offset = offset            # type: int
        self.page_size = page_size      # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('Offset') is not None:
            self.offset = map.get('Offset')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        return self


class DescribeLayer7CCRulesResponse(TeaModel):
    def __init__(self, request_id=None, total=None, layer_7ccrules=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.layer_7ccrules = layer_7ccrules  # type: List[DescribeLayer7CCRulesResponseLayer7CCRules]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.layer_7ccrules, 'layer_7ccrules')
        if self.layer_7ccrules:
            for k in self.layer_7ccrules:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Layer7CCRules'] = []
        if self.layer_7ccrules is not None:
            for k in self.layer_7ccrules:
                result['Layer7CCRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.layer_7ccrules = []
        if map.get('Layer7CCRules') is not None:
            for k in map.get('Layer7CCRules'):
                temp_model = DescribeLayer7CCRulesResponseLayer7CCRules()
                self.layer_7ccrules.append(temp_model.from_map(k))
        return self


class DescribeLayer7CCRulesResponseLayer7CCRules(TeaModel):
    def __init__(self, name=None, act=None, count=None, interval=None, mode=None, ttl=None, uri=None):
        self.name = name                # type: str
        self.act = act                  # type: str
        self.count = count              # type: int
        self.interval = interval        # type: int
        self.mode = mode                # type: str
        self.ttl = ttl                  # type: int
        self.uri = uri                  # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.act, 'act')
        self.validate_required(self.count, 'count')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Act') is not None:
            self.act = map.get('Act')
        if map.get('Count') is not None:
            self.count = map.get('Count')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        if map.get('Mode') is not None:
            self.mode = map.get('Mode')
        if map.get('Ttl') is not None:
            self.ttl = map.get('Ttl')
        if map.get('Uri') is not None:
            self.uri = map.get('Uri')
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, query_domain_pattern=None, offset=None,
                 page_size=None, instance_ids=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.query_domain_pattern = query_domain_pattern  # type: str
        self.offset = offset            # type: int
        self.page_size = page_size      # type: str
        self.instance_ids = instance_ids  # type: List[str]

    def validate(self):
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.query_domain_pattern is not None:
            result['QueryDomainPattern'] = self.query_domain_pattern
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('QueryDomainPattern') is not None:
            self.query_domain_pattern = map.get('QueryDomainPattern')
        if map.get('Offset') is not None:
            self.offset = map.get('Offset')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('InstanceIds') is not None:
            self.instance_ids = map.get('InstanceIds')
        return self


class DescribeDomainsResponse(TeaModel):
    def __init__(self, request_id=None, total=None, domains=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.domains = domains          # type: List[DescribeDomainsResponseDomains]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.domains, 'domains')
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.domains = []
        if map.get('Domains') is not None:
            for k in map.get('Domains'):
                temp_model = DescribeDomainsResponseDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class DescribeDomainsResponseDomainsProxyTypeList(TeaModel):
    def __init__(self, proxy_type=None, proxy_ports=None):
        self.proxy_type = proxy_type    # type: str
        self.proxy_ports = proxy_ports  # type: List[str]

    def validate(self):
        self.validate_required(self.proxy_type, 'proxy_type')
        self.validate_required(self.proxy_ports, 'proxy_ports')

    def to_map(self):
        result = {}
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports
        return result

    def from_map(self, map={}):
        if map.get('ProxyType') is not None:
            self.proxy_type = map.get('ProxyType')
        if map.get('ProxyPorts') is not None:
            self.proxy_ports = map.get('ProxyPorts')
        return self


class DescribeDomainsResponseDomainsRealServers(TeaModel):
    def __init__(self, rs_type=None, real_server=None):
        self.rs_type = rs_type          # type: int
        self.real_server = real_server  # type: str

    def validate(self):
        self.validate_required(self.rs_type, 'rs_type')
        self.validate_required(self.real_server, 'real_server')

    def to_map(self):
        result = {}
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        return result

    def from_map(self, map={}):
        if map.get('RsType') is not None:
            self.rs_type = map.get('RsType')
        if map.get('RealServer') is not None:
            self.real_server = map.get('RealServer')
        return self


class DescribeDomainsResponseDomains(TeaModel):
    def __init__(self, domain=None, cc_enabled=None, cc_rule_enabled=None, cc_template=None, ssl_protocols=None,
                 ssl_ciphers=None, http_2enable=None, cname=None, cert_name=None, proxy_type_list=None, real_servers=None,
                 white_list=None, black_list=None):
        self.domain = domain            # type: str
        self.cc_enabled = cc_enabled    # type: bool
        self.cc_rule_enabled = cc_rule_enabled  # type: bool
        self.cc_template = cc_template  # type: str
        self.ssl_protocols = ssl_protocols  # type: str
        self.ssl_ciphers = ssl_ciphers  # type: str
        self.http_2enable = http_2enable  # type: bool
        self.cname = cname              # type: str
        self.cert_name = cert_name      # type: str
        self.proxy_type_list = proxy_type_list  # type: List[DescribeDomainsResponseDomainsProxyTypeList]
        self.real_servers = real_servers  # type: List[DescribeDomainsResponseDomainsRealServers]
        self.white_list = white_list    # type: List[str]
        self.black_list = black_list    # type: List[str]

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.cc_enabled, 'cc_enabled')
        self.validate_required(self.cc_rule_enabled, 'cc_rule_enabled')
        self.validate_required(self.cc_template, 'cc_template')
        self.validate_required(self.ssl_protocols, 'ssl_protocols')
        self.validate_required(self.ssl_ciphers, 'ssl_ciphers')
        self.validate_required(self.http_2enable, 'http_2enable')
        self.validate_required(self.cname, 'cname')
        self.validate_required(self.cert_name, 'cert_name')
        self.validate_required(self.proxy_type_list, 'proxy_type_list')
        if self.proxy_type_list:
            for k in self.proxy_type_list:
                if k:
                    k.validate()
        self.validate_required(self.real_servers, 'real_servers')
        if self.real_servers:
            for k in self.real_servers:
                if k:
                    k.validate()
        self.validate_required(self.white_list, 'white_list')
        self.validate_required(self.black_list, 'black_list')

    def to_map(self):
        result = {}
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cc_enabled is not None:
            result['CcEnabled'] = self.cc_enabled
        if self.cc_rule_enabled is not None:
            result['CcRuleEnabled'] = self.cc_rule_enabled
        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template
        if self.ssl_protocols is not None:
            result['SslProtocols'] = self.ssl_protocols
        if self.ssl_ciphers is not None:
            result['SslCiphers'] = self.ssl_ciphers
        if self.http_2enable is not None:
            result['Http2Enable'] = self.http_2enable
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        result['ProxyTypeList'] = []
        if self.proxy_type_list is not None:
            for k in self.proxy_type_list:
                result['ProxyTypeList'].append(k.to_map() if k else None)
        result['RealServers'] = []
        if self.real_servers is not None:
            for k in self.real_servers:
                result['RealServers'].append(k.to_map() if k else None)
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        return result

    def from_map(self, map={}):
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('CcEnabled') is not None:
            self.cc_enabled = map.get('CcEnabled')
        if map.get('CcRuleEnabled') is not None:
            self.cc_rule_enabled = map.get('CcRuleEnabled')
        if map.get('CcTemplate') is not None:
            self.cc_template = map.get('CcTemplate')
        if map.get('SslProtocols') is not None:
            self.ssl_protocols = map.get('SslProtocols')
        if map.get('SslCiphers') is not None:
            self.ssl_ciphers = map.get('SslCiphers')
        if map.get('Http2Enable') is not None:
            self.http_2enable = map.get('Http2Enable')
        if map.get('Cname') is not None:
            self.cname = map.get('Cname')
        if map.get('CertName') is not None:
            self.cert_name = map.get('CertName')
        self.proxy_type_list = []
        if map.get('ProxyTypeList') is not None:
            for k in map.get('ProxyTypeList'):
                temp_model = DescribeDomainsResponseDomainsProxyTypeList()
                self.proxy_type_list.append(temp_model.from_map(k))
        self.real_servers = []
        if map.get('RealServers') is not None:
            for k in map.get('RealServers'):
                temp_model = DescribeDomainsResponseDomainsRealServers()
                self.real_servers.append(temp_model.from_map(k))
        if map.get('WhiteList') is not None:
            self.white_list = map.get('WhiteList')
        if map.get('BlackList') is not None:
            self.black_list = map.get('BlackList')
        return self


class DescribeDomainQpsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, start_time=None, end_time=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        return self


class DescribeDomainQpsResponse(TeaModel):
    def __init__(self, request_id=None, interval=None, start_time=None, totals=None, blocks=None, cache_hits=None,
                 precise_blocks=None, region_blocks=None, ip_block_qps=None, cc_js_qps=None, precise_js_qps=None,
                 cc_block_qps=None):
        self.request_id = request_id    # type: str
        self.interval = interval        # type: int
        self.start_time = start_time    # type: int
        self.totals = totals            # type: List[str]
        self.blocks = blocks            # type: List[str]
        self.cache_hits = cache_hits    # type: List[str]
        self.precise_blocks = precise_blocks  # type: List[str]
        self.region_blocks = region_blocks  # type: List[str]
        self.ip_block_qps = ip_block_qps  # type: List[str]
        self.cc_js_qps = cc_js_qps      # type: List[str]
        self.precise_js_qps = precise_js_qps  # type: List[str]
        self.cc_block_qps = cc_block_qps  # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.totals, 'totals')
        self.validate_required(self.blocks, 'blocks')
        self.validate_required(self.cache_hits, 'cache_hits')
        self.validate_required(self.precise_blocks, 'precise_blocks')
        self.validate_required(self.region_blocks, 'region_blocks')
        self.validate_required(self.ip_block_qps, 'ip_block_qps')
        self.validate_required(self.cc_js_qps, 'cc_js_qps')
        self.validate_required(self.precise_js_qps, 'precise_js_qps')
        self.validate_required(self.cc_block_qps, 'cc_block_qps')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.totals is not None:
            result['Totals'] = self.totals
        if self.blocks is not None:
            result['Blocks'] = self.blocks
        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits
        if self.precise_blocks is not None:
            result['PreciseBlocks'] = self.precise_blocks
        if self.region_blocks is not None:
            result['RegionBlocks'] = self.region_blocks
        if self.ip_block_qps is not None:
            result['IpBlockQps'] = self.ip_block_qps
        if self.cc_js_qps is not None:
            result['CcJsQps'] = self.cc_js_qps
        if self.precise_js_qps is not None:
            result['PreciseJsQps'] = self.precise_js_qps
        if self.cc_block_qps is not None:
            result['CcBlockQps'] = self.cc_block_qps
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('Totals') is not None:
            self.totals = map.get('Totals')
        if map.get('Blocks') is not None:
            self.blocks = map.get('Blocks')
        if map.get('CacheHits') is not None:
            self.cache_hits = map.get('CacheHits')
        if map.get('PreciseBlocks') is not None:
            self.precise_blocks = map.get('PreciseBlocks')
        if map.get('RegionBlocks') is not None:
            self.region_blocks = map.get('RegionBlocks')
        if map.get('IpBlockQps') is not None:
            self.ip_block_qps = map.get('IpBlockQps')
        if map.get('CcJsQps') is not None:
            self.cc_js_qps = map.get('CcJsQps')
        if map.get('PreciseJsQps') is not None:
            self.precise_js_qps = map.get('PreciseJsQps')
        if map.get('CcBlockQps') is not None:
            self.cc_block_qps = map.get('CcBlockQps')
        return self


class DescribeDomainAttackEventsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, domain=None,
                 offset=None, page_size=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.domain = domain            # type: str
        self.offset = offset            # type: int
        self.page_size = page_size      # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('Offset') is not None:
            self.offset = map.get('Offset')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        return self


class DescribeDomainAttackEventsResponse(TeaModel):
    def __init__(self, request_id=None, total=None, events=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.events = events            # type: List[DescribeDomainAttackEventsResponseEvents]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.events, 'events')
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.events = []
        if map.get('Events') is not None:
            for k in map.get('Events'):
                temp_model = DescribeDomainAttackEventsResponseEvents()
                self.events.append(temp_model.from_map(k))
        return self


class DescribeDomainAttackEventsResponseEvents(TeaModel):
    def __init__(self, start_time=None, end_time=None, duration=None, finished=None, max_qps=None, block_count=None):
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.duration = duration        # type: int
        self.finished = finished        # type: bool
        self.max_qps = max_qps          # type: int
        self.block_count = block_count  # type: int

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.finished, 'finished')
        self.validate_required(self.max_qps, 'max_qps')
        self.validate_required(self.block_count, 'block_count')

    def to_map(self):
        result = {}
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        return result

    def from_map(self, map={}):
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Duration') is not None:
            self.duration = map.get('Duration')
        if map.get('Finished') is not None:
            self.finished = map.get('Finished')
        if map.get('MaxQps') is not None:
            self.max_qps = map.get('MaxQps')
        if map.get('BlockCount') is not None:
            self.block_count = map.get('BlockCount')
        return self


class DescribeBackSourceCidrRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, line=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.line = line                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Line') is not None:
            self.line = map.get('Line')
        return self


class DescribeBackSourceCidrResponse(TeaModel):
    def __init__(self, request_id=None, cidr_list=None):
        self.request_id = request_id    # type: str
        self.cidr_list = cidr_list      # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.cidr_list, 'cidr_list')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cidr_list is not None:
            result['CidrList'] = self.cidr_list
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('CidrList') is not None:
            self.cidr_list = map.get('CidrList')
        return self


class DeleteLayer7RuleRequest(TeaModel):
    def __init__(self, resource_group_id=None, domain=None):
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        return self


class DeleteLayer7RuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteLayer7CCRuleRequest(TeaModel):
    def __init__(self, resource_group_id=None, domain=None, name=None):
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        return self


class DeleteLayer7CCRuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class CreateLayer7RuleRequest(TeaModel):
    def __init__(self, resource_group_id=None, domain=None, rs_type=None, rules=None, instance_ids=None):
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.rs_type = rs_type          # type: int
        self.rules = rules              # type: str
        self.instance_ids = instance_ids  # type: List[str]

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.rs_type, 'rs_type')
        self.validate_required(self.rules, 'rules')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('RsType') is not None:
            self.rs_type = map.get('RsType')
        if map.get('Rules') is not None:
            self.rules = map.get('Rules')
        if map.get('InstanceIds') is not None:
            self.instance_ids = map.get('InstanceIds')
        return self


class CreateLayer7RuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ConfigLayer7RuleRequest(TeaModel):
    def __init__(self, resource_group_id=None, domain=None, proxy_type_list=None, proxy_types=None, rs_type=None,
                 real_servers=None, instance_ids=None):
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.proxy_type_list = proxy_type_list  # type: str
        self.proxy_types = proxy_types  # type: List[str]
        self.rs_type = rs_type          # type: int
        self.real_servers = real_servers  # type: List[str]
        self.instance_ids = instance_ids  # type: List[str]

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.rs_type, 'rs_type')
        self.validate_required(self.real_servers, 'real_servers')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.proxy_type_list is not None:
            result['ProxyTypeList'] = self.proxy_type_list
        if self.proxy_types is not None:
            result['ProxyTypes'] = self.proxy_types
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('ProxyTypeList') is not None:
            self.proxy_type_list = map.get('ProxyTypeList')
        if map.get('ProxyTypes') is not None:
            self.proxy_types = map.get('ProxyTypes')
        if map.get('RsType') is not None:
            self.rs_type = map.get('RsType')
        if map.get('RealServers') is not None:
            self.real_servers = map.get('RealServers')
        if map.get('InstanceIds') is not None:
            self.instance_ids = map.get('InstanceIds')
        return self


class ConfigLayer7RuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ConfigLayer7CertRequest(TeaModel):
    def __init__(self, resource_group_id=None, domain=None, cert_id=None, cert_name=None, cert=None, key=None):
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.cert_id = cert_id          # type: int
        self.cert_name = cert_name      # type: str
        self.cert = cert                # type: str
        self.key = key                  # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('CertId') is not None:
            self.cert_id = map.get('CertId')
        if map.get('CertName') is not None:
            self.cert_name = map.get('CertName')
        if map.get('Cert') is not None:
            self.cert = map.get('Cert')
        if map.get('Key') is not None:
            self.key = map.get('Key')
        return self


class ConfigLayer7CertResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ConfigLayer7CCTemplateRequest(TeaModel):
    def __init__(self, resource_group_id=None, domain=None, template=None):
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.template = template        # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.template, 'template')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('Template') is not None:
            self.template = map.get('Template')
        return self


class ConfigLayer7CCTemplateResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ConfigLayer7CCRuleRequest(TeaModel):
    def __init__(self, resource_group_id=None, domain=None, name=None, act=None, count=None, interval=None, mode=None,
                 ttl=None, uri=None):
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.name = name                # type: str
        self.act = act                  # type: str
        self.count = count              # type: int
        self.interval = interval        # type: int
        self.mode = mode                # type: str
        self.ttl = ttl                  # type: int
        self.uri = uri                  # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.name, 'name')
        self.validate_required(self.act, 'act')
        self.validate_required(self.count, 'count')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Act') is not None:
            self.act = map.get('Act')
        if map.get('Count') is not None:
            self.count = map.get('Count')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        if map.get('Mode') is not None:
            self.mode = map.get('Mode')
        if map.get('Ttl') is not None:
            self.ttl = map.get('Ttl')
        if map.get('Uri') is not None:
            self.uri = map.get('Uri')
        return self


class ConfigLayer7CCRuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ConfigLayer7BlackWhiteListRequest(TeaModel):
    def __init__(self, resource_group_id=None, domain=None, black_list=None, white_list=None):
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.black_list = black_list    # type: List[str]
        self.white_list = white_list    # type: List[str]

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('BlackList') is not None:
            self.black_list = map.get('BlackList')
        if map.get('WhiteList') is not None:
            self.white_list = map.get('WhiteList')
        return self


class ConfigLayer7BlackWhiteListResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class AddLayer7CCRuleRequest(TeaModel):
    def __init__(self, resource_group_id=None, domain=None, name=None, act=None, count=None, interval=None, mode=None,
                 ttl=None, uri=None):
        self.resource_group_id = resource_group_id  # type: str
        self.domain = domain            # type: str
        self.name = name                # type: str
        self.act = act                  # type: str
        self.count = count              # type: int
        self.interval = interval        # type: int
        self.mode = mode                # type: str
        self.ttl = ttl                  # type: int
        self.uri = uri                  # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.name, 'name')
        self.validate_required(self.act, 'act')
        self.validate_required(self.count, 'count')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Act') is not None:
            self.act = map.get('Act')
        if map.get('Count') is not None:
            self.count = map.get('Count')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        if map.get('Mode') is not None:
            self.mode = map.get('Mode')
        if map.get('Ttl') is not None:
            self.ttl = map.get('Ttl')
        if map.get('Uri') is not None:
            self.uri = map.get('Uri')
        return self


class AddLayer7CCRuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None):
        self.source_ip = source_ip      # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        return self


class ReleaseInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ModifyInstanceRemarkRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, remark=None):
        self.source_ip = source_ip      # type: str
        self.instance_id = instance_id  # type: str
        self.remark = remark            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Remark') is not None:
            self.remark = map.get('Remark')
        return self


class ModifyInstanceRemarkResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ModifyElasticBandWidthRequest(TeaModel):
    def __init__(self, source_ip=None, elastic_bandwidth=None, instance_id=None):
        self.source_ip = source_ip      # type: str
        self.elastic_bandwidth = elastic_bandwidth  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.elastic_bandwidth, 'elastic_bandwidth')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = map.get('ElasticBandwidth')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        return self


class ModifyElasticBandWidthResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, entity_type=None, entity_object=None,
                 start_time=None, end_time=None, page_no=None, page_size=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.entity_type = entity_type  # type: int
        self.entity_object = entity_object  # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('EntityType') is not None:
            self.entity_type = map.get('EntityType')
        if map.get('EntityObject') is not None:
            self.entity_object = map.get('EntityObject')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        return self


class DescribeOpEntitiesResponse(TeaModel):
    def __init__(self, request_id=None, total=None, op_entities=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.op_entities = op_entities  # type: List[DescribeOpEntitiesResponseOpEntities]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.op_entities, 'op_entities')
        if self.op_entities:
            for k in self.op_entities:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.op_entities = []
        if map.get('OpEntities') is not None:
            for k in map.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        return self


class DescribeOpEntitiesResponseOpEntities(TeaModel):
    def __init__(self, gmt_create=None, entity_type=None, entity_object=None, op_action=None, op_account=None,
                 op_desc=None):
        self.gmt_create = gmt_create    # type: int
        self.entity_type = entity_type  # type: int
        self.entity_object = entity_object  # type: str
        self.op_action = op_action      # type: int
        self.op_account = op_account    # type: str
        self.op_desc = op_desc          # type: str

    def validate(self):
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.entity_type, 'entity_type')
        self.validate_required(self.entity_object, 'entity_object')
        self.validate_required(self.op_action, 'op_action')
        self.validate_required(self.op_account, 'op_account')
        self.validate_required(self.op_desc, 'op_desc')

    def to_map(self):
        result = {}
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.op_action is not None:
            result['OpAction'] = self.op_action
        if self.op_account is not None:
            result['OpAccount'] = self.op_account
        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc
        return result

    def from_map(self, map={}):
        if map.get('GmtCreate') is not None:
            self.gmt_create = map.get('GmtCreate')
        if map.get('EntityType') is not None:
            self.entity_type = map.get('EntityType')
        if map.get('EntityObject') is not None:
            self.entity_object = map.get('EntityObject')
        if map.get('OpAction') is not None:
            self.op_action = map.get('OpAction')
        if map.get('OpAccount') is not None:
            self.op_account = map.get('OpAccount')
        if map.get('OpDesc') is not None:
            self.op_desc = map.get('OpDesc')
        return self


class DescribeLayer4RulesRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, forward_protocol=None, frontend_port=None, offset=None,
                 page_size=None):
        self.source_ip = source_ip      # type: str
        self.instance_id = instance_id  # type: str
        self.forward_protocol = forward_protocol  # type: str
        self.frontend_port = frontend_port  # type: int
        self.offset = offset            # type: int
        self.page_size = page_size      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('ForwardProtocol') is not None:
            self.forward_protocol = map.get('ForwardProtocol')
        if map.get('FrontendPort') is not None:
            self.frontend_port = map.get('FrontendPort')
        if map.get('Offset') is not None:
            self.offset = map.get('Offset')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        return self


class DescribeLayer4RulesResponse(TeaModel):
    def __init__(self, request_id=None, total=None, listeners=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.listeners = listeners      # type: List[DescribeLayer4RulesResponseListeners]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.listeners, 'listeners')
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.listeners = []
        if map.get('Listeners') is not None:
            for k in map.get('Listeners'):
                temp_model = DescribeLayer4RulesResponseListeners()
                self.listeners.append(temp_model.from_map(k))
        return self


class DescribeLayer4RulesResponseListeners(TeaModel):
    def __init__(self, instance_id=None, protocol=None, frontend_port=None, backend_port=None, is_auto_create=None,
                 real_servers=None):
        self.instance_id = instance_id  # type: str
        self.protocol = protocol        # type: str
        self.frontend_port = frontend_port  # type: int
        self.backend_port = backend_port  # type: int
        self.is_auto_create = is_auto_create  # type: bool
        self.real_servers = real_servers  # type: List[str]

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.backend_port, 'backend_port')
        self.validate_required(self.is_auto_create, 'is_auto_create')
        self.validate_required(self.real_servers, 'real_servers')

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port
        if self.is_auto_create is not None:
            result['IsAutoCreate'] = self.is_auto_create
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Protocol') is not None:
            self.protocol = map.get('Protocol')
        if map.get('FrontendPort') is not None:
            self.frontend_port = map.get('FrontendPort')
        if map.get('BackendPort') is not None:
            self.backend_port = map.get('BackendPort')
        if map.get('IsAutoCreate') is not None:
            self.is_auto_create = map.get('IsAutoCreate')
        if map.get('RealServers') is not None:
            self.real_servers = map.get('RealServers')
        return self


class DescribeLayer4RuleAttributesRequest(TeaModel):
    def __init__(self, source_ip=None, listeners=None):
        self.source_ip = source_ip      # type: str
        self.listeners = listeners      # type: str

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Listeners') is not None:
            self.listeners = map.get('Listeners')
        return self


class DescribeLayer4RuleAttributesResponse(TeaModel):
    def __init__(self, request_id=None, listeners=None):
        self.request_id = request_id    # type: str
        self.listeners = listeners      # type: List[DescribeLayer4RuleAttributesResponseListeners]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.listeners, 'listeners')
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.listeners = []
        if map.get('Listeners') is not None:
            for k in map.get('Listeners'):
                temp_model = DescribeLayer4RuleAttributesResponseListeners()
                self.listeners.append(temp_model.from_map(k))
        return self


class DescribeLayer4RuleAttributesResponseListenersConfigSla(TeaModel):
    def __init__(self, cps=None, maxconn=None, cps_enable=None, maxconn_enable=None):
        self.cps = cps                  # type: int
        self.maxconn = maxconn          # type: int
        self.cps_enable = cps_enable    # type: int
        self.maxconn_enable = maxconn_enable  # type: int

    def validate(self):
        self.validate_required(self.cps, 'cps')
        self.validate_required(self.maxconn, 'maxconn')
        self.validate_required(self.cps_enable, 'cps_enable')
        self.validate_required(self.maxconn_enable, 'maxconn_enable')

    def to_map(self):
        result = {}
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        return result

    def from_map(self, map={}):
        if map.get('Cps') is not None:
            self.cps = map.get('Cps')
        if map.get('Maxconn') is not None:
            self.maxconn = map.get('Maxconn')
        if map.get('CpsEnable') is not None:
            self.cps_enable = map.get('CpsEnable')
        if map.get('MaxconnEnable') is not None:
            self.maxconn_enable = map.get('MaxconnEnable')
        return self


class DescribeLayer4RuleAttributesResponseListenersConfigSlimit(TeaModel):
    def __init__(self, cps=None, maxconn=None, cps_enable=None, cps_mode=None, maxconn_enable=None, bps=None,
                 pps=None):
        self.cps = cps                  # type: int
        self.maxconn = maxconn          # type: int
        self.cps_enable = cps_enable    # type: int
        self.cps_mode = cps_mode        # type: int
        self.maxconn_enable = maxconn_enable  # type: int
        self.bps = bps                  # type: int
        self.pps = pps                  # type: int

    def validate(self):
        self.validate_required(self.cps, 'cps')
        self.validate_required(self.maxconn, 'maxconn')
        self.validate_required(self.cps_enable, 'cps_enable')
        self.validate_required(self.cps_mode, 'cps_mode')
        self.validate_required(self.maxconn_enable, 'maxconn_enable')
        self.validate_required(self.bps, 'bps')
        self.validate_required(self.pps, 'pps')

    def to_map(self):
        result = {}
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.cps_mode is not None:
            result['CpsMode'] = self.cps_mode
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, map={}):
        if map.get('Cps') is not None:
            self.cps = map.get('Cps')
        if map.get('Maxconn') is not None:
            self.maxconn = map.get('Maxconn')
        if map.get('CpsEnable') is not None:
            self.cps_enable = map.get('CpsEnable')
        if map.get('CpsMode') is not None:
            self.cps_mode = map.get('CpsMode')
        if map.get('MaxconnEnable') is not None:
            self.maxconn_enable = map.get('MaxconnEnable')
        if map.get('Bps') is not None:
            self.bps = map.get('Bps')
        if map.get('Pps') is not None:
            self.pps = map.get('Pps')
        return self


class DescribeLayer4RuleAttributesResponseListenersConfigPayloadLen(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: int
        self.max = max                  # type: int

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        if self.min is not None:
            result['Min'] = self.min
        if self.max is not None:
            result['Max'] = self.max
        return result

    def from_map(self, map={}):
        if map.get('Min') is not None:
            self.min = map.get('Min')
        if map.get('Max') is not None:
            self.max = map.get('Max')
        return self


class DescribeLayer4RuleAttributesResponseListenersConfigCcSblack(TeaModel):
    def __init__(self, during=None, expires=None, cnt=None, type=None):
        self.during = during            # type: int
        self.expires = expires          # type: int
        self.cnt = cnt                  # type: int
        self.type = type                # type: int

    def validate(self):
        self.validate_required(self.during, 'during')
        self.validate_required(self.expires, 'expires')
        self.validate_required(self.cnt, 'cnt')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.during is not None:
            result['During'] = self.during
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.cnt is not None:
            result['Cnt'] = self.cnt
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('During') is not None:
            self.during = map.get('During')
        if map.get('Expires') is not None:
            self.expires = map.get('Expires')
        if map.get('Cnt') is not None:
            self.cnt = map.get('Cnt')
        if map.get('Type') is not None:
            self.type = map.get('Type')
        return self


class DescribeLayer4RuleAttributesResponseListenersConfigCc(TeaModel):
    def __init__(self, sblack=None):
        self.sblack = sblack            # type: List[DescribeLayer4RuleAttributesResponseListenersConfigCcSblack]

    def validate(self):
        self.validate_required(self.sblack, 'sblack')
        if self.sblack:
            for k in self.sblack:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Sblack'] = []
        if self.sblack is not None:
            for k in self.sblack:
                result['Sblack'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.sblack = []
        if map.get('Sblack') is not None:
            for k in map.get('Sblack'):
                temp_model = DescribeLayer4RuleAttributesResponseListenersConfigCcSblack()
                self.sblack.append(temp_model.from_map(k))
        return self


class DescribeLayer4RuleAttributesResponseListenersConfig(TeaModel):
    def __init__(self, persistence_timeout=None, synproxy=None, nodata_conn=None, sla=None, slimit=None,
                 payload_len=None, cc=None):
        self.persistence_timeout = persistence_timeout  # type: int
        self.synproxy = synproxy        # type: str
        self.nodata_conn = nodata_conn  # type: str
        self.sla = sla                  # type: DescribeLayer4RuleAttributesResponseListenersConfigSla
        self.slimit = slimit            # type: DescribeLayer4RuleAttributesResponseListenersConfigSlimit
        self.payload_len = payload_len  # type: DescribeLayer4RuleAttributesResponseListenersConfigPayloadLen
        self.cc = cc                    # type: DescribeLayer4RuleAttributesResponseListenersConfigCc

    def validate(self):
        self.validate_required(self.persistence_timeout, 'persistence_timeout')
        self.validate_required(self.synproxy, 'synproxy')
        self.validate_required(self.nodata_conn, 'nodata_conn')
        self.validate_required(self.sla, 'sla')
        if self.sla:
            self.sla.validate()
        self.validate_required(self.slimit, 'slimit')
        if self.slimit:
            self.slimit.validate()
        self.validate_required(self.payload_len, 'payload_len')
        if self.payload_len:
            self.payload_len.validate()
        self.validate_required(self.cc, 'cc')
        if self.cc:
            self.cc.validate()

    def to_map(self):
        result = {}
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.synproxy is not None:
            result['Synproxy'] = self.synproxy
        if self.nodata_conn is not None:
            result['NodataConn'] = self.nodata_conn
        if self.sla is not None:
            result['Sla'] = self.sla.to_map()
        if self.slimit is not None:
            result['Slimit'] = self.slimit.to_map()
        if self.payload_len is not None:
            result['PayloadLen'] = self.payload_len.to_map()
        if self.cc is not None:
            result['Cc'] = self.cc.to_map()
        return result

    def from_map(self, map={}):
        if map.get('PersistenceTimeout') is not None:
            self.persistence_timeout = map.get('PersistenceTimeout')
        if map.get('Synproxy') is not None:
            self.synproxy = map.get('Synproxy')
        if map.get('NodataConn') is not None:
            self.nodata_conn = map.get('NodataConn')
        if map.get('Sla') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseListenersConfigSla()
            self.sla = temp_model.from_map(map['Sla'])
        if map.get('Slimit') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseListenersConfigSlimit()
            self.slimit = temp_model.from_map(map['Slimit'])
        if map.get('PayloadLen') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseListenersConfigPayloadLen()
            self.payload_len = temp_model.from_map(map['PayloadLen'])
        if map.get('Cc') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseListenersConfigCc()
            self.cc = temp_model.from_map(map['Cc'])
        return self


class DescribeLayer4RuleAttributesResponseListeners(TeaModel):
    def __init__(self, instance_id=None, protocol=None, frontend_port=None, config=None):
        self.instance_id = instance_id  # type: str
        self.protocol = protocol        # type: str
        self.frontend_port = frontend_port  # type: int
        self.config = config            # type: DescribeLayer4RuleAttributesResponseListenersConfig

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.config, 'config')
        if self.config:
            self.config.validate()

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.config is not None:
            result['Config'] = self.config.to_map()
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Protocol') is not None:
            self.protocol = map.get('Protocol')
        if map.get('FrontendPort') is not None:
            self.frontend_port = map.get('FrontendPort')
        if map.get('Config') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseListenersConfig()
            self.config = temp_model.from_map(map['Config'])
        return self


class DescribeIpTrafficRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, interval=None, end_time=None,
                 eip=None, port=None, query_protocol=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.start_time = start_time    # type: int
        self.interval = interval        # type: int
        self.end_time = end_time        # type: int
        self.eip = eip                  # type: str
        self.port = port                # type: int
        self.query_protocol = query_protocol  # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.eip, 'eip')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.port is not None:
            result['Port'] = self.port
        if self.query_protocol is not None:
            result['QueryProtocol'] = self.query_protocol
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Eip') is not None:
            self.eip = map.get('Eip')
        if map.get('Port') is not None:
            self.port = map.get('Port')
        if map.get('QueryProtocol') is not None:
            self.query_protocol = map.get('QueryProtocol')
        return self


class DescribeIpTrafficResponse(TeaModel):
    def __init__(self, request_id=None, max_in_bps=None, avg_in_bps=None, max_out_bps=None, avg_out_bps=None,
                 ip_traffic_points=None):
        self.request_id = request_id    # type: str
        self.max_in_bps = max_in_bps    # type: int
        self.avg_in_bps = avg_in_bps    # type: int
        self.max_out_bps = max_out_bps  # type: int
        self.avg_out_bps = avg_out_bps  # type: int
        self.ip_traffic_points = ip_traffic_points  # type: List[DescribeIpTrafficResponseIpTrafficPoints]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.max_in_bps, 'max_in_bps')
        self.validate_required(self.avg_in_bps, 'avg_in_bps')
        self.validate_required(self.max_out_bps, 'max_out_bps')
        self.validate_required(self.avg_out_bps, 'avg_out_bps')
        self.validate_required(self.ip_traffic_points, 'ip_traffic_points')
        if self.ip_traffic_points:
            for k in self.ip_traffic_points:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_in_bps is not None:
            result['MaxInBps'] = self.max_in_bps
        if self.avg_in_bps is not None:
            result['AvgInBps'] = self.avg_in_bps
        if self.max_out_bps is not None:
            result['MaxOutBps'] = self.max_out_bps
        if self.avg_out_bps is not None:
            result['AvgOutBps'] = self.avg_out_bps
        result['IpTrafficPoints'] = []
        if self.ip_traffic_points is not None:
            for k in self.ip_traffic_points:
                result['IpTrafficPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('MaxInBps') is not None:
            self.max_in_bps = map.get('MaxInBps')
        if map.get('AvgInBps') is not None:
            self.avg_in_bps = map.get('AvgInBps')
        if map.get('MaxOutBps') is not None:
            self.max_out_bps = map.get('MaxOutBps')
        if map.get('AvgOutBps') is not None:
            self.avg_out_bps = map.get('AvgOutBps')
        self.ip_traffic_points = []
        if map.get('IpTrafficPoints') is not None:
            for k in map.get('IpTrafficPoints'):
                temp_model = DescribeIpTrafficResponseIpTrafficPoints()
                self.ip_traffic_points.append(temp_model.from_map(k))
        return self


class DescribeIpTrafficResponseIpTrafficPoints(TeaModel):
    def __init__(self, time=None, max_inbps=None, max_outbps=None, cps=None, act_conns=None, inact_conns=None):
        self.time = time                # type: int
        self.max_inbps = max_inbps      # type: int
        self.max_outbps = max_outbps    # type: int
        self.cps = cps                  # type: int
        self.act_conns = act_conns      # type: int
        self.inact_conns = inact_conns  # type: int

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.max_inbps, 'max_inbps')
        self.validate_required(self.max_outbps, 'max_outbps')
        self.validate_required(self.cps, 'cps')
        self.validate_required(self.act_conns, 'act_conns')
        self.validate_required(self.inact_conns, 'inact_conns')

    def to_map(self):
        result = {}
        if self.time is not None:
            result['Time'] = self.time
        if self.max_inbps is not None:
            result['MaxInbps'] = self.max_inbps
        if self.max_outbps is not None:
            result['MaxOutbps'] = self.max_outbps
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns
        if self.inact_conns is not None:
            result['InactConns'] = self.inact_conns
        return result

    def from_map(self, map={}):
        if map.get('Time') is not None:
            self.time = map.get('Time')
        if map.get('MaxInbps') is not None:
            self.max_inbps = map.get('MaxInbps')
        if map.get('MaxOutbps') is not None:
            self.max_outbps = map.get('MaxOutbps')
        if map.get('Cps') is not None:
            self.cps = map.get('Cps')
        if map.get('ActConns') is not None:
            self.act_conns = map.get('ActConns')
        if map.get('InactConns') is not None:
            self.inact_conns = map.get('InactConns')
        return self


class DescribeInstanceStatisticsRequest(TeaModel):
    def __init__(self, source_ip=None, instance_ids=None):
        self.source_ip = source_ip      # type: str
        self.instance_ids = instance_ids  # type: str

    def validate(self):
        self.validate_required(self.instance_ids, 'instance_ids')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('InstanceIds') is not None:
            self.instance_ids = map.get('InstanceIds')
        return self


class DescribeInstanceStatisticsResponse(TeaModel):
    def __init__(self, request_id=None, instance_statistics=None):
        self.request_id = request_id    # type: str
        self.instance_statistics = instance_statistics  # type: List[DescribeInstanceStatisticsResponseInstanceStatistics]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_statistics, 'instance_statistics')
        if self.instance_statistics:
            for k in self.instance_statistics:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceStatistics'] = []
        if self.instance_statistics is not None:
            for k in self.instance_statistics:
                result['InstanceStatistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.instance_statistics = []
        if map.get('InstanceStatistics') is not None:
            for k in map.get('InstanceStatistics'):
                temp_model = DescribeInstanceStatisticsResponseInstanceStatistics()
                self.instance_statistics.append(temp_model.from_map(k))
        return self


class DescribeInstanceStatisticsResponseInstanceStatistics(TeaModel):
    def __init__(self, instance_id=None, port_usage=None, domain_usage=None, site_usage=None,
                 defense_count_usage=None):
        self.instance_id = instance_id  # type: str
        self.port_usage = port_usage    # type: int
        self.domain_usage = domain_usage  # type: int
        self.site_usage = site_usage    # type: int
        self.defense_count_usage = defense_count_usage  # type: int

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.port_usage, 'port_usage')
        self.validate_required(self.domain_usage, 'domain_usage')
        self.validate_required(self.site_usage, 'site_usage')
        self.validate_required(self.defense_count_usage, 'defense_count_usage')

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port_usage is not None:
            result['PortUsage'] = self.port_usage
        if self.domain_usage is not None:
            result['DomainUsage'] = self.domain_usage
        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage
        if self.defense_count_usage is not None:
            result['DefenseCountUsage'] = self.defense_count_usage
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('PortUsage') is not None:
            self.port_usage = map.get('PortUsage')
        if map.get('DomainUsage') is not None:
            self.domain_usage = map.get('DomainUsage')
        if map.get('SiteUsage') is not None:
            self.site_usage = map.get('SiteUsage')
        if map.get('DefenseCountUsage') is not None:
            self.defense_count_usage = map.get('DefenseCountUsage')
        return self


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(self, source_ip=None, instance_ids=None):
        self.source_ip = source_ip      # type: str
        self.instance_ids = instance_ids  # type: str

    def validate(self):
        self.validate_required(self.instance_ids, 'instance_ids')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('InstanceIds') is not None:
            self.instance_ids = map.get('InstanceIds')
        return self


class DescribeInstanceSpecsResponse(TeaModel):
    def __init__(self, request_id=None, instance_specs=None):
        self.request_id = request_id    # type: str
        self.instance_specs = instance_specs  # type: List[DescribeInstanceSpecsResponseInstanceSpecs]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_specs, 'instance_specs')
        if self.instance_specs:
            for k in self.instance_specs:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k in self.instance_specs:
                result['InstanceSpecs'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.instance_specs = []
        if map.get('InstanceSpecs') is not None:
            for k in map.get('InstanceSpecs'):
                temp_model = DescribeInstanceSpecsResponseInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k))
        return self


class DescribeInstanceSpecsResponseInstanceSpecs(TeaModel):
    def __init__(self, instance_id=None, base_bandwidth=None, elastic_bandwidth=None, port_limit=None,
                 site_limit=None, domain_limit=None, bandwidth_mbps=None, defense_count=None, function_version=None,
                 qps_limit=None):
        self.instance_id = instance_id  # type: str
        self.base_bandwidth = base_bandwidth  # type: int
        self.elastic_bandwidth = elastic_bandwidth  # type: int
        self.port_limit = port_limit    # type: int
        self.site_limit = site_limit    # type: int
        self.domain_limit = domain_limit  # type: int
        self.bandwidth_mbps = bandwidth_mbps  # type: int
        self.defense_count = defense_count  # type: int
        self.function_version = function_version  # type: str
        self.qps_limit = qps_limit      # type: int

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.base_bandwidth, 'base_bandwidth')
        self.validate_required(self.elastic_bandwidth, 'elastic_bandwidth')
        self.validate_required(self.port_limit, 'port_limit')
        self.validate_required(self.site_limit, 'site_limit')
        self.validate_required(self.domain_limit, 'domain_limit')
        self.validate_required(self.bandwidth_mbps, 'bandwidth_mbps')
        self.validate_required(self.defense_count, 'defense_count')
        self.validate_required(self.function_version, 'function_version')
        self.validate_required(self.qps_limit, 'qps_limit')

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.base_bandwidth is not None:
            result['BaseBandwidth'] = self.base_bandwidth
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.port_limit is not None:
            result['PortLimit'] = self.port_limit
        if self.site_limit is not None:
            result['SiteLimit'] = self.site_limit
        if self.domain_limit is not None:
            result['DomainLimit'] = self.domain_limit
        if self.bandwidth_mbps is not None:
            result['BandwidthMbps'] = self.bandwidth_mbps
        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version
        if self.qps_limit is not None:
            result['QpsLimit'] = self.qps_limit
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('BaseBandwidth') is not None:
            self.base_bandwidth = map.get('BaseBandwidth')
        if map.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = map.get('ElasticBandwidth')
        if map.get('PortLimit') is not None:
            self.port_limit = map.get('PortLimit')
        if map.get('SiteLimit') is not None:
            self.site_limit = map.get('SiteLimit')
        if map.get('DomainLimit') is not None:
            self.domain_limit = map.get('DomainLimit')
        if map.get('BandwidthMbps') is not None:
            self.bandwidth_mbps = map.get('BandwidthMbps')
        if map.get('DefenseCount') is not None:
            self.defense_count = map.get('DefenseCount')
        if map.get('FunctionVersion') is not None:
            self.function_version = map.get('FunctionVersion')
        if map.get('QpsLimit') is not None:
            self.qps_limit = map.get('QpsLimit')
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, instance_ids=None, page_no=None, page_size=None,
                 ip=None, remark=None, edition=None, enabled=None, expire_start_time=None, expire_end_time=None,
                 status=None, tag=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.instance_ids = instance_ids  # type: str
        self.page_no = page_no          # type: str
        self.page_size = page_size      # type: str
        self.ip = ip                    # type: str
        self.remark = remark            # type: str
        self.edition = edition          # type: int
        self.enabled = enabled          # type: int
        self.expire_start_time = expire_start_time  # type: int
        self.expire_end_time = expire_end_time  # type: int
        self.status = status            # type: List[int]
        self.tag = tag                  # type: List[DescribeInstancesRequestTag]

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.expire_start_time is not None:
            result['ExpireStartTime'] = self.expire_start_time
        if self.expire_end_time is not None:
            result['ExpireEndTime'] = self.expire_end_time
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('InstanceIds') is not None:
            self.instance_ids = map.get('InstanceIds')
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('Ip') is not None:
            self.ip = map.get('Ip')
        if map.get('Remark') is not None:
            self.remark = map.get('Remark')
        if map.get('Edition') is not None:
            self.edition = map.get('Edition')
        if map.get('Enabled') is not None:
            self.enabled = map.get('Enabled')
        if map.get('ExpireStartTime') is not None:
            self.expire_start_time = map.get('ExpireStartTime')
        if map.get('ExpireEndTime') is not None:
            self.expire_end_time = map.get('ExpireEndTime')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('Key') is not None:
            self.key = map.get('Key')
        if map.get('Value') is not None:
            self.value = map.get('Value')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, request_id=None, total=None, instances=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.instances = instances      # type: List[DescribeInstancesResponseInstances]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.instances = []
        if map.get('Instances') is not None:
            for k in map.get('Instances'):
                temp_model = DescribeInstancesResponseInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseInstances(TeaModel):
    def __init__(self, instance_id=None, remark=None, status=None, debt_status=None, expire_time=None,
                 gmt_create=None, edition=None, enabled=None):
        self.instance_id = instance_id  # type: str
        self.remark = remark            # type: str
        self.status = status            # type: int
        self.debt_status = debt_status  # type: int
        self.expire_time = expire_time  # type: int
        self.gmt_create = gmt_create    # type: int
        self.edition = edition          # type: int
        self.enabled = enabled          # type: int

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.status, 'status')
        self.validate_required(self.debt_status, 'debt_status')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.edition, 'edition')
        self.validate_required(self.enabled, 'enabled')

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.debt_status is not None:
            result['DebtStatus'] = self.debt_status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Remark') is not None:
            self.remark = map.get('Remark')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('DebtStatus') is not None:
            self.debt_status = map.get('DebtStatus')
        if map.get('ExpireTime') is not None:
            self.expire_time = map.get('ExpireTime')
        if map.get('GmtCreate') is not None:
            self.gmt_create = map.get('GmtCreate')
        if map.get('Edition') is not None:
            self.edition = map.get('Edition')
        if map.get('Enabled') is not None:
            self.enabled = map.get('Enabled')
        return self


class DescribeInstanceDetailsRequest(TeaModel):
    def __init__(self, source_ip=None, instance_ids=None):
        self.source_ip = source_ip      # type: str
        self.instance_ids = instance_ids  # type: str

    def validate(self):
        self.validate_required(self.instance_ids, 'instance_ids')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('InstanceIds') is not None:
            self.instance_ids = map.get('InstanceIds')
        return self


class DescribeInstanceDetailsResponse(TeaModel):
    def __init__(self, request_id=None, instance_details=None):
        self.request_id = request_id    # type: str
        self.instance_details = instance_details  # type: List[DescribeInstanceDetailsResponseInstanceDetails]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_details, 'instance_details')
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k in self.instance_details:
                result['InstanceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.instance_details = []
        if map.get('InstanceDetails') is not None:
            for k in map.get('InstanceDetails'):
                temp_model = DescribeInstanceDetailsResponseInstanceDetails()
                self.instance_details.append(temp_model.from_map(k))
        return self


class DescribeInstanceDetailsResponseInstanceDetailsEipInfoList(TeaModel):
    def __init__(self, eip=None, status=None):
        self.eip = eip                  # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.eip, 'eip')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('Eip') is not None:
            self.eip = map.get('Eip')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class DescribeInstanceDetailsResponseInstanceDetails(TeaModel):
    def __init__(self, instance_id=None, line=None, eip_info_list=None):
        self.instance_id = instance_id  # type: str
        self.line = line                # type: str
        self.eip_info_list = eip_info_list  # type: List[DescribeInstanceDetailsResponseInstanceDetailsEipInfoList]

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.line, 'line')
        self.validate_required(self.eip_info_list, 'eip_info_list')
        if self.eip_info_list:
            for k in self.eip_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.line is not None:
            result['Line'] = self.line
        result['EipInfoList'] = []
        if self.eip_info_list is not None:
            for k in self.eip_info_list:
                result['EipInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Line') is not None:
            self.line = map.get('Line')
        self.eip_info_list = []
        if map.get('EipInfoList') is not None:
            for k in map.get('EipInfoList'):
                temp_model = DescribeInstanceDetailsResponseInstanceDetailsEipInfoList()
                self.eip_info_list.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckStatusListRequest(TeaModel):
    def __init__(self, source_ip=None, listeners=None):
        self.source_ip = source_ip      # type: str
        self.listeners = listeners      # type: str

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Listeners') is not None:
            self.listeners = map.get('Listeners')
        return self


class DescribeHealthCheckStatusListResponse(TeaModel):
    def __init__(self, request_id=None, health_check_status_list=None):
        self.request_id = request_id    # type: str
        self.health_check_status_list = health_check_status_list  # type: List[DescribeHealthCheckStatusListResponseHealthCheckStatusList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.health_check_status_list, 'health_check_status_list')
        if self.health_check_status_list:
            for k in self.health_check_status_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HealthCheckStatusList'] = []
        if self.health_check_status_list is not None:
            for k in self.health_check_status_list:
                result['HealthCheckStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.health_check_status_list = []
        if map.get('HealthCheckStatusList') is not None:
            for k in map.get('HealthCheckStatusList'):
                temp_model = DescribeHealthCheckStatusListResponseHealthCheckStatusList()
                self.health_check_status_list.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckStatusListResponseHealthCheckStatusListRealServerStatusList(TeaModel):
    def __init__(self, address=None, status=None):
        self.address = address          # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.address, 'address')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        if self.address is not None:
            result['Address'] = self.address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('Address') is not None:
            self.address = map.get('Address')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class DescribeHealthCheckStatusListResponseHealthCheckStatusList(TeaModel):
    def __init__(self, instance_id=None, protocol=None, frontend_port=None, status=None,
                 real_server_status_list=None):
        self.instance_id = instance_id  # type: str
        self.protocol = protocol        # type: str
        self.frontend_port = frontend_port  # type: int
        self.status = status            # type: str
        self.real_server_status_list = real_server_status_list  # type: List[DescribeHealthCheckStatusListResponseHealthCheckStatusListRealServerStatusList]

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.status, 'status')
        self.validate_required(self.real_server_status_list, 'real_server_status_list')
        if self.real_server_status_list:
            for k in self.real_server_status_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.status is not None:
            result['Status'] = self.status
        result['RealServerStatusList'] = []
        if self.real_server_status_list is not None:
            for k in self.real_server_status_list:
                result['RealServerStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Protocol') is not None:
            self.protocol = map.get('Protocol')
        if map.get('FrontendPort') is not None:
            self.frontend_port = map.get('FrontendPort')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        self.real_server_status_list = []
        if map.get('RealServerStatusList') is not None:
            for k in map.get('RealServerStatusList'):
                temp_model = DescribeHealthCheckStatusListResponseHealthCheckStatusListRealServerStatusList()
                self.real_server_status_list.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckListRequest(TeaModel):
    def __init__(self, source_ip=None, listeners=None):
        self.source_ip = source_ip      # type: str
        self.listeners = listeners      # type: str

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Listeners') is not None:
            self.listeners = map.get('Listeners')
        return self


class DescribeHealthCheckListResponse(TeaModel):
    def __init__(self, request_id=None, listeners=None):
        self.request_id = request_id    # type: str
        self.listeners = listeners      # type: List[DescribeHealthCheckListResponseListeners]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.listeners, 'listeners')
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.listeners = []
        if map.get('Listeners') is not None:
            for k in map.get('Listeners'):
                temp_model = DescribeHealthCheckListResponseListeners()
                self.listeners.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckListResponseListenersHealthCheck(TeaModel):
    def __init__(self, type=None, domain=None, uri=None, down=None, interval=None, port=None, timeout=None, up=None):
        self.type = type                # type: str
        self.domain = domain            # type: str
        self.uri = uri                  # type: str
        self.down = down                # type: int
        self.interval = interval        # type: int
        self.port = port                # type: int
        self.timeout = timeout          # type: int
        self.up = up                    # type: int

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.uri, 'uri')
        self.validate_required(self.down, 'down')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.port, 'port')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.up, 'up')

    def to_map(self):
        result = {}
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.down is not None:
            result['Down'] = self.down
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.port is not None:
            result['Port'] = self.port
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.up is not None:
            result['Up'] = self.up
        return result

    def from_map(self, map={}):
        if map.get('Type') is not None:
            self.type = map.get('Type')
        if map.get('Domain') is not None:
            self.domain = map.get('Domain')
        if map.get('Uri') is not None:
            self.uri = map.get('Uri')
        if map.get('Down') is not None:
            self.down = map.get('Down')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        if map.get('Port') is not None:
            self.port = map.get('Port')
        if map.get('Timeout') is not None:
            self.timeout = map.get('Timeout')
        if map.get('Up') is not None:
            self.up = map.get('Up')
        return self


class DescribeHealthCheckListResponseListeners(TeaModel):
    def __init__(self, instance_id=None, protocol=None, frontend_port=None, health_check=None):
        self.instance_id = instance_id  # type: str
        self.protocol = protocol        # type: str
        self.frontend_port = frontend_port  # type: int
        self.health_check = health_check  # type: DescribeHealthCheckListResponseListenersHealthCheck

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.health_check, 'health_check')
        if self.health_check:
            self.health_check.validate()

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Protocol') is not None:
            self.protocol = map.get('Protocol')
        if map.get('FrontendPort') is not None:
            self.frontend_port = map.get('FrontendPort')
        if map.get('HealthCheck') is not None:
            temp_model = DescribeHealthCheckListResponseListenersHealthCheck()
            self.health_check = temp_model.from_map(map['HealthCheck'])
        return self


class DescribeElasticBandwidthSpecRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None):
        self.source_ip = source_ip      # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        return self


class DescribeElasticBandwidthSpecResponse(TeaModel):
    def __init__(self, request_id=None, elastic_bandwidth_spec=None):
        self.request_id = request_id    # type: str
        self.elastic_bandwidth_spec = elastic_bandwidth_spec  # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.elastic_bandwidth_spec, 'elastic_bandwidth_spec')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.elastic_bandwidth_spec is not None:
            result['ElasticBandwidthSpec'] = self.elastic_bandwidth_spec
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('ElasticBandwidthSpec') is not None:
            self.elastic_bandwidth_spec = map.get('ElasticBandwidthSpec')
        return self


class DescribeDDoSTrafficRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, interval=None, end_time=None,
                 eip=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.start_time = start_time    # type: int
        self.interval = interval        # type: int
        self.end_time = end_time        # type: int
        self.eip = eip                  # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.eip, 'eip')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.eip is not None:
            result['Eip'] = self.eip
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Eip') is not None:
            self.eip = map.get('Eip')
        return self


class DescribeDDoSTrafficResponse(TeaModel):
    def __init__(self, request_id=None, defense_in_bytes=None, source_in_bytes=None, ddo_straffic_points=None):
        self.request_id = request_id    # type: str
        self.defense_in_bytes = defense_in_bytes  # type: int
        self.source_in_bytes = source_in_bytes  # type: int
        self.ddo_straffic_points = ddo_straffic_points  # type: List[DescribeDDoSTrafficResponseDDoSTrafficPoints]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.defense_in_bytes, 'defense_in_bytes')
        self.validate_required(self.source_in_bytes, 'source_in_bytes')
        self.validate_required(self.ddo_straffic_points, 'ddo_straffic_points')
        if self.ddo_straffic_points:
            for k in self.ddo_straffic_points:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.defense_in_bytes is not None:
            result['DefenseInBytes'] = self.defense_in_bytes
        if self.source_in_bytes is not None:
            result['SourceInBytes'] = self.source_in_bytes
        result['DDoSTrafficPoints'] = []
        if self.ddo_straffic_points is not None:
            for k in self.ddo_straffic_points:
                result['DDoSTrafficPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('DefenseInBytes') is not None:
            self.defense_in_bytes = map.get('DefenseInBytes')
        if map.get('SourceInBytes') is not None:
            self.source_in_bytes = map.get('SourceInBytes')
        self.ddo_straffic_points = []
        if map.get('DDoSTrafficPoints') is not None:
            for k in map.get('DDoSTrafficPoints'):
                temp_model = DescribeDDoSTrafficResponseDDoSTrafficPoints()
                self.ddo_straffic_points.append(temp_model.from_map(k))
        return self


class DescribeDDoSTrafficResponseDDoSTrafficPoints(TeaModel):
    def __init__(self, time=None, defense_max_in_bps=None, source_max_in_bps=None):
        self.time = time                # type: int
        self.defense_max_in_bps = defense_max_in_bps  # type: int
        self.source_max_in_bps = source_max_in_bps  # type: int

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.defense_max_in_bps, 'defense_max_in_bps')
        self.validate_required(self.source_max_in_bps, 'source_max_in_bps')

    def to_map(self):
        result = {}
        if self.time is not None:
            result['Time'] = self.time
        if self.defense_max_in_bps is not None:
            result['DefenseMaxInBps'] = self.defense_max_in_bps
        if self.source_max_in_bps is not None:
            result['SourceMaxInBps'] = self.source_max_in_bps
        return result

    def from_map(self, map={}):
        if map.get('Time') is not None:
            self.time = map.get('Time')
        if map.get('DefenseMaxInBps') is not None:
            self.defense_max_in_bps = map.get('DefenseMaxInBps')
        if map.get('SourceMaxInBps') is not None:
            self.source_max_in_bps = map.get('SourceMaxInBps')
        return self


class DescribeDDoSEventsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, eip=None, offset=None,
                 page_size=None):
        self.source_ip = source_ip      # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.eip = eip                  # type: str
        self.offset = offset            # type: int
        self.page_size = page_size      # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.eip, 'eip')
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Eip') is not None:
            self.eip = map.get('Eip')
        if map.get('Offset') is not None:
            self.offset = map.get('Offset')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        return self


class DescribeDDoSEventsResponse(TeaModel):
    def __init__(self, request_id=None, total=None, events=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.events = events            # type: List[DescribeDDoSEventsResponseEvents]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.events, 'events')
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.events = []
        if map.get('Events') is not None:
            for k in map.get('Events'):
                temp_model = DescribeDDoSEventsResponseEvents()
                self.events.append(temp_model.from_map(k))
        return self


class DescribeDDoSEventsResponseEvents(TeaModel):
    def __init__(self, start_time=None, end_time=None, interval=None, status=None):
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.interval = interval        # type: int
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class DeleteLayer4RuleRequest(TeaModel):
    def __init__(self, listeners=None):
        self.listeners = listeners      # type: str

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        result = {}
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, map={}):
        if map.get('Listeners') is not None:
            self.listeners = map.get('Listeners')
        return self


class DeleteLayer4RuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class CreateLayer4RuleRequest(TeaModel):
    def __init__(self, listeners=None):
        self.listeners = listeners      # type: str

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        result = {}
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, map={}):
        if map.get('Listeners') is not None:
            self.listeners = map.get('Listeners')
        return self


class CreateLayer4RuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ConfigLayer4RuleAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, forward_protocol=None, frontend_port=None, config=None):
        self.instance_id = instance_id  # type: str
        self.forward_protocol = forward_protocol  # type: str
        self.frontend_port = frontend_port  # type: int
        self.config = config            # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.forward_protocol, 'forward_protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.config, 'config')

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('ForwardProtocol') is not None:
            self.forward_protocol = map.get('ForwardProtocol')
        if map.get('FrontendPort') is not None:
            self.frontend_port = map.get('FrontendPort')
        if map.get('Config') is not None:
            self.config = map.get('Config')
        return self


class ConfigLayer4RuleAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ConfigLayer4RuleRequest(TeaModel):
    def __init__(self, listeners=None):
        self.listeners = listeners      # type: str

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        result = {}
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, map={}):
        if map.get('Listeners') is not None:
            self.listeners = map.get('Listeners')
        return self


class ConfigLayer4RuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ConfigHealthCheckRequest(TeaModel):
    def __init__(self, instance_id=None, forward_protocol=None, frontend_port=None, health_check=None):
        self.instance_id = instance_id  # type: str
        self.forward_protocol = forward_protocol  # type: str
        self.frontend_port = frontend_port  # type: int
        self.health_check = health_check  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.forward_protocol, 'forward_protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.health_check, 'health_check')

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('ForwardProtocol') is not None:
            self.forward_protocol = map.get('ForwardProtocol')
        if map.get('FrontendPort') is not None:
            self.frontend_port = map.get('FrontendPort')
        if map.get('HealthCheck') is not None:
            self.health_check = map.get('HealthCheck')
        return self


class ConfigHealthCheckResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self

# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class ModifyFullLogTtlRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ttl: int = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ttl = ttl
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.ttl, 'ttl')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyFullLogTtlResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseValueAddedRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleaseValueAddedResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListValueAddedRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListValueAddedResponseValueAddedList(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        status: int = None,
        expire_time: int = None,
        gmt_create: int = None,
        log_size: int = None,
    ):
        self.instance_id = instance_id
        self.status = status
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.log_size = log_size

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.log_size, 'log_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        return self


class ListValueAddedResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        value_added_list: List[ListValueAddedResponseValueAddedList] = None,
    ):
        self.request_id = request_id
        self.value_added_list = value_added_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.value_added_list, 'value_added_list')
        if self.value_added_list:
            for k in self.value_added_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ValueAddedList'] = []
        if self.value_added_list is not None:
            for k in self.value_added_list:
                result['ValueAddedList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.value_added_list = []
        if m.get('ValueAddedList') is not None:
            for k in m.get('ValueAddedList'):
                temp_model = ListValueAddedResponseValueAddedList()
                self.value_added_list.append(temp_model.from_map(k))
        return self


class ListLayer7CustomPortsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListLayer7CustomPortsResponseLayer7CustomPorts(TeaModel):
    def __init__(
        self,
        proxy_type: str = None,
        proxy_ports: List[str] = None,
    ):
        self.proxy_type = proxy_type
        self.proxy_ports = proxy_ports

    def validate(self):
        self.validate_required(self.proxy_type, 'proxy_type')
        self.validate_required(self.proxy_ports, 'proxy_ports')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')
        return self


class ListLayer7CustomPortsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        layer_7custom_ports: List[ListLayer7CustomPortsResponseLayer7CustomPorts] = None,
    ):
        self.request_id = request_id
        self.layer_7custom_ports = layer_7custom_ports

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.layer_7custom_ports, 'layer_7custom_ports')
        if self.layer_7custom_ports:
            for k in self.layer_7custom_ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Layer7CustomPorts'] = []
        if self.layer_7custom_ports is not None:
            for k in self.layer_7custom_ports:
                result['Layer7CustomPorts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.layer_7custom_ports = []
        if m.get('Layer7CustomPorts') is not None:
            for k in m.get('Layer7CustomPorts'):
                temp_model = ListLayer7CustomPortsResponseLayer7CustomPorts()
                self.layer_7custom_ports.append(temp_model.from_map(k))
        return self


class DescribeSimpleDomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeSimpleDomainsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_list: List[str] = None,
    ):
        self.request_id = request_id
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        return self


class DescribeDefenseCountStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDefenseCountStatisticsResponseDefenseCountStatistics(TeaModel):
    def __init__(
        self,
        defense_count_total_usage_of_current_month: int = None,
        flow_pack_count_remain: int = None,
        max_usable_defense_count_current_month: int = None,
    ):
        self.defense_count_total_usage_of_current_month = defense_count_total_usage_of_current_month
        self.flow_pack_count_remain = flow_pack_count_remain
        self.max_usable_defense_count_current_month = max_usable_defense_count_current_month

    def validate(self):
        self.validate_required(self.defense_count_total_usage_of_current_month, 'defense_count_total_usage_of_current_month')
        self.validate_required(self.flow_pack_count_remain, 'flow_pack_count_remain')
        self.validate_required(self.max_usable_defense_count_current_month, 'max_usable_defense_count_current_month')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_count_total_usage_of_current_month is not None:
            result['DefenseCountTotalUsageOfCurrentMonth'] = self.defense_count_total_usage_of_current_month
        if self.flow_pack_count_remain is not None:
            result['FlowPackCountRemain'] = self.flow_pack_count_remain
        if self.max_usable_defense_count_current_month is not None:
            result['MaxUsableDefenseCountCurrentMonth'] = self.max_usable_defense_count_current_month
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseCountTotalUsageOfCurrentMonth') is not None:
            self.defense_count_total_usage_of_current_month = m.get('DefenseCountTotalUsageOfCurrentMonth')
        if m.get('FlowPackCountRemain') is not None:
            self.flow_pack_count_remain = m.get('FlowPackCountRemain')
        if m.get('MaxUsableDefenseCountCurrentMonth') is not None:
            self.max_usable_defense_count_current_month = m.get('MaxUsableDefenseCountCurrentMonth')
        return self


class DescribeDefenseCountStatisticsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        defense_count_statistics: DescribeDefenseCountStatisticsResponseDefenseCountStatistics = None,
    ):
        self.request_id = request_id
        self.defense_count_statistics = defense_count_statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.defense_count_statistics, 'defense_count_statistics')
        if self.defense_count_statistics:
            self.defense_count_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.defense_count_statistics is not None:
            result['DefenseCountStatistics'] = self.defense_count_statistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DefenseCountStatistics') is not None:
            temp_model = DescribeDefenseCountStatisticsResponseDefenseCountStatistics()
            self.defense_count_statistics = temp_model.from_map(m['DefenseCountStatistics'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
        all: bool = None,
    ):
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key
        self.all = all

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag
        self.next_token = next_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTagResourcesResponseTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        self.validate_required(self.tag_resource, 'tag_resource')
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        tag_resources: ListTagResourcesResponseTagResources = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.tag_resources = tag_resources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class ListTagKeysResponseTagKeys(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_count: int = None,
    ):
        self.tag_key = tag_key
        self.tag_count = tag_count

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_count, 'tag_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        tag_keys: List[ListTagKeysResponseTagKeys] = None,
    ):
        self.request_id = request_id
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.tag_keys = tag_keys

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        return self


class DescribeDomainQpsWithCacheRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDomainQpsWithCacheResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        interval: int = None,
        start_time: int = None,
        totals: List[str] = None,
        blocks: List[str] = None,
        cache_hits: List[str] = None,
        precise_blocks: List[str] = None,
        region_blocks: List[str] = None,
        ip_block_qps: List[str] = None,
        cc_js_qps: List[str] = None,
        precise_js_qps: List[str] = None,
        cc_block_qps: List[str] = None,
    ):
        self.request_id = request_id
        self.interval = interval
        self.start_time = start_time
        self.totals = totals
        self.blocks = blocks
        self.cache_hits = cache_hits
        self.precise_blocks = precise_blocks
        self.region_blocks = region_blocks
        self.ip_block_qps = ip_block_qps
        self.cc_js_qps = cc_js_qps
        self.precise_js_qps = precise_js_qps
        self.cc_block_qps = cc_block_qps

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Totals') is not None:
            self.totals = m.get('Totals')
        if m.get('Blocks') is not None:
            self.blocks = m.get('Blocks')
        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')
        if m.get('PreciseBlocks') is not None:
            self.precise_blocks = m.get('PreciseBlocks')
        if m.get('RegionBlocks') is not None:
            self.region_blocks = m.get('RegionBlocks')
        if m.get('IpBlockQps') is not None:
            self.ip_block_qps = m.get('IpBlockQps')
        if m.get('CcJsQps') is not None:
            self.cc_js_qps = m.get('CcJsQps')
        if m.get('PreciseJsQps') is not None:
            self.precise_js_qps = m.get('PreciseJsQps')
        if m.get('CcBlockQps') is not None:
            self.cc_block_qps = m.get('CcBlockQps')
        return self


class DescribeLogStoreExistStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeLogStoreExistStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        exist_status: bool = None,
    ):
        self.request_id = request_id
        self.exist_status = exist_status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.exist_status, 'exist_status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')
        return self


class DescribeBatchSlsDispatchStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeBatchSlsDispatchStatusResponseSlsConfigStatusList(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        domain: str = None,
    ):
        self.enable = enable
        self.domain = domain

    def validate(self):
        self.validate_required(self.enable, 'enable')
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeBatchSlsDispatchStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        sls_config_status_list: List[DescribeBatchSlsDispatchStatusResponseSlsConfigStatusList] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.sls_config_status_list = sls_config_status_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.sls_config_status_list, 'sls_config_status_list')
        if self.sls_config_status_list:
            for k in self.sls_config_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['SlsConfigStatusList'] = []
        if self.sls_config_status_list is not None:
            for k in self.sls_config_status_list:
                result['SlsConfigStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.sls_config_status_list = []
        if m.get('SlsConfigStatusList') is not None:
            for k in m.get('SlsConfigStatusList'):
                temp_model = DescribeBatchSlsDispatchStatusResponseSlsConfigStatusList()
                self.sls_config_status_list.append(temp_model.from_map(k))
        return self


class DescribeSlsEmptyCountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlsEmptyCountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        available_count: int = None,
    ):
        self.request_id = request_id
        self.available_count = available_count

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.available_count, 'available_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_count is not None:
            result['AvailableCount'] = self.available_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AvailableCount') is not None:
            self.available_count = m.get('AvailableCount')
        return self


class EmptySlsLogstoreRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class EmptySlsLogstoreResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloseDomainSlsConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class CloseDomainSlsConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenDomainSlsConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class OpenDomainSlsConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSlsLogstoreInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlsLogstoreInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        quota: int = None,
        log_store: str = None,
        used: int = None,
        project: str = None,
        ttl: int = None,
    ):
        self.request_id = request_id
        self.quota = quota
        self.log_store = log_store
        self.used = used
        self.project = project
        self.ttl = ttl

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.quota, 'quota')
        self.validate_required(self.log_store, 'log_store')
        self.validate_required(self.used, 'used')
        self.validate_required(self.project, 'project')
        self.validate_required(self.ttl, 'ttl')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class DescribeSlsAuthStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlsAuthStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_auth_status: bool = None,
    ):
        self.request_id = request_id
        self.sls_auth_status = sls_auth_status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sls_auth_status, 'sls_auth_status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_auth_status is not None:
            result['SlsAuthStatus'] = self.sls_auth_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsAuthStatus') is not None:
            self.sls_auth_status = m.get('SlsAuthStatus')
        return self


class DescribeSlsOpenStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlsOpenStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_open_status: bool = None,
    ):
        self.request_id = request_id
        self.sls_open_status = sls_open_status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sls_open_status, 'sls_open_status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_open_status is not None:
            result['SlsOpenStatus'] = self.sls_open_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsOpenStatus') is not None:
            self.sls_open_status = m.get('SlsOpenStatus')
        return self


class DescribeDomainSlsStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainSlsStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_status: bool = None,
        sls_logstore: str = None,
        sls_project: str = None,
    ):
        self.request_id = request_id
        self.sls_status = sls_status
        self.sls_logstore = sls_logstore
        self.sls_project = sls_project

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sls_status, 'sls_status')
        self.validate_required(self.sls_logstore, 'sls_logstore')
        self.validate_required(self.sls_project, 'sls_project')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_status is not None:
            result['SlsStatus'] = self.sls_status
        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsStatus') is not None:
            self.sls_status = m.get('SlsStatus')
        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        return self


class ConfigDomainAccessModeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        domain: str = None,
        access_mode: int = None,
    ):
        self.source_ip = source_ip
        self.domain = domain
        self.access_mode = access_mode

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.access_mode, 'access_mode')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class ConfigDomainAccessModeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainAccessModeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        domain_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        return self


class DescribeDomainAccessModeResponseDomainModeList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        access_mode: int = None,
    ):
        self.domain = domain
        self.access_mode = access_mode

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.access_mode, 'access_mode')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class DescribeDomainAccessModeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_mode_list: List[DescribeDomainAccessModeResponseDomainModeList] = None,
    ):
        self.request_id = request_id
        self.domain_mode_list = domain_mode_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_mode_list, 'domain_mode_list')
        if self.domain_mode_list:
            for k in self.domain_mode_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainModeList'] = []
        if self.domain_mode_list is not None:
            for k in self.domain_mode_list:
                result['DomainModeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_mode_list = []
        if m.get('DomainModeList') is not None:
            for k in m.get('DomainModeList'):
                temp_model = DescribeDomainAccessModeResponseDomainModeList()
                self.domain_mode_list.append(temp_model.from_map(k))
        return self


class DeleteAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        task_id: int = None,
    ):
        self.resource_group_id = resource_group_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        task_type: int = None,
        task_params: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.task_type = task_type
        self.task_params = task_params

    def validate(self):
        self.validate_required(self.task_type, 'task_type')
        self.validate_required(self.task_params, 'task_params')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        return self


class CreateAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_group_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAsyncTaskResponseAsyncTasks(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        end_time: int = None,
        start_time: int = None,
        task_status: int = None,
        task_result: str = None,
        task_params: str = None,
        task_type: int = None,
    ):
        self.task_id = task_id
        self.end_time = end_time
        self.start_time = start_time
        self.task_status = task_status
        self.task_result = task_result
        self.task_params = task_params
        self.task_type = task_type

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.task_status, 'task_status')
        self.validate_required(self.task_result, 'task_result')
        self.validate_required(self.task_params, 'task_params')
        self.validate_required(self.task_type, 'task_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        async_tasks: List[ListAsyncTaskResponseAsyncTasks] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.async_tasks = async_tasks

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.async_tasks, 'async_tasks')
        if self.async_tasks:
            for k in self.async_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['AsyncTasks'] = []
        if self.async_tasks is not None:
            for k in self.async_tasks:
                result['AsyncTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.async_tasks = []
        if m.get('AsyncTasks') is not None:
            for k in m.get('AsyncTasks'):
                temp_model = ListAsyncTaskResponseAsyncTasks()
                self.async_tasks.append(temp_model.from_map(k))
        return self


class EnableLayer7CCRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class EnableLayer7CCRuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableLayer7CCRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class EnableLayer7CCResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableLayer7CCRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DisableLayer7CCRuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableLayer7CCRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DisableLayer7CCResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribleLayer7InstanceRelationsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        return self


class DescribleLayer7InstanceRelationsResponseLayer7InstanceRelationsInstanceDetails(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        function_version: str = None,
        eip_list: List[str] = None,
    ):
        self.instance_id = instance_id
        self.function_version = function_version
        self.eip_list = eip_list

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.function_version, 'function_version')
        self.validate_required(self.eip_list, 'eip_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version
        if self.eip_list is not None:
            result['EipList'] = self.eip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')
        if m.get('EipList') is not None:
            self.eip_list = m.get('EipList')
        return self


class DescribleLayer7InstanceRelationsResponseLayer7InstanceRelations(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_details: List[DescribleLayer7InstanceRelationsResponseLayer7InstanceRelationsInstanceDetails] = None,
    ):
        self.domain = domain
        self.instance_details = instance_details

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.instance_details, 'instance_details')
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k in self.instance_details:
                result['InstanceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k in m.get('InstanceDetails'):
                temp_model = DescribleLayer7InstanceRelationsResponseLayer7InstanceRelationsInstanceDetails()
                self.instance_details.append(temp_model.from_map(k))
        return self


class DescribleLayer7InstanceRelationsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        layer_7instance_relations: List[DescribleLayer7InstanceRelationsResponseLayer7InstanceRelations] = None,
    ):
        self.request_id = request_id
        self.layer_7instance_relations = layer_7instance_relations

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.layer_7instance_relations, 'layer_7instance_relations')
        if self.layer_7instance_relations:
            for k in self.layer_7instance_relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Layer7InstanceRelations'] = []
        if self.layer_7instance_relations is not None:
            for k in self.layer_7instance_relations:
                result['Layer7InstanceRelations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.layer_7instance_relations = []
        if m.get('Layer7InstanceRelations') is not None:
            for k in m.get('Layer7InstanceRelations'):
                temp_model = DescribleLayer7InstanceRelationsResponseLayer7InstanceRelations()
                self.layer_7instance_relations.append(temp_model.from_map(k))
        return self


class DescribleCertListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribleCertListResponseCertList(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        common: str = None,
        issuer: str = None,
        start_date: str = None,
        end_date: str = None,
        domain_related: bool = None,
    ):
        self.id = id
        self.name = name
        self.common = common
        self.issuer = issuer
        self.start_date = start_date
        self.end_date = end_date
        self.domain_related = domain_related

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.common, 'common')
        self.validate_required(self.issuer, 'issuer')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.domain_related, 'domain_related')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DomainRelated') is not None:
            self.domain_related = m.get('DomainRelated')
        return self


class DescribleCertListResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cert_list: List[DescribleCertListResponseCertList] = None,
    ):
        self.request_id = request_id
        self.cert_list = cert_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.cert_list, 'cert_list')
        if self.cert_list:
            for k in self.cert_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CertList'] = []
        if self.cert_list is not None:
            for k in self.cert_list:
                result['CertList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.cert_list = []
        if m.get('CertList') is not None:
            for k in m.get('CertList'):
                temp_model = DescribleCertListResponseCertList()
                self.cert_list.append(temp_model.from_map(k))
        return self


class DescribeLayer7CCRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        offset: int = None,
        page_size: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.offset = offset
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeLayer7CCRulesResponseLayer7CCRules(TeaModel):
    def __init__(
        self,
        name: str = None,
        act: str = None,
        count: int = None,
        interval: int = None,
        mode: str = None,
        ttl: int = None,
        uri: str = None,
    ):
        self.name = name
        self.act = act
        self.count = count
        self.interval = interval
        self.mode = mode
        self.ttl = ttl
        self.uri = uri

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.act, 'act')
        self.validate_required(self.count, 'count')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeLayer7CCRulesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        layer_7ccrules: List[DescribeLayer7CCRulesResponseLayer7CCRules] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.layer_7ccrules = layer_7ccrules

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.layer_7ccrules, 'layer_7ccrules')
        if self.layer_7ccrules:
            for k in self.layer_7ccrules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Layer7CCRules'] = []
        if self.layer_7ccrules is not None:
            for k in self.layer_7ccrules:
                result['Layer7CCRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.layer_7ccrules = []
        if m.get('Layer7CCRules') is not None:
            for k in m.get('Layer7CCRules'):
                temp_model = DescribeLayer7CCRulesResponseLayer7CCRules()
                self.layer_7ccrules.append(temp_model.from_map(k))
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        query_domain_pattern: str = None,
        offset: int = None,
        page_size: str = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.query_domain_pattern = query_domain_pattern
        self.offset = offset
        self.page_size = page_size
        self.instance_ids = instance_ids

    def validate(self):
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('QueryDomainPattern') is not None:
            self.query_domain_pattern = m.get('QueryDomainPattern')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeDomainsResponseDomainsProxyTypeList(TeaModel):
    def __init__(
        self,
        proxy_type: str = None,
        proxy_ports: List[str] = None,
    ):
        self.proxy_type = proxy_type
        self.proxy_ports = proxy_ports

    def validate(self):
        self.validate_required(self.proxy_type, 'proxy_type')
        self.validate_required(self.proxy_ports, 'proxy_ports')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')
        return self


class DescribeDomainsResponseDomainsRealServers(TeaModel):
    def __init__(
        self,
        rs_type: int = None,
        real_server: str = None,
    ):
        self.rs_type = rs_type
        self.real_server = real_server

    def validate(self):
        self.validate_required(self.rs_type, 'rs_type')
        self.validate_required(self.real_server, 'real_server')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        return self


class DescribeDomainsResponseDomains(TeaModel):
    def __init__(
        self,
        domain: str = None,
        cc_enabled: bool = None,
        cc_rule_enabled: bool = None,
        cc_template: str = None,
        ssl_protocols: str = None,
        ssl_ciphers: str = None,
        http_2enable: bool = None,
        cname: str = None,
        cert_name: str = None,
        proxy_type_list: List[DescribeDomainsResponseDomainsProxyTypeList] = None,
        real_servers: List[DescribeDomainsResponseDomainsRealServers] = None,
        white_list: List[str] = None,
        black_list: List[str] = None,
    ):
        self.domain = domain
        self.cc_enabled = cc_enabled
        self.cc_rule_enabled = cc_rule_enabled
        self.cc_template = cc_template
        self.ssl_protocols = ssl_protocols
        self.ssl_ciphers = ssl_ciphers
        self.http_2enable = http_2enable
        self.cname = cname
        self.cert_name = cert_name
        self.proxy_type_list = proxy_type_list
        self.real_servers = real_servers
        self.white_list = white_list
        self.black_list = black_list

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CcEnabled') is not None:
            self.cc_enabled = m.get('CcEnabled')
        if m.get('CcRuleEnabled') is not None:
            self.cc_rule_enabled = m.get('CcRuleEnabled')
        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')
        if m.get('SslProtocols') is not None:
            self.ssl_protocols = m.get('SslProtocols')
        if m.get('SslCiphers') is not None:
            self.ssl_ciphers = m.get('SslCiphers')
        if m.get('Http2Enable') is not None:
            self.http_2enable = m.get('Http2Enable')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        self.proxy_type_list = []
        if m.get('ProxyTypeList') is not None:
            for k in m.get('ProxyTypeList'):
                temp_model = DescribeDomainsResponseDomainsProxyTypeList()
                self.proxy_type_list.append(temp_model.from_map(k))
        self.real_servers = []
        if m.get('RealServers') is not None:
            for k in m.get('RealServers'):
                temp_model = DescribeDomainsResponseDomainsRealServers()
                self.real_servers.append(temp_model.from_map(k))
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        return self


class DescribeDomainsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        domains: List[DescribeDomainsResponseDomains] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.domains = domains

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.domains, 'domains')
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = DescribeDomainsResponseDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class DescribeDomainQpsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        domain: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDomainQpsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        interval: int = None,
        start_time: int = None,
        totals: List[str] = None,
        blocks: List[str] = None,
        cache_hits: List[str] = None,
        precise_blocks: List[str] = None,
        region_blocks: List[str] = None,
        ip_block_qps: List[str] = None,
        cc_js_qps: List[str] = None,
        precise_js_qps: List[str] = None,
        cc_block_qps: List[str] = None,
    ):
        self.request_id = request_id
        self.interval = interval
        self.start_time = start_time
        self.totals = totals
        self.blocks = blocks
        self.cache_hits = cache_hits
        self.precise_blocks = precise_blocks
        self.region_blocks = region_blocks
        self.ip_block_qps = ip_block_qps
        self.cc_js_qps = cc_js_qps
        self.precise_js_qps = precise_js_qps
        self.cc_block_qps = cc_block_qps

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Totals') is not None:
            self.totals = m.get('Totals')
        if m.get('Blocks') is not None:
            self.blocks = m.get('Blocks')
        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')
        if m.get('PreciseBlocks') is not None:
            self.precise_blocks = m.get('PreciseBlocks')
        if m.get('RegionBlocks') is not None:
            self.region_blocks = m.get('RegionBlocks')
        if m.get('IpBlockQps') is not None:
            self.ip_block_qps = m.get('IpBlockQps')
        if m.get('CcJsQps') is not None:
            self.cc_js_qps = m.get('CcJsQps')
        if m.get('PreciseJsQps') is not None:
            self.precise_js_qps = m.get('PreciseJsQps')
        if m.get('CcBlockQps') is not None:
            self.cc_block_qps = m.get('CcBlockQps')
        return self


class DescribeDomainAttackEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        domain: str = None,
        offset: int = None,
        page_size: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain = domain
        self.offset = offset
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDomainAttackEventsResponseEvents(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        duration: int = None,
        finished: bool = None,
        max_qps: int = None,
        block_count: int = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.finished = finished
        self.max_qps = max_qps
        self.block_count = block_count

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.finished, 'finished')
        self.validate_required(self.max_qps, 'max_qps')
        self.validate_required(self.block_count, 'block_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        return self


class DescribeDomainAttackEventsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        events: List[DescribeDomainAttackEventsResponseEvents] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.events = events

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.events, 'events')
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeDomainAttackEventsResponseEvents()
                self.events.append(temp_model.from_map(k))
        return self


class DescribeBackSourceCidrRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        line: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class DescribeBackSourceCidrResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cidr_list: List[str] = None,
    ):
        self.request_id = request_id
        self.cidr_list = cidr_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.cidr_list, 'cidr_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cidr_list is not None:
            result['CidrList'] = self.cidr_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CidrList') is not None:
            self.cidr_list = m.get('CidrList')
        return self


class DeleteLayer7RuleRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        domain: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DeleteLayer7RuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLayer7CCRuleRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        domain: str = None,
        name: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.name = name

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteLayer7CCRuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLayer7RuleRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        domain: str = None,
        rs_type: int = None,
        rules: str = None,
        instance_ids: List[str] = None,
    ):
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.rs_type = rs_type
        self.rules = rules
        self.instance_ids = instance_ids

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.rs_type, 'rs_type')
        self.validate_required(self.rules, 'rules')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class CreateLayer7RuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigLayer7RuleRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        domain: str = None,
        proxy_type_list: str = None,
        proxy_types: List[str] = None,
        rs_type: int = None,
        real_servers: List[str] = None,
        instance_ids: List[str] = None,
    ):
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.proxy_type_list = proxy_type_list
        self.proxy_types = proxy_types
        self.rs_type = rs_type
        self.real_servers = real_servers
        self.instance_ids = instance_ids

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.rs_type, 'rs_type')
        self.validate_required(self.real_servers, 'real_servers')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ProxyTypeList') is not None:
            self.proxy_type_list = m.get('ProxyTypeList')
        if m.get('ProxyTypes') is not None:
            self.proxy_types = m.get('ProxyTypes')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class ConfigLayer7RuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigLayer7CertRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        domain: str = None,
        cert_id: int = None,
        cert_name: str = None,
        cert: str = None,
        key: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.cert = cert
        self.key = key

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ConfigLayer7CertResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigLayer7CCTemplateRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        domain: str = None,
        template: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.template = template

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.template, 'template')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ConfigLayer7CCTemplateResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigLayer7CCRuleRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        domain: str = None,
        name: str = None,
        act: str = None,
        count: int = None,
        interval: int = None,
        mode: str = None,
        ttl: int = None,
        uri: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.name = name
        self.act = act
        self.count = count
        self.interval = interval
        self.mode = mode
        self.ttl = ttl
        self.uri = uri

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ConfigLayer7CCRuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigLayer7BlackWhiteListRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        domain: str = None,
        black_list: List[str] = None,
        white_list: List[str] = None,
    ):
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.black_list = black_list
        self.white_list = white_list

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ConfigLayer7BlackWhiteListResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddLayer7CCRuleRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        domain: str = None,
        name: str = None,
        act: str = None,
        count: int = None,
        interval: int = None,
        mode: str = None,
        ttl: int = None,
        uri: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.domain = domain
        self.name = name
        self.act = act
        self.count = count
        self.interval = interval
        self.mode = mode
        self.ttl = ttl
        self.uri = uri

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class AddLayer7CCRuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleaseInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceRemarkRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        remark: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ModifyInstanceRemarkResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyElasticBandWidthRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        elastic_bandwidth: int = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.elastic_bandwidth = elastic_bandwidth
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.elastic_bandwidth, 'elastic_bandwidth')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyElasticBandWidthResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        entity_type: int = None,
        entity_object: str = None,
        start_time: int = None,
        end_time: int = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.entity_type = entity_type
        self.entity_object = entity_object
        self.start_time = start_time
        self.end_time = end_time
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeOpEntitiesResponseOpEntities(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        entity_type: int = None,
        entity_object: str = None,
        op_action: int = None,
        op_account: str = None,
        op_desc: str = None,
    ):
        self.gmt_create = gmt_create
        self.entity_type = entity_type
        self.entity_object = entity_object
        self.op_action = op_action
        self.op_account = op_account
        self.op_desc = op_desc

    def validate(self):
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.entity_type, 'entity_type')
        self.validate_required(self.entity_object, 'entity_object')
        self.validate_required(self.op_action, 'op_action')
        self.validate_required(self.op_account, 'op_account')
        self.validate_required(self.op_desc, 'op_desc')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')
        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')
        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')
        return self


class DescribeOpEntitiesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        op_entities: List[DescribeOpEntitiesResponseOpEntities] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.op_entities = op_entities

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.op_entities, 'op_entities')
        if self.op_entities:
            for k in self.op_entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.op_entities = []
        if m.get('OpEntities') is not None:
            for k in m.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        return self


class DescribeLayer4RulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        forward_protocol: str = None,
        frontend_port: int = None,
        offset: int = None,
        page_size: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.forward_protocol = forward_protocol
        self.frontend_port = frontend_port
        self.offset = offset
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeLayer4RulesResponseListeners(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        protocol: str = None,
        frontend_port: int = None,
        backend_port: int = None,
        is_auto_create: bool = None,
        real_servers: List[str] = None,
    ):
        self.instance_id = instance_id
        self.protocol = protocol
        self.frontend_port = frontend_port
        self.backend_port = backend_port
        self.is_auto_create = is_auto_create
        self.real_servers = real_servers

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.backend_port, 'backend_port')
        self.validate_required(self.is_auto_create, 'is_auto_create')
        self.validate_required(self.real_servers, 'real_servers')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')
        if m.get('IsAutoCreate') is not None:
            self.is_auto_create = m.get('IsAutoCreate')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        return self


class DescribeLayer4RulesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        listeners: List[DescribeLayer4RulesResponseListeners] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.listeners = listeners

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.listeners, 'listeners')
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = DescribeLayer4RulesResponseListeners()
                self.listeners.append(temp_model.from_map(k))
        return self


class DescribeLayer4RuleAttributesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        listeners: str = None,
    ):
        self.source_ip = source_ip
        self.listeners = listeners

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class DescribeLayer4RuleAttributesResponseListenersConfigSla(TeaModel):
    def __init__(
        self,
        cps: int = None,
        maxconn: int = None,
        cps_enable: int = None,
        maxconn_enable: int = None,
    ):
        self.cps = cps
        self.maxconn = maxconn
        self.cps_enable = cps_enable
        self.maxconn_enable = maxconn_enable

    def validate(self):
        self.validate_required(self.cps, 'cps')
        self.validate_required(self.maxconn, 'maxconn')
        self.validate_required(self.cps_enable, 'cps_enable')
        self.validate_required(self.maxconn_enable, 'maxconn_enable')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')
        return self


class DescribeLayer4RuleAttributesResponseListenersConfigSlimit(TeaModel):
    def __init__(
        self,
        cps: int = None,
        maxconn: int = None,
        cps_enable: int = None,
        cps_mode: int = None,
        maxconn_enable: int = None,
        bps: int = None,
        pps: int = None,
    ):
        self.cps = cps
        self.maxconn = maxconn
        self.cps_enable = cps_enable
        self.cps_mode = cps_mode
        self.maxconn_enable = maxconn_enable
        self.bps = bps
        self.pps = pps

    def validate(self):
        self.validate_required(self.cps, 'cps')
        self.validate_required(self.maxconn, 'maxconn')
        self.validate_required(self.cps_enable, 'cps_enable')
        self.validate_required(self.cps_mode, 'cps_mode')
        self.validate_required(self.maxconn_enable, 'maxconn_enable')
        self.validate_required(self.bps, 'bps')
        self.validate_required(self.pps, 'pps')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('CpsMode') is not None:
            self.cps_mode = m.get('CpsMode')
        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeLayer4RuleAttributesResponseListenersConfigPayloadLen(TeaModel):
    def __init__(
        self,
        min: int = None,
        max: int = None,
    ):
        self.min = min
        self.max = max

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.min is not None:
            result['Min'] = self.min
        if self.max is not None:
            result['Max'] = self.max
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Max') is not None:
            self.max = m.get('Max')
        return self


class DescribeLayer4RuleAttributesResponseListenersConfigCcSblack(TeaModel):
    def __init__(
        self,
        during: int = None,
        expires: int = None,
        cnt: int = None,
        type: int = None,
    ):
        self.during = during
        self.expires = expires
        self.cnt = cnt
        self.type = type

    def validate(self):
        self.validate_required(self.during, 'during')
        self.validate_required(self.expires, 'expires')
        self.validate_required(self.cnt, 'cnt')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.during is not None:
            result['During'] = self.during
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.cnt is not None:
            result['Cnt'] = self.cnt
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('During') is not None:
            self.during = m.get('During')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeLayer4RuleAttributesResponseListenersConfigCc(TeaModel):
    def __init__(
        self,
        sblack: List[DescribeLayer4RuleAttributesResponseListenersConfigCcSblack] = None,
    ):
        self.sblack = sblack

    def validate(self):
        self.validate_required(self.sblack, 'sblack')
        if self.sblack:
            for k in self.sblack:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sblack'] = []
        if self.sblack is not None:
            for k in self.sblack:
                result['Sblack'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sblack = []
        if m.get('Sblack') is not None:
            for k in m.get('Sblack'):
                temp_model = DescribeLayer4RuleAttributesResponseListenersConfigCcSblack()
                self.sblack.append(temp_model.from_map(k))
        return self


class DescribeLayer4RuleAttributesResponseListenersConfig(TeaModel):
    def __init__(
        self,
        persistence_timeout: int = None,
        synproxy: str = None,
        nodata_conn: str = None,
        sla: DescribeLayer4RuleAttributesResponseListenersConfigSla = None,
        slimit: DescribeLayer4RuleAttributesResponseListenersConfigSlimit = None,
        payload_len: DescribeLayer4RuleAttributesResponseListenersConfigPayloadLen = None,
        cc: DescribeLayer4RuleAttributesResponseListenersConfigCc = None,
    ):
        self.persistence_timeout = persistence_timeout
        self.synproxy = synproxy
        self.nodata_conn = nodata_conn
        self.sla = sla
        self.slimit = slimit
        self.payload_len = payload_len
        self.cc = cc

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('Synproxy') is not None:
            self.synproxy = m.get('Synproxy')
        if m.get('NodataConn') is not None:
            self.nodata_conn = m.get('NodataConn')
        if m.get('Sla') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseListenersConfigSla()
            self.sla = temp_model.from_map(m['Sla'])
        if m.get('Slimit') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseListenersConfigSlimit()
            self.slimit = temp_model.from_map(m['Slimit'])
        if m.get('PayloadLen') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseListenersConfigPayloadLen()
            self.payload_len = temp_model.from_map(m['PayloadLen'])
        if m.get('Cc') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseListenersConfigCc()
            self.cc = temp_model.from_map(m['Cc'])
        return self


class DescribeLayer4RuleAttributesResponseListeners(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        protocol: str = None,
        frontend_port: int = None,
        config: DescribeLayer4RuleAttributesResponseListenersConfig = None,
    ):
        self.instance_id = instance_id
        self.protocol = protocol
        self.frontend_port = frontend_port
        self.config = config

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.config, 'config')
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.config is not None:
            result['Config'] = self.config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Config') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseListenersConfig()
            self.config = temp_model.from_map(m['Config'])
        return self


class DescribeLayer4RuleAttributesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        listeners: List[DescribeLayer4RuleAttributesResponseListeners] = None,
    ):
        self.request_id = request_id
        self.listeners = listeners

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.listeners, 'listeners')
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = DescribeLayer4RuleAttributesResponseListeners()
                self.listeners.append(temp_model.from_map(k))
        return self


class DescribeIpTrafficRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        interval: int = None,
        end_time: int = None,
        eip: str = None,
        port: int = None,
        query_protocol: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.interval = interval
        self.end_time = end_time
        self.eip = eip
        self.port = port
        self.query_protocol = query_protocol

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.eip, 'eip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('QueryProtocol') is not None:
            self.query_protocol = m.get('QueryProtocol')
        return self


class DescribeIpTrafficResponseIpTrafficPoints(TeaModel):
    def __init__(
        self,
        time: int = None,
        max_inbps: int = None,
        max_outbps: int = None,
        cps: int = None,
        act_conns: int = None,
        inact_conns: int = None,
    ):
        self.time = time
        self.max_inbps = max_inbps
        self.max_outbps = max_outbps
        self.cps = cps
        self.act_conns = act_conns
        self.inact_conns = inact_conns

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.max_inbps, 'max_inbps')
        self.validate_required(self.max_outbps, 'max_outbps')
        self.validate_required(self.cps, 'cps')
        self.validate_required(self.act_conns, 'act_conns')
        self.validate_required(self.inact_conns, 'inact_conns')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('MaxInbps') is not None:
            self.max_inbps = m.get('MaxInbps')
        if m.get('MaxOutbps') is not None:
            self.max_outbps = m.get('MaxOutbps')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')
        if m.get('InactConns') is not None:
            self.inact_conns = m.get('InactConns')
        return self


class DescribeIpTrafficResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        max_in_bps: int = None,
        avg_in_bps: int = None,
        max_out_bps: int = None,
        avg_out_bps: int = None,
        ip_traffic_points: List[DescribeIpTrafficResponseIpTrafficPoints] = None,
    ):
        self.request_id = request_id
        self.max_in_bps = max_in_bps
        self.avg_in_bps = avg_in_bps
        self.max_out_bps = max_out_bps
        self.avg_out_bps = avg_out_bps
        self.ip_traffic_points = ip_traffic_points

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxInBps') is not None:
            self.max_in_bps = m.get('MaxInBps')
        if m.get('AvgInBps') is not None:
            self.avg_in_bps = m.get('AvgInBps')
        if m.get('MaxOutBps') is not None:
            self.max_out_bps = m.get('MaxOutBps')
        if m.get('AvgOutBps') is not None:
            self.avg_out_bps = m.get('AvgOutBps')
        self.ip_traffic_points = []
        if m.get('IpTrafficPoints') is not None:
            for k in m.get('IpTrafficPoints'):
                temp_model = DescribeIpTrafficResponseIpTrafficPoints()
                self.ip_traffic_points.append(temp_model.from_map(k))
        return self


class DescribeInstanceStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_ids: str = None,
    ):
        self.source_ip = source_ip
        self.instance_ids = instance_ids

    def validate(self):
        self.validate_required(self.instance_ids, 'instance_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceStatisticsResponseInstanceStatistics(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        port_usage: int = None,
        domain_usage: int = None,
        site_usage: int = None,
        defense_count_usage: int = None,
    ):
        self.instance_id = instance_id
        self.port_usage = port_usage
        self.domain_usage = domain_usage
        self.site_usage = site_usage
        self.defense_count_usage = defense_count_usage

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.port_usage, 'port_usage')
        self.validate_required(self.domain_usage, 'domain_usage')
        self.validate_required(self.site_usage, 'site_usage')
        self.validate_required(self.defense_count_usage, 'defense_count_usage')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PortUsage') is not None:
            self.port_usage = m.get('PortUsage')
        if m.get('DomainUsage') is not None:
            self.domain_usage = m.get('DomainUsage')
        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')
        if m.get('DefenseCountUsage') is not None:
            self.defense_count_usage = m.get('DefenseCountUsage')
        return self


class DescribeInstanceStatisticsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_statistics: List[DescribeInstanceStatisticsResponseInstanceStatistics] = None,
    ):
        self.request_id = request_id
        self.instance_statistics = instance_statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_statistics, 'instance_statistics')
        if self.instance_statistics:
            for k in self.instance_statistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceStatistics'] = []
        if self.instance_statistics is not None:
            for k in self.instance_statistics:
                result['InstanceStatistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_statistics = []
        if m.get('InstanceStatistics') is not None:
            for k in m.get('InstanceStatistics'):
                temp_model = DescribeInstanceStatisticsResponseInstanceStatistics()
                self.instance_statistics.append(temp_model.from_map(k))
        return self


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_ids: str = None,
    ):
        self.source_ip = source_ip
        self.instance_ids = instance_ids

    def validate(self):
        self.validate_required(self.instance_ids, 'instance_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceSpecsResponseInstanceSpecs(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        base_bandwidth: int = None,
        elastic_bandwidth: int = None,
        port_limit: int = None,
        site_limit: int = None,
        domain_limit: int = None,
        bandwidth_mbps: int = None,
        defense_count: int = None,
        function_version: str = None,
        qps_limit: int = None,
    ):
        self.instance_id = instance_id
        self.base_bandwidth = base_bandwidth
        self.elastic_bandwidth = elastic_bandwidth
        self.port_limit = port_limit
        self.site_limit = site_limit
        self.domain_limit = domain_limit
        self.bandwidth_mbps = bandwidth_mbps
        self.defense_count = defense_count
        self.function_version = function_version
        self.qps_limit = qps_limit

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BaseBandwidth') is not None:
            self.base_bandwidth = m.get('BaseBandwidth')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('PortLimit') is not None:
            self.port_limit = m.get('PortLimit')
        if m.get('SiteLimit') is not None:
            self.site_limit = m.get('SiteLimit')
        if m.get('DomainLimit') is not None:
            self.domain_limit = m.get('DomainLimit')
        if m.get('BandwidthMbps') is not None:
            self.bandwidth_mbps = m.get('BandwidthMbps')
        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')
        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')
        if m.get('QpsLimit') is not None:
            self.qps_limit = m.get('QpsLimit')
        return self


class DescribeInstanceSpecsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_specs: List[DescribeInstanceSpecsResponseInstanceSpecs] = None,
    ):
        self.request_id = request_id
        self.instance_specs = instance_specs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_specs, 'instance_specs')
        if self.instance_specs:
            for k in self.instance_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k in self.instance_specs:
                result['InstanceSpecs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_specs = []
        if m.get('InstanceSpecs') is not None:
            for k in m.get('InstanceSpecs'):
                temp_model = DescribeInstanceSpecsResponseInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k))
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        instance_ids: str = None,
        page_no: str = None,
        page_size: str = None,
        ip: str = None,
        remark: str = None,
        edition: int = None,
        enabled: int = None,
        expire_start_time: int = None,
        expire_end_time: int = None,
        status: List[int] = None,
        tag: List[DescribeInstancesRequestTag] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.instance_ids = instance_ids
        self.page_no = page_no
        self.page_size = page_size
        self.ip = ip
        self.remark = remark
        self.edition = edition
        self.enabled = enabled
        self.expire_start_time = expire_start_time
        self.expire_end_time = expire_end_time
        self.status = status
        self.tag = tag

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExpireStartTime') is not None:
            self.expire_start_time = m.get('ExpireStartTime')
        if m.get('ExpireEndTime') is not None:
            self.expire_end_time = m.get('ExpireEndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        remark: str = None,
        status: int = None,
        debt_status: int = None,
        expire_time: int = None,
        gmt_create: int = None,
        edition: int = None,
        enabled: int = None,
    ):
        self.instance_id = instance_id
        self.remark = remark
        self.status = status
        self.debt_status = debt_status
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.edition = edition
        self.enabled = enabled

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DebtStatus') is not None:
            self.debt_status = m.get('DebtStatus')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        instances: List[DescribeInstancesResponseInstances] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.instances = instances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeInstanceDetailsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_ids: str = None,
    ):
        self.source_ip = source_ip
        self.instance_ids = instance_ids

    def validate(self):
        self.validate_required(self.instance_ids, 'instance_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceDetailsResponseInstanceDetailsEipInfoList(TeaModel):
    def __init__(
        self,
        eip: str = None,
        status: str = None,
    ):
        self.eip = eip
        self.status = status

    def validate(self):
        self.validate_required(self.eip, 'eip')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstanceDetailsResponseInstanceDetails(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        line: str = None,
        eip_info_list: List[DescribeInstanceDetailsResponseInstanceDetailsEipInfoList] = None,
    ):
        self.instance_id = instance_id
        self.line = line
        self.eip_info_list = eip_info_list

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.line, 'line')
        self.validate_required(self.eip_info_list, 'eip_info_list')
        if self.eip_info_list:
            for k in self.eip_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.line is not None:
            result['Line'] = self.line
        result['EipInfoList'] = []
        if self.eip_info_list is not None:
            for k in self.eip_info_list:
                result['EipInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        self.eip_info_list = []
        if m.get('EipInfoList') is not None:
            for k in m.get('EipInfoList'):
                temp_model = DescribeInstanceDetailsResponseInstanceDetailsEipInfoList()
                self.eip_info_list.append(temp_model.from_map(k))
        return self


class DescribeInstanceDetailsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_details: List[DescribeInstanceDetailsResponseInstanceDetails] = None,
    ):
        self.request_id = request_id
        self.instance_details = instance_details

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_details, 'instance_details')
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k in self.instance_details:
                result['InstanceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k in m.get('InstanceDetails'):
                temp_model = DescribeInstanceDetailsResponseInstanceDetails()
                self.instance_details.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckStatusListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        listeners: str = None,
    ):
        self.source_ip = source_ip
        self.listeners = listeners

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class DescribeHealthCheckStatusListResponseHealthCheckStatusListRealServerStatusList(TeaModel):
    def __init__(
        self,
        address: str = None,
        status: str = None,
    ):
        self.address = address
        self.status = status

    def validate(self):
        self.validate_required(self.address, 'address')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeHealthCheckStatusListResponseHealthCheckStatusList(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        protocol: str = None,
        frontend_port: int = None,
        status: str = None,
        real_server_status_list: List[DescribeHealthCheckStatusListResponseHealthCheckStatusListRealServerStatusList] = None,
    ):
        self.instance_id = instance_id
        self.protocol = protocol
        self.frontend_port = frontend_port
        self.status = status
        self.real_server_status_list = real_server_status_list

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.real_server_status_list = []
        if m.get('RealServerStatusList') is not None:
            for k in m.get('RealServerStatusList'):
                temp_model = DescribeHealthCheckStatusListResponseHealthCheckStatusListRealServerStatusList()
                self.real_server_status_list.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckStatusListResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        health_check_status_list: List[DescribeHealthCheckStatusListResponseHealthCheckStatusList] = None,
    ):
        self.request_id = request_id
        self.health_check_status_list = health_check_status_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.health_check_status_list, 'health_check_status_list')
        if self.health_check_status_list:
            for k in self.health_check_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HealthCheckStatusList'] = []
        if self.health_check_status_list is not None:
            for k in self.health_check_status_list:
                result['HealthCheckStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.health_check_status_list = []
        if m.get('HealthCheckStatusList') is not None:
            for k in m.get('HealthCheckStatusList'):
                temp_model = DescribeHealthCheckStatusListResponseHealthCheckStatusList()
                self.health_check_status_list.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        listeners: str = None,
    ):
        self.source_ip = source_ip
        self.listeners = listeners

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class DescribeHealthCheckListResponseListenersHealthCheck(TeaModel):
    def __init__(
        self,
        type: str = None,
        domain: str = None,
        uri: str = None,
        down: int = None,
        interval: int = None,
        port: int = None,
        timeout: int = None,
        up: int = None,
    ):
        self.type = type
        self.domain = domain
        self.uri = uri
        self.down = down
        self.interval = interval
        self.port = port
        self.timeout = timeout
        self.up = up

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('Down') is not None:
            self.down = m.get('Down')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Up') is not None:
            self.up = m.get('Up')
        return self


class DescribeHealthCheckListResponseListeners(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        protocol: str = None,
        frontend_port: int = None,
        health_check: DescribeHealthCheckListResponseListenersHealthCheck = None,
    ):
        self.instance_id = instance_id
        self.protocol = protocol
        self.frontend_port = frontend_port
        self.health_check = health_check

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.health_check, 'health_check')
        if self.health_check:
            self.health_check.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('HealthCheck') is not None:
            temp_model = DescribeHealthCheckListResponseListenersHealthCheck()
            self.health_check = temp_model.from_map(m['HealthCheck'])
        return self


class DescribeHealthCheckListResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        listeners: List[DescribeHealthCheckListResponseListeners] = None,
    ):
        self.request_id = request_id
        self.listeners = listeners

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.listeners, 'listeners')
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = DescribeHealthCheckListResponseListeners()
                self.listeners.append(temp_model.from_map(k))
        return self


class DescribeElasticBandwidthSpecRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeElasticBandwidthSpecResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        elastic_bandwidth_spec: List[str] = None,
    ):
        self.request_id = request_id
        self.elastic_bandwidth_spec = elastic_bandwidth_spec

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.elastic_bandwidth_spec, 'elastic_bandwidth_spec')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.elastic_bandwidth_spec is not None:
            result['ElasticBandwidthSpec'] = self.elastic_bandwidth_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ElasticBandwidthSpec') is not None:
            self.elastic_bandwidth_spec = m.get('ElasticBandwidthSpec')
        return self


class DescribeDDoSTrafficRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        interval: int = None,
        end_time: int = None,
        eip: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.interval = interval
        self.end_time = end_time
        self.eip = eip

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.eip, 'eip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        return self


class DescribeDDoSTrafficResponseDDoSTrafficPoints(TeaModel):
    def __init__(
        self,
        time: int = None,
        defense_max_in_bps: int = None,
        source_max_in_bps: int = None,
    ):
        self.time = time
        self.defense_max_in_bps = defense_max_in_bps
        self.source_max_in_bps = source_max_in_bps

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.defense_max_in_bps, 'defense_max_in_bps')
        self.validate_required(self.source_max_in_bps, 'source_max_in_bps')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.defense_max_in_bps is not None:
            result['DefenseMaxInBps'] = self.defense_max_in_bps
        if self.source_max_in_bps is not None:
            result['SourceMaxInBps'] = self.source_max_in_bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('DefenseMaxInBps') is not None:
            self.defense_max_in_bps = m.get('DefenseMaxInBps')
        if m.get('SourceMaxInBps') is not None:
            self.source_max_in_bps = m.get('SourceMaxInBps')
        return self


class DescribeDDoSTrafficResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        defense_in_bytes: int = None,
        source_in_bytes: int = None,
        ddo_straffic_points: List[DescribeDDoSTrafficResponseDDoSTrafficPoints] = None,
    ):
        self.request_id = request_id
        self.defense_in_bytes = defense_in_bytes
        self.source_in_bytes = source_in_bytes
        self.ddo_straffic_points = ddo_straffic_points

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DefenseInBytes') is not None:
            self.defense_in_bytes = m.get('DefenseInBytes')
        if m.get('SourceInBytes') is not None:
            self.source_in_bytes = m.get('SourceInBytes')
        self.ddo_straffic_points = []
        if m.get('DDoSTrafficPoints') is not None:
            for k in m.get('DDoSTrafficPoints'):
                temp_model = DescribeDDoSTrafficResponseDDoSTrafficPoints()
                self.ddo_straffic_points.append(temp_model.from_map(k))
        return self


class DescribeDDoSEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        eip: str = None,
        offset: int = None,
        page_size: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.eip = eip
        self.offset = offset
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.eip, 'eip')
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDDoSEventsResponseEvents(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        interval: int = None,
        status: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.status = status

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDDoSEventsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        events: List[DescribeDDoSEventsResponseEvents] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.events = events

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.events, 'events')
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeDDoSEventsResponseEvents()
                self.events.append(temp_model.from_map(k))
        return self


class DeleteLayer4RuleRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
    ):
        self.listeners = listeners

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class DeleteLayer4RuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLayer4RuleRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
    ):
        self.listeners = listeners

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class CreateLayer4RuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigLayer4RuleAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        forward_protocol: str = None,
        frontend_port: int = None,
        config: str = None,
    ):
        self.instance_id = instance_id
        self.forward_protocol = forward_protocol
        self.frontend_port = frontend_port
        self.config = config

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.forward_protocol, 'forward_protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.config, 'config')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ConfigLayer4RuleAttributeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigLayer4RuleRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
    ):
        self.listeners = listeners

    def validate(self):
        self.validate_required(self.listeners, 'listeners')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class ConfigLayer4RuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigHealthCheckRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        forward_protocol: str = None,
        frontend_port: int = None,
        health_check: str = None,
    ):
        self.instance_id = instance_id
        self.forward_protocol = forward_protocol
        self.frontend_port = frontend_port
        self.health_check = health_check

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.forward_protocol, 'forward_protocol')
        self.validate_required(self.frontend_port, 'frontend_port')
        self.validate_required(self.health_check, 'health_check')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        return self


class ConfigHealthCheckResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self



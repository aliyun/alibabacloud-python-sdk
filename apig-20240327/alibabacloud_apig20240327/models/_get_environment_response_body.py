# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetEnvironmentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetEnvironmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Response data.
        self.data = data
        # Response message.
        self.message = message
        # Request ID, used for tracing the API call chain.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetEnvironmentResponseBodyData(DaraModel):
    def __init__(
        self,
        alias: str = None,
        create_timestamp: int = None,
        default: bool = None,
        description: str = None,
        environment_id: str = None,
        gateway_info: main_models.GatewayInfo = None,
        name: str = None,
        resource_group_id: str = None,
        statistics_info: main_models.GetEnvironmentResponseBodyDataStatisticsInfo = None,
        sub_domain_infos: List[main_models.SubDomainInfo] = None,
        update_timestamp: int = None,
    ):
        # Environment alias.
        self.alias = alias
        # Creation timestamp.
        self.create_timestamp = create_timestamp
        # Whether it is the default environment.
        self.default = default
        # Environment description.
        self.description = description
        # Environment ID.
        self.environment_id = environment_id
        # Gateway information
        self.gateway_info = gateway_info
        # Environment name.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Related resource information.
        self.statistics_info = statistics_info
        # List of subdomains.
        self.sub_domain_infos = sub_domain_infos
        # Update timestamp.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.gateway_info:
            self.gateway_info.validate()
        if self.statistics_info:
            self.statistics_info.validate()
        if self.sub_domain_infos:
            for v1 in self.sub_domain_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.default is not None:
            result['default'] = self.default

        if self.description is not None:
            result['description'] = self.description

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.statistics_info is not None:
            result['statisticsInfo'] = self.statistics_info.to_map()

        result['subDomainInfos'] = []
        if self.sub_domain_infos is not None:
            for k1 in self.sub_domain_infos:
                result['subDomainInfos'].append(k1.to_map() if k1 else None)

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('default') is not None:
            self.default = m.get('default')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.GatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('statisticsInfo') is not None:
            temp_model = main_models.GetEnvironmentResponseBodyDataStatisticsInfo()
            self.statistics_info = temp_model.from_map(m.get('statisticsInfo'))

        self.sub_domain_infos = []
        if m.get('subDomainInfos') is not None:
            for k1 in m.get('subDomainInfos'):
                temp_model = main_models.SubDomainInfo()
                self.sub_domain_infos.append(temp_model.from_map(k1))

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

class GetEnvironmentResponseBodyDataStatisticsInfo(DaraModel):
    def __init__(
        self,
        resource_statistics: List[main_models.ResourceStatistic] = None,
        total_count: int = None,
    ):
        # The array of related resource information.
        self.resource_statistics = resource_statistics
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resource_statistics:
            for v1 in self.resource_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['resourceStatistics'] = []
        if self.resource_statistics is not None:
            for k1 in self.resource_statistics:
                result['resourceStatistics'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_statistics = []
        if m.get('resourceStatistics') is not None:
            for k1 in m.get('resourceStatistics'):
                temp_model = main_models.ResourceStatistic()
                self.resource_statistics.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self


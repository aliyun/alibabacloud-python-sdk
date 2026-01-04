# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        instance_statistics: List[main_models.DescribeInstanceStatisticsResponseBodyInstanceStatistics] = None,
        request_id: str = None,
    ):
        # The statistics on the instance.
        self.instance_statistics = instance_statistics
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.instance_statistics:
            for v1 in self.instance_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceStatistics'] = []
        if self.instance_statistics is not None:
            for k1 in self.instance_statistics:
                result['InstanceStatistics'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_statistics = []
        if m.get('InstanceStatistics') is not None:
            for k1 in m.get('InstanceStatistics'):
                temp_model = main_models.DescribeInstanceStatisticsResponseBodyInstanceStatistics()
                self.instance_statistics.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceStatisticsResponseBodyInstanceStatistics(DaraModel):
    def __init__(
        self,
        defense_count_usage: int = None,
        domain_usage: int = None,
        instance_id: str = None,
        port_usage: int = None,
        site_usage: int = None,
    ):
        # The number of advanced mitigation sessions that are used in this month.
        # 
        # >  This parameter is returned only if Anti-DDoS Proxy (Outside Chinese Mainland) instances are queried.
        self.defense_count_usage = defense_count_usage
        # The number of domain names that are protected by the instance.
        self.domain_usage = domain_usage
        # The ID of the instance.
        self.instance_id = instance_id
        # The number of ports that are protected by the instance.
        self.port_usage = port_usage
        # The number of websites that are protected by the instance.
        self.site_usage = site_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_count_usage is not None:
            result['DefenseCountUsage'] = self.defense_count_usage

        if self.domain_usage is not None:
            result['DomainUsage'] = self.domain_usage

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.port_usage is not None:
            result['PortUsage'] = self.port_usage

        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseCountUsage') is not None:
            self.defense_count_usage = m.get('DefenseCountUsage')

        if m.get('DomainUsage') is not None:
            self.domain_usage = m.get('DomainUsage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PortUsage') is not None:
            self.port_usage = m.get('PortUsage')

        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')

        return self


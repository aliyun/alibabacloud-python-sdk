# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceSpecsResponseBody(DaraModel):
    def __init__(
        self,
        instance_specs: List[main_models.DescribeInstanceSpecsResponseBodyInstanceSpecs] = None,
        request_id: str = None,
    ):
        self.instance_specs = instance_specs
        self.request_id = request_id

    def validate(self):
        if self.instance_specs:
            for v1 in self.instance_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k1 in self.instance_specs:
                result['InstanceSpecs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_specs = []
        if m.get('InstanceSpecs') is not None:
            for k1 in m.get('InstanceSpecs'):
                temp_model = main_models.DescribeInstanceSpecsResponseBodyInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceSpecsResponseBodyInstanceSpecs(DaraModel):
    def __init__(
        self,
        bandwidth_mbps: int = None,
        base_bandwidth: int = None,
        defense_count: int = None,
        domain_limit: int = None,
        elastic_bandwidth: int = None,
        function_version: str = None,
        instance_id: str = None,
        port_limit: int = None,
        qps_limit: int = None,
        site_limit: int = None,
    ):
        self.bandwidth_mbps = bandwidth_mbps
        self.base_bandwidth = base_bandwidth
        self.defense_count = defense_count
        self.domain_limit = domain_limit
        self.elastic_bandwidth = elastic_bandwidth
        self.function_version = function_version
        self.instance_id = instance_id
        self.port_limit = port_limit
        self.qps_limit = qps_limit
        self.site_limit = site_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_mbps is not None:
            result['BandwidthMbps'] = self.bandwidth_mbps

        if self.base_bandwidth is not None:
            result['BaseBandwidth'] = self.base_bandwidth

        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count

        if self.domain_limit is not None:
            result['DomainLimit'] = self.domain_limit

        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth

        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.port_limit is not None:
            result['PortLimit'] = self.port_limit

        if self.qps_limit is not None:
            result['QpsLimit'] = self.qps_limit

        if self.site_limit is not None:
            result['SiteLimit'] = self.site_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthMbps') is not None:
            self.bandwidth_mbps = m.get('BandwidthMbps')

        if m.get('BaseBandwidth') is not None:
            self.base_bandwidth = m.get('BaseBandwidth')

        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')

        if m.get('DomainLimit') is not None:
            self.domain_limit = m.get('DomainLimit')

        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')

        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PortLimit') is not None:
            self.port_limit = m.get('PortLimit')

        if m.get('QpsLimit') is not None:
            self.qps_limit = m.get('QpsLimit')

        if m.get('SiteLimit') is not None:
            self.site_limit = m.get('SiteLimit')

        return self


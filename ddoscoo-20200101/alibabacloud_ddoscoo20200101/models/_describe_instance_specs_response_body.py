# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceSpecsResponseBody(DaraModel):
    def __init__(
        self,
        instance_specs: List[main_models.DescribeInstanceSpecsResponseBodyInstanceSpecs] = None,
        request_id: str = None,
    ):
        # The details of the specifications of the instance.
        self.instance_specs = instance_specs
        # The ID of the request, which is used to locate and troubleshoot issues.
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
        conn_limit: int = None,
        cps_limit: int = None,
        defense_count: int = None,
        domain_limit: int = None,
        elastic_bandwidth: int = None,
        elastic_bw: int = None,
        elastic_bw_model: str = None,
        elastic_qps: int = None,
        elastic_qps_mode: str = None,
        function_version: str = None,
        instance_id: str = None,
        port_limit: int = None,
        qps_limit: int = None,
        real_limit_bw: int = None,
        site_limit: int = None,
    ):
        # The clean bandwidth. Unit: Mbit/s.
        self.bandwidth_mbps = bandwidth_mbps
        # The basic protection bandwidth. Unit: Gbit/s.
        self.base_bandwidth = base_bandwidth
        # The specification of concurrent connections of the instance.
        self.conn_limit = conn_limit
        # The specification of new connections of the instance.
        self.cps_limit = cps_limit
        # The number of available advanced mitigation sessions for this month. **-1**: unlimited
        # 
        # >  This parameter is returned only when the request parameter **RegionId** is set to **ap-southeast-1**. If RegionId is set to ap-southeast-1, the specifications of Anti-DDoS Proxy (Outside Chinese Mainland) instances are queried.
        self.defense_count = defense_count
        # The number of domain names that can be protected by the instance.
        self.domain_limit = domain_limit
        # The burstable protection bandwidth. Unit: Gbit/s.
        self.elastic_bandwidth = elastic_bandwidth
        # The burstable clean bandwidth. Unit: Mbit/s.
        self.elastic_bw = elastic_bw
        # The metering method of the burstable clean bandwidth. Valid values:
        # 
        # *   **day**: the metering method of daily 95th percentile
        # *   **month**: the metering method of monthly 95th percentile
        self.elastic_bw_model = elastic_bw_model
        # The burstable QPS. Unit: QPS
        self.elastic_qps = elastic_qps
        # The metering method of the burstable QPS. Valid values:
        # 
        # *   **day**: the metering method of daily 95th percentile
        # *   **month**: the metering method of monthly 95th percentile
        self.elastic_qps_mode = elastic_qps_mode
        # The function plan of the instance. Valid values:
        # 
        # *   **default**: Standard
        # *   **enhance**: Enhanced
        # *   **cnhk**: Chinese Mainland Acceleration (CMA)
        # *   **cnhk_default**: Secure Chinese Mainland Acceleration (Sec-CMA) standard
        # *   **cnhk_enhance**: Sec-CMA enhanced
        self.function_version = function_version
        # The ID of the instance.
        self.instance_id = instance_id
        # The number of ports that can be protected by the instance.
        self.port_limit = port_limit
        # The clean QPS.
        self.qps_limit = qps_limit
        # The threshold of the clean bandwidth. Valid values: 0 to 15360. The value 0 indicates that rate limiting is never triggered. Unit: Mbit/s
        self.real_limit_bw = real_limit_bw
        # The number of sites that can be protected by the instance.
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

        if self.conn_limit is not None:
            result['ConnLimit'] = self.conn_limit

        if self.cps_limit is not None:
            result['CpsLimit'] = self.cps_limit

        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count

        if self.domain_limit is not None:
            result['DomainLimit'] = self.domain_limit

        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth

        if self.elastic_bw is not None:
            result['ElasticBw'] = self.elastic_bw

        if self.elastic_bw_model is not None:
            result['ElasticBwModel'] = self.elastic_bw_model

        if self.elastic_qps is not None:
            result['ElasticQps'] = self.elastic_qps

        if self.elastic_qps_mode is not None:
            result['ElasticQpsMode'] = self.elastic_qps_mode

        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.port_limit is not None:
            result['PortLimit'] = self.port_limit

        if self.qps_limit is not None:
            result['QpsLimit'] = self.qps_limit

        if self.real_limit_bw is not None:
            result['RealLimitBw'] = self.real_limit_bw

        if self.site_limit is not None:
            result['SiteLimit'] = self.site_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthMbps') is not None:
            self.bandwidth_mbps = m.get('BandwidthMbps')

        if m.get('BaseBandwidth') is not None:
            self.base_bandwidth = m.get('BaseBandwidth')

        if m.get('ConnLimit') is not None:
            self.conn_limit = m.get('ConnLimit')

        if m.get('CpsLimit') is not None:
            self.cps_limit = m.get('CpsLimit')

        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')

        if m.get('DomainLimit') is not None:
            self.domain_limit = m.get('DomainLimit')

        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')

        if m.get('ElasticBw') is not None:
            self.elastic_bw = m.get('ElasticBw')

        if m.get('ElasticBwModel') is not None:
            self.elastic_bw_model = m.get('ElasticBwModel')

        if m.get('ElasticQps') is not None:
            self.elastic_qps = m.get('ElasticQps')

        if m.get('ElasticQpsMode') is not None:
            self.elastic_qps_mode = m.get('ElasticQpsMode')

        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PortLimit') is not None:
            self.port_limit = m.get('PortLimit')

        if m.get('QpsLimit') is not None:
            self.qps_limit = m.get('QpsLimit')

        if m.get('RealLimitBw') is not None:
            self.real_limit_bw = m.get('RealLimitBw')

        if m.get('SiteLimit') is not None:
            self.site_limit = m.get('SiteLimit')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceExtResponseBody(DaraModel):
    def __init__(
        self,
        instance_ext_specs: List[main_models.DescribeInstanceExtResponseBodyInstanceExtSpecs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The extended information about the Anti-DDoS Proxy instance.
        self.instance_ext_specs = instance_ext_specs
        # The request ID.
        self.request_id = request_id
        # The total number of queried instances.
        self.total_count = total_count

    def validate(self):
        if self.instance_ext_specs:
            for v1 in self.instance_ext_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceExtSpecs'] = []
        if self.instance_ext_specs is not None:
            for k1 in self.instance_ext_specs:
                result['InstanceExtSpecs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_ext_specs = []
        if m.get('InstanceExtSpecs') is not None:
            for k1 in m.get('InstanceExtSpecs'):
                temp_model = main_models.DescribeInstanceExtResponseBodyInstanceExtSpecs()
                self.instance_ext_specs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceExtResponseBodyInstanceExtSpecs(DaraModel):
    def __init__(
        self,
        function_version: int = None,
        instance_id: str = None,
        normal_bandwidth: int = None,
        product_plan: int = None,
        service_partner: str = None,
    ):
        # The function plan. Valid values:
        # 
        # *   **0**: Standard
        # *   **1**: Enhanced
        self.function_version = function_version
        # The ID of the instance.
        self.instance_id = instance_id
        # The clean bandwidth. Unit: Mbit/s.
        self.normal_bandwidth = normal_bandwidth
        # The type of the instance. Valid values:
        # 
        # *   **0**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the Insurance mitigation plan
        # *   **1**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the Unlimited mitigation plan
        # *   **2**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the Chinese Mainland Acceleration (CMA) mitigation plan
        # *   **3**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the Secure Chinese Mainland Acceleration (Sec-CMA) mitigation plan
        # *   **9**: Anti-DDoS Proxy (Chinese Mainland) instance of the Profession mitigation plan
        self.product_plan = product_plan
        # The Internet service provider (ISP) line of the Anti-DDoS Proxy (Chinese Mainland) instance.
        self.service_partner = service_partner

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.normal_bandwidth is not None:
            result['NormalBandwidth'] = self.normal_bandwidth

        if self.product_plan is not None:
            result['ProductPlan'] = self.product_plan

        if self.service_partner is not None:
            result['ServicePartner'] = self.service_partner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NormalBandwidth') is not None:
            self.normal_bandwidth = m.get('NormalBandwidth')

        if m.get('ProductPlan') is not None:
            self.product_plan = m.get('ProductPlan')

        if m.get('ServicePartner') is not None:
            self.service_partner = m.get('ServicePartner')

        return self


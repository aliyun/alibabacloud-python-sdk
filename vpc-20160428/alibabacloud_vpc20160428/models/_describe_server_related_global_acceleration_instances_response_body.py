# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeServerRelatedGlobalAccelerationInstancesResponseBody(DaraModel):
    def __init__(
        self,
        global_acceleration_instances: main_models.DescribeServerRelatedGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstances = None,
        request_id: str = None,
    ):
        # The list of GA instances.
        self.global_acceleration_instances = global_acceleration_instances
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.global_acceleration_instances:
            self.global_acceleration_instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_acceleration_instances is not None:
            result['GlobalAccelerationInstances'] = self.global_acceleration_instances.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalAccelerationInstances') is not None:
            temp_model = main_models.DescribeServerRelatedGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstances()
            self.global_acceleration_instances = temp_model.from_map(m.get('GlobalAccelerationInstances'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeServerRelatedGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstances(DaraModel):
    def __init__(
        self,
        global_acceleration_instance: List[main_models.DescribeServerRelatedGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstance] = None,
    ):
        self.global_acceleration_instance = global_acceleration_instance

    def validate(self):
        if self.global_acceleration_instance:
            for v1 in self.global_acceleration_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GlobalAccelerationInstance'] = []
        if self.global_acceleration_instance is not None:
            for k1 in self.global_acceleration_instance:
                result['GlobalAccelerationInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.global_acceleration_instance = []
        if m.get('GlobalAccelerationInstance') is not None:
            for k1 in m.get('GlobalAccelerationInstance'):
                temp_model = main_models.DescribeServerRelatedGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstance()
                self.global_acceleration_instance.append(temp_model.from_map(k1))

        return self

class DescribeServerRelatedGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstance(DaraModel):
    def __init__(
        self,
        global_acceleration_instance_id: str = None,
        ip_address: str = None,
        region_id: str = None,
        server_ip_address: str = None,
    ):
        # The ID of the GA instance.
        self.global_acceleration_instance_id = global_acceleration_instance_id
        # The public IP address of the GA instance.
        self.ip_address = ip_address
        # The region ID of the GA instance.
        self.region_id = region_id
        # The IP address of the backend service.
        self.server_ip_address = server_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_acceleration_instance_id is not None:
            result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.server_ip_address is not None:
            result['ServerIpAddress'] = self.server_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalAccelerationInstanceId') is not None:
            self.global_acceleration_instance_id = m.get('GlobalAccelerationInstanceId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServerIpAddress') is not None:
            self.server_ip_address = m.get('ServerIpAddress')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adbai20250812 import models as main_models
from darabonba.model import DaraModel

class DescribeEapDeviceResourceAllocationResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeEapDeviceResourceAllocationResponseBodyItems] = None,
        request_id: str = None,
    ):
        # List of specification recommendations.
        self.items = items
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeEapDeviceResourceAllocationResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEapDeviceResourceAllocationResponseBodyItems(DaraModel):
    def __init__(
        self,
        device_count: int = None,
        head_acu: float = None,
        head_cpu: int = None,
        head_spec_name: str = None,
        total_acu: float = None,
        total_deployed_cpu: int = None,
        total_target_cpu: int = None,
        webserver_acu: float = None,
        webserver_cpu: int = None,
        webserver_spec_name: str = None,
        worker_acu: float = None,
        worker_count: int = None,
        worker_cpu: int = None,
        worker_spec_name: str = None,
    ):
        # Total number of devices
        self.device_count = device_count
        # Total ACU count for the Ray Cluster Head of the Embodied Intelligence platform
        self.head_acu = head_acu
        # Number of vCPU cores for the Ray Cluster Head node on the Intelligent Embodiment platform
        self.head_cpu = head_cpu
        # Ray Cluster Head specification of the Embodied Intelligence platform
        self.head_spec_name = head_spec_name
        # Total number of ACUs actually deployed on the Intelligent Embodiment platform
        self.total_acu = total_acu
        # Total number of vCPU cores actually deployed on the Intelligent Embodiment platform
        self.total_deployed_cpu = total_deployed_cpu
        # Total target number of vCPU cores
        self.total_target_cpu = total_target_cpu
        # Total ACU count for the Embodied Intelligence platform
        self.webserver_acu = webserver_acu
        # Total number of vCPU cores for the Embodied Intelligence platform
        self.webserver_cpu = webserver_cpu
        # Webserver specification of the Embodied Intelligence platform.
        self.webserver_spec_name = webserver_spec_name
        # Total ACU count per Ray Cluster Worker of the Embodied Intelligence platform
        self.worker_acu = worker_acu
        # Total number of Ray Cluster Worker nodes on the Intelligent Embodiment platform
        self.worker_count = worker_count
        # Number of vCPU cores per Ray Cluster Worker of the Embodied Intelligence platform
        self.worker_cpu = worker_cpu
        # Ray Cluster Worker specification of the Embodied Intelligence platform
        self.worker_spec_name = worker_spec_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count

        if self.head_acu is not None:
            result['HeadAcu'] = self.head_acu

        if self.head_cpu is not None:
            result['HeadCpu'] = self.head_cpu

        if self.head_spec_name is not None:
            result['HeadSpecName'] = self.head_spec_name

        if self.total_acu is not None:
            result['TotalAcu'] = self.total_acu

        if self.total_deployed_cpu is not None:
            result['TotalDeployedCpu'] = self.total_deployed_cpu

        if self.total_target_cpu is not None:
            result['TotalTargetCpu'] = self.total_target_cpu

        if self.webserver_acu is not None:
            result['WebserverAcu'] = self.webserver_acu

        if self.webserver_cpu is not None:
            result['WebserverCpu'] = self.webserver_cpu

        if self.webserver_spec_name is not None:
            result['WebserverSpecName'] = self.webserver_spec_name

        if self.worker_acu is not None:
            result['WorkerAcu'] = self.worker_acu

        if self.worker_count is not None:
            result['WorkerCount'] = self.worker_count

        if self.worker_cpu is not None:
            result['WorkerCpu'] = self.worker_cpu

        if self.worker_spec_name is not None:
            result['WorkerSpecName'] = self.worker_spec_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')

        if m.get('HeadAcu') is not None:
            self.head_acu = m.get('HeadAcu')

        if m.get('HeadCpu') is not None:
            self.head_cpu = m.get('HeadCpu')

        if m.get('HeadSpecName') is not None:
            self.head_spec_name = m.get('HeadSpecName')

        if m.get('TotalAcu') is not None:
            self.total_acu = m.get('TotalAcu')

        if m.get('TotalDeployedCpu') is not None:
            self.total_deployed_cpu = m.get('TotalDeployedCpu')

        if m.get('TotalTargetCpu') is not None:
            self.total_target_cpu = m.get('TotalTargetCpu')

        if m.get('WebserverAcu') is not None:
            self.webserver_acu = m.get('WebserverAcu')

        if m.get('WebserverCpu') is not None:
            self.webserver_cpu = m.get('WebserverCpu')

        if m.get('WebserverSpecName') is not None:
            self.webserver_spec_name = m.get('WebserverSpecName')

        if m.get('WorkerAcu') is not None:
            self.worker_acu = m.get('WorkerAcu')

        if m.get('WorkerCount') is not None:
            self.worker_count = m.get('WorkerCount')

        if m.get('WorkerCpu') is not None:
            self.worker_cpu = m.get('WorkerCpu')

        if m.get('WorkerSpecName') is not None:
            self.worker_spec_name = m.get('WorkerSpecName')

        return self


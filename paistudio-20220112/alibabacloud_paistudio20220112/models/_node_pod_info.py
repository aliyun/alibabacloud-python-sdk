# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class NodePodInfo(DaraModel):
    def __init__(
        self,
        gpuindexes: List[int] = None,
        phase: str = None,
        pod_ip: str = None,
        pod_name: str = None,
        pod_namespace: str = None,
        resource_spec: main_models.ResourceAmount = None,
        workload_id: str = None,
        workload_type: str = None,
    ):
        # The occupied GPU indexes.
        self.gpuindexes = gpuindexes
        # The Pod status.
        self.phase = phase
        # The IP address of the Pod.
        self.pod_ip = pod_ip
        # The Pod name.
        self.pod_name = pod_name
        # The namespace of the Pod.
        self.pod_namespace = pod_namespace
        # The resource usage information.
        self.resource_spec = resource_spec
        # The task ID or service ID.
        self.workload_id = workload_id
        # The sub-product that the Pod belongs to.
        self.workload_type = workload_type

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gpuindexes is not None:
            result['GPUIndexes'] = self.gpuindexes

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.pod_ip is not None:
            result['PodIP'] = self.pod_ip

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        if self.pod_namespace is not None:
            result['PodNamespace'] = self.pod_namespace

        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()

        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id

        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GPUIndexes') is not None:
            self.gpuindexes = m.get('GPUIndexes')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('PodIP') is not None:
            self.pod_ip = m.get('PodIP')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        if m.get('PodNamespace') is not None:
            self.pod_namespace = m.get('PodNamespace')

        if m.get('ResourceSpec') is not None:
            temp_model = main_models.ResourceAmount()
            self.resource_spec = temp_model.from_map(m.get('ResourceSpec'))

        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        return self


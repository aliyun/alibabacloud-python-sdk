# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeServcieScheduleResponseBody(DaraModel):
    def __init__(
        self,
        index: int = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_port: int = None,
        pod_abstract_info: main_models.DescribeServcieScheduleResponseBodyPodAbstractInfo = None,
        request_id: str = None,
        request_repeated: bool = None,
        tcp_ports: str = None,
    ):
        # The index number of the scheduled virtual device (pod).
        self.index = index
        # The ID of the scheduled instance.
        self.instance_id = instance_id
        # The ID of the scheduled instance.
        self.instance_ip = instance_ip
        # The start port of the scheduled instance.
        self.instance_port = instance_port
        # The summary information about the scheduled virtual device.
        self.pod_abstract_info = pod_abstract_info
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is repeated.
        self.request_repeated = request_repeated
        # The TCP port range of the scheduled instance or container. The value is in the ${from}-$-{to} format. Example: 80-88.
        self.tcp_ports = tcp_ports

    def validate(self):
        if self.pod_abstract_info:
            self.pod_abstract_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip

        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port

        if self.pod_abstract_info is not None:
            result['PodAbstractInfo'] = self.pod_abstract_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_repeated is not None:
            result['RequestRepeated'] = self.request_repeated

        if self.tcp_ports is not None:
            result['TcpPorts'] = self.tcp_ports

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')

        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')

        if m.get('PodAbstractInfo') is not None:
            temp_model = main_models.DescribeServcieScheduleResponseBodyPodAbstractInfo()
            self.pod_abstract_info = temp_model.from_map(m.get('PodAbstractInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestRepeated') is not None:
            self.request_repeated = m.get('RequestRepeated')

        if m.get('TcpPorts') is not None:
            self.tcp_ports = m.get('TcpPorts')

        return self

class DescribeServcieScheduleResponseBodyPodAbstractInfo(DaraModel):
    def __init__(
        self,
        container_service: bool = None,
        container_statuses: main_models.DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatuses = None,
        name: bool = None,
        namespace: bool = None,
        resource_scope: bool = None,
        status: bool = None,
    ):
        # The name of the container service.
        self.container_service = container_service
        # The information about the container.
        self.container_statuses = container_statuses
        # The name of the pod.
        self.name = name
        # The name of the namespace.
        self.namespace = namespace
        # The pod scope.
        self.resource_scope = resource_scope
        # The status of the pod.
        self.status = status

    def validate(self):
        if self.container_statuses:
            self.container_statuses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_service is not None:
            result['ContainerService'] = self.container_service

        if self.container_statuses is not None:
            result['ContainerStatuses'] = self.container_statuses.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.resource_scope is not None:
            result['ResourceScope'] = self.resource_scope

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerService') is not None:
            self.container_service = m.get('ContainerService')

        if m.get('ContainerStatuses') is not None:
            temp_model = main_models.DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatuses()
            self.container_statuses = temp_model.from_map(m.get('ContainerStatuses'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ResourceScope') is not None:
            self.resource_scope = m.get('ResourceScope')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatuses(DaraModel):
    def __init__(
        self,
        container_status: List[main_models.DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatusesContainerStatus] = None,
    ):
        self.container_status = container_status

    def validate(self):
        if self.container_status:
            for v1 in self.container_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContainerStatus'] = []
        if self.container_status is not None:
            for k1 in self.container_status:
                result['ContainerStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_status = []
        if m.get('ContainerStatus') is not None:
            for k1 in m.get('ContainerStatus'):
                temp_model = main_models.DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatusesContainerStatus()
                self.container_status.append(temp_model.from_map(k1))

        return self

class DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatusesContainerStatus(DaraModel):
    def __init__(
        self,
        container_id: str = None,
        name: str = None,
    ):
        # The ID of the container.
        self.container_id = container_id
        # The name of the container.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self


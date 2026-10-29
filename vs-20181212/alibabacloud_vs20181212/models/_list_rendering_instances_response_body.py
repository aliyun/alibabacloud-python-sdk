# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListRenderingInstancesResponseBody(DaraModel):
    def __init__(
        self,
        rendering_instances: List[main_models.ListRenderingInstancesResponseBodyRenderingInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of cloud application service instances.
        self.rendering_instances = rendering_instances
        # The ID of the request.
        self.request_id = request_id
        # The total number of cloud application service instances.
        self.total_count = total_count

    def validate(self):
        if self.rendering_instances:
            for v1 in self.rendering_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RenderingInstances'] = []
        if self.rendering_instances is not None:
            for k1 in self.rendering_instances:
                result['RenderingInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rendering_instances = []
        if m.get('RenderingInstances') is not None:
            for k1 in m.get('RenderingInstances'):
                temp_model = main_models.ListRenderingInstancesResponseBodyRenderingInstances()
                self.rendering_instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRenderingInstancesResponseBodyRenderingInstances(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        creation_time: str = None,
        expire_time: str = None,
        instance_name: str = None,
        max_egress_bandwidth: str = None,
        max_ingress_bandwidth: str = None,
        rendering_instance_id: str = None,
        rendering_spec: str = None,
        server_status: str = None,
        status: str = None,
        storage_size: int = None,
    ):
        # The billing method.
        self.charge_type = charge_type
        # The time when the cloud application service instance was created. The time is in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.creation_time = creation_time
        # The expiration time.
        self.expire_time = expire_time
        # The name of the instance.
        self.instance_name = instance_name
        # The maximum outbound bandwidth limit. Unit: Mbit/s. A value of 0 indicates that no bandwidth limit is configured.
        self.max_egress_bandwidth = max_egress_bandwidth
        # The maximum inbound bandwidth limit. Unit: Mbit/s. A value of 0 indicates that no bandwidth limit is configured.
        self.max_ingress_bandwidth = max_ingress_bandwidth
        # The instance ID of the cloud application service.
        self.rendering_instance_id = rendering_instance_id
        # The instance type of the cloud application service instance.
        self.rendering_spec = rendering_spec
        # The status of the service host.
        self.server_status = server_status
        # The instance status.
        self.status = status
        # The cloud storage capacity. Unit: GB.
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.max_egress_bandwidth is not None:
            result['MaxEgressBandwidth'] = self.max_egress_bandwidth

        if self.max_ingress_bandwidth is not None:
            result['MaxIngressBandwidth'] = self.max_ingress_bandwidth

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.rendering_spec is not None:
            result['RenderingSpec'] = self.rendering_spec

        if self.server_status is not None:
            result['ServerStatus'] = self.server_status

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaxEgressBandwidth') is not None:
            self.max_egress_bandwidth = m.get('MaxEgressBandwidth')

        if m.get('MaxIngressBandwidth') is not None:
            self.max_ingress_bandwidth = m.get('MaxIngressBandwidth')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('RenderingSpec') is not None:
            self.rendering_spec = m.get('RenderingSpec')

        if m.get('ServerStatus') is not None:
            self.server_status = m.get('ServerStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self


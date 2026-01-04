# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information of instances.
        self.instances = instances
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        default_endpoint: main_models.ListInstancesResponseBodyInstancesDefaultEndpoint = None,
        description: str = None,
        instance_id: str = None,
        managed_service_code: str = None,
        service_managed: bool = None,
        status: str = None,
    ):
        # The time when the instance was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The default endpoint of the instance.
        self.default_endpoint = default_endpoint
        # The description of the instance.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        self.managed_service_code = managed_service_code
        self.service_managed = service_managed
        # The status of the instance. Valid values:
        # 
        # *   creating
        # *   running
        self.status = status

    def validate(self):
        if self.default_endpoint:
            self.default_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.managed_service_code is not None:
            result['ManagedServiceCode'] = self.managed_service_code

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultEndpoint') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesDefaultEndpoint()
            self.default_endpoint = temp_model.from_map(m.get('DefaultEndpoint'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ManagedServiceCode') is not None:
            self.managed_service_code = m.get('ManagedServiceCode')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstancesResponseBodyInstancesDefaultEndpoint(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        status: str = None,
    ):
        # The endpoint of the instance.
        self.endpoint = endpoint
        # The status of the endpoint. Valid values:
        # 
        # *   resolved
        # *   unresolved
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


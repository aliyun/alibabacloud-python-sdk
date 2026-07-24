# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafkastreaming20260202 import models as main_models
from darabonba.model import DaraModel

class ListComputeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListComputeInstancesResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListComputeInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListComputeInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        cu: int = None,
        instance_id: str = None,
        instance_name: str = None,
        service_status: str = None,
        total_jobs: int = None,
        total_running_jobs: int = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.cu = cu
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.service_status = service_status
        self.total_jobs = total_jobs
        self.total_running_jobs = total_running_jobs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.total_jobs is not None:
            result['TotalJobs'] = self.total_jobs

        if self.total_running_jobs is not None:
            result['TotalRunningJobs'] = self.total_running_jobs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('TotalJobs') is not None:
            self.total_jobs = m.get('TotalJobs')

        if m.get('TotalRunningJobs') is not None:
            self.total_running_jobs = m.get('TotalRunningJobs')

        return self


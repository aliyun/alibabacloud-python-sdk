# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListDoctorJobsStatsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDoctorJobsStatsResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The summary of job information.
        self.data = data
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDoctorJobsStatsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDoctorJobsStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        apps_count: main_models.ListDoctorJobsStatsResponseBodyDataAppsCount = None,
        mem_seconds: main_models.ListDoctorJobsStatsResponseBodyDataMemSeconds = None,
        queue: str = None,
        type: str = None,
        user: str = None,
        vcore_seconds: main_models.ListDoctorJobsStatsResponseBodyDataVcoreSeconds = None,
    ):
        # The total number of jobs.
        self.apps_count = apps_count
        # The aggregated amount of memory that is allocated to the job multiplied by the number of seconds the job has been running.
        self.mem_seconds = mem_seconds
        # The YARN queue to which the job was submitted.
        self.queue = queue
        # The type of the compute engine.
        self.type = type
        # The username that is used to submit the job.
        self.user = user
        # The aggregated number of vCPUs that are allocated to the job multiplied by the number of seconds the job has been running.
        self.vcore_seconds = vcore_seconds

    def validate(self):
        if self.apps_count:
            self.apps_count.validate()
        if self.mem_seconds:
            self.mem_seconds.validate()
        if self.vcore_seconds:
            self.vcore_seconds.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apps_count is not None:
            result['AppsCount'] = self.apps_count.to_map()

        if self.mem_seconds is not None:
            result['MemSeconds'] = self.mem_seconds.to_map()

        if self.queue is not None:
            result['Queue'] = self.queue

        if self.type is not None:
            result['Type'] = self.type

        if self.user is not None:
            result['User'] = self.user

        if self.vcore_seconds is not None:
            result['VcoreSeconds'] = self.vcore_seconds.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppsCount') is not None:
            temp_model = main_models.ListDoctorJobsStatsResponseBodyDataAppsCount()
            self.apps_count = temp_model.from_map(m.get('AppsCount'))

        if m.get('MemSeconds') is not None:
            temp_model = main_models.ListDoctorJobsStatsResponseBodyDataMemSeconds()
            self.mem_seconds = temp_model.from_map(m.get('MemSeconds'))

        if m.get('Queue') is not None:
            self.queue = m.get('Queue')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('VcoreSeconds') is not None:
            temp_model = main_models.ListDoctorJobsStatsResponseBodyDataVcoreSeconds()
            self.vcore_seconds = temp_model.from_map(m.get('VcoreSeconds'))

        return self

class ListDoctorJobsStatsResponseBodyDataVcoreSeconds(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorJobsStatsResponseBodyDataMemSeconds(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorJobsStatsResponseBodyDataAppsCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


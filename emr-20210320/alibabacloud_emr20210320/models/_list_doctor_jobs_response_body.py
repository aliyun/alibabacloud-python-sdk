# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListDoctorJobsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDoctorJobsResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the jobs.
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
                temp_model = main_models.ListDoctorJobsResponseBodyData()
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

class ListDoctorJobsResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        elapsed_time: int = None,
        final_status: str = None,
        finish_time: int = None,
        launch_time: int = None,
        metrics: main_models.ListDoctorJobsResponseBodyDataMetrics = None,
        queue: str = None,
        start_time: int = None,
        state: str = None,
        type: str = None,
        user: str = None,
    ):
        # The ID of the job that was submitted to YARN.
        self.app_id = app_id
        # The name of the job.
        self.app_name = app_name
        # The total running time of the job. Unit: milliseconds.
        self.elapsed_time = elapsed_time
        # The final state of the job. Valid values:
        # 
        # *   SUCCEEDED
        # *   FAILED
        # *   KILLED
        # *   ENDED
        # *   UNDEFINED
        self.final_status = final_status
        # The end time of the job. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Unit: milliseconds.
        self.finish_time = finish_time
        # The time when the job was started. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Unit: milliseconds.
        self.launch_time = launch_time
        # The data about the metrics.
        self.metrics = metrics
        # The YARN queue to which the job was submitted.
        self.queue = queue
        # The time when the job was submitted. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Unit: milliseconds.
        self.start_time = start_time
        # The running state of the job. Valid values:
        # 
        # *   FINISHED
        # *   FAILED
        # *   KILLED
        self.state = state
        # The type of the compute engine.
        self.type = type
        # The username that was used to submit the job.
        self.user = user

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time

        if self.final_status is not None:
            result['FinalStatus'] = self.final_status

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time

        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        if self.queue is not None:
            result['Queue'] = self.queue

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.type is not None:
            result['Type'] = self.type

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')

        if m.get('FinalStatus') is not None:
            self.final_status = m.get('FinalStatus')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')

        if m.get('Metrics') is not None:
            temp_model = main_models.ListDoctorJobsResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        if m.get('Queue') is not None:
            self.queue = m.get('Queue')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

class ListDoctorJobsResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        mem_seconds: main_models.ListDoctorJobsResponseBodyDataMetricsMemSeconds = None,
        vcore_seconds: main_models.ListDoctorJobsResponseBodyDataMetricsVcoreSeconds = None,
    ):
        # The amount of memory consumed.
        self.mem_seconds = mem_seconds
        # The CPU usage.
        self.vcore_seconds = vcore_seconds

    def validate(self):
        if self.mem_seconds:
            self.mem_seconds.validate()
        if self.vcore_seconds:
            self.vcore_seconds.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mem_seconds is not None:
            result['MemSeconds'] = self.mem_seconds.to_map()

        if self.vcore_seconds is not None:
            result['VcoreSeconds'] = self.vcore_seconds.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemSeconds') is not None:
            temp_model = main_models.ListDoctorJobsResponseBodyDataMetricsMemSeconds()
            self.mem_seconds = temp_model.from_map(m.get('MemSeconds'))

        if m.get('VcoreSeconds') is not None:
            temp_model = main_models.ListDoctorJobsResponseBodyDataMetricsVcoreSeconds()
            self.vcore_seconds = temp_model.from_map(m.get('VcoreSeconds'))

        return self

class ListDoctorJobsResponseBodyDataMetricsVcoreSeconds(DaraModel):
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

class ListDoctorJobsResponseBodyDataMetricsMemSeconds(DaraModel):
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


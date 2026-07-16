# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListDoctorApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDoctorApplicationsResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of jobs.
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
                temp_model = main_models.ListDoctorApplicationsResponseBodyData()
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

class ListDoctorApplicationsResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis: main_models.ListDoctorApplicationsResponseBodyDataAnalysis = None,
        app_id: str = None,
        app_name: str = None,
        end_time: int = None,
        ids: List[str] = None,
        metrics: main_models.ListDoctorApplicationsResponseBodyDataMetrics = None,
        query_sql: str = None,
        queue: str = None,
        start_time: int = None,
        type: str = None,
        user: str = None,
    ):
        # The analysis results of the jobs.
        self.analysis = analysis
        # The job ID in YARN. The value of QueryID or SessionID is returned for a Hive job.
        self.app_id = app_id
        # The name of the job.
        self.app_name = app_name
        # The time when the job ended. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Unit: milliseconds.
        self.end_time = end_time
        # The job IDs. Multiple job IDs are separated with commas (,).
        self.ids = ids
        # The data about metrics.
        self.metrics = metrics
        # The query statement. This parameter is left empty for non-SQL jobs.
        self.query_sql = query_sql
        # The YARN queue to which the job was submitted.
        self.queue = queue
        # The time when the job was submitted. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Unit: milliseconds.
        self.start_time = start_time
        # The type of the compute engine.
        self.type = type
        # The username that was used to submit the job.
        self.user = user

    def validate(self):
        if self.analysis:
            self.analysis.validate()
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis is not None:
            result['Analysis'] = self.analysis.to_map()

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        if self.query_sql is not None:
            result['QuerySql'] = self.query_sql

        if self.queue is not None:
            result['Queue'] = self.queue

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Analysis') is not None:
            temp_model = main_models.ListDoctorApplicationsResponseBodyDataAnalysis()
            self.analysis = temp_model.from_map(m.get('Analysis'))

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Metrics') is not None:
            temp_model = main_models.ListDoctorApplicationsResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        if m.get('QuerySql') is not None:
            self.query_sql = m.get('QuerySql')

        if m.get('Queue') is not None:
            self.queue = m.get('Queue')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

class ListDoctorApplicationsResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        mem_seconds: main_models.ListDoctorApplicationsResponseBodyDataMetricsMemSeconds = None,
        mem_utilization: main_models.ListDoctorApplicationsResponseBodyDataMetricsMemUtilization = None,
        vcore_seconds: main_models.ListDoctorApplicationsResponseBodyDataMetricsVcoreSeconds = None,
        vcore_utilization: main_models.ListDoctorApplicationsResponseBodyDataMetricsVcoreUtilization = None,
    ):
        # The amount of memory consumed.
        self.mem_seconds = mem_seconds
        # The memory usage
        self.mem_utilization = mem_utilization
        # The CPU usage.
        self.vcore_seconds = vcore_seconds
        # The CPU utilization. This parameter has the same meaning as %CPU in the Linux top command.
        self.vcore_utilization = vcore_utilization

    def validate(self):
        if self.mem_seconds:
            self.mem_seconds.validate()
        if self.mem_utilization:
            self.mem_utilization.validate()
        if self.vcore_seconds:
            self.vcore_seconds.validate()
        if self.vcore_utilization:
            self.vcore_utilization.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mem_seconds is not None:
            result['MemSeconds'] = self.mem_seconds.to_map()

        if self.mem_utilization is not None:
            result['MemUtilization'] = self.mem_utilization.to_map()

        if self.vcore_seconds is not None:
            result['VcoreSeconds'] = self.vcore_seconds.to_map()

        if self.vcore_utilization is not None:
            result['VcoreUtilization'] = self.vcore_utilization.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemSeconds') is not None:
            temp_model = main_models.ListDoctorApplicationsResponseBodyDataMetricsMemSeconds()
            self.mem_seconds = temp_model.from_map(m.get('MemSeconds'))

        if m.get('MemUtilization') is not None:
            temp_model = main_models.ListDoctorApplicationsResponseBodyDataMetricsMemUtilization()
            self.mem_utilization = temp_model.from_map(m.get('MemUtilization'))

        if m.get('VcoreSeconds') is not None:
            temp_model = main_models.ListDoctorApplicationsResponseBodyDataMetricsVcoreSeconds()
            self.vcore_seconds = temp_model.from_map(m.get('VcoreSeconds'))

        if m.get('VcoreUtilization') is not None:
            temp_model = main_models.ListDoctorApplicationsResponseBodyDataMetricsVcoreUtilization()
            self.vcore_utilization = temp_model.from_map(m.get('VcoreUtilization'))

        return self

class ListDoctorApplicationsResponseBodyDataMetricsVcoreUtilization(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
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

class ListDoctorApplicationsResponseBodyDataMetricsVcoreSeconds(DaraModel):
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

class ListDoctorApplicationsResponseBodyDataMetricsMemUtilization(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
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

class ListDoctorApplicationsResponseBodyDataMetricsMemSeconds(DaraModel):
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

class ListDoctorApplicationsResponseBodyDataAnalysis(DaraModel):
    def __init__(
        self,
        score: int = None,
        suggestion: str = None,
    ):
        # The score of the job.
        self.score = score
        # The suggestion on executing the job.
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.score is not None:
            result['Score'] = self.score

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self


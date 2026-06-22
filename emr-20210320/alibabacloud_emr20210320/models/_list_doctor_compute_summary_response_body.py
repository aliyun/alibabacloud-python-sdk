# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListDoctorComputeSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDoctorComputeSummaryResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of resource usage.
        self.data = data
        # The maximum number of entries that are returned.
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
                temp_model = main_models.ListDoctorComputeSummaryResponseBodyData()
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

class ListDoctorComputeSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis: main_models.ListDoctorComputeSummaryResponseBodyDataAnalysis = None,
        component_name: str = None,
        metrics: main_models.ListDoctorComputeSummaryResponseBodyDataMetrics = None,
    ):
        # The resource analysis results.
        self.analysis = analysis
        # The name of the resource whose details are obtained based on the value of ComponentTypes. For example, if the value of ComponentTypes is Queue, the value of this parameter is a queue, such as DW.
        self.component_name = component_name
        # The metric information.
        self.metrics = metrics

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

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Analysis') is not None:
            temp_model = main_models.ListDoctorComputeSummaryResponseBodyDataAnalysis()
            self.analysis = temp_model.from_map(m.get('Analysis'))

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('Metrics') is not None:
            temp_model = main_models.ListDoctorComputeSummaryResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        return self

class ListDoctorComputeSummaryResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        mem_seconds: main_models.ListDoctorComputeSummaryResponseBodyDataMetricsMemSeconds = None,
        mem_seconds_day_growth_ratio: main_models.ListDoctorComputeSummaryResponseBodyDataMetricsMemSecondsDayGrowthRatio = None,
        mem_utilization: main_models.ListDoctorComputeSummaryResponseBodyDataMetricsMemUtilization = None,
        read_size: main_models.ListDoctorComputeSummaryResponseBodyDataMetricsReadSize = None,
        vcore_seconds: main_models.ListDoctorComputeSummaryResponseBodyDataMetricsVcoreSeconds = None,
        vcore_seconds_day_growth_ratio: main_models.ListDoctorComputeSummaryResponseBodyDataMetricsVcoreSecondsDayGrowthRatio = None,
        vcore_utilization: main_models.ListDoctorComputeSummaryResponseBodyDataMetricsVcoreUtilization = None,
        write_size: main_models.ListDoctorComputeSummaryResponseBodyDataMetricsWriteSize = None,
    ):
        # The total memory consumption over time in seconds.
        self.mem_seconds = mem_seconds
        # The day-to-day growth rate of the total memory consumption over time in seconds.
        self.mem_seconds_day_growth_ratio = mem_seconds_day_growth_ratio
        # The average memory usage.
        self.mem_utilization = mem_utilization
        # The total amount of data read from the file system.
        self.read_size = read_size
        # The total CPU consumption over time in seconds.
        self.vcore_seconds = vcore_seconds
        # The day-to-day growth rate of the total CPU consumption over time in seconds.
        self.vcore_seconds_day_growth_ratio = vcore_seconds_day_growth_ratio
        # The average CPU utilization. The meaning is the same as the %CPU parameter in the output of the top command in Linux.
        self.vcore_utilization = vcore_utilization
        # The total amount of data written to the file system.
        self.write_size = write_size

    def validate(self):
        if self.mem_seconds:
            self.mem_seconds.validate()
        if self.mem_seconds_day_growth_ratio:
            self.mem_seconds_day_growth_ratio.validate()
        if self.mem_utilization:
            self.mem_utilization.validate()
        if self.read_size:
            self.read_size.validate()
        if self.vcore_seconds:
            self.vcore_seconds.validate()
        if self.vcore_seconds_day_growth_ratio:
            self.vcore_seconds_day_growth_ratio.validate()
        if self.vcore_utilization:
            self.vcore_utilization.validate()
        if self.write_size:
            self.write_size.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mem_seconds is not None:
            result['MemSeconds'] = self.mem_seconds.to_map()

        if self.mem_seconds_day_growth_ratio is not None:
            result['MemSecondsDayGrowthRatio'] = self.mem_seconds_day_growth_ratio.to_map()

        if self.mem_utilization is not None:
            result['MemUtilization'] = self.mem_utilization.to_map()

        if self.read_size is not None:
            result['ReadSize'] = self.read_size.to_map()

        if self.vcore_seconds is not None:
            result['VcoreSeconds'] = self.vcore_seconds.to_map()

        if self.vcore_seconds_day_growth_ratio is not None:
            result['VcoreSecondsDayGrowthRatio'] = self.vcore_seconds_day_growth_ratio.to_map()

        if self.vcore_utilization is not None:
            result['VcoreUtilization'] = self.vcore_utilization.to_map()

        if self.write_size is not None:
            result['WriteSize'] = self.write_size.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemSeconds') is not None:
            temp_model = main_models.ListDoctorComputeSummaryResponseBodyDataMetricsMemSeconds()
            self.mem_seconds = temp_model.from_map(m.get('MemSeconds'))

        if m.get('MemSecondsDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorComputeSummaryResponseBodyDataMetricsMemSecondsDayGrowthRatio()
            self.mem_seconds_day_growth_ratio = temp_model.from_map(m.get('MemSecondsDayGrowthRatio'))

        if m.get('MemUtilization') is not None:
            temp_model = main_models.ListDoctorComputeSummaryResponseBodyDataMetricsMemUtilization()
            self.mem_utilization = temp_model.from_map(m.get('MemUtilization'))

        if m.get('ReadSize') is not None:
            temp_model = main_models.ListDoctorComputeSummaryResponseBodyDataMetricsReadSize()
            self.read_size = temp_model.from_map(m.get('ReadSize'))

        if m.get('VcoreSeconds') is not None:
            temp_model = main_models.ListDoctorComputeSummaryResponseBodyDataMetricsVcoreSeconds()
            self.vcore_seconds = temp_model.from_map(m.get('VcoreSeconds'))

        if m.get('VcoreSecondsDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorComputeSummaryResponseBodyDataMetricsVcoreSecondsDayGrowthRatio()
            self.vcore_seconds_day_growth_ratio = temp_model.from_map(m.get('VcoreSecondsDayGrowthRatio'))

        if m.get('VcoreUtilization') is not None:
            temp_model = main_models.ListDoctorComputeSummaryResponseBodyDataMetricsVcoreUtilization()
            self.vcore_utilization = temp_model.from_map(m.get('VcoreUtilization'))

        if m.get('WriteSize') is not None:
            temp_model = main_models.ListDoctorComputeSummaryResponseBodyDataMetricsWriteSize()
            self.write_size = temp_model.from_map(m.get('WriteSize'))

        return self

class ListDoctorComputeSummaryResponseBodyDataMetricsWriteSize(DaraModel):
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

class ListDoctorComputeSummaryResponseBodyDataMetricsVcoreUtilization(DaraModel):
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

class ListDoctorComputeSummaryResponseBodyDataMetricsVcoreSecondsDayGrowthRatio(DaraModel):
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

class ListDoctorComputeSummaryResponseBodyDataMetricsVcoreSeconds(DaraModel):
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

class ListDoctorComputeSummaryResponseBodyDataMetricsReadSize(DaraModel):
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

class ListDoctorComputeSummaryResponseBodyDataMetricsMemUtilization(DaraModel):
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

class ListDoctorComputeSummaryResponseBodyDataMetricsMemSecondsDayGrowthRatio(DaraModel):
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

class ListDoctorComputeSummaryResponseBodyDataMetricsMemSeconds(DaraModel):
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

class ListDoctorComputeSummaryResponseBodyDataAnalysis(DaraModel):
    def __init__(
        self,
        healthy_job_count: int = None,
        need_attention_job_count: int = None,
        score: int = None,
        score_day_growth_ratio: float = None,
        sub_healthy_job_count: int = None,
        unhealthy_job_count: int = None,
    ):
        # The total number of healthy jobs.
        self.healthy_job_count = healthy_job_count
        # The total number of jobs that require attention.
        self.need_attention_job_count = need_attention_job_count
        # The score for jobs.
        self.score = score
        # The day-to-day growth rate of the score for jobs.
        self.score_day_growth_ratio = score_day_growth_ratio
        # The total number of sub-healthy jobs.
        self.sub_healthy_job_count = sub_healthy_job_count
        # The total number of unhealthy jobs.
        self.unhealthy_job_count = unhealthy_job_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.healthy_job_count is not None:
            result['HealthyJobCount'] = self.healthy_job_count

        if self.need_attention_job_count is not None:
            result['NeedAttentionJobCount'] = self.need_attention_job_count

        if self.score is not None:
            result['Score'] = self.score

        if self.score_day_growth_ratio is not None:
            result['ScoreDayGrowthRatio'] = self.score_day_growth_ratio

        if self.sub_healthy_job_count is not None:
            result['SubHealthyJobCount'] = self.sub_healthy_job_count

        if self.unhealthy_job_count is not None:
            result['UnhealthyJobCount'] = self.unhealthy_job_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthyJobCount') is not None:
            self.healthy_job_count = m.get('HealthyJobCount')

        if m.get('NeedAttentionJobCount') is not None:
            self.need_attention_job_count = m.get('NeedAttentionJobCount')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ScoreDayGrowthRatio') is not None:
            self.score_day_growth_ratio = m.get('ScoreDayGrowthRatio')

        if m.get('SubHealthyJobCount') is not None:
            self.sub_healthy_job_count = m.get('SubHealthyJobCount')

        if m.get('UnhealthyJobCount') is not None:
            self.unhealthy_job_count = m.get('UnhealthyJobCount')

        return self


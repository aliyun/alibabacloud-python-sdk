# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListComputeMetricsByInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListComputeMetricsByInstanceResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListComputeMetricsByInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListComputeMetricsByInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        instance_compute_metrics: List[main_models.ListComputeMetricsByInstanceResponseBodyDataInstanceComputeMetrics] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # List of pay-as-you-go job compute usage.
        self.instance_compute_metrics = instance_compute_metrics
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of results returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_compute_metrics:
            for v1 in self.instance_compute_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['instanceComputeMetrics'] = []
        if self.instance_compute_metrics is not None:
            for k1 in self.instance_compute_metrics:
                result['instanceComputeMetrics'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_compute_metrics = []
        if m.get('instanceComputeMetrics') is not None:
            for k1 in m.get('instanceComputeMetrics'):
                temp_model = main_models.ListComputeMetricsByInstanceResponseBodyDataInstanceComputeMetrics()
                self.instance_compute_metrics.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListComputeMetricsByInstanceResponseBodyDataInstanceComputeMetrics(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        job_owner: str = None,
        project_name: str = None,
        signature: str = None,
        spec_code: str = None,
        submit_time: int = None,
        type: str = None,
        unit: str = None,
        usage: float = None,
    ):
        # The end time of the job execution.
        self.end_time = end_time
        # The job(instance) ID.
        self.instance_id = instance_id
        # The owner of the job.
        self.job_owner = job_owner
        # The name of the project.
        self.project_name = project_name
        # The signature of the SQL job.
        self.signature = signature
        # Specifications Type, specifies the resource package that you select when you purchase the MaxCompute service.
        # - OdpsStandard: the pay-as-you-go resource package.
        # 
        # - OdpsSpot: the pay-as-you-go spot resource package.
        self.spec_code = spec_code
        # The submission time of the job.
        self.submit_time = submit_time
        # Metering types.
        # - ComputationSql: the metering data of SQL jobs that involve internal tables.
        # 
        # - ComputationSqlOTS: the metering data of SQL jobs that involve Tablestore external tables.
        # 
        # - ComputationSqlOSS: the metering data of SQL jobs that involve OSS external tables.
        # 
        # - MapReduce: the metering data of MapReduce jobs.
        # 
        # - spark: the metering data of Spark jobs.
        # 
        # - mars: the metering data of Mars jobs.
        self.type = type
        # The unit of computing resource usage
        self.unit = unit
        # The computing resource usage is calculated based on the following items:
        # 
        # - Amount of scanned data in the unit of GB. For the jobs whose metering types are ComputationSql, ComputationSqlOTS, or ComputationSqlOSS, they are billed based on the amount of scanned data. The computing resource usage of such a job is calculated by using the following formula: Amount of scanned data × Complexity. The complexity is fixed at 1 for the jobs whose metering types are ComputationSqlOTS or ComputationSqlOSS.
        # 
        # - CU-hours. For the jobs whose metering types are MapReduce, spark, or mars, they are billed based on CU-hours.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.signature is not None:
            result['signature'] = self.signature

        if self.spec_code is not None:
            result['specCode'] = self.spec_code

        if self.submit_time is not None:
            result['submitTime'] = self.submit_time

        if self.type is not None:
            result['type'] = self.type

        if self.unit is not None:
            result['unit'] = self.unit

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('specCode') is not None:
            self.spec_code = m.get('specCode')

        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self


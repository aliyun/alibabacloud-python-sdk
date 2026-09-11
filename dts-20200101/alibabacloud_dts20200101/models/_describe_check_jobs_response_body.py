# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeCheckJobsResponseBody(DaraModel):
    def __init__(
        self,
        check_jobs: List[main_models.DescribeCheckJobsResponseBodyCheckJobs] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: bool = None,
        total_record_count: int = None,
    ):
        # The information about the data validation tasks.
        self.check_jobs = check_jobs
        # The dynamic error code. This parameter will be deprecated.
        self.dynamic_code = dynamic_code
        # The dynamic error message used to replace the **%s** variable in the **ErrMessage** parameter. > If **ErrMessage** returns **The value of input parameter %s is not valid** and **DynamicMessage** returns **[1,2,3]**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The current page number.
        self.page_number = page_number
        # The maximum number of records that can be displayed on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.check_jobs:
            for v1 in self.check_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckJobs'] = []
        if self.check_jobs is not None:
            for k1 in self.check_jobs:
                result['CheckJobs'].append(k1.to_map() if k1 else None)

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_jobs = []
        if m.get('CheckJobs') is not None:
            for k1 in m.get('CheckJobs'):
                temp_model = main_models.DescribeCheckJobsResponseBodyCheckJobs()
                self.check_jobs.append(temp_model.from_map(k1))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeCheckJobsResponseBodyCheckJobs(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        check_point: int = None,
        check_type: int = None,
        diff_count: int = None,
        diff_sum: int = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        finish_count: int = None,
        group_id: str = None,
        instance_class: str = None,
        job_name: str = None,
        job_step_id: str = None,
        parent_job_type: str = None,
        region_id: str = None,
        status: int = None,
        total_count: int = None,
    ):
        # The billing method. Valid values:
        # - **POSTPAY**: pay-as-you-go.
        # - **PREPAY**: subscription.
        self.charge_type = charge_type
        # The checkpoint.
        self.check_point = check_point
        # The data validation method. Valid values:
        # 
        # - **1**: full data validation.
        # - **2**: incremental data validation.
        self.check_type = check_type
        # The number of rows with data inconsistency.
        self.diff_count = diff_count
        # The progress of initial synchronization, in percentage.
        self.diff_sum = diff_sum
        # The ID of the data migration, data synchronization, or change tracking instance.
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The number of rows that have been validated in the table.
        self.finish_count = finish_count
        # The DTS task ID. > In most cases, you do not need to specify this parameter.
        self.group_id = group_id
        # The instance specifications.
        self.instance_class = instance_class
        # The name of the data validation task.
        self.job_name = job_name
        # The task ID.
        self.job_step_id = job_step_id
        # This parameter will be deprecated.
        self.parent_job_type = parent_job_type
        # The region ID.
        self.region_id = region_id
        # The validation result. Valid values: - **0**: passed. - **1**: failed.
        self.status = status
        # The total number of rows to be validated.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.check_point is not None:
            result['CheckPoint'] = self.check_point

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.diff_count is not None:
            result['DiffCount'] = self.diff_count

        if self.diff_sum is not None:
            result['DiffSum'] = self.diff_sum

        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_step_id is not None:
            result['JobStepId'] = self.job_step_id

        if self.parent_job_type is not None:
            result['ParentJobType'] = self.parent_job_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CheckPoint') is not None:
            self.check_point = m.get('CheckPoint')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('DiffCount') is not None:
            self.diff_count = m.get('DiffCount')

        if m.get('DiffSum') is not None:
            self.diff_sum = m.get('DiffSum')

        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobStepId') is not None:
            self.job_step_id = m.get('JobStepId')

        if m.get('ParentJobType') is not None:
            self.parent_job_type = m.get('ParentJobType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self


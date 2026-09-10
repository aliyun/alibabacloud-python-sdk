# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListMetaDataComponentPageResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListMetaDataComponentPageResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The data list returned by the operation. For the structure of each element, see the child parameters.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The page number, starting from 1.
        self.page_index = page_index
        # The page size, which is the number of records returned per page.
        self.page_size = page_size
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # - true: Successful.
        # - false: Failed. Check errCode and errMessage for details.
        self.success = success
        # The total number of records that meet the query conditions. This parameter is used for pagination.
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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListMetaDataComponentPageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListMetaDataComponentPageResponseBodyData(DaraModel):
    def __init__(
        self,
        component_type: int = None,
        create_time: str = None,
        ds_config: str = None,
        ds_desc: str = None,
        ds_id: str = None,
        ds_name: str = None,
        ds_status: int = None,
        ds_type: str = None,
        ds_version: str = None,
        expired: bool = None,
        id: int = None,
        profiling_job: main_models.ListMetaDataComponentPageResponseBodyDataProfilingJob = None,
    ):
        # The entry component type. In some operations, this parameter is used as a backward compatible field for version 1.1.0. Valid values:
        # - 0: source
        # - 1: destination
        self.component_type = component_type
        # The creation time of the table or partition.
        self.create_time = create_time
        # The datasource config in JSON string format. The structure is defined by each dsType. Parse the JSON string before use. Sensitive fields such as tokens are masked in the response.
        self.ds_config = ds_config
        # The description of the data source.
        self.ds_desc = ds_desc
        # The business ID of the data source (external ID, which may be the same as the primary key ID).
        self.ds_id = ds_id
        # The data source name. Exact match and fuzzy match are supported.
        self.ds_name = ds_name
        # The connectivity status of the data source. Valid values:
        # - 0: Not tested.
        # - 1: Connected.
        # - 2: Connection failed.
        # - -1: Connectivity test not supported.
        self.ds_status = ds_status
        # The data source type, such as Hive or MaxCompute.
        self.ds_type = ds_type
        # The version number of the data source.
        self.ds_version = ds_version
        # Indicates whether the data source has expired. Valid values:
        # - true: Expired.
        # - false: Not expired.
        self.expired = expired
        # The primary key ID that uniquely identifies a record.
        self.id = id
        # The profiling task information, including the task status, scheduling ID, profiling rule, and profiling type. This field is empty if the data source is not associated with a profiling task.
        self.profiling_job = profiling_job

    def validate(self):
        if self.profiling_job:
            self.profiling_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['componentType'] = self.component_type

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.ds_config is not None:
            result['dsConfig'] = self.ds_config

        if self.ds_desc is not None:
            result['dsDesc'] = self.ds_desc

        if self.ds_id is not None:
            result['dsId'] = self.ds_id

        if self.ds_name is not None:
            result['dsName'] = self.ds_name

        if self.ds_status is not None:
            result['dsStatus'] = self.ds_status

        if self.ds_type is not None:
            result['dsType'] = self.ds_type

        if self.ds_version is not None:
            result['dsVersion'] = self.ds_version

        if self.expired is not None:
            result['expired'] = self.expired

        if self.id is not None:
            result['id'] = self.id

        if self.profiling_job is not None:
            result['profilingJob'] = self.profiling_job.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dsConfig') is not None:
            self.ds_config = m.get('dsConfig')

        if m.get('dsDesc') is not None:
            self.ds_desc = m.get('dsDesc')

        if m.get('dsId') is not None:
            self.ds_id = m.get('dsId')

        if m.get('dsName') is not None:
            self.ds_name = m.get('dsName')

        if m.get('dsStatus') is not None:
            self.ds_status = m.get('dsStatus')

        if m.get('dsType') is not None:
            self.ds_type = m.get('dsType')

        if m.get('dsVersion') is not None:
            self.ds_version = m.get('dsVersion')

        if m.get('expired') is not None:
            self.expired = m.get('expired')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('profilingJob') is not None:
            temp_model = main_models.ListMetaDataComponentPageResponseBodyDataProfilingJob()
            self.profiling_job = temp_model.from_map(m.get('profilingJob'))

        return self

class ListMetaDataComponentPageResponseBodyDataProfilingJob(DaraModel):
    def __init__(
        self,
        component_id: int = None,
        create_time: str = None,
        id: int = None,
        job_desc: str = None,
        job_name: str = None,
        last_batch_id: str = None,
        profiling_enable: int = None,
        profiling_permission: int = None,
        profiling_rule: str = None,
        profiling_type: int = None,
        scheduler_token: str = None,
    ):
        # The component ID, which is the primary key of the data source component.
        self.component_id = component_id
        # The creation time of the table or partition.
        self.create_time = create_time
        # The primary key ID that uniquely identifies a record.
        self.id = id
        # The description of the profiling task.
        self.job_desc = job_desc
        # The name of the profiling task.
        self.job_name = job_name
        # The ID of the most recent profiling task batch.
        self.last_batch_id = last_batch_id
        # The profiling task status. Valid values:
        # - 0: Not started.
        # - 1: Running.
        # - 2: Stopped.
        self.profiling_enable = profiling_enable
        # The profiling permission. Valid values:
        # - 0: read-only link
        # - 1: client
        self.profiling_permission = profiling_permission
        # The cron expression for scheduled profiling. This parameter takes effect only when profilingType is set to CRON.
        self.profiling_rule = profiling_rule
        # The profiling policy (scheduling type). Valid values:
        # - 0: daily
        # - 1: CRON
        self.profiling_type = profiling_type
        # The scheduling ID, which uniquely identifies the profiling task on the scheduling side.
        self.scheduler_token = scheduler_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['componentId'] = self.component_id

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.id is not None:
            result['id'] = self.id

        if self.job_desc is not None:
            result['jobDesc'] = self.job_desc

        if self.job_name is not None:
            result['jobName'] = self.job_name

        if self.last_batch_id is not None:
            result['lastBatchId'] = self.last_batch_id

        if self.profiling_enable is not None:
            result['profilingEnable'] = self.profiling_enable

        if self.profiling_permission is not None:
            result['profilingPermission'] = self.profiling_permission

        if self.profiling_rule is not None:
            result['profilingRule'] = self.profiling_rule

        if self.profiling_type is not None:
            result['profilingType'] = self.profiling_type

        if self.scheduler_token is not None:
            result['schedulerToken'] = self.scheduler_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentId') is not None:
            self.component_id = m.get('componentId')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('jobDesc') is not None:
            self.job_desc = m.get('jobDesc')

        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')

        if m.get('lastBatchId') is not None:
            self.last_batch_id = m.get('lastBatchId')

        if m.get('profilingEnable') is not None:
            self.profiling_enable = m.get('profilingEnable')

        if m.get('profilingPermission') is not None:
            self.profiling_permission = m.get('profilingPermission')

        if m.get('profilingRule') is not None:
            self.profiling_rule = m.get('profilingRule')

        if m.get('profilingType') is not None:
            self.profiling_type = m.get('profilingType')

        if m.get('schedulerToken') is not None:
            self.scheduler_token = m.get('schedulerToken')

        return self


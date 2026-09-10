# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListDataCheckReportStepResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataCheckReportStepResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The data list returned by the operation. For the structure of each element, see the child field descriptions.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The page number, starting from 1.
        self.page_index = page_index
        # The page size, which is the number of records returned per page.
        self.page_size = page_size
        # The request ID, which is used to locate and troubleshoot issues with this call.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success. A value of false indicates failure. If the call fails, check errCode and errMessage for troubleshooting.
        self.success = success
        # The total number of records that meet the query conditions. This value is used for pagination.
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
                temp_model = main_models.ListDataCheckReportStepResponseBodyData()
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

class ListDataCheckReportStepResponseBodyData(DaraModel):
    def __init__(
        self,
        boundary: str = None,
        check_colum_count: int = None,
        dst_count: str = None,
        dst_sql: str = None,
        err_message: str = None,
        extra: str = None,
        gmt_create: str = None,
        gmt_end: str = None,
        gmt_modified: str = None,
        gmt_start: str = None,
        id: int = None,
        is_consistent: int = None,
        job_id: int = None,
        metric_colum_count: int = None,
        metric_pass_colum_count: int = None,
        pass_colum_count: int = None,
        result_id: str = None,
        sign_name_list: List[str] = None,
        source_pt_name: str = None,
        src_count: str = None,
        src_sql: str = None,
        status: int = None,
        step_id: str = None,
        target_pt_name: str = None,
    ):
        # The shard boundary information.
        self.boundary = boundary
        # The number of verified fields.
        self.check_colum_count = check_colum_count
        # The destination data volume. For single-SQL verification, this indicates the data volume of the destination result set. For data volume verification and full verification, this indicates the total data volume on the destination.
        self.dst_count = dst_count
        # The SQL statement executed on the destination.
        self.dst_sql = dst_sql
        # The error message.
        self.err_message = err_message
        # The reserved field.
        self.extra = extra
        # The creation time.
        self.gmt_create = gmt_create
        # The job end time.
        self.gmt_end = gmt_end
        # The modification time.
        self.gmt_modified = gmt_modified
        # The job start time.
        self.gmt_start = gmt_start
        # The primary key ID that uniquely identifies a record.
        self.id = id
        # Indicates whether the data is consistent. Valid values:
        # 
        # - 0: inconsistent.
        # - 1: consistent.
        self.is_consistent = is_consistent
        # The unique job ID.
        self.job_id = job_id
        # The number of verified metrics.
        self.metric_colum_count = metric_colum_count
        # The number of metrics that passed verification.
        self.metric_pass_colum_count = metric_pass_colum_count
        # The number of fields that passed verification.
        self.pass_colum_count = pass_colum_count
        # The unique ID of the verification result.
        self.result_id = result_id
        # The list of label names.
        self.sign_name_list = sign_name_list
        # The source partition name.
        self.source_pt_name = source_pt_name
        # The source data volume. For single-SQL verification, this indicates the data volume of the source result set. For data volume verification and full verification, this indicates the total data volume on the source.
        self.src_count = src_count
        # The SQL statement executed on the source.
        self.src_sql = src_sql
        # The task status. Valid values:
        # 
        # - 0: created.
        # - 1: running.
        # - 2: completed.
        # - 3: stopped.
        # - 4: canceled.
        self.status = status
        # The step ID that uniquely identifies an execution step within the job.
        self.step_id = step_id
        # The destination partition name.
        self.target_pt_name = target_pt_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boundary is not None:
            result['boundary'] = self.boundary

        if self.check_colum_count is not None:
            result['checkColumCount'] = self.check_colum_count

        if self.dst_count is not None:
            result['dstCount'] = self.dst_count

        if self.dst_sql is not None:
            result['dstSql'] = self.dst_sql

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.extra is not None:
            result['extra'] = self.extra

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_end is not None:
            result['gmtEnd'] = self.gmt_end

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.gmt_start is not None:
            result['gmtStart'] = self.gmt_start

        if self.id is not None:
            result['id'] = self.id

        if self.is_consistent is not None:
            result['isConsistent'] = self.is_consistent

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.metric_colum_count is not None:
            result['metricColumCount'] = self.metric_colum_count

        if self.metric_pass_colum_count is not None:
            result['metricPassColumCount'] = self.metric_pass_colum_count

        if self.pass_colum_count is not None:
            result['passColumCount'] = self.pass_colum_count

        if self.result_id is not None:
            result['resultId'] = self.result_id

        if self.sign_name_list is not None:
            result['signNameList'] = self.sign_name_list

        if self.source_pt_name is not None:
            result['sourcePtName'] = self.source_pt_name

        if self.src_count is not None:
            result['srcCount'] = self.src_count

        if self.src_sql is not None:
            result['srcSql'] = self.src_sql

        if self.status is not None:
            result['status'] = self.status

        if self.step_id is not None:
            result['stepId'] = self.step_id

        if self.target_pt_name is not None:
            result['targetPtName'] = self.target_pt_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boundary') is not None:
            self.boundary = m.get('boundary')

        if m.get('checkColumCount') is not None:
            self.check_colum_count = m.get('checkColumCount')

        if m.get('dstCount') is not None:
            self.dst_count = m.get('dstCount')

        if m.get('dstSql') is not None:
            self.dst_sql = m.get('dstSql')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtEnd') is not None:
            self.gmt_end = m.get('gmtEnd')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('gmtStart') is not None:
            self.gmt_start = m.get('gmtStart')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isConsistent') is not None:
            self.is_consistent = m.get('isConsistent')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('metricColumCount') is not None:
            self.metric_colum_count = m.get('metricColumCount')

        if m.get('metricPassColumCount') is not None:
            self.metric_pass_colum_count = m.get('metricPassColumCount')

        if m.get('passColumCount') is not None:
            self.pass_colum_count = m.get('passColumCount')

        if m.get('resultId') is not None:
            self.result_id = m.get('resultId')

        if m.get('signNameList') is not None:
            self.sign_name_list = m.get('signNameList')

        if m.get('sourcePtName') is not None:
            self.source_pt_name = m.get('sourcePtName')

        if m.get('srcCount') is not None:
            self.src_count = m.get('srcCount')

        if m.get('srcSql') is not None:
            self.src_sql = m.get('srcSql')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('stepId') is not None:
            self.step_id = m.get('stepId')

        if m.get('targetPtName') is not None:
            self.target_pt_name = m.get('targetPtName')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListBatchMediaProducingJobsResponseBody(DaraModel):
    def __init__(
        self,
        editing_batch_job_list: List[main_models.ListBatchMediaProducingJobsResponseBodyEditingBatchJobList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The queried quick video production jobs.
        self.editing_batch_job_list = editing_batch_job_list
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.editing_batch_job_list:
            for v1 in self.editing_batch_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EditingBatchJobList'] = []
        if self.editing_batch_job_list is not None:
            for k1 in self.editing_batch_job_list:
                result['EditingBatchJobList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.editing_batch_job_list = []
        if m.get('EditingBatchJobList') is not None:
            for k1 in m.get('EditingBatchJobList'):
                temp_model = main_models.ListBatchMediaProducingJobsResponseBodyEditingBatchJobList()
                self.editing_batch_job_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListBatchMediaProducingJobsResponseBodyEditingBatchJobList(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        create_time: str = None,
        editing_config: str = None,
        extend: str = None,
        input_config: str = None,
        job_id: str = None,
        job_type: str = None,
        modified_time: str = None,
        output_config: str = None,
        status: str = None,
        user_data: str = None,
    ):
        # The time when the job was complete. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.complete_time = complete_time
        # The time when the job was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The editing configurations. For more information, see [EditingConfig](~~2692547#1be9bba03b7qu~~).
        self.editing_config = editing_config
        # The extended information of the job.
        self.extend = extend
        # The input configurations.
        self.input_config = input_config
        # The ID of the quick video production job.
        self.job_id = job_id
        # The job type.
        # 
        # Valid values:
        # 
        # *   Script: script-based editing job that mixes media assets.
        # *   Smart_Mix: intelligent editing job that mixes media assets.
        self.job_type = job_type
        # The time when the job was last modified.
        self.modified_time = modified_time
        # The output configurations. For more information, see [OutputConfig](~~2692547#447b928fcbuoa~~).
        self.output_config = output_config
        # The job state.
        # 
        # Valid values:
        # 
        # *   Finished
        # *   Init
        # *   Failed
        # *   Processing
        self.status = status
        # The user-defined data in the JSON format, which can be up to 512 bytes in length. You can specify a custom callback URL. For more information, see [Configure a callback upon editing completion](https://help.aliyun.com/document_detail/451631.html).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.input_config is not None:
            result['InputConfig'] = self.input_config

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self


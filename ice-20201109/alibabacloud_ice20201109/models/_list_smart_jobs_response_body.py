# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListSmartJobsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        smart_job_list: List[main_models.ListSmartJobsResponseBodySmartJobList] = None,
        total_count: str = None,
    ):
        # The maximum number of entries returned on a single page. The value is set to the maximum number of entries returned on each page except for the last page. Valid example: 10,10,5. Invalid example: 10,5,10.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The queried intelligent jobs.
        self.smart_job_list = smart_job_list
        # Optional. The total number of entries returned. By default, this parameter is not returned.
        self.total_count = total_count

    def validate(self):
        if self.smart_job_list:
            for v1 in self.smart_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SmartJobList'] = []
        if self.smart_job_list is not None:
            for k1 in self.smart_job_list:
                result['SmartJobList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.smart_job_list = []
        if m.get('SmartJobList') is not None:
            for k1 in m.get('SmartJobList'):
                temp_model = main_models.ListSmartJobsResponseBodySmartJobList()
                self.smart_job_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSmartJobsResponseBodySmartJobList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        editing_config: str = None,
        input_config: main_models.ListSmartJobsResponseBodySmartJobListInputConfig = None,
        job_id: str = None,
        job_state: str = None,
        job_type: str = None,
        modified_time: str = None,
        output_config: main_models.ListSmartJobsResponseBodySmartJobListOutputConfig = None,
        title: str = None,
        user_data: str = None,
        user_id: int = None,
    ):
        # The time when the job was created.
        self.create_time = create_time
        # The job description.
        self.description = description
        # The editing configurations.
        self.editing_config = editing_config
        # The input configurations.
        self.input_config = input_config
        # The job ID.
        self.job_id = job_id
        # The job state.
        # 
        # Valid values:
        # 
        # *   Finished: The job is complete.
        # *   Failed: The job failed.
        # *   Executing: The job is in progress.
        # *   Created: The job is created.
        self.job_state = job_state
        # The job type.
        # 
        # Valid values:
        # 
        # *   ASR: ASR job.
        # *   DynamicChart: dynamic chart job.
        # *   TextToSpeech: intelligent audio production job.
        self.job_type = job_type
        # The time when the job was last modified.
        self.modified_time = modified_time
        # The output configurations.
        self.output_config = output_config
        # The job title.
        self.title = title
        # The user-defined data.
        self.user_data = user_data
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.input_config:
            self.input_config.validate()
        if self.output_config:
            self.output_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config

        if self.input_config is not None:
            result['InputConfig'] = self.input_config.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_state is not None:
            result['JobState'] = self.job_state

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config.to_map()

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')

        if m.get('InputConfig') is not None:
            temp_model = main_models.ListSmartJobsResponseBodySmartJobListInputConfig()
            self.input_config = temp_model.from_map(m.get('InputConfig'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('OutputConfig') is not None:
            temp_model = main_models.ListSmartJobsResponseBodySmartJobListOutputConfig()
            self.output_config = temp_model.from_map(m.get('OutputConfig'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ListSmartJobsResponseBodySmartJobListOutputConfig(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        object: str = None,
    ):
        # The Object Storage Service (OSS) bucket.
        self.bucket = bucket
        # The OSS object.
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

class ListSmartJobsResponseBodySmartJobListInputConfig(DaraModel):
    def __init__(
        self,
        input_file: str = None,
        keyword: str = None,
    ):
        # The information about the input file.
        self.input_file = input_file
        # The keyword information.
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_file is not None:
            result['InputFile'] = self.input_file

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListPackageJobsResponseBody(DaraModel):
    def __init__(
        self,
        package_job_list: main_models.ListPackageJobsResponseBodyPackageJobList = None,
        request_id: str = None,
    ):
        # The list of packaging jobs.
        self.package_job_list = package_job_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.package_job_list:
            self.package_job_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.package_job_list is not None:
            result['PackageJobList'] = self.package_job_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageJobList') is not None:
            temp_model = main_models.ListPackageJobsResponseBodyPackageJobList()
            self.package_job_list = temp_model.from_map(m.get('PackageJobList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPackageJobsResponseBodyPackageJobList(DaraModel):
    def __init__(
        self,
        next_page_token: str = None,
        package_jobs: List[main_models.ListPackageJobsResponseBodyPackageJobListPackageJobs] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. The token of the next page is returned after you call this operation for the first time.
        self.next_page_token = next_page_token
        # The list of packaging jobs.
        self.package_jobs = package_jobs

    def validate(self):
        if self.package_jobs:
            for v1 in self.package_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        result['PackageJobs'] = []
        if self.package_jobs is not None:
            for k1 in self.package_jobs:
                result['PackageJobs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        self.package_jobs = []
        if m.get('PackageJobs') is not None:
            for k1 in m.get('PackageJobs'):
                temp_model = main_models.ListPackageJobsResponseBodyPackageJobListPackageJobs()
                self.package_jobs.append(temp_model.from_map(k1))

        return self

class ListPackageJobsResponseBodyPackageJobListPackageJobs(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: str = None,
        finish_time: str = None,
        inputs: List[main_models.ListPackageJobsResponseBodyPackageJobListPackageJobsInputs] = None,
        job_id: str = None,
        message: str = None,
        modified_time: str = None,
        name: str = None,
        output: main_models.ListPackageJobsResponseBodyPackageJobListPackageJobsOutput = None,
        pipeline_id: str = None,
        priority: int = None,
        status: str = None,
        submit_time: str = None,
        trigger_source: str = None,
        user_data: str = None,
    ):
        # The error code returned if the job fails.
        self.code = code
        # The time when the job was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the job was complete. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.finish_time = finish_time
        # The input of the job.
        self.inputs = inputs
        # The job ID.
        self.job_id = job_id
        # The error message that is returned.
        self.message = message
        # The time when the job was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modified_time = modified_time
        # The name of the job.
        self.name = name
        # The output of the job.
        self.output = output
        # The ID of the ApsaraVideo Media Processing (MPS) queue that is used to run the job.
        self.pipeline_id = pipeline_id
        # The priority of the job. Valid values: 1 to 10. The greater the value, the higher the priority. Default value: 6.
        self.priority = priority
        # The state of the job.
        self.status = status
        # The time when the job was submitted. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.submit_time = submit_time
        # The source of the job. Valid values:
        # 
        # *   API
        # *   WorkFlow
        # *   Console
        self.trigger_source = trigger_source
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        if self.inputs:
            for v1 in self.inputs:
                 if v1:
                    v1.validate()
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        result['Inputs'] = []
        if self.inputs is not None:
            for k1 in self.inputs:
                result['Inputs'].append(k1.to_map() if k1 else None)

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        if self.trigger_source is not None:
            result['TriggerSource'] = self.trigger_source

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        self.inputs = []
        if m.get('Inputs') is not None:
            for k1 in m.get('Inputs'):
                temp_model = main_models.ListPackageJobsResponseBodyPackageJobListPackageJobsInputs()
                self.inputs.append(temp_model.from_map(k1))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            temp_model = main_models.ListPackageJobsResponseBodyPackageJobListPackageJobsOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class ListPackageJobsResponseBodyPackageJobListPackageJobsOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The media object.
        # 
        # *   If Type is set to OSS, the URL of an OSS object is returned. Both the OSS and HTTP protocols are supported.
        # *   If Type is set to Media, set this parameter to the ID of a media asset.
        self.media = media
        # The type of the media object. Valid values:
        # 
        # *   OSS: an OSS object.
        # *   Media: a media asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListPackageJobsResponseBodyPackageJobListPackageJobsInputs(DaraModel):
    def __init__(
        self,
        input: main_models.ListPackageJobsResponseBodyPackageJobListPackageJobsInputsInput = None,
    ):
        # The information about the input stream file.
        self.input = input

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = main_models.ListPackageJobsResponseBodyPackageJobListPackageJobsInputsInput()
            self.input = temp_model.from_map(m.get('Input'))

        return self

class ListPackageJobsResponseBodyPackageJobListPackageJobsInputsInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The media object.
        # 
        # *   If Type is set to OSS, the URL of an OSS object is returned. Both the OSS and HTTP protocols are supported.
        # *   If Type is set to Media, set this parameter to the ID of a media asset.
        self.media = media
        # The type of the media object. Valid values:
        # 
        # *   OSS: an Object Storage Service (OSS) object.
        # *   Media: a media asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListSnapshotJobsResponseBody(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.ListSnapshotJobsResponseBodyJobs] = None,
        next_page_token: str = None,
        request_id: str = None,
    ):
        # The list of jobs.
        self.jobs = jobs
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_page_token = next_page_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['Jobs'].append(k1.to_map() if k1 else None)

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k1 in m.get('Jobs'):
                temp_model = main_models.ListSnapshotJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSnapshotJobsResponseBodyJobs(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        count: int = None,
        create_time: str = None,
        finish_time: str = None,
        input: main_models.ListSnapshotJobsResponseBodyJobsInput = None,
        job_id: str = None,
        modified_time: str = None,
        name: str = None,
        output: main_models.ListSnapshotJobsResponseBodyJobsOutput = None,
        pipeline_id: str = None,
        status: str = None,
        submit_time: str = None,
        template_id: str = None,
        trigger_source: str = None,
        type: str = None,
    ):
        # Indicates whether the snapshots were captured in asynchronous mode.
        self.async_ = async_
        # The number of snapshots.
        self.count = count
        # The time when the job was created.
        self.create_time = create_time
        # The time when the job was complete.
        self.finish_time = finish_time
        # The input of the job.
        self.input = input
        # The job ID.
        self.job_id = job_id
        # The time when the job was last modified.
        self.modified_time = modified_time
        # The name of the job.
        self.name = name
        # The output of the job.
        self.output = output
        # The ID of the MPS queue to which the job was submitted.
        self.pipeline_id = pipeline_id
        # The state of the job.
        # 
        # *   **Success**: The job is successful.
        # *   **Fail**: The job failed.
        # *   **Init**: The job is submitted.
        self.status = status
        # The time when the job was submitted.
        self.submit_time = submit_time
        # The template ID.
        self.template_id = template_id
        # The request trigger source.
        # 
        # Valid values:
        # 
        # *   Console
        # *   Workflow
        # *   API
        self.trigger_source = trigger_source
        # The type of the job.
        # 
        # Valid values:
        # 
        # *   WebVtt
        # *   Sprite
        # *   Normal
        self.type = type

    def validate(self):
        if self.input:
            self.input.validate()
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['Async'] = self.async_

        if self.count is not None:
            result['Count'] = self.count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.trigger_source is not None:
            result['TriggerSource'] = self.trigger_source

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Input') is not None:
            temp_model = main_models.ListSnapshotJobsResponseBodyJobsInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            temp_model = main_models.ListSnapshotJobsResponseBodyJobsOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListSnapshotJobsResponseBodyJobsOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The output file. If Type is set to OSS, the URL of an OSS object is returned. If Type is set to Media, the ID of a media asset is returned. The URL of an OSS object can be in one of the following formats:
        # 
        # 1.  OSS://bucket/object
        # 2.  http(s)://bucket.oss-[RegionId].aliyuncs.com/object
        # 
        # In the URL, bucket specifies an OSS bucket that resides in the same region as the job, and object specifies the object URL in OSS. If multiple static snapshots were captured, the object must contain the "{Count}" placeholder. In the case of a sprite, the object must contain the "{TileCount}" placeholder. The suffix of the WebVTT snapshot objects must be ".vtt".
        self.media = media
        # The type of the output file. Valid values:
        # 
        # 1.  OSS: an OSS object.
        # 2.  Media: a media asset.
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

class ListSnapshotJobsResponseBodyJobsInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The input file. If Type is set to OSS, the URL of an OSS object is returned. If Type is set to Media, the ID of a media asset is returned. The URL of an OSS object can be in one of the following formats: 1. OSS://bucket/object 2. http(s)://bucket.oss-[RegionId].aliyuncs.com/object In the URL, bucket specifies an OSS bucket that resides in the same region as the job, and object specifies the object URL in OSS.
        self.media = media
        # The type of the input file. Valid values:
        # 
        # 1.  OSS: an Object Storage Service (OSS) object.
        # 2.  Media: a media asset.
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListEdgeTranscodeJobResponseBody(DaraModel):
    def __init__(
        self,
        job_list: main_models.ListEdgeTranscodeJobResponseBodyJobList = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The edge transcoding tasks.
        self.job_list = job_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.job_list:
            self.job_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_list is not None:
            result['JobList'] = self.job_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobList') is not None:
            temp_model = main_models.ListEdgeTranscodeJobResponseBodyJobList()
            self.job_list = temp_model.from_map(m.get('JobList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEdgeTranscodeJobResponseBodyJobList(DaraModel):
    def __init__(
        self,
        job: List[main_models.ListEdgeTranscodeJobResponseBodyJobListJob] = None,
    ):
        self.job = job

    def validate(self):
        if self.job:
            for v1 in self.job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Job'] = []
        if self.job is not None:
            for k1 in self.job:
                result['Job'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job = []
        if m.get('Job') is not None:
            for k1 in m.get('Job'):
                temp_model = main_models.ListEdgeTranscodeJobResponseBodyJobListJob()
                self.job.append(temp_model.from_map(k1))

        return self

class ListEdgeTranscodeJobResponseBodyJobListJob(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        job_id: str = None,
        last_start_at: str = None,
        last_stop_at: str = None,
        name: str = None,
        status: str = None,
        stream_input: str = None,
        stream_output: str = None,
        template_id: str = None,
        template_name: str = None,
        type: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The ID of the task.
        self.job_id = job_id
        # The time when the task was last started.
        self.last_start_at = last_start_at
        # The time when the task was last stopped.
        self.last_stop_at = last_stop_at
        # The name of the task.
        self.name = name
        # The status of the task. Valid values:
        # 
        # *   0: not started
        # *   1: in progress
        self.status = status
        # The URL of the input stream.
        self.stream_input = stream_input
        # The URL of the output stream.
        self.stream_output = stream_output
        # The ID of the edge transcoding template used by the task.
        self.template_id = template_id
        # The name of the edge transcoding template used by the task.
        self.template_name = template_name
        # The type of edge transcoding. Valid values:
        # 
        # *   common: standard transcoding and Narrowband HD™ 1.0 transcoding.
        # *   nbhd-2: Narrowband HD™ 2.0 transcoding
        # *   ultra-hd: ultra-high definition transcoding
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.last_start_at is not None:
            result['LastStartAt'] = self.last_start_at

        if self.last_stop_at is not None:
            result['LastStopAt'] = self.last_stop_at

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.stream_input is not None:
            result['StreamInput'] = self.stream_input

        if self.stream_output is not None:
            result['StreamOutput'] = self.stream_output

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('LastStartAt') is not None:
            self.last_start_at = m.get('LastStartAt')

        if m.get('LastStopAt') is not None:
            self.last_stop_at = m.get('LastStopAt')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StreamInput') is not None:
            self.stream_input = m.get('StreamInput')

        if m.get('StreamOutput') is not None:
            self.stream_output = m.get('StreamOutput')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


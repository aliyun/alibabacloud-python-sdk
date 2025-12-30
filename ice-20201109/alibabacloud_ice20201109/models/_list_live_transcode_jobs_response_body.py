# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListLiveTranscodeJobsResponseBody(DaraModel):
    def __init__(
        self,
        job_list: List[main_models.ListLiveTranscodeJobsResponseBodyJobList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of transcoding jobs.
        self.job_list = job_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.job_list:
            for v1 in self.job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobList'] = []
        if self.job_list is not None:
            for k1 in self.job_list:
                result['JobList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k1 in m.get('JobList'):
                temp_model = main_models.ListLiveTranscodeJobsResponseBodyJobList()
                self.job_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLiveTranscodeJobsResponseBodyJobList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        job_id: str = None,
        name: str = None,
        output_stream: main_models.ListLiveTranscodeJobsResponseBodyJobListOutputStream = None,
        start_mode: int = None,
        status: int = None,
        stream_input: main_models.ListLiveTranscodeJobsResponseBodyJobListStreamInput = None,
        template_id: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The time when the job was created.
        self.create_time = create_time
        # The job ID.
        self.job_id = job_id
        # The name of the transcoding job.
        self.name = name
        # The information about the output stream.
        self.output_stream = output_stream
        # The start mode of the job.
        self.start_mode = start_mode
        # The state of the job.
        self.status = status
        # The information about the input stream.
        self.stream_input = stream_input
        # The ID of the transcoding template used by the transcoding job.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The type of the transcoding template used by the transcoding job.
        self.template_type = template_type

    def validate(self):
        if self.output_stream:
            self.output_stream.validate()
        if self.stream_input:
            self.stream_input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.output_stream is not None:
            result['OutputStream'] = self.output_stream.to_map()

        if self.start_mode is not None:
            result['StartMode'] = self.start_mode

        if self.status is not None:
            result['Status'] = self.status

        if self.stream_input is not None:
            result['StreamInput'] = self.stream_input.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputStream') is not None:
            temp_model = main_models.ListLiveTranscodeJobsResponseBodyJobListOutputStream()
            self.output_stream = temp_model.from_map(m.get('OutputStream'))

        if m.get('StartMode') is not None:
            self.start_mode = m.get('StartMode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StreamInput') is not None:
            temp_model = main_models.ListLiveTranscodeJobsResponseBodyJobListStreamInput()
            self.stream_input = temp_model.from_map(m.get('StreamInput'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

class ListLiveTranscodeJobsResponseBodyJobListStreamInput(DaraModel):
    def __init__(
        self,
        input_url: str = None,
        type: str = None,
    ):
        # The URL of the input stream.
        self.input_url = input_url
        # The type of the input stream.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_url is not None:
            result['InputUrl'] = self.input_url

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputUrl') is not None:
            self.input_url = m.get('InputUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListLiveTranscodeJobsResponseBodyJobListOutputStream(DaraModel):
    def __init__(
        self,
        stream_infos: List[main_models.ListLiveTranscodeJobsResponseBodyJobListOutputStreamStreamInfos] = None,
    ):
        # The list of stream URLs.
        self.stream_infos = stream_infos

    def validate(self):
        if self.stream_infos:
            for v1 in self.stream_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StreamInfos'] = []
        if self.stream_infos is not None:
            for k1 in self.stream_infos:
                result['StreamInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_infos = []
        if m.get('StreamInfos') is not None:
            for k1 in m.get('StreamInfos'):
                temp_model = main_models.ListLiveTranscodeJobsResponseBodyJobListOutputStreamStreamInfos()
                self.stream_infos.append(temp_model.from_map(k1))

        return self

class ListLiveTranscodeJobsResponseBodyJobListOutputStreamStreamInfos(DaraModel):
    def __init__(
        self,
        output_url: str = None,
        type: str = None,
    ):
        # The URL of the output stream.
        self.output_url = output_url
        # The type of the output stream protocol. Only the RTMP protocol is supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


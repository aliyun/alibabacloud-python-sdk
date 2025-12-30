# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetMediaConvertJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetMediaConvertJobResponseBodyJob = None,
        request_id: str = None,
    ):
        # The transcoding task.
        self.job = job
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job is not None:
            result['Job'] = self.job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = main_models.GetMediaConvertJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaConvertJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        code: str = None,
        config: main_models.GetMediaConvertJobResponseBodyJobConfig = None,
        create_time: str = None,
        finish_time: str = None,
        job_id: str = None,
        message: str = None,
        output_details: List[main_models.MediaConvertOutputDetail] = None,
        output_group_details: List[main_models.MediaConvertOutputGroupDetail] = None,
        percent: int = None,
        pipeline_id: str = None,
        request_id: str = None,
        state: str = None,
        user_data: str = None,
    ):
        # The idempotency key of the request for creating the transcoding task.
        self.client_token = client_token
        # The error code returned when the transcoding task failed.
        self.code = code
        # The configurations of the transcoding task.
        self.config = config
        self.create_time = create_time
        self.finish_time = finish_time
        # The ID of the transcoding task, which is a 32-bit string.
        self.job_id = job_id
        # The error message returned when the transcoding task failed.
        self.message = message
        # The details of the transcoded outputs, each corresponding to an output configuration.
        self.output_details = output_details
        # The details of the output groups, each corresponding to an output group configuration.
        self.output_group_details = output_group_details
        self.percent = percent
        # The ID of the queue.
        self.pipeline_id = pipeline_id
        # The ID of the request for creating the transcoding task.
        self.request_id = request_id
        # The status of the transcoding task. Valid values:
        # 
        # *   Inited: The task is initialized.
        # *   Running
        # *   Success
        # *   Failed
        # *   Cancelled
        self.state = state
        # The user data.
        self.user_data = user_data

    def validate(self):
        if self.config:
            self.config.validate()
        if self.output_details:
            for v1 in self.output_details:
                 if v1:
                    v1.validate()
        if self.output_group_details:
            for v1 in self.output_group_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.code is not None:
            result['Code'] = self.code

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        result['OutputDetails'] = []
        if self.output_details is not None:
            for k1 in self.output_details:
                result['OutputDetails'].append(k1.to_map() if k1 else None)

        result['OutputGroupDetails'] = []
        if self.output_group_details is not None:
            for k1 in self.output_group_details:
                result['OutputGroupDetails'].append(k1.to_map() if k1 else None)

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Config') is not None:
            temp_model = main_models.GetMediaConvertJobResponseBodyJobConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.output_details = []
        if m.get('OutputDetails') is not None:
            for k1 in m.get('OutputDetails'):
                temp_model = main_models.MediaConvertOutputDetail()
                self.output_details.append(temp_model.from_map(k1))

        self.output_group_details = []
        if m.get('OutputGroupDetails') is not None:
            for k1 in m.get('OutputGroupDetails'):
                temp_model = main_models.MediaConvertOutputGroupDetail()
                self.output_group_details.append(temp_model.from_map(k1))

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetMediaConvertJobResponseBodyJobConfig(DaraModel):
    def __init__(
        self,
        inputs: List[main_models.MediaConvertInput] = None,
        job_name: str = None,
        output_groups: List[main_models.MediaConvertOutputGroup] = None,
        outputs: List[main_models.MediaConvertOutput] = None,
    ):
        # The inputs of the transcoding task.
        self.inputs = inputs
        self.job_name = job_name
        # The output group configurations.
        self.output_groups = output_groups
        # The output configurations.
        self.outputs = outputs

    def validate(self):
        if self.inputs:
            for v1 in self.inputs:
                 if v1:
                    v1.validate()
        if self.output_groups:
            for v1 in self.output_groups:
                 if v1:
                    v1.validate()
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Inputs'] = []
        if self.inputs is not None:
            for k1 in self.inputs:
                result['Inputs'].append(k1.to_map() if k1 else None)

        if self.job_name is not None:
            result['JobName'] = self.job_name

        result['OutputGroups'] = []
        if self.output_groups is not None:
            for k1 in self.output_groups:
                result['OutputGroups'].append(k1.to_map() if k1 else None)

        result['Outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['Outputs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inputs = []
        if m.get('Inputs') is not None:
            for k1 in m.get('Inputs'):
                temp_model = main_models.MediaConvertInput()
                self.inputs.append(temp_model.from_map(k1))

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        self.output_groups = []
        if m.get('OutputGroups') is not None:
            for k1 in m.get('OutputGroups'):
                temp_model = main_models.MediaConvertOutputGroup()
                self.output_groups.append(temp_model.from_map(k1))

        self.outputs = []
        if m.get('Outputs') is not None:
            for k1 in m.get('Outputs'):
                temp_model = main_models.MediaConvertOutput()
                self.outputs.append(temp_model.from_map(k1))

        return self


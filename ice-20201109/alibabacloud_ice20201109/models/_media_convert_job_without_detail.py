# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertJobWithoutDetail(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        code: str = None,
        config: main_models.MediaConvertJobWithoutDetailConfig = None,
        create_time: str = None,
        finish_time: str = None,
        job_id: str = None,
        message: str = None,
        pipeline_id: str = None,
        request_id: str = None,
        state: str = None,
        user_data: str = None,
    ):
        self.client_token = client_token
        self.code = code
        self.config = config
        self.create_time = create_time
        self.finish_time = finish_time
        self.job_id = job_id
        self.message = message
        self.pipeline_id = pipeline_id
        self.request_id = request_id
        self.state = state
        self.user_data = user_data

    def validate(self):
        if self.config:
            self.config.validate()

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
            temp_model = main_models.MediaConvertJobWithoutDetailConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class MediaConvertJobWithoutDetailConfig(DaraModel):
    def __init__(
        self,
        inputs: List[main_models.MediaConvertInput] = None,
        job_name: str = None,
        output_groups: List[main_models.MediaConvertOutputGroup] = None,
        outputs: List[main_models.MediaConvertOutput] = None,
    ):
        self.inputs = inputs
        self.job_name = job_name
        self.output_groups = output_groups
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


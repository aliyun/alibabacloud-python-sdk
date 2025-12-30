# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertJob(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        code: str = None,
        config: main_models.MediaConvertJobConfig = None,
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
        self.client_token = client_token
        self.code = code
        self.config = config
        self.create_time = create_time
        self.finish_time = finish_time
        self.job_id = job_id
        self.message = message
        self.output_details = output_details
        self.output_group_details = output_group_details
        self.percent = percent
        self.pipeline_id = pipeline_id
        self.request_id = request_id
        self.state = state
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
            temp_model = main_models.MediaConvertJobConfig()
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


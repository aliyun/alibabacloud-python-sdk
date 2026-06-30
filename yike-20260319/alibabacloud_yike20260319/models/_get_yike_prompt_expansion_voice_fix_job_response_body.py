# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260319 import models as main_models
from darabonba.model import DaraModel

class GetYikePromptExpansionVoiceFixJobResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        job_params: str = None,
        job_result: List[main_models.GetYikePromptExpansionVoiceFixJobResponseBodyJobResult] = None,
        job_status: str = None,
        request_id: str = None,
        start_time: str = None,
        user_data: str = None,
    ):
        # The end time.
        self.end_time = end_time
        # The error code. This parameter is returned when the task is in the Failed state.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The task ID.
        self.job_id = job_id
        # The task parameters, in JSON format. The following fields are included:
        # - model (String, required): The model name. Example: happyhorse-1.0-r2v.
        # - input (Object, required): The input data object.
        #   - prompt (String, required): The prompt content. The maximum length is 10,000 characters.
        #   - media (Array(Object), required): The list of media materials used to specify reference images and audio.
        #     - type (String, required): The input media type. Valid values: reference_image and reference_audio.
        #     - url (String, required): The URL of the input media.
        # - parameters (Object, required): The video generation parameter object.
        #   - duration (Integer, required): The video duration in seconds. The value must be a positive integer. Valid values: 5 to 15.
        #   - ratio (String, required): The aspect ratio. Valid values: 16:9, 9:16, 4:3, 3:4, and 1:1.
        #   - resolution (String, required): The video resolution. Valid values: 720P and 1080P.
        #   - specialEdition (Bool, optional): The cost-effective edition parameter. This parameter can be set to true only when the resolution is 1080P.
        #   - skipPromptEnhancer (Bool, optional): Specifies whether to skip prompt enhancement. Default value: false.
        #   - skipVoiceResync (Bool, optional): Specifies whether to skip audio repair. Default value: false.
        self.job_params = job_params
        # The task result of the node.
        self.job_result = job_result
        # The task status. Valid values:
        # 
        # - **Succeeded**: The task is processed.
        # 
        # - **Failed**: The task failed.
        # 
        # - **Running**: The task is being processed.
        self.job_status = job_status
        # RequestId
        self.request_id = request_id
        # The start time.
        self.start_time = start_time
        # The custom user parameter.
        self.user_data = user_data

    def validate(self):
        if self.job_result:
            for v1 in self.job_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        result['JobResult'] = []
        if self.job_result is not None:
            for k1 in self.job_result:
                result['JobResult'].append(k1.to_map() if k1 else None)

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        self.job_result = []
        if m.get('JobResult') is not None:
            for k1 in m.get('JobResult'):
                temp_model = main_models.GetYikePromptExpansionVoiceFixJobResponseBodyJobResult()
                self.job_result.append(temp_model.from_map(k1))

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetYikePromptExpansionVoiceFixJobResponseBodyJobResult(DaraModel):
    def __init__(
        self,
        output_url: str = None,
    ):
        # Oss Url
        self.output_url = output_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        return self


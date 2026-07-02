# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260319 import models as main_models
from darabonba.model import DaraModel

class GetImageGenerationJobResponseBody(DaraModel):
    def __init__(
        self,
        image_generation_job: main_models.GetImageGenerationJobResponseBodyImageGenerationJob = None,
        request_id: str = None,
    ):
        self.image_generation_job = image_generation_job
        self.request_id = request_id

    def validate(self):
        if self.image_generation_job:
            self.image_generation_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_generation_job is not None:
            result['ImageGenerationJob'] = self.image_generation_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageGenerationJob') is not None:
            temp_model = main_models.GetImageGenerationJobResponseBodyImageGenerationJob()
            self.image_generation_job = temp_model.from_map(m.get('ImageGenerationJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetImageGenerationJobResponseBodyImageGenerationJob(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        error_message: str = None,
        input: str = None,
        job_id: str = None,
        job_parameters: str = None,
        job_type: str = None,
        model: str = None,
        n: str = None,
        output: str = None,
        resolution: str = None,
        scene: str = None,
        status: str = None,
        user_data: str = None,
    ):
        self.aspect_ratio = aspect_ratio
        self.error_message = error_message
        self.input = input
        self.job_id = job_id
        self.job_parameters = job_parameters
        self.job_type = job_type
        self.model = model
        self.n = n
        self.output = output
        self.resolution = resolution
        self.scene = scene
        self.status = status
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.input is not None:
            result['Input'] = self.input

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_parameters is not None:
            result['JobParameters'] = self.job_parameters

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.model is not None:
            result['Model'] = self.model

        if self.n is not None:
            result['N'] = self.n

        if self.output is not None:
            result['Output'] = self.output

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobParameters') is not None:
            self.job_parameters = m.get('JobParameters')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self


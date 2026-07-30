# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetVideoGenerationJobResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        video_generation_job: main_models.GetVideoGenerationJobResponseBodyVideoGenerationJob = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The video generation task.
        self.video_generation_job = video_generation_job

    def validate(self):
        if self.video_generation_job:
            self.video_generation_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.video_generation_job is not None:
            result['VideoGenerationJob'] = self.video_generation_job.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VideoGenerationJob') is not None:
            temp_model = main_models.GetVideoGenerationJobResponseBodyVideoGenerationJob()
            self.video_generation_job = temp_model.from_map(m.get('VideoGenerationJob'))

        return self

class GetVideoGenerationJobResponseBodyVideoGenerationJob(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        duration: str = None,
        error_message: str = None,
        input: str = None,
        job_id: str = None,
        job_parameters: str = None,
        job_type: str = None,
        model: str = None,
        n: int = None,
        output: str = None,
        resolution: str = None,
        scene: str = None,
        status: str = None,
        user_data: str = None,
    ):
        # The aspect ratio.
        self.aspect_ratio = aspect_ratio
        # The video duration. Unit: seconds.
        self.duration = duration
        # The error message. This parameter is returned only when the task is in the Failed state.
        self.error_message = error_message
        # The task input.
        self.input = input
        # The task ID.
        self.job_id = job_id
        # The task feature configuration. No configuration is required at this time.
        self.job_parameters = job_parameters
        # The task type.
        self.job_type = job_type
        # The model name.
        self.model = model
        # The number of generated videos.
        self.n = n
        # The generation result. The value is a JSON string that contains the following fields:
        # 
        # Medias: a list of media information (Media objects). The Media object contains the following fields:
        # MediaId: String. The media asset ID.
        # OutputUrl: String. The media URL (with authentication string).
        self.output = output
        # The resolution.
        self.resolution = resolution
        # The scene type. Currently, only general is supported.
        self.scene = scene
        # The task status. Valid values:
        # 
        # - Created: The task is created.
        # - Queuing: The task is queuing.
        # - Executing: The task is being executed.
        # - Finished: The task is completed.
        # - Failed: The task failed.
        self.status = status
        # The user business information.
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

        if self.duration is not None:
            result['Duration'] = self.duration

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

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetYikeStoryboardJobResponseBody(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        job_params: main_models.GetYikeStoryboardJobResponseBodyJobParams = None,
        job_result: main_models.GetYikeStoryboardJobResponseBodyJobResult = None,
        job_status: str = None,
        request_id: str = None,
    ):
        # The storyboard job ID. You can obtain this ID from the response parameters of the [SubmitStoryboardJob](https://help.aliyun.com/document_detail/461964.html) operation.
        self.job_id = job_id
        # A JSON object that contains the parameters for the job. The structure of this object varies based on the AI algorithm.
        self.job_params = job_params
        # The job result.
        self.job_result = job_result
        # The job status. Valid values:
        # 
        # - **Succeeded**: The job completed successfully.
        # 
        # - **Failed**: The job failed to complete.
        # 
        # - **Running**: The job is in progress.
        self.job_status = job_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job_params:
            self.job_params.validate()
        if self.job_result:
            self.job_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_params is not None:
            result['JobParams'] = self.job_params.to_map()

        if self.job_result is not None:
            result['JobResult'] = self.job_result.to_map()

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobParams') is not None:
            temp_model = main_models.GetYikeStoryboardJobResponseBodyJobParams()
            self.job_params = temp_model.from_map(m.get('JobParams'))

        if m.get('JobResult') is not None:
            temp_model = main_models.GetYikeStoryboardJobResponseBodyJobResult()
            self.job_result = temp_model.from_map(m.get('JobResult'))

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetYikeStoryboardJobResponseBodyJobResult(DaraModel):
    def __init__(
        self,
        exception_storyboard_ids: str = None,
        failure_shot_list: str = None,
        output_url: str = None,
        storyboard_info_list: str = None,
        success_storyboard_ids: str = None,
        success_storyboard_list: str = None,
    ):
        # A list of IDs for storyboards that encountered an exception.
        self.exception_storyboard_ids = exception_storyboard_ids
        # A list of shots that failed to generate.
        self.failure_shot_list = failure_shot_list
        # The downloadable OSS URL.
        self.output_url = output_url
        # Detailed information about each storyboard in the job.
        self.storyboard_info_list = storyboard_info_list
        # A comma-separated list of successful storyboard IDs.
        self.success_storyboard_ids = success_storyboard_ids
        # A list of IDs for successful storyboards.
        self.success_storyboard_list = success_storyboard_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_storyboard_ids is not None:
            result['ExceptionStoryboardIds'] = self.exception_storyboard_ids

        if self.failure_shot_list is not None:
            result['FailureShotList'] = self.failure_shot_list

        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        if self.storyboard_info_list is not None:
            result['StoryboardInfoList'] = self.storyboard_info_list

        if self.success_storyboard_ids is not None:
            result['SuccessStoryboardIds'] = self.success_storyboard_ids

        if self.success_storyboard_list is not None:
            result['SuccessStoryboardList'] = self.success_storyboard_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionStoryboardIds') is not None:
            self.exception_storyboard_ids = m.get('ExceptionStoryboardIds')

        if m.get('FailureShotList') is not None:
            self.failure_shot_list = m.get('FailureShotList')

        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        if m.get('StoryboardInfoList') is not None:
            self.storyboard_info_list = m.get('StoryboardInfoList')

        if m.get('SuccessStoryboardIds') is not None:
            self.success_storyboard_ids = m.get('SuccessStoryboardIds')

        if m.get('SuccessStoryboardList') is not None:
            self.success_storyboard_list = m.get('SuccessStoryboardList')

        return self

class GetYikeStoryboardJobResponseBodyJobParams(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        file_url: str = None,
        model_params: str = None,
        narration_voice_id: str = None,
        resolution: str = None,
        shot_prompt_mode: str = None,
        shot_split_mode: str = None,
        source_type: str = None,
        style_id: str = None,
        title: str = None,
        video_model: str = None,
    ):
        # The aspect ratio of the video.
        self.aspect_ratio = aspect_ratio
        # The OSS URL of the file.
        self.file_url = file_url
        # The model parameters.
        self.model_params = model_params
        # The narration voice.
        self.narration_voice_id = narration_voice_id
        # The resolution of the generated video.
        self.resolution = resolution
        # The shot generation mode.
        self.shot_prompt_mode = shot_prompt_mode
        # The shot splitting mode.
        self.shot_split_mode = shot_split_mode
        # The source type.
        self.source_type = source_type
        # The style ID.
        self.style_id = style_id
        # The job title.
        # 
        # \\- Maximum length: 128 bytes.
        # 
        # \\- UTF-8 encoding.
        self.title = title
        # The video model.
        self.video_model = video_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.model_params is not None:
            result['ModelParams'] = self.model_params

        if self.narration_voice_id is not None:
            result['NarrationVoiceId'] = self.narration_voice_id

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.shot_prompt_mode is not None:
            result['ShotPromptMode'] = self.shot_prompt_mode

        if self.shot_split_mode is not None:
            result['ShotSplitMode'] = self.shot_split_mode

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.style_id is not None:
            result['StyleId'] = self.style_id

        if self.title is not None:
            result['Title'] = self.title

        if self.video_model is not None:
            result['VideoModel'] = self.video_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('ModelParams') is not None:
            self.model_params = m.get('ModelParams')

        if m.get('NarrationVoiceId') is not None:
            self.narration_voice_id = m.get('NarrationVoiceId')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('ShotPromptMode') is not None:
            self.shot_prompt_mode = m.get('ShotPromptMode')

        if m.get('ShotSplitMode') is not None:
            self.shot_split_mode = m.get('ShotSplitMode')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StyleId') is not None:
            self.style_id = m.get('StyleId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('VideoModel') is not None:
            self.video_model = m.get('VideoModel')

        return self


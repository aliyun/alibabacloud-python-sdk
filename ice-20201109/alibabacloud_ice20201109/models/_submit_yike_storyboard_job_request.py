# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitYikeStoryboardJobRequest(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        exec_mode: str = None,
        file_url: str = None,
        model_params: str = None,
        narration_voice_id: str = None,
        resolution: str = None,
        shot_prompt_mode: str = None,
        shot_split_mode: str = None,
        skip_failure_shot: bool = None,
        source_type: str = None,
        style_id: str = None,
        title: str = None,
        user_data: str = None,
        video_model: str = None,
    ):
        # The aspect ratio of the output video.
        self.aspect_ratio = aspect_ratio
        # The storyboard generation execution mode.
        # 
        # - `FullPipeline`: Executes the full generation pipeline, including both storyboard creation and shot video generation.
        # 
        # - `StoryboardOnly`: Generates only the storyboard.
        self.exec_mode = exec_mode
        # The OSS address of the file.
        self.file_url = file_url
        # Parameters for the model, in JSON format.
        self.model_params = model_params
        # The narration voice ID.
        self.narration_voice_id = narration_voice_id
        # The resolution of the output video.
        self.resolution = resolution
        # The storyboard shot generation mode.
        self.shot_prompt_mode = shot_prompt_mode
        # The shot split mode.
        self.shot_split_mode = shot_split_mode
        # Specifies whether to skip a failed shot. The default value is `true`.
        self.skip_failure_shot = skip_failure_shot
        # The source type.
        self.source_type = source_type
        # The storyboard style ID.
        self.style_id = style_id
        # The job title. It must be a UTF-8 encoded string of up to 128 bytes. If you do not specify a title, the system generates a default one based on the date.
        self.title = title
        # Custom settings in JSON format. This parameter can contain the following field:
        # 
        # - The `NotifyAddress` field specifies the callback URL that is invoked when the job is complete. Both MNS and HTTP callbacks are supported.
        self.user_data = user_data
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

        if self.exec_mode is not None:
            result['ExecMode'] = self.exec_mode

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

        if self.skip_failure_shot is not None:
            result['SkipFailureShot'] = self.skip_failure_shot

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.style_id is not None:
            result['StyleId'] = self.style_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_model is not None:
            result['VideoModel'] = self.video_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')

        if m.get('ExecMode') is not None:
            self.exec_mode = m.get('ExecMode')

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

        if m.get('SkipFailureShot') is not None:
            self.skip_failure_shot = m.get('SkipFailureShot')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StyleId') is not None:
            self.style_id = m.get('StyleId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoModel') is not None:
            self.video_model = m.get('VideoModel')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitIProductionJobShrinkRequest(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        input_shrink: str = None,
        job_params: str = None,
        model_id: str = None,
        name: str = None,
        output_shrink: str = None,
        schedule_config_shrink: str = None,
        template_id: str = None,
        user_data: str = None,
    ):
        # The name of the algorithm that you want to use for the job. Valid values:
        # 
        # *   **Cover**: This algorithm intelligently generates a thumbnail image for a video.
        # *   **VideoClip**: This algorithm intelligently generates a summary for a video.
        # *   **VideoDelogo**: This algorithm removes logos from a video.
        # *   **VideoDetext**: This algorithm removes captions from a video.
        # *   **CaptionExtraction**: This algorithm extracts captions from a video and generates the caption file.
        # *   **VideoGreenScreenMatting**: This algorithm performs green-screen image matting on a video and generates a new video.
        # *   **FaceBeauty**: This algorithm performs video retouching.
        # *   **VideoH2V**: This algorithm transforms a video from the landscape mode to the portrait mode.
        # *   **MusicSegmentDetect**: This algorithm detects the chorus of a song.
        # *   **AudioBeatDetection**: This algorithm detects rhythms.
        # *   **AudioQualityAssessment**: This algorithm assesses the audio quality.
        # *   **SpeechDenoise**: This algorithm performs noise reduction.
        # *   **AudioMixing**: This algorithm mixes audio streams.
        # 
        # This parameter is required.
        self.function_name = function_name
        # The input file. The file can be an Object Storage Service (OSS) object or a media asset.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The algorithm-specific parameters. The parameters are specified as JSON objects and vary based on the algorithm. For more information, see the "Parameters of JobParams" section of this topic.
        self.job_params = job_params
        self.model_id = model_id
        # The name of the intelligent production job. The name can be up to 100 characters in length.
        self.name = name
        # The output file. The file can be an OSS object or a media asset.
        # 
        # This parameter is required.
        self.output_shrink = output_shrink
        # The scheduling configuration.
        self.schedule_config_shrink = schedule_config_shrink
        # The template ID.
        self.template_id = template_id
        # The user-defined data that is returned in the response. The value can be up to 1,024 bytes in length.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.name is not None:
            result['Name'] = self.name

        if self.output_shrink is not None:
            result['Output'] = self.output_shrink

        if self.schedule_config_shrink is not None:
            result['ScheduleConfig'] = self.schedule_config_shrink

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            self.output_shrink = m.get('Output')

        if m.get('ScheduleConfig') is not None:
            self.schedule_config_shrink = m.get('ScheduleConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self


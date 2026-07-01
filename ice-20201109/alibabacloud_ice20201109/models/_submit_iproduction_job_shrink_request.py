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
        # The name of the algorithm function. Valid values:
        # 
        # - **Cover**: Generates a smart cover.
        # 
        # - **VideoClip**: Creates a video summary.
        # 
        # - **VideoDelogo**: Removes logos from a video.
        # 
        # - **VideoDetext**: Removes text from a video.
        # 
        # - **CaptionExtraction**: Extracts captions from a video.
        # 
        # - **VideoGreenScreenMatting**: Performs green screen keying for a video.
        # 
        # - **FaceBeauty**: Applies beauty filters to faces in a video.
        # 
        # - **VideoH2V**: Converts a horizontal video to a vertical video.
        # 
        # - **MusicSegmentDetect**: Detects chorus segments in music.
        # 
        # - **AudioBeatDetection**: Detects the beat of an audio track.
        # 
        # - **AudioQualityAssessment**: Assesses audio quality.
        # 
        # - **SpeechDenoise**: Reduces noise in speech audio.
        # 
        # - **AudioMixing**: Mixes audio tracks.
        # 
        # - **MusicDemix**: Separates vocals from accompaniment in music.
        # 
        # This parameter is required.
        self.function_name = function_name
        # The input media asset. You can specify an OSS file or a media asset ID.
        # 
        # The requirements for input files vary by algorithm function. For more information, see the supplementary instructions.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The algorithm job parameters, specified as a JSON-formatted string. The content of the JSON object varies by algorithm function. For more information, see the supplementary instructions.
        self.job_params = job_params
        # The ID of the algorithm model. If you do not specify this parameter, the system uses the default model for the selected function. We recommend leaving this parameter empty unless you need to use a specific alternative model.
        # 
        # The following function offers an alternative model:
        # 
        # - `VideoDetext`
        # 
        #   - Set `ModelId` to `algo-video-detext-new` to use an advanced subtitle removal algorithm. This model provides higher quality results but is slower and more expensive than the default model.
        self.model_id = model_id
        # The name of the job, which can be up to 100 characters long.
        self.name = name
        # The output destination. You can specify an OSS file path or a media asset ID.
        # 
        # The output files vary by algorithm function. For more information, see the supplementary instructions.
        # 
        # This parameter is required.
        self.output_shrink = output_shrink
        # The configuration for job scheduling.
        self.schedule_config_shrink = schedule_config_shrink
        # The ID of the template.
        self.template_id = template_id
        # Custom user data. The system passes this data through and returns it as-is in the callback or response. The length cannot exceed 256 characters.
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


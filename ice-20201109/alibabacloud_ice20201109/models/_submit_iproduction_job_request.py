# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitIProductionJobRequest(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        input: main_models.SubmitIProductionJobRequestInput = None,
        job_params: str = None,
        model_id: str = None,
        name: str = None,
        output: main_models.SubmitIProductionJobRequestOutput = None,
        schedule_config: main_models.SubmitIProductionJobRequestScheduleConfig = None,
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
        self.input = input
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
        self.output = output
        # The configuration for job scheduling.
        self.schedule_config = schedule_config
        # The ID of the template.
        self.template_id = template_id
        # Custom user data. The system passes this data through and returns it as-is in the callback or response. The length cannot exceed 256 characters.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.output:
            self.output.validate()
        if self.schedule_config:
            self.schedule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

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
            temp_model = main_models.SubmitIProductionJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            temp_model = main_models.SubmitIProductionJobRequestOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitIProductionJobRequestScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitIProductionJobRequestScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: int = None,
    ):
        # The ID of the pipeline.
        self.pipeline_id = pipeline_id
        # The job priority, which can be an integer from 1 to 10. A smaller value indicates a higher priority.
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class SubmitIProductionJobRequestOutput(DaraModel):
    def __init__(
        self,
        biz: str = None,
        media: str = None,
        output_url: str = None,
        type: str = None,
    ):
        # The service to which the media asset belongs.
        self.biz = biz
        # This parameter is required.
        self.media = media
        # If `Type` is set to `Media`, you can use this parameter to specify the OSS URL for the output file. The bucket must be registered in either IMS or VOD.
        self.output_url = output_url
        # The type of the output media. Valid values:
        # 
        # - `OSS`: An OSS file path.
        # 
        # - `Media`: A media asset ID.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz is not None:
            result['Biz'] = self.biz

        if self.media is not None:
            result['Media'] = self.media

        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitIProductionJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The OSS URL of the input file or the ID of the input media asset.
        # The OSS URL can be in one of the following formats:
        # 
        # 1. `oss://<bucket>/<object>`
        # 
        # 2. `http(s)://<bucket>.oss-<regionId>.aliyuncs.com/<object>`
        #    In these formats, `<bucket>` is the name of an OSS bucket in the same region as your project, and `<object>` is the file path.
        # 
        # This parameter is required.
        self.media = media
        # The type of input media. Valid values:
        # 
        # - `OSS`: An OSS file path.
        # 
        # - `Media`: A media asset ID.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


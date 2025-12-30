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
        self.input = input
        # The algorithm-specific parameters. The parameters are specified as JSON objects and vary based on the algorithm. For more information, see the "Parameters of JobParams" section of this topic.
        self.job_params = job_params
        self.model_id = model_id
        # The name of the intelligent production job. The name can be up to 100 characters in length.
        self.name = name
        # The output file. The file can be an OSS object or a media asset.
        # 
        # This parameter is required.
        self.output = output
        # The scheduling configuration.
        self.schedule_config = schedule_config
        # The template ID.
        self.template_id = template_id
        # The user-defined data that is returned in the response. The value can be up to 1,024 bytes in length.
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
        # The ID of the ApsaraVideo Media Processing (MPS) queue.
        self.pipeline_id = pipeline_id
        # The priority of the job. Valid values: 1 to 10. A smaller value indicates a higher priority.
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
        self.biz = biz
        # The output file. If Type is set to OSS, set this parameter to the path of an OSS object. If Type is set to Media, set this parameter to the ID of a media asset. You can specify the path of an OSS object in one of the following formats:
        # 
        # 1.  oss://bucket/object
        # 2.  http(s)://bucket.oss-[RegionId].aliyuncs.com/object bucket in the path specifies an OSS bucket that resides in the same region as the intelligent production job. object in the path specifies the object path in OSS.
        # 
        # This parameter is required.
        self.media = media
        self.output_url = output_url
        # The media type. Valid values:
        # 
        # *   OSS: OSS object
        # *   Media: media asset
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
        # The input file. The file can be an OSS object or a media asset. You can specify the path of an OSS object in one of the following formats:
        # 
        # 1.  oss://bucket/object
        # 2.  http(s)://bucket.oss-[regionId].aliyuncs.com/object bucket in the path specifies an OSS bucket that resides in the same region as the intelligent production job. object in the path specifies the object path in OSS.
        # 
        # This parameter is required.
        self.media = media
        # The media type. Valid values:
        # 
        # *   OSS: OSS object
        # *   Media: media asset
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitDynamicImageJobRequest(DaraModel):
    def __init__(
        self,
        input: main_models.SubmitDynamicImageJobRequestInput = None,
        name: str = None,
        output: main_models.SubmitDynamicImageJobRequestOutput = None,
        schedule_config: main_models.SubmitDynamicImageJobRequestScheduleConfig = None,
        template_config: main_models.SubmitDynamicImageJobRequestTemplateConfig = None,
        user_data: str = None,
    ):
        # The input of the job.
        # 
        # This parameter is required.
        self.input = input
        # The name of the job.
        self.name = name
        # The output of the job.
        # 
        # This parameter is required.
        self.output = output
        # The scheduling settings.
        self.schedule_config = schedule_config
        # The snapshot template configuration.
        # 
        # This parameter is required.
        self.template_config = template_config
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.output:
            self.output.validate()
        if self.schedule_config:
            self.schedule_config.validate()
        if self.template_config:
            self.template_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = main_models.SubmitDynamicImageJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            temp_model = main_models.SubmitDynamicImageJobRequestOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitDynamicImageJobRequestScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('TemplateConfig') is not None:
            temp_model = main_models.SubmitDynamicImageJobRequestTemplateConfig()
            self.template_config = temp_model.from_map(m.get('TemplateConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitDynamicImageJobRequestTemplateConfig(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitDynamicImageJobRequestTemplateConfigOverwriteParams = None,
        template_id: str = None,
    ):
        # The parameters that are used to overwrite the corresponding parameters.
        self.overwrite_params = overwrite_params
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.overwrite_params:
            self.overwrite_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overwrite_params is not None:
            result['OverwriteParams'] = self.overwrite_params.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverwriteParams') is not None:
            temp_model = main_models.SubmitDynamicImageJobRequestTemplateConfigOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitDynamicImageJobRequestTemplateConfigOverwriteParams(DaraModel):
    def __init__(
        self,
        format: str = None,
        fps: int = None,
        height: int = None,
        long_short_mode: bool = None,
        scan_mode: str = None,
        time_span: main_models.SubmitDynamicImageJobRequestTemplateConfigOverwriteParamsTimeSpan = None,
        width: int = None,
    ):
        # The format of the animated image. Valid values:
        # 
        # *   **gif**
        # *   **webp**
        self.format = format
        # The frame rate. Valid values: [1,60].
        self.fps = fps
        # The height of the animated image. Valid values: [128,4096].
        self.height = height
        # Specifies whether to enable the auto-rotate screen feature. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # Default value: **true**.
        # 
        # >  If this feature is enabled, the width of the output video corresponds to the long side of the input video, which is the height of the input video in portrait mode. The height of the output video corresponds to the short side of the input video, which is the width of the input video in portrait mode.
        self.long_short_mode = long_short_mode
        # The scan mode. Valid values:
        # 
        # *   **interlaced**
        # *   **progressive** This is the default value.
        self.scan_mode = scan_mode
        # The timeline parameters.
        self.time_span = time_span
        # The width of the animated image. Valid values: [128,4096].
        self.width = width

    def validate(self):
        if self.time_span:
            self.time_span.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.long_short_mode is not None:
            result['LongShortMode'] = self.long_short_mode

        if self.scan_mode is not None:
            result['ScanMode'] = self.scan_mode

        if self.time_span is not None:
            result['TimeSpan'] = self.time_span.to_map()

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('LongShortMode') is not None:
            self.long_short_mode = m.get('LongShortMode')

        if m.get('ScanMode') is not None:
            self.scan_mode = m.get('ScanMode')

        if m.get('TimeSpan') is not None:
            temp_model = main_models.SubmitDynamicImageJobRequestTemplateConfigOverwriteParamsTimeSpan()
            self.time_span = temp_model.from_map(m.get('TimeSpan'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitDynamicImageJobRequestTemplateConfigOverwriteParamsTimeSpan(DaraModel):
    def __init__(
        self,
        duration: str = None,
        end: str = None,
        seek: str = None,
    ):
        # The length of the clip.
        # 
        # *   Format: `hh:mm:ss[.SSS]` or `sssss[.SSS]`.
        # *   Valid values: `[00:00:00.000,23:59:59.999]` or `[0.000,86399.999]`.
        self.duration = duration
        # The length of the ending part of the original clip to be cropped out. If you specify this parameter, the Duration parameter becomes invalid.
        # 
        # *   Format: `hh:mm:ss[.SSS]` or `sssss[.SSS]`.
        # *   Valid values: `[00:00:00.000,23:59:59.999]` or `[0.000,86399.999]`.
        self.end = end
        # The start point of the clip.
        # 
        # *   Format: `hh:mm:ss[.SSS]` or `sssss[.SSS]`.
        # *   Valid values: `[00:00:00.000,23:59:59.999]` or `[0.000,86399.999]`.
        self.seek = seek

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end is not None:
            result['End'] = self.end

        if self.seek is not None:
            result['Seek'] = self.seek

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Seek') is not None:
            self.seek = m.get('Seek')

        return self

class SubmitDynamicImageJobRequestScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: int = None,
    ):
        # The ID of the MPS queue to which the job was submitted.
        self.pipeline_id = pipeline_id
        # The priority. Valid values: 1 to 10. Default value: 6. A greater value specifies a higher priority.
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

class SubmitDynamicImageJobRequestOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The output file. The file can be an OSS object or a media asset. The URL of an OSS object can be in one of the following formats:
        # 
        # *   oss://bucket/object
        # *   http(s)://bucket.oss-[regionId].aliyuncs.com/object
        # 
        # In the URL, bucket specifies an OSS bucket that resides in the same region as the job, and object specifies the object URL in OSS.
        # 
        # >  Before you use the OSS bucket in the URL, you must add the bucket on the [Storage Management](https://help.aliyun.com/document_detail/609918.html) page of the IMS console.
        # 
        # This parameter is required.
        self.media = media
        # The type of the output file. Valid values:
        # 
        # 1.  OSS: an OSS object.
        # 2.  Media: a media asset.
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

class SubmitDynamicImageJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The input file. If Type is set to OSS, set this parameter to the URL of an OSS object. If Type is set to Media, set this parameter to the ID of a media asset. The URL of an OSS object can be in one of the following formats:
        # 
        # 1.  oss://bucket/object
        # 2.  http(s)://bucket.oss-[RegionId].aliyuncs.com/object
        # 
        # In the URL, bucket specifies an OSS bucket that resides in the same region as the job, and object specifies the object URL in OSS.
        # 
        # >  Before you use the OSS bucket in the URL, you must add the bucket on the [Storage Management](https://help.aliyun.com/document_detail/609918.html) page of the Intelligent Media Services (IMS) console.
        # 
        # This parameter is required.
        self.media = media
        # The type of the input file. Valid values:
        # 
        # 1.  OSS: an Object Storage Service (OSS) object.
        # 2.  Media: a media asset.
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


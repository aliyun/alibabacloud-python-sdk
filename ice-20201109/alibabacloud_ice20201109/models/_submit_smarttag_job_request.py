# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitSmarttagJobRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_addr: str = None,
        content_type: str = None,
        input: main_models.SubmitSmarttagJobRequestInput = None,
        notify_url: str = None,
        params: str = None,
        schedule_config: main_models.SubmitSmarttagJobRequestScheduleConfig = None,
        template_config: str = None,
        template_id: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The description of the video content can contain Chinese characters, English letters, digits, and hyphens (-). It cannot start with a special character and must not exceed 1 KB.
        self.content = content
        # Deprecated.
        self.content_addr = content_addr
        # Deprecated.
        self.content_type = content_type
        # The input file for the job.
        self.input = input
        # The callback URL. Only HTTP and HTTPS URLs are supported.
        self.notify_url = notify_url
        # Additional request parameters, specified as a JSON string. For example: `{"needAsrData":true, "needOcrData":false}`.
        # 
        # - `needAsrData`: Specifies whether to include the raw Automatic Speech Recognition (ASR) results in the analysis output. The default is `false`.
        # 
        # - `needOcrData`: Specifies whether to include the raw Optical Character Recognition (OCR) results in the analysis output. The default is `false`.
        # 
        # - `needMetaData`: Specifies whether to include metadata in the analysis output. The default is `false`.
        # 
        # - `nlpParams`: A JSON object that specifies the input parameters for the Natural Language Processing (NLP) operator. If left empty, the operator is not used. For details, see the `nlpParams` table below.
        self.params = params
        # The scheduling configurations.
        self.schedule_config = schedule_config
        # Dynamic parameters for the job, which temporarily override or supplement the base template specified by `TemplateId`. The service merges the dynamic and template parameters to generate the final configuration for the current job and validates it before execution.
        # 
        # - Merge rules:
        # 
        # 1. Values in the request override corresponding values in the template.
        # 
        # 2. Fields in the request that do not exist in the template are added to the configuration.
        # 
        # - Currently supported dynamic fields:
        # 
        # 1. `FaceCategoryIds`: A list of face library IDs for recognition, separated by commas (,). You can include both system and custom library IDs.
        # 
        # - Note: These dynamic parameters affect only the current job and do not modify the template itself.
        self.template_config = template_config
        # The ID of the template that specifies the analysis algorithms to use.
        self.template_id = template_id
        # The video title can contain Chinese characters, English letters, digits, and hyphens (-). It cannot start with a special character and must not exceed 256 bytes.
        self.title = title
        # Custom data to include in the callback. If you use Message Service (MNS) for callbacks, this data is included in the message. The maximum length is 1 KB.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.schedule_config:
            self.schedule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_addr is not None:
            result['ContentAddr'] = self.content_addr

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.params is not None:
            result['Params'] = self.params

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentAddr') is not None:
            self.content_addr = m.get('ContentAddr')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Input') is not None:
            temp_model = main_models.SubmitSmarttagJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitSmarttagJobRequestScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitSmarttagJobRequestScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: str = None,
    ):
        # The ID of the pipeline. Pipelines separate business workloads and bind message notifications.
        # 
        # If you do not specify this parameter, the default pipeline is used. The default pipeline has a concurrency of 2. To increase the concurrency, submit a ticket.
        self.pipeline_id = pipeline_id
        # The priority of the job. This feature is not yet implemented. You can leave this parameter empty or specify any value.
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

class SubmitSmarttagJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # - If you set the `Type` parameter to `OSS`, specify the OSS URL of the media file. Example: `OSS://test-bucket/video/202208/test.mp4`.
        # 
        # - If you set the `Type` parameter to `Media`, specify the media ID. Example: `c5c62d8f0361337cab312dce8e77dc6d`.
        # 
        # - If you set the `Type` parameter to `URL`, specify the HTTP or HTTPS URL of the media file. Example: `https://zc-test.oss-cn-shanghai.aliyuncs.com/test/unknowFace.mp4`.
        self.media = media
        # The type of the input media file. Valid values:
        # 
        # - OSS
        # 
        # - Media
        # 
        # - URL
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


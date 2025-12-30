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
        # The video description. The description can contain letters, digits, and hyphens (-) and cannot start with a special character. The description can be up to 1 KB in length.
        self.content = content
        # This parameter is discontinued.
        self.content_addr = content_addr
        # This parameter is discontinued.
        self.content_type = content_type
        # The job input.
        self.input = input
        # The URL for receiving callbacks. Set the value to an HTTP URL or an HTTPS URL.
        self.notify_url = notify_url
        # The additional request parameters. The value is a JSON string. Example: {"needAsrData":true, "needOcrData":false}. The following parameters are supported:
        # 
        # *   needAsrData: specifies whether to query the automatic speech recognition (ASR) data. The value is of the BOOLEAN type. Default value: false. Valid values: true and false.
        # *   needOcrData: specifies whether to query the optical character recognition (OCR) data. The value is of the BOOLEAN type. Default value: false. Valid values: true and false.
        # *   needMetaData: specifies whether to query the metadata. The value is of the BOOLEAN type. Default value: false. Valid values: true and false.
        # *   nlpParams: the input parameters of the natural language processing (NLP) operator. The value is a JSON object. This parameter is empty by default, which indicates that the NLP operator is not used. For more information, see the "nlpParams" section of this topic.
        self.params = params
        # The scheduling configurations.
        self.schedule_config = schedule_config
        self.template_config = template_config
        # The ID of the template that specifies the analysis algorithms. For more information about template operations, see [Configure templates](https://help.aliyun.com/document_detail/445702.html).
        self.template_id = template_id
        # The video title. The title can contain letters, digits, and hyphens (-) and cannot start with a special character. The title can be up to 256 bytes in length.
        self.title = title
        # The data to be passed through Simple Message Queue (SMQ, formerly MNS) during callbacks. The data can be up to 1 KB in length. For more information about how to specify an SMQ queue for receiving callbacks, see UpdatePipeline.
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
        # The ID of the ApsaraVideo Media Processing (MPS) queue to which you want to submit the smart tagging job. The MPS queue is bound to an SMQ queue. This parameter specifies the default MPS queue. By default, an MPS queue can process a maximum of two concurrent smart tagging jobs. To increase the limit, submit a ticket.
        self.pipeline_id = pipeline_id
        # The job priority. This parameter is not implemented. You can leave this parameter empty or enter a random value.
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
        # If Type is set to OSS, specify an OSS path. Example: OSS://test-bucket/video/202208/test.mp4.
        # 
        # If Type is set to Media, specify a media asset ID. Example: c5c62d8f0361337cab312dce8e77dc6d.
        # 
        # If Type is set to URL, specify an HTTP URL. Example: https://zc-test.oss-cn-shanghai.aliyuncs.com/test/unknowFace.mp4.
        self.media = media
        # The media type. Valid values:
        # 
        # *   OSS
        # *   Media
        # *   URL
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


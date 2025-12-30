# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitVideoCognitionJobRequest(DaraModel):
    def __init__(
        self,
        input: main_models.SubmitVideoCognitionJobRequestInput = None,
        params: str = None,
        template_config: str = None,
        template_id: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The media input object.
        self.input = input
        # Additional request parameters, provided as a JSON string. This is used to pass specific settings for various AI analysis modules, such as Natural Language Processing (NLP), shot segmentation, tagging, and action recognition.
        self.params = params
        self.template_config = template_config
        # The ID of the template that specifies the analysis algorithms to be used. For details, see [CreateCustomTemplate](https://help.aliyun.com/zh/ims/developer-reference/api-ice-2020-11-09-createcustomtemplate?spm=a2c4g.11186623.help-menu-193643.d_5_0_3_3_0_0.17b66afamjKySv) and [smart tagging template](https://help.aliyun.com/zh/ims/user-guide/smart-tagging-template?spm=a2c4g.11186623.0.i15).
        self.template_id = template_id
        # The video title. It supports letters, digits, and hyphens (-), and cannot start with a special character. Max length: 256 bytes.
        self.title = title
        # The user-defined data that is passed through and returned as-is in the response. Max length: 1,024 bytes.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.params is not None:
            result['Params'] = self.params

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
        if m.get('Input') is not None:
            temp_model = main_models.SubmitVideoCognitionJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitVideoCognitionJobRequestInput(DaraModel):
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
        # The type of media input. Valid values:
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


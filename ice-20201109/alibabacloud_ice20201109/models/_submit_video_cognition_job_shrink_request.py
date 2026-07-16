# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoCognitionJobShrinkRequest(DaraModel):
    def __init__(
        self,
        input_shrink: str = None,
        params: str = None,
        template_config: str = None,
        template_id: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The input media object.
        self.input_shrink = input_shrink
        # A JSON string containing additional parameters for operators such as natural language processing, shot detection, custom tagging, and action recognition.
        self.params = params
        # The template configuration.
        self.template_config = template_config
        # The ID of the template that specifies the analysis algorithms to use. For more information about managing templates, see [Create Custom Template](https://help.aliyun.com/zh/ims/developer-reference/api-ice-2020-11-09-createcustomtemplate?spm=a2c4g.11186623.help-menu-193643.d_5_0_3_3_0_0.17b66afamjKySv) and [AI-powered tagging template](https://help.aliyun.com/zh/ims/user-guide/smart-tagging-template?spm=a2c4g.11186623.0.i15).
        self.template_id = template_id
        # The title of the video. The title can contain Chinese characters, English letters, digits, and hyphens (-). The title cannot start with a special character and must not exceed 256 bytes in length.
        self.title = title
        # The user-defined data. The service returns this data unmodified in the callback notification. This parameter cannot exceed 1,024 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

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
            self.input_shrink = m.get('Input')

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


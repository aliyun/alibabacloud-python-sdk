# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTextGenerateJobRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        generate_config: str = None,
        title: str = None,
        type: str = None,
        user_data: str = None,
    ):
        # The job description, with a maximum length of 1,024 bytes (UTF-8 encoded).
        self.description = description
        # The generation configuration, in JSON format.
        # 
        # If `Type` is set to `Title` or `MarketingCopy`, specify the following fields:
        # 
        # - `keywords`: The keywords used to generate the title or marketing copy. This parameter is required.
        # 
        # - `textLength`: The target length of the generated text, in characters. Valid values: 5 to 1,000. The actual length of the output is less than or equal to this value. This parameter is required.
        # 
        # - `targetCount`: The number of copy variations to generate. Valid values: 1 to 1,000. This parameter is required.
        # 
        # If `Type` is set to `StoryboardScript`, specify the following field:
        # 
        # - `originText`: The original text used to generate the storyboard script. This parameter is required.
        self.generate_config = generate_config
        # The job title.
        # 
        # \\- The maximum length is 128 bytes.
        # 
        # \\- UTF-8 encoding is required.
        self.title = title
        # The job type.
        # 
        # **Valid values:**
        # 
        # - `MarketingCopy`: Generates marketing copy.
        # 
        # - `Title`: Generates a short video title.
        # 
        # - `StoryboardScript`: Generates a storyboard script from text.
        self.type = type
        # The custom settings in JSON format. The maximum length is 512 bytes. You can use this parameter to specify a [custom callback address](https://help.aliyun.com/document_detail/451631.html).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.generate_config is not None:
            result['GenerateConfig'] = self.generate_config

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GenerateConfig') is not None:
            self.generate_config = m.get('GenerateConfig')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self


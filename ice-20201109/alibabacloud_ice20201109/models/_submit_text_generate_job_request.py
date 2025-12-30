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
        # The job description, which can be up to 1,024 bytes in length and must be encoded in UTF-8.
        self.description = description
        # The text generation configurations, including keywords and the requirements for the word count and number of output copies.
        self.generate_config = generate_config
        # The job title.
        # 
        # The job title can be up to 128 bytes in length.
        # 
        # The value must be encoded in UTF-8.
        self.title = title
        # The job type.
        # 
        # Valid values:
        # 
        # *   MarketingCopy: the marketing copy.
        # *   Title: the short video title.
        self.type = type
        # The user-defined data in the JSON format, which can be up to 512 bytes in length. You can specify a custom callback URL. For more information, see [Configure a callback upon editing completion](https://help.aliyun.com/document_detail/451631.html).
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


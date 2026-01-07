# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class GenerateOutputFormatRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        content: str = None,
        extra_info: str = None,
        tags: List[main_models.GenerateOutputFormatRequestTags] = None,
        task_description: str = None,
    ):
        self.business_type = business_type
        self.content = content
        self.extra_info = extra_info
        # This parameter is required.
        self.tags = tags
        self.task_description = task_description

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['businessType'] = self.business_type

        if self.content is not None:
            result['content'] = self.content

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.task_description is not None:
            result['taskDescription'] = self.task_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GenerateOutputFormatRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')

        return self

class GenerateOutputFormatRequestTags(DaraModel):
    def __init__(
        self,
        tag_define_prompt: str = None,
        tag_name: str = None,
    ):
        self.tag_define_prompt = tag_define_prompt
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_define_prompt is not None:
            result['tagDefinePrompt'] = self.tag_define_prompt

        if self.tag_name is not None:
            result['tagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagDefinePrompt') is not None:
            self.tag_define_prompt = m.get('tagDefinePrompt')

        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')

        return self


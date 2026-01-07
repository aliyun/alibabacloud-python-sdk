# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunTagMiningAnalysisShrinkRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        business_type: str = None,
        content: str = None,
        extra_info: str = None,
        model_id: str = None,
        output_format: str = None,
        tags_shrink: str = None,
        task_description: str = None,
    ):
        self.api_key = api_key
        self.business_type = business_type
        # This parameter is required.
        self.content = content
        self.extra_info = extra_info
        self.model_id = model_id
        self.output_format = output_format
        self.tags_shrink = tags_shrink
        self.task_description = task_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.business_type is not None:
            result['businessType'] = self.business_type

        if self.content is not None:
            result['content'] = self.content

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.output_format is not None:
            result['outputFormat'] = self.output_format

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        if self.task_description is not None:
            result['taskDescription'] = self.task_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')

        return self


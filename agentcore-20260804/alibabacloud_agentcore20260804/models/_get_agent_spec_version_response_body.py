# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetAgentSpecVersionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAgentSpecVersionResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetAgentSpecVersionResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetAgentSpecVersionResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_tags: str = None,
        content: str = None,
        description: str = None,
        name: str = None,
        resource: Dict[str, main_models.DataResourceValue] = None,
    ):
        # The business tags.
        self.biz_tags = biz_tags
        # The content.
        self.content = content
        # The description.
        self.description = description
        # The name.
        self.name = name
        # The resource file mapping.
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tags is not None:
            result['bizTags'] = self.biz_tags

        if self.content is not None:
            result['content'] = self.content

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        result['resource'] = {}
        if self.resource is not None:
            for k1, v1 in self.resource.items():
                result['resource'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizTags') is not None:
            self.biz_tags = m.get('bizTags')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.resource = {}
        if m.get('resource') is not None:
            for k1, v1 in m.get('resource').items():
                temp_model = main_models.DataResourceValue()
                self.resource[k1] = temp_model.from_map(v1)

        return self


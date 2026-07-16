# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePromptShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_tags_shrink: str = None,
        description: str = None,
        labels_shrink: str = None,
        namespace_id: str = None,
        prompt_key: str = None,
    ):
        self.biz_tags_shrink = biz_tags_shrink
        self.description = description
        self.labels_shrink = labels_shrink
        # This parameter is required.
        self.namespace_id = namespace_id
        # This parameter is required.
        self.prompt_key = prompt_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tags_shrink is not None:
            result['BizTags'] = self.biz_tags_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.labels_shrink is not None:
            result['Labels'] = self.labels_shrink

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.prompt_key is not None:
            result['PromptKey'] = self.prompt_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTags') is not None:
            self.biz_tags_shrink = m.get('BizTags')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Labels') is not None:
            self.labels_shrink = m.get('Labels')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PromptKey') is not None:
            self.prompt_key = m.get('PromptKey')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeliveryTasksShrinkRequest(DaraModel):
    def __init__(
        self,
        key_words: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        tag_shrink: str = None,
    ):
        self.key_words = key_words
        self.max_results = max_results
        self.next_token = next_token
        self.resource_group_id = resource_group_id
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_words is not None:
            result['keyWords'] = self.key_words

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyWords') is not None:
            self.key_words = m.get('keyWords')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')

        return self


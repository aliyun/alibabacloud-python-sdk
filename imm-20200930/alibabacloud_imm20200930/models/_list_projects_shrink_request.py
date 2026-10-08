# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProjectsShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prefix: str = None,
        tag_shrink: str = None,
    ):
        # The maximum number of projects to return. Valid values: 0 to 200. If this parameter is not set or is set to 0, the default value is 100.
        self.max_results = max_results
        # The query token. Set the value to the NextToken value returned from the previous API call. The list of projects is returned in lexicographical order starting from the NextToken value. Leave this parameter empty when you call this API operation for the first time.
        self.next_token = next_token
        # The prefix used to filter projects. The length is limited to 0 to 128 characters.
        self.prefix = prefix
        # The tag list.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self


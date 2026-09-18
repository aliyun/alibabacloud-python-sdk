# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGraphSchemasShrinkRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        semantic_tags_shrink: str = None,
        tenant_id: str = None,
    ):
        # The keyword for fuzzy match of component data in the form.
        self.keyword = keyword
        # The semantic tags used for filtering. A graph is retained if any tag matches.
        self.semantic_tags_shrink = semantic_tags_shrink
        # The tenant ID. This is a common parameter. If this parameter is not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.semantic_tags_shrink is not None:
            result['semanticTags'] = self.semantic_tags_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('semanticTags') is not None:
            self.semantic_tags_shrink = m.get('semanticTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


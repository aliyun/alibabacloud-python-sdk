# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeBaseSourceTagsRequest(DaraModel):
    def __init__(
        self,
        source_id: str = None,
        source_tags: str = None,
        tenant_id: str = None,
    ):
        # The unique identifier on the business system side, that is, the business ID.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The resource tags. This is an optional parameter that accepts a JSON string list, such as ["tagA","tagB"].
        self.source_tags = source_tags
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


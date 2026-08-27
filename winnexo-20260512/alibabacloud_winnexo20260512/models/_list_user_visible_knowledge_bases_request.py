# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserVisibleKnowledgeBasesRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        tenant_id: str = None,
    ):
        # The keyword for fuzzy match on knowledge base name or description.
        self.keyword = keyword
        # The tenant ID. This is a common parameter. In winnexo-cli, pass it explicitly with --tenant-id.
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

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSourceRequest(DaraModel):
    def __init__(
        self,
        include_details: bool = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # Specifies whether to return large detail fields (settings / notes / structuredTables / unstructuredDocs). Default value: False. When set to False, only metadata is returned.
        self.include_details = include_details
        # The primary ID of the resource.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The tenant ID to which the task belongs.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_details is not None:
            result['includeDetails'] = self.include_details

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includeDetails') is not None:
            self.include_details = m.get('includeDetails')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


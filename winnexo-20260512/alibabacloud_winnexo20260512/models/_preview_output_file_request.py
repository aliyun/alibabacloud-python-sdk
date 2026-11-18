# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreviewOutputFileRequest(DaraModel):
    def __init__(
        self,
        output_item_id: str = None,
        tenant_id: str = None,
        version_id: str = None,
    ):
        # The output item ID.
        # 
        # This parameter is required.
        self.output_item_id = output_item_id
        # The tenant ID.
        self.tenant_id = tenant_id
        # The version referenced by the alias.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_item_id is not None:
            result['outputItemId'] = self.output_item_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.version_id is not None:
            result['versionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('outputItemId') is not None:
            self.output_item_id = m.get('outputItemId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        return self


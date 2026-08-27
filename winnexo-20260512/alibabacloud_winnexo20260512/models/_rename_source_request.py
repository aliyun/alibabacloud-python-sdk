# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenameSourceRequest(DaraModel):
    def __init__(
        self,
        new_name: str = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # The new name of the data source.
        self.new_name = new_name
        # The data source ID, which is unique within the tenant.
        self.source_id = source_id
        # The tenant ID. This is a common parameter. You can pass this parameter explicitly by using --tenant-id in winnexo-cli.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_name is not None:
            result['newName'] = self.new_name

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newName') is not None:
            self.new_name = m.get('newName')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MTRSOCRServiceRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        image_raw: str = None,
        mask: bool = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.image_raw = image_raw
        self.mask = mask
        self.tenant_id = tenant_id
        # This parameter is required.
        self.type = type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.image_raw is not None:
            result['ImageRaw'] = self.image_raw

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ImageRaw') is not None:
            self.image_raw = m.get('ImageRaw')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self


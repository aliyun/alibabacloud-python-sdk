# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCollaborationGroupOutputItemPreviewRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        item_id: str = None,
        tenant_id: str = None,
    ):
        # The collaboration space ID.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The output detail ID. This ID is obtained from the ref.id of a USER_OUTPUT_ITEM node or the space output list.
        # 
        # This parameter is required.
        self.item_id = item_id
        # The tenant ID. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


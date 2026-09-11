# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevertGraphDraftResourceRequest(DaraModel):
    def __init__(
        self,
        draft_change_id: int = None,
        graph_name: str = None,
        tenant_id: str = None,
    ):
        # The draft change ID (the draftChangeId returned by listGraphDraftResources).
        # 
        # This parameter is required.
        self.draft_change_id = draft_change_id
        # The knowledge graph name.
        self.graph_name = graph_name
        # The tenant ID. This is a common parameter. Pass it explicitly by using --tenant-id in winnexo-cli.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.draft_change_id is not None:
            result['draftChangeId'] = self.draft_change_id

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('draftChangeId') is not None:
            self.draft_change_id = m.get('draftChangeId')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


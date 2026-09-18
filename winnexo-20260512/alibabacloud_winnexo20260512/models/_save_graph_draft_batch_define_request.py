# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveGraphDraftBatchDefineRequest(DaraModel):
    def __init__(
        self,
        draft_change_ids: List[int] = None,
        graph_name: str = None,
        save_mode: str = None,
        tenant_id: str = None,
        yaml_edit: str = None,
    ):
        # The list of draft change IDs.
        self.draft_change_ids = draft_change_ids
        # The graph name.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # The save mode.
        self.save_mode = save_mode
        # The tenant ID.
        self.tenant_id = tenant_id
        # The raw YAML text of the graph schema trimmed by READ permissions, with $ref references retained within the authorized subgraph.
        # 
        # This parameter is required.
        self.yaml_edit = yaml_edit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.draft_change_ids is not None:
            result['draftChangeIds'] = self.draft_change_ids

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.save_mode is not None:
            result['saveMode'] = self.save_mode

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.yaml_edit is not None:
            result['yamlEdit'] = self.yaml_edit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('draftChangeIds') is not None:
            self.draft_change_ids = m.get('draftChangeIds')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('saveMode') is not None:
            self.save_mode = m.get('saveMode')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('yamlEdit') is not None:
            self.yaml_edit = m.get('yamlEdit')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateApprovalProcessShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        match_schemas_shrink: str = None,
        process_name: str = None,
        process_nodes: List[List[str]] = None,
    ):
        self.description = description
        self.match_schemas_shrink = match_schemas_shrink
        # This parameter is required.
        self.process_name = process_name
        # This parameter is required.
        self.process_nodes = process_nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.match_schemas_shrink is not None:
            result['MatchSchemas'] = self.match_schemas_shrink

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_nodes is not None:
            result['ProcessNodes'] = self.process_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MatchSchemas') is not None:
            self.match_schemas_shrink = m.get('MatchSchemas')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessNodes') is not None:
            self.process_nodes = m.get('ProcessNodes')

        return self


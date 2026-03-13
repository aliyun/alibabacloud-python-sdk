# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyExternalNodeStatusUpdateShrinkRequest(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        operation_records_shrink: str = None,
        process_action_result: str = None,
    ):
        # This parameter is required.
        self.node_id = node_id
        self.operation_records_shrink = operation_records_shrink
        # This parameter is required.
        self.process_action_result = process_action_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['node_id'] = self.node_id

        if self.operation_records_shrink is not None:
            result['operation_records'] = self.operation_records_shrink

        if self.process_action_result is not None:
            result['process_action_result'] = self.process_action_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('node_id') is not None:
            self.node_id = m.get('node_id')

        if m.get('operation_records') is not None:
            self.operation_records_shrink = m.get('operation_records')

        if m.get('process_action_result') is not None:
            self.process_action_result = m.get('process_action_result')

        return self


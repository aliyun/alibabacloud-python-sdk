# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDiagnosticTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        ai_job_log_info_shrink: str = None,
        cluster_id: str = None,
        diagnostic_type: str = None,
        node_ids_shrink: str = None,
    ):
        # The log information.
        self.ai_job_log_info_shrink = ai_job_log_info_shrink
        # The cluster ID.
        self.cluster_id = cluster_id
        # The diagnostics type.
        self.diagnostic_type = diagnostic_type
        # The IDs of the nodes.
        self.node_ids_shrink = node_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_job_log_info_shrink is not None:
            result['AiJobLogInfo'] = self.ai_job_log_info_shrink

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.diagnostic_type is not None:
            result['DiagnosticType'] = self.diagnostic_type

        if self.node_ids_shrink is not None:
            result['NodeIds'] = self.node_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiJobLogInfo') is not None:
            self.ai_job_log_info_shrink = m.get('AiJobLogInfo')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DiagnosticType') is not None:
            self.diagnostic_type = m.get('DiagnosticType')

        if m.get('NodeIds') is not None:
            self.node_ids_shrink = m.get('NodeIds')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillRunRequest(DaraModel):
    def __init__(
        self,
        include_logs: bool = None,
        run_id: str = None,
        tenant_id: str = None,
    ):
        # Specifies whether to include execution logs. Default value: false. Enable this parameter only for troubleshooting.
        self.include_logs = include_logs
        # The evaluation run ID.
        # 
        # This parameter is required.
        self.run_id = run_id
        # The tenant ID to which the task belongs.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_logs is not None:
            result['includeLogs'] = self.include_logs

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includeLogs') is not None:
            self.include_logs = m.get('includeLogs')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


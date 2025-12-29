# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetClusterAuditProjectResponseBody(DaraModel):
    def __init__(
        self,
        audit_enabled: bool = None,
        sls_project_name: str = None,
    ):
        # Indicates whether the cluster auditing feature is enabled for the cluster. 
        # 
        # * `true`: The cluster auditing feature is enabled for the cluster. 
        # * `false`: The cluster auditing feature is disabled for the cluster.
        self.audit_enabled = audit_enabled
        # The SLS project in which the audit logs of the API server are stored.
        self.sls_project_name = sls_project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_enabled is not None:
            result['audit_enabled'] = self.audit_enabled

        if self.sls_project_name is not None:
            result['sls_project_name'] = self.sls_project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audit_enabled') is not None:
            self.audit_enabled = m.get('audit_enabled')

        if m.get('sls_project_name') is not None:
            self.sls_project_name = m.get('sls_project_name')

        return self


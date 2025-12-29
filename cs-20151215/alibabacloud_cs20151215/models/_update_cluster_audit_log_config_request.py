# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateClusterAuditLogConfigRequest(DaraModel):
    def __init__(
        self,
        disable: bool = None,
        sls_project_name: str = None,
    ):
        # Enable or disable audit logging.
        # 
        # *   false: enables audit logging or updates the audit logging configurations.
        # *   true: disables audit logging.
        self.disable = disable
        # The [Simple Log Service project](https://help.aliyun.com/document_detail/48873.html) to which the [Logstore](https://help.aliyun.com/document_detail/48873.html) storing the cluster audit logs belongs.
        # 
        # *   Default value: k8s-log-{clusterid}.
        # *   After the cluster audit log feature is enabled, a Logstore is created in the specified Simple Log Service project to store cluster audit logs.
        # *   If you want to change the project after audit logging is enabled for the cluster, you can use this parameter to specify another project. You can perform this operation only in ACK managed clusters.
        self.sls_project_name = sls_project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable is not None:
            result['disable'] = self.disable

        if self.sls_project_name is not None:
            result['sls_project_name'] = self.sls_project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disable') is not None:
            self.disable = m.get('disable')

        if m.get('sls_project_name') is not None:
            self.sls_project_name = m.get('sls_project_name')

        return self


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
        # Specifies whether to disable the cluster audit log feature. Valid values:
        # - false: enables the audit log feature or updates the audit log configuration.
        # 
        # - true: disables the audit log feature.
        self.disable = disable
        # The [SLS Project](https://help.aliyun.com/document_detail/48873.html) that contains the [Logstore](https://help.aliyun.com/document_detail/48874.html) for cluster audit logs.
        # 
        # - Default value: k8s-log-{clusterid}.
        # 
        # - After you enable the cluster audit log feature, a Logstore for cluster audit logs is created in the specified SLS Project.
        # 
        # - If you need to change the SLS Project after enabling the cluster audit log feature, use this parameter to specify a new SLS Project. Only ACK managed clusters support changing the SLS Project.
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


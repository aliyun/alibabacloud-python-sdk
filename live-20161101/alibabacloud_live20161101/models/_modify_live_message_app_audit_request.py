# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLiveMessageAppAuditRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        audit_type: int = None,
        audit_url: str = None,
        data_center: str = None,
    ):
        # The ID of the interactive messaging application to modify.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The security audit method. Valid values:
        # - 0: No security audit.
        # - 1: Built-in security audit.
        # - 2: Custom security audit.
        self.audit_type = audit_type
        # The security audit URL required when custom security audit is used (AuditType=2). The URL must start with http:// or https://, must not contain private IP addresses, and must not include port numbers.
        self.audit_url = audit_url
        # The data center. This value must be the same as the data center specified in [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html). Valid values: cn-shanghai (Shanghai) and ap-southeast-1 (Singapore).
        self.data_center = data_center

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.audit_type is not None:
            result['AuditType'] = self.audit_type

        if self.audit_url is not None:
            result['AuditUrl'] = self.audit_url

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AuditType') is not None:
            self.audit_type = m.get('AuditType')

        if m.get('AuditUrl') is not None:
            self.audit_url = m.get('AuditUrl')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        return self


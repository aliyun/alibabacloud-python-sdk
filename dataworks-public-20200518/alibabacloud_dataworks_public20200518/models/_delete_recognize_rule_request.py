# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRecognizeRuleRequest(DaraModel):
    def __init__(
        self,
        sensitive_id: str = None,
        tenant_id: str = None,
    ):
        # The ID of the sensitive field. You can call the [QuerySensNodeInfo](https://help.aliyun.com/document_detail/2747189.html) operation to query the ID.
        # 
        # This parameter is required.
        self.sensitive_id = sensitive_id
        # The tenant ID. To obtain the tenant ID, perform the following steps: Log on to the [DataWorks console](https://workbench.data.aliyun.com/console). Find your workspace and go to the DataStudio page. On the DataStudio page, click the logon username in the upper-right corner and click User Info in the Menu section.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sensitive_id is not None:
            result['SensitiveId'] = self.sensitive_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SensitiveId') is not None:
            self.sensitive_id = m.get('SensitiveId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self


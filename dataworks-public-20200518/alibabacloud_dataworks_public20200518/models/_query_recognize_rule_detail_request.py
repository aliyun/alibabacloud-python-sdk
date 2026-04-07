# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRecognizeRuleDetailRequest(DaraModel):
    def __init__(
        self,
        sensitive_name: str = None,
        tenant_id: str = None,
    ):
        # The name of the sensitive field. To obtain the name of the sensitive field, call the [QuerySensNodeInfo](https://help.aliyun.com/document_detail/2747189.html) operation or log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Data Category and Sensitivity Level page.
        # 
        # This parameter is required.
        self.sensitive_name = sensitive_name
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
        if self.sensitive_name is not None:
            result['SensitiveName'] = self.sensitive_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SensitiveName') is not None:
            self.sensitive_name = m.get('SensitiveName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self


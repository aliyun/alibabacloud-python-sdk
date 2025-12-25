# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSensitivityLevelRequest(DaraModel):
    def __init__(
        self,
        template_id: int = None,
        template_type: str = None,
        tid: int = None,
    ):
        # The ID of the classification template. You can call the [ListClassificationTemplates](https://help.aliyun.com/document_detail/460613.html) operation to query the ID of the classification template.
        self.template_id = template_id
        # The type of the classification template. You can call the [ListClassificationTemplates](https://help.aliyun.com/document_detail/460613.html) operation to query the type of the classification template.
        # 
        # Valid values:
        # 
        # *   USER_DEFINE: a custom template.
        # *   INNER: a built-in template.
        self.template_type = template_type
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) in the topic "Manage DMS tenants."
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self


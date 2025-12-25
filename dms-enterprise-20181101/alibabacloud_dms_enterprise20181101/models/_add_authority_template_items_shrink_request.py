# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAuthorityTemplateItemsShrinkRequest(DaraModel):
    def __init__(
        self,
        items_shrink: str = None,
        template_id: int = None,
        tid: int = None,
    ):
        # The resources that you want to add to the permission template.
        # 
        # This parameter is required.
        self.items_shrink = items_shrink
        # The ID of the permission template. You can call the [CreateAuthorityTemplate](https://help.aliyun.com/document_detail/600705.html) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The ID of the tenant.
        # 
        # > To view the tenant ID, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items_shrink is not None:
            result['Items'] = self.items_shrink

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items_shrink = m.get('Items')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self


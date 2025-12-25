# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAuthorityTemplateRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        template_id: int = None,
        tid: int = None,
    ):
        # The description of the permission template.
        # 
        # >  You must specify the Name or Description parameter. Otherwise, the API call fails.
        # 
        # This parameter is required.
        self.description = description
        # The name of the permission template.
        # 
        # >  You must specify the Name or Description parameter. Otherwise, the API call fails.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the permission template.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self


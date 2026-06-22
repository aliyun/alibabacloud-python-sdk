# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiTemplatesDTO(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        content: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        operator_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        template_id: str = None,
        template_name: str = None,
        user_id: str = None,
    ):
        self.api_name = api_name
        self.content = content
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.operator_id = operator_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.status = status
        self.template_id = template_id
        self.template_name = template_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.content is not None:
            result['Content'] = self.content

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self


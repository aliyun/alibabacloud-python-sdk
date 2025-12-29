# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTemplateRequest(DaraModel):
    def __init__(
        self,
        auto_delete_executions: bool = None,
        region_id: str = None,
        template_name: str = None,
    ):
        # Specifies whether to delete the related executions when a template is deleted.
        self.auto_delete_executions = auto_delete_executions
        # The region ID.
        self.region_id = region_id
        # The name of the template. The name can be 1 to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (_). It cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        # 
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_delete_executions is not None:
            result['AutoDeleteExecutions'] = self.auto_delete_executions

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDeleteExecutions') is not None:
            self.auto_delete_executions = m.get('AutoDeleteExecutions')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self


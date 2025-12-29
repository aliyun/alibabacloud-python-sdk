# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateExecutionPolicyRequest(DaraModel):
    def __init__(
        self,
        ram_role: str = None,
        region_id: str = None,
        template_content: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The RAM role.
        self.ram_role = ram_role
        # The ID of the region.
        self.region_id = region_id
        # The content of the template in the JSON or YAML format. This parameter is the same as the Content parameter that you can specify when you call the CreateTemplate operation. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_content = template_content
        # The name of the template.
        self.template_name = template_name
        # The version of the template. The default value is the latest version of the template.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self


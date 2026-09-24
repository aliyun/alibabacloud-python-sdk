# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTemplateBaseInfoRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_name: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # The template description.
        self.description = description
        # The instance name.
        self.instance_name = instance_name
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self


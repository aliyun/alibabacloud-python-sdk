# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAITemplateRequest(DaraModel):
    def __init__(
        self,
        template_config: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The detailed configurations of the AI template. The value must be a JSON string. For more information, see [AITemplateConfig](~~89863#title-vd3-499-o36~~).
        # 
        # This parameter is required.
        self.template_config = template_config
        # The name of the AI template. The name can be up to 128 bytes in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The type of the AI template. Valid values:
        # 
        # *   **AIMediaAudit**: automated review
        # *   **AIImage**: smart thumbnail
        # 
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self


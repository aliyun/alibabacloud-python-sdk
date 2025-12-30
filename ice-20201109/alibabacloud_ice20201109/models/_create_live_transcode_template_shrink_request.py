# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLiveTranscodeTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        template_config_shrink: str = None,
        type: str = None,
    ):
        # The name of the template.
        # 
        # This parameter is required.
        self.name = name
        # The configuration of the template.
        self.template_config_shrink = template_config_shrink
        # The type of the template. Valid values:
        # 
        # *   normal
        # *   narrow-band
        # *   audio-only
        # *   origin
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.template_config_shrink is not None:
            result['TemplateConfig'] = self.template_config_shrink

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateConfig') is not None:
            self.template_config_shrink = m.get('TemplateConfig')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


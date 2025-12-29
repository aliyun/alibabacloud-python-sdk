# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddMessageTemplateRequest(DaraModel):
    def __init__(
        self,
        template_detail: str = None,
        template_name: str = None,
    ):
        # This parameter is required.
        self.template_detail = template_detail
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_detail is not None:
            result['TemplateDetail'] = self.template_detail

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateDetail') is not None:
            self.template_detail = m.get('TemplateDetail')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self


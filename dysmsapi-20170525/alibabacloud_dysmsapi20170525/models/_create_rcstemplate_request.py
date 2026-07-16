# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRCSTemplateRequest(DaraModel):
    def __init__(
        self,
        related_sign_names: str = None,
        template_content: str = None,
        template_format: str = None,
        template_menu: str = None,
        template_name: str = None,
        template_rule: str = None,
        template_type: int = None,
    ):
        # This parameter is required.
        self.related_sign_names = related_sign_names
        # This parameter is required.
        self.template_content = template_content
        # This parameter is required.
        self.template_format = template_format
        self.template_menu = template_menu
        # This parameter is required.
        self.template_name = template_name
        self.template_rule = template_rule
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.related_sign_names is not None:
            result['RelatedSignNames'] = self.related_sign_names

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format

        if self.template_menu is not None:
            result['TemplateMenu'] = self.template_menu

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_rule is not None:
            result['TemplateRule'] = self.template_rule

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelatedSignNames') is not None:
            self.related_sign_names = m.get('RelatedSignNames')

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')

        if m.get('TemplateMenu') is not None:
            self.template_menu = m.get('TemplateMenu')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateRule') is not None:
            self.template_rule = m.get('TemplateRule')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self


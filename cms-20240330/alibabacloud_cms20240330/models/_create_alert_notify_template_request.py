# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateAlertNotifyTemplateRequest(DaraModel):
    def __init__(
        self,
        alert_notify_template_id: str = None,
        alert_notify_template_name: str = None,
        program_lang: str = None,
        templates: Dict[str, dict] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.alert_notify_template_id = alert_notify_template_id
        self.alert_notify_template_name = alert_notify_template_name
        self.program_lang = program_lang
        self.templates = templates
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_notify_template_id is not None:
            result['alertNotifyTemplateId'] = self.alert_notify_template_id

        if self.alert_notify_template_name is not None:
            result['alertNotifyTemplateName'] = self.alert_notify_template_name

        if self.program_lang is not None:
            result['programLang'] = self.program_lang

        if self.templates is not None:
            result['templates'] = self.templates

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertNotifyTemplateId') is not None:
            self.alert_notify_template_id = m.get('alertNotifyTemplateId')

        if m.get('alertNotifyTemplateName') is not None:
            self.alert_notify_template_name = m.get('alertNotifyTemplateName')

        if m.get('programLang') is not None:
            self.program_lang = m.get('programLang')

        if m.get('templates') is not None:
            self.templates = m.get('templates')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self


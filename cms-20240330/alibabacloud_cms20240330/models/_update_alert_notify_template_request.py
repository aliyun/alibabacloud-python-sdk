# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class UpdateAlertNotifyTemplateRequest(DaraModel):
    def __init__(
        self,
        alert_notify_template_name: str = None,
        templates: Dict[str, dict] = None,
    ):
        self.alert_notify_template_name = alert_notify_template_name
        self.templates = templates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_notify_template_name is not None:
            result['alertNotifyTemplateName'] = self.alert_notify_template_name

        if self.templates is not None:
            result['templates'] = self.templates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertNotifyTemplateName') is not None:
            self.alert_notify_template_name = m.get('alertNotifyTemplateName')

        if m.get('templates') is not None:
            self.templates = m.get('templates')

        return self


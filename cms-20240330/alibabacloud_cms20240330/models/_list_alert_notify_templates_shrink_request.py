# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertNotifyTemplatesShrinkRequest(DaraModel):
    def __init__(
        self,
        alert_notify_template_ids_shrink: str = None,
        alert_notify_template_name: str = None,
        page_number: int = None,
        page_size: int = None,
        program_lang: str = None,
        type: str = None,
    ):
        self.alert_notify_template_ids_shrink = alert_notify_template_ids_shrink
        self.alert_notify_template_name = alert_notify_template_name
        self.page_number = page_number
        self.page_size = page_size
        self.program_lang = program_lang
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_notify_template_ids_shrink is not None:
            result['alertNotifyTemplateIds'] = self.alert_notify_template_ids_shrink

        if self.alert_notify_template_name is not None:
            result['alertNotifyTemplateName'] = self.alert_notify_template_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.program_lang is not None:
            result['programLang'] = self.program_lang

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertNotifyTemplateIds') is not None:
            self.alert_notify_template_ids_shrink = m.get('alertNotifyTemplateIds')

        if m.get('alertNotifyTemplateName') is not None:
            self.alert_notify_template_name = m.get('alertNotifyTemplateName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('programLang') is not None:
            self.program_lang = m.get('programLang')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self


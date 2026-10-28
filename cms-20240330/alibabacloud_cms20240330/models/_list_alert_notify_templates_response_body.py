# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListAlertNotifyTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        alert_notify_templates: List[main_models.ListAlertNotifyTemplatesResponseBodyAlertNotifyTemplates] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The list of notification templates.
        self.alert_notify_templates = alert_notify_templates
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total = total

    def validate(self):
        if self.alert_notify_templates:
            for v1 in self.alert_notify_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['alertNotifyTemplates'] = []
        if self.alert_notify_templates is not None:
            for k1 in self.alert_notify_templates:
                result['alertNotifyTemplates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_notify_templates = []
        if m.get('alertNotifyTemplates') is not None:
            for k1 in m.get('alertNotifyTemplates'):
                temp_model = main_models.ListAlertNotifyTemplatesResponseBodyAlertNotifyTemplates()
                self.alert_notify_templates.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAlertNotifyTemplatesResponseBodyAlertNotifyTemplates(DaraModel):
    def __init__(
        self,
        alert_notify_template_id: str = None,
        alert_notify_template_name: str = None,
        program_lang: str = None,
        templates: Dict[str, dict] = None,
        type: str = None,
    ):
        # The notification template ID.
        self.alert_notify_template_id = alert_notify_template_id
        # The notification template name.
        self.alert_notify_template_name = alert_notify_template_name
        # The template syntax type. The current template syntax is fixed to GO and uses the Go template syntax.
        self.program_lang = program_lang
        # The multilingual notification templates. The key is the language code: zh (Chinese) or en (English). The value is the template configuration object for the language. When a notification is sent, the corresponding template is selected based on the recipient\\"s language. The content format varies by type: Markdown for DING, WEIXIN, and FEISHU; HTML for EMAIL; plain text for SMS, CALL, and SLACK; and JSON for CUSTOM.
        self.templates = templates
        # The notification channel type. Valid values:
        # - DING
        # - WEIXIN
        # - FEISHU
        # - SLACK
        # - CUSTOM
        # - TEAMS
        # - SMS
        # - EMAIL
        # - CALL
        # - PAGER_DUTY
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


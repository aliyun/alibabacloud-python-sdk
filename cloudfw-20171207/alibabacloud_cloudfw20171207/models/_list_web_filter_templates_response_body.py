# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ListWebFilterTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        web_filter_templates: List[main_models.ListWebFilterTemplatesResponseBodyWebFilterTemplates] = None,
    ):
        # The current page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of web filtering templates that meet the filter conditions.
        self.total_count = total_count
        # The list of web filtering templates.
        self.web_filter_templates = web_filter_templates

    def validate(self):
        if self.web_filter_templates:
            for v1 in self.web_filter_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WebFilterTemplates'] = []
        if self.web_filter_templates is not None:
            for k1 in self.web_filter_templates:
                result['WebFilterTemplates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.web_filter_templates = []
        if m.get('WebFilterTemplates') is not None:
            for k1 in m.get('WebFilterTemplates'):
                temp_model = main_models.ListWebFilterTemplatesResponseBodyWebFilterTemplates()
                self.web_filter_templates.append(temp_model.from_map(k1))

        return self

class ListWebFilterTemplatesResponseBodyWebFilterTemplates(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        name: str = None,
        rule_action_statistics: main_models.ListWebFilterTemplatesResponseBodyWebFilterTemplatesRuleActionStatistics = None,
        status: str = None,
        web_filter_template_id: str = None,
    ):
        # The creation time of the web filtering template. The value is a UNIX timestamp in seconds.
        self.create_time = create_time
        # The description of the web filtering template.
        self.description = description
        # The name of the web filtering template.
        self.name = name
        # The statistics on the number of web filtering rules in the template categorized by action.
        self.rule_action_statistics = rule_action_statistics
        # The status of the web filtering template. Valid values:
        # - **Enable**: Enabled.
        # - **Disable**: Disabled.
        self.status = status
        # The ID of the web filtering template.
        self.web_filter_template_id = web_filter_template_id

    def validate(self):
        if self.rule_action_statistics:
            self.rule_action_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_action_statistics is not None:
            result['RuleActionStatistics'] = self.rule_action_statistics.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.web_filter_template_id is not None:
            result['WebFilterTemplateId'] = self.web_filter_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleActionStatistics') is not None:
            temp_model = main_models.ListWebFilterTemplatesResponseBodyWebFilterTemplatesRuleActionStatistics()
            self.rule_action_statistics = temp_model.from_map(m.get('RuleActionStatistics'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WebFilterTemplateId') is not None:
            self.web_filter_template_id = m.get('WebFilterTemplateId')

        return self

class ListWebFilterTemplatesResponseBodyWebFilterTemplatesRuleActionStatistics(DaraModel):
    def __init__(
        self,
        alert: int = None,
        allow: int = None,
        deny: int = None,
    ):
        # The number of web filtering rules whose action is Alert in the template.
        self.alert = alert
        # The number of web filtering rules whose action is Allow in the template.
        self.allow = allow
        # The number of web filtering rules whose action is Deny in the template.
        self.deny = deny

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert is not None:
            result['Alert'] = self.alert

        if self.allow is not None:
            result['Allow'] = self.allow

        if self.deny is not None:
            result['Deny'] = self.deny

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alert') is not None:
            self.alert = m.get('Alert')

        if m.get('Allow') is not None:
            self.allow = m.get('Allow')

        if m.get('Deny') is not None:
            self.deny = m.get('Deny')

        return self


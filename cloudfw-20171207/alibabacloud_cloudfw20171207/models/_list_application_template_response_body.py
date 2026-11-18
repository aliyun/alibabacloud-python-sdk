# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ListApplicationTemplateResponseBody(DaraModel):
    def __init__(
        self,
        application_templates: List[main_models.ListApplicationTemplateResponseBodyApplicationTemplates] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of application templates.
        self.application_templates = application_templates
        # The current page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of application templates that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.application_templates:
            for v1 in self.application_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationTemplates'] = []
        if self.application_templates is not None:
            for k1 in self.application_templates:
                result['ApplicationTemplates'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_templates = []
        if m.get('ApplicationTemplates') is not None:
            for k1 in m.get('ApplicationTemplates'):
                temp_model = main_models.ListApplicationTemplateResponseBodyApplicationTemplates()
                self.application_templates.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationTemplateResponseBodyApplicationTemplates(DaraModel):
    def __init__(
        self,
        application_template_id: str = None,
        application_template_name: str = None,
        built_in_application_action_statistics: main_models.ListApplicationTemplateResponseBodyApplicationTemplatesBuiltInApplicationActionStatistics = None,
        built_in_application_status: str = None,
        create_time: int = None,
        custom_rule_count: int = None,
        custom_rule_status: str = None,
        description: str = None,
        template_status: str = None,
        unknown_action: str = None,
        update_time: int = None,
    ):
        # The application template ID.
        self.application_template_id = application_template_id
        # The name of the application template.
        self.application_template_name = application_template_name
        # The statistics on the number of built-in applications in the template, categorized by the final effective action.
        self.built_in_application_action_statistics = built_in_application_action_statistics
        # The switch status of built-in application control. Valid values:
        # - **Enable**: enabled
        # - **Disable**: disabled
        self.built_in_application_status = built_in_application_status
        # The creation time of the application template. The value is a UNIX timestamp in seconds.
        self.create_time = create_time
        # The number of custom application rules under the template.
        self.custom_rule_count = custom_rule_count
        # The switch status of custom application rules. Valid values:
        # - **Enable**: enabled
        # - **Disable**: disabled
        self.custom_rule_status = custom_rule_status
        # The description of the application template.
        self.description = description
        # The master switch status of the application template. Valid values:
        # - **Enable**: enabled
        # - **Disable**: disabled
        self.template_status = template_status
        # The action for unrecognized applications. Valid values:
        # - **Allow**: allow
        # - **Alert**: monitor
        # - **Deny**: block
        self.unknown_action = unknown_action
        # The last modification time of the application template. The value is a UNIX timestamp in seconds.
        self.update_time = update_time

    def validate(self):
        if self.built_in_application_action_statistics:
            self.built_in_application_action_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        if self.application_template_name is not None:
            result['ApplicationTemplateName'] = self.application_template_name

        if self.built_in_application_action_statistics is not None:
            result['BuiltInApplicationActionStatistics'] = self.built_in_application_action_statistics.to_map()

        if self.built_in_application_status is not None:
            result['BuiltInApplicationStatus'] = self.built_in_application_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_rule_count is not None:
            result['CustomRuleCount'] = self.custom_rule_count

        if self.custom_rule_status is not None:
            result['CustomRuleStatus'] = self.custom_rule_status

        if self.description is not None:
            result['Description'] = self.description

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.unknown_action is not None:
            result['UnknownAction'] = self.unknown_action

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        if m.get('ApplicationTemplateName') is not None:
            self.application_template_name = m.get('ApplicationTemplateName')

        if m.get('BuiltInApplicationActionStatistics') is not None:
            temp_model = main_models.ListApplicationTemplateResponseBodyApplicationTemplatesBuiltInApplicationActionStatistics()
            self.built_in_application_action_statistics = temp_model.from_map(m.get('BuiltInApplicationActionStatistics'))

        if m.get('BuiltInApplicationStatus') is not None:
            self.built_in_application_status = m.get('BuiltInApplicationStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomRuleCount') is not None:
            self.custom_rule_count = m.get('CustomRuleCount')

        if m.get('CustomRuleStatus') is not None:
            self.custom_rule_status = m.get('CustomRuleStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('UnknownAction') is not None:
            self.unknown_action = m.get('UnknownAction')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListApplicationTemplateResponseBodyApplicationTemplatesBuiltInApplicationActionStatistics(DaraModel):
    def __init__(
        self,
        alert_application_count: int = None,
        allow_application_count: int = None,
        deny_application_count: int = None,
    ):
        # The number of built-in applications whose final effective action is Alert.
        self.alert_application_count = alert_application_count
        # The number of built-in applications whose final effective action is Allow.
        self.allow_application_count = allow_application_count
        # The number of built-in applications whose final effective action is Deny.
        self.deny_application_count = deny_application_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_application_count is not None:
            result['AlertApplicationCount'] = self.alert_application_count

        if self.allow_application_count is not None:
            result['AllowApplicationCount'] = self.allow_application_count

        if self.deny_application_count is not None:
            result['DenyApplicationCount'] = self.deny_application_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertApplicationCount') is not None:
            self.alert_application_count = m.get('AlertApplicationCount')

        if m.get('AllowApplicationCount') is not None:
            self.allow_application_count = m.get('AllowApplicationCount')

        if m.get('DenyApplicationCount') is not None:
            self.deny_application_count = m.get('DenyApplicationCount')

        return self


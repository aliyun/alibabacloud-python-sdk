# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApplicationTemplateRequest(DaraModel):
    def __init__(
        self,
        application_template_ids: List[str] = None,
        application_template_name: str = None,
        built_in_application_status: str = None,
        custom_rule_status: str = None,
        description: str = None,
        page_no: int = None,
        page_size: int = None,
        template_status: str = None,
        unknown_action: str = None,
    ):
        # The list of application template IDs for batch exact matching.
        self.application_template_ids = application_template_ids
        # The application template name for fuzzy matching.
        self.application_template_name = application_template_name
        # The switch status of built-in application control for exact matching. Valid values:
        # - **Enable**: enabled
        # - **Disable**: disabled
        self.built_in_application_status = built_in_application_status
        # The switch status of custom application rules for exact matching. Valid values:
        # - **Enable**: enabled
        # - **Disable**: disabled
        self.custom_rule_status = custom_rule_status
        # The description of the application template for fuzzy matching.
        self.description = description
        # The page number. Pages start from 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. The value must be greater than or equal to 1. Default value: 10.
        self.page_size = page_size
        # The master switch status of the application template for exact matching. Valid values:
        # - **Enable**: enabled
        # - **Disable**: disabled
        self.template_status = template_status
        # The action for unrecognized applications for exact matching. Valid values:
        # - **Allow**: allow
        # - **Alert**: monitor
        # - **Deny**: block
        self.unknown_action = unknown_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_template_ids is not None:
            result['ApplicationTemplateIds'] = self.application_template_ids

        if self.application_template_name is not None:
            result['ApplicationTemplateName'] = self.application_template_name

        if self.built_in_application_status is not None:
            result['BuiltInApplicationStatus'] = self.built_in_application_status

        if self.custom_rule_status is not None:
            result['CustomRuleStatus'] = self.custom_rule_status

        if self.description is not None:
            result['Description'] = self.description

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.unknown_action is not None:
            result['UnknownAction'] = self.unknown_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTemplateIds') is not None:
            self.application_template_ids = m.get('ApplicationTemplateIds')

        if m.get('ApplicationTemplateName') is not None:
            self.application_template_name = m.get('ApplicationTemplateName')

        if m.get('BuiltInApplicationStatus') is not None:
            self.built_in_application_status = m.get('BuiltInApplicationStatus')

        if m.get('CustomRuleStatus') is not None:
            self.custom_rule_status = m.get('CustomRuleStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('UnknownAction') is not None:
            self.unknown_action = m.get('UnknownAction')

        return self


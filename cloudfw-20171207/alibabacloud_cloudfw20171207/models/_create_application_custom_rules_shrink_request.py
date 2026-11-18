# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationCustomRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        application_template_id: str = None,
        rules_shrink: str = None,
    ):
        # The ID of the application template to which the custom rules belong. The template must exist within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.application_template_id = application_template_id
        # The list of custom rules for the application. You can specify up to 100 rules at a time, and the total number of rules in the template after creation must not exceed 100.
        # 
        # This parameter is required.
        self.rules_shrink = rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        return self


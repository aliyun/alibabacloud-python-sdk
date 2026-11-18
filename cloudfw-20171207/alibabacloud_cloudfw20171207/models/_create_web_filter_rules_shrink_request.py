# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWebFilterRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        rules_shrink: str = None,
        web_filter_template_id: str = None,
    ):
        # The list of web filtering rules. You can specify a maximum of 100 rules at a time, and the total number of rules in the template after creation must not exceed 100.
        # 
        # This parameter is required.
        self.rules_shrink = rules_shrink
        # The ID of the web filtering template to which the web filtering rules belong. The template must exist within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.web_filter_template_id = web_filter_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

        if self.web_filter_template_id is not None:
            result['WebFilterTemplateId'] = self.web_filter_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        if m.get('WebFilterTemplateId') is not None:
            self.web_filter_template_id = m.get('WebFilterTemplateId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetAegisContainerPluginRuleResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAegisContainerPluginRuleResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetAegisContainerPluginRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAegisContainerPluginRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        mode: int = None,
        rule_description: str = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_template_id: str = None,
        rule_template_name: str = None,
        selected_policy: List[str] = None,
        switch_id: str = None,
        white_images: List[str] = None,
    ):
        # The timestamp when the rule was created. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The timestamp when the rule was modified. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The action mode of the rule. Valid values:
        # 
        # *   **0**: allows escape behavior.
        # *   **1**: triggers alerts.
        # *   **2**: blocks escape behavior.
        self.mode = mode
        # The description of the rule.
        self.rule_description = rule_description
        # The ID of the rule.
        self.rule_id = rule_id
        # The name of the rule.
        self.rule_name = rule_name
        # The template ID of the rule.
        self.rule_template_id = rule_template_id
        # The template name of the rule.
        self.rule_template_name = rule_template_name
        # The rule items.
        self.selected_policy = selected_policy
        # The ID of the switch.
        self.switch_id = switch_id
        # The images that are added to the whitelist.
        self.white_images = white_images

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.rule_description is not None:
            result['RuleDescription'] = self.rule_description

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_template_id is not None:
            result['RuleTemplateId'] = self.rule_template_id

        if self.rule_template_name is not None:
            result['RuleTemplateName'] = self.rule_template_name

        if self.selected_policy is not None:
            result['SelectedPolicy'] = self.selected_policy

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.white_images is not None:
            result['WhiteImages'] = self.white_images

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RuleDescription') is not None:
            self.rule_description = m.get('RuleDescription')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleTemplateId') is not None:
            self.rule_template_id = m.get('RuleTemplateId')

        if m.get('RuleTemplateName') is not None:
            self.rule_template_name = m.get('RuleTemplateName')

        if m.get('SelectedPolicy') is not None:
            self.selected_policy = m.get('SelectedPolicy')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('WhiteImages') is not None:
            self.white_images = m.get('WhiteImages')

        return self


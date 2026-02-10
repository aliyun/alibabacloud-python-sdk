# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class AddClientUserDefineRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_define_rule_add_result: main_models.AddClientUserDefineRuleResponseBodyUserDefineRuleAddResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The identifier of the custom defense rule.
        self.user_define_rule_add_result = user_define_rule_add_result

    def validate(self):
        if self.user_define_rule_add_result:
            self.user_define_rule_add_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_define_rule_add_result is not None:
            result['UserDefineRuleAddResult'] = self.user_define_rule_add_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserDefineRuleAddResult') is not None:
            temp_model = main_models.AddClientUserDefineRuleResponseBodyUserDefineRuleAddResult()
            self.user_define_rule_add_result = temp_model.from_map(m.get('UserDefineRuleAddResult'))

        return self

class AddClientUserDefineRuleResponseBodyUserDefineRuleAddResult(DaraModel):
    def __init__(
        self,
        id: int = None,
        platform: str = None,
        switch_id: str = None,
    ):
        # The ID of the rule.
        self.id = id
        # The type of the operating system. Valid values:
        # 
        # *   **windows**: Windows
        # *   **linux**: Linux
        # *   **all**: all types
        self.platform = platform
        # The switch ID of the custom defense rule.
        self.switch_id = switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        return self


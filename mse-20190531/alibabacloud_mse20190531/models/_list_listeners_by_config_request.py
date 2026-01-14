# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListListenersByConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        data_id: str = None,
        ext_gray_rules: List[main_models.ListListenersByConfigRequestExtGrayRules] = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        request_pars: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the data.
        # 
        # This parameter is required.
        self.data_id = data_id
        self.ext_gray_rules = ext_gray_rules
        # The name of the group.
        # 
        # This parameter is required.
        self.group = group
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars

    def validate(self):
        if self.ext_gray_rules:
            for v1 in self.ext_gray_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.data_id is not None:
            result['DataId'] = self.data_id

        result['ExtGrayRules'] = []
        if self.ext_gray_rules is not None:
            for k1 in self.ext_gray_rules:
                result['ExtGrayRules'].append(k1.to_map() if k1 else None)

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        self.ext_gray_rules = []
        if m.get('ExtGrayRules') is not None:
            for k1 in m.get('ExtGrayRules'):
                temp_model = main_models.ListListenersByConfigRequestExtGrayRules()
                self.ext_gray_rules.append(temp_model.from_map(k1))

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

class ListListenersByConfigRequestExtGrayRules(DaraModel):
    def __init__(
        self,
        gray_rule: str = None,
        gray_rule_name: str = None,
        gray_rule_priority: int = None,
        gray_rule_type: str = None,
    ):
        self.gray_rule = gray_rule
        self.gray_rule_name = gray_rule_name
        self.gray_rule_priority = gray_rule_priority
        self.gray_rule_type = gray_rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gray_rule is not None:
            result['GrayRule'] = self.gray_rule

        if self.gray_rule_name is not None:
            result['GrayRuleName'] = self.gray_rule_name

        if self.gray_rule_priority is not None:
            result['GrayRulePriority'] = self.gray_rule_priority

        if self.gray_rule_type is not None:
            result['GrayRuleType'] = self.gray_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrayRule') is not None:
            self.gray_rule = m.get('GrayRule')

        if m.get('GrayRuleName') is not None:
            self.gray_rule_name = m.get('GrayRuleName')

        if m.get('GrayRulePriority') is not None:
            self.gray_rule_priority = m.get('GrayRulePriority')

        if m.get('GrayRuleType') is not None:
            self.gray_rule_type = m.get('GrayRuleType')

        return self


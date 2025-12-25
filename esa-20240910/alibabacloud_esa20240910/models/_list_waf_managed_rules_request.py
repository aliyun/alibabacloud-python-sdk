# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListWafManagedRulesRequest(DaraModel):
    def __init__(
        self,
        attack_type: int = None,
        id: int = None,
        instance_id: str = None,
        language: str = None,
        managed_ruleset: main_models.ListWafManagedRulesRequestManagedRuleset = None,
        page_number: int = None,
        page_size: int = None,
        protection_level: int = None,
        query_args: main_models.ListWafManagedRulesRequestQueryArgs = None,
        site_id: int = None,
    ):
        # Attack type of the vulnerability protection event. Values:
        # - SQL injection
        # - Cross-site scripting
        # - Code execution
        # - CRLF
        # - Local file inclusion
        # - Remote file inclusion
        # - Webshell
        # - Cross-site request forgery
        # - Other
        # - SEMA
        # 
        # This parameter is required.
        self.attack_type = attack_type
        # ID of the WAF rule.
        self.id = id
        self.instance_id = instance_id
        # Language type, which will be used to return the response. Value range:
        # 
        # - **en**: English.
        # - **zh**: Chinese.
        self.language = language
        self.managed_ruleset = managed_ruleset
        # Query page number.
        self.page_number = page_number
        # Query page size.
        self.page_size = page_size
        self.protection_level = protection_level
        # Query conditions.
        self.query_args = query_args
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) interface.
        self.site_id = site_id

    def validate(self):
        if self.managed_ruleset:
            self.managed_ruleset.validate()
        if self.query_args:
            self.query_args.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.language is not None:
            result['Language'] = self.language

        if self.managed_ruleset is not None:
            result['ManagedRuleset'] = self.managed_ruleset.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level

        if self.query_args is not None:
            result['QueryArgs'] = self.query_args.to_map()

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ManagedRuleset') is not None:
            temp_model = main_models.ListWafManagedRulesRequestManagedRuleset()
            self.managed_ruleset = temp_model.from_map(m.get('ManagedRuleset'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')

        if m.get('QueryArgs') is not None:
            temp_model = main_models.ListWafManagedRulesRequestQueryArgs()
            self.query_args = temp_model.from_map(m.get('QueryArgs'))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

class ListWafManagedRulesRequestQueryArgs(DaraModel):
    def __init__(
        self,
        action: str = None,
        id_name_like: str = None,
        protection_levels: List[int] = None,
        status: str = None,
    ):
        # Action.
        self.action = action
        # Fuzzy search for rule ID or rule name.
        self.id_name_like = id_name_like
        # List of rule protection levels.
        self.protection_levels = protection_levels
        # Status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.id_name_like is not None:
            result['IdNameLike'] = self.id_name_like

        if self.protection_levels is not None:
            result['ProtectionLevels'] = self.protection_levels

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('IdNameLike') is not None:
            self.id_name_like = m.get('IdNameLike')

        if m.get('ProtectionLevels') is not None:
            self.protection_levels = m.get('ProtectionLevels')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListWafManagedRulesRequestManagedRuleset(DaraModel):
    def __init__(
        self,
        action: str = None,
        attack_type: int = None,
        managed_rules: List[main_models.ListWafManagedRulesRequestManagedRulesetManagedRules] = None,
        protection_level: int = None,
    ):
        self.action = action
        self.attack_type = attack_type
        self.managed_rules = managed_rules
        self.protection_level = protection_level

    def validate(self):
        if self.managed_rules:
            for v1 in self.managed_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        result['ManagedRules'] = []
        if self.managed_rules is not None:
            for k1 in self.managed_rules:
                result['ManagedRules'].append(k1.to_map() if k1 else None)

        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        self.managed_rules = []
        if m.get('ManagedRules') is not None:
            for k1 in m.get('ManagedRules'):
                temp_model = main_models.ListWafManagedRulesRequestManagedRulesetManagedRules()
                self.managed_rules.append(temp_model.from_map(k1))

        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')

        return self

class ListWafManagedRulesRequestManagedRulesetManagedRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        id: int = None,
        status: str = None,
    ):
        self.action = action
        self.id = id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


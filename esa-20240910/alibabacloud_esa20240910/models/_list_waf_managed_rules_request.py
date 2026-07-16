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
        # The attack type of the vulnerability prevention event. Valid values:
        # - SQL injection
        # - cross-site scripting (XSS)
        # - code execute
        # - CRLF
        # - local file inclusion (LFI)
        # - remote file inclusion (RFI)
        # - webshell
        # - cross-site request forgery
        # - Others
        # - SEMA
        # 
        # This parameter is required.
        self.attack_type = attack_type
        # The ID of the WAF rule.
        self.id = id
        # The WAF instance ID.
        self.instance_id = instance_id
        # The language type. The response is returned in the specified language. Valid values:
        # 
        # - **en**: English.
        # - **zh**: Chinese.
        self.language = language
        # The managed ruleset configuration in JSON string format.
        # 
        # Contains the AttackType, ProtectionLevel, Action, and ManagedRules subfields. When ProtectionLevel is set to -1 (custom mode), specify the status and action for each rule through the ManagedRules array.
        self.managed_ruleset = managed_ruleset
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The currently saved protection level, which represents the existing configuration state in the database.
        # 
        # Valid values: -1 (custom mode), 1 (loose), 2 (medium), 3 (strict), 4 (super strict).
        # 
        # Difference from ManagedRuleset.ProtectionLevel: this parameter indicates the currently effective configuration, while ManagedRuleset.ProtectionLevel indicates the target value being passed in.
        self.protection_level = protection_level
        # The query conditions.
        self.query_args = query_args
        # The site ID. You can obtain the site ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
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
        # The action.
        self.action = action
        # Fuzzy match by rule ID or rule name.
        self.id_name_like = id_name_like
        # The list of rule protection levels.
        self.protection_levels = protection_levels
        # The status.
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
        # The unified action when ProtectionLevel is greater than 0. This parameter cannot be empty in this case.
        # 
        # Common valid values: monitor, deny, js, captcha. The actual available values depend on the instance quota.
        self.action = action
        # The attack type encoding. The value cannot be 0.
        # 
        # Example values: 11 (SQL injection), 12 (XSS), 13 (code execute), 14 (CRLF), 15 (local file inclusion (LFI)), 16 (remote file inclusion (RFI)), 17 (WebShell), 22 (command injection), 26 (SSRF), 27 (path traversal), 28 (protocol violation), 31 (scanner behavior).
        self.attack_type = attack_type
        # The rule configuration list in custom mode. This parameter is used only when ProtectionLevel is set to -1.
        # 
        # Each element contains Id, Status, and Action, which are used to specify the enabled status and action for each managed rule.
        self.managed_rules = managed_rules
        # The protection level within the ruleset.
        # 
        # Valid values: -1 (custom mode, specify each rule through ManagedRules), 1 (loose), 2 (medium), 3 (strict), 4 (super strict).
        # 
        # When the value is -1, ManagedRules cannot be empty. When the value is greater than 0, Action cannot be empty.
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
        # The action for a single rule. This parameter takes effect only in custom mode (ProtectionLevel = -1).
        # 
        # Common valid values: monitor, deny, js, captcha. The actual available values depend on the instance quota.
        self.action = action
        # The unique ID of a single managed rule.
        self.id = id
        # The rule enabled status.
        # 
        # Valid values:
        # - on: enabled.
        # - off: disabled.
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


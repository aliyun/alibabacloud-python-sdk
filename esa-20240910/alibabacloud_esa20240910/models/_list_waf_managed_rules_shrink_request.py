# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWafManagedRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        attack_type: int = None,
        id: int = None,
        instance_id: str = None,
        language: str = None,
        managed_ruleset_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        protection_level: int = None,
        query_args_shrink: str = None,
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
        self.managed_ruleset_shrink = managed_ruleset_shrink
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
        self.query_args_shrink = query_args_shrink
        # The site ID. You can obtain the site ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.site_id = site_id

    def validate(self):
        pass

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

        if self.managed_ruleset_shrink is not None:
            result['ManagedRuleset'] = self.managed_ruleset_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level

        if self.query_args_shrink is not None:
            result['QueryArgs'] = self.query_args_shrink

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
            self.managed_ruleset_shrink = m.get('ManagedRuleset')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')

        if m.get('QueryArgs') is not None:
            self.query_args_shrink = m.get('QueryArgs')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class WafRuleConfig(DaraModel):
    def __init__(
        self,
        action: str = None,
        actions: main_models.WafRuleConfigActions = None,
        app_package: main_models.WafRuleConfigAppPackage = None,
        app_sdk: main_models.WafRuleConfigAppSdk = None,
        expression: str = None,
        id: int = None,
        managed_group_id: int = None,
        managed_list: str = None,
        managed_rulesets: List[main_models.WafRuleConfigManagedRulesets] = None,
        name: str = None,
        notes: str = None,
        rate_limit: main_models.WafRuleConfigRateLimit = None,
        security_level: main_models.WafRuleConfigSecurityLevel = None,
        sigchl: List[str] = None,
        status: str = None,
        timer: main_models.WafTimer = None,
        type: str = None,
        value: str = None,
    ):
        self.action = action
        self.actions = actions
        self.app_package = app_package
        self.app_sdk = app_sdk
        self.expression = expression
        self.id = id
        self.managed_group_id = managed_group_id
        self.managed_list = managed_list
        self.managed_rulesets = managed_rulesets
        self.name = name
        self.notes = notes
        self.rate_limit = rate_limit
        self.security_level = security_level
        self.sigchl = sigchl
        self.status = status
        self.timer = timer
        self.type = type
        self.value = value

    def validate(self):
        if self.actions:
            self.actions.validate()
        if self.app_package:
            self.app_package.validate()
        if self.app_sdk:
            self.app_sdk.validate()
        if self.managed_rulesets:
            for v1 in self.managed_rulesets:
                 if v1:
                    v1.validate()
        if self.rate_limit:
            self.rate_limit.validate()
        if self.security_level:
            self.security_level.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.actions is not None:
            result['Actions'] = self.actions.to_map()

        if self.app_package is not None:
            result['AppPackage'] = self.app_package.to_map()

        if self.app_sdk is not None:
            result['AppSdk'] = self.app_sdk.to_map()

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.id is not None:
            result['Id'] = self.id

        if self.managed_group_id is not None:
            result['ManagedGroupId'] = self.managed_group_id

        if self.managed_list is not None:
            result['ManagedList'] = self.managed_list

        result['ManagedRulesets'] = []
        if self.managed_rulesets is not None:
            for k1 in self.managed_rulesets:
                result['ManagedRulesets'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.notes is not None:
            result['Notes'] = self.notes

        if self.rate_limit is not None:
            result['RateLimit'] = self.rate_limit.to_map()

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level.to_map()

        if self.sigchl is not None:
            result['Sigchl'] = self.sigchl

        if self.status is not None:
            result['Status'] = self.status

        if self.timer is not None:
            result['Timer'] = self.timer.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Actions') is not None:
            temp_model = main_models.WafRuleConfigActions()
            self.actions = temp_model.from_map(m.get('Actions'))

        if m.get('AppPackage') is not None:
            temp_model = main_models.WafRuleConfigAppPackage()
            self.app_package = temp_model.from_map(m.get('AppPackage'))

        if m.get('AppSdk') is not None:
            temp_model = main_models.WafRuleConfigAppSdk()
            self.app_sdk = temp_model.from_map(m.get('AppSdk'))

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ManagedGroupId') is not None:
            self.managed_group_id = m.get('ManagedGroupId')

        if m.get('ManagedList') is not None:
            self.managed_list = m.get('ManagedList')

        self.managed_rulesets = []
        if m.get('ManagedRulesets') is not None:
            for k1 in m.get('ManagedRulesets'):
                temp_model = main_models.WafRuleConfigManagedRulesets()
                self.managed_rulesets.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Notes') is not None:
            self.notes = m.get('Notes')

        if m.get('RateLimit') is not None:
            temp_model = main_models.WafRuleConfigRateLimit()
            self.rate_limit = temp_model.from_map(m.get('RateLimit'))

        if m.get('SecurityLevel') is not None:
            temp_model = main_models.WafRuleConfigSecurityLevel()
            self.security_level = temp_model.from_map(m.get('SecurityLevel'))

        if m.get('Sigchl') is not None:
            self.sigchl = m.get('Sigchl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Timer') is not None:
            temp_model = main_models.WafTimer()
            self.timer = temp_model.from_map(m.get('Timer'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class WafRuleConfigSecurityLevel(DaraModel):
    def __init__(
        self,
        value: str = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class WafRuleConfigRateLimit(DaraModel):
    def __init__(
        self,
        characteristics: main_models.WafRatelimitCharacteristics = None,
        interval: int = None,
        on_hit: bool = None,
        ttl: int = None,
        threshold: main_models.WafRuleConfigRateLimitThreshold = None,
    ):
        self.characteristics = characteristics
        self.interval = interval
        self.on_hit = on_hit
        self.ttl = ttl
        self.threshold = threshold

    def validate(self):
        if self.characteristics:
            self.characteristics.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.characteristics is not None:
            result['Characteristics'] = self.characteristics.to_map()

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.on_hit is not None:
            result['OnHit'] = self.on_hit

        if self.ttl is not None:
            result['TTL'] = self.ttl

        if self.threshold is not None:
            result['Threshold'] = self.threshold.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Characteristics') is not None:
            temp_model = main_models.WafRatelimitCharacteristics()
            self.characteristics = temp_model.from_map(m.get('Characteristics'))

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OnHit') is not None:
            self.on_hit = m.get('OnHit')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        if m.get('Threshold') is not None:
            temp_model = main_models.WafRuleConfigRateLimitThreshold()
            self.threshold = temp_model.from_map(m.get('Threshold'))

        return self

class WafRuleConfigRateLimitThreshold(DaraModel):
    def __init__(
        self,
        distinct_managed_rules: int = None,
        managed_rules_blocked: int = None,
        request: int = None,
        response_status: main_models.WafRuleConfigRateLimitThresholdResponseStatus = None,
        traffic: str = None,
    ):
        self.distinct_managed_rules = distinct_managed_rules
        self.managed_rules_blocked = managed_rules_blocked
        self.request = request
        self.response_status = response_status
        self.traffic = traffic

    def validate(self):
        if self.response_status:
            self.response_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distinct_managed_rules is not None:
            result['DistinctManagedRules'] = self.distinct_managed_rules

        if self.managed_rules_blocked is not None:
            result['ManagedRulesBlocked'] = self.managed_rules_blocked

        if self.request is not None:
            result['Request'] = self.request

        if self.response_status is not None:
            result['ResponseStatus'] = self.response_status.to_map()

        if self.traffic is not None:
            result['Traffic'] = self.traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistinctManagedRules') is not None:
            self.distinct_managed_rules = m.get('DistinctManagedRules')

        if m.get('ManagedRulesBlocked') is not None:
            self.managed_rules_blocked = m.get('ManagedRulesBlocked')

        if m.get('Request') is not None:
            self.request = m.get('Request')

        if m.get('ResponseStatus') is not None:
            temp_model = main_models.WafRuleConfigRateLimitThresholdResponseStatus()
            self.response_status = temp_model.from_map(m.get('ResponseStatus'))

        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')

        return self

class WafRuleConfigRateLimitThresholdResponseStatus(DaraModel):
    def __init__(
        self,
        code: int = None,
        count: int = None,
        ratio: int = None,
    ):
        self.code = code
        self.count = count
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        return self

class WafRuleConfigManagedRulesets(DaraModel):
    def __init__(
        self,
        action: str = None,
        attack_type: int = None,
        managed_rules: List[main_models.WafRuleConfigManagedRulesetsManagedRules] = None,
        number_enabled: int = None,
        number_total: int = None,
        protection_level: int = None,
    ):
        self.action = action
        self.attack_type = attack_type
        self.managed_rules = managed_rules
        self.number_enabled = number_enabled
        self.number_total = number_total
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

        if self.number_enabled is not None:
            result['NumberEnabled'] = self.number_enabled

        if self.number_total is not None:
            result['NumberTotal'] = self.number_total

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
                temp_model = main_models.WafRuleConfigManagedRulesetsManagedRules()
                self.managed_rules.append(temp_model.from_map(k1))

        if m.get('NumberEnabled') is not None:
            self.number_enabled = m.get('NumberEnabled')

        if m.get('NumberTotal') is not None:
            self.number_total = m.get('NumberTotal')

        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')

        return self

class WafRuleConfigManagedRulesetsManagedRules(DaraModel):
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

class WafRuleConfigAppSdk(DaraModel):
    def __init__(
        self,
        custom_sign: main_models.WafRuleConfigAppSdkCustomSign = None,
        custom_sign_status: str = None,
        feature_abnormal: List[str] = None,
    ):
        self.custom_sign = custom_sign
        self.custom_sign_status = custom_sign_status
        self.feature_abnormal = feature_abnormal

    def validate(self):
        if self.custom_sign:
            self.custom_sign.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_sign is not None:
            result['CustomSign'] = self.custom_sign.to_map()

        if self.custom_sign_status is not None:
            result['CustomSignStatus'] = self.custom_sign_status

        if self.feature_abnormal is not None:
            result['FeatureAbnormal'] = self.feature_abnormal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSign') is not None:
            temp_model = main_models.WafRuleConfigAppSdkCustomSign()
            self.custom_sign = temp_model.from_map(m.get('CustomSign'))

        if m.get('CustomSignStatus') is not None:
            self.custom_sign_status = m.get('CustomSignStatus')

        if m.get('FeatureAbnormal') is not None:
            self.feature_abnormal = m.get('FeatureAbnormal')

        return self

class WafRuleConfigAppSdkCustomSign(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class WafRuleConfigAppPackage(DaraModel):
    def __init__(
        self,
        package_signs: List[main_models.WafRuleConfigAppPackagePackageSigns] = None,
    ):
        self.package_signs = package_signs

    def validate(self):
        if self.package_signs:
            for v1 in self.package_signs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PackageSigns'] = []
        if self.package_signs is not None:
            for k1 in self.package_signs:
                result['PackageSigns'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package_signs = []
        if m.get('PackageSigns') is not None:
            for k1 in m.get('PackageSigns'):
                temp_model = main_models.WafRuleConfigAppPackagePackageSigns()
                self.package_signs.append(temp_model.from_map(k1))

        return self

class WafRuleConfigAppPackagePackageSigns(DaraModel):
    def __init__(
        self,
        name: str = None,
        sign: str = None,
    ):
        self.name = name
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.sign is not None:
            result['Sign'] = self.sign

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Sign') is not None:
            self.sign = m.get('Sign')

        return self

class WafRuleConfigActions(DaraModel):
    def __init__(
        self,
        bypass: main_models.WafRuleConfigActionsBypass = None,
        response: main_models.WafRuleConfigActionsResponse = None,
    ):
        self.bypass = bypass
        self.response = response

    def validate(self):
        if self.bypass:
            self.bypass.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bypass is not None:
            result['Bypass'] = self.bypass.to_map()

        if self.response is not None:
            result['Response'] = self.response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bypass') is not None:
            temp_model = main_models.WafRuleConfigActionsBypass()
            self.bypass = temp_model.from_map(m.get('Bypass'))

        if m.get('Response') is not None:
            temp_model = main_models.WafRuleConfigActionsResponse()
            self.response = temp_model.from_map(m.get('Response'))

        return self

class WafRuleConfigActionsResponse(DaraModel):
    def __init__(
        self,
        code: int = None,
        id: int = None,
    ):
        self.code = code
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class WafRuleConfigActionsBypass(DaraModel):
    def __init__(
        self,
        custom_rules: List[int] = None,
        regular_rules: List[int] = None,
        regular_types: List[str] = None,
        skip: str = None,
        tags: List[str] = None,
    ):
        self.custom_rules = custom_rules
        self.regular_rules = regular_rules
        self.regular_types = regular_types
        self.skip = skip
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_rules is not None:
            result['CustomRules'] = self.custom_rules

        if self.regular_rules is not None:
            result['RegularRules'] = self.regular_rules

        if self.regular_types is not None:
            result['RegularTypes'] = self.regular_types

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomRules') is not None:
            self.custom_rules = m.get('CustomRules')

        if m.get('RegularRules') is not None:
            self.regular_rules = m.get('RegularRules')

        if m.get('RegularTypes') is not None:
            self.regular_types = m.get('RegularTypes')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self


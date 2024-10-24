# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Any, List, Dict, BinaryIO


class WafBatchRuleSharedActionsResponse(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class WafBatchRuleSharedActions(TeaModel):
    def __init__(
        self,
        response: WafBatchRuleSharedActionsResponse = None,
    ):
        self.response = response

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response is not None:
            result['Response'] = self.response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Response') is not None:
            temp_model = WafBatchRuleSharedActionsResponse()
            self.response = temp_model.from_map(m['Response'])
        return self


class WafRuleMatch2CriteriaCriteriaCriteria(TeaModel):
    def __init__(
        self,
        convert_to_lower: bool = None,
        match_operator: str = None,
        match_type: str = None,
        match_value: Any = None,
        negate: bool = None,
    ):
        self.convert_to_lower = convert_to_lower
        self.match_operator = match_operator
        self.match_type = match_type
        self.match_value = match_value
        self.negate = negate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_to_lower is not None:
            result['ConvertToLower'] = self.convert_to_lower
        if self.match_operator is not None:
            result['MatchOperator'] = self.match_operator
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.match_value is not None:
            result['MatchValue'] = self.match_value
        if self.negate is not None:
            result['Negate'] = self.negate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertToLower') is not None:
            self.convert_to_lower = m.get('ConvertToLower')
        if m.get('MatchOperator') is not None:
            self.match_operator = m.get('MatchOperator')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MatchValue') is not None:
            self.match_value = m.get('MatchValue')
        if m.get('Negate') is not None:
            self.negate = m.get('Negate')
        return self


class WafRuleMatch2CriteriaCriteria(TeaModel):
    def __init__(
        self,
        convert_to_lower: bool = None,
        criteria: List[WafRuleMatch2CriteriaCriteriaCriteria] = None,
        logic: str = None,
        match_operator: str = None,
        match_type: str = None,
        match_value: Any = None,
        negate: bool = None,
    ):
        self.convert_to_lower = convert_to_lower
        self.criteria = criteria
        self.logic = logic
        self.match_operator = match_operator
        self.match_type = match_type
        self.match_value = match_value
        self.negate = negate

    def validate(self):
        if self.criteria:
            for k in self.criteria:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_to_lower is not None:
            result['ConvertToLower'] = self.convert_to_lower
        result['Criteria'] = []
        if self.criteria is not None:
            for k in self.criteria:
                result['Criteria'].append(k.to_map() if k else None)
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.match_operator is not None:
            result['MatchOperator'] = self.match_operator
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.match_value is not None:
            result['MatchValue'] = self.match_value
        if self.negate is not None:
            result['Negate'] = self.negate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertToLower') is not None:
            self.convert_to_lower = m.get('ConvertToLower')
        self.criteria = []
        if m.get('Criteria') is not None:
            for k in m.get('Criteria'):
                temp_model = WafRuleMatch2CriteriaCriteriaCriteria()
                self.criteria.append(temp_model.from_map(k))
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('MatchOperator') is not None:
            self.match_operator = m.get('MatchOperator')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MatchValue') is not None:
            self.match_value = m.get('MatchValue')
        if m.get('Negate') is not None:
            self.negate = m.get('Negate')
        return self


class WafRuleMatch2Criteria(TeaModel):
    def __init__(
        self,
        convert_to_lower: bool = None,
        criteria: List[WafRuleMatch2CriteriaCriteria] = None,
        logic: str = None,
        match_operator: str = None,
        match_type: str = None,
        match_value: Any = None,
        negate: bool = None,
    ):
        self.convert_to_lower = convert_to_lower
        self.criteria = criteria
        self.logic = logic
        self.match_operator = match_operator
        self.match_type = match_type
        self.match_value = match_value
        self.negate = negate

    def validate(self):
        if self.criteria:
            for k in self.criteria:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_to_lower is not None:
            result['ConvertToLower'] = self.convert_to_lower
        result['Criteria'] = []
        if self.criteria is not None:
            for k in self.criteria:
                result['Criteria'].append(k.to_map() if k else None)
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.match_operator is not None:
            result['MatchOperator'] = self.match_operator
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.match_value is not None:
            result['MatchValue'] = self.match_value
        if self.negate is not None:
            result['Negate'] = self.negate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertToLower') is not None:
            self.convert_to_lower = m.get('ConvertToLower')
        self.criteria = []
        if m.get('Criteria') is not None:
            for k in m.get('Criteria'):
                temp_model = WafRuleMatch2CriteriaCriteria()
                self.criteria.append(temp_model.from_map(k))
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('MatchOperator') is not None:
            self.match_operator = m.get('MatchOperator')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MatchValue') is not None:
            self.match_value = m.get('MatchValue')
        if m.get('Negate') is not None:
            self.negate = m.get('Negate')
        return self


class WafRuleMatch2(TeaModel):
    def __init__(
        self,
        convert_to_lower: bool = None,
        criteria: List[WafRuleMatch2Criteria] = None,
        logic: str = None,
        match_operator: str = None,
        match_type: str = None,
        match_value: Any = None,
        negate: bool = None,
    ):
        self.convert_to_lower = convert_to_lower
        self.criteria = criteria
        self.logic = logic
        self.match_operator = match_operator
        self.match_type = match_type
        self.match_value = match_value
        self.negate = negate

    def validate(self):
        if self.criteria:
            for k in self.criteria:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_to_lower is not None:
            result['ConvertToLower'] = self.convert_to_lower
        result['Criteria'] = []
        if self.criteria is not None:
            for k in self.criteria:
                result['Criteria'].append(k.to_map() if k else None)
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.match_operator is not None:
            result['MatchOperator'] = self.match_operator
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.match_value is not None:
            result['MatchValue'] = self.match_value
        if self.negate is not None:
            result['Negate'] = self.negate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertToLower') is not None:
            self.convert_to_lower = m.get('ConvertToLower')
        self.criteria = []
        if m.get('Criteria') is not None:
            for k in m.get('Criteria'):
                temp_model = WafRuleMatch2Criteria()
                self.criteria.append(temp_model.from_map(k))
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('MatchOperator') is not None:
            self.match_operator = m.get('MatchOperator')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MatchValue') is not None:
            self.match_value = m.get('MatchValue')
        if m.get('Negate') is not None:
            self.negate = m.get('Negate')
        return self


class WafBatchRuleShared(TeaModel):
    def __init__(
        self,
        action: str = None,
        actions: WafBatchRuleSharedActions = None,
        cross_site_id: int = None,
        expression: str = None,
        match: WafRuleMatch2 = None,
        mode: str = None,
        name: str = None,
        target: str = None,
    ):
        self.action = action
        self.actions = actions
        self.cross_site_id = cross_site_id
        self.expression = expression
        self.match = match
        self.mode = mode
        self.name = name
        self.target = target

    def validate(self):
        if self.actions:
            self.actions.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.actions is not None:
            result['Actions'] = self.actions.to_map()
        if self.cross_site_id is not None:
            result['CrossSiteId'] = self.cross_site_id
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.match is not None:
            result['Match'] = self.match.to_map()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Actions') is not None:
            temp_model = WafBatchRuleSharedActions()
            self.actions = temp_model.from_map(m['Actions'])
        if m.get('CrossSiteId') is not None:
            self.cross_site_id = m.get('CrossSiteId')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Match') is not None:
            temp_model = WafRuleMatch2()
            self.match = temp_model.from_map(m['Match'])
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class WafQuotaInteger(TeaModel):
    def __init__(
        self,
        equal: int = None,
        greater_than: int = None,
        greater_than_or_equal: int = None,
        less_than: int = None,
        less_than_or_equal: int = None,
    ):
        self.equal = equal
        self.greater_than = greater_than
        self.greater_than_or_equal = greater_than_or_equal
        self.less_than = less_than
        self.less_than_or_equal = less_than_or_equal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.equal is not None:
            result['Equal'] = self.equal
        if self.greater_than is not None:
            result['GreaterThan'] = self.greater_than
        if self.greater_than_or_equal is not None:
            result['GreaterThanOrEqual'] = self.greater_than_or_equal
        if self.less_than is not None:
            result['LessThan'] = self.less_than
        if self.less_than_or_equal is not None:
            result['LessThanOrEqual'] = self.less_than_or_equal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Equal') is not None:
            self.equal = m.get('Equal')
        if m.get('GreaterThan') is not None:
            self.greater_than = m.get('GreaterThan')
        if m.get('GreaterThanOrEqual') is not None:
            self.greater_than_or_equal = m.get('GreaterThanOrEqual')
        if m.get('LessThan') is not None:
            self.less_than = m.get('LessThan')
        if m.get('LessThanOrEqual') is not None:
            self.less_than_or_equal = m.get('LessThanOrEqual')
        return self


class WafQuotaString(TeaModel):
    def __init__(
        self,
        regexp: str = None,
    ):
        self.regexp = regexp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regexp is not None:
            result['Regexp'] = self.regexp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regexp') is not None:
            self.regexp = m.get('Regexp')
        return self


class WafRuleConfigActionsBypass(TeaModel):
    def __init__(
        self,
        regular_rules: List[int] = None,
        regular_types: List[str] = None,
        skip: str = None,
        tags: List[str] = None,
    ):
        self.regular_rules = regular_rules
        self.regular_types = regular_types
        self.skip = skip
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('RegularRules') is not None:
            self.regular_rules = m.get('RegularRules')
        if m.get('RegularTypes') is not None:
            self.regular_types = m.get('RegularTypes')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class WafRuleConfigActionsResponse(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class WafRuleConfigActions(TeaModel):
    def __init__(
        self,
        bypass: WafRuleConfigActionsBypass = None,
        response: WafRuleConfigActionsResponse = None,
    ):
        self.bypass = bypass
        self.response = response

    def validate(self):
        if self.bypass:
            self.bypass.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bypass is not None:
            result['Bypass'] = self.bypass.to_map()
        if self.response is not None:
            result['Response'] = self.response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bypass') is not None:
            temp_model = WafRuleConfigActionsBypass()
            self.bypass = temp_model.from_map(m['Bypass'])
        if m.get('Response') is not None:
            temp_model = WafRuleConfigActionsResponse()
            self.response = temp_model.from_map(m['Response'])
        return self


class WafRuleConfigAppPackagePackageSigns(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class WafRuleConfigAppPackage(TeaModel):
    def __init__(
        self,
        package_signs: List[WafRuleConfigAppPackagePackageSigns] = None,
    ):
        self.package_signs = package_signs

    def validate(self):
        if self.package_signs:
            for k in self.package_signs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PackageSigns'] = []
        if self.package_signs is not None:
            for k in self.package_signs:
                result['PackageSigns'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package_signs = []
        if m.get('PackageSigns') is not None:
            for k in m.get('PackageSigns'):
                temp_model = WafRuleConfigAppPackagePackageSigns()
                self.package_signs.append(temp_model.from_map(k))
        return self


class WafRuleConfigAppSdkCustomSign(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class WafRuleConfigAppSdk(TeaModel):
    def __init__(
        self,
        custom_sign: WafRuleConfigAppSdkCustomSign = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = WafRuleConfigAppSdkCustomSign()
            self.custom_sign = temp_model.from_map(m['CustomSign'])
        if m.get('CustomSignStatus') is not None:
            self.custom_sign_status = m.get('CustomSignStatus')
        if m.get('FeatureAbnormal') is not None:
            self.feature_abnormal = m.get('FeatureAbnormal')
        return self


class WafRuleConfigManagedRulesetsManagedRules(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class WafRuleConfigManagedRulesets(TeaModel):
    def __init__(
        self,
        action: str = None,
        attack_type: int = None,
        managed_rules: List[WafRuleConfigManagedRulesetsManagedRules] = None,
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
            for k in self.managed_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        result['ManagedRules'] = []
        if self.managed_rules is not None:
            for k in self.managed_rules:
                result['ManagedRules'].append(k.to_map() if k else None)
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
            for k in m.get('ManagedRules'):
                temp_model = WafRuleConfigManagedRulesetsManagedRules()
                self.managed_rules.append(temp_model.from_map(k))
        if m.get('NumberEnabled') is not None:
            self.number_enabled = m.get('NumberEnabled')
        if m.get('NumberTotal') is not None:
            self.number_total = m.get('NumberTotal')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        return self


class WafRuleConfigRateLimitThresholdResponseStatus(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class WafRuleConfigRateLimitThreshold(TeaModel):
    def __init__(
        self,
        distinct_managed_rules: int = None,
        managed_rules_blocked: int = None,
        request: int = None,
        response_status: WafRuleConfigRateLimitThresholdResponseStatus = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = WafRuleConfigRateLimitThresholdResponseStatus()
            self.response_status = temp_model.from_map(m['ResponseStatus'])
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class WafRuleConfigRateLimit(TeaModel):
    def __init__(
        self,
        characteristics: WafRuleMatch2 = None,
        interval: int = None,
        on_hit: bool = None,
        ttl: int = None,
        threshold: WafRuleConfigRateLimitThreshold = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = WafRuleMatch2()
            self.characteristics = temp_model.from_map(m['Characteristics'])
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OnHit') is not None:
            self.on_hit = m.get('OnHit')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Threshold') is not None:
            temp_model = WafRuleConfigRateLimitThreshold()
            self.threshold = temp_model.from_map(m['Threshold'])
        return self


class WafRuleMatch(TeaModel):
    def __init__(
        self,
        convert_to_lower: bool = None,
        criteria: List['WafRuleMatch'] = None,
        logic: str = None,
        match_operator: str = None,
        match_type: str = None,
        match_value: Any = None,
        negate: bool = None,
    ):
        self.convert_to_lower = convert_to_lower
        self.criteria = criteria
        self.logic = logic
        self.match_operator = match_operator
        self.match_type = match_type
        self.match_value = match_value
        self.negate = negate

    def validate(self):
        if self.criteria:
            for k in self.criteria:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_to_lower is not None:
            result['ConvertToLower'] = self.convert_to_lower
        result['Criteria'] = []
        if self.criteria is not None:
            for k in self.criteria:
                result['Criteria'].append(k.to_map() if k else None)
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.match_operator is not None:
            result['MatchOperator'] = self.match_operator
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.match_value is not None:
            result['MatchValue'] = self.match_value
        if self.negate is not None:
            result['Negate'] = self.negate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertToLower') is not None:
            self.convert_to_lower = m.get('ConvertToLower')
        self.criteria = []
        if m.get('Criteria') is not None:
            for k in m.get('Criteria'):
                temp_model = WafRuleMatch()
                self.criteria.append(temp_model.from_map(k))
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('MatchOperator') is not None:
            self.match_operator = m.get('MatchOperator')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MatchValue') is not None:
            self.match_value = m.get('MatchValue')
        if m.get('Negate') is not None:
            self.negate = m.get('Negate')
        return self


class WafTimerPeriods(TeaModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class WafTimerWeeklyPeriodsDailyPeriods(TeaModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class WafTimerWeeklyPeriods(TeaModel):
    def __init__(
        self,
        daily_periods: List[WafTimerWeeklyPeriodsDailyPeriods] = None,
        days: str = None,
    ):
        self.daily_periods = daily_periods
        self.days = days

    def validate(self):
        if self.daily_periods:
            for k in self.daily_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DailyPeriods'] = []
        if self.daily_periods is not None:
            for k in self.daily_periods:
                result['DailyPeriods'].append(k.to_map() if k else None)
        if self.days is not None:
            result['Days'] = self.days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.daily_periods = []
        if m.get('DailyPeriods') is not None:
            for k in m.get('DailyPeriods'):
                temp_model = WafTimerWeeklyPeriodsDailyPeriods()
                self.daily_periods.append(temp_model.from_map(k))
        if m.get('Days') is not None:
            self.days = m.get('Days')
        return self


class WafTimer(TeaModel):
    def __init__(
        self,
        periods: List[WafTimerPeriods] = None,
        scopes: str = None,
        weekly_periods: List[WafTimerWeeklyPeriods] = None,
        zone: int = None,
    ):
        self.periods = periods
        self.scopes = scopes
        self.weekly_periods = weekly_periods
        self.zone = zone

    def validate(self):
        if self.periods:
            for k in self.periods:
                if k:
                    k.validate()
        if self.weekly_periods:
            for k in self.weekly_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Periods'] = []
        if self.periods is not None:
            for k in self.periods:
                result['Periods'].append(k.to_map() if k else None)
        if self.scopes is not None:
            result['Scopes'] = self.scopes
        result['WeeklyPeriods'] = []
        if self.weekly_periods is not None:
            for k in self.weekly_periods:
                result['WeeklyPeriods'].append(k.to_map() if k else None)
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.periods = []
        if m.get('Periods') is not None:
            for k in m.get('Periods'):
                temp_model = WafTimerPeriods()
                self.periods.append(temp_model.from_map(k))
        if m.get('Scopes') is not None:
            self.scopes = m.get('Scopes')
        self.weekly_periods = []
        if m.get('WeeklyPeriods') is not None:
            for k in m.get('WeeklyPeriods'):
                temp_model = WafTimerWeeklyPeriods()
                self.weekly_periods.append(temp_model.from_map(k))
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class WafRuleConfig(TeaModel):
    def __init__(
        self,
        action: str = None,
        actions: WafRuleConfigActions = None,
        app_package: WafRuleConfigAppPackage = None,
        app_sdk: WafRuleConfigAppSdk = None,
        expression: str = None,
        id: int = None,
        managed_group_id: int = None,
        managed_list: str = None,
        managed_rulesets: List[WafRuleConfigManagedRulesets] = None,
        match: WafRuleMatch = None,
        name: str = None,
        rate_limit: WafRuleConfigRateLimit = None,
        sigchl: List[str] = None,
        status: str = None,
        timer: WafTimer = None,
        type: str = None,
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
        self.match = match
        self.name = name
        self.rate_limit = rate_limit
        self.sigchl = sigchl
        self.status = status
        self.timer = timer
        self.type = type

    def validate(self):
        if self.actions:
            self.actions.validate()
        if self.app_package:
            self.app_package.validate()
        if self.app_sdk:
            self.app_sdk.validate()
        if self.managed_rulesets:
            for k in self.managed_rulesets:
                if k:
                    k.validate()
        if self.match:
            self.match.validate()
        if self.rate_limit:
            self.rate_limit.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.managed_rulesets:
                result['ManagedRulesets'].append(k.to_map() if k else None)
        if self.match is not None:
            result['Match'] = self.match.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.rate_limit is not None:
            result['RateLimit'] = self.rate_limit.to_map()
        if self.sigchl is not None:
            result['Sigchl'] = self.sigchl
        if self.status is not None:
            result['Status'] = self.status
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Actions') is not None:
            temp_model = WafRuleConfigActions()
            self.actions = temp_model.from_map(m['Actions'])
        if m.get('AppPackage') is not None:
            temp_model = WafRuleConfigAppPackage()
            self.app_package = temp_model.from_map(m['AppPackage'])
        if m.get('AppSdk') is not None:
            temp_model = WafRuleConfigAppSdk()
            self.app_sdk = temp_model.from_map(m['AppSdk'])
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
            for k in m.get('ManagedRulesets'):
                temp_model = WafRuleConfigManagedRulesets()
                self.managed_rulesets.append(temp_model.from_map(k))
        if m.get('Match') is not None:
            temp_model = WafRuleMatch()
            self.match = temp_model.from_map(m['Match'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RateLimit') is not None:
            temp_model = WafRuleConfigRateLimit()
            self.rate_limit = temp_model.from_map(m['RateLimit'])
        if m.get('Sigchl') is not None:
            self.sigchl = m.get('Sigchl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Timer') is not None:
            temp_model = WafTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class WafSiteSettingsAddBotProtectionHeaders(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class WafSiteSettingsAddSecurityHeaders(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class WafSiteSettingsClientIpIdentifier(TeaModel):
    def __init__(
        self,
        headers: List[str] = None,
        mode: str = None,
    ):
        self.headers = headers
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class WafSiteSettingsSecurityLevel(TeaModel):
    def __init__(
        self,
        value: str = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class WafSiteSettings(TeaModel):
    def __init__(
        self,
        add_bot_protection_headers: WafSiteSettingsAddBotProtectionHeaders = None,
        add_security_headers: WafSiteSettingsAddSecurityHeaders = None,
        client_ip_identifier: WafSiteSettingsClientIpIdentifier = None,
        security_level: WafSiteSettingsSecurityLevel = None,
    ):
        self.add_bot_protection_headers = add_bot_protection_headers
        self.add_security_headers = add_security_headers
        self.client_ip_identifier = client_ip_identifier
        self.security_level = security_level

    def validate(self):
        if self.add_bot_protection_headers:
            self.add_bot_protection_headers.validate()
        if self.add_security_headers:
            self.add_security_headers.validate()
        if self.client_ip_identifier:
            self.client_ip_identifier.validate()
        if self.security_level:
            self.security_level.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_bot_protection_headers is not None:
            result['AddBotProtectionHeaders'] = self.add_bot_protection_headers.to_map()
        if self.add_security_headers is not None:
            result['AddSecurityHeaders'] = self.add_security_headers.to_map()
        if self.client_ip_identifier is not None:
            result['ClientIpIdentifier'] = self.client_ip_identifier.to_map()
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddBotProtectionHeaders') is not None:
            temp_model = WafSiteSettingsAddBotProtectionHeaders()
            self.add_bot_protection_headers = temp_model.from_map(m['AddBotProtectionHeaders'])
        if m.get('AddSecurityHeaders') is not None:
            temp_model = WafSiteSettingsAddSecurityHeaders()
            self.add_security_headers = temp_model.from_map(m['AddSecurityHeaders'])
        if m.get('ClientIpIdentifier') is not None:
            temp_model = WafSiteSettingsClientIpIdentifier()
            self.client_ip_identifier = temp_model.from_map(m['ClientIpIdentifier'])
        if m.get('SecurityLevel') is not None:
            temp_model = WafSiteSettingsSecurityLevel()
            self.security_level = temp_model.from_map(m['SecurityLevel'])
        return self


class HttpDeliveryHeaderParamValue(TeaModel):
    def __init__(
        self,
        static_value: str = None,
    ):
        self.static_value = static_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.static_value is not None:
            result['StaticValue'] = self.static_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StaticValue') is not None:
            self.static_value = m.get('StaticValue')
        return self


class HttpDeliveryQueryParamValue(TeaModel):
    def __init__(
        self,
        static_value: str = None,
    ):
        self.static_value = static_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.static_value is not None:
            result['StaticValue'] = self.static_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StaticValue') is not None:
            self.static_value = m.get('StaticValue')
        return self


class FieldContentValueFieldList(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        description: str = None,
        description_cn: str = None,
        category: str = None,
        data_type: str = None,
        sort_order: int = None,
        is_default: bool = None,
    ):
        self.field_name = field_name
        self.description = description
        self.description_cn = description_cn
        self.category = category
        self.data_type = data_type
        self.sort_order = sort_order
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.description is not None:
            result['Description'] = self.description
        if self.description_cn is not None:
            result['DescriptionCn'] = self.description_cn
        if self.category is not None:
            result['Category'] = self.category
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DescriptionCn') is not None:
            self.description_cn = m.get('DescriptionCn')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        return self


class FieldContentValue(TeaModel):
    def __init__(
        self,
        sort_order: int = None,
        field_list: List[FieldContentValueFieldList] = None,
    ):
        self.sort_order = sort_order
        self.field_list = field_list

    def validate(self):
        if self.field_list:
            for k in self.field_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        result['FieldList'] = []
        if self.field_list is not None:
            for k in self.field_list:
                result['FieldList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        self.field_list = []
        if m.get('FieldList') is not None:
            for k in m.get('FieldList'):
                temp_model = FieldContentValueFieldList()
                self.field_list.append(temp_model.from_map(k))
        return self


class QuotaListItemsValue(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        value: WafQuotaString = None,
    ):
        self.enable = enable
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Value') is not None:
            temp_model = WafQuotaString()
            self.value = temp_model.from_map(m['Value'])
        return self


class QuotaPageContentTypesValue(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        content_length: WafQuotaInteger = None,
    ):
        self.enable = enable
        self.content_length = content_length

    def validate(self):
        if self.content_length:
            self.content_length.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.content_length is not None:
            result['ContentLength'] = self.content_length.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ContentLength') is not None:
            temp_model = WafQuotaInteger()
            self.content_length = temp_model.from_map(m['ContentLength'])
        return self


class ActivateClientCertificateRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ActivateClientCertificateResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
        site_id: int = None,
        site_name: str = None,
    ):
        self.id = id
        self.request_id = request_id
        self.site_id = site_id
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        return self


class ActivateClientCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateClientCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ActivateClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreateRecordsRequestRecordListData(TeaModel):
    def __init__(
        self,
        algorithm: int = None,
        certificate: str = None,
        fingerprint: str = None,
        flag: int = None,
        key_tag: int = None,
        matching_type: int = None,
        port: int = None,
        priority: int = None,
        selector: int = None,
        tag: str = None,
        type: int = None,
        usage: int = None,
        value: str = None,
        weight: int = None,
    ):
        self.algorithm = algorithm
        self.certificate = certificate
        self.fingerprint = fingerprint
        self.flag = flag
        self.key_tag = key_tag
        self.matching_type = matching_type
        self.port = port
        self.priority = priority
        self.selector = selector
        self.tag = tag
        self.type = type
        self.usage = usage
        self.value = value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.matching_type is not None:
            result['MatchingType'] = self.matching_type
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.selector is not None:
            result['Selector'] = self.selector
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.value is not None:
            result['Value'] = self.value
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('MatchingType') is not None:
            self.matching_type = m.get('MatchingType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Selector') is not None:
            self.selector = m.get('Selector')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class BatchCreateRecordsRequestRecordList(TeaModel):
    def __init__(
        self,
        biz_name: str = None,
        data: BatchCreateRecordsRequestRecordListData = None,
        proxied: bool = None,
        record_name: str = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        self.biz_name = biz_name
        # This parameter is required.
        self.data = data
        # This parameter is required.
        self.proxied = proxied
        # This parameter is required.
        self.record_name = record_name
        self.source_type = source_type
        # This parameter is required.
        self.ttl = ttl
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.proxied is not None:
            result['Proxied'] = self.proxied
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Data') is not None:
            temp_model = BatchCreateRecordsRequestRecordListData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class BatchCreateRecordsRequest(TeaModel):
    def __init__(
        self,
        record_list: List[BatchCreateRecordsRequestRecordList] = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.record_list = record_list
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        if self.record_list:
            for k in self.record_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RecordList'] = []
        if self.record_list is not None:
            for k in self.record_list:
                result['RecordList'].append(k.to_map() if k else None)
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_list = []
        if m.get('RecordList') is not None:
            for k in m.get('RecordList'):
                temp_model = BatchCreateRecordsRequestRecordList()
                self.record_list.append(temp_model.from_map(k))
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class BatchCreateRecordsShrinkRequest(TeaModel):
    def __init__(
        self,
        record_list_shrink: str = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.record_list_shrink = record_list_shrink
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_list_shrink is not None:
            result['RecordList'] = self.record_list_shrink
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordList') is not None:
            self.record_list_shrink = m.get('RecordList')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class BatchCreateRecordsResponseBodyRecordResultListFailedData(TeaModel):
    def __init__(
        self,
        algorithm: int = None,
        certificate: str = None,
        fingerprint: str = None,
        flag: int = None,
        key_tag: int = None,
        matching_type: int = None,
        port: int = None,
        priority: int = None,
        selector: int = None,
        tag: str = None,
        type: int = None,
        usage: int = None,
        value: str = None,
        weight: int = None,
    ):
        self.algorithm = algorithm
        self.certificate = certificate
        self.fingerprint = fingerprint
        self.flag = flag
        self.key_tag = key_tag
        self.matching_type = matching_type
        self.port = port
        self.priority = priority
        self.selector = selector
        self.tag = tag
        self.type = type
        self.usage = usage
        self.value = value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.matching_type is not None:
            result['MatchingType'] = self.matching_type
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.selector is not None:
            result['Selector'] = self.selector
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.value is not None:
            result['Value'] = self.value
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('MatchingType') is not None:
            self.matching_type = m.get('MatchingType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Selector') is not None:
            self.selector = m.get('Selector')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class BatchCreateRecordsResponseBodyRecordResultListFailed(TeaModel):
    def __init__(
        self,
        biz_name: str = None,
        data: BatchCreateRecordsResponseBodyRecordResultListFailedData = None,
        description: str = None,
        proxied: bool = None,
        record_id: int = None,
        record_name: str = None,
        record_type: str = None,
        source_type: str = None,
        ttl: int = None,
    ):
        self.biz_name = biz_name
        self.data = data
        self.description = description
        self.proxied = proxied
        self.record_id = record_id
        self.record_name = record_name
        self.record_type = record_type
        self.source_type = source_type
        self.ttl = ttl

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.proxied is not None:
            result['Proxied'] = self.proxied
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Data') is not None:
            temp_model = BatchCreateRecordsResponseBodyRecordResultListFailedData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class BatchCreateRecordsResponseBodyRecordResultListSuccessData(TeaModel):
    def __init__(
        self,
        algorithm: int = None,
        certificate: str = None,
        fingerprint: str = None,
        flag: int = None,
        key_tag: int = None,
        matching_type: int = None,
        port: int = None,
        priority: int = None,
        selector: int = None,
        tag: str = None,
        type: int = None,
        usage: int = None,
        value: str = None,
        weight: int = None,
    ):
        self.algorithm = algorithm
        self.certificate = certificate
        self.fingerprint = fingerprint
        self.flag = flag
        self.key_tag = key_tag
        self.matching_type = matching_type
        self.port = port
        self.priority = priority
        self.selector = selector
        self.tag = tag
        self.type = type
        self.usage = usage
        self.value = value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.matching_type is not None:
            result['MatchingType'] = self.matching_type
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.selector is not None:
            result['Selector'] = self.selector
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.value is not None:
            result['Value'] = self.value
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('MatchingType') is not None:
            self.matching_type = m.get('MatchingType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Selector') is not None:
            self.selector = m.get('Selector')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class BatchCreateRecordsResponseBodyRecordResultListSuccess(TeaModel):
    def __init__(
        self,
        biz_name: str = None,
        data: BatchCreateRecordsResponseBodyRecordResultListSuccessData = None,
        description: str = None,
        proxied: bool = None,
        record_id: int = None,
        record_name: str = None,
        record_type: str = None,
        source_type: str = None,
        ttl: int = None,
    ):
        self.biz_name = biz_name
        self.data = data
        self.description = description
        self.proxied = proxied
        self.record_id = record_id
        self.record_name = record_name
        self.record_type = record_type
        self.source_type = source_type
        self.ttl = ttl

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.proxied is not None:
            result['Proxied'] = self.proxied
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Data') is not None:
            temp_model = BatchCreateRecordsResponseBodyRecordResultListSuccessData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class BatchCreateRecordsResponseBodyRecordResultList(TeaModel):
    def __init__(
        self,
        failed: List[BatchCreateRecordsResponseBodyRecordResultListFailed] = None,
        success: List[BatchCreateRecordsResponseBodyRecordResultListSuccess] = None,
        total_count: int = None,
    ):
        self.failed = failed
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.failed:
            for k in self.failed:
                if k:
                    k.validate()
        if self.success:
            for k in self.success:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Failed'] = []
        if self.failed is not None:
            for k in self.failed:
                result['Failed'].append(k.to_map() if k else None)
        result['Success'] = []
        if self.success is not None:
            for k in self.success:
                result['Success'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed = []
        if m.get('Failed') is not None:
            for k in m.get('Failed'):
                temp_model = BatchCreateRecordsResponseBodyRecordResultListFailed()
                self.failed.append(temp_model.from_map(k))
        self.success = []
        if m.get('Success') is not None:
            for k in m.get('Success'):
                temp_model = BatchCreateRecordsResponseBodyRecordResultListSuccess()
                self.success.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class BatchCreateRecordsResponseBody(TeaModel):
    def __init__(
        self,
        record_result_list: BatchCreateRecordsResponseBodyRecordResultList = None,
        request_id: str = None,
    ):
        self.record_result_list = record_result_list
        self.request_id = request_id

    def validate(self):
        if self.record_result_list:
            self.record_result_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_result_list is not None:
            result['RecordResultList'] = self.record_result_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordResultList') is not None:
            temp_model = BatchCreateRecordsResponseBodyRecordResultList()
            self.record_result_list = temp_model.from_map(m['RecordResultList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchCreateRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCreateRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchCreateRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreateWafRulesRequest(TeaModel):
    def __init__(
        self,
        configs: List[WafRuleConfig] = None,
        phase: str = None,
        shared: WafBatchRuleShared = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.configs = configs
        self.phase = phase
        self.shared = shared
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.shared:
            self.shared.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.shared is not None:
            result['Shared'] = self.shared.to_map()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = WafRuleConfig()
                self.configs.append(temp_model.from_map(k))
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('Shared') is not None:
            temp_model = WafBatchRuleShared()
            self.shared = temp_model.from_map(m['Shared'])
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class BatchCreateWafRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        configs_shrink: str = None,
        phase: str = None,
        shared_shrink: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.configs_shrink = configs_shrink
        self.phase = phase
        self.shared_shrink = shared_shrink
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs_shrink is not None:
            result['Configs'] = self.configs_shrink
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.shared_shrink is not None:
            result['Shared'] = self.shared_shrink
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs_shrink = m.get('Configs')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('Shared') is not None:
            self.shared_shrink = m.get('Shared')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class BatchCreateWafRulesResponseBody(TeaModel):
    def __init__(
        self,
        ids: List[int] = None,
        request_id: str = None,
        ruleset_id: int = None,
    ):
        self.ids = ids
        # Id of the request
        self.request_id = request_id
        self.ruleset_id = ruleset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')
        return self


class BatchCreateWafRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCreateWafRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchCreateWafRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteKvRequest(TeaModel):
    def __init__(
        self,
        keys: List[str] = None,
        namespace: str = None,
    ):
        # This parameter is required.
        self.keys = keys
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class BatchDeleteKvShrinkRequest(TeaModel):
    def __init__(
        self,
        keys_shrink: str = None,
        namespace: str = None,
    ):
        # This parameter is required.
        self.keys_shrink = keys_shrink
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class BatchDeleteKvResponseBody(TeaModel):
    def __init__(
        self,
        fail_keys: List[str] = None,
        request_id: str = None,
        success_keys: List[str] = None,
    ):
        self.fail_keys = fail_keys
        # Id of the request
        self.request_id = request_id
        self.success_keys = success_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_keys is not None:
            result['FailKeys'] = self.fail_keys
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_keys is not None:
            result['SuccessKeys'] = self.success_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailKeys') is not None:
            self.fail_keys = m.get('FailKeys')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessKeys') is not None:
            self.success_keys = m.get('SuccessKeys')
        return self


class BatchDeleteKvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteKvResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchDeleteKvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteKvWithHighCapacityRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class BatchDeleteKvWithHighCapacityAdvanceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        url_object: BinaryIO = None,
    ):
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class BatchDeleteKvWithHighCapacityResponseBody(TeaModel):
    def __init__(
        self,
        fail_keys: List[str] = None,
        request_id: str = None,
        success_keys: List[str] = None,
    ):
        self.fail_keys = fail_keys
        # Id of the request
        self.request_id = request_id
        self.success_keys = success_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_keys is not None:
            result['FailKeys'] = self.fail_keys
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_keys is not None:
            result['SuccessKeys'] = self.success_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailKeys') is not None:
            self.fail_keys = m.get('FailKeys')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessKeys') is not None:
            self.success_keys = m.get('SuccessKeys')
        return self


class BatchDeleteKvWithHighCapacityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteKvWithHighCapacityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchDeleteKvWithHighCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetExpressionFieldsRequestExpressions(TeaModel):
    def __init__(
        self,
        expression: str = None,
        id: int = None,
    ):
        self.expression = expression
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchGetExpressionFieldsRequest(TeaModel):
    def __init__(
        self,
        expressions: List[BatchGetExpressionFieldsRequestExpressions] = None,
        phase: str = None,
        site_id: int = None,
    ):
        self.expressions = expressions
        self.phase = phase
        self.site_id = site_id

    def validate(self):
        if self.expressions:
            for k in self.expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Expressions'] = []
        if self.expressions is not None:
            for k in self.expressions:
                result['Expressions'].append(k.to_map() if k else None)
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.expressions = []
        if m.get('Expressions') is not None:
            for k in m.get('Expressions'):
                temp_model = BatchGetExpressionFieldsRequestExpressions()
                self.expressions.append(temp_model.from_map(k))
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class BatchGetExpressionFieldsShrinkRequest(TeaModel):
    def __init__(
        self,
        expressions_shrink: str = None,
        phase: str = None,
        site_id: int = None,
    ):
        self.expressions_shrink = expressions_shrink
        self.phase = phase
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expressions_shrink is not None:
            result['Expressions'] = self.expressions_shrink
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expressions') is not None:
            self.expressions_shrink = m.get('Expressions')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class BatchGetExpressionFieldsResponseBodyFields(TeaModel):
    def __init__(
        self,
        fields: List[str] = None,
        id: str = None,
    ):
        self.fields = fields
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchGetExpressionFieldsResponseBody(TeaModel):
    def __init__(
        self,
        fields: List[BatchGetExpressionFieldsResponseBodyFields] = None,
        request_id: str = None,
    ):
        self.fields = fields
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = BatchGetExpressionFieldsResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchGetExpressionFieldsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetExpressionFieldsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchGetExpressionFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchPutKvRequestKvList(TeaModel):
    def __init__(
        self,
        expiration: int = None,
        expiration_ttl: int = None,
        key: str = None,
        value: str = None,
    ):
        self.expiration = expiration
        self.expiration_ttl = expiration_ttl
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.expiration_ttl is not None:
            result['ExpirationTtl'] = self.expiration_ttl
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('ExpirationTtl') is not None:
            self.expiration_ttl = m.get('ExpirationTtl')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class BatchPutKvRequest(TeaModel):
    def __init__(
        self,
        kv_list: List[BatchPutKvRequestKvList] = None,
        namespace: str = None,
    ):
        # This parameter is required.
        self.kv_list = kv_list
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        if self.kv_list:
            for k in self.kv_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KvList'] = []
        if self.kv_list is not None:
            for k in self.kv_list:
                result['KvList'].append(k.to_map() if k else None)
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kv_list = []
        if m.get('KvList') is not None:
            for k in m.get('KvList'):
                temp_model = BatchPutKvRequestKvList()
                self.kv_list.append(temp_model.from_map(k))
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class BatchPutKvShrinkRequest(TeaModel):
    def __init__(
        self,
        kv_list_shrink: str = None,
        namespace: str = None,
    ):
        # This parameter is required.
        self.kv_list_shrink = kv_list_shrink
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kv_list_shrink is not None:
            result['KvList'] = self.kv_list_shrink
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KvList') is not None:
            self.kv_list_shrink = m.get('KvList')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class BatchPutKvResponseBody(TeaModel):
    def __init__(
        self,
        fail_keys: List[str] = None,
        request_id: str = None,
        success_keys: List[str] = None,
    ):
        self.fail_keys = fail_keys
        # Id of the request
        self.request_id = request_id
        self.success_keys = success_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_keys is not None:
            result['FailKeys'] = self.fail_keys
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_keys is not None:
            result['SuccessKeys'] = self.success_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailKeys') is not None:
            self.fail_keys = m.get('FailKeys')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessKeys') is not None:
            self.success_keys = m.get('SuccessKeys')
        return self


class BatchPutKvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchPutKvResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchPutKvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchPutKvWithHighCapacityRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class BatchPutKvWithHighCapacityAdvanceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        url_object: BinaryIO = None,
    ):
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class BatchPutKvWithHighCapacityResponseBody(TeaModel):
    def __init__(
        self,
        fail_keys: List[str] = None,
        request_id: str = None,
        success_keys: List[str] = None,
    ):
        self.fail_keys = fail_keys
        # Id of the request
        self.request_id = request_id
        self.success_keys = success_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_keys is not None:
            result['FailKeys'] = self.fail_keys
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_keys is not None:
            result['SuccessKeys'] = self.success_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailKeys') is not None:
            self.fail_keys = m.get('FailKeys')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessKeys') is not None:
            self.success_keys = m.get('SuccessKeys')
        return self


class BatchPutKvWithHighCapacityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchPutKvWithHighCapacityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchPutKvWithHighCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateWafRulesRequest(TeaModel):
    def __init__(
        self,
        configs: List[WafRuleConfig] = None,
        phase: str = None,
        ruleset_id: int = None,
        shared: WafBatchRuleShared = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.configs = configs
        self.phase = phase
        self.ruleset_id = ruleset_id
        self.shared = shared
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.shared:
            self.shared.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id
        if self.shared is not None:
            result['Shared'] = self.shared.to_map()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = WafRuleConfig()
                self.configs.append(temp_model.from_map(k))
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')
        if m.get('Shared') is not None:
            temp_model = WafBatchRuleShared()
            self.shared = temp_model.from_map(m['Shared'])
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class BatchUpdateWafRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        configs_shrink: str = None,
        phase: str = None,
        ruleset_id: int = None,
        shared_shrink: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.configs_shrink = configs_shrink
        self.phase = phase
        self.ruleset_id = ruleset_id
        self.shared_shrink = shared_shrink
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs_shrink is not None:
            result['Configs'] = self.configs_shrink
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id
        if self.shared_shrink is not None:
            result['Shared'] = self.shared_shrink
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs_shrink = m.get('Configs')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')
        if m.get('Shared') is not None:
            self.shared_shrink = m.get('Shared')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class BatchUpdateWafRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchUpdateWafRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateWafRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchUpdateWafRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BlockObjectRequest(TeaModel):
    def __init__(
        self,
        content: List[str] = None,
        extension: str = None,
        maxage: int = None,
        site_id: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.extension = extension
        self.maxage = maxage
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.maxage is not None:
            result['Maxage'] = self.maxage
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Maxage') is not None:
            self.maxage = m.get('Maxage')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class BlockObjectShrinkRequest(TeaModel):
    def __init__(
        self,
        content_shrink: str = None,
        extension: str = None,
        maxage: int = None,
        site_id: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.content_shrink = content_shrink
        self.extension = extension
        self.maxage = maxage
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.maxage is not None:
            result['Maxage'] = self.maxage
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Maxage') is not None:
            self.maxage = m.get('Maxage')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class BlockObjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BlockObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BlockObjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BlockObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_group_id: str = None,
        security_token: str = None,
        site_id: int = None,
    ):
        self.owner_id = owner_id
        # This parameter is required.
        self.resource_group_id = resource_group_id
        self.security_token = security_token
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckSiteNameRequest(TeaModel):
    def __init__(
        self,
        site_name: str = None,
    ):
        # This parameter is required.
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        return self


class CheckSiteNameResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        is_sub_site: bool = None,
        messeage: str = None,
        passed: bool = None,
        request_id: str = None,
    ):
        self.description = description
        self.is_sub_site = is_sub_site
        self.messeage = messeage
        self.passed = passed
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.is_sub_site is not None:
            result['IsSubSite'] = self.is_sub_site
        if self.messeage is not None:
            result['Messeage'] = self.messeage
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsSubSite') is not None:
            self.is_sub_site = m.get('IsSubSite')
        if m.get('Messeage') is not None:
            self.messeage = m.get('Messeage')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckSiteNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckSiteNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckSiteNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckSiteProjectNameRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.project_name = project_name
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class CheckSiteProjectNameResponseBody(TeaModel):
    def __init__(
        self,
        check: bool = None,
        description: str = None,
        project_name: str = None,
        request_id: str = None,
    ):
        self.check = check
        self.description = description
        self.project_name = project_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check is not None:
            result['Check'] = self.check
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check') is not None:
            self.check = m.get('Check')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckSiteProjectNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckSiteProjectNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckSiteProjectNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUserProjectNameRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
    ):
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class CheckUserProjectNameResponseBody(TeaModel):
    def __init__(
        self,
        check: bool = None,
        description: str = None,
        project_name: str = None,
        request_id: str = None,
    ):
        self.check = check
        self.description = description
        self.project_name = project_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check is not None:
            result['Check'] = self.check
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check') is not None:
            self.check = m.get('Check')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckUserProjectNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckUserProjectNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckUserProjectNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommitRoutineStagingCodeRequest(TeaModel):
    def __init__(
        self,
        code_description: str = None,
        name: str = None,
    ):
        self.code_description = code_description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CommitRoutineStagingCodeResponseBody(TeaModel):
    def __init__(
        self,
        code_version: str = None,
        request_id: str = None,
    ):
        self.code_version = code_version
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CommitRoutineStagingCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CommitRoutineStagingCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CommitRoutineStagingCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomScenePolicyRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        objects: str = None,
        start_time: str = None,
        template: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.name = name
        self.objects = objects
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.name is not None:
            result['Name'] = self.name
        if self.objects is not None:
            result['Objects'] = self.objects
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class CreateCustomScenePolicyResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        objects: List[str] = None,
        policy_id: int = None,
        request_id: str = None,
        start_time: str = None,
        template: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.objects = objects
        self.policy_id = policy_id
        # Id of the request
        self.request_id = request_id
        self.start_time = start_time
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.name is not None:
            result['Name'] = self.name
        if self.objects is not None:
            result['Objects'] = self.objects
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class CreateCustomScenePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomScenePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomScenePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKvNamespaceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        namespace: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class CreateKvNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        namespace: str = None,
        namespace_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.description = description
        self.namespace = namespace
        self.namespace_id = namespace_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateKvNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKvNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateKvNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateListRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        items: List[str] = None,
        kind: str = None,
        name: str = None,
    ):
        self.description = description
        self.items = items
        self.kind = kind
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.items is not None:
            result['Items'] = self.items
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateListShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        items_shrink: str = None,
        kind: str = None,
        name: str = None,
    ):
        self.description = description
        self.items_shrink = items_shrink
        self.kind = kind
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.items_shrink is not None:
            result['Items'] = self.items_shrink
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Items') is not None:
            self.items_shrink = m.get('Items')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateListResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePageRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        name: str = None,
    ):
        self.content = content
        # This parameter is required.
        self.content_type = content_type
        self.description = description
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePageResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecordRequestAuthConf(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        self.access_key = access_key
        self.auth_type = auth_type
        self.region = region
        self.secret_key = secret_key
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.region is not None:
            result['Region'] = self.region
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateRecordRequestData(TeaModel):
    def __init__(
        self,
        algorithm: int = None,
        certificate: str = None,
        fingerprint: str = None,
        flag: int = None,
        key_tag: int = None,
        matching_type: int = None,
        port: int = None,
        priority: int = None,
        selector: int = None,
        tag: str = None,
        type: int = None,
        usage: int = None,
        value: str = None,
        weight: int = None,
    ):
        self.algorithm = algorithm
        self.certificate = certificate
        self.fingerprint = fingerprint
        self.flag = flag
        self.key_tag = key_tag
        self.matching_type = matching_type
        self.port = port
        self.priority = priority
        self.selector = selector
        self.tag = tag
        self.type = type
        self.usage = usage
        self.value = value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.matching_type is not None:
            result['MatchingType'] = self.matching_type
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.selector is not None:
            result['Selector'] = self.selector
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.value is not None:
            result['Value'] = self.value
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('MatchingType') is not None:
            self.matching_type = m.get('MatchingType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Selector') is not None:
            self.selector = m.get('Selector')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateRecordRequest(TeaModel):
    def __init__(
        self,
        auth_conf: CreateRecordRequestAuthConf = None,
        biz_name: str = None,
        comment: str = None,
        data: CreateRecordRequestData = None,
        host_policy: str = None,
        proxied: bool = None,
        record_name: str = None,
        site_id: int = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        self.auth_conf = auth_conf
        # 业务场景
        self.biz_name = biz_name
        self.comment = comment
        # This parameter is required.
        self.data = data
        self.host_policy = host_policy
        # 是否代理加速
        self.proxied = proxied
        # 记录名称
        # 
        # This parameter is required.
        self.record_name = record_name
        # This parameter is required.
        self.site_id = site_id
        self.source_type = source_type
        self.ttl = ttl
        # 记录类型
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.auth_conf:
            self.auth_conf.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_conf is not None:
            result['AuthConf'] = self.auth_conf.to_map()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.host_policy is not None:
            result['HostPolicy'] = self.host_policy
        if self.proxied is not None:
            result['Proxied'] = self.proxied
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConf') is not None:
            temp_model = CreateRecordRequestAuthConf()
            self.auth_conf = temp_model.from_map(m['AuthConf'])
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Data') is not None:
            temp_model = CreateRecordRequestData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')
        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateRecordShrinkRequest(TeaModel):
    def __init__(
        self,
        auth_conf_shrink: str = None,
        biz_name: str = None,
        comment: str = None,
        data_shrink: str = None,
        host_policy: str = None,
        proxied: bool = None,
        record_name: str = None,
        site_id: int = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        self.auth_conf_shrink = auth_conf_shrink
        # 业务场景
        self.biz_name = biz_name
        self.comment = comment
        # This parameter is required.
        self.data_shrink = data_shrink
        self.host_policy = host_policy
        # 是否代理加速
        self.proxied = proxied
        # 记录名称
        # 
        # This parameter is required.
        self.record_name = record_name
        # This parameter is required.
        self.site_id = site_id
        self.source_type = source_type
        self.ttl = ttl
        # 记录类型
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_conf_shrink is not None:
            result['AuthConf'] = self.auth_conf_shrink
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.data_shrink is not None:
            result['Data'] = self.data_shrink
        if self.host_policy is not None:
            result['HostPolicy'] = self.host_policy
        if self.proxied is not None:
            result['Proxied'] = self.proxied
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConf') is not None:
            self.auth_conf_shrink = m.get('AuthConf')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Data') is not None:
            self.data_shrink = m.get('Data')
        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')
        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateRecordResponseBody(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        request_id: str = None,
    ):
        self.record_id = record_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoutineRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        spec_name: str = None,
    ):
        self.description = description
        self.name = name
        self.spec_name = spec_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        return self


class CreateRoutineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateRoutineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRoutineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRoutineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoutineRelatedRecordRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        record_name: str = None,
        site_id: int = None,
    ):
        self.name = name
        self.record_name = record_name
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class CreateRoutineRelatedRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateRoutineRelatedRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRoutineRelatedRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRoutineRelatedRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoutineRelatedRouteRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        route: str = None,
        site_id: int = None,
    ):
        self.name = name
        self.route = route
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.route is not None:
            result['Route'] = self.route
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class CreateRoutineRelatedRouteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateRoutineRelatedRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRoutineRelatedRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRoutineRelatedRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledPreloadExecutionsRequestExecutions(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        interval: int = None,
        slice_len: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.interval = interval
        # This parameter is required.
        self.slice_len = slice_len
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateScheduledPreloadExecutionsRequest(TeaModel):
    def __init__(
        self,
        executions: List[CreateScheduledPreloadExecutionsRequestExecutions] = None,
        id: str = None,
    ):
        # This parameter is required.
        self.executions = executions
        self.id = id

    def validate(self):
        if self.executions:
            for k in self.executions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Executions'] = []
        if self.executions is not None:
            for k in self.executions:
                result['Executions'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.executions = []
        if m.get('Executions') is not None:
            for k in m.get('Executions'):
                temp_model = CreateScheduledPreloadExecutionsRequestExecutions()
                self.executions.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateScheduledPreloadExecutionsShrinkRequest(TeaModel):
    def __init__(
        self,
        executions_shrink: str = None,
        id: str = None,
    ):
        # This parameter is required.
        self.executions_shrink = executions_shrink
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executions_shrink is not None:
            result['Executions'] = self.executions_shrink
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Executions') is not None:
            self.executions_shrink = m.get('Executions')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateScheduledPreloadExecutionsResponseBodyFailedExecutions(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        end_time: str = None,
        id: str = None,
        interval: int = None,
        job_id: str = None,
        slice_len: int = None,
        start_time: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.end_time = end_time
        self.id = id
        self.interval = interval
        self.job_id = job_id
        self.slice_len = slice_len
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateScheduledPreloadExecutionsResponseBodySuccessExecutions(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        end_time: str = None,
        id: str = None,
        interval: int = None,
        job_id: str = None,
        slice_len: int = None,
        start_time: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.end_time = end_time
        self.id = id
        self.interval = interval
        self.job_id = job_id
        self.slice_len = slice_len
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateScheduledPreloadExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        failed_executions: List[CreateScheduledPreloadExecutionsResponseBodyFailedExecutions] = None,
        failed_messages: List[str] = None,
        request_id: str = None,
        success_count: int = None,
        success_executions: List[CreateScheduledPreloadExecutionsResponseBodySuccessExecutions] = None,
        total_count: int = None,
    ):
        self.failed_executions = failed_executions
        self.failed_messages = failed_messages
        # Id of the request
        self.request_id = request_id
        self.success_count = success_count
        self.success_executions = success_executions
        self.total_count = total_count

    def validate(self):
        if self.failed_executions:
            for k in self.failed_executions:
                if k:
                    k.validate()
        if self.success_executions:
            for k in self.success_executions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedExecutions'] = []
        if self.failed_executions is not None:
            for k in self.failed_executions:
                result['FailedExecutions'].append(k.to_map() if k else None)
        if self.failed_messages is not None:
            result['FailedMessages'] = self.failed_messages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        result['SuccessExecutions'] = []
        if self.success_executions is not None:
            for k in self.success_executions:
                result['SuccessExecutions'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_executions = []
        if m.get('FailedExecutions') is not None:
            for k in m.get('FailedExecutions'):
                temp_model = CreateScheduledPreloadExecutionsResponseBodyFailedExecutions()
                self.failed_executions.append(temp_model.from_map(k))
        if m.get('FailedMessages') is not None:
            self.failed_messages = m.get('FailedMessages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        self.success_executions = []
        if m.get('SuccessExecutions') is not None:
            for k in m.get('SuccessExecutions'):
                temp_model = CreateScheduledPreloadExecutionsResponseBodySuccessExecutions()
                self.success_executions.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CreateScheduledPreloadExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScheduledPreloadExecutionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScheduledPreloadExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledPreloadJobRequest(TeaModel):
    def __init__(
        self,
        insert_way: str = None,
        name: str = None,
        oss_url: str = None,
        site_id: int = None,
        url_list: str = None,
    ):
        # This parameter is required.
        self.insert_way = insert_way
        # This parameter is required.
        self.name = name
        self.oss_url = oss_url
        # This parameter is required.
        self.site_id = site_id
        self.url_list = url_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.insert_way is not None:
            result['InsertWay'] = self.insert_way
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.url_list is not None:
            result['UrlList'] = self.url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InsertWay') is not None:
            self.insert_way = m.get('InsertWay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('UrlList') is not None:
            self.url_list = m.get('UrlList')
        return self


class CreateScheduledPreloadJobResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        created_at: str = None,
        domains: str = None,
        error_info: str = None,
        failed_file_oss: str = None,
        file_id: str = None,
        id: str = None,
        insert_way: str = None,
        name: str = None,
        request_id: str = None,
        site_id: int = None,
        task_submitted: int = None,
        task_type: str = None,
        url_count: int = None,
        url_submitted: int = None,
    ):
        self.ali_uid = ali_uid
        self.created_at = created_at
        self.domains = domains
        self.error_info = error_info
        self.failed_file_oss = failed_file_oss
        self.file_id = file_id
        self.id = id
        self.insert_way = insert_way
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id
        self.task_submitted = task_submitted
        self.task_type = task_type
        self.url_count = url_count
        self.url_submitted = url_submitted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.failed_file_oss is not None:
            result['FailedFileOss'] = self.failed_file_oss
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id is not None:
            result['Id'] = self.id
        if self.insert_way is not None:
            result['InsertWay'] = self.insert_way
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.task_submitted is not None:
            result['TaskSubmitted'] = self.task_submitted
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.url_count is not None:
            result['UrlCount'] = self.url_count
        if self.url_submitted is not None:
            result['UrlSubmitted'] = self.url_submitted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('FailedFileOss') is not None:
            self.failed_file_oss = m.get('FailedFileOss')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsertWay') is not None:
            self.insert_way = m.get('InsertWay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaskSubmitted') is not None:
            self.task_submitted = m.get('TaskSubmitted')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UrlCount') is not None:
            self.url_count = m.get('UrlCount')
        if m.get('UrlSubmitted') is not None:
            self.url_submitted = m.get('UrlSubmitted')
        return self


class CreateScheduledPreloadJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScheduledPreloadJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScheduledPreloadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSiteRequest(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        coverage: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        site_name: str = None,
    ):
        # This parameter is required.
        self.access_type = access_type
        # This parameter is required.
        self.coverage = coverage
        # This parameter is required.
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id
        # 记录名称
        # 
        # This parameter is required.
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        return self


class CreateSiteResponseBody(TeaModel):
    def __init__(
        self,
        name_server_list: str = None,
        request_id: str = None,
        site_id: int = None,
        verify_code: str = None,
    ):
        self.name_server_list = name_server_list
        self.request_id = request_id
        self.site_id = site_id
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_server_list is not None:
            result['NameServerList'] = self.name_server_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameServerList') is not None:
            self.name_server_list = m.get('NameServerList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class CreateSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSiteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSiteCustomLogRequest(TeaModel):
    def __init__(
        self,
        cookies: List[str] = None,
        request_headers: List[str] = None,
        response_headers: List[str] = None,
        site_id: int = None,
    ):
        self.cookies = cookies
        self.request_headers = request_headers
        self.response_headers = response_headers
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers
        if self.response_headers is not None:
            result['ResponseHeaders'] = self.response_headers
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')
        if m.get('ResponseHeaders') is not None:
            self.response_headers = m.get('ResponseHeaders')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class CreateSiteCustomLogShrinkRequest(TeaModel):
    def __init__(
        self,
        cookies_shrink: str = None,
        request_headers_shrink: str = None,
        response_headers_shrink: str = None,
        site_id: int = None,
    ):
        self.cookies_shrink = cookies_shrink
        self.request_headers_shrink = request_headers_shrink
        self.response_headers_shrink = response_headers_shrink
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookies_shrink is not None:
            result['Cookies'] = self.cookies_shrink
        if self.request_headers_shrink is not None:
            result['RequestHeaders'] = self.request_headers_shrink
        if self.response_headers_shrink is not None:
            result['ResponseHeaders'] = self.response_headers_shrink
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookies') is not None:
            self.cookies_shrink = m.get('Cookies')
        if m.get('RequestHeaders') is not None:
            self.request_headers_shrink = m.get('RequestHeaders')
        if m.get('ResponseHeaders') is not None:
            self.response_headers_shrink = m.get('ResponseHeaders')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class CreateSiteCustomLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSiteCustomLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSiteCustomLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSiteCustomLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSiteDeliveryTaskRequestHttpDeliveryStandardAuthParam(TeaModel):
    def __init__(
        self,
        expired_time: int = None,
        private_key: str = None,
        url_path: str = None,
    ):
        self.expired_time = expired_time
        self.private_key = private_key
        self.url_path = url_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.url_path is not None:
            result['UrlPath'] = self.url_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('UrlPath') is not None:
            self.url_path = m.get('UrlPath')
        return self


class CreateSiteDeliveryTaskRequestHttpDelivery(TeaModel):
    def __init__(
        self,
        compress: str = None,
        dest_url: str = None,
        header_param: Dict[str, HttpDeliveryHeaderParamValue] = None,
        log_body_prefix: str = None,
        log_body_suffix: str = None,
        max_batch_mb: int = None,
        max_batch_size: int = None,
        max_retry: int = None,
        query_param: Dict[str, HttpDeliveryQueryParamValue] = None,
        standard_auth_on: bool = None,
        standard_auth_param: CreateSiteDeliveryTaskRequestHttpDeliveryStandardAuthParam = None,
        transform_timeout: int = None,
    ):
        self.compress = compress
        self.dest_url = dest_url
        self.header_param = header_param
        self.log_body_prefix = log_body_prefix
        self.log_body_suffix = log_body_suffix
        self.max_batch_mb = max_batch_mb
        self.max_batch_size = max_batch_size
        self.max_retry = max_retry
        self.query_param = query_param
        self.standard_auth_on = standard_auth_on
        self.standard_auth_param = standard_auth_param
        self.transform_timeout = transform_timeout

    def validate(self):
        if self.header_param:
            for v in self.header_param.values():
                if v:
                    v.validate()
        if self.query_param:
            for v in self.query_param.values():
                if v:
                    v.validate()
        if self.standard_auth_param:
            self.standard_auth_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress is not None:
            result['Compress'] = self.compress
        if self.dest_url is not None:
            result['DestUrl'] = self.dest_url
        result['HeaderParam'] = {}
        if self.header_param is not None:
            for k, v in self.header_param.items():
                result['HeaderParam'][k] = v.to_map()
        if self.log_body_prefix is not None:
            result['LogBodyPrefix'] = self.log_body_prefix
        if self.log_body_suffix is not None:
            result['LogBodySuffix'] = self.log_body_suffix
        if self.max_batch_mb is not None:
            result['MaxBatchMB'] = self.max_batch_mb
        if self.max_batch_size is not None:
            result['MaxBatchSize'] = self.max_batch_size
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        result['QueryParam'] = {}
        if self.query_param is not None:
            for k, v in self.query_param.items():
                result['QueryParam'][k] = v.to_map()
        if self.standard_auth_on is not None:
            result['StandardAuthOn'] = self.standard_auth_on
        if self.standard_auth_param is not None:
            result['StandardAuthParam'] = self.standard_auth_param.to_map()
        if self.transform_timeout is not None:
            result['TransformTimeout'] = self.transform_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compress') is not None:
            self.compress = m.get('Compress')
        if m.get('DestUrl') is not None:
            self.dest_url = m.get('DestUrl')
        self.header_param = {}
        if m.get('HeaderParam') is not None:
            for k, v in m.get('HeaderParam').items():
                temp_model = HttpDeliveryHeaderParamValue()
                self.header_param[k] = temp_model.from_map(v)
        if m.get('LogBodyPrefix') is not None:
            self.log_body_prefix = m.get('LogBodyPrefix')
        if m.get('LogBodySuffix') is not None:
            self.log_body_suffix = m.get('LogBodySuffix')
        if m.get('MaxBatchMB') is not None:
            self.max_batch_mb = m.get('MaxBatchMB')
        if m.get('MaxBatchSize') is not None:
            self.max_batch_size = m.get('MaxBatchSize')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        self.query_param = {}
        if m.get('QueryParam') is not None:
            for k, v in m.get('QueryParam').items():
                temp_model = HttpDeliveryQueryParamValue()
                self.query_param[k] = temp_model.from_map(v)
        if m.get('StandardAuthOn') is not None:
            self.standard_auth_on = m.get('StandardAuthOn')
        if m.get('StandardAuthParam') is not None:
            temp_model = CreateSiteDeliveryTaskRequestHttpDeliveryStandardAuthParam()
            self.standard_auth_param = temp_model.from_map(m['StandardAuthParam'])
        if m.get('TransformTimeout') is not None:
            self.transform_timeout = m.get('TransformTimeout')
        return self


class CreateSiteDeliveryTaskRequestKafkaDelivery(TeaModel):
    def __init__(
        self,
        balancer: str = None,
        brokers: List[str] = None,
        compress: str = None,
        machanism_type: str = None,
        password: str = None,
        topic: str = None,
        user_auth: bool = None,
        user_name: str = None,
    ):
        self.balancer = balancer
        self.brokers = brokers
        self.compress = compress
        self.machanism_type = machanism_type
        self.password = password
        self.topic = topic
        self.user_auth = user_auth
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.balancer is not None:
            result['Balancer'] = self.balancer
        if self.brokers is not None:
            result['Brokers'] = self.brokers
        if self.compress is not None:
            result['Compress'] = self.compress
        if self.machanism_type is not None:
            result['MachanismType'] = self.machanism_type
        if self.password is not None:
            result['Password'] = self.password
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.user_auth is not None:
            result['UserAuth'] = self.user_auth
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Balancer') is not None:
            self.balancer = m.get('Balancer')
        if m.get('Brokers') is not None:
            self.brokers = m.get('Brokers')
        if m.get('Compress') is not None:
            self.compress = m.get('Compress')
        if m.get('MachanismType') is not None:
            self.machanism_type = m.get('MachanismType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('UserAuth') is not None:
            self.user_auth = m.get('UserAuth')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateSiteDeliveryTaskRequestOssDelivery(TeaModel):
    def __init__(
        self,
        aliuid: str = None,
        bucket_name: str = None,
        prefix_path: str = None,
        region: str = None,
    ):
        self.aliuid = aliuid
        self.bucket_name = bucket_name
        self.prefix_path = prefix_path
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.prefix_path is not None:
            result['PrefixPath'] = self.prefix_path
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('PrefixPath') is not None:
            self.prefix_path = m.get('PrefixPath')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateSiteDeliveryTaskRequestS3Delivery(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        bucket_path: str = None,
        endpoint: str = None,
        prefix_path: str = None,
        region: str = None,
        s_3cmpt: bool = None,
        secret_key: str = None,
        server_side_encryption: bool = None,
        vertify_type: str = None,
    ):
        self.access_key = access_key
        self.bucket_path = bucket_path
        self.endpoint = endpoint
        self.prefix_path = prefix_path
        self.region = region
        self.s_3cmpt = s_3cmpt
        self.secret_key = secret_key
        self.server_side_encryption = server_side_encryption
        self.vertify_type = vertify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.bucket_path is not None:
            result['BucketPath'] = self.bucket_path
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.prefix_path is not None:
            result['PrefixPath'] = self.prefix_path
        if self.region is not None:
            result['Region'] = self.region
        if self.s_3cmpt is not None:
            result['S3Cmpt'] = self.s_3cmpt
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.server_side_encryption is not None:
            result['ServerSideEncryption'] = self.server_side_encryption
        if self.vertify_type is not None:
            result['VertifyType'] = self.vertify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('BucketPath') is not None:
            self.bucket_path = m.get('BucketPath')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('PrefixPath') is not None:
            self.prefix_path = m.get('PrefixPath')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('S3Cmpt') is not None:
            self.s_3cmpt = m.get('S3Cmpt')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('ServerSideEncryption') is not None:
            self.server_side_encryption = m.get('ServerSideEncryption')
        if m.get('VertifyType') is not None:
            self.vertify_type = m.get('VertifyType')
        return self


class CreateSiteDeliveryTaskRequestSlsDelivery(TeaModel):
    def __init__(
        self,
        slslog_store: str = None,
        slsproject: str = None,
        slsregion: str = None,
    ):
        self.slslog_store = slslog_store
        self.slsproject = slsproject
        self.slsregion = slsregion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store
        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject
        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')
        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')
        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')
        return self


class CreateSiteDeliveryTaskRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        discard_rate: float = None,
        field_name: str = None,
        http_delivery: CreateSiteDeliveryTaskRequestHttpDelivery = None,
        kafka_delivery: CreateSiteDeliveryTaskRequestKafkaDelivery = None,
        oss_delivery: CreateSiteDeliveryTaskRequestOssDelivery = None,
        s_3delivery: CreateSiteDeliveryTaskRequestS3Delivery = None,
        site_id: int = None,
        sls_delivery: CreateSiteDeliveryTaskRequestSlsDelivery = None,
        task_name: str = None,
    ):
        # This parameter is required.
        self.business_type = business_type
        # This parameter is required.
        self.data_center = data_center
        # This parameter is required.
        self.delivery_type = delivery_type
        self.discard_rate = discard_rate
        # This parameter is required.
        self.field_name = field_name
        self.http_delivery = http_delivery
        self.kafka_delivery = kafka_delivery
        self.oss_delivery = oss_delivery
        self.s_3delivery = s_3delivery
        # This parameter is required.
        self.site_id = site_id
        self.sls_delivery = sls_delivery
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        if self.http_delivery:
            self.http_delivery.validate()
        if self.kafka_delivery:
            self.kafka_delivery.validate()
        if self.oss_delivery:
            self.oss_delivery.validate()
        if self.s_3delivery:
            self.s_3delivery.validate()
        if self.sls_delivery:
            self.sls_delivery.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.http_delivery is not None:
            result['HttpDelivery'] = self.http_delivery.to_map()
        if self.kafka_delivery is not None:
            result['KafkaDelivery'] = self.kafka_delivery.to_map()
        if self.oss_delivery is not None:
            result['OssDelivery'] = self.oss_delivery.to_map()
        if self.s_3delivery is not None:
            result['S3Delivery'] = self.s_3delivery.to_map()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.sls_delivery is not None:
            result['SlsDelivery'] = self.sls_delivery.to_map()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('HttpDelivery') is not None:
            temp_model = CreateSiteDeliveryTaskRequestHttpDelivery()
            self.http_delivery = temp_model.from_map(m['HttpDelivery'])
        if m.get('KafkaDelivery') is not None:
            temp_model = CreateSiteDeliveryTaskRequestKafkaDelivery()
            self.kafka_delivery = temp_model.from_map(m['KafkaDelivery'])
        if m.get('OssDelivery') is not None:
            temp_model = CreateSiteDeliveryTaskRequestOssDelivery()
            self.oss_delivery = temp_model.from_map(m['OssDelivery'])
        if m.get('S3Delivery') is not None:
            temp_model = CreateSiteDeliveryTaskRequestS3Delivery()
            self.s_3delivery = temp_model.from_map(m['S3Delivery'])
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SlsDelivery') is not None:
            temp_model = CreateSiteDeliveryTaskRequestSlsDelivery()
            self.sls_delivery = temp_model.from_map(m['SlsDelivery'])
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateSiteDeliveryTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        discard_rate: float = None,
        field_name: str = None,
        http_delivery_shrink: str = None,
        kafka_delivery_shrink: str = None,
        oss_delivery_shrink: str = None,
        s_3delivery_shrink: str = None,
        site_id: int = None,
        sls_delivery_shrink: str = None,
        task_name: str = None,
    ):
        # This parameter is required.
        self.business_type = business_type
        # This parameter is required.
        self.data_center = data_center
        # This parameter is required.
        self.delivery_type = delivery_type
        self.discard_rate = discard_rate
        # This parameter is required.
        self.field_name = field_name
        self.http_delivery_shrink = http_delivery_shrink
        self.kafka_delivery_shrink = kafka_delivery_shrink
        self.oss_delivery_shrink = oss_delivery_shrink
        self.s_3delivery_shrink = s_3delivery_shrink
        # This parameter is required.
        self.site_id = site_id
        self.sls_delivery_shrink = sls_delivery_shrink
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.http_delivery_shrink is not None:
            result['HttpDelivery'] = self.http_delivery_shrink
        if self.kafka_delivery_shrink is not None:
            result['KafkaDelivery'] = self.kafka_delivery_shrink
        if self.oss_delivery_shrink is not None:
            result['OssDelivery'] = self.oss_delivery_shrink
        if self.s_3delivery_shrink is not None:
            result['S3Delivery'] = self.s_3delivery_shrink
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.sls_delivery_shrink is not None:
            result['SlsDelivery'] = self.sls_delivery_shrink
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('HttpDelivery') is not None:
            self.http_delivery_shrink = m.get('HttpDelivery')
        if m.get('KafkaDelivery') is not None:
            self.kafka_delivery_shrink = m.get('KafkaDelivery')
        if m.get('OssDelivery') is not None:
            self.oss_delivery_shrink = m.get('OssDelivery')
        if m.get('S3Delivery') is not None:
            self.s_3delivery_shrink = m.get('S3Delivery')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SlsDelivery') is not None:
            self.sls_delivery_shrink = m.get('SlsDelivery')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateSiteDeliveryTaskResponseBody(TeaModel):
    def __init__(
        self,
        data_center: str = None,
        request_id: str = None,
        site_id: str = None,
        task_name: str = None,
    ):
        self.data_center = data_center
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateSiteDeliveryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSiteDeliveryTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSiteDeliveryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserDeliveryTaskRequestHttpDeliveryStandardAuthParam(TeaModel):
    def __init__(
        self,
        expired_time: int = None,
        private_key: str = None,
        url_path: str = None,
    ):
        self.expired_time = expired_time
        self.private_key = private_key
        self.url_path = url_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.url_path is not None:
            result['UrlPath'] = self.url_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('UrlPath') is not None:
            self.url_path = m.get('UrlPath')
        return self


class CreateUserDeliveryTaskRequestHttpDelivery(TeaModel):
    def __init__(
        self,
        compress: str = None,
        dest_url: str = None,
        header_param: Dict[str, HttpDeliveryHeaderParamValue] = None,
        last_log_split: str = None,
        log_body_prefix: str = None,
        log_body_suffix: str = None,
        log_split: str = None,
        log_split_words: str = None,
        max_backoff_ms: int = None,
        max_batch_mb: int = None,
        max_batch_size: int = None,
        max_retry: int = None,
        min_backoff_ms: int = None,
        query_param: Dict[str, HttpDeliveryQueryParamValue] = None,
        response_body_key: str = None,
        standard_auth_on: bool = None,
        standard_auth_param: CreateUserDeliveryTaskRequestHttpDeliveryStandardAuthParam = None,
        success_code: int = None,
        transform_timeout: int = None,
    ):
        self.compress = compress
        self.dest_url = dest_url
        self.header_param = header_param
        self.last_log_split = last_log_split
        self.log_body_prefix = log_body_prefix
        self.log_body_suffix = log_body_suffix
        self.log_split = log_split
        self.log_split_words = log_split_words
        self.max_backoff_ms = max_backoff_ms
        self.max_batch_mb = max_batch_mb
        self.max_batch_size = max_batch_size
        self.max_retry = max_retry
        self.min_backoff_ms = min_backoff_ms
        self.query_param = query_param
        self.response_body_key = response_body_key
        self.standard_auth_on = standard_auth_on
        self.standard_auth_param = standard_auth_param
        self.success_code = success_code
        self.transform_timeout = transform_timeout

    def validate(self):
        if self.header_param:
            for v in self.header_param.values():
                if v:
                    v.validate()
        if self.query_param:
            for v in self.query_param.values():
                if v:
                    v.validate()
        if self.standard_auth_param:
            self.standard_auth_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress is not None:
            result['Compress'] = self.compress
        if self.dest_url is not None:
            result['DestUrl'] = self.dest_url
        result['HeaderParam'] = {}
        if self.header_param is not None:
            for k, v in self.header_param.items():
                result['HeaderParam'][k] = v.to_map()
        if self.last_log_split is not None:
            result['LastLogSplit'] = self.last_log_split
        if self.log_body_prefix is not None:
            result['LogBodyPrefix'] = self.log_body_prefix
        if self.log_body_suffix is not None:
            result['LogBodySuffix'] = self.log_body_suffix
        if self.log_split is not None:
            result['LogSplit'] = self.log_split
        if self.log_split_words is not None:
            result['LogSplitWords'] = self.log_split_words
        if self.max_backoff_ms is not None:
            result['MaxBackoffMS'] = self.max_backoff_ms
        if self.max_batch_mb is not None:
            result['MaxBatchMB'] = self.max_batch_mb
        if self.max_batch_size is not None:
            result['MaxBatchSize'] = self.max_batch_size
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        if self.min_backoff_ms is not None:
            result['MinBackoffMS'] = self.min_backoff_ms
        result['QueryParam'] = {}
        if self.query_param is not None:
            for k, v in self.query_param.items():
                result['QueryParam'][k] = v.to_map()
        if self.response_body_key is not None:
            result['ResponseBodyKey'] = self.response_body_key
        if self.standard_auth_on is not None:
            result['StandardAuthOn'] = self.standard_auth_on
        if self.standard_auth_param is not None:
            result['StandardAuthParam'] = self.standard_auth_param.to_map()
        if self.success_code is not None:
            result['SuccessCode'] = self.success_code
        if self.transform_timeout is not None:
            result['TransformTimeout'] = self.transform_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compress') is not None:
            self.compress = m.get('Compress')
        if m.get('DestUrl') is not None:
            self.dest_url = m.get('DestUrl')
        self.header_param = {}
        if m.get('HeaderParam') is not None:
            for k, v in m.get('HeaderParam').items():
                temp_model = HttpDeliveryHeaderParamValue()
                self.header_param[k] = temp_model.from_map(v)
        if m.get('LastLogSplit') is not None:
            self.last_log_split = m.get('LastLogSplit')
        if m.get('LogBodyPrefix') is not None:
            self.log_body_prefix = m.get('LogBodyPrefix')
        if m.get('LogBodySuffix') is not None:
            self.log_body_suffix = m.get('LogBodySuffix')
        if m.get('LogSplit') is not None:
            self.log_split = m.get('LogSplit')
        if m.get('LogSplitWords') is not None:
            self.log_split_words = m.get('LogSplitWords')
        if m.get('MaxBackoffMS') is not None:
            self.max_backoff_ms = m.get('MaxBackoffMS')
        if m.get('MaxBatchMB') is not None:
            self.max_batch_mb = m.get('MaxBatchMB')
        if m.get('MaxBatchSize') is not None:
            self.max_batch_size = m.get('MaxBatchSize')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        if m.get('MinBackoffMS') is not None:
            self.min_backoff_ms = m.get('MinBackoffMS')
        self.query_param = {}
        if m.get('QueryParam') is not None:
            for k, v in m.get('QueryParam').items():
                temp_model = HttpDeliveryQueryParamValue()
                self.query_param[k] = temp_model.from_map(v)
        if m.get('ResponseBodyKey') is not None:
            self.response_body_key = m.get('ResponseBodyKey')
        if m.get('StandardAuthOn') is not None:
            self.standard_auth_on = m.get('StandardAuthOn')
        if m.get('StandardAuthParam') is not None:
            temp_model = CreateUserDeliveryTaskRequestHttpDeliveryStandardAuthParam()
            self.standard_auth_param = temp_model.from_map(m['StandardAuthParam'])
        if m.get('SuccessCode') is not None:
            self.success_code = m.get('SuccessCode')
        if m.get('TransformTimeout') is not None:
            self.transform_timeout = m.get('TransformTimeout')
        return self


class CreateUserDeliveryTaskRequestKafkaDelivery(TeaModel):
    def __init__(
        self,
        balancer: str = None,
        brokers: List[str] = None,
        compress: str = None,
        machanism_type: str = None,
        password: str = None,
        topic: str = None,
        user_auth: bool = None,
        user_name: str = None,
    ):
        self.balancer = balancer
        self.brokers = brokers
        self.compress = compress
        self.machanism_type = machanism_type
        self.password = password
        self.topic = topic
        self.user_auth = user_auth
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.balancer is not None:
            result['Balancer'] = self.balancer
        if self.brokers is not None:
            result['Brokers'] = self.brokers
        if self.compress is not None:
            result['Compress'] = self.compress
        if self.machanism_type is not None:
            result['MachanismType'] = self.machanism_type
        if self.password is not None:
            result['Password'] = self.password
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.user_auth is not None:
            result['UserAuth'] = self.user_auth
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Balancer') is not None:
            self.balancer = m.get('Balancer')
        if m.get('Brokers') is not None:
            self.brokers = m.get('Brokers')
        if m.get('Compress') is not None:
            self.compress = m.get('Compress')
        if m.get('MachanismType') is not None:
            self.machanism_type = m.get('MachanismType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('UserAuth') is not None:
            self.user_auth = m.get('UserAuth')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserDeliveryTaskRequestOssDelivery(TeaModel):
    def __init__(
        self,
        aliuid: str = None,
        bucket_name: str = None,
        prefix_path: str = None,
        region: str = None,
    ):
        self.aliuid = aliuid
        self.bucket_name = bucket_name
        self.prefix_path = prefix_path
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.prefix_path is not None:
            result['PrefixPath'] = self.prefix_path
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('PrefixPath') is not None:
            self.prefix_path = m.get('PrefixPath')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateUserDeliveryTaskRequestS3Delivery(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        bucket_path: str = None,
        endpoint: str = None,
        prefix_path: str = None,
        region: str = None,
        s_3cmpt: bool = None,
        secret_key: str = None,
        server_side_encryption: bool = None,
        vertify_type: str = None,
    ):
        self.access_key = access_key
        self.bucket_path = bucket_path
        self.endpoint = endpoint
        self.prefix_path = prefix_path
        self.region = region
        self.s_3cmpt = s_3cmpt
        self.secret_key = secret_key
        self.server_side_encryption = server_side_encryption
        self.vertify_type = vertify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.bucket_path is not None:
            result['BucketPath'] = self.bucket_path
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.prefix_path is not None:
            result['PrefixPath'] = self.prefix_path
        if self.region is not None:
            result['Region'] = self.region
        if self.s_3cmpt is not None:
            result['S3Cmpt'] = self.s_3cmpt
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.server_side_encryption is not None:
            result['ServerSideEncryption'] = self.server_side_encryption
        if self.vertify_type is not None:
            result['VertifyType'] = self.vertify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('BucketPath') is not None:
            self.bucket_path = m.get('BucketPath')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('PrefixPath') is not None:
            self.prefix_path = m.get('PrefixPath')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('S3Cmpt') is not None:
            self.s_3cmpt = m.get('S3Cmpt')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('ServerSideEncryption') is not None:
            self.server_side_encryption = m.get('ServerSideEncryption')
        if m.get('VertifyType') is not None:
            self.vertify_type = m.get('VertifyType')
        return self


class CreateUserDeliveryTaskRequestSlsDelivery(TeaModel):
    def __init__(
        self,
        slslog_store: str = None,
        slsproject: str = None,
        slsregion: str = None,
    ):
        self.slslog_store = slslog_store
        self.slsproject = slsproject
        self.slsregion = slsregion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store
        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject
        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')
        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')
        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')
        return self


class CreateUserDeliveryTaskRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        discard_rate: float = None,
        field_name: str = None,
        http_delivery: CreateUserDeliveryTaskRequestHttpDelivery = None,
        kafka_delivery: CreateUserDeliveryTaskRequestKafkaDelivery = None,
        oss_delivery: CreateUserDeliveryTaskRequestOssDelivery = None,
        s_3delivery: CreateUserDeliveryTaskRequestS3Delivery = None,
        sls_delivery: CreateUserDeliveryTaskRequestSlsDelivery = None,
        task_name: str = None,
    ):
        # This parameter is required.
        self.business_type = business_type
        # This parameter is required.
        self.data_center = data_center
        # This parameter is required.
        self.delivery_type = delivery_type
        self.discard_rate = discard_rate
        # This parameter is required.
        self.field_name = field_name
        self.http_delivery = http_delivery
        self.kafka_delivery = kafka_delivery
        self.oss_delivery = oss_delivery
        self.s_3delivery = s_3delivery
        self.sls_delivery = sls_delivery
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        if self.http_delivery:
            self.http_delivery.validate()
        if self.kafka_delivery:
            self.kafka_delivery.validate()
        if self.oss_delivery:
            self.oss_delivery.validate()
        if self.s_3delivery:
            self.s_3delivery.validate()
        if self.sls_delivery:
            self.sls_delivery.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.http_delivery is not None:
            result['HttpDelivery'] = self.http_delivery.to_map()
        if self.kafka_delivery is not None:
            result['KafkaDelivery'] = self.kafka_delivery.to_map()
        if self.oss_delivery is not None:
            result['OssDelivery'] = self.oss_delivery.to_map()
        if self.s_3delivery is not None:
            result['S3Delivery'] = self.s_3delivery.to_map()
        if self.sls_delivery is not None:
            result['SlsDelivery'] = self.sls_delivery.to_map()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('HttpDelivery') is not None:
            temp_model = CreateUserDeliveryTaskRequestHttpDelivery()
            self.http_delivery = temp_model.from_map(m['HttpDelivery'])
        if m.get('KafkaDelivery') is not None:
            temp_model = CreateUserDeliveryTaskRequestKafkaDelivery()
            self.kafka_delivery = temp_model.from_map(m['KafkaDelivery'])
        if m.get('OssDelivery') is not None:
            temp_model = CreateUserDeliveryTaskRequestOssDelivery()
            self.oss_delivery = temp_model.from_map(m['OssDelivery'])
        if m.get('S3Delivery') is not None:
            temp_model = CreateUserDeliveryTaskRequestS3Delivery()
            self.s_3delivery = temp_model.from_map(m['S3Delivery'])
        if m.get('SlsDelivery') is not None:
            temp_model = CreateUserDeliveryTaskRequestSlsDelivery()
            self.sls_delivery = temp_model.from_map(m['SlsDelivery'])
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateUserDeliveryTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        discard_rate: float = None,
        field_name: str = None,
        http_delivery_shrink: str = None,
        kafka_delivery_shrink: str = None,
        oss_delivery_shrink: str = None,
        s_3delivery_shrink: str = None,
        sls_delivery_shrink: str = None,
        task_name: str = None,
    ):
        # This parameter is required.
        self.business_type = business_type
        # This parameter is required.
        self.data_center = data_center
        # This parameter is required.
        self.delivery_type = delivery_type
        self.discard_rate = discard_rate
        # This parameter is required.
        self.field_name = field_name
        self.http_delivery_shrink = http_delivery_shrink
        self.kafka_delivery_shrink = kafka_delivery_shrink
        self.oss_delivery_shrink = oss_delivery_shrink
        self.s_3delivery_shrink = s_3delivery_shrink
        self.sls_delivery_shrink = sls_delivery_shrink
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.http_delivery_shrink is not None:
            result['HttpDelivery'] = self.http_delivery_shrink
        if self.kafka_delivery_shrink is not None:
            result['KafkaDelivery'] = self.kafka_delivery_shrink
        if self.oss_delivery_shrink is not None:
            result['OssDelivery'] = self.oss_delivery_shrink
        if self.s_3delivery_shrink is not None:
            result['S3Delivery'] = self.s_3delivery_shrink
        if self.sls_delivery_shrink is not None:
            result['SlsDelivery'] = self.sls_delivery_shrink
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('HttpDelivery') is not None:
            self.http_delivery_shrink = m.get('HttpDelivery')
        if m.get('KafkaDelivery') is not None:
            self.kafka_delivery_shrink = m.get('KafkaDelivery')
        if m.get('OssDelivery') is not None:
            self.oss_delivery_shrink = m.get('OssDelivery')
        if m.get('S3Delivery') is not None:
            self.s_3delivery_shrink = m.get('S3Delivery')
        if m.get('SlsDelivery') is not None:
            self.sls_delivery_shrink = m.get('SlsDelivery')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateUserDeliveryTaskResponseBody(TeaModel):
    def __init__(
        self,
        data_center: str = None,
        request_id: str = None,
        status: str = None,
        task_name: str = None,
    ):
        self.data_center = data_center
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateUserDeliveryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserDeliveryTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUserDeliveryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWafRuleRequest(TeaModel):
    def __init__(
        self,
        config: WafRuleConfig = None,
        phase: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.config = config
        # This parameter is required.
        self.phase = phase
        # This parameter is required.
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = WafRuleConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class CreateWafRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        config_shrink: str = None,
        phase: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.config_shrink = config_shrink
        # This parameter is required.
        self.phase = phase
        # This parameter is required.
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class CreateWafRuleResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
        ruleset_id: int = None,
    ):
        self.id = id
        # Id of the request
        self.request_id = request_id
        self.ruleset_id = ruleset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')
        return self


class CreateWafRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWafRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWafRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWaitingRoomRequestHostNameAndPath(TeaModel):
    def __init__(
        self,
        domain: str = None,
        path: str = None,
        subdomain: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.path = path
        # This parameter is required.
        self.subdomain = subdomain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.path is not None:
            result['Path'] = self.path
        if self.subdomain is not None:
            result['Subdomain'] = self.subdomain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Subdomain') is not None:
            self.subdomain = m.get('Subdomain')
        return self


class CreateWaitingRoomRequest(TeaModel):
    def __init__(
        self,
        cookie_name: str = None,
        custom_page_html: str = None,
        description: str = None,
        disable_session_renewal_enable: str = None,
        enable: str = None,
        host_name_and_path: List[CreateWaitingRoomRequestHostNameAndPath] = None,
        json_response_enable: str = None,
        language: str = None,
        name: str = None,
        new_users_per_minute: str = None,
        queue_all_enable: str = None,
        queuing_method: str = None,
        queuing_status_code: str = None,
        session_duration: str = None,
        site_id: int = None,
        total_active_users: str = None,
        waiting_room_type: str = None,
    ):
        # This parameter is required.
        self.cookie_name = cookie_name
        self.custom_page_html = custom_page_html
        self.description = description
        self.disable_session_renewal_enable = disable_session_renewal_enable
        # This parameter is required.
        self.enable = enable
        # This parameter is required.
        self.host_name_and_path = host_name_and_path
        self.json_response_enable = json_response_enable
        self.language = language
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.new_users_per_minute = new_users_per_minute
        self.queue_all_enable = queue_all_enable
        # This parameter is required.
        self.queuing_method = queuing_method
        # This parameter is required.
        self.queuing_status_code = queuing_status_code
        # This parameter is required.
        self.session_duration = session_duration
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.total_active_users = total_active_users
        # This parameter is required.
        self.waiting_room_type = waiting_room_type

    def validate(self):
        if self.host_name_and_path:
            for k in self.host_name_and_path:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_name is not None:
            result['CookieName'] = self.cookie_name
        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_session_renewal_enable is not None:
            result['DisableSessionRenewalEnable'] = self.disable_session_renewal_enable
        if self.enable is not None:
            result['Enable'] = self.enable
        result['HostNameAndPath'] = []
        if self.host_name_and_path is not None:
            for k in self.host_name_and_path:
                result['HostNameAndPath'].append(k.to_map() if k else None)
        if self.json_response_enable is not None:
            result['JsonResponseEnable'] = self.json_response_enable
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.new_users_per_minute is not None:
            result['NewUsersPerMinute'] = self.new_users_per_minute
        if self.queue_all_enable is not None:
            result['QueueAllEnable'] = self.queue_all_enable
        if self.queuing_method is not None:
            result['QueuingMethod'] = self.queuing_method
        if self.queuing_status_code is not None:
            result['QueuingStatusCode'] = self.queuing_status_code
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users
        if self.waiting_room_type is not None:
            result['WaitingRoomType'] = self.waiting_room_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieName') is not None:
            self.cookie_name = m.get('CookieName')
        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableSessionRenewalEnable') is not None:
            self.disable_session_renewal_enable = m.get('DisableSessionRenewalEnable')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        self.host_name_and_path = []
        if m.get('HostNameAndPath') is not None:
            for k in m.get('HostNameAndPath'):
                temp_model = CreateWaitingRoomRequestHostNameAndPath()
                self.host_name_and_path.append(temp_model.from_map(k))
        if m.get('JsonResponseEnable') is not None:
            self.json_response_enable = m.get('JsonResponseEnable')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewUsersPerMinute') is not None:
            self.new_users_per_minute = m.get('NewUsersPerMinute')
        if m.get('QueueAllEnable') is not None:
            self.queue_all_enable = m.get('QueueAllEnable')
        if m.get('QueuingMethod') is not None:
            self.queuing_method = m.get('QueuingMethod')
        if m.get('QueuingStatusCode') is not None:
            self.queuing_status_code = m.get('QueuingStatusCode')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')
        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')
        return self


class CreateWaitingRoomShrinkRequest(TeaModel):
    def __init__(
        self,
        cookie_name: str = None,
        custom_page_html: str = None,
        description: str = None,
        disable_session_renewal_enable: str = None,
        enable: str = None,
        host_name_and_path_shrink: str = None,
        json_response_enable: str = None,
        language: str = None,
        name: str = None,
        new_users_per_minute: str = None,
        queue_all_enable: str = None,
        queuing_method: str = None,
        queuing_status_code: str = None,
        session_duration: str = None,
        site_id: int = None,
        total_active_users: str = None,
        waiting_room_type: str = None,
    ):
        # This parameter is required.
        self.cookie_name = cookie_name
        self.custom_page_html = custom_page_html
        self.description = description
        self.disable_session_renewal_enable = disable_session_renewal_enable
        # This parameter is required.
        self.enable = enable
        # This parameter is required.
        self.host_name_and_path_shrink = host_name_and_path_shrink
        self.json_response_enable = json_response_enable
        self.language = language
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.new_users_per_minute = new_users_per_minute
        self.queue_all_enable = queue_all_enable
        # This parameter is required.
        self.queuing_method = queuing_method
        # This parameter is required.
        self.queuing_status_code = queuing_status_code
        # This parameter is required.
        self.session_duration = session_duration
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.total_active_users = total_active_users
        # This parameter is required.
        self.waiting_room_type = waiting_room_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_name is not None:
            result['CookieName'] = self.cookie_name
        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_session_renewal_enable is not None:
            result['DisableSessionRenewalEnable'] = self.disable_session_renewal_enable
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.host_name_and_path_shrink is not None:
            result['HostNameAndPath'] = self.host_name_and_path_shrink
        if self.json_response_enable is not None:
            result['JsonResponseEnable'] = self.json_response_enable
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.new_users_per_minute is not None:
            result['NewUsersPerMinute'] = self.new_users_per_minute
        if self.queue_all_enable is not None:
            result['QueueAllEnable'] = self.queue_all_enable
        if self.queuing_method is not None:
            result['QueuingMethod'] = self.queuing_method
        if self.queuing_status_code is not None:
            result['QueuingStatusCode'] = self.queuing_status_code
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users
        if self.waiting_room_type is not None:
            result['WaitingRoomType'] = self.waiting_room_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieName') is not None:
            self.cookie_name = m.get('CookieName')
        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableSessionRenewalEnable') is not None:
            self.disable_session_renewal_enable = m.get('DisableSessionRenewalEnable')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('HostNameAndPath') is not None:
            self.host_name_and_path_shrink = m.get('HostNameAndPath')
        if m.get('JsonResponseEnable') is not None:
            self.json_response_enable = m.get('JsonResponseEnable')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewUsersPerMinute') is not None:
            self.new_users_per_minute = m.get('NewUsersPerMinute')
        if m.get('QueueAllEnable') is not None:
            self.queue_all_enable = m.get('QueueAllEnable')
        if m.get('QueuingMethod') is not None:
            self.queuing_method = m.get('QueuingMethod')
        if m.get('QueuingStatusCode') is not None:
            self.queuing_status_code = m.get('QueuingStatusCode')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')
        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')
        return self


class CreateWaitingRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWaitingRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWaitingRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWaitingRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWaitingRoomEventRequest(TeaModel):
    def __init__(
        self,
        custom_page_html: str = None,
        description: str = None,
        disable_session_renewal_enable: str = None,
        enable: str = None,
        end_time: str = None,
        json_response_enable: str = None,
        language: str = None,
        name: str = None,
        new_users_per_minute: str = None,
        pre_queue_enable: str = None,
        pre_queue_start_time: str = None,
        queuing_method: str = None,
        queuing_status_code: str = None,
        random_pre_queue_enable: str = None,
        session_duration: str = None,
        site_id: int = None,
        start_time: str = None,
        total_active_users: str = None,
        waiting_room_id: str = None,
        waiting_room_type: str = None,
    ):
        self.custom_page_html = custom_page_html
        self.description = description
        self.disable_session_renewal_enable = disable_session_renewal_enable
        # This parameter is required.
        self.enable = enable
        # This parameter is required.
        self.end_time = end_time
        self.json_response_enable = json_response_enable
        self.language = language
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.new_users_per_minute = new_users_per_minute
        self.pre_queue_enable = pre_queue_enable
        self.pre_queue_start_time = pre_queue_start_time
        # This parameter is required.
        self.queuing_method = queuing_method
        # This parameter is required.
        self.queuing_status_code = queuing_status_code
        self.random_pre_queue_enable = random_pre_queue_enable
        # This parameter is required.
        self.session_duration = session_duration
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.total_active_users = total_active_users
        self.waiting_room_id = waiting_room_id
        # This parameter is required.
        self.waiting_room_type = waiting_room_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_session_renewal_enable is not None:
            result['DisableSessionRenewalEnable'] = self.disable_session_renewal_enable
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.json_response_enable is not None:
            result['JsonResponseEnable'] = self.json_response_enable
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.new_users_per_minute is not None:
            result['NewUsersPerMinute'] = self.new_users_per_minute
        if self.pre_queue_enable is not None:
            result['PreQueueEnable'] = self.pre_queue_enable
        if self.pre_queue_start_time is not None:
            result['PreQueueStartTime'] = self.pre_queue_start_time
        if self.queuing_method is not None:
            result['QueuingMethod'] = self.queuing_method
        if self.queuing_status_code is not None:
            result['QueuingStatusCode'] = self.queuing_status_code
        if self.random_pre_queue_enable is not None:
            result['RandomPreQueueEnable'] = self.random_pre_queue_enable
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users
        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id
        if self.waiting_room_type is not None:
            result['WaitingRoomType'] = self.waiting_room_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableSessionRenewalEnable') is not None:
            self.disable_session_renewal_enable = m.get('DisableSessionRenewalEnable')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JsonResponseEnable') is not None:
            self.json_response_enable = m.get('JsonResponseEnable')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewUsersPerMinute') is not None:
            self.new_users_per_minute = m.get('NewUsersPerMinute')
        if m.get('PreQueueEnable') is not None:
            self.pre_queue_enable = m.get('PreQueueEnable')
        if m.get('PreQueueStartTime') is not None:
            self.pre_queue_start_time = m.get('PreQueueStartTime')
        if m.get('QueuingMethod') is not None:
            self.queuing_method = m.get('QueuingMethod')
        if m.get('QueuingStatusCode') is not None:
            self.queuing_status_code = m.get('QueuingStatusCode')
        if m.get('RandomPreQueueEnable') is not None:
            self.random_pre_queue_enable = m.get('RandomPreQueueEnable')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')
        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')
        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')
        return self


class CreateWaitingRoomEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWaitingRoomEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWaitingRoomEventResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWaitingRoomEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWaitingRoomRuleRequest(TeaModel):
    def __init__(
        self,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        site_id: int = None,
        waiting_room_id: str = None,
    ):
        # This parameter is required.
        self.rule = rule
        # This parameter is required.
        self.rule_enable = rule_enable
        # This parameter is required.
        self.rule_name = rule_name
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.waiting_room_id = waiting_room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')
        return self


class CreateWaitingRoomRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWaitingRoomRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWaitingRoomRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWaitingRoomRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomScenePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
    ):
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DeleteCustomScenePolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
        request_id: str = None,
    ):
        self.policy_id = policy_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCustomScenePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomScenePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCustomScenePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKvRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        namespace: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class DeleteKvResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKvResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteKvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKvNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class DeleteKvNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKvNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKvNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteKvNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteListRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePageRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeletePageResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordRequest(TeaModel):
    def __init__(
        self,
        record_id: int = None,
    ):
        # This parameter is required.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class DeleteRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoutineRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteRoutineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteRoutineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRoutineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRoutineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoutineCodeVersionRequest(TeaModel):
    def __init__(
        self,
        code_version: str = None,
        name: str = None,
    ):
        self.code_version = code_version
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteRoutineCodeVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteRoutineCodeVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRoutineCodeVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRoutineCodeVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoutineRelatedRecordRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        record_id: int = None,
        record_name: str = None,
        site_id: int = None,
    ):
        self.name = name
        self.record_id = record_id
        self.record_name = record_name
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class DeleteRoutineRelatedRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteRoutineRelatedRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRoutineRelatedRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRoutineRelatedRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoutineRelatedRouteRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        route: str = None,
        route_id: str = None,
        site_id: int = None,
    ):
        self.name = name
        self.route = route
        self.route_id = route_id
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.route is not None:
            result['Route'] = self.route
        if self.route_id is not None:
            result['RouteId'] = self.route_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class DeleteRoutineRelatedRouteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteRoutineRelatedRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRoutineRelatedRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRoutineRelatedRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduledPreloadExecutionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteScheduledPreloadExecutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScheduledPreloadExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScheduledPreloadExecutionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScheduledPreloadExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduledPreloadJobRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteScheduledPreloadJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScheduledPreloadJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScheduledPreloadJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScheduledPreloadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSiteRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        site_id: int = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class DeleteSiteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSiteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSiteDeliveryTaskRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        task_name: str = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DeleteSiteDeliveryTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSiteDeliveryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSiteDeliveryTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSiteDeliveryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserDeliveryTaskRequest(TeaModel):
    def __init__(
        self,
        task_name: str = None,
    ):
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DeleteUserDeliveryTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserDeliveryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserDeliveryTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserDeliveryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWafRuleRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class DeleteWafRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWafRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWafRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWafRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWafRulesetRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # This parameter is required.
        self.id = id
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class DeleteWafRulesetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWafRulesetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWafRulesetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWafRulesetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWaitingRoomRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        waiting_room_id: str = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.waiting_room_id = waiting_room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')
        return self


class DeleteWaitingRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWaitingRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWaitingRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWaitingRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWaitingRoomEventRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        waiting_room_event_id: int = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        self.waiting_room_event_id = waiting_room_event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.waiting_room_event_id is not None:
            result['WaitingRoomEventId'] = self.waiting_room_event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('WaitingRoomEventId') is not None:
            self.waiting_room_event_id = m.get('WaitingRoomEventId')
        return self


class DeleteWaitingRoomEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWaitingRoomEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWaitingRoomEventResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWaitingRoomEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWaitingRoomRuleRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        waiting_room_rule_id: int = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        self.waiting_room_rule_id = waiting_room_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.waiting_room_rule_id is not None:
            result['WaitingRoomRuleId'] = self.waiting_room_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('WaitingRoomRuleId') is not None:
            self.waiting_room_rule_id = m.get('WaitingRoomRuleId')
        return self


class DeleteWaitingRoomRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWaitingRoomRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWaitingRoomRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWaitingRoomRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomScenePoliciesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policy_id: int = None,
    ):
        # This parameter is required.
        self.page_number = page_number
        self.page_size = page_size
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DescribeCustomScenePoliciesResponseBodyDataModule(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        objects: List[str] = None,
        policy_id: int = None,
        start_time: str = None,
        status: str = None,
        template: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.objects = objects
        self.policy_id = policy_id
        self.start_time = start_time
        self.status = status
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.name is not None:
            result['Name'] = self.name
        if self.objects is not None:
            result['Objects'] = self.objects
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class DescribeCustomScenePoliciesResponseBody(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeCustomScenePoliciesResponseBodyDataModule] = None,
        page_number: int = None,
        page_size: int = None,
        quota: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_module = data_module
        self.page_number = page_number
        self.page_size = page_size
        self.quota = quota
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeCustomScenePoliciesResponseBodyDataModule()
                self.data_module.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCustomScenePoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomScenePoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCustomScenePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDoSAllEventListRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event_type: str = None,
        page_number: int = None,
        page_size: int = None,
        site_id: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.event_type = event_type
        # This parameter is required.
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.site_id = site_id
        # A short description of struct
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDoSAllEventListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        bps: int = None,
        cps: int = None,
        end_time: str = None,
        event_id: str = None,
        event_type: str = None,
        pps: int = None,
        qps: int = None,
        start_time: str = None,
        target: str = None,
        target_id: str = None,
    ):
        self.bps = bps
        self.cps = cps
        self.end_time = end_time
        self.event_id = event_id
        self.event_type = event_type
        self.pps = pps
        self.qps = qps
        self.start_time = start_time
        self.target = target
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.target is not None:
            result['Target'] = self.target
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class DescribeDDoSAllEventListResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeDDoSAllEventListResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        site_id: int = None,
        total_count: int = None,
    ):
        self.data_list = data_list
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeDDoSAllEventListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDDoSAllEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDDoSAllEventListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDDoSAllEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHttpDDoSAttackIntelligentProtectionRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
    ):
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class DescribeHttpDDoSAttackIntelligentProtectionResponseBody(TeaModel):
    def __init__(
        self,
        ai_mode: str = None,
        ai_template: str = None,
        request_id: str = None,
        site_id: int = None,
    ):
        self.ai_mode = ai_mode
        self.ai_template = ai_template
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_mode is not None:
            result['AiMode'] = self.ai_mode
        if self.ai_template is not None:
            result['AiTemplate'] = self.ai_template
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiMode') is not None:
            self.ai_mode = m.get('AiMode')
        if m.get('AiTemplate') is not None:
            self.ai_template = m.get('AiTemplate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class DescribeHttpDDoSAttackIntelligentProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHttpDDoSAttackIntelligentProtectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHttpDDoSAttackIntelligentProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHttpDDoSAttackProtectionRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
    ):
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class DescribeHttpDDoSAttackProtectionResponseBody(TeaModel):
    def __init__(
        self,
        global_mode: str = None,
        request_id: str = None,
        site_id: int = None,
    ):
        self.global_mode = global_mode
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_mode is not None:
            result['GlobalMode'] = self.global_mode
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalMode') is not None:
            self.global_mode = m.get('GlobalMode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class DescribeHttpDDoSAttackProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHttpDDoSAttackProtectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHttpDDoSAttackProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIPRangeListResponseBodyContent(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        ip_type: str = None,
    ):
        self.cidr = cidr
        self.ip_type = ip_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        return self


class DescribeIPRangeListResponseBody(TeaModel):
    def __init__(
        self,
        content: List[DescribeIPRangeListResponseBodyContent] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeIPRangeListResponseBodyContent()
                self.content.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIPRangeListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIPRangeListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIPRangeListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKvAccountStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeKvAccountStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeKvAccountStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeKvAccountStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePreloadTasksRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        site_id: int = None,
        start_time: str = None,
        status: str = None,
    ):
        self.content = content
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.site_id = site_id
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePreloadTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        description: str = None,
        process: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.description = description
        self.process = process
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.process is not None:
            result['Process'] = self.process
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribePreloadTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[DescribePreloadTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DescribePreloadTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePreloadTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePreloadTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePreloadTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurgeTasksRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        site_id: int = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        self.content = content
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.site_id = site_id
        self.start_time = start_time
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribePurgeTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        description: str = None,
        process: str = None,
        status: str = None,
        task_id: str = None,
        type: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.description = description
        self.process = process
        self.status = status
        self.task_id = task_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.process is not None:
            result['Process'] = self.process
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribePurgeTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[DescribePurgeTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DescribePurgeTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePurgeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePurgeTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePurgeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableCustomScenePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
    ):
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DisableCustomScenePolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
        request_id: str = None,
    ):
        self.policy_id = policy_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableCustomScenePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableCustomScenePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableCustomScenePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditSiteWafSettingsRequest(TeaModel):
    def __init__(
        self,
        settings: WafSiteSettings = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.settings = settings
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        if self.settings:
            self.settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Settings') is not None:
            temp_model = WafSiteSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class EditSiteWafSettingsShrinkRequest(TeaModel):
    def __init__(
        self,
        settings_shrink: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.settings_shrink = settings_shrink
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.settings_shrink is not None:
            result['Settings'] = self.settings_shrink
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Settings') is not None:
            self.settings_shrink = m.get('Settings')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class EditSiteWafSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditSiteWafSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EditSiteWafSettingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EditSiteWafSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableCustomScenePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
    ):
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class EnableCustomScenePolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
        request_id: str = None,
    ):
        self.policy_id = policy_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableCustomScenePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableCustomScenePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableCustomScenePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportRecordsRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
    ):
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ExportRecordsResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExportRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCacheReserveSpecificationResponseBody(TeaModel):
    def __init__(
        self,
        cache_reserve_capacity: List[str] = None,
        cache_reserve_region: List[str] = None,
        request_id: str = None,
    ):
        self.cache_reserve_capacity = cache_reserve_capacity
        self.cache_reserve_region = cache_reserve_region
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_reserve_capacity is not None:
            result['CacheReserveCapacity'] = self.cache_reserve_capacity
        if self.cache_reserve_region is not None:
            result['CacheReserveRegion'] = self.cache_reserve_region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheReserveCapacity') is not None:
            self.cache_reserve_capacity = m.get('CacheReserveCapacity')
        if m.get('CacheReserveRegion') is not None:
            self.cache_reserve_region = m.get('CacheReserveRegion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCacheReserveSpecificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCacheReserveSpecificationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCacheReserveSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetErServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetErServiceResponseBody(TeaModel):
    def __init__(
        self,
        plan_name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.plan_name = plan_name
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetErServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetErServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetErServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKvRequest(TeaModel):
    def __init__(
        self,
        base_64: bool = None,
        key: str = None,
        namespace: str = None,
    ):
        self.base_64 = base_64
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_64 is not None:
            result['Base64'] = self.base_64
        if self.key is not None:
            result['Key'] = self.key
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base64') is not None:
            self.base_64 = m.get('Base64')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class GetKvResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        value: str = None,
    ):
        self.request_id = request_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetKvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetKvResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetKvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKvAccountResponseBodyNamespaceList(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        capacity_string: str = None,
        capacity_used: int = None,
        capacity_used_string: str = None,
        description: str = None,
        namespace: str = None,
        namespace_id: str = None,
        status: str = None,
    ):
        self.capacity = capacity
        self.capacity_string = capacity_string
        self.capacity_used = capacity_used
        self.capacity_used_string = capacity_used_string
        self.description = description
        self.namespace = namespace
        self.namespace_id = namespace_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.capacity_string is not None:
            result['CapacityString'] = self.capacity_string
        if self.capacity_used is not None:
            result['CapacityUsed'] = self.capacity_used
        if self.capacity_used_string is not None:
            result['CapacityUsedString'] = self.capacity_used_string
        if self.description is not None:
            result['Description'] = self.description
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CapacityString') is not None:
            self.capacity_string = m.get('CapacityString')
        if m.get('CapacityUsed') is not None:
            self.capacity_used = m.get('CapacityUsed')
        if m.get('CapacityUsedString') is not None:
            self.capacity_used_string = m.get('CapacityUsedString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetKvAccountResponseBody(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        capacity_string: str = None,
        capacity_used: int = None,
        capacity_used_string: str = None,
        namespace_list: List[GetKvAccountResponseBodyNamespaceList] = None,
        namespace_quota: int = None,
        namespace_used: int = None,
        request_id: str = None,
        status: str = None,
    ):
        self.capacity = capacity
        self.capacity_string = capacity_string
        self.capacity_used = capacity_used
        self.capacity_used_string = capacity_used_string
        self.namespace_list = namespace_list
        self.namespace_quota = namespace_quota
        self.namespace_used = namespace_used
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.namespace_list:
            for k in self.namespace_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.capacity_string is not None:
            result['CapacityString'] = self.capacity_string
        if self.capacity_used is not None:
            result['CapacityUsed'] = self.capacity_used
        if self.capacity_used_string is not None:
            result['CapacityUsedString'] = self.capacity_used_string
        result['NamespaceList'] = []
        if self.namespace_list is not None:
            for k in self.namespace_list:
                result['NamespaceList'].append(k.to_map() if k else None)
        if self.namespace_quota is not None:
            result['NamespaceQuota'] = self.namespace_quota
        if self.namespace_used is not None:
            result['NamespaceUsed'] = self.namespace_used
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CapacityString') is not None:
            self.capacity_string = m.get('CapacityString')
        if m.get('CapacityUsed') is not None:
            self.capacity_used = m.get('CapacityUsed')
        if m.get('CapacityUsedString') is not None:
            self.capacity_used_string = m.get('CapacityUsedString')
        self.namespace_list = []
        if m.get('NamespaceList') is not None:
            for k in m.get('NamespaceList'):
                temp_model = GetKvAccountResponseBodyNamespaceList()
                self.namespace_list.append(temp_model.from_map(k))
        if m.get('NamespaceQuota') is not None:
            self.namespace_quota = m.get('NamespaceQuota')
        if m.get('NamespaceUsed') is not None:
            self.namespace_used = m.get('NamespaceUsed')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetKvAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetKvAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetKvAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKvNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class GetKvNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        capacity_string: str = None,
        capacity_used: int = None,
        capacity_used_string: str = None,
        description: str = None,
        namespace: str = None,
        namespace_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.capacity = capacity
        self.capacity_string = capacity_string
        self.capacity_used = capacity_used
        self.capacity_used_string = capacity_used_string
        self.description = description
        self.namespace = namespace
        self.namespace_id = namespace_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.capacity_string is not None:
            result['CapacityString'] = self.capacity_string
        if self.capacity_used is not None:
            result['CapacityUsed'] = self.capacity_used
        if self.capacity_used_string is not None:
            result['CapacityUsedString'] = self.capacity_used_string
        if self.description is not None:
            result['Description'] = self.description
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CapacityString') is not None:
            self.capacity_string = m.get('CapacityString')
        if m.get('CapacityUsed') is not None:
            self.capacity_used = m.get('CapacityUsed')
        if m.get('CapacityUsedString') is not None:
            self.capacity_used_string = m.get('CapacityUsedString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetKvNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetKvNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetKvNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetListRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetListResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        items: List[str] = None,
        kind: str = None,
        name: str = None,
        request_id: str = None,
        update_time: str = None,
    ):
        # 自定义响应页面描述
        self.description = description
        # 自定义响应页面ID
        self.id = id
        self.items = items
        self.kind = kind
        # 自定义响应页面名称
        # 
        # This parameter is required.
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.items is not None:
            result['Items'] = self.items
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPageRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetPageResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        id: int = None,
        kind: str = None,
        name: str = None,
        request_id: str = None,
        update_time: str = None,
    ):
        # 自定义响应页面内容BASE64编码
        # 
        # This parameter is required.
        self.content = content
        # 自定义响应页面内容类型
        # 
        # This parameter is required.
        self.content_type = content_type
        # 自定义响应页面描述
        self.description = description
        # 自定义响应页面ID
        self.id = id
        self.kind = kind
        # 自定义响应页面名称
        # 
        # This parameter is required.
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPurgeQuotaRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        type: str = None,
    ):
        self.site_id = site_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetPurgeQuotaResponseBody(TeaModel):
    def __init__(
        self,
        quota: str = None,
        request_id: str = None,
        usage: str = None,
    ):
        self.quota = quota
        # Id of the request
        self.request_id = request_id
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class GetPurgeQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPurgeQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPurgeQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRealtimeDeliveryFieldRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
    ):
        # This parameter is required.
        self.business_type = business_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        return self


class GetRealtimeDeliveryFieldResponseBody(TeaModel):
    def __init__(
        self,
        field_content: Dict[str, FieldContentValue] = None,
        request_id: str = None,
    ):
        self.field_content = field_content
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.field_content:
            for v in self.field_content.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FieldContent'] = {}
        if self.field_content is not None:
            for k, v in self.field_content.items():
                result['FieldContent'][k] = v.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.field_content = {}
        if m.get('FieldContent') is not None:
            for k, v in m.get('FieldContent').items():
                temp_model = FieldContentValue()
                self.field_content[k] = temp_model.from_map(v)
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRealtimeDeliveryFieldResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRealtimeDeliveryFieldResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRealtimeDeliveryFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecordRequest(TeaModel):
    def __init__(
        self,
        record_id: int = None,
    ):
        # This parameter is required.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class GetRecordResponseBodyRecordModelAuthConf(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        self.access_key = access_key
        self.auth_type = auth_type
        self.region = region
        self.secret_key = secret_key
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.region is not None:
            result['Region'] = self.region
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetRecordResponseBodyRecordModelData(TeaModel):
    def __init__(
        self,
        algorithm: int = None,
        certificate: str = None,
        fingerprint: str = None,
        flag: int = None,
        key_tag: int = None,
        matching_type: int = None,
        port: int = None,
        priority: int = None,
        selector: int = None,
        tag: str = None,
        type: int = None,
        usage: int = None,
        value: str = None,
        weight: int = None,
    ):
        self.algorithm = algorithm
        self.certificate = certificate
        self.fingerprint = fingerprint
        self.flag = flag
        self.key_tag = key_tag
        self.matching_type = matching_type
        self.port = port
        self.priority = priority
        self.selector = selector
        self.tag = tag
        self.type = type
        self.usage = usage
        self.value = value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.matching_type is not None:
            result['MatchingType'] = self.matching_type
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.selector is not None:
            result['Selector'] = self.selector
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.value is not None:
            result['Value'] = self.value
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('MatchingType') is not None:
            self.matching_type = m.get('MatchingType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Selector') is not None:
            self.selector = m.get('Selector')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class GetRecordResponseBodyRecordModel(TeaModel):
    def __init__(
        self,
        auth_conf: GetRecordResponseBodyRecordModelAuthConf = None,
        biz_name: str = None,
        comment: str = None,
        create_time: str = None,
        data: GetRecordResponseBodyRecordModelData = None,
        host_policy: str = None,
        proxied: bool = None,
        record_cname: str = None,
        record_id: int = None,
        record_name: str = None,
        record_source_type: str = None,
        record_type: str = None,
        site_id: int = None,
        site_name: str = None,
        ttl: int = None,
        update_time: str = None,
    ):
        self.auth_conf = auth_conf
        self.biz_name = biz_name
        self.comment = comment
        self.create_time = create_time
        self.data = data
        self.host_policy = host_policy
        self.proxied = proxied
        self.record_cname = record_cname
        self.record_id = record_id
        self.record_name = record_name
        self.record_source_type = record_source_type
        self.record_type = record_type
        self.site_id = site_id
        self.site_name = site_name
        self.ttl = ttl
        self.update_time = update_time

    def validate(self):
        if self.auth_conf:
            self.auth_conf.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_conf is not None:
            result['AuthConf'] = self.auth_conf.to_map()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.host_policy is not None:
            result['HostPolicy'] = self.host_policy
        if self.proxied is not None:
            result['Proxied'] = self.proxied
        if self.record_cname is not None:
            result['RecordCname'] = self.record_cname
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.record_source_type is not None:
            result['RecordSourceType'] = self.record_source_type
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConf') is not None:
            temp_model = GetRecordResponseBodyRecordModelAuthConf()
            self.auth_conf = temp_model.from_map(m['AuthConf'])
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            temp_model = GetRecordResponseBodyRecordModelData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')
        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')
        if m.get('RecordCname') is not None:
            self.record_cname = m.get('RecordCname')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('RecordSourceType') is not None:
            self.record_source_type = m.get('RecordSourceType')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetRecordResponseBody(TeaModel):
    def __init__(
        self,
        record_model: GetRecordResponseBodyRecordModel = None,
        request_id: str = None,
    ):
        self.record_model = record_model
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.record_model:
            self.record_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_model is not None:
            result['RecordModel'] = self.record_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordModel') is not None:
            temp_model = GetRecordResponseBodyRecordModel()
            self.record_model = temp_model.from_map(m['RecordModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoutineRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetRoutineResponseBodyCodeVersions(TeaModel):
    def __init__(
        self,
        code_description: str = None,
        code_version: str = None,
        create_time: str = None,
    ):
        self.code_description = code_description
        self.code_version = code_version
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class GetRoutineResponseBodyEnvs(TeaModel):
    def __init__(
        self,
        canary_area_list: List[str] = None,
        canary_code_version: str = None,
        code_version: str = None,
        env: str = None,
        spec_name: str = None,
    ):
        self.canary_area_list = canary_area_list
        self.canary_code_version = canary_code_version
        self.code_version = code_version
        self.env = env
        self.spec_name = spec_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.canary_area_list is not None:
            result['CanaryAreaList'] = self.canary_area_list
        if self.canary_code_version is not None:
            result['CanaryCodeVersion'] = self.canary_code_version
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version
        if self.env is not None:
            result['Env'] = self.env
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanaryAreaList') is not None:
            self.canary_area_list = m.get('CanaryAreaList')
        if m.get('CanaryCodeVersion') is not None:
            self.canary_code_version = m.get('CanaryCodeVersion')
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        return self


class GetRoutineResponseBodyRelatedRecords(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        record_name: str = None,
        site_id: int = None,
        site_name: str = None,
    ):
        self.record_id = record_id
        self.record_name = record_name
        self.site_id = site_id
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        return self


class GetRoutineResponseBodyRelatedRoutes(TeaModel):
    def __init__(
        self,
        route: str = None,
        route_id: str = None,
        site_id: int = None,
        site_name: str = None,
    ):
        self.route = route
        self.route_id = route_id
        self.site_id = site_id
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route is not None:
            result['Route'] = self.route
        if self.route_id is not None:
            result['RouteId'] = self.route_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        return self


class GetRoutineResponseBody(TeaModel):
    def __init__(
        self,
        code_versions: List[GetRoutineResponseBodyCodeVersions] = None,
        create_time: str = None,
        default_related_record: str = None,
        description: str = None,
        envs: List[GetRoutineResponseBodyEnvs] = None,
        related_records: List[GetRoutineResponseBodyRelatedRecords] = None,
        related_routes: List[GetRoutineResponseBodyRelatedRoutes] = None,
        request_id: str = None,
    ):
        self.code_versions = code_versions
        self.create_time = create_time
        self.default_related_record = default_related_record
        self.description = description
        self.envs = envs
        self.related_records = related_records
        self.related_routes = related_routes
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.code_versions:
            for k in self.code_versions:
                if k:
                    k.validate()
        if self.envs:
            for k in self.envs:
                if k:
                    k.validate()
        if self.related_records:
            for k in self.related_records:
                if k:
                    k.validate()
        if self.related_routes:
            for k in self.related_routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CodeVersions'] = []
        if self.code_versions is not None:
            for k in self.code_versions:
                result['CodeVersions'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_related_record is not None:
            result['DefaultRelatedRecord'] = self.default_related_record
        if self.description is not None:
            result['Description'] = self.description
        result['Envs'] = []
        if self.envs is not None:
            for k in self.envs:
                result['Envs'].append(k.to_map() if k else None)
        result['RelatedRecords'] = []
        if self.related_records is not None:
            for k in self.related_records:
                result['RelatedRecords'].append(k.to_map() if k else None)
        result['RelatedRoutes'] = []
        if self.related_routes is not None:
            for k in self.related_routes:
                result['RelatedRoutes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_versions = []
        if m.get('CodeVersions') is not None:
            for k in m.get('CodeVersions'):
                temp_model = GetRoutineResponseBodyCodeVersions()
                self.code_versions.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultRelatedRecord') is not None:
            self.default_related_record = m.get('DefaultRelatedRecord')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.envs = []
        if m.get('Envs') is not None:
            for k in m.get('Envs'):
                temp_model = GetRoutineResponseBodyEnvs()
                self.envs.append(temp_model.from_map(k))
        self.related_records = []
        if m.get('RelatedRecords') is not None:
            for k in m.get('RelatedRecords'):
                temp_model = GetRoutineResponseBodyRelatedRecords()
                self.related_records.append(temp_model.from_map(k))
        self.related_routes = []
        if m.get('RelatedRoutes') is not None:
            for k in m.get('RelatedRoutes'):
                temp_model = GetRoutineResponseBodyRelatedRoutes()
                self.related_routes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRoutineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoutineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRoutineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoutineStagingCodeUploadInfoRequest(TeaModel):
    def __init__(
        self,
        code_description: str = None,
        name: str = None,
    ):
        self.code_description = code_description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetRoutineStagingCodeUploadInfoResponseBody(TeaModel):
    def __init__(
        self,
        code_version: str = None,
        oss_post_config: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.code_version = code_version
        self.oss_post_config = oss_post_config
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version
        if self.oss_post_config is not None:
            result['OssPostConfig'] = self.oss_post_config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')
        if m.get('OssPostConfig') is not None:
            self.oss_post_config = m.get('OssPostConfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRoutineStagingCodeUploadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoutineStagingCodeUploadInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRoutineStagingCodeUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoutineStagingEnvIpResponseBody(TeaModel):
    def __init__(
        self,
        ipv4: List[str] = None,
        request_id: str = None,
    ):
        self.ipv4 = ipv4
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv4 is not None:
            result['IPV4'] = self.ipv4
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPV4') is not None:
            self.ipv4 = m.get('IPV4')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRoutineStagingEnvIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoutineStagingEnvIpResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRoutineStagingEnvIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoutineUserInfoResponseBodyRoutines(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        routine_name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.routine_name = routine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')
        return self


class GetRoutineUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        routines: List[GetRoutineUserInfoResponseBodyRoutines] = None,
        subdomains: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.routines = routines
        self.subdomains = subdomains

    def validate(self):
        if self.routines:
            for k in self.routines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Routines'] = []
        if self.routines is not None:
            for k in self.routines:
                result['Routines'].append(k.to_map() if k else None)
        if self.subdomains is not None:
            result['Subdomains'] = self.subdomains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.routines = []
        if m.get('Routines') is not None:
            for k in m.get('Routines'):
                temp_model = GetRoutineUserInfoResponseBodyRoutines()
                self.routines.append(temp_model.from_map(k))
        if m.get('Subdomains') is not None:
            self.subdomains = m.get('Subdomains')
        return self


class GetRoutineUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoutineUserInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRoutineUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScheduledPreloadJobRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetScheduledPreloadJobResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        created_at: str = None,
        domains: str = None,
        error_info: str = None,
        failed_file_oss: str = None,
        file_id: str = None,
        id: str = None,
        insert_way: str = None,
        name: str = None,
        request_id: str = None,
        site_id: int = None,
        task_submitted: int = None,
        task_type: str = None,
        url_count: int = None,
        url_submitted: int = None,
    ):
        self.ali_uid = ali_uid
        self.created_at = created_at
        self.domains = domains
        self.error_info = error_info
        self.failed_file_oss = failed_file_oss
        self.file_id = file_id
        self.id = id
        self.insert_way = insert_way
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id
        self.task_submitted = task_submitted
        self.task_type = task_type
        self.url_count = url_count
        self.url_submitted = url_submitted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.failed_file_oss is not None:
            result['FailedFileOss'] = self.failed_file_oss
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id is not None:
            result['Id'] = self.id
        if self.insert_way is not None:
            result['InsertWay'] = self.insert_way
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.task_submitted is not None:
            result['TaskSubmitted'] = self.task_submitted
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.url_count is not None:
            result['UrlCount'] = self.url_count
        if self.url_submitted is not None:
            result['UrlSubmitted'] = self.url_submitted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('FailedFileOss') is not None:
            self.failed_file_oss = m.get('FailedFileOss')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsertWay') is not None:
            self.insert_way = m.get('InsertWay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaskSubmitted') is not None:
            self.task_submitted = m.get('TaskSubmitted')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UrlCount') is not None:
            self.url_count = m.get('UrlCount')
        if m.get('UrlSubmitted') is not None:
            self.url_submitted = m.get('UrlSubmitted')
        return self


class GetScheduledPreloadJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetScheduledPreloadJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetScheduledPreloadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSiteRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
    ):
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class GetSiteResponseBodySiteModel(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        cname_zone: str = None,
        coverage: str = None,
        create_time: str = None,
        instance_id: str = None,
        name_server_list: str = None,
        plan_name: str = None,
        plan_spec_name: str = None,
        resource_group_id: str = None,
        site_id: int = None,
        site_name: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        update_time: str = None,
        vanity_nslist: Dict[str, str] = None,
        verify_code: str = None,
        version_management: bool = None,
    ):
        self.access_type = access_type
        self.cname_zone = cname_zone
        self.coverage = coverage
        self.create_time = create_time
        self.instance_id = instance_id
        self.name_server_list = name_server_list
        self.plan_name = plan_name
        self.plan_spec_name = plan_spec_name
        self.resource_group_id = resource_group_id
        self.site_id = site_id
        self.site_name = site_name
        self.status = status
        self.tags = tags
        self.update_time = update_time
        self.vanity_nslist = vanity_nslist
        self.verify_code = verify_code
        self.version_management = version_management

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.cname_zone is not None:
            result['CnameZone'] = self.cname_zone
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name_server_list is not None:
            result['NameServerList'] = self.name_server_list
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_spec_name is not None:
            result['PlanSpecName'] = self.plan_spec_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vanity_nslist is not None:
            result['VanityNSList'] = self.vanity_nslist
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        if self.version_management is not None:
            result['VersionManagement'] = self.version_management
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('CnameZone') is not None:
            self.cname_zone = m.get('CnameZone')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NameServerList') is not None:
            self.name_server_list = m.get('NameServerList')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanSpecName') is not None:
            self.plan_spec_name = m.get('PlanSpecName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VanityNSList') is not None:
            self.vanity_nslist = m.get('VanityNSList')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        if m.get('VersionManagement') is not None:
            self.version_management = m.get('VersionManagement')
        return self


class GetSiteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        site_model: GetSiteResponseBodySiteModel = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.site_model = site_model

    def validate(self):
        if self.site_model:
            self.site_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_model is not None:
            result['SiteModel'] = self.site_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteModel') is not None:
            temp_model = GetSiteResponseBodySiteModel()
            self.site_model = temp_model.from_map(m['SiteModel'])
        return self


class GetSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSiteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSiteCurrentNSRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
    ):
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class GetSiteCurrentNSResponseBody(TeaModel):
    def __init__(
        self,
        nslist: List[str] = None,
        request_id: str = None,
    ):
        self.nslist = nslist
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nslist is not None:
            result['NSList'] = self.nslist
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NSList') is not None:
            self.nslist = m.get('NSList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSiteCurrentNSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSiteCurrentNSResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSiteCurrentNSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSiteCustomLogRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
    ):
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class GetSiteCustomLogResponseBodyLogCustomField(TeaModel):
    def __init__(
        self,
        cookies: List[str] = None,
        request_headers: List[str] = None,
        response_headers: List[str] = None,
    ):
        self.cookies = cookies
        self.request_headers = request_headers
        self.response_headers = response_headers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers
        if self.response_headers is not None:
            result['ResponseHeaders'] = self.response_headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')
        if m.get('ResponseHeaders') is not None:
            self.response_headers = m.get('ResponseHeaders')
        return self


class GetSiteCustomLogResponseBody(TeaModel):
    def __init__(
        self,
        config_id: int = None,
        is_exist: bool = None,
        log_custom_field: GetSiteCustomLogResponseBodyLogCustomField = None,
        request_id: str = None,
        site_id: int = None,
    ):
        self.config_id = config_id
        self.is_exist = is_exist
        self.log_custom_field = log_custom_field
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id

    def validate(self):
        if self.log_custom_field:
            self.log_custom_field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.is_exist is not None:
            result['IsExist'] = self.is_exist
        if self.log_custom_field is not None:
            result['LogCustomField'] = self.log_custom_field.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('IsExist') is not None:
            self.is_exist = m.get('IsExist')
        if m.get('LogCustomField') is not None:
            temp_model = GetSiteCustomLogResponseBodyLogCustomField()
            self.log_custom_field = temp_model.from_map(m['LogCustomField'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class GetSiteCustomLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSiteCustomLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSiteCustomLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSiteDeliveryTaskRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        task_name: str = None,
    ):
        self.site_id = site_id
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class GetSiteDeliveryTaskResponseBody(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        discard_rate: float = None,
        field_list: str = None,
        filter_rules: str = None,
        request_id: str = None,
        sink_config: Any = None,
        site_id: int = None,
        site_name: str = None,
        status: str = None,
        task_name: str = None,
    ):
        self.business_type = business_type
        self.data_center = data_center
        self.delivery_type = delivery_type
        self.discard_rate = discard_rate
        self.field_list = field_list
        self.filter_rules = filter_rules
        # Id of the request
        self.request_id = request_id
        self.sink_config = sink_config
        self.site_id = site_id
        self.site_name = site_name
        self.status = status
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate
        if self.field_list is not None:
            result['FieldList'] = self.field_list
        if self.filter_rules is not None:
            result['FilterRules'] = self.filter_rules
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sink_config is not None:
            result['SinkConfig'] = self.sink_config
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')
        if m.get('FieldList') is not None:
            self.field_list = m.get('FieldList')
        if m.get('FilterRules') is not None:
            self.filter_rules = m.get('FilterRules')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SinkConfig') is not None:
            self.sink_config = m.get('SinkConfig')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class GetSiteDeliveryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSiteDeliveryTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSiteDeliveryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSiteLogDeliveryQuotaRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.business_type = business_type
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class GetSiteLogDeliveryQuotaResponseBody(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        free_quota: int = None,
        request_id: str = None,
        site_id: int = None,
    ):
        self.business_type = business_type
        self.free_quota = free_quota
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.free_quota is not None:
            result['FreeQuota'] = self.free_quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('FreeQuota') is not None:
            self.free_quota = m.get('FreeQuota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class GetSiteLogDeliveryQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSiteLogDeliveryQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSiteLogDeliveryQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSiteWafSettingsRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        site_version: int = None,
    ):
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class GetSiteWafSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        settings: WafSiteSettings = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.settings = settings

    def validate(self):
        if self.settings:
            self.settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Settings') is not None:
            temp_model = WafSiteSettings()
            self.settings = temp_model.from_map(m['Settings'])
        return self


class GetSiteWafSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSiteWafSettingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSiteWafSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadTaskRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        upload_id: int = None,
    ):
        self.site_id = site_id
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.upload_id is not None:
            result['UploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')
        return self


class GetUploadTaskResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.description = description
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetUploadTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUploadTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUploadTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserDeliveryTaskRequest(TeaModel):
    def __init__(
        self,
        task_name: str = None,
    ):
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class GetUserDeliveryTaskResponseBody(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        discard_rate: float = None,
        field_list: str = None,
        filter_rules: str = None,
        request_id: str = None,
        sink_config: Any = None,
        status: str = None,
        task_name: str = None,
    ):
        self.business_type = business_type
        self.data_center = data_center
        self.delivery_type = delivery_type
        self.discard_rate = discard_rate
        self.field_list = field_list
        self.filter_rules = filter_rules
        # Id of the request
        self.request_id = request_id
        self.sink_config = sink_config
        self.status = status
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate
        if self.field_list is not None:
            result['FieldList'] = self.field_list
        if self.filter_rules is not None:
            result['FilterRules'] = self.filter_rules
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sink_config is not None:
            result['SinkConfig'] = self.sink_config
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')
        if m.get('FieldList') is not None:
            self.field_list = m.get('FieldList')
        if m.get('FilterRules') is not None:
            self.filter_rules = m.get('FilterRules')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SinkConfig') is not None:
            self.sink_config = m.get('SinkConfig')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class GetUserDeliveryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserDeliveryTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserDeliveryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserLogDeliveryQuotaRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
    ):
        # This parameter is required.
        self.business_type = business_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        return self


class GetUserLogDeliveryQuotaResponseBody(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        free_quota: int = None,
        request_id: str = None,
    ):
        self.business_type = business_type
        self.free_quota = free_quota
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.free_quota is not None:
            result['FreeQuota'] = self.free_quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('FreeQuota') is not None:
            self.free_quota = m.get('FreeQuota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserLogDeliveryQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserLogDeliveryQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserLogDeliveryQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWafBotAppKeyResponseBody(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        request_id: str = None,
    ):
        # APP key
        self.app_key = app_key
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWafBotAppKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWafBotAppKeyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWafBotAppKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWafFilterRequest(TeaModel):
    def __init__(
        self,
        phase: str = None,
        site_id: int = None,
        target: str = None,
        type: str = None,
    ):
        self.phase = phase
        self.site_id = site_id
        self.target = target
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.target is not None:
            result['Target'] = self.target
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWafFilterResponseBodyFilterFieldsLogicsValidator(TeaModel):
    def __init__(
        self,
        err_msg: str = None,
        length: WafQuotaInteger = None,
        pattern: str = None,
        range: WafQuotaInteger = None,
    ):
        self.err_msg = err_msg
        self.length = length
        self.pattern = pattern
        self.range = range

    def validate(self):
        if self.length:
            self.length.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.length is not None:
            result['Length'] = self.length.to_map()
        if self.pattern is not None:
            result['Pattern'] = self.pattern
        if self.range is not None:
            result['Range'] = self.range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('Length') is not None:
            temp_model = WafQuotaInteger()
            self.length = temp_model.from_map(m['Length'])
        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')
        if m.get('Range') is not None:
            temp_model = WafQuotaInteger()
            self.range = temp_model.from_map(m['Range'])
        return self


class GetWafFilterResponseBodyFilterFieldsLogics(TeaModel):
    def __init__(
        self,
        attributes: int = None,
        kind: str = None,
        negative: bool = None,
        operator: str = None,
        symbol: str = None,
        tip: str = None,
        type: str = None,
        validator: GetWafFilterResponseBodyFilterFieldsLogicsValidator = None,
    ):
        self.attributes = attributes
        self.kind = kind
        self.negative = negative
        self.operator = operator
        self.symbol = symbol
        self.tip = tip
        self.type = type
        self.validator = validator

    def validate(self):
        if self.validator:
            self.validator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.negative is not None:
            result['Negative'] = self.negative
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.symbol is not None:
            result['Symbol'] = self.symbol
        if self.tip is not None:
            result['Tip'] = self.tip
        if self.type is not None:
            result['Type'] = self.type
        if self.validator is not None:
            result['Validator'] = self.validator.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Negative') is not None:
            self.negative = m.get('Negative')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')
        if m.get('Tip') is not None:
            self.tip = m.get('Tip')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Validator') is not None:
            temp_model = GetWafFilterResponseBodyFilterFieldsLogicsValidator()
            self.validator = temp_model.from_map(m['Validator'])
        return self


class GetWafFilterResponseBodyFilterFieldsSelectorData(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetWafFilterResponseBodyFilterFieldsSelector(TeaModel):
    def __init__(
        self,
        data: List[GetWafFilterResponseBodyFilterFieldsSelectorData] = None,
        kind: str = None,
    ):
        self.data = data
        self.kind = kind

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.kind is not None:
            result['Kind'] = self.kind
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetWafFilterResponseBodyFilterFieldsSelectorData()
                self.data.append(temp_model.from_map(k))
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        return self


class GetWafFilterResponseBodyFilterFields(TeaModel):
    def __init__(
        self,
        key: str = None,
        label: str = None,
        logics: List[GetWafFilterResponseBodyFilterFieldsLogics] = None,
        selector: GetWafFilterResponseBodyFilterFieldsSelector = None,
        sub: bool = None,
        sub_tip: str = None,
    ):
        self.key = key
        self.label = label
        self.logics = logics
        self.selector = selector
        self.sub = sub
        self.sub_tip = sub_tip

    def validate(self):
        if self.logics:
            for k in self.logics:
                if k:
                    k.validate()
        if self.selector:
            self.selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.label is not None:
            result['Label'] = self.label
        result['Logics'] = []
        if self.logics is not None:
            for k in self.logics:
                result['Logics'].append(k.to_map() if k else None)
        if self.selector is not None:
            result['Selector'] = self.selector.to_map()
        if self.sub is not None:
            result['Sub'] = self.sub
        if self.sub_tip is not None:
            result['SubTip'] = self.sub_tip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        self.logics = []
        if m.get('Logics') is not None:
            for k in m.get('Logics'):
                temp_model = GetWafFilterResponseBodyFilterFieldsLogics()
                self.logics.append(temp_model.from_map(k))
        if m.get('Selector') is not None:
            temp_model = GetWafFilterResponseBodyFilterFieldsSelector()
            self.selector = temp_model.from_map(m['Selector'])
        if m.get('Sub') is not None:
            self.sub = m.get('Sub')
        if m.get('SubTip') is not None:
            self.sub_tip = m.get('SubTip')
        return self


class GetWafFilterResponseBodyFilter(TeaModel):
    def __init__(
        self,
        fields: List[GetWafFilterResponseBodyFilterFields] = None,
        phase: str = None,
        target: str = None,
        type: str = None,
    ):
        self.fields = fields
        self.phase = phase
        self.target = target
        self.type = type

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.target is not None:
            result['Target'] = self.target
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = GetWafFilterResponseBodyFilterFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWafFilterResponseBody(TeaModel):
    def __init__(
        self,
        filter: GetWafFilterResponseBodyFilter = None,
        request_id: str = None,
    ):
        self.filter = filter
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = GetWafFilterResponseBodyFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWafFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWafFilterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWafFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWafQuotaRequest(TeaModel):
    def __init__(
        self,
        paths: str = None,
    ):
        self.paths = paths

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paths is not None:
            result['Paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        return self


class GetWafQuotaResponseBodyQuotaList(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        items: Dict[str, QuotaListItemsValue] = None,
        number_items_per_list: WafQuotaInteger = None,
        number_items_total: WafQuotaInteger = None,
        number_total: WafQuotaInteger = None,
    ):
        self.enable = enable
        self.items = items
        self.number_items_per_list = number_items_per_list
        self.number_items_total = number_items_total
        self.number_total = number_total

    def validate(self):
        if self.items:
            for v in self.items.values():
                if v:
                    v.validate()
        if self.number_items_per_list:
            self.number_items_per_list.validate()
        if self.number_items_total:
            self.number_items_total.validate()
        if self.number_total:
            self.number_total.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        result['Items'] = {}
        if self.items is not None:
            for k, v in self.items.items():
                result['Items'][k] = v.to_map()
        if self.number_items_per_list is not None:
            result['NumberItemsPerList'] = self.number_items_per_list.to_map()
        if self.number_items_total is not None:
            result['NumberItemsTotal'] = self.number_items_total.to_map()
        if self.number_total is not None:
            result['NumberTotal'] = self.number_total.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        self.items = {}
        if m.get('Items') is not None:
            for k, v in m.get('Items').items():
                temp_model = QuotaListItemsValue()
                self.items[k] = temp_model.from_map(v)
        if m.get('NumberItemsPerList') is not None:
            temp_model = WafQuotaInteger()
            self.number_items_per_list = temp_model.from_map(m['NumberItemsPerList'])
        if m.get('NumberItemsTotal') is not None:
            temp_model = WafQuotaInteger()
            self.number_items_total = temp_model.from_map(m['NumberItemsTotal'])
        if m.get('NumberTotal') is not None:
            temp_model = WafQuotaInteger()
            self.number_total = temp_model.from_map(m['NumberTotal'])
        return self


class GetWafQuotaResponseBodyQuotaManagedRulesGroup(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        number_total: WafQuotaInteger = None,
    ):
        self.enable = enable
        self.number_total = number_total

    def validate(self):
        if self.number_total:
            self.number_total.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.number_total is not None:
            result['NumberTotal'] = self.number_total.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('NumberTotal') is not None:
            temp_model = WafQuotaInteger()
            self.number_total = temp_model.from_map(m['NumberTotal'])
        return self


class GetWafQuotaResponseBodyQuotaPage(TeaModel):
    def __init__(
        self,
        content_types: Dict[str, QuotaPageContentTypesValue] = None,
        enable: bool = None,
        number_total: WafQuotaInteger = None,
    ):
        self.content_types = content_types
        self.enable = enable
        self.number_total = number_total

    def validate(self):
        if self.content_types:
            for v in self.content_types.values():
                if v:
                    v.validate()
        if self.number_total:
            self.number_total.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContentTypes'] = {}
        if self.content_types is not None:
            for k, v in self.content_types.items():
                result['ContentTypes'][k] = v.to_map()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.number_total is not None:
            result['NumberTotal'] = self.number_total.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content_types = {}
        if m.get('ContentTypes') is not None:
            for k, v in m.get('ContentTypes').items():
                temp_model = QuotaPageContentTypesValue()
                self.content_types[k] = temp_model.from_map(v)
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('NumberTotal') is not None:
            temp_model = WafQuotaInteger()
            self.number_total = temp_model.from_map(m['NumberTotal'])
        return self


class GetWafQuotaResponseBodyQuotaScenePolicy(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        number_total: WafQuotaInteger = None,
    ):
        self.enable = enable
        self.number_total = number_total

    def validate(self):
        if self.number_total:
            self.number_total.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.number_total is not None:
            result['NumberTotal'] = self.number_total.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('NumberTotal') is not None:
            temp_model = WafQuotaInteger()
            self.number_total = temp_model.from_map(m['NumberTotal'])
        return self


class GetWafQuotaResponseBodyQuota(TeaModel):
    def __init__(
        self,
        list: GetWafQuotaResponseBodyQuotaList = None,
        managed_rules_group: GetWafQuotaResponseBodyQuotaManagedRulesGroup = None,
        page: GetWafQuotaResponseBodyQuotaPage = None,
        scene_policy: GetWafQuotaResponseBodyQuotaScenePolicy = None,
    ):
        self.list = list
        self.managed_rules_group = managed_rules_group
        self.page = page
        self.scene_policy = scene_policy

    def validate(self):
        if self.list:
            self.list.validate()
        if self.managed_rules_group:
            self.managed_rules_group.validate()
        if self.page:
            self.page.validate()
        if self.scene_policy:
            self.scene_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.managed_rules_group is not None:
            result['ManagedRulesGroup'] = self.managed_rules_group.to_map()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.scene_policy is not None:
            result['ScenePolicy'] = self.scene_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = GetWafQuotaResponseBodyQuotaList()
            self.list = temp_model.from_map(m['List'])
        if m.get('ManagedRulesGroup') is not None:
            temp_model = GetWafQuotaResponseBodyQuotaManagedRulesGroup()
            self.managed_rules_group = temp_model.from_map(m['ManagedRulesGroup'])
        if m.get('Page') is not None:
            temp_model = GetWafQuotaResponseBodyQuotaPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('ScenePolicy') is not None:
            temp_model = GetWafQuotaResponseBodyQuotaScenePolicy()
            self.scene_policy = temp_model.from_map(m['ScenePolicy'])
        return self


class GetWafQuotaResponseBody(TeaModel):
    def __init__(
        self,
        quota: GetWafQuotaResponseBodyQuota = None,
        request_id: str = None,
    ):
        self.quota = quota
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            temp_model = GetWafQuotaResponseBodyQuota()
            self.quota = temp_model.from_map(m['Quota'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWafQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWafQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWafQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWafRuleRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class GetWafRuleResponseBody(TeaModel):
    def __init__(
        self,
        config: WafRuleConfig = None,
        id: int = None,
        name: str = None,
        phase: str = None,
        position: int = None,
        request_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.config = config
        # 自定义响应页面ID
        self.id = id
        # 自定义响应页面名称
        # 
        # This parameter is required.
        self.name = name
        # 自定义响应页面内容类型
        # 
        # This parameter is required.
        self.phase = phase
        self.position = position
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.update_time = update_time

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.position is not None:
            result['Position'] = self.position
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = WafRuleConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetWafRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWafRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWafRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWafRulesetRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        phase: str = None,
        site_id: int = None,
    ):
        self.id = id
        self.phase = phase
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class GetWafRulesetResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        phase: str = None,
        request_id: str = None,
        rules: List[WafRuleConfig] = None,
        shared: WafBatchRuleShared = None,
        status: str = None,
        update_time: str = None,
    ):
        # 自定义响应页面ID
        self.id = id
        # 自定义响应页面名称
        # 
        # This parameter is required.
        self.name = name
        # 自定义响应页面内容类型
        # 
        # This parameter is required.
        self.phase = phase
        # Id of the request
        self.request_id = request_id
        self.rules = rules
        self.shared = shared
        self.status = status
        self.update_time = update_time

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()
        if self.shared:
            self.shared.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.shared is not None:
            result['Shared'] = self.shared.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = WafRuleConfig()
                self.rules.append(temp_model.from_map(k))
        if m.get('Shared') is not None:
            temp_model = WafBatchRuleShared()
            self.shared = temp_model.from_map(m['Shared'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetWafRulesetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWafRulesetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWafRulesetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCacheReserveInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCacheReserveInstancesResponseBodyInstanceInfo(TeaModel):
    def __init__(
        self,
        cache_reserve_capacity: str = None,
        cache_reserve_region: str = None,
        create_time: str = None,
        duration: int = None,
        expire_time: str = None,
        instance_id: str = None,
        status: str = None,
    ):
        self.cache_reserve_capacity = cache_reserve_capacity
        self.cache_reserve_region = cache_reserve_region
        self.create_time = create_time
        self.duration = duration
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_reserve_capacity is not None:
            result['CacheReserveCapacity'] = self.cache_reserve_capacity
        if self.cache_reserve_region is not None:
            result['CacheReserveRegion'] = self.cache_reserve_region
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheReserveCapacity') is not None:
            self.cache_reserve_capacity = m.get('CacheReserveCapacity')
        if m.get('CacheReserveRegion') is not None:
            self.cache_reserve_region = m.get('CacheReserveRegion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCacheReserveInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_info: List[ListCacheReserveInstancesResponseBodyInstanceInfo] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.instance_info = instance_info
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.instance_info:
            for k in self.instance_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k in self.instance_info:
                result['InstanceInfo'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k in m.get('InstanceInfo'):
                temp_model = ListCacheReserveInstancesResponseBodyInstanceInfo()
                self.instance_info.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListCacheReserveInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCacheReserveInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCacheReserveInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClientCertificatesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        site_id: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ListClientCertificatesResponseBodyResult(TeaModel):
    def __init__(
        self,
        cacertificate_id: str = None,
        common_name: str = None,
        create_time: str = None,
        id: str = None,
        issuer: str = None,
        name: str = None,
        not_after: str = None,
        not_before: str = None,
        pubkey_algorithm: str = None,
        san: str = None,
        signature_algorithm: str = None,
        status: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.cacertificate_id = cacertificate_id
        self.common_name = common_name
        self.create_time = create_time
        self.id = id
        self.issuer = issuer
        self.name = name
        self.not_after = not_after
        self.not_before = not_before
        self.pubkey_algorithm = pubkey_algorithm
        self.san = san
        self.signature_algorithm = signature_algorithm
        self.status = status
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.name is not None:
            result['Name'] = self.name
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.pubkey_algorithm is not None:
            result['PubkeyAlgorithm'] = self.pubkey_algorithm
        if self.san is not None:
            result['SAN'] = self.san
        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('PubkeyAlgorithm') is not None:
            self.pubkey_algorithm = m.get('PubkeyAlgorithm')
        if m.get('SAN') is not None:
            self.san = m.get('SAN')
        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListClientCertificatesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result: List[ListClientCertificatesResponseBodyResult] = None,
        site_id: int = None,
        site_name: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result = result
        self.site_id = site_id
        self.site_name = site_name
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListClientCertificatesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClientCertificatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClientCertificatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClientCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEdgeContainerAppRecordsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        order_key: str = None,
        order_type: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.order_key = order_key
        self.order_type = order_type
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.order_key is not None:
            result['OrderKey'] = self.order_key
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OrderKey') is not None:
            self.order_key = m.get('OrderKey')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class ListEdgeContainerAppRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        cname: str = None,
        config_id: int = None,
        create_time: str = None,
        record_id: int = None,
        record_name: str = None,
        schemd_id: int = None,
        site_id: int = None,
        update_time: str = None,
    ):
        self.app_id = app_id
        self.cname = cname
        self.config_id = config_id
        self.create_time = create_time
        self.record_id = record_id
        self.record_name = record_name
        self.schemd_id = schemd_id
        self.site_id = site_id
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.schemd_id is not None:
            result['SchemdId'] = self.schemd_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SchemdId') is not None:
            self.schemd_id = m.get('SchemdId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListEdgeContainerAppRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[ListEdgeContainerAppRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListEdgeContainerAppRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEdgeContainerAppRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEdgeContainerAppRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEdgeContainerAppRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEdgeContainerAppsRequest(TeaModel):
    def __init__(
        self,
        order_key: str = None,
        order_type: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        search_type: str = None,
    ):
        self.order_key = order_key
        self.order_type = order_type
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.search_type = search_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_key is not None:
            result['OrderKey'] = self.order_key
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderKey') is not None:
            self.order_key = m.get('OrderKey')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        return self


class ListEdgeContainerAppsResponseBodyAppsHealthCheck(TeaModel):
    def __init__(
        self,
        fail_times: int = None,
        host: str = None,
        http_code: str = None,
        interval: int = None,
        method: str = None,
        port: int = None,
        succ_times: int = None,
        timeout: int = None,
        type: str = None,
        uri: str = None,
    ):
        self.fail_times = fail_times
        self.host = host
        self.http_code = http_code
        self.interval = interval
        self.method = method
        self.port = port
        self.succ_times = succ_times
        self.timeout = timeout
        self.type = type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.host is not None:
            result['Host'] = self.host
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.method is not None:
            result['Method'] = self.method
        if self.port is not None:
            result['Port'] = self.port
        if self.succ_times is not None:
            result['SuccTimes'] = self.succ_times
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SuccTimes') is not None:
            self.succ_times = m.get('SuccTimes')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ListEdgeContainerAppsResponseBodyApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: str = None,
        domain_name: str = None,
        gateway_type: str = None,
        health_check: ListEdgeContainerAppsResponseBodyAppsHealthCheck = None,
        name: str = None,
        percentage: int = None,
        quic_cid: str = None,
        remarks: str = None,
        service_port: int = None,
        status: str = None,
        target_port: int = None,
        update_time: str = None,
        version_count: int = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.domain_name = domain_name
        self.gateway_type = gateway_type
        self.health_check = health_check
        self.name = name
        self.percentage = percentage
        self.quic_cid = quic_cid
        self.remarks = remarks
        self.service_port = service_port
        self.status = status
        self.target_port = target_port
        self.update_time = update_time
        self.version_count = version_count

    def validate(self):
        if self.health_check:
            self.health_check.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.quic_cid is not None:
            result['QuicCid'] = self.quic_cid
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.service_port is not None:
            result['ServicePort'] = self.service_port
        if self.status is not None:
            result['Status'] = self.status
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_count is not None:
            result['VersionCount'] = self.version_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')
        if m.get('HealthCheck') is not None:
            temp_model = ListEdgeContainerAppsResponseBodyAppsHealthCheck()
            self.health_check = temp_model.from_map(m['HealthCheck'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('QuicCid') is not None:
            self.quic_cid = m.get('QuicCid')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionCount') is not None:
            self.version_count = m.get('VersionCount')
        return self


class ListEdgeContainerAppsResponseBody(TeaModel):
    def __init__(
        self,
        apps: List[ListEdgeContainerAppsResponseBodyApps] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.apps = apps
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListEdgeContainerAppsResponseBodyApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEdgeContainerAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEdgeContainerAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEdgeContainerAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEdgeContainerRecordsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        record_match_type: str = None,
        record_name: str = None,
        site_id: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.record_match_type = record_match_type
        self.record_name = record_name
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.record_match_type is not None:
            result['RecordMatchType'] = self.record_match_type
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecordMatchType') is not None:
            self.record_match_type = m.get('RecordMatchType')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ListEdgeContainerRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        record_cname: str = None,
        record_name: str = None,
        site_id: int = None,
        site_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.record_cname = record_cname
        self.record_name = record_name
        self.site_id = site_id
        self.site_name = site_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.record_cname is not None:
            result['RecordCname'] = self.record_cname
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RecordCname') is not None:
            self.record_cname = m.get('RecordCname')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListEdgeContainerRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[ListEdgeContainerRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListEdgeContainerRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEdgeContainerRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEdgeContainerRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEdgeContainerRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEdgeRoutinePlansResponseBodyPlanInfo(TeaModel):
    def __init__(
        self,
        billing_mode: str = None,
        er_routine_code_version_quota: str = None,
        er_routine_quota: str = None,
        er_routine_route_site_count_quota: str = None,
        payment_method: str = None,
        plan_name: str = None,
    ):
        self.billing_mode = billing_mode
        self.er_routine_code_version_quota = er_routine_code_version_quota
        self.er_routine_quota = er_routine_quota
        self.er_routine_route_site_count_quota = er_routine_route_site_count_quota
        self.payment_method = payment_method
        self.plan_name = plan_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_mode is not None:
            result['BillingMode'] = self.billing_mode
        if self.er_routine_code_version_quota is not None:
            result['ErRoutineCodeVersionQuota'] = self.er_routine_code_version_quota
        if self.er_routine_quota is not None:
            result['ErRoutineQuota'] = self.er_routine_quota
        if self.er_routine_route_site_count_quota is not None:
            result['ErRoutineRouteSiteCountQuota'] = self.er_routine_route_site_count_quota
        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingMode') is not None:
            self.billing_mode = m.get('BillingMode')
        if m.get('ErRoutineCodeVersionQuota') is not None:
            self.er_routine_code_version_quota = m.get('ErRoutineCodeVersionQuota')
        if m.get('ErRoutineQuota') is not None:
            self.er_routine_quota = m.get('ErRoutineQuota')
        if m.get('ErRoutineRouteSiteCountQuota') is not None:
            self.er_routine_route_site_count_quota = m.get('ErRoutineRouteSiteCountQuota')
        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        return self


class ListEdgeRoutinePlansResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plan_info: List[ListEdgeRoutinePlansResponseBodyPlanInfo] = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.plan_info = plan_info
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.plan_info:
            for k in self.plan_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PlanInfo'] = []
        if self.plan_info is not None:
            for k in self.plan_info:
                result['PlanInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.plan_info = []
        if m.get('PlanInfo') is not None:
            for k in m.get('PlanInfo'):
                temp_model = ListEdgeRoutinePlansResponseBodyPlanInfo()
                self.plan_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListEdgeRoutinePlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEdgeRoutinePlansResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEdgeRoutinePlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEdgeRoutineRecordsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        record_match_type: str = None,
        record_name: str = None,
        site_id: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.record_match_type = record_match_type
        self.record_name = record_name
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.record_match_type is not None:
            result['RecordMatchType'] = self.record_match_type
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecordMatchType') is not None:
            self.record_match_type = m.get('RecordMatchType')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ListEdgeRoutineRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        record_cname: str = None,
        record_name: str = None,
        site_id: int = None,
        site_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.record_cname = record_cname
        self.record_name = record_name
        self.site_id = site_id
        self.site_name = site_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.record_cname is not None:
            result['RecordCname'] = self.record_cname
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RecordCname') is not None:
            self.record_cname = m.get('RecordCname')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListEdgeRoutineRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[ListEdgeRoutineRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListEdgeRoutineRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEdgeRoutineRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEdgeRoutineRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEdgeRoutineRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceQuotasRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        quota_names: str = None,
        site_id: int = None,
    ):
        self.instance_id = instance_id
        # This parameter is required.
        self.quota_names = quota_names
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.quota_names is not None:
            result['QuotaNames'] = self.quota_names
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QuotaNames') is not None:
            self.quota_names = m.get('QuotaNames')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ListInstanceQuotasResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        quota_name: str = None,
        quota_value: str = None,
        quota_value_type: str = None,
    ):
        self.quota_name = quota_name
        self.quota_value = quota_value
        self.quota_value_type = quota_value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value
        if self.quota_value_type is not None:
            result['QuotaValueType'] = self.quota_value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')
        if m.get('QuotaValueType') is not None:
            self.quota_value_type = m.get('QuotaValueType')
        return self


class ListInstanceQuotasResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        quotas: List[ListInstanceQuotasResponseBodyQuotas] = None,
        request_id: str = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.quotas = quotas
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListInstanceQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstanceQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceQuotasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstanceQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceQuotasWithUsageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        quota_names: str = None,
        site_id: int = None,
    ):
        self.instance_id = instance_id
        # This parameter is required.
        self.quota_names = quota_names
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.quota_names is not None:
            result['QuotaNames'] = self.quota_names
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QuotaNames') is not None:
            self.quota_names = m.get('QuotaNames')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ListInstanceQuotasWithUsageResponseBodyQuotasSiteUsage(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        site_name: str = None,
        site_usage: str = None,
    ):
        self.site_id = site_id
        self.site_name = site_name
        self.site_usage = site_usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')
        return self


class ListInstanceQuotasWithUsageResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        quota_name: str = None,
        quota_value: str = None,
        site_usage: List[ListInstanceQuotasWithUsageResponseBodyQuotasSiteUsage] = None,
        usage: str = None,
    ):
        self.quota_name = quota_name
        self.quota_value = quota_value
        self.site_usage = site_usage
        self.usage = usage

    def validate(self):
        if self.site_usage:
            for k in self.site_usage:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value
        result['SiteUsage'] = []
        if self.site_usage is not None:
            for k in self.site_usage:
                result['SiteUsage'].append(k.to_map() if k else None)
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')
        self.site_usage = []
        if m.get('SiteUsage') is not None:
            for k in m.get('SiteUsage'):
                temp_model = ListInstanceQuotasWithUsageResponseBodyQuotasSiteUsage()
                self.site_usage.append(temp_model.from_map(k))
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class ListInstanceQuotasWithUsageResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        quotas: List[ListInstanceQuotasWithUsageResponseBodyQuotas] = None,
        request_id: str = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.quotas = quotas
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListInstanceQuotasWithUsageResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstanceQuotasWithUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceQuotasWithUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstanceQuotasWithUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKvsRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
        prefix: str = None,
    ):
        # This parameter is required.
        self.namespace = namespace
        self.page_number = page_number
        self.page_size = page_size
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListKvsResponseBodyKeys(TeaModel):
    def __init__(
        self,
        name: str = None,
        update_time: str = None,
    ):
        self.name = name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListKvsResponseBody(TeaModel):
    def __init__(
        self,
        keys: List[ListKvsResponseBodyKeys] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.keys = keys
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.keys:
            for k in self.keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Keys'] = []
        if self.keys is not None:
            for k in self.keys:
                result['Keys'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.keys = []
        if m.get('Keys') is not None:
            for k in m.get('Keys'):
                temp_model = ListKvsResponseBodyKeys()
                self.keys.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListKvsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListKvsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListKvsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListsRequestQueryArgs(TeaModel):
    def __init__(
        self,
        desc: bool = None,
        description_like: str = None,
        id_like: str = None,
        item_like: str = None,
        kind: str = None,
        name_item_like: str = None,
        name_like: str = None,
        order_by: str = None,
    ):
        self.desc = desc
        self.description_like = description_like
        self.id_like = id_like
        self.item_like = item_like
        self.kind = kind
        self.name_item_like = name_item_like
        self.name_like = name_like
        self.order_by = order_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.description_like is not None:
            result['DescriptionLike'] = self.description_like
        if self.id_like is not None:
            result['IdLike'] = self.id_like
        if self.item_like is not None:
            result['ItemLike'] = self.item_like
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name_item_like is not None:
            result['NameItemLike'] = self.name_item_like
        if self.name_like is not None:
            result['NameLike'] = self.name_like
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('DescriptionLike') is not None:
            self.description_like = m.get('DescriptionLike')
        if m.get('IdLike') is not None:
            self.id_like = m.get('IdLike')
        if m.get('ItemLike') is not None:
            self.item_like = m.get('ItemLike')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('NameItemLike') is not None:
            self.name_item_like = m.get('NameItemLike')
        if m.get('NameLike') is not None:
            self.name_like = m.get('NameLike')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        return self


class ListListsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        query_args: ListListsRequestQueryArgs = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.query_args = query_args

    def validate(self):
        if self.query_args:
            self.query_args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_args is not None:
            result['QueryArgs'] = self.query_args.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryArgs') is not None:
            temp_model = ListListsRequestQueryArgs()
            self.query_args = temp_model.from_map(m['QueryArgs'])
        return self


class ListListsShrinkRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        query_args_shrink: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.query_args_shrink = query_args_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_args_shrink is not None:
            result['QueryArgs'] = self.query_args_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryArgs') is not None:
            self.query_args_shrink = m.get('QueryArgs')
        return self


class ListListsResponseBodyLists(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        kind: str = None,
        length: int = None,
        name: str = None,
        update_time: str = None,
    ):
        # 自定义响应页面描述
        self.description = description
        self.id = id
        self.kind = kind
        self.length = length
        self.name = name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.length is not None:
            result['Length'] = self.length
        if self.name is not None:
            result['Name'] = self.name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListListsResponseBody(TeaModel):
    def __init__(
        self,
        lists: List[ListListsResponseBodyLists] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        usage: int = None,
    ):
        self.lists = lists
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.usage = usage

    def validate(self):
        if self.lists:
            for k in self.lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Lists'] = []
        if self.lists is not None:
            for k in self.lists:
                result['Lists'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lists = []
        if m.get('Lists') is not None:
            for k in m.get('Lists'):
                temp_model = ListListsResponseBodyLists()
                self.lists.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class ListListsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListListsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListListsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLoadBalancerRegionsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListLoadBalancerRegionsResponseBodyRegionsSubRegions(TeaModel):
    def __init__(
        self,
        sub_region_cn_name: str = None,
        sub_region_code: str = None,
        sub_region_en_name: str = None,
    ):
        self.sub_region_cn_name = sub_region_cn_name
        self.sub_region_code = sub_region_code
        self.sub_region_en_name = sub_region_en_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_region_cn_name is not None:
            result['SubRegionCnName'] = self.sub_region_cn_name
        if self.sub_region_code is not None:
            result['SubRegionCode'] = self.sub_region_code
        if self.sub_region_en_name is not None:
            result['SubRegionEnName'] = self.sub_region_en_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubRegionCnName') is not None:
            self.sub_region_cn_name = m.get('SubRegionCnName')
        if m.get('SubRegionCode') is not None:
            self.sub_region_code = m.get('SubRegionCode')
        if m.get('SubRegionEnName') is not None:
            self.sub_region_en_name = m.get('SubRegionEnName')
        return self


class ListLoadBalancerRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_cn_name: str = None,
        region_code: str = None,
        region_en_name: str = None,
        sub_regions: List[ListLoadBalancerRegionsResponseBodyRegionsSubRegions] = None,
    ):
        self.region_cn_name = region_cn_name
        self.region_code = region_code
        self.region_en_name = region_en_name
        self.sub_regions = sub_regions

    def validate(self):
        if self.sub_regions:
            for k in self.sub_regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_cn_name is not None:
            result['RegionCnName'] = self.region_cn_name
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_en_name is not None:
            result['RegionEnName'] = self.region_en_name
        result['SubRegions'] = []
        if self.sub_regions is not None:
            for k in self.sub_regions:
                result['SubRegions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionCnName') is not None:
            self.region_cn_name = m.get('RegionCnName')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionEnName') is not None:
            self.region_en_name = m.get('RegionEnName')
        self.sub_regions = []
        if m.get('SubRegions') is not None:
            for k in m.get('SubRegions'):
                temp_model = ListLoadBalancerRegionsResponseBodyRegionsSubRegions()
                self.sub_regions.append(temp_model.from_map(k))
        return self


class ListLoadBalancerRegionsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        regions: List[ListLoadBalancerRegionsResponseBodyRegions] = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.regions = regions
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListLoadBalancerRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListLoadBalancerRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLoadBalancerRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLoadBalancerRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListManagedRulesGroupsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListManagedRulesGroupsResponseBodyManagedRulesGroups(TeaModel):
    def __init__(
        self,
        name: str = None,
        rule_count: int = None,
    ):
        self.name = name
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        return self


class ListManagedRulesGroupsResponseBody(TeaModel):
    def __init__(
        self,
        managed_rules_groups: List[ListManagedRulesGroupsResponseBodyManagedRulesGroups] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.managed_rules_groups = managed_rules_groups
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.managed_rules_groups:
            for k in self.managed_rules_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ManagedRulesGroups'] = []
        if self.managed_rules_groups is not None:
            for k in self.managed_rules_groups:
                result['ManagedRulesGroups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.managed_rules_groups = []
        if m.get('ManagedRulesGroups') is not None:
            for k in m.get('ManagedRulesGroups'):
                temp_model = ListManagedRulesGroupsResponseBodyManagedRulesGroups()
                self.managed_rules_groups.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListManagedRulesGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListManagedRulesGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListManagedRulesGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPagesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListPagesResponseBodyPages(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        id: int = None,
        kind: str = None,
        name: str = None,
        update_time: str = None,
    ):
        # 自定义响应页面内容BASE64编码
        # 
        # This parameter is required.
        self.content = content
        # 自定义响应页面内容类型
        # 
        # This parameter is required.
        self.content_type = content_type
        # 自定义响应页面描述
        self.description = description
        self.id = id
        self.kind = kind
        self.name = name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListPagesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pages: List[ListPagesResponseBodyPages] = None,
        request_id: str = None,
        total_count: int = None,
        usage: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.pages = pages
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.usage = usage

    def validate(self):
        if self.pages:
            for k in self.pages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Pages'] = []
        if self.pages is not None:
            for k in self.pages:
                result['Pages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.pages = []
        if m.get('Pages') is not None:
            for k in m.get('Pages'):
                temp_model = ListPagesResponseBodyPages()
                self.pages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class ListPagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecordsRequest(TeaModel):
    def __init__(
        self,
        biz_name: str = None,
        page_number: int = None,
        page_size: int = None,
        proxied: str = None,
        record_match_type: str = None,
        record_name: str = None,
        site_id: int = None,
        source_type: str = None,
        type: str = None,
    ):
        self.biz_name = biz_name
        self.page_number = page_number
        self.page_size = page_size
        self.proxied = proxied
        self.record_match_type = record_match_type
        self.record_name = record_name
        # This parameter is required.
        self.site_id = site_id
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proxied is not None:
            result['Proxied'] = self.proxied
        if self.record_match_type is not None:
            result['RecordMatchType'] = self.record_match_type
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')
        if m.get('RecordMatchType') is not None:
            self.record_match_type = m.get('RecordMatchType')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRecordsResponseBodyRecordsAuthConf(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        self.access_key = access_key
        self.auth_type = auth_type
        self.region = region
        self.secret_key = secret_key
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.region is not None:
            result['Region'] = self.region
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListRecordsResponseBodyRecordsData(TeaModel):
    def __init__(
        self,
        algorithm: int = None,
        certificate: str = None,
        fingerprint: str = None,
        flag: int = None,
        key_tag: int = None,
        matching_type: int = None,
        port: int = None,
        priority: int = None,
        selector: int = None,
        tag: str = None,
        type: int = None,
        usage: int = None,
        value: str = None,
        weight: int = None,
    ):
        self.algorithm = algorithm
        self.certificate = certificate
        self.fingerprint = fingerprint
        self.flag = flag
        self.key_tag = key_tag
        self.matching_type = matching_type
        self.port = port
        self.priority = priority
        self.selector = selector
        self.tag = tag
        self.type = type
        self.usage = usage
        self.value = value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.matching_type is not None:
            result['MatchingType'] = self.matching_type
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.selector is not None:
            result['Selector'] = self.selector
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.value is not None:
            result['Value'] = self.value
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('MatchingType') is not None:
            self.matching_type = m.get('MatchingType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Selector') is not None:
            self.selector = m.get('Selector')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ListRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        auth_conf: ListRecordsResponseBodyRecordsAuthConf = None,
        biz_name: str = None,
        comment: str = None,
        create_time: str = None,
        data: ListRecordsResponseBodyRecordsData = None,
        host_policy: str = None,
        proxied: bool = None,
        record_cname: str = None,
        record_id: int = None,
        record_name: str = None,
        record_source_type: str = None,
        record_type: str = None,
        site_id: int = None,
        site_name: str = None,
        ttl: int = None,
        update_time: str = None,
    ):
        self.auth_conf = auth_conf
        self.biz_name = biz_name
        self.comment = comment
        self.create_time = create_time
        self.data = data
        self.host_policy = host_policy
        self.proxied = proxied
        self.record_cname = record_cname
        self.record_id = record_id
        self.record_name = record_name
        self.record_source_type = record_source_type
        self.record_type = record_type
        self.site_id = site_id
        self.site_name = site_name
        self.ttl = ttl
        self.update_time = update_time

    def validate(self):
        if self.auth_conf:
            self.auth_conf.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_conf is not None:
            result['AuthConf'] = self.auth_conf.to_map()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.host_policy is not None:
            result['HostPolicy'] = self.host_policy
        if self.proxied is not None:
            result['Proxied'] = self.proxied
        if self.record_cname is not None:
            result['RecordCname'] = self.record_cname
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.record_name is not None:
            result['RecordName'] = self.record_name
        if self.record_source_type is not None:
            result['RecordSourceType'] = self.record_source_type
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConf') is not None:
            temp_model = ListRecordsResponseBodyRecordsAuthConf()
            self.auth_conf = temp_model.from_map(m['AuthConf'])
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            temp_model = ListRecordsResponseBodyRecordsData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')
        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')
        if m.get('RecordCname') is not None:
            self.record_cname = m.get('RecordCname')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')
        if m.get('RecordSourceType') is not None:
            self.record_source_type = m.get('RecordSourceType')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[ListRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoutineCanaryAreasResponseBody(TeaModel):
    def __init__(
        self,
        canary_areas: List[str] = None,
        request_id: str = None,
    ):
        self.canary_areas = canary_areas
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.canary_areas is not None:
            result['CanaryAreas'] = self.canary_areas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanaryAreas') is not None:
            self.canary_areas = m.get('CanaryAreas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRoutineCanaryAreasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRoutineCanaryAreasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRoutineCanaryAreasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoutineOptionalSpecsResponseBodySpecs(TeaModel):
    def __init__(
        self,
        is_available: bool = None,
        spec_name: str = None,
    ):
        self.is_available = is_available
        self.spec_name = spec_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_available is not None:
            result['IsAvailable'] = self.is_available
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        return self


class ListRoutineOptionalSpecsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        specs: List[ListRoutineOptionalSpecsResponseBodySpecs] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.specs = specs

    def validate(self):
        if self.specs:
            for k in self.specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Specs'] = []
        if self.specs is not None:
            for k in self.specs:
                result['Specs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.specs = []
        if m.get('Specs') is not None:
            for k in m.get('Specs'):
                temp_model = ListRoutineOptionalSpecsResponseBodySpecs()
                self.specs.append(temp_model.from_map(k))
        return self


class ListRoutineOptionalSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRoutineOptionalSpecsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRoutineOptionalSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScheduledPreloadExecutionsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListScheduledPreloadExecutionsResponseBodyExecutions(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        end_time: str = None,
        id: str = None,
        interval: int = None,
        job_id: str = None,
        slice_len: int = None,
        start_time: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.end_time = end_time
        self.id = id
        self.interval = interval
        self.job_id = job_id
        self.slice_len = slice_len
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListScheduledPreloadExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        executions: List[ListScheduledPreloadExecutionsResponseBodyExecutions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.executions = executions
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.executions:
            for k in self.executions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Executions'] = []
        if self.executions is not None:
            for k in self.executions:
                result['Executions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.executions = []
        if m.get('Executions') is not None:
            for k in m.get('Executions'):
                temp_model = ListScheduledPreloadExecutionsResponseBodyExecutions()
                self.executions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListScheduledPreloadExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScheduledPreloadExecutionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListScheduledPreloadExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScheduledPreloadJobsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        site_id: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.site_id = site_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListScheduledPreloadJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        created_at: str = None,
        domains: str = None,
        error_info: str = None,
        failed_file_oss: str = None,
        file_id: str = None,
        id: str = None,
        insert_way: str = None,
        name: str = None,
        site_id: int = None,
        task_submitted: int = None,
        task_type: str = None,
        url_count: int = None,
        url_submitted: int = None,
    ):
        self.ali_uid = ali_uid
        self.created_at = created_at
        self.domains = domains
        self.error_info = error_info
        self.failed_file_oss = failed_file_oss
        self.file_id = file_id
        self.id = id
        self.insert_way = insert_way
        self.name = name
        self.site_id = site_id
        self.task_submitted = task_submitted
        self.task_type = task_type
        self.url_count = url_count
        self.url_submitted = url_submitted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.failed_file_oss is not None:
            result['FailedFileOss'] = self.failed_file_oss
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id is not None:
            result['Id'] = self.id
        if self.insert_way is not None:
            result['InsertWay'] = self.insert_way
        if self.name is not None:
            result['Name'] = self.name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.task_submitted is not None:
            result['TaskSubmitted'] = self.task_submitted
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.url_count is not None:
            result['UrlCount'] = self.url_count
        if self.url_submitted is not None:
            result['UrlSubmitted'] = self.url_submitted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('FailedFileOss') is not None:
            self.failed_file_oss = m.get('FailedFileOss')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsertWay') is not None:
            self.insert_way = m.get('InsertWay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaskSubmitted') is not None:
            self.task_submitted = m.get('TaskSubmitted')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UrlCount') is not None:
            self.url_count = m.get('UrlCount')
        if m.get('UrlSubmitted') is not None:
            self.url_submitted = m.get('UrlSubmitted')
        return self


class ListScheduledPreloadJobsResponseBody(TeaModel):
    def __init__(
        self,
        jobs: List[ListScheduledPreloadJobsResponseBodyJobs] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.jobs = jobs
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListScheduledPreloadJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListScheduledPreloadJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScheduledPreloadJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListScheduledPreloadJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSiteDeliveryTasksRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        page_number: int = None,
        page_size: int = None,
        site_id: int = None,
    ):
        self.business_type = business_type
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ListSiteDeliveryTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        status: str = None,
        task_name: str = None,
    ):
        self.business_type = business_type
        self.data_center = data_center
        self.delivery_type = delivery_type
        self.status = status
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListSiteDeliveryTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[ListSiteDeliveryTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListSiteDeliveryTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSiteDeliveryTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSiteDeliveryTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSiteDeliveryTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSitesRequestTagFilter(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListSitesRequest(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        coverage: str = None,
        only_enterprise: bool = None,
        page_number: int = None,
        page_size: int = None,
        plan_subscribe_type: str = None,
        resource_group_id: str = None,
        site_name: str = None,
        site_search_type: str = None,
        status: str = None,
        tag_filter: List[ListSitesRequestTagFilter] = None,
    ):
        self.access_type = access_type
        self.coverage = coverage
        self.only_enterprise = only_enterprise
        self.page_number = page_number
        self.page_size = page_size
        self.plan_subscribe_type = plan_subscribe_type
        self.resource_group_id = resource_group_id
        self.site_name = site_name
        self.site_search_type = site_search_type
        self.status = status
        self.tag_filter = tag_filter

    def validate(self):
        if self.tag_filter:
            for k in self.tag_filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.only_enterprise is not None:
            result['OnlyEnterprise'] = self.only_enterprise
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plan_subscribe_type is not None:
            result['PlanSubscribeType'] = self.plan_subscribe_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.site_search_type is not None:
            result['SiteSearchType'] = self.site_search_type
        if self.status is not None:
            result['Status'] = self.status
        result['TagFilter'] = []
        if self.tag_filter is not None:
            for k in self.tag_filter:
                result['TagFilter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('OnlyEnterprise') is not None:
            self.only_enterprise = m.get('OnlyEnterprise')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlanSubscribeType') is not None:
            self.plan_subscribe_type = m.get('PlanSubscribeType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('SiteSearchType') is not None:
            self.site_search_type = m.get('SiteSearchType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag_filter = []
        if m.get('TagFilter') is not None:
            for k in m.get('TagFilter'):
                temp_model = ListSitesRequestTagFilter()
                self.tag_filter.append(temp_model.from_map(k))
        return self


class ListSitesShrinkRequest(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        coverage: str = None,
        only_enterprise: bool = None,
        page_number: int = None,
        page_size: int = None,
        plan_subscribe_type: str = None,
        resource_group_id: str = None,
        site_name: str = None,
        site_search_type: str = None,
        status: str = None,
        tag_filter_shrink: str = None,
    ):
        self.access_type = access_type
        self.coverage = coverage
        self.only_enterprise = only_enterprise
        self.page_number = page_number
        self.page_size = page_size
        self.plan_subscribe_type = plan_subscribe_type
        self.resource_group_id = resource_group_id
        self.site_name = site_name
        self.site_search_type = site_search_type
        self.status = status
        self.tag_filter_shrink = tag_filter_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.only_enterprise is not None:
            result['OnlyEnterprise'] = self.only_enterprise
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plan_subscribe_type is not None:
            result['PlanSubscribeType'] = self.plan_subscribe_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.site_search_type is not None:
            result['SiteSearchType'] = self.site_search_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_filter_shrink is not None:
            result['TagFilter'] = self.tag_filter_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('OnlyEnterprise') is not None:
            self.only_enterprise = m.get('OnlyEnterprise')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlanSubscribeType') is not None:
            self.plan_subscribe_type = m.get('PlanSubscribeType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('SiteSearchType') is not None:
            self.site_search_type = m.get('SiteSearchType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagFilter') is not None:
            self.tag_filter_shrink = m.get('TagFilter')
        return self


class ListSitesResponseBodySites(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        cname_zone: str = None,
        coverage: str = None,
        create_time: str = None,
        instance_id: str = None,
        name_server_list: str = None,
        plan_name: str = None,
        plan_spec_name: str = None,
        resource_group_id: str = None,
        site_id: int = None,
        site_name: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        update_time: str = None,
        verify_code: str = None,
    ):
        self.access_type = access_type
        self.cname_zone = cname_zone
        self.coverage = coverage
        self.create_time = create_time
        self.instance_id = instance_id
        self.name_server_list = name_server_list
        self.plan_name = plan_name
        self.plan_spec_name = plan_spec_name
        self.resource_group_id = resource_group_id
        self.site_id = site_id
        self.site_name = site_name
        self.status = status
        self.tags = tags
        self.update_time = update_time
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.cname_zone is not None:
            result['CnameZone'] = self.cname_zone
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name_server_list is not None:
            result['NameServerList'] = self.name_server_list
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_spec_name is not None:
            result['PlanSpecName'] = self.plan_spec_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('CnameZone') is not None:
            self.cname_zone = m.get('CnameZone')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NameServerList') is not None:
            self.name_server_list = m.get('NameServerList')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanSpecName') is not None:
            self.plan_spec_name = m.get('PlanSpecName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class ListSitesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sites: List[ListSitesResponseBodySites] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.sites = sites
        self.total_count = total_count

    def validate(self):
        if self.sites:
            for k in self.sites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Sites'] = []
        if self.sites is not None:
            for k in self.sites:
                result['Sites'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sites = []
        if m.get('Sites') is not None:
            for k in m.get('Sites'):
                temp_model = ListSitesResponseBodySites()
                self.sites.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSitesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSitesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSitesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签键
        self.key = key
        # 标签值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        max_item: int = None,
        next_token: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        security_token: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.max_item = max_item
        self.next_token = next_token
        self.owner_id = owner_id
        # 要创建并绑定标签的资源所在的地域ID。
        # 
        # This parameter is required.
        self.region_id = region_id
        # 资源ID,最多 50个子项
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.security_token = security_token
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_item is not None:
            result['MaxItem'] = self.max_item
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxItem') is not None:
            self.max_item = m.get('MaxItem')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
        total_count: int = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources
        self.total_count = total_count

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUploadTasksRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        site_id: int = None,
        start_time: str = None,
        type: str = None,
    ):
        self.end_time = end_time
        self.site_id = site_id
        self.start_time = start_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListUploadTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        error_code: str = None,
        status: str = None,
        type: str = None,
        upload_id: str = None,
        upload_task_name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.error_code = error_code
        self.status = status
        self.type = type
        self.upload_id = upload_id
        self.upload_task_name = upload_task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.upload_id is not None:
            result['UploadId'] = self.upload_id
        if self.upload_task_name is not None:
            result['UploadTaskName'] = self.upload_task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')
        if m.get('UploadTaskName') is not None:
            self.upload_task_name = m.get('UploadTaskName')
        return self


class ListUploadTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[ListUploadTasksResponseBodyTasks] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListUploadTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListUploadTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUploadTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUploadTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDeliveryTasksRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.business_type = business_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserDeliveryTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        status: str = None,
        task_name: str = None,
    ):
        self.business_type = business_type
        self.data_center = data_center
        self.delivery_type = delivery_type
        self.status = status
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListUserDeliveryTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[ListUserDeliveryTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListUserDeliveryTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserDeliveryTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserDeliveryTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserDeliveryTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserRatePlanInstancesRequest(TeaModel):
    def __init__(
        self,
        check_remaining_site_quota: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        status: str = None,
    ):
        self.check_remaining_site_quota = check_remaining_site_quota
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_remaining_site_quota is not None:
            result['CheckRemainingSiteQuota'] = self.check_remaining_site_quota
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRemainingSiteQuota') is not None:
            self.check_remaining_site_quota = m.get('CheckRemainingSiteQuota')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListUserRatePlanInstancesResponseBodyInstanceInfoSites(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        site_name: str = None,
        site_status: str = None,
    ):
        self.site_id = site_id
        self.site_name = site_name
        self.site_status = site_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.site_status is not None:
            result['SiteStatus'] = self.site_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('SiteStatus') is not None:
            self.site_status = m.get('SiteStatus')
        return self


class ListUserRatePlanInstancesResponseBodyInstanceInfo(TeaModel):
    def __init__(
        self,
        billing_mode: str = None,
        coverages: str = None,
        create_time: str = None,
        duration: int = None,
        expire_time: str = None,
        instance_id: str = None,
        plan_name: str = None,
        plan_type: str = None,
        site_quota: str = None,
        sites: List[ListUserRatePlanInstancesResponseBodyInstanceInfoSites] = None,
        status: str = None,
    ):
        self.billing_mode = billing_mode
        self.coverages = coverages
        self.create_time = create_time
        self.duration = duration
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.plan_name = plan_name
        self.plan_type = plan_type
        self.site_quota = site_quota
        self.sites = sites
        self.status = status

    def validate(self):
        if self.sites:
            for k in self.sites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_mode is not None:
            result['BillingMode'] = self.billing_mode
        if self.coverages is not None:
            result['Coverages'] = self.coverages
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        if self.site_quota is not None:
            result['SiteQuota'] = self.site_quota
        result['Sites'] = []
        if self.sites is not None:
            for k in self.sites:
                result['Sites'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingMode') is not None:
            self.billing_mode = m.get('BillingMode')
        if m.get('Coverages') is not None:
            self.coverages = m.get('Coverages')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        if m.get('SiteQuota') is not None:
            self.site_quota = m.get('SiteQuota')
        self.sites = []
        if m.get('Sites') is not None:
            for k in m.get('Sites'):
                temp_model = ListUserRatePlanInstancesResponseBodyInstanceInfoSites()
                self.sites.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListUserRatePlanInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_info: List[ListUserRatePlanInstancesResponseBodyInstanceInfo] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.instance_info = instance_info
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.instance_info:
            for k in self.instance_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k in self.instance_info:
                result['InstanceInfo'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k in m.get('InstanceInfo'):
                temp_model = ListUserRatePlanInstancesResponseBodyInstanceInfo()
                self.instance_info.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListUserRatePlanInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserRatePlanInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserRatePlanInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWafManagedRulesRequestQueryArgs(TeaModel):
    def __init__(
        self,
        action: str = None,
        id_name_like: str = None,
        protection_level: int = None,
        protection_levels: List[int] = None,
        status: str = None,
    ):
        self.action = action
        self.id_name_like = id_name_like
        self.protection_level = protection_level
        self.protection_levels = protection_levels
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.id_name_like is not None:
            result['IdNameLike'] = self.id_name_like
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
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
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('ProtectionLevels') is not None:
            self.protection_levels = m.get('ProtectionLevels')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListWafManagedRulesRequest(TeaModel):
    def __init__(
        self,
        attack_type: int = None,
        id: int = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        query_args: ListWafManagedRulesRequestQueryArgs = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.attack_type = attack_type
        # This parameter is required.
        self.id = id
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.query_args = query_args
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        if self.query_args:
            self.query_args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.id is not None:
            result['Id'] = self.id
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryArgs') is not None:
            temp_model = ListWafManagedRulesRequestQueryArgs()
            self.query_args = temp_model.from_map(m['QueryArgs'])
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ListWafManagedRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        attack_type: int = None,
        id: int = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        query_args_shrink: str = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.attack_type = attack_type
        # This parameter is required.
        self.id = id
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.query_args_shrink = query_args_shrink
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.id is not None:
            result['Id'] = self.id
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryArgs') is not None:
            self.query_args_shrink = m.get('QueryArgs')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ListWafManagedRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        action: str = None,
        id: int = None,
        name: str = None,
        protection_level: int = None,
        status: str = None,
    ):
        self.action = action
        self.id = id
        self.name = name
        self.protection_level = protection_level
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListWafManagedRulesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[ListWafManagedRulesResponseBodyRules] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.rules = rules
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListWafManagedRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListWafManagedRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWafManagedRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWafManagedRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWafPhasesRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        site_version: int = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class ListWafPhasesResponseBodyPhasesRulesets(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        rules: List[WafRuleConfig] = None,
        shared: WafBatchRuleShared = None,
    ):
        self.id = id
        self.name = name
        self.rules = rules
        self.shared = shared

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()
        if self.shared:
            self.shared.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.shared is not None:
            result['Shared'] = self.shared.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = WafRuleConfig()
                self.rules.append(temp_model.from_map(k))
        if m.get('Shared') is not None:
            temp_model = WafBatchRuleShared()
            self.shared = temp_model.from_map(m['Shared'])
        return self


class ListWafPhasesResponseBodyPhases(TeaModel):
    def __init__(
        self,
        phase: str = None,
        rulesets: List[ListWafPhasesResponseBodyPhasesRulesets] = None,
    ):
        self.phase = phase
        self.rulesets = rulesets

    def validate(self):
        if self.rulesets:
            for k in self.rulesets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['Phase'] = self.phase
        result['Rulesets'] = []
        if self.rulesets is not None:
            for k in self.rulesets:
                result['Rulesets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        self.rulesets = []
        if m.get('Rulesets') is not None:
            for k in m.get('Rulesets'):
                temp_model = ListWafPhasesResponseBodyPhasesRulesets()
                self.rulesets.append(temp_model.from_map(k))
        return self


class ListWafPhasesResponseBody(TeaModel):
    def __init__(
        self,
        phases: List[ListWafPhasesResponseBodyPhases] = None,
        request_id: str = None,
    ):
        self.phases = phases
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.phases:
            for k in self.phases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Phases'] = []
        if self.phases is not None:
            for k in self.phases:
                result['Phases'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.phases = []
        if m.get('Phases') is not None:
            for k in m.get('Phases'):
                temp_model = ListWafPhasesResponseBodyPhases()
                self.phases.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListWafPhasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWafPhasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWafPhasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWafRulesRequestQueryArgs(TeaModel):
    def __init__(
        self,
        desc: bool = None,
        id: int = None,
        id_name_like: str = None,
        name_like: str = None,
        order_by: str = None,
        ruleset_id: int = None,
        status: str = None,
    ):
        self.desc = desc
        self.id = id
        self.id_name_like = id_name_like
        self.name_like = name_like
        self.order_by = order_by
        self.ruleset_id = ruleset_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.id is not None:
            result['Id'] = self.id
        if self.id_name_like is not None:
            result['IdNameLike'] = self.id_name_like
        if self.name_like is not None:
            result['NameLike'] = self.name_like
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdNameLike') is not None:
            self.id_name_like = m.get('IdNameLike')
        if m.get('NameLike') is not None:
            self.name_like = m.get('NameLike')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListWafRulesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        phase: str = None,
        query_args: ListWafRulesRequestQueryArgs = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.phase = phase
        self.query_args = query_args
        # This parameter is required.
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        if self.query_args:
            self.query_args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.query_args is not None:
            result['QueryArgs'] = self.query_args.to_map()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('QueryArgs') is not None:
            temp_model = ListWafRulesRequestQueryArgs()
            self.query_args = temp_model.from_map(m['QueryArgs'])
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class ListWafRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        phase: str = None,
        query_args_shrink: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.phase = phase
        self.query_args_shrink = query_args_shrink
        # This parameter is required.
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.query_args_shrink is not None:
            result['QueryArgs'] = self.query_args_shrink
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('QueryArgs') is not None:
            self.query_args_shrink = m.get('QueryArgs')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class ListWafRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        action: str = None,
        characteristics_fields: List[str] = None,
        config: WafRuleConfig = None,
        fields: List[str] = None,
        id: int = None,
        name: str = None,
        phase: str = None,
        position: int = None,
        ruleset_id: int = None,
        skip: str = None,
        status: str = None,
        tags: List[str] = None,
        timer: WafTimer = None,
        type: str = None,
        update_time: str = None,
    ):
        self.action = action
        self.characteristics_fields = characteristics_fields
        self.config = config
        self.fields = fields
        self.id = id
        self.name = name
        self.phase = phase
        self.position = position
        self.ruleset_id = ruleset_id
        self.skip = skip
        self.status = status
        self.tags = tags
        self.timer = timer
        self.type = type
        self.update_time = update_time

    def validate(self):
        if self.config:
            self.config.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.characteristics_fields is not None:
            result['CharacteristicsFields'] = self.characteristics_fields
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.position is not None:
            result['Position'] = self.position
        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('CharacteristicsFields') is not None:
            self.characteristics_fields = m.get('CharacteristicsFields')
        if m.get('Config') is not None:
            temp_model = WafRuleConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Timer') is not None:
            temp_model = WafTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListWafRulesResponseBody(TeaModel):
    def __init__(
        self,
        instance_usage: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[ListWafRulesResponseBodyRules] = None,
        site_usage: int = None,
        total_count: int = None,
    ):
        self.instance_usage = instance_usage
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.rules = rules
        self.site_usage = site_usage
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_usage is not None:
            result['InstanceUsage'] = self.instance_usage
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceUsage') is not None:
            self.instance_usage = m.get('InstanceUsage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListWafRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListWafRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWafRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWafRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWafRulesetsRequestQueryArgs(TeaModel):
    def __init__(
        self,
        any_like: str = None,
        desc: bool = None,
        name_like: str = None,
        order_by: str = None,
    ):
        self.any_like = any_like
        self.desc = desc
        self.name_like = name_like
        self.order_by = order_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.any_like is not None:
            result['AnyLike'] = self.any_like
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name_like is not None:
            result['NameLike'] = self.name_like
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnyLike') is not None:
            self.any_like = m.get('AnyLike')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('NameLike') is not None:
            self.name_like = m.get('NameLike')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        return self


class ListWafRulesetsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        phase: str = None,
        query_args: ListWafRulesetsRequestQueryArgs = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.phase = phase
        self.query_args = query_args
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        if self.query_args:
            self.query_args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.query_args is not None:
            result['QueryArgs'] = self.query_args.to_map()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('QueryArgs') is not None:
            temp_model = ListWafRulesetsRequestQueryArgs()
            self.query_args = temp_model.from_map(m['QueryArgs'])
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class ListWafRulesetsShrinkRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        phase: str = None,
        query_args_shrink: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.phase = phase
        self.query_args_shrink = query_args_shrink
        self.site_id = site_id
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.query_args_shrink is not None:
            result['QueryArgs'] = self.query_args_shrink
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('QueryArgs') is not None:
            self.query_args_shrink = m.get('QueryArgs')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        return self


class ListWafRulesetsResponseBodyRulesets(TeaModel):
    def __init__(
        self,
        fields: List[str] = None,
        id: int = None,
        name: str = None,
        phase: str = None,
        status: str = None,
        target: str = None,
        types: List[str] = None,
        update_time: str = None,
    ):
        self.fields = fields
        self.id = id
        self.name = name
        self.phase = phase
        self.status = status
        self.target = target
        self.types = types
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.status is not None:
            result['Status'] = self.status
        if self.target is not None:
            result['Target'] = self.target
        if self.types is not None:
            result['Types'] = self.types
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListWafRulesetsResponseBody(TeaModel):
    def __init__(
        self,
        instance_usage: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rulesets: List[ListWafRulesetsResponseBodyRulesets] = None,
        site_usage: int = None,
        total_count: int = None,
    ):
        self.instance_usage = instance_usage
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.rulesets = rulesets
        self.site_usage = site_usage
        self.total_count = total_count

    def validate(self):
        if self.rulesets:
            for k in self.rulesets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_usage is not None:
            result['InstanceUsage'] = self.instance_usage
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rulesets'] = []
        if self.rulesets is not None:
            for k in self.rulesets:
                result['Rulesets'].append(k.to_map() if k else None)
        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceUsage') is not None:
            self.instance_usage = m.get('InstanceUsage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rulesets = []
        if m.get('Rulesets') is not None:
            for k in m.get('Rulesets'):
                temp_model = ListWafRulesetsResponseBodyRulesets()
                self.rulesets.append(temp_model.from_map(k))
        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListWafRulesetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWafRulesetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWafRulesetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWafTemplateRulesRequestQueryArgs(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListWafTemplateRulesRequest(TeaModel):
    def __init__(
        self,
        phase: str = None,
        query_args: ListWafTemplateRulesRequestQueryArgs = None,
    ):
        self.phase = phase
        self.query_args = query_args

    def validate(self):
        if self.query_args:
            self.query_args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.query_args is not None:
            result['QueryArgs'] = self.query_args.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('QueryArgs') is not None:
            temp_model = ListWafTemplateRulesRequestQueryArgs()
            self.query_args = temp_model.from_map(m['QueryArgs'])
        return self


class ListWafTemplateRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        phase: str = None,
        query_args_shrink: str = None,
    ):
        self.phase = phase
        self.query_args_shrink = query_args_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.query_args_shrink is not None:
            result['QueryArgs'] = self.query_args_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('QueryArgs') is not None:
            self.query_args_shrink = m.get('QueryArgs')
        return self


class ListWafTemplateRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        config: WafRuleConfig = None,
        name: str = None,
        phase: str = None,
        status: str = None,
        type: str = None,
    ):
        self.config = config
        self.name = name
        self.phase = phase
        self.status = status
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = WafRuleConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListWafTemplateRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rules: List[ListWafTemplateRulesResponseBodyRules] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListWafTemplateRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class ListWafTemplateRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWafTemplateRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWafTemplateRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWafUsageOfRulesRequest(TeaModel):
    def __init__(
        self,
        phase: str = None,
        site_id: int = None,
    ):
        self.phase = phase
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class ListWafUsageOfRulesResponseBodySites(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        usage: int = None,
    ):
        self.id = id
        self.name = name
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class ListWafUsageOfRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sites: List[ListWafUsageOfRulesResponseBodySites] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.sites = sites

    def validate(self):
        if self.sites:
            for k in self.sites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Sites'] = []
        if self.sites is not None:
            for k in self.sites:
                result['Sites'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sites = []
        if m.get('Sites') is not None:
            for k in m.get('Sites'):
                temp_model = ListWafUsageOfRulesResponseBodySites()
                self.sites.append(temp_model.from_map(k))
        return self


class ListWafUsageOfRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWafUsageOfRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWafUsageOfRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWaitingRoomEventsRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        waiting_room_event_id: int = None,
        waiting_room_id: str = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        self.waiting_room_event_id = waiting_room_event_id
        # This parameter is required.
        self.waiting_room_id = waiting_room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.waiting_room_event_id is not None:
            result['WaitingRoomEventId'] = self.waiting_room_event_id
        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('WaitingRoomEventId') is not None:
            self.waiting_room_event_id = m.get('WaitingRoomEventId')
        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')
        return self


class ListWaitingRoomEventsResponseBodyWaitingRoomEvents(TeaModel):
    def __init__(
        self,
        custom_page_html: str = None,
        description: str = None,
        disable_session_renewal_enable: str = None,
        enable: str = None,
        end_time: str = None,
        json_response_enable: str = None,
        language: str = None,
        name: str = None,
        new_users_per_minute: str = None,
        pre_queue_enable: str = None,
        pre_queue_start_time: str = None,
        queuing_method: str = None,
        queuing_status_code: str = None,
        random_pre_queue_enable: str = None,
        session_duration: str = None,
        start_time: str = None,
        total_active_users: str = None,
        waiting_room_event_id: int = None,
        waiting_room_id: str = None,
        waiting_room_type: str = None,
    ):
        self.custom_page_html = custom_page_html
        self.description = description
        self.disable_session_renewal_enable = disable_session_renewal_enable
        self.enable = enable
        self.end_time = end_time
        self.json_response_enable = json_response_enable
        self.language = language
        self.name = name
        self.new_users_per_minute = new_users_per_minute
        self.pre_queue_enable = pre_queue_enable
        self.pre_queue_start_time = pre_queue_start_time
        self.queuing_method = queuing_method
        self.queuing_status_code = queuing_status_code
        self.random_pre_queue_enable = random_pre_queue_enable
        self.session_duration = session_duration
        self.start_time = start_time
        self.total_active_users = total_active_users
        self.waiting_room_event_id = waiting_room_event_id
        self.waiting_room_id = waiting_room_id
        self.waiting_room_type = waiting_room_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_session_renewal_enable is not None:
            result['DisableSessionRenewalEnable'] = self.disable_session_renewal_enable
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.json_response_enable is not None:
            result['JsonResponseEnable'] = self.json_response_enable
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.new_users_per_minute is not None:
            result['NewUsersPerMinute'] = self.new_users_per_minute
        if self.pre_queue_enable is not None:
            result['PreQueueEnable'] = self.pre_queue_enable
        if self.pre_queue_start_time is not None:
            result['PreQueueStartTime'] = self.pre_queue_start_time
        if self.queuing_method is not None:
            result['QueuingMethod'] = self.queuing_method
        if self.queuing_status_code is not None:
            result['QueuingStatusCode'] = self.queuing_status_code
        if self.random_pre_queue_enable is not None:
            result['RandomPreQueueEnable'] = self.random_pre_queue_enable
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users
        if self.waiting_room_event_id is not None:
            result['WaitingRoomEventId'] = self.waiting_room_event_id
        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id
        if self.waiting_room_type is not None:
            result['WaitingRoomType'] = self.waiting_room_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableSessionRenewalEnable') is not None:
            self.disable_session_renewal_enable = m.get('DisableSessionRenewalEnable')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JsonResponseEnable') is not None:
            self.json_response_enable = m.get('JsonResponseEnable')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewUsersPerMinute') is not None:
            self.new_users_per_minute = m.get('NewUsersPerMinute')
        if m.get('PreQueueEnable') is not None:
            self.pre_queue_enable = m.get('PreQueueEnable')
        if m.get('PreQueueStartTime') is not None:
            self.pre_queue_start_time = m.get('PreQueueStartTime')
        if m.get('QueuingMethod') is not None:
            self.queuing_method = m.get('QueuingMethod')
        if m.get('QueuingStatusCode') is not None:
            self.queuing_status_code = m.get('QueuingStatusCode')
        if m.get('RandomPreQueueEnable') is not None:
            self.random_pre_queue_enable = m.get('RandomPreQueueEnable')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')
        if m.get('WaitingRoomEventId') is not None:
            self.waiting_room_event_id = m.get('WaitingRoomEventId')
        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')
        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')
        return self


class ListWaitingRoomEventsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        waiting_room_events: List[ListWaitingRoomEventsResponseBodyWaitingRoomEvents] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.waiting_room_events = waiting_room_events

    def validate(self):
        if self.waiting_room_events:
            for k in self.waiting_room_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WaitingRoomEvents'] = []
        if self.waiting_room_events is not None:
            for k in self.waiting_room_events:
                result['WaitingRoomEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.waiting_room_events = []
        if m.get('WaitingRoomEvents') is not None:
            for k in m.get('WaitingRoomEvents'):
                temp_model = ListWaitingRoomEventsResponseBodyWaitingRoomEvents()
                self.waiting_room_events.append(temp_model.from_map(k))
        return self


class ListWaitingRoomEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWaitingRoomEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWaitingRoomEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWaitingRoomRulesRequest(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
        site_id: int = None,
        waiting_room_id: str = None,
        waiting_room_rule_id: int = None,
    ):
        self.rule_name = rule_name
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.waiting_room_id = waiting_room_id
        self.waiting_room_rule_id = waiting_room_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id
        if self.waiting_room_rule_id is not None:
            result['WaitingRoomRuleId'] = self.waiting_room_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')
        if m.get('WaitingRoomRuleId') is not None:
            self.waiting_room_rule_id = m.get('WaitingRoomRuleId')
        return self


class ListWaitingRoomRulesResponseBodyWaitingRoomRules(TeaModel):
    def __init__(
        self,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        waiting_room_rule_id: int = None,
    ):
        self.rule = rule
        self.rule_enable = rule_enable
        self.rule_name = rule_name
        self.waiting_room_rule_id = waiting_room_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.waiting_room_rule_id is not None:
            result['WaitingRoomRuleId'] = self.waiting_room_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('WaitingRoomRuleId') is not None:
            self.waiting_room_rule_id = m.get('WaitingRoomRuleId')
        return self


class ListWaitingRoomRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        waiting_room_rules: List[ListWaitingRoomRulesResponseBodyWaitingRoomRules] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.waiting_room_rules = waiting_room_rules

    def validate(self):
        if self.waiting_room_rules:
            for k in self.waiting_room_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WaitingRoomRules'] = []
        if self.waiting_room_rules is not None:
            for k in self.waiting_room_rules:
                result['WaitingRoomRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.waiting_room_rules = []
        if m.get('WaitingRoomRules') is not None:
            for k in m.get('WaitingRoomRules'):
                temp_model = ListWaitingRoomRulesResponseBodyWaitingRoomRules()
                self.waiting_room_rules.append(temp_model.from_map(k))
        return self


class ListWaitingRoomRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWaitingRoomRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWaitingRoomRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWaitingRoomsRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        waiting_room_id: str = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        self.waiting_room_id = waiting_room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')
        return self


class ListWaitingRoomsResponseBodyWaitingRoomsHostNameAndPath(TeaModel):
    def __init__(
        self,
        domain: str = None,
        path: str = None,
        subdomain: str = None,
    ):
        self.domain = domain
        self.path = path
        self.subdomain = subdomain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.path is not None:
            result['Path'] = self.path
        if self.subdomain is not None:
            result['Subdomain'] = self.subdomain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Subdomain') is not None:
            self.subdomain = m.get('Subdomain')
        return self


class ListWaitingRoomsResponseBodyWaitingRooms(TeaModel):
    def __init__(
        self,
        cookie_name: str = None,
        custom_page_html: str = None,
        description: str = None,
        disable_session_renewal_enable: str = None,
        enable: str = None,
        host_name_and_path: List[ListWaitingRoomsResponseBodyWaitingRoomsHostNameAndPath] = None,
        json_response_enable: str = None,
        language: str = None,
        name: str = None,
        new_users_per_minute: str = None,
        queue_all_enable: str = None,
        queuing_method: str = None,
        queuing_status_code: str = None,
        session_duration: str = None,
        total_active_users: str = None,
        waiting_room_id: str = None,
        waiting_room_type: str = None,
    ):
        self.cookie_name = cookie_name
        self.custom_page_html = custom_page_html
        self.description = description
        self.disable_session_renewal_enable = disable_session_renewal_enable
        self.enable = enable
        self.host_name_and_path = host_name_and_path
        self.json_response_enable = json_response_enable
        self.language = language
        self.name = name
        self.new_users_per_minute = new_users_per_minute
        self.queue_all_enable = queue_all_enable
        self.queuing_method = queuing_method
        self.queuing_status_code = queuing_status_code
        self.session_duration = session_duration
        self.total_active_users = total_active_users
        self.waiting_room_id = waiting_room_id
        self.waiting_room_type = waiting_room_type

    def validate(self):
        if self.host_name_and_path:
            for k in self.host_name_and_path:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_name is not None:
            result['CookieName'] = self.cookie_name
        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_session_renewal_enable is not None:
            result['DisableSessionRenewalEnable'] = self.disable_session_renewal_enable
        if self.enable is not None:
            result['Enable'] = self.enable
        result['HostNameAndPath'] = []
        if self.host_name_and_path is not None:
            for k in self.host_name_and_path:
                result['HostNameAndPath'].append(k.to_map() if k else None)
        if self.json_response_enable is not None:
            result['JsonResponseEnable'] = self.json_response_enable
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.new_users_per_minute is not None:
            result['NewUsersPerMinute'] = self.new_users_per_minute
        if self.queue_all_enable is not None:
            result['QueueAllEnable'] = self.queue_all_enable
        if self.queuing_method is not None:
            result['QueuingMethod'] = self.queuing_method
        if self.queuing_status_code is not None:
            result['QueuingStatusCode'] = self.queuing_status_code
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users
        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id
        if self.waiting_room_type is not None:
            result['WaitingRoomType'] = self.waiting_room_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieName') is not None:
            self.cookie_name = m.get('CookieName')
        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableSessionRenewalEnable') is not None:
            self.disable_session_renewal_enable = m.get('DisableSessionRenewalEnable')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        self.host_name_and_path = []
        if m.get('HostNameAndPath') is not None:
            for k in m.get('HostNameAndPath'):
                temp_model = ListWaitingRoomsResponseBodyWaitingRoomsHostNameAndPath()
                self.host_name_and_path.append(temp_model.from_map(k))
        if m.get('JsonResponseEnable') is not None:
            self.json_response_enable = m.get('JsonResponseEnable')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewUsersPerMinute') is not None:
            self.new_users_per_minute = m.get('NewUsersPerMinute')
        if m.get('QueueAllEnable') is not None:
            self.queue_all_enable = m.get('QueueAllEnable')
        if m.get('QueuingMethod') is not None:
            self.queuing_method = m.get('QueuingMethod')
        if m.get('QueuingStatusCode') is not None:
            self.queuing_status_code = m.get('QueuingStatusCode')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')
        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')
        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')
        return self


class ListWaitingRoomsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        waiting_rooms: List[ListWaitingRoomsResponseBodyWaitingRooms] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.waiting_rooms = waiting_rooms

    def validate(self):
        if self.waiting_rooms:
            for k in self.waiting_rooms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WaitingRooms'] = []
        if self.waiting_rooms is not None:
            for k in self.waiting_rooms:
                result['WaitingRooms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.waiting_rooms = []
        if m.get('WaitingRooms') is not None:
            for k in m.get('WaitingRooms'):
                temp_model = ListWaitingRoomsResponseBodyWaitingRooms()
                self.waiting_rooms.append(temp_model.from_map(k))
        return self


class ListWaitingRoomsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWaitingRoomsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWaitingRoomsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreloadCachesRequest(TeaModel):
    def __init__(
        self,
        content: List[str] = None,
        headers: Dict[str, str] = None,
        site_id: int = None,
    ):
        self.content = content
        self.headers = headers
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class PreloadCachesShrinkRequest(TeaModel):
    def __init__(
        self,
        content_shrink: str = None,
        headers_shrink: str = None,
        site_id: int = None,
    ):
        self.content_shrink = content_shrink
        self.headers_shrink = headers_shrink
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink
        if self.headers_shrink is not None:
            result['Headers'] = self.headers_shrink
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')
        if m.get('Headers') is not None:
            self.headers_shrink = m.get('Headers')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class PreloadCachesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class PreloadCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PreloadCachesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PreloadCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRoutineCodeVersionRequest(TeaModel):
    def __init__(
        self,
        canary_area_list: List[str] = None,
        canary_code_version: str = None,
        code_version: str = None,
        env: str = None,
        name: str = None,
    ):
        self.canary_area_list = canary_area_list
        self.canary_code_version = canary_code_version
        self.code_version = code_version
        self.env = env
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.canary_area_list is not None:
            result['CanaryAreaList'] = self.canary_area_list
        if self.canary_code_version is not None:
            result['CanaryCodeVersion'] = self.canary_code_version
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version
        if self.env is not None:
            result['Env'] = self.env
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanaryAreaList') is not None:
            self.canary_area_list = m.get('CanaryAreaList')
        if m.get('CanaryCodeVersion') is not None:
            self.canary_code_version = m.get('CanaryCodeVersion')
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class PublishRoutineCodeVersionShrinkRequest(TeaModel):
    def __init__(
        self,
        canary_area_list_shrink: str = None,
        canary_code_version: str = None,
        code_version: str = None,
        env: str = None,
        name: str = None,
    ):
        self.canary_area_list_shrink = canary_area_list_shrink
        self.canary_code_version = canary_code_version
        self.code_version = code_version
        self.env = env
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.canary_area_list_shrink is not None:
            result['CanaryAreaList'] = self.canary_area_list_shrink
        if self.canary_code_version is not None:
            result['CanaryCodeVersion'] = self.canary_code_version
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version
        if self.env is not None:
            result['Env'] = self.env
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanaryAreaList') is not None:
            self.canary_area_list_shrink = m.get('CanaryAreaList')
        if m.get('CanaryCodeVersion') is not None:
            self.canary_code_version = m.get('CanaryCodeVersion')
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class PublishRoutineCodeVersionResponseBody(TeaModel):
    def __init__(
        self,
        code_version: str = None,
        request_id: str = None,
    ):
        self.code_version = code_version
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishRoutineCodeVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishRoutineCodeVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishRoutineCodeVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurgeCachesRequestContent(TeaModel):
    def __init__(
        self,
        cache_tags: List[str] = None,
        directories: List[str] = None,
        files: List[Any] = None,
        hostnames: List[str] = None,
        ignore_params: List[str] = None,
        purge_all: bool = None,
    ):
        self.cache_tags = cache_tags
        self.directories = directories
        self.files = files
        self.hostnames = hostnames
        self.ignore_params = ignore_params
        self.purge_all = purge_all

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_tags is not None:
            result['CacheTags'] = self.cache_tags
        if self.directories is not None:
            result['Directories'] = self.directories
        if self.files is not None:
            result['Files'] = self.files
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.ignore_params is not None:
            result['IgnoreParams'] = self.ignore_params
        if self.purge_all is not None:
            result['PurgeAll'] = self.purge_all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheTags') is not None:
            self.cache_tags = m.get('CacheTags')
        if m.get('Directories') is not None:
            self.directories = m.get('Directories')
        if m.get('Files') is not None:
            self.files = m.get('Files')
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        if m.get('IgnoreParams') is not None:
            self.ignore_params = m.get('IgnoreParams')
        if m.get('PurgeAll') is not None:
            self.purge_all = m.get('PurgeAll')
        return self


class PurgeCachesRequest(TeaModel):
    def __init__(
        self,
        content: PurgeCachesRequestContent = None,
        edge_compute_purge: bool = None,
        force: bool = None,
        site_id: int = None,
        type: str = None,
    ):
        self.content = content
        self.edge_compute_purge = edge_compute_purge
        self.force = force
        self.site_id = site_id
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.edge_compute_purge is not None:
            result['EdgeComputePurge'] = self.edge_compute_purge
        if self.force is not None:
            result['Force'] = self.force
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = PurgeCachesRequestContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('EdgeComputePurge') is not None:
            self.edge_compute_purge = m.get('EdgeComputePurge')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PurgeCachesShrinkRequest(TeaModel):
    def __init__(
        self,
        content_shrink: str = None,
        edge_compute_purge: bool = None,
        force: bool = None,
        site_id: int = None,
        type: str = None,
    ):
        self.content_shrink = content_shrink
        self.edge_compute_purge = edge_compute_purge
        self.force = force
        self.site_id = site_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink
        if self.edge_compute_purge is not None:
            result['EdgeComputePurge'] = self.edge_compute_purge
        if self.force is not None:
            result['Force'] = self.force
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')
        if m.get('EdgeComputePurge') is not None:
            self.edge_compute_purge = m.get('EdgeComputePurge')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PurgeCachesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class PurgeCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PurgeCachesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PurgeCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutKvRequest(TeaModel):
    def __init__(
        self,
        base_64: bool = None,
        expiration: int = None,
        expiration_ttl: int = None,
        key: str = None,
        namespace: str = None,
        value: str = None,
    ):
        self.base_64 = base_64
        self.expiration = expiration
        self.expiration_ttl = expiration_ttl
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_64 is not None:
            result['Base64'] = self.base_64
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.expiration_ttl is not None:
            result['ExpirationTtl'] = self.expiration_ttl
        if self.key is not None:
            result['Key'] = self.key
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base64') is not None:
            self.base_64 = m.get('Base64')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('ExpirationTtl') is not None:
            self.expiration_ttl = m.get('ExpirationTtl')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PutKvResponseBody(TeaModel):
    def __init__(
        self,
        length: str = None,
        request_id: str = None,
        value: str = None,
    ):
        self.length = length
        # Id of the request
        self.request_id = request_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.length is not None:
            result['Length'] = self.length
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PutKvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutKvResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutKvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutKvWithHighCapacityRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        namespace: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PutKvWithHighCapacityAdvanceRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        namespace: str = None,
        url_object: BinaryIO = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class PutKvWithHighCapacityResponseBody(TeaModel):
    def __init__(
        self,
        length: str = None,
        request_id: str = None,
        value: str = None,
    ):
        self.length = length
        # Id of the request
        self.request_id = request_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.length is not None:
            result['Length'] = self.length
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PutKvWithHighCapacityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutKvWithHighCapacityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutKvWithHighCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetScheduledPreloadJobRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ResetScheduledPreloadJobResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        created_at: str = None,
        domains: str = None,
        error_info: str = None,
        failed_file_oss: str = None,
        file_id: str = None,
        id: str = None,
        insert_way: str = None,
        name: str = None,
        request_id: str = None,
        site_id: int = None,
        task_submitted: int = None,
        task_type: str = None,
        url_count: int = None,
        url_submitted: int = None,
    ):
        self.ali_uid = ali_uid
        self.created_at = created_at
        self.domains = domains
        self.error_info = error_info
        self.failed_file_oss = failed_file_oss
        self.file_id = file_id
        self.id = id
        self.insert_way = insert_way
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id
        self.task_submitted = task_submitted
        self.task_type = task_type
        self.url_count = url_count
        self.url_submitted = url_submitted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.failed_file_oss is not None:
            result['FailedFileOss'] = self.failed_file_oss
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id is not None:
            result['Id'] = self.id
        if self.insert_way is not None:
            result['InsertWay'] = self.insert_way
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.task_submitted is not None:
            result['TaskSubmitted'] = self.task_submitted
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.url_count is not None:
            result['UrlCount'] = self.url_count
        if self.url_submitted is not None:
            result['UrlSubmitted'] = self.url_submitted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('FailedFileOss') is not None:
            self.failed_file_oss = m.get('FailedFileOss')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsertWay') is not None:
            self.insert_way = m.get('InsertWay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaskSubmitted') is not None:
            self.task_submitted = m.get('TaskSubmitted')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UrlCount') is not None:
            self.url_count = m.get('UrlCount')
        if m.get('UrlSubmitted') is not None:
            self.url_submitted = m.get('UrlSubmitted')
        return self


class ResetScheduledPreloadJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetScheduledPreloadJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetScheduledPreloadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCertificateRequest(TeaModel):
    def __init__(
        self,
        cas_id: int = None,
        certificate: str = None,
        id: str = None,
        name: str = None,
        owner_id: int = None,
        private_key: str = None,
        region: str = None,
        security_token: str = None,
        site_id: int = None,
        type: str = None,
        update: bool = None,
    ):
        self.cas_id = cas_id
        self.certificate = certificate
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.private_key = private_key
        self.region = region
        self.security_token = security_token
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.type = type
        self.update = update

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cas_id is not None:
            result['CasId'] = self.cas_id
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.region is not None:
            result['Region'] = self.region
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.type is not None:
            result['Type'] = self.type
        if self.update is not None:
            result['Update'] = self.update
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasId') is not None:
            self.cas_id = m.get('CasId')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Update') is not None:
            self.update = m.get('Update')
        return self


class SetCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetHttpDDoSAttackIntelligentProtectionRequest(TeaModel):
    def __init__(
        self,
        ai_mode: str = None,
        ai_template: str = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.ai_mode = ai_mode
        # This parameter is required.
        self.ai_template = ai_template
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_mode is not None:
            result['AiMode'] = self.ai_mode
        if self.ai_template is not None:
            result['AiTemplate'] = self.ai_template
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiMode') is not None:
            self.ai_mode = m.get('AiMode')
        if m.get('AiTemplate') is not None:
            self.ai_template = m.get('AiTemplate')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class SetHttpDDoSAttackIntelligentProtectionResponseBody(TeaModel):
    def __init__(
        self,
        ai_mode: str = None,
        ai_template: str = None,
        request_id: str = None,
        site_id: int = None,
    ):
        self.ai_mode = ai_mode
        self.ai_template = ai_template
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_mode is not None:
            result['AiMode'] = self.ai_mode
        if self.ai_template is not None:
            result['AiTemplate'] = self.ai_template
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiMode') is not None:
            self.ai_mode = m.get('AiMode')
        if m.get('AiTemplate') is not None:
            self.ai_template = m.get('AiTemplate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class SetHttpDDoSAttackIntelligentProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetHttpDDoSAttackIntelligentProtectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetHttpDDoSAttackIntelligentProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetHttpDDoSAttackProtectionRequest(TeaModel):
    def __init__(
        self,
        global_mode: str = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.global_mode = global_mode
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_mode is not None:
            result['GlobalMode'] = self.global_mode
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalMode') is not None:
            self.global_mode = m.get('GlobalMode')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class SetHttpDDoSAttackProtectionResponseBody(TeaModel):
    def __init__(
        self,
        global_mode: str = None,
        request_id: str = None,
        site_id: int = None,
    ):
        self.global_mode = global_mode
        # Id of the request
        self.request_id = request_id
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_mode is not None:
            result['GlobalMode'] = self.global_mode
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalMode') is not None:
            self.global_mode = m.get('GlobalMode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class SetHttpDDoSAttackProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetHttpDDoSAttackProtectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetHttpDDoSAttackProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartScheduledPreloadExecutionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StartScheduledPreloadExecutionResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        end_time: str = None,
        id: str = None,
        interval: int = None,
        job_id: str = None,
        request_id: str = None,
        slice_len: int = None,
        start_time: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.end_time = end_time
        self.id = id
        self.interval = interval
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id
        self.slice_len = slice_len
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class StartScheduledPreloadExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartScheduledPreloadExecutionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartScheduledPreloadExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopScheduledPreloadExecutionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StopScheduledPreloadExecutionResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        end_time: str = None,
        id: str = None,
        interval: int = None,
        job_id: str = None,
        request_id: str = None,
        slice_len: int = None,
        start_time: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.end_time = end_time
        self.id = id
        self.interval = interval
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id
        self.slice_len = slice_len
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class StopScheduledPreloadExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopScheduledPreloadExecutionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopScheduledPreloadExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransformExpressionToMatchRequest(TeaModel):
    def __init__(
        self,
        expression: str = None,
        phase: str = None,
        site_id: int = None,
    ):
        self.expression = expression
        self.phase = phase
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class TransformExpressionToMatchResponseBody(TeaModel):
    def __init__(
        self,
        match: WafRuleMatch = None,
        request_id: str = None,
    ):
        self.match = match
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['Match'] = self.match.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Match') is not None:
            temp_model = WafRuleMatch()
            self.match = temp_model.from_map(m['Match'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TransformExpressionToMatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransformExpressionToMatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TransformExpressionToMatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransformMatchToExpressionRequest(TeaModel):
    def __init__(
        self,
        match: WafRuleMatch = None,
        phase: str = None,
        site_id: int = None,
    ):
        self.match = match
        self.phase = phase
        self.site_id = site_id

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['Match'] = self.match.to_map()
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Match') is not None:
            temp_model = WafRuleMatch()
            self.match = temp_model.from_map(m['Match'])
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class TransformMatchToExpressionShrinkRequest(TeaModel):
    def __init__(
        self,
        match_shrink: str = None,
        phase: str = None,
        site_id: int = None,
    ):
        self.match_shrink = match_shrink
        self.phase = phase
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_shrink is not None:
            result['Match'] = self.match_shrink
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Match') is not None:
            self.match_shrink = m.get('Match')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class TransformMatchToExpressionResponseBody(TeaModel):
    def __init__(
        self,
        expression: str = None,
        request_id: str = None,
    ):
        self.expression = expression
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TransformMatchToExpressionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransformMatchToExpressionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TransformMatchToExpressionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        security_token: str = None,
        tag_key: List[str] = None,
    ):
        # 是否全部删除，只针对TagKey.N为空时有效
        self.all = all
        self.owner_id = owner_id
        # 要创建并绑定标签的资源所在的地域ID。
        # 
        # This parameter is required.
        self.region_id = region_id
        # 资源ID,最多 50个子项
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.security_token = security_token
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomScenePolicyRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        objects: str = None,
        policy_id: int = None,
        start_time: str = None,
        template: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.name = name
        self.objects = objects
        # This parameter is required.
        self.policy_id = policy_id
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.name is not None:
            result['Name'] = self.name
        if self.objects is not None:
            result['Objects'] = self.objects
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class UpdateCustomScenePolicyResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        objects: List[str] = None,
        policy_id: int = None,
        request_id: str = None,
        start_time: str = None,
        template: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.objects = objects
        self.policy_id = policy_id
        # Id of the request
        self.request_id = request_id
        self.start_time = start_time
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.name is not None:
            result['Name'] = self.name
        if self.objects is not None:
            result['Objects'] = self.objects
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class UpdateCustomScenePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomScenePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCustomScenePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKvNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateKvNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        namespace: str = None,
        namespace_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.description = description
        self.namespace = namespace
        self.namespace_id = namespace_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateKvNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateKvNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateKvNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateListRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        items: List[str] = None,
        name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.id = id
        self.items = items
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.items is not None:
            result['Items'] = self.items
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateListShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        items_shrink: str = None,
        name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.id = id
        self.items_shrink = items_shrink
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.items_shrink is not None:
            result['Items'] = self.items_shrink
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Items') is not None:
            self.items_shrink = m.get('Items')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePageRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.content_type = content_type
        self.description = description
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdatePageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordRequestAuthConf(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        self.access_key = access_key
        self.auth_type = auth_type
        self.region = region
        self.secret_key = secret_key
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.region is not None:
            result['Region'] = self.region
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateRecordRequestData(TeaModel):
    def __init__(
        self,
        algorithm: int = None,
        certificate: str = None,
        fingerprint: str = None,
        flag: int = None,
        key_tag: int = None,
        matching_type: int = None,
        port: int = None,
        priority: int = None,
        selector: int = None,
        tag: str = None,
        type: int = None,
        usage: int = None,
        value: str = None,
        weight: int = None,
    ):
        self.algorithm = algorithm
        self.certificate = certificate
        self.fingerprint = fingerprint
        self.flag = flag
        self.key_tag = key_tag
        self.matching_type = matching_type
        self.port = port
        self.priority = priority
        self.selector = selector
        self.tag = tag
        self.type = type
        self.usage = usage
        self.value = value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.matching_type is not None:
            result['MatchingType'] = self.matching_type
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.selector is not None:
            result['Selector'] = self.selector
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.value is not None:
            result['Value'] = self.value
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('MatchingType') is not None:
            self.matching_type = m.get('MatchingType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Selector') is not None:
            self.selector = m.get('Selector')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateRecordRequest(TeaModel):
    def __init__(
        self,
        auth_conf: UpdateRecordRequestAuthConf = None,
        biz_name: str = None,
        comment: str = None,
        data: UpdateRecordRequestData = None,
        host_policy: str = None,
        proxied: bool = None,
        record_id: int = None,
        source_type: str = None,
        ttl: int = None,
    ):
        self.auth_conf = auth_conf
        self.biz_name = biz_name
        self.comment = comment
        # This parameter is required.
        self.data = data
        self.host_policy = host_policy
        # 是否代理加速
        self.proxied = proxied
        # This parameter is required.
        self.record_id = record_id
        self.source_type = source_type
        self.ttl = ttl

    def validate(self):
        if self.auth_conf:
            self.auth_conf.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_conf is not None:
            result['AuthConf'] = self.auth_conf.to_map()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.host_policy is not None:
            result['HostPolicy'] = self.host_policy
        if self.proxied is not None:
            result['Proxied'] = self.proxied
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConf') is not None:
            temp_model = UpdateRecordRequestAuthConf()
            self.auth_conf = temp_model.from_map(m['AuthConf'])
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Data') is not None:
            temp_model = UpdateRecordRequestData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')
        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class UpdateRecordShrinkRequest(TeaModel):
    def __init__(
        self,
        auth_conf_shrink: str = None,
        biz_name: str = None,
        comment: str = None,
        data_shrink: str = None,
        host_policy: str = None,
        proxied: bool = None,
        record_id: int = None,
        source_type: str = None,
        ttl: int = None,
    ):
        self.auth_conf_shrink = auth_conf_shrink
        self.biz_name = biz_name
        self.comment = comment
        # This parameter is required.
        self.data_shrink = data_shrink
        self.host_policy = host_policy
        # 是否代理加速
        self.proxied = proxied
        # This parameter is required.
        self.record_id = record_id
        self.source_type = source_type
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_conf_shrink is not None:
            result['AuthConf'] = self.auth_conf_shrink
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.data_shrink is not None:
            result['Data'] = self.data_shrink
        if self.host_policy is not None:
            result['HostPolicy'] = self.host_policy
        if self.proxied is not None:
            result['Proxied'] = self.proxied
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConf') is not None:
            self.auth_conf_shrink = m.get('AuthConf')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Data') is not None:
            self.data_shrink = m.get('Data')
        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')
        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class UpdateRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateScheduledPreloadExecutionRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        id: str = None,
        interval: int = None,
        slice_len: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.id = id
        self.interval = interval
        self.slice_len = slice_len
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class UpdateScheduledPreloadExecutionResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        end_time: str = None,
        id: str = None,
        interval: int = None,
        job_id: str = None,
        request_id: str = None,
        slice_len: int = None,
        start_time: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.end_time = end_time
        self.id = id
        self.interval = interval
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id
        self.slice_len = slice_len
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateScheduledPreloadExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateScheduledPreloadExecutionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateScheduledPreloadExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSiteAccessTypeRequest(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.access_type = access_type
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class UpdateSiteAccessTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSiteAccessTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSiteAccessTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSiteAccessTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSiteCoverageRequest(TeaModel):
    def __init__(
        self,
        coverage: str = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.coverage = coverage
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class UpdateSiteCoverageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSiteCoverageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSiteCoverageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSiteCoverageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSiteCustomLogRequest(TeaModel):
    def __init__(
        self,
        cookies: List[str] = None,
        request_headers: List[str] = None,
        response_headers: List[str] = None,
        site_id: int = None,
    ):
        self.cookies = cookies
        self.request_headers = request_headers
        self.response_headers = response_headers
        # site id
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers
        if self.response_headers is not None:
            result['ResponseHeaders'] = self.response_headers
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')
        if m.get('ResponseHeaders') is not None:
            self.response_headers = m.get('ResponseHeaders')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class UpdateSiteCustomLogShrinkRequest(TeaModel):
    def __init__(
        self,
        cookies_shrink: str = None,
        request_headers_shrink: str = None,
        response_headers_shrink: str = None,
        site_id: int = None,
    ):
        self.cookies_shrink = cookies_shrink
        self.request_headers_shrink = request_headers_shrink
        self.response_headers_shrink = response_headers_shrink
        # site id
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookies_shrink is not None:
            result['Cookies'] = self.cookies_shrink
        if self.request_headers_shrink is not None:
            result['RequestHeaders'] = self.request_headers_shrink
        if self.response_headers_shrink is not None:
            result['ResponseHeaders'] = self.response_headers_shrink
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookies') is not None:
            self.cookies_shrink = m.get('Cookies')
        if m.get('RequestHeaders') is not None:
            self.request_headers_shrink = m.get('RequestHeaders')
        if m.get('ResponseHeaders') is not None:
            self.response_headers_shrink = m.get('ResponseHeaders')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class UpdateSiteCustomLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSiteCustomLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSiteCustomLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSiteCustomLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSiteDeliveryTaskRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        discard_rate: float = None,
        field_name: str = None,
        site_id: int = None,
        task_name: str = None,
    ):
        self.business_type = business_type
        self.discard_rate = discard_rate
        # This parameter is required.
        self.field_name = field_name
        self.site_id = site_id
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UpdateSiteDeliveryTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSiteDeliveryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSiteDeliveryTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSiteDeliveryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSiteDeliveryTaskStatusRequest(TeaModel):
    def __init__(
        self,
        method: str = None,
        site_id: int = None,
        task_name: str = None,
    ):
        # This parameter is required.
        self.method = method
        self.site_id = site_id
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['Method'] = self.method
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UpdateSiteDeliveryTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
        task_name: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UpdateSiteDeliveryTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSiteDeliveryTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSiteDeliveryTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSiteVanityNSRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        vanity_nslist: str = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        self.vanity_nslist = vanity_nslist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.vanity_nslist is not None:
            result['VanityNSList'] = self.vanity_nslist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('VanityNSList') is not None:
            self.vanity_nslist = m.get('VanityNSList')
        return self


class UpdateSiteVanityNSResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSiteVanityNSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSiteVanityNSResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSiteVanityNSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserDeliveryTaskRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        discard_rate: float = None,
        field_name: str = None,
        task_name: str = None,
    ):
        self.business_type = business_type
        self.discard_rate = discard_rate
        # This parameter is required.
        self.field_name = field_name
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UpdateUserDeliveryTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUserDeliveryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserDeliveryTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserDeliveryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserDeliveryTaskStatusRequest(TeaModel):
    def __init__(
        self,
        method: str = None,
        task_name: str = None,
    ):
        # This parameter is required.
        self.method = method
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['Method'] = self.method
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UpdateUserDeliveryTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
        task_name: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UpdateUserDeliveryTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserDeliveryTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserDeliveryTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWafRuleRequest(TeaModel):
    def __init__(
        self,
        config: WafRuleConfig = None,
        id: int = None,
        position: int = None,
        site_id: int = None,
        site_version: int = None,
        status: str = None,
    ):
        self.config = config
        # This parameter is required.
        self.id = id
        self.position = position
        # This parameter is required.
        self.site_id = site_id
        self.site_version = site_version
        self.status = status

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.position is not None:
            result['Position'] = self.position
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = WafRuleConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateWafRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        config_shrink: str = None,
        id: int = None,
        position: int = None,
        site_id: int = None,
        site_version: int = None,
        status: str = None,
    ):
        self.config_shrink = config_shrink
        # This parameter is required.
        self.id = id
        self.position = position
        # This parameter is required.
        self.site_id = site_id
        self.site_version = site_version
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
        if self.id is not None:
            result['Id'] = self.id
        if self.position is not None:
            result['Position'] = self.position
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateWafRuleResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWafRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWafRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWafRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWafRulesetRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        site_id: int = None,
        site_version: int = None,
        status: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.site_id = site_id
        self.site_version = site_version
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateWafRulesetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWafRulesetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWafRulesetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWafRulesetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWaitingRoomRequestHostNameAndPath(TeaModel):
    def __init__(
        self,
        domain: str = None,
        path: str = None,
        subdomain: str = None,
    ):
        self.domain = domain
        self.path = path
        self.subdomain = subdomain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.path is not None:
            result['Path'] = self.path
        if self.subdomain is not None:
            result['Subdomain'] = self.subdomain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Subdomain') is not None:
            self.subdomain = m.get('Subdomain')
        return self


class UpdateWaitingRoomRequest(TeaModel):
    def __init__(
        self,
        cookie_name: str = None,
        custom_page_html: str = None,
        description: str = None,
        disable_session_renewal_enable: str = None,
        enable: str = None,
        host_name_and_path: List[UpdateWaitingRoomRequestHostNameAndPath] = None,
        json_response_enable: str = None,
        language: str = None,
        name: str = None,
        new_users_per_minute: str = None,
        queue_all_enable: str = None,
        queuing_method: str = None,
        queuing_status_code: str = None,
        session_duration: str = None,
        site_id: int = None,
        total_active_users: str = None,
        waiting_room_id: str = None,
        waiting_room_type: str = None,
    ):
        self.cookie_name = cookie_name
        self.custom_page_html = custom_page_html
        self.description = description
        self.disable_session_renewal_enable = disable_session_renewal_enable
        self.enable = enable
        self.host_name_and_path = host_name_and_path
        self.json_response_enable = json_response_enable
        self.language = language
        self.name = name
        self.new_users_per_minute = new_users_per_minute
        self.queue_all_enable = queue_all_enable
        self.queuing_method = queuing_method
        self.queuing_status_code = queuing_status_code
        self.session_duration = session_duration
        # This parameter is required.
        self.site_id = site_id
        self.total_active_users = total_active_users
        # This parameter is required.
        self.waiting_room_id = waiting_room_id
        self.waiting_room_type = waiting_room_type

    def validate(self):
        if self.host_name_and_path:
            for k in self.host_name_and_path:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_name is not None:
            result['CookieName'] = self.cookie_name
        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_session_renewal_enable is not None:
            result['DisableSessionRenewalEnable'] = self.disable_session_renewal_enable
        if self.enable is not None:
            result['Enable'] = self.enable
        result['HostNameAndPath'] = []
        if self.host_name_and_path is not None:
            for k in self.host_name_and_path:
                result['HostNameAndPath'].append(k.to_map() if k else None)
        if self.json_response_enable is not None:
            result['JsonResponseEnable'] = self.json_response_enable
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.new_users_per_minute is not None:
            result['NewUsersPerMinute'] = self.new_users_per_minute
        if self.queue_all_enable is not None:
            result['QueueAllEnable'] = self.queue_all_enable
        if self.queuing_method is not None:
            result['QueuingMethod'] = self.queuing_method
        if self.queuing_status_code is not None:
            result['QueuingStatusCode'] = self.queuing_status_code
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users
        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id
        if self.waiting_room_type is not None:
            result['WaitingRoomType'] = self.waiting_room_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieName') is not None:
            self.cookie_name = m.get('CookieName')
        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableSessionRenewalEnable') is not None:
            self.disable_session_renewal_enable = m.get('DisableSessionRenewalEnable')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        self.host_name_and_path = []
        if m.get('HostNameAndPath') is not None:
            for k in m.get('HostNameAndPath'):
                temp_model = UpdateWaitingRoomRequestHostNameAndPath()
                self.host_name_and_path.append(temp_model.from_map(k))
        if m.get('JsonResponseEnable') is not None:
            self.json_response_enable = m.get('JsonResponseEnable')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewUsersPerMinute') is not None:
            self.new_users_per_minute = m.get('NewUsersPerMinute')
        if m.get('QueueAllEnable') is not None:
            self.queue_all_enable = m.get('QueueAllEnable')
        if m.get('QueuingMethod') is not None:
            self.queuing_method = m.get('QueuingMethod')
        if m.get('QueuingStatusCode') is not None:
            self.queuing_status_code = m.get('QueuingStatusCode')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')
        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')
        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')
        return self


class UpdateWaitingRoomShrinkRequest(TeaModel):
    def __init__(
        self,
        cookie_name: str = None,
        custom_page_html: str = None,
        description: str = None,
        disable_session_renewal_enable: str = None,
        enable: str = None,
        host_name_and_path_shrink: str = None,
        json_response_enable: str = None,
        language: str = None,
        name: str = None,
        new_users_per_minute: str = None,
        queue_all_enable: str = None,
        queuing_method: str = None,
        queuing_status_code: str = None,
        session_duration: str = None,
        site_id: int = None,
        total_active_users: str = None,
        waiting_room_id: str = None,
        waiting_room_type: str = None,
    ):
        self.cookie_name = cookie_name
        self.custom_page_html = custom_page_html
        self.description = description
        self.disable_session_renewal_enable = disable_session_renewal_enable
        self.enable = enable
        self.host_name_and_path_shrink = host_name_and_path_shrink
        self.json_response_enable = json_response_enable
        self.language = language
        self.name = name
        self.new_users_per_minute = new_users_per_minute
        self.queue_all_enable = queue_all_enable
        self.queuing_method = queuing_method
        self.queuing_status_code = queuing_status_code
        self.session_duration = session_duration
        # This parameter is required.
        self.site_id = site_id
        self.total_active_users = total_active_users
        # This parameter is required.
        self.waiting_room_id = waiting_room_id
        self.waiting_room_type = waiting_room_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_name is not None:
            result['CookieName'] = self.cookie_name
        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_session_renewal_enable is not None:
            result['DisableSessionRenewalEnable'] = self.disable_session_renewal_enable
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.host_name_and_path_shrink is not None:
            result['HostNameAndPath'] = self.host_name_and_path_shrink
        if self.json_response_enable is not None:
            result['JsonResponseEnable'] = self.json_response_enable
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.new_users_per_minute is not None:
            result['NewUsersPerMinute'] = self.new_users_per_minute
        if self.queue_all_enable is not None:
            result['QueueAllEnable'] = self.queue_all_enable
        if self.queuing_method is not None:
            result['QueuingMethod'] = self.queuing_method
        if self.queuing_status_code is not None:
            result['QueuingStatusCode'] = self.queuing_status_code
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users
        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id
        if self.waiting_room_type is not None:
            result['WaitingRoomType'] = self.waiting_room_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieName') is not None:
            self.cookie_name = m.get('CookieName')
        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableSessionRenewalEnable') is not None:
            self.disable_session_renewal_enable = m.get('DisableSessionRenewalEnable')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('HostNameAndPath') is not None:
            self.host_name_and_path_shrink = m.get('HostNameAndPath')
        if m.get('JsonResponseEnable') is not None:
            self.json_response_enable = m.get('JsonResponseEnable')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewUsersPerMinute') is not None:
            self.new_users_per_minute = m.get('NewUsersPerMinute')
        if m.get('QueueAllEnable') is not None:
            self.queue_all_enable = m.get('QueueAllEnable')
        if m.get('QueuingMethod') is not None:
            self.queuing_method = m.get('QueuingMethod')
        if m.get('QueuingStatusCode') is not None:
            self.queuing_status_code = m.get('QueuingStatusCode')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')
        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')
        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')
        return self


class UpdateWaitingRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWaitingRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWaitingRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWaitingRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWaitingRoomEventRequest(TeaModel):
    def __init__(
        self,
        custom_page_html: str = None,
        description: str = None,
        disable_session_renewal_enable: str = None,
        enable: str = None,
        end_time: str = None,
        json_response_enable: str = None,
        language: str = None,
        name: str = None,
        new_users_per_minute: str = None,
        pre_queue_enable: str = None,
        pre_queue_start_time: str = None,
        queuing_method: str = None,
        queuing_status_code: str = None,
        random_pre_queue_enable: str = None,
        session_duration: str = None,
        site_id: int = None,
        start_time: str = None,
        total_active_users: str = None,
        waiting_room_event_id: int = None,
        waiting_room_type: str = None,
    ):
        self.custom_page_html = custom_page_html
        self.description = description
        self.disable_session_renewal_enable = disable_session_renewal_enable
        self.enable = enable
        self.end_time = end_time
        self.json_response_enable = json_response_enable
        self.language = language
        self.name = name
        self.new_users_per_minute = new_users_per_minute
        self.pre_queue_enable = pre_queue_enable
        self.pre_queue_start_time = pre_queue_start_time
        self.queuing_method = queuing_method
        self.queuing_status_code = queuing_status_code
        self.random_pre_queue_enable = random_pre_queue_enable
        self.session_duration = session_duration
        # This parameter is required.
        self.site_id = site_id
        self.start_time = start_time
        self.total_active_users = total_active_users
        self.waiting_room_event_id = waiting_room_event_id
        self.waiting_room_type = waiting_room_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_session_renewal_enable is not None:
            result['DisableSessionRenewalEnable'] = self.disable_session_renewal_enable
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.json_response_enable is not None:
            result['JsonResponseEnable'] = self.json_response_enable
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.new_users_per_minute is not None:
            result['NewUsersPerMinute'] = self.new_users_per_minute
        if self.pre_queue_enable is not None:
            result['PreQueueEnable'] = self.pre_queue_enable
        if self.pre_queue_start_time is not None:
            result['PreQueueStartTime'] = self.pre_queue_start_time
        if self.queuing_method is not None:
            result['QueuingMethod'] = self.queuing_method
        if self.queuing_status_code is not None:
            result['QueuingStatusCode'] = self.queuing_status_code
        if self.random_pre_queue_enable is not None:
            result['RandomPreQueueEnable'] = self.random_pre_queue_enable
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users
        if self.waiting_room_event_id is not None:
            result['WaitingRoomEventId'] = self.waiting_room_event_id
        if self.waiting_room_type is not None:
            result['WaitingRoomType'] = self.waiting_room_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableSessionRenewalEnable') is not None:
            self.disable_session_renewal_enable = m.get('DisableSessionRenewalEnable')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JsonResponseEnable') is not None:
            self.json_response_enable = m.get('JsonResponseEnable')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewUsersPerMinute') is not None:
            self.new_users_per_minute = m.get('NewUsersPerMinute')
        if m.get('PreQueueEnable') is not None:
            self.pre_queue_enable = m.get('PreQueueEnable')
        if m.get('PreQueueStartTime') is not None:
            self.pre_queue_start_time = m.get('PreQueueStartTime')
        if m.get('QueuingMethod') is not None:
            self.queuing_method = m.get('QueuingMethod')
        if m.get('QueuingStatusCode') is not None:
            self.queuing_status_code = m.get('QueuingStatusCode')
        if m.get('RandomPreQueueEnable') is not None:
            self.random_pre_queue_enable = m.get('RandomPreQueueEnable')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')
        if m.get('WaitingRoomEventId') is not None:
            self.waiting_room_event_id = m.get('WaitingRoomEventId')
        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')
        return self


class UpdateWaitingRoomEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWaitingRoomEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWaitingRoomEventResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWaitingRoomEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWaitingRoomRuleRequest(TeaModel):
    def __init__(
        self,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        site_id: int = None,
        waiting_room_rule_id: int = None,
    ):
        # This parameter is required.
        self.rule = rule
        # This parameter is required.
        self.rule_enable = rule_enable
        # This parameter is required.
        self.rule_name = rule_name
        # This parameter is required.
        self.site_id = site_id
        self.waiting_room_rule_id = waiting_room_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.waiting_room_rule_id is not None:
            result['WaitingRoomRuleId'] = self.waiting_room_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('WaitingRoomRuleId') is not None:
            self.waiting_room_rule_id = m.get('WaitingRoomRuleId')
        return self


class UpdateWaitingRoomRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWaitingRoomRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWaitingRoomRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWaitingRoomRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadFileRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        type: str = None,
        upload_task_name: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.upload_task_name = upload_task_name
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.type is not None:
            result['Type'] = self.type
        if self.upload_task_name is not None:
            result['UploadTaskName'] = self.upload_task_name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UploadTaskName') is not None:
            self.upload_task_name = m.get('UploadTaskName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UploadFileAdvanceRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
        type: str = None,
        upload_task_name: str = None,
        url_object: BinaryIO = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.upload_task_name = upload_task_name
        # This parameter is required.
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.type is not None:
            result['Type'] = self.type
        if self.upload_task_name is not None:
            result['UploadTaskName'] = self.upload_task_name
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UploadTaskName') is not None:
            self.upload_task_name = m.get('UploadTaskName')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class UploadFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        upload_id: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_id is not None:
            result['UploadId'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')
        return self


class UploadFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifySiteRequest(TeaModel):
    def __init__(
        self,
        site_id: int = None,
    ):
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class VerifySiteResponseBody(TeaModel):
    def __init__(
        self,
        passed: bool = None,
        request_id: str = None,
    ):
        self.passed = passed
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifySiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifySiteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifySiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



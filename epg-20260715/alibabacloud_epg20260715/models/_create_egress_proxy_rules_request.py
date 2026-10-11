# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class CreateEgressProxyRulesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        egress_proxy_rule_group_id: str = None,
        egress_proxy_rules: main_models.CreateEgressProxyRulesRequestEgressProxyRules = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > Note If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request is different.
        self.client_token = client_token
        # Specifies whether to perform only a dry run on the request. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the request for potential issues, including missing required parameters, invalid request formats, and service limits, but does not create the rules. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # 
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the egress proxy rule group.
        # 
        # This parameter is required.
        self.egress_proxy_rule_group_id = egress_proxy_rule_group_id
        # The list of egress rules grouped by effective phase (PreDns, PreRequest, or PostResponse).
        # 
        # This parameter is required.
        self.egress_proxy_rules = egress_proxy_rules

    def validate(self):
        if self.egress_proxy_rules:
            self.egress_proxy_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_rule_group_id is not None:
            result['EgressProxyRuleGroupId'] = self.egress_proxy_rule_group_id

        if self.egress_proxy_rules is not None:
            result['EgressProxyRules'] = self.egress_proxy_rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyRuleGroupId') is not None:
            self.egress_proxy_rule_group_id = m.get('EgressProxyRuleGroupId')

        if m.get('EgressProxyRules') is not None:
            temp_model = main_models.CreateEgressProxyRulesRequestEgressProxyRules()
            self.egress_proxy_rules = temp_model.from_map(m.get('EgressProxyRules'))

        return self

class CreateEgressProxyRulesRequestEgressProxyRules(DaraModel):
    def __init__(
        self,
        post_response: List[main_models.CreateEgressProxyRulesRequestEgressProxyRulesPostResponse] = None,
        pre_dns: List[main_models.CreateEgressProxyRulesRequestEgressProxyRulesPreDns] = None,
        pre_request: List[main_models.CreateEgressProxyRulesRequestEgressProxyRulesPreRequest] = None,
    ):
        # The list of rules in the PostResponse phase (after the response is returned).
        self.post_response = post_response
        # The list of rules for the pre-DNS stage (before DNS resolution).
        self.pre_dns = pre_dns
        # The list of rules in the PreRequest stage (before request forwarding).
        self.pre_request = pre_request

    def validate(self):
        if self.post_response:
            for v1 in self.post_response:
                 if v1:
                    v1.validate()
        if self.pre_dns:
            for v1 in self.pre_dns:
                 if v1:
                    v1.validate()
        if self.pre_request:
            for v1 in self.pre_request:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PostResponse'] = []
        if self.post_response is not None:
            for k1 in self.post_response:
                result['PostResponse'].append(k1.to_map() if k1 else None)

        result['PreDns'] = []
        if self.pre_dns is not None:
            for k1 in self.pre_dns:
                result['PreDns'].append(k1.to_map() if k1 else None)

        result['PreRequest'] = []
        if self.pre_request is not None:
            for k1 in self.pre_request:
                result['PreRequest'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.post_response = []
        if m.get('PostResponse') is not None:
            for k1 in m.get('PostResponse'):
                temp_model = main_models.CreateEgressProxyRulesRequestEgressProxyRulesPostResponse()
                self.post_response.append(temp_model.from_map(k1))

        self.pre_dns = []
        if m.get('PreDns') is not None:
            for k1 in m.get('PreDns'):
                temp_model = main_models.CreateEgressProxyRulesRequestEgressProxyRulesPreDns()
                self.pre_dns.append(temp_model.from_map(k1))

        self.pre_request = []
        if m.get('PreRequest') is not None:
            for k1 in m.get('PreRequest'):
                temp_model = main_models.CreateEgressProxyRulesRequestEgressProxyRulesPreRequest()
                self.pre_request.append(temp_model.from_map(k1))

        return self

class CreateEgressProxyRulesRequestEgressProxyRulesPreRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        conditions: List[main_models.CreateEgressProxyRulesRequestEgressProxyRulesPreRequestConditions] = None,
        description: str = None,
        egress_proxy_rule_name: str = None,
        priority: int = None,
    ):
        # The action to perform on the matched traffic after the rule is hit. Valid values:
        # 
        # - **Allow**: allows the traffic that matches the rule.
        # 
        # - **Deny**: denies the traffic that matches the rule.
        # 
        # This parameter is required.
        self.action = action
        # The list of matching conditions for the rule. Each condition consists of a condition key (ConditionKey), an operator (ConditionOperator), and condition values (ConditionValues). The combination of a condition key and an operator must be unique within the same rule.
        # 
        # This parameter is required.
        self.conditions = conditions
        # The description of the egress rule. The description must be 2 to 256 characters in length, and can contain Chinese characters, letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        self.description = description
        # The name of the egress rule. The name must be 2 to 128 characters in length, and must start with a letter or a Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.egress_proxy_rule_name = egress_proxy_rule_name
        # The priority of the egress rule within the phase to which it belongs. Valid values: 1 to 1000. A smaller value indicates a higher priority. Within the same phase of a rule group, the priority of rules must be unique.
        # 
        # This parameter is required.
        self.priority = priority

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_rule_name is not None:
            result['EgressProxyRuleName'] = self.egress_proxy_rule_name

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.CreateEgressProxyRulesRequestEgressProxyRulesPreRequestConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyRuleName') is not None:
            self.egress_proxy_rule_name = m.get('EgressProxyRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class CreateEgressProxyRulesRequestEgressProxyRulesPreRequestConditions(DaraModel):
    def __init__(
        self,
        condition_key: str = None,
        condition_operator: str = None,
        condition_values: List[str] = None,
    ):
        # The key of the matching condition. The value must match the effective phase (Phase) of the rule and be used with an operator (ConditionOperator) of the corresponding category. Valid values:
        # 
        # - **request:SourceIp**: the source IP address of the request. Used with IP address operators. Supported in the PreDns and PreRequest phases.
        # 
        # - **request:DestinationDomain**: the destination domain name of the request. Used with string operators. Supported in the PreDns and PreRequest phases.
        # 
        # - **request:Http:Uri**: the URI of the HTTP request. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:Method**: the HTTP request method. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:UserAgent**: the User-Agent of the HTTP request. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:ContentType**: the Content-Type of the HTTP request. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:Header**: the HTTP request header. Used with string operators. Supported in the PreRequest phase. When you use this key, append the request header name to the key in the format of request:Http:Header/<HeaderName>.
        # 
        # - **request:Protocol**: the request protocol. Used with string operators. Supported in the PreRequest phase.
        # 
        # This parameter is required.
        self.condition_key = condition_key
        # The operator of the matching condition. Must be used with a condition key (ConditionKey). Valid values:
        # 
        # - **StringEquals**: exact string match.
        # 
        # - **StringNotEquals**: string not equal.
        # 
        # - **StringEqualsIgnoreCase**: case-insensitive exact string match.
        # 
        # - **StringNotEqualsIgnoreCase**: case-insensitive string not equal.
        # 
        # - **StringPrefixMatch**: string prefix match.
        # 
        # - **StringPrefixMatchIgnoreCase**: case-insensitive string prefix match.
        # 
        # - **StringPrefixNotMatch**: string prefix not match.
        # 
        # - **StringPrefixNotMatchIgnoreCase**: case-insensitive string prefix not match.
        # 
        # - **StringSuffixMatch**: string suffix match.
        # 
        # - **StringSuffixMatchIgnoreCase**: case-insensitive string suffix match.
        # 
        # - **StringSuffixNotMatch**: string suffix not match.
        # 
        # - **StringSuffixNotMatchIgnoreCase**: case-insensitive string suffix not match.
        # 
        # - **StringRegexMatch**: string regular expression match.
        # 
        # - **StringRegexNotMatch**: string regular expression not match.
        # 
        # - **StringWildcardMatch**: string wildcard match.
        # 
        # - **StringWildcardMatchIgnoreCase**: case-insensitive string wildcard match.
        # 
        # - **StringWildcardNotMatch**: string wildcard not match.
        # 
        # - **StringWildcardNotMatchIgnoreCase**: case-insensitive string wildcard not match.
        # 
        # - **IpAddress**: the source IP address belongs to the specified IP address or CIDR block.
        # 
        # - **NotIpAddress**: the source IP address does not belong to the specified IP address or CIDR block.
        # 
        # This parameter is required.
        self.condition_operator = condition_operator
        # The list of condition values.
        # 
        # This parameter is required.
        self.condition_values = condition_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_key is not None:
            result['ConditionKey'] = self.condition_key

        if self.condition_operator is not None:
            result['ConditionOperator'] = self.condition_operator

        if self.condition_values is not None:
            result['ConditionValues'] = self.condition_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionKey') is not None:
            self.condition_key = m.get('ConditionKey')

        if m.get('ConditionOperator') is not None:
            self.condition_operator = m.get('ConditionOperator')

        if m.get('ConditionValues') is not None:
            self.condition_values = m.get('ConditionValues')

        return self

class CreateEgressProxyRulesRequestEgressProxyRulesPreDns(DaraModel):
    def __init__(
        self,
        action: str = None,
        conditions: List[main_models.CreateEgressProxyRulesRequestEgressProxyRulesPreDnsConditions] = None,
        description: str = None,
        egress_proxy_rule_name: str = None,
        priority: int = None,
    ):
        # The action to perform on the matched traffic after the rule is hit. Valid values:
        # 
        # - **Allow**: allows the traffic that matches the rule.
        # 
        # - **Deny**: denies the traffic that matches the rule.
        # 
        # This parameter is required.
        self.action = action
        # The list of matching conditions for the rule. Each condition consists of a condition key (ConditionKey), an operator (ConditionOperator), and condition values (ConditionValues). The combination of a condition key and an operator must be unique within the same rule.
        # 
        # This parameter is required.
        self.conditions = conditions
        # The description of the egress rule. The description must be 2 to 256 characters in length and can contain Chinese characters, letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        self.description = description
        # The name of the egress rule. The name must be 2 to 128 characters in length, and must start with a letter or a Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.egress_proxy_rule_name = egress_proxy_rule_name
        # The priority of the egress rule within the phase to which it belongs. Valid values: 1 to 1000. A smaller value indicates a higher priority. Within the same phase of a rule group, the priority of rules must be unique.
        # 
        # This parameter is required.
        self.priority = priority

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_rule_name is not None:
            result['EgressProxyRuleName'] = self.egress_proxy_rule_name

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.CreateEgressProxyRulesRequestEgressProxyRulesPreDnsConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyRuleName') is not None:
            self.egress_proxy_rule_name = m.get('EgressProxyRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class CreateEgressProxyRulesRequestEgressProxyRulesPreDnsConditions(DaraModel):
    def __init__(
        self,
        condition_key: str = None,
        condition_operator: str = None,
        condition_values: List[str] = None,
    ):
        # The key of the matching condition. The value must match the effective phase (Phase) of the rule and be used with an operator (ConditionOperator) of the corresponding category. Valid values:
        # 
        # - **request:SourceIp**: the source IP address of the request. Used with IP address operators. Supported in the PreDns and PreRequest phases.
        # 
        # - **request:DestinationDomain**: the destination domain name of the request. Used with string operators. Supported in the PreDns and PreRequest phases.
        # 
        # - **request:Http:Uri**: the URI of the HTTP request. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:Method**: the HTTP request method. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:UserAgent**: the User-Agent of the HTTP request. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:ContentType**: the Content-Type of the HTTP request. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:Header**: the HTTP request header. Used with string operators. Supported in the PreRequest phase. When you use this key, append the request header name to the key in the format of request:Http:Header/<HeaderName>.
        # 
        # - **request:Protocol**: the request protocol. Used with string operators. Supported in the PreRequest phase.
        # 
        # This parameter is required.
        self.condition_key = condition_key
        # The operator of the matching condition. Must be used with a condition key (ConditionKey). Valid values:
        # 
        # - **StringEquals**: exact string match.
        # 
        # - **StringNotEquals**: string not equal.
        # 
        # - **StringEqualsIgnoreCase**: case-insensitive exact string match.
        # 
        # - **StringNotEqualsIgnoreCase**: case-insensitive string not equal.
        # 
        # - **StringPrefixMatch**: string prefix match.
        # 
        # - **StringPrefixMatchIgnoreCase**: case-insensitive string prefix match.
        # 
        # - **StringPrefixNotMatch**: string prefix not match.
        # 
        # - **StringPrefixNotMatchIgnoreCase**: case-insensitive string prefix not match.
        # 
        # - **StringSuffixMatch**: string suffix match.
        # 
        # - **StringSuffixMatchIgnoreCase**: case-insensitive string suffix match.
        # 
        # - **StringSuffixNotMatch**: string suffix not match.
        # 
        # - **StringSuffixNotMatchIgnoreCase**: case-insensitive string suffix not match.
        # 
        # - **StringRegexMatch**: string regular expression match.
        # 
        # - **StringRegexNotMatch**: string regular expression not match.
        # 
        # - **StringWildcardMatch**: string wildcard match.
        # 
        # - **StringWildcardMatchIgnoreCase**: case-insensitive string wildcard match.
        # 
        # - **StringWildcardNotMatch**: string wildcard not match.
        # 
        # - **StringWildcardNotMatchIgnoreCase**: case-insensitive string wildcard not match.
        # 
        # - **IpAddress**: the source IP address belongs to the specified IP address or CIDR block.
        # 
        # - **NotIpAddress**: the source IP address does not belong to the specified IP address or CIDR block.
        # 
        # This parameter is required.
        self.condition_operator = condition_operator
        # The list of condition values.
        # 
        # This parameter is required.
        self.condition_values = condition_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_key is not None:
            result['ConditionKey'] = self.condition_key

        if self.condition_operator is not None:
            result['ConditionOperator'] = self.condition_operator

        if self.condition_values is not None:
            result['ConditionValues'] = self.condition_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionKey') is not None:
            self.condition_key = m.get('ConditionKey')

        if m.get('ConditionOperator') is not None:
            self.condition_operator = m.get('ConditionOperator')

        if m.get('ConditionValues') is not None:
            self.condition_values = m.get('ConditionValues')

        return self

class CreateEgressProxyRulesRequestEgressProxyRulesPostResponse(DaraModel):
    def __init__(
        self,
        action: str = None,
        conditions: List[main_models.CreateEgressProxyRulesRequestEgressProxyRulesPostResponseConditions] = None,
        description: str = None,
        egress_proxy_rule_name: str = None,
        priority: int = None,
    ):
        # The action to perform on the matched traffic after the rule is hit. Valid values:
        # 
        # - **Allow**: allows the traffic that matches the rule.
        # 
        # - **Deny**: denies the traffic that matches the rule.
        # 
        # This parameter is required.
        self.action = action
        # The list of matching conditions for the rule. Each condition consists of a condition key (ConditionKey), an operator (ConditionOperator), and condition values (ConditionValues). The combination of a condition key and an operator must be unique within the same rule.
        # 
        # This parameter is required.
        self.conditions = conditions
        # The description of the egress rule. The description must be 2 to 256 characters in length, and can contain Chinese characters, letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        self.description = description
        # The name of the egress rule. The name must be 2 to 128 characters in length, and must start with a letter or a Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.egress_proxy_rule_name = egress_proxy_rule_name
        # The priority of the egress rule within the phase to which it belongs. Valid values: 1 to 1000. A smaller value indicates a higher priority. Within the same phase of a rule group, the priority of rules must be unique.
        # 
        # This parameter is required.
        self.priority = priority

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_rule_name is not None:
            result['EgressProxyRuleName'] = self.egress_proxy_rule_name

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.CreateEgressProxyRulesRequestEgressProxyRulesPostResponseConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyRuleName') is not None:
            self.egress_proxy_rule_name = m.get('EgressProxyRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class CreateEgressProxyRulesRequestEgressProxyRulesPostResponseConditions(DaraModel):
    def __init__(
        self,
        condition_key: str = None,
        condition_operator: str = None,
        condition_values: List[str] = None,
    ):
        # The key of the matching condition. The value must match the effective phase (Phase) of the rule and be used with an operator (ConditionOperator) of the corresponding category. Valid values:
        # 
        # - **request:SourceIp**: the source IP address of the request. Used with IP address operators. Supported in the PreDns and PreRequest phases.
        # 
        # - **request:DestinationDomain**: the destination domain name of the request. Used with string operators. Supported in the PreDns and PreRequest phases.
        # 
        # - **request:Http:Uri**: the URI of the HTTP request. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:Method**: the HTTP request method. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:UserAgent**: the User-Agent of the HTTP request. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:ContentType**: the Content-Type of the HTTP request. Used with string operators. Supported in the PreRequest phase.
        # 
        # - **request:Http:Header**: the HTTP request header. Used with string operators. Supported in the PreRequest phase. When you use this key, append the request header name to the key in the format of request:Http:Header/<HeaderName>.
        # 
        # - **request:Protocol**: the request protocol. Used with string operators. Supported in the PreRequest phase.
        # 
        # This parameter is required.
        self.condition_key = condition_key
        # The operator of the matching condition. Must be used with a condition key (ConditionKey). Valid values:
        # 
        # - **StringEquals**: exact string match.
        # 
        # - **StringNotEquals**: string not equal.
        # 
        # - **StringEqualsIgnoreCase**: case-insensitive exact string match.
        # 
        # - **StringNotEqualsIgnoreCase**: case-insensitive string not equal.
        # 
        # - **StringPrefixMatch**: string prefix match.
        # 
        # - **StringPrefixMatchIgnoreCase**: case-insensitive string prefix match.
        # 
        # - **StringPrefixNotMatch**: string prefix not match.
        # 
        # - **StringPrefixNotMatchIgnoreCase**: case-insensitive string prefix not match.
        # 
        # - **StringSuffixMatch**: string suffix match.
        # 
        # - **StringSuffixMatchIgnoreCase**: case-insensitive string suffix match.
        # 
        # - **StringSuffixNotMatch**: string suffix not match.
        # 
        # - **StringSuffixNotMatchIgnoreCase**: case-insensitive string suffix not match.
        # 
        # - **StringRegexMatch**: string regular expression match.
        # 
        # - **StringRegexNotMatch**: string regular expression not match.
        # 
        # - **StringWildcardMatch**: string wildcard match.
        # 
        # - **StringWildcardMatchIgnoreCase**: case-insensitive string wildcard match.
        # 
        # - **StringWildcardNotMatch**: string wildcard not match.
        # 
        # - **StringWildcardNotMatchIgnoreCase**: case-insensitive string wildcard not match.
        # 
        # - **IpAddress**: the source IP address belongs to the specified IP address or CIDR block.
        # 
        # - **NotIpAddress**: the source IP address does not belong to the specified IP address or CIDR block.
        # 
        # This parameter is required.
        self.condition_operator = condition_operator
        # The list of condition values.
        # 
        # This parameter is required.
        self.condition_values = condition_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_key is not None:
            result['ConditionKey'] = self.condition_key

        if self.condition_operator is not None:
            result['ConditionOperator'] = self.condition_operator

        if self.condition_values is not None:
            result['ConditionValues'] = self.condition_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionKey') is not None:
            self.condition_key = m.get('ConditionKey')

        if m.get('ConditionOperator') is not None:
            self.condition_operator = m.get('ConditionOperator')

        if m.get('ConditionValues') is not None:
            self.condition_values = m.get('ConditionValues')

        return self


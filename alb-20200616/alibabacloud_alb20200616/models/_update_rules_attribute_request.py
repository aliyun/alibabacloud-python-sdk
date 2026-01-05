# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class UpdateRulesAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        rules: List[main_models.UpdateRulesAttributeRequestRules] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a `2xx HTTP` status code is returned and the operation is performed.
        self.dry_run = dry_run
        # This parameter is required.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.UpdateRulesAttributeRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class UpdateRulesAttributeRequestRules(DaraModel):
    def __init__(
        self,
        priority: int = None,
        rule_actions: List[main_models.UpdateRulesAttributeRequestRulesRuleActions] = None,
        rule_conditions: List[main_models.UpdateRulesAttributeRequestRulesRuleConditions] = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        self.priority = priority
        self.rule_actions = rule_actions
        self.rule_conditions = rule_conditions
        # This parameter is required.
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        if self.rule_actions:
            for v1 in self.rule_actions:
                 if v1:
                    v1.validate()
        if self.rule_conditions:
            for v1 in self.rule_conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.priority is not None:
            result['Priority'] = self.priority

        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k1 in self.rule_actions:
                result['RuleActions'].append(k1.to_map() if k1 else None)

        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k1 in self.rule_conditions:
                result['RuleConditions'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k1 in m.get('RuleActions'):
                temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class UpdateRulesAttributeRequestRulesRuleConditions(DaraModel):
    def __init__(
        self,
        cookie_config: main_models.UpdateRulesAttributeRequestRulesRuleConditionsCookieConfig = None,
        header_config: main_models.UpdateRulesAttributeRequestRulesRuleConditionsHeaderConfig = None,
        host_config: main_models.UpdateRulesAttributeRequestRulesRuleConditionsHostConfig = None,
        method_config: main_models.UpdateRulesAttributeRequestRulesRuleConditionsMethodConfig = None,
        path_config: main_models.UpdateRulesAttributeRequestRulesRuleConditionsPathConfig = None,
        query_string_config: main_models.UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfig = None,
        response_header_config: main_models.UpdateRulesAttributeRequestRulesRuleConditionsResponseHeaderConfig = None,
        response_status_code_config: main_models.UpdateRulesAttributeRequestRulesRuleConditionsResponseStatusCodeConfig = None,
        source_ip_config: main_models.UpdateRulesAttributeRequestRulesRuleConditionsSourceIpConfig = None,
        type: str = None,
    ):
        self.cookie_config = cookie_config
        self.header_config = header_config
        self.host_config = host_config
        self.method_config = method_config
        self.path_config = path_config
        self.query_string_config = query_string_config
        self.response_header_config = response_header_config
        self.response_status_code_config = response_status_code_config
        self.source_ip_config = source_ip_config
        self.type = type

    def validate(self):
        if self.cookie_config:
            self.cookie_config.validate()
        if self.header_config:
            self.header_config.validate()
        if self.host_config:
            self.host_config.validate()
        if self.method_config:
            self.method_config.validate()
        if self.path_config:
            self.path_config.validate()
        if self.query_string_config:
            self.query_string_config.validate()
        if self.response_header_config:
            self.response_header_config.validate()
        if self.response_status_code_config:
            self.response_status_code_config.validate()
        if self.source_ip_config:
            self.source_ip_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cookie_config is not None:
            result['CookieConfig'] = self.cookie_config.to_map()

        if self.header_config is not None:
            result['HeaderConfig'] = self.header_config.to_map()

        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()

        if self.method_config is not None:
            result['MethodConfig'] = self.method_config.to_map()

        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()

        if self.query_string_config is not None:
            result['QueryStringConfig'] = self.query_string_config.to_map()

        if self.response_header_config is not None:
            result['ResponseHeaderConfig'] = self.response_header_config.to_map()

        if self.response_status_code_config is not None:
            result['ResponseStatusCodeConfig'] = self.response_status_code_config.to_map()

        if self.source_ip_config is not None:
            result['SourceIpConfig'] = self.source_ip_config.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsCookieConfig()
            self.cookie_config = temp_model.from_map(m.get('CookieConfig'))

        if m.get('HeaderConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsHeaderConfig()
            self.header_config = temp_model.from_map(m.get('HeaderConfig'))

        if m.get('HostConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m.get('HostConfig'))

        if m.get('MethodConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsMethodConfig()
            self.method_config = temp_model.from_map(m.get('MethodConfig'))

        if m.get('PathConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m.get('PathConfig'))

        if m.get('QueryStringConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfig()
            self.query_string_config = temp_model.from_map(m.get('QueryStringConfig'))

        if m.get('ResponseHeaderConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsResponseHeaderConfig()
            self.response_header_config = temp_model.from_map(m.get('ResponseHeaderConfig'))

        if m.get('ResponseStatusCodeConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsResponseStatusCodeConfig()
            self.response_status_code_config = temp_model.from_map(m.get('ResponseStatusCodeConfig'))

        if m.get('SourceIpConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsSourceIpConfig()
            self.source_ip_config = temp_model.from_map(m.get('SourceIpConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateRulesAttributeRequestRulesRuleConditionsSourceIpConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class UpdateRulesAttributeRequestRulesRuleConditionsResponseStatusCodeConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class UpdateRulesAttributeRequestRulesRuleConditionsResponseHeaderConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfig(DaraModel):
    def __init__(
        self,
        values: List[main_models.UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfigValues] = None,
    ):
        self.values = values

    def validate(self):
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfigValues()
                self.values.append(temp_model.from_map(k1))

        return self

class UpdateRulesAttributeRequestRulesRuleConditionsQueryStringConfigValues(DaraModel):
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

class UpdateRulesAttributeRequestRulesRuleConditionsPathConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class UpdateRulesAttributeRequestRulesRuleConditionsMethodConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class UpdateRulesAttributeRequestRulesRuleConditionsHostConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class UpdateRulesAttributeRequestRulesRuleConditionsHeaderConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class UpdateRulesAttributeRequestRulesRuleConditionsCookieConfig(DaraModel):
    def __init__(
        self,
        values: List[main_models.UpdateRulesAttributeRequestRulesRuleConditionsCookieConfigValues] = None,
    ):
        self.values = values

    def validate(self):
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.UpdateRulesAttributeRequestRulesRuleConditionsCookieConfigValues()
                self.values.append(temp_model.from_map(k1))

        return self

class UpdateRulesAttributeRequestRulesRuleConditionsCookieConfigValues(DaraModel):
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

class UpdateRulesAttributeRequestRulesRuleActions(DaraModel):
    def __init__(
        self,
        cors_config: main_models.UpdateRulesAttributeRequestRulesRuleActionsCorsConfig = None,
        fixed_response_config: main_models.UpdateRulesAttributeRequestRulesRuleActionsFixedResponseConfig = None,
        forward_group_config: main_models.UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfig = None,
        insert_header_config: main_models.UpdateRulesAttributeRequestRulesRuleActionsInsertHeaderConfig = None,
        order: int = None,
        redirect_config: main_models.UpdateRulesAttributeRequestRulesRuleActionsRedirectConfig = None,
        remove_header_config: main_models.UpdateRulesAttributeRequestRulesRuleActionsRemoveHeaderConfig = None,
        rewrite_config: main_models.UpdateRulesAttributeRequestRulesRuleActionsRewriteConfig = None,
        traffic_limit_config: main_models.UpdateRulesAttributeRequestRulesRuleActionsTrafficLimitConfig = None,
        traffic_mirror_config: main_models.UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfig = None,
        type: str = None,
    ):
        self.cors_config = cors_config
        self.fixed_response_config = fixed_response_config
        self.forward_group_config = forward_group_config
        self.insert_header_config = insert_header_config
        # This parameter is required.
        self.order = order
        self.redirect_config = redirect_config
        self.remove_header_config = remove_header_config
        self.rewrite_config = rewrite_config
        self.traffic_limit_config = traffic_limit_config
        self.traffic_mirror_config = traffic_mirror_config
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.cors_config:
            self.cors_config.validate()
        if self.fixed_response_config:
            self.fixed_response_config.validate()
        if self.forward_group_config:
            self.forward_group_config.validate()
        if self.insert_header_config:
            self.insert_header_config.validate()
        if self.redirect_config:
            self.redirect_config.validate()
        if self.remove_header_config:
            self.remove_header_config.validate()
        if self.rewrite_config:
            self.rewrite_config.validate()
        if self.traffic_limit_config:
            self.traffic_limit_config.validate()
        if self.traffic_mirror_config:
            self.traffic_mirror_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cors_config is not None:
            result['CorsConfig'] = self.cors_config.to_map()

        if self.fixed_response_config is not None:
            result['FixedResponseConfig'] = self.fixed_response_config.to_map()

        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()

        if self.insert_header_config is not None:
            result['InsertHeaderConfig'] = self.insert_header_config.to_map()

        if self.order is not None:
            result['Order'] = self.order

        if self.redirect_config is not None:
            result['RedirectConfig'] = self.redirect_config.to_map()

        if self.remove_header_config is not None:
            result['RemoveHeaderConfig'] = self.remove_header_config.to_map()

        if self.rewrite_config is not None:
            result['RewriteConfig'] = self.rewrite_config.to_map()

        if self.traffic_limit_config is not None:
            result['TrafficLimitConfig'] = self.traffic_limit_config.to_map()

        if self.traffic_mirror_config is not None:
            result['TrafficMirrorConfig'] = self.traffic_mirror_config.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorsConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsCorsConfig()
            self.cors_config = temp_model.from_map(m.get('CorsConfig'))

        if m.get('FixedResponseConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsFixedResponseConfig()
            self.fixed_response_config = temp_model.from_map(m.get('FixedResponseConfig'))

        if m.get('ForwardGroupConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m.get('ForwardGroupConfig'))

        if m.get('InsertHeaderConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsInsertHeaderConfig()
            self.insert_header_config = temp_model.from_map(m.get('InsertHeaderConfig'))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('RedirectConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsRedirectConfig()
            self.redirect_config = temp_model.from_map(m.get('RedirectConfig'))

        if m.get('RemoveHeaderConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsRemoveHeaderConfig()
            self.remove_header_config = temp_model.from_map(m.get('RemoveHeaderConfig'))

        if m.get('RewriteConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsRewriteConfig()
            self.rewrite_config = temp_model.from_map(m.get('RewriteConfig'))

        if m.get('TrafficLimitConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsTrafficLimitConfig()
            self.traffic_limit_config = temp_model.from_map(m.get('TrafficLimitConfig'))

        if m.get('TrafficMirrorConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfig()
            self.traffic_mirror_config = temp_model.from_map(m.get('TrafficMirrorConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfig(DaraModel):
    def __init__(
        self,
        mirror_group_config: main_models.UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig = None,
        target_type: str = None,
    ):
        self.mirror_group_config = mirror_group_config
        self.target_type = target_type

    def validate(self):
        if self.mirror_group_config:
            self.mirror_group_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mirror_group_config is not None:
            result['MirrorGroupConfig'] = self.mirror_group_config.to_map()

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MirrorGroupConfig') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig()
            self.mirror_group_config = temp_model.from_map(m.get('MirrorGroupConfig'))

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_tuples: List[main_models.UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples] = None,
    ):
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for v1 in self.server_group_tuples:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k1 in self.server_group_tuples:
                result['ServerGroupTuples'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k1 in m.get('ServerGroupTuples'):
                temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class UpdateRulesAttributeRequestRulesRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsTrafficLimitConfig(DaraModel):
    def __init__(
        self,
        per_ip_qps: int = None,
        qps: int = None,
    ):
        self.per_ip_qps = per_ip_qps
        self.qps = qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.per_ip_qps is not None:
            result['PerIpQps'] = self.per_ip_qps

        if self.qps is not None:
            result['QPS'] = self.qps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerIpQps') is not None:
            self.per_ip_qps = m.get('PerIpQps')

        if m.get('QPS') is not None:
            self.qps = m.get('QPS')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsRewriteConfig(DaraModel):
    def __init__(
        self,
        host: str = None,
        path: str = None,
        query: str = None,
    ):
        self.host = host
        self.path = path
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.path is not None:
            result['Path'] = self.path

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsRemoveHeaderConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
    ):
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsRedirectConfig(DaraModel):
    def __init__(
        self,
        host: str = None,
        http_code: str = None,
        path: str = None,
        port: str = None,
        protocol: str = None,
        query: str = None,
    ):
        self.host = host
        self.http_code = http_code
        self.path = path
        self.port = port
        self.protocol = protocol
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.path is not None:
            result['Path'] = self.path

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsInsertHeaderConfig(DaraModel):
    def __init__(
        self,
        cover_enabled: bool = None,
        key: str = None,
        value: str = None,
        value_type: str = None,
    ):
        self.cover_enabled = cover_enabled
        self.key = key
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_enabled is not None:
            result['CoverEnabled'] = self.cover_enabled

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverEnabled') is not None:
            self.cover_enabled = m.get('CoverEnabled')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_sticky_session: main_models.UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupStickySession = None,
        server_group_tuples: List[main_models.UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        self.server_group_sticky_session = server_group_sticky_session
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_sticky_session:
            self.server_group_sticky_session.validate()
        if self.server_group_tuples:
            for v1 in self.server_group_tuples:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.server_group_sticky_session is not None:
            result['ServerGroupStickySession'] = self.server_group_sticky_session.to_map()

        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k1 in self.server_group_tuples:
                result['ServerGroupTuples'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupStickySession') is not None:
            temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupStickySession()
            self.server_group_sticky_session = temp_model.from_map(m.get('ServerGroupStickySession'))

        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k1 in m.get('ServerGroupTuples'):
                temp_model = main_models.UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        server_group_id: str = None,
        weight: int = None,
    ):
        self.server_group_id = server_group_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsForwardGroupConfigServerGroupStickySession(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        timeout: int = None,
    ):
        self.enabled = enabled
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsFixedResponseConfig(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        http_code: str = None,
    ):
        self.content = content
        self.content_type = content_type
        self.http_code = http_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        return self

class UpdateRulesAttributeRequestRulesRuleActionsCorsConfig(DaraModel):
    def __init__(
        self,
        allow_credentials: str = None,
        allow_headers: List[str] = None,
        allow_methods: List[str] = None,
        allow_origin: List[str] = None,
        expose_headers: List[str] = None,
        max_age: int = None,
    ):
        self.allow_credentials = allow_credentials
        self.allow_headers = allow_headers
        self.allow_methods = allow_methods
        self.allow_origin = allow_origin
        self.expose_headers = expose_headers
        self.max_age = max_age

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_credentials is not None:
            result['AllowCredentials'] = self.allow_credentials

        if self.allow_headers is not None:
            result['AllowHeaders'] = self.allow_headers

        if self.allow_methods is not None:
            result['AllowMethods'] = self.allow_methods

        if self.allow_origin is not None:
            result['AllowOrigin'] = self.allow_origin

        if self.expose_headers is not None:
            result['ExposeHeaders'] = self.expose_headers

        if self.max_age is not None:
            result['MaxAge'] = self.max_age

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCredentials') is not None:
            self.allow_credentials = m.get('AllowCredentials')

        if m.get('AllowHeaders') is not None:
            self.allow_headers = m.get('AllowHeaders')

        if m.get('AllowMethods') is not None:
            self.allow_methods = m.get('AllowMethods')

        if m.get('AllowOrigin') is not None:
            self.allow_origin = m.get('AllowOrigin')

        if m.get('ExposeHeaders') is not None:
            self.expose_headers = m.get('ExposeHeaders')

        if m.get('MaxAge') is not None:
            self.max_age = m.get('MaxAge')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class UpdateForwardingRulesRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        forwarding_rules: List[main_models.UpdateForwardingRulesRequestForwardingRules] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The ID of the Global Accelerator instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the request as the **client token**. The **RequestId** of each request is different.
        self.client_token = client_token
        # The configurations of the forwarding rules.
        # 
        # This parameter is required.
        self.forwarding_rules = forwarding_rules
        # The ID of the listener.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The region ID of the Global Accelerator instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.forwarding_rules:
            for v1 in self.forwarding_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k1 in self.forwarding_rules:
                result['ForwardingRules'].append(k1.to_map() if k1 else None)

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k1 in m.get('ForwardingRules'):
                temp_model = main_models.UpdateForwardingRulesRequestForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k1))

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class UpdateForwardingRulesRequestForwardingRules(DaraModel):
    def __init__(
        self,
        forwarding_rule_id: str = None,
        forwarding_rule_name: str = None,
        priority: int = None,
        rule_actions: List[main_models.UpdateForwardingRulesRequestForwardingRulesRuleActions] = None,
        rule_conditions: List[main_models.UpdateForwardingRulesRequestForwardingRulesRuleConditions] = None,
        rule_direction: str = None,
    ):
        # The ID of the forwarding rule.
        # 
        # This parameter is required.
        self.forwarding_rule_id = forwarding_rule_id
        # The name of the forwarding rule.
        # 
        # The name must be 2 to 128 characters in length, start with a letter or a Chinese character, and can contain digits, periods (.), underscores (_), and hyphens (-).
        self.forwarding_rule_name = forwarding_rule_name
        # The priority of the forwarding rule. A smaller value indicates a higher priority. Valid values: **1** to **10000**.
        # 
        # This parameter is required.
        self.priority = priority
        # The actions that are performed when the forwarding conditions are met.
        # 
        # This parameter is required.
        self.rule_actions = rule_actions
        # The forwarding conditions.
        # 
        # This parameter is required.
        self.rule_conditions = rule_conditions
        # The direction of the rule. You do not need to specify this parameter.
        # 
        # This parameter is set to **request** by default, which indicates that the rule applies to inbound requests.
        self.rule_direction = rule_direction

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
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id

        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name

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

        if self.rule_direction is not None:
            result['RuleDirection'] = self.rule_direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')

        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k1 in m.get('RuleActions'):
                temp_model = main_models.UpdateForwardingRulesRequestForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.UpdateForwardingRulesRequestForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('RuleDirection') is not None:
            self.rule_direction = m.get('RuleDirection')

        return self

class UpdateForwardingRulesRequestForwardingRulesRuleConditions(DaraModel):
    def __init__(
        self,
        host_config: main_models.UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig = None,
        path_config: main_models.UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig = None,
        rule_condition_type: str = None,
        rule_condition_value: str = None,
    ):
        # The domain configuration.
        # 
        # > This parameter is deprecated. We recommend that you use the **RuleConditionType** and **RuleConditionValue** parameters.
        self.host_config = host_config
        # The path configuration.
        # 
        # > This parameter is deprecated. We recommend that you use the **RuleConditionType** and **RuleConditionValue** parameters.
        self.path_config = path_config
        # The type of the forwarding condition. Valid values:
        # 
        # - **Host**: matches a request based on its domain name.
        # 
        # - **Path**: matches a request based on its path.
        # 
        # - **RequestHeader**: matches a request based on its HTTP header.
        # 
        # - **Query**: matches a request based on its query string.
        # 
        # - **Method**: matches a request based on its HTTP request method.
        # 
        # - **Cookie**: matches a request based on its cookie.
        # 
        # - **SourceIP**: matches a request based on its source IP address.
        # 
        # This parameter is required.
        self.rule_condition_type = rule_condition_type
        # The value of the forwarding condition.
        # The value is a JSON string that varies based on the value of **RuleConditionType**.
        # 
        # - If **RuleConditionType** is set to **Host**, this parameter specifies the domain configuration. A forwarding rule can contain only one Host-based rule condition. The condition can contain multiple domains that are evaluated with a logical OR. A domain must be 3 to 128 characters in length and can contain letters, digits, hyphens (-), and periods (.). You can use asterisks (\\*) and question marks (?) as wildcards. Example: `["www.example.com", "www.aliyun.com"]`.
        # 
        # - If **RuleConditionType** is set to **Path**, this parameter specifies the path configuration. A forwarding rule can contain multiple path-based rule conditions, which are evaluated with a logical OR. Each condition can contain multiple paths, which are also evaluated with a logical OR. A path must be 1 to 128 characters in length, start with a forward slash (/), and contain only letters, digits, and the following special characters: `$`, `-`, `_`, `.`, `+`, `/`, `&`, `~`, `@`, `:`, and `\\"`. You can use asterisks (\\*) and question marks (?) as wildcards. Example: `["/a", "/b/"]`.
        # 
        # - If **RuleConditionType** is set to **RequestHeader**, this parameter specifies the HTTP header configuration, which consists of key-value pairs. The values for a specific header must be unique. Example: `[{"header1":["value1","value2"]}]`.
        # 
        #   - Key: The key of the HTTP header. The key must be 1 to 40 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        #   - Value: The value of the HTTP header. The value must be 1 to 128 characters in length and can contain printable ASCII characters whose character codes are in the range of `ch >= 32 && ch < 127`. The value cannot start or end with a space.
        # 
        # - If **RuleConditionType** is set to **Query**, this parameter specifies the query string configuration, which consists of key-value pairs. Example: `[{"query1":["value1"]}, {"query2":["value2"]}]`.
        # 
        #   - Key: The key of the query string. The key must be 1 to 100 characters in length and can contain printable ASCII characters whose character codes are in the range of `ch >= 32 && ch < 127`. The letters must be in lowercase. Spaces and the following characters are not allowed: `[]{}<>\\;/?:@&=+,$%|"^~`.
        # 
        #   - Value: The value of the query string. The value must be 1 to 128 characters in length and can contain printable ASCII characters whose character codes are in the range of `ch >= 32 && ch < 127`. The letters must be in lowercase. Spaces and the following characters are not allowed: `[]{}<>\\;/?:@&=+,$%|"^~`.
        # 
        # - If **RuleConditionType** is set to **Method**, this parameter specifies the HTTP request method configuration. Valid values: **HEAD**, **GET**, **POST**, **OPTIONS**, **PUT**, **PATCH**, and **DELETE**. Example: `["GET", "OPTIONS", "POST"]`.
        # 
        # - If **RuleConditionType** is set to **Cookie**, this parameter specifies the cookie configuration, which consists of key-value pairs. Example: `[{"cookie1":["value1"]}, {"cookie2":["value2"]}]`
        # 
        #   - Key: The key of the cookie. The key must be 1 to 100 characters in length and can contain printable ASCII characters whose character codes are in the range of `ch >= 32 && ch < 127`. The letters must be in lowercase. Spaces and the following characters are not allowed: `#[]{}\\|<>&`.
        # 
        #   - Value: The value of the cookie. The value must be 1 to 128 characters in length and can contain printable ASCII characters whose character codes are in the range of `ch >= 32 && ch < 127`. The letters must be in lowercase. Spaces and the following characters are not allowed: `#[]{}\\|<>&`.
        # 
        # - If **RuleConditionType** is set to **SourceIP**, this parameter specifies the source IP configuration. You can specify IP addresses such as 1.1.XX.XX/32 or CIDR blocks such as 2.2.XX.XX/24. A forwarding rule can contain only one source IP-based rule condition, which can contain multiple source IP addresses or CIDR blocks that are evaluated with a logical OR. Example: `["1.1.XX.XX/32", "2.2.XX.XX/24"]`.
        self.rule_condition_value = rule_condition_value

    def validate(self):
        if self.host_config:
            self.host_config.validate()
        if self.path_config:
            self.path_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()

        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()

        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type

        if self.rule_condition_value is not None:
            result['RuleConditionValue'] = self.rule_condition_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostConfig') is not None:
            temp_model = main_models.UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m.get('HostConfig'))

        if m.get('PathConfig') is not None:
            temp_model = main_models.UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m.get('PathConfig'))

        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')

        if m.get('RuleConditionValue') is not None:
            self.rule_condition_value = m.get('RuleConditionValue')

        return self

class UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The path configuration.
        # 
        # > This parameter is deprecated. We recommend that you use the **RuleConditionType** and **RuleConditionValue** parameters.
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

class UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The domain configuration.
        # 
        # > This parameter is deprecated. We recommend that you use the **RuleConditionType** and **RuleConditionValue** parameters.
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

class UpdateForwardingRulesRequestForwardingRulesRuleActions(DaraModel):
    def __init__(
        self,
        forward_group_config: main_models.UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig = None,
        order: int = None,
        rule_action_type: str = None,
        rule_action_value: str = None,
    ):
        # The forwarding configuration.
        # 
        # > This parameter is deprecated. We recommend that you use the **RuleActionType** and **RuleActionValue** parameters.
        self.forward_group_config = forward_group_config
        # The priority of the action.
        # 
        # > This parameter is not in use. You do not need to specify this parameter.
        # 
        # This parameter is required.
        self.order = order
        # The type of the action. Valid values:
        # 
        # - **ForwardGroup**: forwards a request to an endpoint group.
        # 
        # - **Redirect**: redirects a request.
        # 
        # - **FixResponse**: returns a fixed response.
        # 
        # - **Rewrite**: rewrites a request.
        # 
        # - **AddHeader**: adds a header to a request.
        # 
        # - **RemoveHeader**: removes a header from a request.
        # 
        # - **Drop**: drops a request.
        # 
        # This parameter is required.
        self.rule_action_type = rule_action_type
        # The value of the action.
        # 
        # The value is a JSON string that varies based on the value of **RuleActionType**.
        # 
        # A forwarding rule can have at most one action of the **ForwardGroup**, **Redirect**, or **FixResponse** type. The `Rewrite`, `AddHeader`, and `RemoveHeader` actions must precede a `ForwardGroup` action.
        # 
        # - If **RuleActionType** is set to **ForwardGroup**, this parameter specifies the endpoint group configuration. You can forward requests to only one endpoint group. Example: `{"type":"endpointgroup", "value":"epg-bp1enpdcrqhl78g6r****"}`, where:
        # 
        #   - `type`: Set the value to `endpointgroup`.
        # 
        #   - `value`: The ID of the destination endpoint group.
        # 
        # - If **RuleActionType** is set to **Redirect**, this parameter specifies the redirect configuration. In a **Redirect** action, at least one of the following fields must be specified with a non-default value: `protocol`, `domain`, `port`, `path`, or `query`. Example: `{"protocol":"HTTP", "domain":"www.example.com", "port":"80", "path":"/a","query":"value1", "code":"301" }`, where:
        # 
        #   - `protocol`: The protocol to which requests are redirected. Valid values: `${protocol}` (default), `HTTP`, and `HTTPS`.
        # 
        #   - `domain`: The domain to which requests are redirected. The default value is `${host}`. You can also specify another domain. The domain must be 3 to 128 characters in length and can contain only lowercase letters, digits, and the following special characters: `.-?=~_-+/^*!$&|()[]`.
        # 
        #   - `port`: The port to which requests are redirected. The default value is `${port}`. You can also specify another port. Valid values: 1 to 63335.
        # 
        #   - `path`: The path to which requests are redirected. The default value is `${path}`. The path must be 1 to 128 characters in length. A regular expression-based path must start with a tilde (\\~) and can contain letters, digits, and the following special characters: `.-_/=?~^*$:()[]+|`. A path that is not a regular expression must start with a forward slash (/) and can contain letters, digits, and the following special characters: `.-_/=?:`.
        # 
        #   - `query`: The query string to which requests are redirected. The default value is `${query}`. You can also specify another query string. The query string must be 1 to 128 characters in length and can contain printable ASCII characters whose character codes are in the range of `ch >= 32 && ch < 127`. The letters must be in lowercase. Spaces and the following characters are not allowed: `[]{}<>\\#|&`.
        # 
        #   - `code`: The redirect type. Valid values: `301`, `302`, `303`, `307`, and `308`.
        # 
        # - If **RuleActionType** is set to **FixResponse**, this parameter specifies the fixed response configuration. Example: `{"code":"200", "type":"text/plain", "content":"dssacav" }`, where:
        # 
        #   - `code`: The HTTP status code. You can specify a numeric string that represents a `2xx`, `4xx`, or `5xx` status code, where `x` indicates a digit.
        # 
        #   - `type`: The content type of the response body. Valid values: **text/plain**, **text/css**, **text/html**, **application/javascript**, and **application/json**.
        # 
        #   - `content`: The content of the response body. The content can be up to 1,024 characters in length and cannot contain Chinese characters.
        # 
        # - If **RuleActionType** is set to **AddHeader**, this parameter specifies the configuration for adding an HTTP header. An **AddHeader** action must be used together with a **ForwardGroup** action. Example: `[{"name":"header1","type":"user-defined", "value":"value"}]`, where:
        # 
        #   - `name`: The name of the HTTP header. The name must be 1 to 40 characters in length and can contain letters, digits, hyphens (-), and underscores (_). The header names specified for **AddHeader** must be unique and cannot be the same as those specified for **RemoveHeader**.
        # 
        #   - `type`: The content type of the HTTP header. Valid values: `user-defined`, `ref` (reference), and `system-defined`.
        # 
        #   - `value`: The content of the HTTP header. This parameter cannot be left empty. If `type` is set to `user-defined`, the content must be 1 to 128 characters in length and can contain printable ASCII characters whose character codes are in the range of `ch >= 32 && ch < 127`. The content can include letters, digits, hyphens (-), and underscores (_). The content cannot start or end with a space. If `type` is set to `ref` (reference), the content must be 1 to 128 characters in length and can contain letters, digits, hyphens (-), and underscores (_). The content cannot start or end with a space. If `type` is set to `system-defined`, the only valid value is `ClientSrcIp`.
        # 
        # - If **RuleActionType** is set to **RemoveHeader**, this parameter specifies the configuration for removing an HTTP header. A **RemoveHeader** action must be used together with a **ForwardGroup** action. The header name must be 1 to 40 characters in length and can contain letters, digits, hyphens (-), and underscores (_). Example: `["header1"]`.
        # 
        # - If **RuleActionType** is set to **Rewrite**, this parameter specifies the rewrite configuration. A **Rewrite** action must be used together with a **ForwardGroup** action. Example: `{"domain":"value1", "path":"value2", "query":"value3"}`, where:
        # 
        #   - `domain`: The domain to which requests are rewritten. The default value is `${host}`. You can also specify another domain. The domain must be 3 to 128 characters in length and can contain only lowercase letters, digits, and the following special characters: `.-?=~_-+/^*!$&|()[]`.
        # 
        #   - `path`: The path to which requests are rewritten. The default value is `${path}`. The path must be 1 to 128 characters in length. A regular expression-based path must start with a tilde (\\~) and can contain letters, digits, and the following special characters: `.-_/=?~^*$:()[]+|`. A path that is not a regular expression must start with a forward slash (/) and can contain letters, digits, and the following special characters: `.-_/=?:`.
        # 
        #   - `query`: The query string to which requests are rewritten. The default value is `${query}`. You can also specify another query string. The query string must be 1 to 128 characters in length and can contain printable ASCII characters whose character codes are in the range of `ch >= 32 && ch < 127`. The letters must be in lowercase. Spaces and the following characters are not allowed: `[]{}<>\\#|&`.
        # 
        # - If **RuleActionType** is set to **Drop**, you do not need to specify this parameter.
        self.rule_action_value = rule_action_value

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()

        if self.order is not None:
            result['Order'] = self.order

        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type

        if self.rule_action_value is not None:
            result['RuleActionValue'] = self.rule_action_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = main_models.UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m.get('ForwardGroupConfig'))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')

        if m.get('RuleActionValue') is not None:
            self.rule_action_value = m.get('RuleActionValue')

        return self

class UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_tuples: List[main_models.UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # The endpoint group configuration.
        # 
        # > This parameter is deprecated. We recommend that you use the **RuleActionType** and **RuleActionValue** parameters.
        # 
        # This parameter is required.
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
                temp_model = main_models.UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
    ):
        # The ID of the endpoint group.
        # 
        # > This parameter is deprecated. We recommend that you use the **RuleActionType** and **RuleActionValue** parameters.
        # 
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        return self


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
        # The GA instance ID.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The configurations of the forwarding rules.
        # 
        # This parameter is required.
        self.forwarding_rules = forwarding_rules
        # The listener ID.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
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
        # The forwarding rule ID.
        # 
        # This parameter is required.
        self.forwarding_rule_id = forwarding_rule_id
        # The forwarding rule name.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.forwarding_rule_name = forwarding_rule_name
        # The priority of the forwarding rule. Valid values: **1** to **10000**. A smaller value specifies a higher priority.
        # 
        # This parameter is required.
        self.priority = priority
        # The configurations of the forwarding actions.
        # 
        # This parameter is required.
        self.rule_actions = rule_actions
        # The conditions that trigger the forwarding rule.
        # 
        # This parameter is required.
        self.rule_conditions = rule_conditions
        # The direction in which the rule takes effect. You do not need to specify this parameter.
        # 
        # By default, this parameter is set to **request**, which specifies that the rule takes effect on requests.
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
        # The domain name configuration.
        # 
        # >  We recommend that you use **RuleConditionType** and **RuleConditionValue** rather than this parameter to configure forwarding conditions.
        self.host_config = host_config
        # The path configuration.
        # 
        # >  We recommend that you use **RuleConditionType** and **RuleConditionValue** rather than this parameter to configure forwarding conditions.
        self.path_config = path_config
        # The type of the forwarding condition. Valid values:
        # 
        # *   **Host**: Requests are forwarded based on domain names.
        # *   **Path**: Requests are forwarded based on paths.
        # *   **RequestHeader**: Requests are forwarded based on HTTP headers.
        # *   **Query**: Requests are forwarded based on query strings.
        # *   **Method**: Requests are forwarded based on HTTP request methods.
        # *   **Cookie**: Requests are forwarded based on cookies.
        # *   **SourceIp**: Requests are forwarded based on source IP addresses.
        # 
        # This parameter is required.
        self.rule_condition_type = rule_condition_type
        # The value of the forwarding condition. You must specify different JSON strings based on **RuleConditionType**.
        # 
        # *   If **RuleConditionType** is set to **Host**, RuleConditionValue specifies a domain name condition. A forwarding rule can contain only one forwarding condition of the host type. You can specify multiple domain names in a forwarding condition. The relationship between multiple domain names is OR. The domain name must be 3 to 128 characters in length, and can contain letters, digits, hyphens (-), and periods (.). You can use asterisks (\\*) and question marks (?) as wildcard characters. Example: `["www.example.com", "www.aliyun.com"]`.
        # 
        # *   If **RuleConditionType** is set to **Path**, RuleConditionValue specifies a path condition. A forwarding rule can contain multiple forwarding conditions of the path type. The relationship between multiple path conditions is OR. You can specify multiple paths in a forwarding condition. The relationship between multiple paths is OR. The path must be 1 to 128 characters in length, and must start with a forward slash (/). The path can contain letters, digits, and the following special characters: $ - _ . + / & ~ @ : \\". Supported wildcard characters are asterisks (\\*) and question marks (?). Example: `["/a", "/b/"]`.
        # 
        # *   If **RuleConditionType** is set to **RequestHeader**, RuleConditionValue specifies an HTTP header condition. An HTTP header consists of a key and a value. The header values in a forwarding condition must be unique. Example: `[{"header1":["value1","value2"]}]`.
        # 
        #     *   Key: The key of an HTTP header must be 1 to 40 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        #     *   Value: The value of an HTTP header must be 1 to 128 characters in length and can contain printable characters whose ASCII values `are larger than or equal to 32 and smaller than 127`. The value cannot start or end with a space.
        # 
        # *   If **RuleConditionType** is set to **Query**, RuleConditionValue specifies a query string condition. A query string consists of a key and a value. Example: `[{"query1":["value1"]}, {"query2":["value2"]}]`.
        # 
        #     *   Key: The key must be 1 to 100 characters in length and can contain printable characters whose ASCII values `are larger than or equal to 32 and smaller than 127`, excluding uppercase letters, spaces, and the following special characters: `[ ] { } < > \\ ; / ? : @ & = + , $ % " ^ ~`.
        #     *   Value: The value must be 1 to 128 characters in length and can contain printable characters whose ASCII values `are larger than or equal to 32 and smaller than 127`, excluding uppercase letters, spaces, and the following special characters: `[ ] { } < > \\ ; / ? : @ & = + , $ % " ^ ~`.
        # 
        # *   If **RuleConditionType** is set to **Method**, RuleConditionValue specifies an HTTP method condition. Valid values: **HEAD**, **GET**, **POST**, **OPTIONS**, **PUT**, **PATCH**, and **DELETE**. Example: `["GET", "OPTIONS", "POST"]`.
        # 
        # *   If **RuleConditionType** is set to **Cookie**, RuleConditionValue specifies a cookie condition. A cookie consists of a key and a value. Example: `[{"cookie1":["value1"]}, {"cookie2":["value2"]}]`.
        # 
        #     *   Key: The key of a cookie must be 1 to 100 characters in length and can contain printable characters whose ASCII values `are larger than or equal to 32 and smaller than 127`, excluding uppercase letters, spaces, and the following special characters: `# [ ] { } \\ < > &`.
        #     *   Value: The value of a cookie must be 1 to 128 characters in length and can contain printable characters whose ASCII values `are larger than or equal to 32 and smaller than 127`, excluding uppercase letters, spaces, and the following special characters: `# [ ] { } \\ < > &`.
        # 
        # *   If **RuleConditionType** is set to **SourceIP**, RuleConditionValue specifies a source IP address condition. IP addresses, such as 1.1.XX.XX/32, and CIDR blocks, such as 2.2.XX.XX/24, are supported. A forwarding rule can contain only one forwarding condition of the SourceIP type. You can specify multiple source IP addresses or CIDR blocks in a forwarding condition. The relationship between multiple IP addresses or CIDR blocks is OR. Example: `["1.1.XX.XX/32", "2.2.XX.XX/24"]`.
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
        # >  We recommend that you use **RuleConditionType** and **RuleConditionValue** rather than this parameter to configure forwarding conditions.
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
        # The domain name configuration.
        # 
        # >  We recommend that you use **RuleConditionType** and **RuleConditionValue** rather than this parameter to configure forwarding conditions.
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
        # >  We recommend that you use **RuleActionType** and **RuleActionValue** rather than this parameter to configure forwarding actions.
        self.forward_group_config = forward_group_config
        # The forwarding priority.
        # 
        # >  This parameter does not take effect. Ignore this parameter.
        # 
        # This parameter is required.
        self.order = order
        # The type of the forwarding action. Valid values:
        # 
        # *   **ForwardGroup**: forwards a request.
        # *   **Redirect**: redirects a request.
        # *   **FixResponse**: returns a fixed response.
        # *   **Rewrite**: rewrites a request.
        # *   **AddHeader**: adds a header to a request.
        # *   **RemoveHeaderConfig**: deletes the header of a request.
        # *   **Drop**: drops a request.
        # 
        # This parameter is required.
        self.rule_action_type = rule_action_type
        # The value of the forwarding action.
        # 
        # You must specify different JSON strings based on **RuleActionType**.
        # 
        # A forwarding rule can contain only one forwarding action whose type is **ForwardGroup**, **Redirect**, or **FixResponse**. You must specify a forwarding action whose type is **Rewrite**, **AddHeader**, or **RemoveHeader** before a forwarding action whose type is **ForwardGroup**.
        # 
        # *   If **RuleActionType** is set to **ForwardGroup**, this parameter specifies the information of a virtual endpoint group. You can forward requests to only one virtual endpoint group. Example: `{"type":"endpointgroup", "value":"epg-bp1enpdcrqhl78g6r****"}`.
        # 
        #     *   `type`: Set this parameter to `endpointgroup`.
        #     *   `value`: Set this parameter to the ID of a virtual endpoint group.
        # 
        # *   If **RuleActionType** is set to **Redirect**, this parameter specifies redirecting configurations. You cannot leave the following parameters empty or use the default values for the following parameters for a forwarding action whose type is **Redirect**: `protocol`, `domain`, `port`, `path`, and `query`. Example: `{"protocol":"HTTP", "domain":"www.example.com", "port":"80", "path":"/a","query":"value1", "code":"301" }`.
        # 
        #     *   `protocol`: the protocol of requests after the requests are redirected. Valid values: `${protocol}` (default), `HTTP`, and `HTTPS`.
        #     *   `domain`: the domain name to which requests are redirected. Default value: `${host}`. You can also enter a domain name. The domain name must be 3 to 128 characters in length, and can contain only letters, digits, and the following special characters: `. - ? = ~ _ - + / ^ * ! $ & | ( ) [ ]`.
        #     *   `port`: the port to which requests are redirected. Default value: `${port}`. You can enter a port number from 1 to 63335.
        #     *   `path`: the path to which requests are redirected. Default value: `${path}`. The path must be 1 to 128 characters in length. To use a regular expression, the path can contain letters, digits, and the following special characters: `. - _ / = ? ~ ^ * $ : ( ) [ ] + |`. The path must start with a tilde (~). If you do not want to use a regular expression, the path can contain letters, digits, and the following special characters: `. - _ / = ? :`. The path must start with a forward slash (/).
        #     *   `query`: the query string of the requests that are redirected. Default value: `${query}`. You can also specify a query string. The query string must be 1 to 128 characters in length, and can contain printable characters whose ASCII values are `greater than or equal to 32 and smaller than 127`. The query string cannot contain uppercase letters, space characters, or the following special characters: `[ ] { } < > # | &`.
        #     *   `code`: the redirect code. Valid values: `301`, `302`, `303`, `307`, and `308`.
        # 
        # *   If **RuleActionType** is set to **FixResponse**, this parameter specifies a fixed response. Example: `{"code":"200", "type":"text/plain", "content":"dssacav" }`.
        # 
        #     *   `code`: the HTTP response status code. The response status code must be one of the following numeric strings: `2xx`, `4xx`, and `5xx`. The letter `x` indicates a number from 0 to 9.
        #     *   `type`: the type of the response content. Valid values: **text/plain**, **text/css**, **text/html**, **application/javascript**, and **application/json**.
        #     *   `content`: the response content. The response content cannot exceed 1,000 characters in length, and does not support Chinese characters.
        # 
        # *   If **RuleActionType** is set to **AddHeader**, this parameter specifies an HTTP header to be added. If a forwarding rule contains a forwarding action whose type is **AddHeader**, you must specify another forwarding action whose type is **ForwardGroup**. Example: `[{"name":"header1","type":"userdefined", "value":"value"}]`.
        # 
        #     *   `name`: the name of the HTTP header. The name must be 1 to 40 characters in length, and can contain letters, digits, hyphens (-), and underscores (_). The name of the HTTP header specified by **AddHeader** must be unique and cannot be the same as the name of the HTTP header specified by **RemoveHeader**.
        #     *   `type`: the content type of the HTTP header. Valid values: `user-defined`, `ref`, and `system-defined`.
        #     *   `value`: the content of the HTTP header. You cannot leave this parameter empty. If you set `type` to `user-defined`, the content must be 1 to 128 characters in length, and can contain printable characters whose ASCII values are `greater than or equal to 32 and smaller than 127`. The content can contain letters, digits, hyphens (-), and underscores (_*). The content cannot start or end with a space character. If you set `type` to `ref`, the content must be 1 to 128 characters in length, and can contain letters, digits, hyphens (-), and underscores (_*). The content cannot start or end with a space character. If you set `type` to `system-defined`, only `ClientSrcIp` is supported.
        # 
        # *   If **RuleActionType** is set to **RemoveHeader**, this parameter specifies an HTTP header to be removed. If a forwarding rule contains a forwarding action whose type is **RemoveHeader**, you must specify another forwarding action whose type is **ForwardGroup**. The header must be 1 to 40 characters in length, and can contain letters, digits, hyphens (-), and underscores (_). Example: `["header1"]`.
        # 
        # *   If **RuleActionType** is set to **Rewrite**, this parameter specifies the rewriting configuration. If a forwarding rule contains a forwarding action whose type is **Rewrite**, you must specify another forwarding action whose type is **ForwardGroup**. Example: `{"domain":"value1", "path":"value2", "query":"value3"}`.
        # 
        #     *   `domain`: the domain name to which requests are redirected. Default value: `${host}`. You can also enter a domain name. The domain name must be 3 to 128 characters in length, and can contain only lowercase letters, digits, and the following special characters: `. - ? = ~ _ - + / ^ * ! $ & | ( ) [ ]`.
        #     *   `path`: the path to which requests are redirected. Default value: `${path}`. The path must be 1 to 128 characters in length. To use a regular expression, the path can contain letters, digits, and the following special characters: `. - _ / = ? ~ ^ * $ : ( ) [ ] + |`. The path must start with a tilde (~). If you do not want to use a regular expression, the path can contain letters, digits, and the following special characters: `. - _ / = ? :`. The path must start with a forward slash (/).
        #     *   `query`: the query string of the requests that are redirected. Default value: `${query}`. You can also specify a query string. The query string must be 1 to 128 characters in length, and can contain printable characters whose ASCII values are `greater than or equal to 32 and smaller than 127`. The query string cannot contain uppercase letters, space characters, or the following special characters: `[ ] { } < > # | &`.
        # 
        # *   If **RuleActionType** is set to **Drop**, you do not need to specify this parameter.
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
        # The configuration of an endpoint group.
        # 
        # >  We recommend that you use **RuleActionType** and **RuleActionValue** rather than this parameter to configure forwarding actions.
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
        # >  We recommend that you use **RuleActionType** and **RuleActionValue** rather than this parameter to configure forwarding actions.
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


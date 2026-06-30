# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateForwardingRulesRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        forwarding_rules: List[main_models.CreateForwardingRulesRequestForwardingRules] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The ID of the Global Accelerator instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a client token from your client and make sure that the client token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the request as the **ClientToken**. The **RequestId** of each request is different.
        self.client_token = client_token
        # The forwarding rule configurations.
        # 
        # This parameter is required.
        self.forwarding_rules = forwarding_rules
        # The ID of the listener.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The ID of the region where the Global Accelerator instance is deployed. The only valid value is **cn-hangzhou**.
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
                temp_model = main_models.CreateForwardingRulesRequestForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k1))

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateForwardingRulesRequestForwardingRules(DaraModel):
    def __init__(
        self,
        forwarding_rule_name: str = None,
        priority: int = None,
        rule_actions: List[main_models.CreateForwardingRulesRequestForwardingRulesRuleActions] = None,
        rule_conditions: List[main_models.CreateForwardingRulesRequestForwardingRulesRuleConditions] = None,
        rule_direction: str = None,
    ):
        # The name of the forwarding rule. The name must be 2 to 128 characters long. It must start with a letter or a Chinese character, and can contain letters, Chinese characters, digits, periods (.), underscores (_), and hyphens (-).
        self.forwarding_rule_name = forwarding_rule_name
        # The priority of the forwarding rule.
        # Valid values: **1** to **10000**. A smaller value indicates a higher priority.
        self.priority = priority
        # The rule actions.
        # 
        # This parameter is required.
        self.rule_actions = rule_actions
        # The rule conditions.
        # 
        # This parameter is required.
        self.rule_conditions = rule_conditions
        # The direction in which the rule takes effect. This parameter does not need to be configured.
        # 
        # By default, this parameter is set to **request**, which indicates that the rule applies to requests.
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
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k1 in m.get('RuleActions'):
                temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('RuleDirection') is not None:
            self.rule_direction = m.get('RuleDirection')

        return self

class CreateForwardingRulesRequestForwardingRulesRuleConditions(DaraModel):
    def __init__(
        self,
        host_config: main_models.CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig = None,
        path_config: main_models.CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig = None,
        rule_condition_type: str = None,
        rule_condition_value: str = None,
    ):
        # The domain name configuration.
        # 
        # > This parameter is deprecated. We recommend that you use **RuleConditionType** and **RuleConditionValue** to configure rule conditions.
        self.host_config = host_config
        # The path configuration.
        # 
        # > This parameter is deprecated. We recommend that you use **RuleConditionType** and **RuleConditionValue** to configure rule conditions.
        self.path_config = path_config
        # The type of the rule condition. Valid values:
        # 
        # - **Host**: Matches requests by domain name.
        # 
        # - **Path**: Matches requests by path.
        # 
        # - **RequestHeader**: Matches requests by HTTP header.
        # 
        # - **Query**: Matches requests by query string.
        # 
        # - **Method**: Matches requests by HTTP method.
        # 
        # - **Cookie**: Matches requests by cookie.
        # 
        # - **SourceIP**: Matches requests by source IP address.
        self.rule_condition_type = rule_condition_type
        # The value of the rule condition.
        # This is a JSON-formatted string whose structure depends on the specified **RuleConditionType**.
        # 
        # - If **RuleConditionType** is set to **Host**, this parameter specifies the domain name conditions. A forwarding rule can have only one **Host** rule condition. This rule condition can contain multiple domain names, which are evaluated with a logical OR. A domain name must be 3 to 128 characters long and can contain letters, digits, hyphens (-), and periods (.). You can use asterisks (\\*) and question marks (?) as wildcards. Example: `["www.example.com", "www.aliyun.com"]`.
        # 
        # - If **RuleConditionType** is set to **Path**, this parameter specifies the path conditions. A forwarding rule can have multiple **Path** rule conditions, which are evaluated with a logical OR. Each path rule condition can contain multiple paths, which are also evaluated with a logical OR. A path must be 1 to 128 characters long and must start with a forward slash (/). It can contain letters, digits, dollar signs ($), hyphens (-), underscores (_), periods (.), plus signs (+), forward slashes (/), ampersands (&), tildes (\\~), at signs (@), colons (:), and apostrophes (\\"). You can use asterisks (\\*) and question marks (?) as wildcards. Example: `["/a", "/b/"]`.
        # 
        # - If **RuleConditionType** is set to **RequestHeader**, this parameter specifies the HTTP header conditions. The value is a key-value pair. The header values within the same rule condition must be unique. Example: `[{"header1":["value1","value2"]}]`.
        # 
        #   - Key: The HTTP header key must be 1 to 40 characters long and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        #   - Value: The HTTP header value must be 1 to 128 characters long and contain only printable characters within the ASCII range of` ch >= 32 && ch < 127`. The value cannot start or end with a space.
        # 
        # - If **RuleConditionType** is set to **Query**, this parameter specifies the query string conditions. The value is a key-value pair. Example: `[{"query1":["value1"]}, {"query2":["value2"]}]`.
        # 
        #   - Key: The key must be 1 to 100 characters long and contain only printable characters within the ASCII range of` ch >= 32 && ch < 127`. Letters must be lowercase. Spaces and the following characters are not supported:` []{}<>\\;/?:@&=+,$%"^~`.
        # 
        #   - Value: The value must be 1 to 128 characters long and contain only printable characters within the ASCII range of` ch >= 32 && ch < 127`. Letters must be lowercase. Spaces and the following characters are not supported:` []{}<>\\;/?:@&=+,$%"^~`.
        # 
        # - If **RuleConditionType** is set to **Method**, this parameter specifies the HTTP method conditions. Valid values: **HEAD**, **GET**, **POST**, **OPTIONS**, **PUT**, **PATCH**, and **DELETE**. Example: `["GET", "OPTIONS", "POST"]`.
        # 
        # - If **RuleConditionType** is set to **Cookie**, this parameter specifies the cookie conditions. The value is a key-value pair. Example: `[{"cookie1":["value1"]}, {"cookie2":["value2"]}]`
        # 
        #   - Key: The cookie key must be 1 to 100 characters long and contain only printable characters within the ASCII range of` ch >= 32 && ch < 127`. Letters must be lowercase. Spaces and the following characters are not supported:` #[]{}\\<>&`.
        # 
        #   - Value: The cookie value must be 1 to 128 characters long and contain only printable characters within the ASCII range of` ch >= 32 && ch < 127`. Letters must be lowercase. Spaces and the following characters are not supported:` #[]{}\\<>&`.
        # 
        # - If **RuleConditionType** is set to **SourceIP**, this parameter specifies the source IP conditions. You can specify IP addresses, for example, `1.1.XX.XX/32`, or CIDR blocks, for example, `2.2.XX.XX/24`. A forwarding rule can have only one **SourceIP** rule condition. This rule condition can contain multiple source IP addresses, which are evaluated with a logical OR. Example: `["1.1.XX.XX/32", "2.2.XX.XX/24"]`.
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
            temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m.get('HostConfig'))

        if m.get('PathConfig') is not None:
            temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m.get('PathConfig'))

        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')

        if m.get('RuleConditionValue') is not None:
            self.rule_condition_value = m.get('RuleConditionValue')

        return self

class CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The path configuration.
        # 
        # A path must be 1 to 128 characters long and must start with a forward slash (/). It can contain letters, digits, dollar signs ($), hyphens (-), underscores (_), periods (.), plus signs (+), forward slashes (/), ampersands (&), tildes (\\~), at signs (@), colons (:), and apostrophes (\\"). You can use asterisks (\\*) and question marks (?) as wildcards.
        # 
        # > This parameter is deprecated. We recommend that you use **RuleConditionType** and **RuleConditionValue** to configure rule conditions.
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

class CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The domain name configuration.
        # 
        # > This parameter is deprecated. We recommend that you use **RuleConditionType** and **RuleConditionValue** to configure rule conditions.
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

class CreateForwardingRulesRequestForwardingRulesRuleActions(DaraModel):
    def __init__(
        self,
        forward_group_config: main_models.CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig = None,
        order: int = None,
        rule_action_type: str = None,
        rule_action_value: str = None,
    ):
        # The forwarding configuration.
        # 
        # > This parameter is deprecated. We recommend that you use **RuleActionType** and **RuleActionValue** to configure rule actions.
        self.forward_group_config = forward_group_config
        # The priority of the action.
        # 
        # > This parameter is not in use and can be ignored.
        # 
        # This parameter is required.
        self.order = order
        # The type of the rule action. Valid values:
        # 
        # - **ForwardGroup**: Forwards requests.
        # 
        # - **Redirect**: Redirects requests.
        # 
        # - **FixResponse**: Returns a fixed response.
        # 
        # - **Rewrite**: Rewrites requests.
        # 
        # - **AddHeader**: Adds a header.
        # 
        # - **RemoveHeader**: Removes a header.
        # 
        # - **Drop**: Drops requests.
        # 
        # This parameter is required.
        self.rule_action_type = rule_action_type
        # The value for the rule action.
        # 
        # This is a JSON-formatted string whose structure depends on the specified **RuleActionType**.
        # 
        # A forwarding rule can have at most one action of type **ForwardGroup**, **Redirect**, or **FixResponse**. Actions of type **Rewrite**, **AddHeader**, and **RemoveHeader** must be specified before a **ForwardGroup** action.
        # 
        # - If **RuleActionType** is set to **ForwardGroup**, this parameter specifies the endpoint group. You can forward requests to only one endpoint group. Example: `{"type":"endpointgroup", "value":"epg-bp1enpdcrqhl78g6r****"}`, where:
        # 
        #   - `type`: Set the value to` endpointgroup`.
        # 
        #   - `value`: The ID of the target endpoint group.
        # 
        # - If **RuleActionType** is set to **Redirect**, this parameter specifies the redirect configuration. At least one of the `protocol`, `domain`, `port`, `path`, or `query` fields must be set to a value other than its default. Example: `{"protocol":"HTTP", "domain":"www.example.com", "port":"80", "path":"/a","query":"value1", "code":"301" }`, where:
        # 
        #   - `protocol`: The protocol for the redirect. Valid values: `${protocol}` (default), `HTTP`, and `HTTPS`.
        # 
        #   - `domain`: The domain name for the redirect. The default value is `${host}`. You can also specify another domain name. A domain name must be 3 to 128 characters long and can contain only lowercase letters, digits, and the following special characters:` .-=~_-+/^*!$&()[]?`.
        # 
        #   - `port`: The port for the redirect. The default value is `${port}`. You can also specify a port number. Valid values: 1 to 63335.
        # 
        #   - `path`: The path for the redirect. The default value is `${path}`. The path must be 1 to 128 characters long. For a regular expression path, it must start with a tilde (\\~) and can contain uppercase and lowercase letters, digits, and the following special characters:` .-_/=?~^*$:()[]+`. For a non-regular expression path, it must start with a forward slash (/) and can contain uppercase and lowercase letters, digits, and the following special characters:` .-_/=:?`.
        # 
        #   - `query`: The query string for the redirect. The default value is `${query}`. You can also specify another query string. The query string must be 1 to 128 characters long and contain only printable characters within the ASCII range of` ch >= 32 && ch < 127`. Letters must be lowercase. Spaces and the following special characters are not supported:` []{}<>\\#&`.
        # 
        #   - `code`: The redirect code. Valid values: `301`, `302`, `303`, `307`, and `308`.
        # 
        # - If **RuleActionType** is set to **FixResponse**, this parameter specifies the fixed response configuration. Example: `{"code":"200", "type":"text/plain", "content":"dssacav" }`, where:
        # 
        #   - `code`: The response status code. The value must be a numeric string in the `2xx`, `4xx`, or `5xx` format, where `x` is any digit.
        # 
        #   - `type`: The content type of the response body. Valid values: **text/plain**, **text/css**, **text/html**, **application/javascript**, and **application/json**.
        # 
        #   - `content`: The content of the response body. The content cannot exceed 1,000 characters and does not support Chinese characters.
        # 
        # - If **RuleActionType** is set to **AddHeader**, this parameter specifies the configuration for adding an HTTP header. If a forwarding rule contains an **AddHeader** action, it must also contain a **ForwardGroup** action. Example: `[{"name":"header1","type":"user-defined", "value":"value"}]`, where:
        # 
        #   - `name`: The name of the HTTP header. The name must be 1 to 40 characters long and can contain uppercase and lowercase letters, digits, hyphens (-), and underscores (_). The header names in **AddHeader** actions must be unique and cannot be the same as any header name in a **RemoveHeader** action.
        # 
        #   - `type`: The type of the header value. Valid values: `user-defined`, `ref` (reference), and `system-defined`.
        # 
        #   - `value`: The content of the HTTP header. This field cannot be empty. If `type` is `user-defined`, the value must be 1 to 128 characters long and contain only printable characters within the ASCII range of `ch >= 32 && ch < 127`. The value can contain uppercase and lowercase letters, digits, hyphens (-), and underscores (_), and cannot start or end with a space. If `type` is `ref`, the value must be 1 to 128 characters long and can contain uppercase and lowercase letters, digits, hyphens (-), and underscores (_). The value cannot start or end with a space. If `type` is `system-defined`, the only valid value is `ClientSrcIp`.
        # 
        # - If **RuleActionType** is set to **RemoveHeader**, this parameter specifies the HTTP headers to remove. If a forwarding rule contains a **RemoveHeader** action, it must also contain a **ForwardGroup** action. The value must be 1 to 40 characters long and can contain uppercase and lowercase letters, digits, hyphens (-), and underscores (_). Example: `["header1"]`.
        # 
        # - If **RuleActionType** is set to **Rewrite**, this parameter specifies the rewrite configuration. If a forwarding rule contains a **Rewrite** action, it must also contain a **ForwardGroup** action. Example: `{"domain":"value1", "path":"value2", "query":"value3"}`, where:
        # 
        #   - `domain`: The domain name to rewrite. The default value is `${host}`. You can also specify another domain name. A domain name must be 3 to 128 characters long and can contain only lowercase letters, digits, and the following special characters:` .-=~_-+/^*!$&()[]?`.
        # 
        #   - `path`: The path to rewrite. The default value is `${path}`. The path must be 1 to 128 characters long. For a regular expression path, it must start with a tilde (\\~) and can contain uppercase and lowercase letters, digits, and the following special characters:` .-_/=?~^*$:()[]+`. For a non-regular expression path, it must start with a forward slash (/) and can contain uppercase and lowercase letters, digits, and the following special characters:` .-_/=:?`.
        # 
        #   - `query`: The query string to rewrite. The default value is `${query}`. You can also specify another query string. The query string must be 1 to 128 characters long and contain only printable characters within the ASCII range of` ch >= 32 && ch < 127`. Letters must be lowercase. Spaces and the following special characters are not supported:` []{}<>\\#&`.
        # 
        # - If **RuleActionType** is set to **Drop**, you do not need to specify a value for this parameter.
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
            temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m.get('ForwardGroupConfig'))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')

        if m.get('RuleActionValue') is not None:
            self.rule_action_value = m.get('RuleActionValue')

        return self

class CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_tuples: List[main_models.CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # The endpoint group configuration.
        # 
        # > This parameter is deprecated. We recommend that you use **RuleActionType** and **RuleActionValue** to configure rule actions.
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
                temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
    ):
        # The ID of the endpoint group.
        # 
        # > This parameter is deprecated. We recommend that you use **RuleActionType** and **RuleActionValue** to configure rule actions.
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


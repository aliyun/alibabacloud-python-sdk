# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListForwardingRulesResponseBody(DaraModel):
    def __init__(
        self,
        forwarding_rules: List[main_models.ListForwardingRulesResponseBodyForwardingRules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The forwarding rules.
        self.forwarding_rules = forwarding_rules
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If **NextToken** is not returned, it indicates that no additional results exist.
        # *   If **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

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
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k1 in self.forwarding_rules:
                result['ForwardingRules'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k1 in m.get('ForwardingRules'):
                temp_model = main_models.ListForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListForwardingRulesResponseBodyForwardingRules(DaraModel):
    def __init__(
        self,
        forwarding_rule_direction: str = None,
        forwarding_rule_id: str = None,
        forwarding_rule_name: str = None,
        forwarding_rule_status: str = None,
        listener_id: str = None,
        priority: int = None,
        rule_actions: List[main_models.ListForwardingRulesResponseBodyForwardingRulesRuleActions] = None,
        rule_conditions: List[main_models.ListForwardingRulesResponseBodyForwardingRulesRuleConditions] = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.ListForwardingRulesResponseBodyForwardingRulesServiceManagedInfos] = None,
    ):
        # The direction in which the forwarding rule takes effect.
        # 
        # By default, **request** is returned, which indicates that the forwarding rule takes effect on requests.
        self.forwarding_rule_direction = forwarding_rule_direction
        # The forwarding rule ID.
        self.forwarding_rule_id = forwarding_rule_id
        # The forwarding rule name.
        self.forwarding_rule_name = forwarding_rule_name
        # The state of the forwarding rule. Valid values:
        # 
        # *   **active:** The forwarding rule is normal.
        # *   **configuring:** The forwarding rule is being modified.
        # *   **deleting:** The forwarding rule is being deleted.
        self.forwarding_rule_status = forwarding_rule_status
        # The listener ID.
        self.listener_id = listener_id
        # The priority of the forwarding rule.
        # 
        # A value between **1** and **10000** is returned. A smaller value indicates a higher priority.
        self.priority = priority
        # The forwarding actions.
        self.rule_actions = rule_actions
        # The conditions that trigger the forwarding rule.
        self.rule_conditions = rule_conditions
        # The ID of the service that manages the instance.
        # 
        # >  This parameter is returned only if the value of **ServiceManaged** is **true**.
        self.service_id = service_id
        # Indicates whether the GA instance is managed. Valid values:
        # 
        # *   **true**: The GA instance is managed.
        # *   **false**: The GA instance is not managed.
        self.service_managed = service_managed
        # The actions that you can perform on the managed instance.
        # 
        # >  This parameter takes effect only if **ServiceManaged** is set to **True**.
        # 
        # *   You can perform only specific actions on the managed instance.
        self.service_managed_infos = service_managed_infos

    def validate(self):
        if self.rule_actions:
            for v1 in self.rule_actions:
                 if v1:
                    v1.validate()
        if self.rule_conditions:
            for v1 in self.rule_conditions:
                 if v1:
                    v1.validate()
        if self.service_managed_infos:
            for v1 in self.service_managed_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forwarding_rule_direction is not None:
            result['ForwardingRuleDirection'] = self.forwarding_rule_direction

        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id

        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name

        if self.forwarding_rule_status is not None:
            result['ForwardingRuleStatus'] = self.forwarding_rule_status

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

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

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        result['ServiceManagedInfos'] = []
        if self.service_managed_infos is not None:
            for k1 in self.service_managed_infos:
                result['ServiceManagedInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardingRuleDirection') is not None:
            self.forwarding_rule_direction = m.get('ForwardingRuleDirection')

        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')

        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')

        if m.get('ForwardingRuleStatus') is not None:
            self.forwarding_rule_status = m.get('ForwardingRuleStatus')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k1 in m.get('RuleActions'):
                temp_model = main_models.ListForwardingRulesResponseBodyForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.ListForwardingRulesResponseBodyForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.ListForwardingRulesResponseBodyForwardingRulesServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        return self

class ListForwardingRulesResponseBodyForwardingRulesServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # The name of the action that you can perform on the managed instance. Valid values:
        # 
        # *   **Create**: Create an instance.
        # *   **Update**: Update the current instance.
        # *   **Delete**: Delete the current instance.
        # *   **Associate**: Reference the current instance.
        # *   **UserUnmanaged**: Unmanage the instance.
        # *   **CreateChild**: Create a child resource on the current instance.
        self.action = action
        # The type of the child resource. Valid values:
        # 
        # *   **Listener**: listener.
        # *   **IpSet**: acceleration region.
        # *   **EndpointGroup**: endpoint group.
        # *   **ForwardingRule**: forwarding rule.
        # *   **Endpoint**: endpoint.
        # *   **EndpointGroupDestination**: the protocol mapping of an endpoint group associated with a custom routing listener.
        # *   **EndpointPolicy**: the traffic policy of an endpoint associated with a custom routing listener.
        # 
        # >  This parameter is returned only if the value of **Action** is **CreateChild**.
        self.child_type = child_type
        # Indicates whether the specified actions are managed. Valid values:
        # 
        # *   **true**: The specified actions are managed, and users cannot perform the specified actions on the managed instance.
        # *   **false**: The specified actions are not managed, and users can perform the specified actions on the managed instance.
        self.is_managed = is_managed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.child_type is not None:
            result['ChildType'] = self.child_type

        if self.is_managed is not None:
            result['IsManaged'] = self.is_managed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ChildType') is not None:
            self.child_type = m.get('ChildType')

        if m.get('IsManaged') is not None:
            self.is_managed = m.get('IsManaged')

        return self

class ListForwardingRulesResponseBodyForwardingRulesRuleConditions(DaraModel):
    def __init__(
        self,
        host_config: main_models.ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig = None,
        path_config: main_models.ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig = None,
        rule_condition_type: str = None,
        rule_condition_value: str = None,
    ):
        # The domain name configuration.
        # 
        # >  GA instances created after July 12, 2022 support all forwarding condition types and action types. We recommend that you query forwarding conditions and actions by calling the **RuleActionType** and **RuleActionValue** operations.
        self.host_config = host_config
        # The path configuration.
        # 
        # >  GA instances created after July 12, 2022 support all forwarding condition types and action types. We recommend that you query forwarding conditions and actions by calling the **RuleActionType** and **RuleActionValue** operations.
        self.path_config = path_config
        # The type of the forwarding condition. Valid values:
        # 
        # *   **Host:** domain name.
        # *   **Path:** path.
        # *   **RequestHeader:** HTTP header.
        # *   **Query:** query string.
        # *   **Method:** HTTP method.
        # *   **Cookie:** cookie.
        # *   **SourceIP:** source IP address.
        self.rule_condition_type = rule_condition_type
        # The value of the forwarding condition type.
        # 
        # Different JSON strings are returned based on the value of the **RuleConditionType** parameter.
        # 
        # *   If you set **RuleConditionType** to **Host**, a domain name condition is returned. If multiple domain names are returned in a forwarding condition, the relationship between the domain names is OR.
        # *   If you set **RuleConditionType** to **Path**, a path condition is returned. If multiple forwarding conditions of the path type are returned in a forwarding rule, the relationship between the forwarding conditions is OR. If multiple paths are returned in a forwarding condition, the relationship between the paths is OR.
        # *   If you set **RuleConditionType** to **RequestHeader**, an HTTP header condition that consists of key-value pairs is returned.
        # *   If you set **RuleConditionType** to **Query**, a query string condition that consists of key-value pairs is returned.
        # *   If you set **RuleConditionType** to **Method**, an HTTP method condition is returned.
        # *   If you set **RuleConditionType** to **Cookie**, a cookie condition that consists of key-value pairs is returned.
        # *   If you set **RuleConditionType** to **SourceIP**, a source IP address condition is returned. If multiple source IP addresses are returned in a forwarding condition, the relationship between the source IP addresses is OR.
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
            temp_model = main_models.ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m.get('HostConfig'))

        if m.get('PathConfig') is not None:
            temp_model = main_models.ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m.get('PathConfig'))

        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')

        if m.get('RuleConditionValue') is not None:
            self.rule_condition_value = m.get('RuleConditionValue')

        return self

class ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The path configuration.
        # 
        # >  GA instances created after July 12, 2022 support all forwarding condition types and action types. We recommend that you query forwarding conditions and actions by calling the **RuleActionType** and **RuleActionValue** operations.
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

class ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The domain name configuration.
        # 
        # >  GA instances created after July 12, 2022 support all forwarding condition types and action types. We recommend that you query forwarding conditions and actions by calling the **RuleActionType** and **RuleActionValue** operations.
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

class ListForwardingRulesResponseBodyForwardingRulesRuleActions(DaraModel):
    def __init__(
        self,
        forward_group_config: main_models.ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig = None,
        order: int = None,
        rule_action_type: str = None,
        rule_action_value: str = None,
    ):
        # The forwarding action configuration.
        # 
        # >  GA instances created after July 12, 2022 support all forwarding condition types and action types. We recommend that you query forwarding conditions and actions by calling the **RuleActionType** and **RuleActionValue** operations.
        self.forward_group_config = forward_group_config
        # The forwarding priority.
        # 
        # >  This parameter does not take effect.
        self.order = order
        # The type of the forwarding action. Valid values:
        # 
        # *   **ForwardGroup**: forwards a request.
        # *   **Redirect**: redirects a request.
        # *   **FixResponse**: returns a fixed response.
        # *   **Rewrite**: rewrites a request.
        # *   **AddHeader**: adds a header to a request.
        # *   **RemoveHeaderConfig**: deletes the header from a request.
        # *   **Drop**: drops a request.
        self.rule_action_type = rule_action_type
        # The value of the forwarding action.
        # 
        # Different JSON strings are returned based on the value of **RuleActionType**.
        # 
        # *   If you set **RuleActionType** to **ForwardGroup**, the information about a virtual endpoint group is returned. The following section describes the parameters:
        # 
        #     *   `type`: `endpointgroup` is returned.
        #     *   `value`: the ID of the virtual endpoint group.
        # 
        # *   If you set **RuleActionType** to **Redirect**, the redirecting configuration is returned. The following section describes the parameters:
        # 
        #     *   `protocol`: the protocol of requests after the requests are redirected.
        #     *   `domain`: the domain name to which requests are redirected.
        #     *   `port`: the port to which requests are redirected.
        #     *   `path`: the path to which requests are redirected.
        #     *   `query`: the query string of the requests that are redirected.
        #     *   `code`: the redirecting code.
        # 
        # *   If you set **RuleActionType** to **FixResponse**, the information about the fixed response that you configured is returned. The following section describes the parameters:
        # 
        #     *   `code`: the HTTP status code.
        #     *   `type`: the content type of the response.
        #     *   `content`: the content of the response.
        # 
        # *   If **RuleActionType** is set to **AddHeader**, the information about the HTTP header that is added is returned. The following section describes the parameters:
        # 
        #     *   `name`: the name of the HTTP header.
        #     *   `type`: the content type of the HTTP header.
        #     *   `value`: the content of the HTTP header.
        # 
        # *   If you set **RuleActionType** to **RemoveHeader**, the information about the HTTP header that is deleted is returned.
        # 
        # *   If you set **RuleActionType** to **Rewrite**, the rewriting configuration is returned. The following section describes the parameters:
        # 
        #     *   `domain`: the domain name to which requests are redirected.
        #     *   `path`: the path to which requests are redirected.
        #     *   `query`: the query string of the requests that are redirected.
        # 
        # *   If you set **RuleActionType** to **Drop**, an empty string is returned.
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
            temp_model = main_models.ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m.get('ForwardGroupConfig'))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')

        if m.get('RuleActionValue') is not None:
            self.rule_action_value = m.get('RuleActionValue')

        return self

class ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_tuples: List[main_models.ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # The information about the endpoint groups.
        # 
        # >  GA instances created after July 12, 2022 support all forwarding condition types and action types. We recommend that you query forwarding conditions and actions by calling the **RuleActionType** and **RuleActionValue** operations.
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
                temp_model = main_models.ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
    ):
        # The endpoint group ID.
        # 
        # >  GA instances created after July 12, 2022 support all forwarding condition types and action types. We recommend that you query forwarding conditions and actions by calling the **RuleActionType** and **RuleActionValue** operations.
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


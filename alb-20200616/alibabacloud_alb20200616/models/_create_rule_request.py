# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class CreateRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        direction: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        priority: int = None,
        rule_actions: List[main_models.CreateRuleRequestRuleActions] = None,
        rule_conditions: List[main_models.CreateRuleRequestRuleConditions] = None,
        rule_name: str = None,
        tag: List[main_models.CreateRuleRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The direction to which the forwarding rule is applied. Valid values:
        # 
        # *   **Request** (default): The forwarding rule is applied to the requests received by ALB.
        # *   **Response**: The forwarding rule is applied to the responses returned by backend servers.
        # 
        # > Basic ALB instances do not support the **Response** value.
        self.direction = direction
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a `2xx HTTP` status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The listener ID of the ALB instance.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The priority of the forwarding rule. Valid values: **1 to 10000**. A smaller value indicates a higher priority.
        # 
        # > The priorities of the forwarding rules created for the same listener must be unique.
        # 
        # This parameter is required.
        self.priority = priority
        # The actions of the forwarding rule.
        # 
        # This parameter is required.
        self.rule_actions = rule_actions
        # The match conditions of the forwarding rule.
        # 
        # This parameter is required.
        self.rule_conditions = rule_conditions
        # The name of the forwarding rule.
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   It can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The tags.
        self.tag = tag

    def validate(self):
        if self.rule_actions:
            for v1 in self.rule_actions:
                 if v1:
                    v1.validate()
        if self.rule_conditions:
            for v1 in self.rule_conditions:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k1 in m.get('RuleActions'):
                temp_model = main_models.CreateRuleRequestRuleActions()
                self.rule_actions.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.CreateRuleRequestRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateRuleRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateRuleRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        self.key = key
        # The tag value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
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

class CreateRuleRequestRuleConditions(DaraModel):
    def __init__(
        self,
        cookie_config: main_models.CreateRuleRequestRuleConditionsCookieConfig = None,
        header_config: main_models.CreateRuleRequestRuleConditionsHeaderConfig = None,
        host_config: main_models.CreateRuleRequestRuleConditionsHostConfig = None,
        method_config: main_models.CreateRuleRequestRuleConditionsMethodConfig = None,
        path_config: main_models.CreateRuleRequestRuleConditionsPathConfig = None,
        query_string_config: main_models.CreateRuleRequestRuleConditionsQueryStringConfig = None,
        response_header_config: main_models.CreateRuleRequestRuleConditionsResponseHeaderConfig = None,
        response_status_code_config: main_models.CreateRuleRequestRuleConditionsResponseStatusCodeConfig = None,
        source_ip_config: main_models.CreateRuleRequestRuleConditionsSourceIpConfig = None,
        type: str = None,
    ):
        # The key-value pairs of the cookie.
        self.cookie_config = cookie_config
        # The configuration of the header.
        self.header_config = header_config
        # The configuration of the host.
        self.host_config = host_config
        # The configurations of the request method.
        self.method_config = method_config
        # The configurations of the URL to which requests are forwarded.
        self.path_config = path_config
        # The configuration of the query strings.
        self.query_string_config = query_string_config
        # The configuration of headers.
        self.response_header_config = response_header_config
        # The configuration of the response status codes.
        self.response_status_code_config = response_status_code_config
        # Configuration of traffic matching based on source IP addresses. This parameter is required and valid when **Type** is set to **SourceIP**.
        self.source_ip_config = source_ip_config
        # The type of forwarding rule. Valid values:
        # 
        # *   **Host**: Requests are distributed based on hosts.
        # *   **Path**: Requests are distributed based on paths.
        # *   **Header**: Requests are distributed based on HTTP headers.
        # *   **QueryString**: Requests are distributed based on query strings.
        # *   **Method**: Requests are distributed based on request methods.
        # *   **Cookie**: Requests are distributed based on cookies.
        # *   **SourceIp**: Requests are forwarded based on source IP addresses.
        # *   **ResponseHeader**: Requests are forwarded based on HTTP response headers.
        # *   **ResponseStatusCode**: Requests are forwarded based on response status codes.
        # 
        # This parameter is required.
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
            temp_model = main_models.CreateRuleRequestRuleConditionsCookieConfig()
            self.cookie_config = temp_model.from_map(m.get('CookieConfig'))

        if m.get('HeaderConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleConditionsHeaderConfig()
            self.header_config = temp_model.from_map(m.get('HeaderConfig'))

        if m.get('HostConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m.get('HostConfig'))

        if m.get('MethodConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleConditionsMethodConfig()
            self.method_config = temp_model.from_map(m.get('MethodConfig'))

        if m.get('PathConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m.get('PathConfig'))

        if m.get('QueryStringConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleConditionsQueryStringConfig()
            self.query_string_config = temp_model.from_map(m.get('QueryStringConfig'))

        if m.get('ResponseHeaderConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleConditionsResponseHeaderConfig()
            self.response_header_config = temp_model.from_map(m.get('ResponseHeaderConfig'))

        if m.get('ResponseStatusCodeConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleConditionsResponseStatusCodeConfig()
            self.response_status_code_config = temp_model.from_map(m.get('ResponseStatusCodeConfig'))

        if m.get('SourceIpConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleConditionsSourceIpConfig()
            self.source_ip_config = temp_model.from_map(m.get('SourceIpConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateRuleRequestRuleConditionsSourceIpConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The source IP addresses used for traffic matching.
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

class CreateRuleRequestRuleConditionsResponseStatusCodeConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The response status codes.
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

class CreateRuleRequestRuleConditionsResponseHeaderConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The header key.
        # 
        # *   The key must be 1 to 40 characters in length.
        # *   It can contain letters, digits, hyphens (-), and underscores (_).
        # *   Cookie and Host are not supported.
        self.key = key
        # The header values.
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

class CreateRuleRequestRuleConditionsQueryStringConfig(DaraModel):
    def __init__(
        self,
        values: List[main_models.CreateRuleRequestRuleConditionsQueryStringConfigValues] = None,
    ):
        # The query strings.
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
                temp_model = main_models.CreateRuleRequestRuleConditionsQueryStringConfigValues()
                self.values.append(temp_model.from_map(k1))

        return self

class CreateRuleRequestRuleConditionsQueryStringConfigValues(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # They key of the query string.
        # 
        # *   The key must be 1 to 100 characters in length.
        # *   You can use asterisks (\\*) and question marks (?) as wildcard characters. It can contain printable characters, excluding uppercase letters, space characters, and the following special characters: `# [ ] { } \\ | < > & "`.
        self.key = key
        # The value of the query string.
        # 
        # *   The value must be 1 to 128 characters in length.
        # *   It can contain printable characters, but cannot contain uppercase letters, space characters, or the following special characters: `# [ ] { } \\ | < > &`. You can use asterisks (\\*) and question marks (?) as wildcard characters.
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

class CreateRuleRequestRuleConditionsPathConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The forwarding URLs.
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

class CreateRuleRequestRuleConditionsMethodConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The request methods.
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

class CreateRuleRequestRuleConditionsHostConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # The hostnames.
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

class CreateRuleRequestRuleConditionsHeaderConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The header key.
        # 
        # *   The header key must be 1 to 40 characters in length.
        # *   The key can contain letters, digits, hyphens (-), and underscores (_).
        # *   Cookie and Host are not supported.
        self.key = key
        # The header values.
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

class CreateRuleRequestRuleConditionsCookieConfig(DaraModel):
    def __init__(
        self,
        values: List[main_models.CreateRuleRequestRuleConditionsCookieConfigValues] = None,
    ):
        # The cookie values.
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
                temp_model = main_models.CreateRuleRequestRuleConditionsCookieConfigValues()
                self.values.append(temp_model.from_map(k1))

        return self

class CreateRuleRequestRuleConditionsCookieConfigValues(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The cookie key.
        # 
        # *   The cookie key must be 1 to 100 characters in length.
        # *   You can use asterisks (\\*) and question marks (?) as wildcard characters.
        # *   The value can contain printable characters, excluding uppercase letters, space characters, and the following special characters: `; # [ ] { } \\ | < > & "`.
        self.key = key
        # The cookie value.
        # 
        # *   The cookie value must be 1 to 100 characters in length.
        # *   You can use asterisks (\\*) and question marks (?) as wildcard characters.
        # *   The value can contain printable characters, excluding uppercase letters, space characters, and the following special characters: `; # [ ] { } \\ | < > & "`.
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

class CreateRuleRequestRuleActions(DaraModel):
    def __init__(
        self,
        cors_config: main_models.CreateRuleRequestRuleActionsCorsConfig = None,
        fixed_response_config: main_models.CreateRuleRequestRuleActionsFixedResponseConfig = None,
        forward_group_config: main_models.CreateRuleRequestRuleActionsForwardGroupConfig = None,
        insert_header_config: main_models.CreateRuleRequestRuleActionsInsertHeaderConfig = None,
        order: int = None,
        redirect_config: main_models.CreateRuleRequestRuleActionsRedirectConfig = None,
        remove_header_config: main_models.CreateRuleRequestRuleActionsRemoveHeaderConfig = None,
        rewrite_config: main_models.CreateRuleRequestRuleActionsRewriteConfig = None,
        traffic_limit_config: main_models.CreateRuleRequestRuleActionsTrafficLimitConfig = None,
        traffic_mirror_config: main_models.CreateRuleRequestRuleActionsTrafficMirrorConfig = None,
        type: str = None,
    ):
        # Request forwarding based on CORS.
        self.cors_config = cors_config
        # The configuration of the custom response.
        self.fixed_response_config = fixed_response_config
        # The server groups to which requests are forwarded. You can specify at most five server groups for each forwarding rule.
        self.forward_group_config = forward_group_config
        # The key of the header to be inserted.
        self.insert_header_config = insert_header_config
        # The priority of the action. Valid values: **1 to 50000**. A smaller value indicates a higher priority. The actions of a forwarding rule are applied in descending order of priority. This parameter cannot empty. The priority of each action within a forwarding rule must be unique.
        # 
        # This parameter is required.
        self.order = order
        # The configuration of the redirect action.
        # 
        # >  Do not set all fields in **RedirectConfig** to default values, except for **httpCode**.
        self.redirect_config = redirect_config
        # The HTTP headers to be removed.
        self.remove_header_config = remove_header_config
        # The configuration of the rewrite action.
        # 
        # >  If you specify multiple actions for a forwarding rule, you must configure the **ForwardGroup** parameter for the **RewriteConfig** action.
        self.rewrite_config = rewrite_config
        # The configuration of the traffic throttling action.
        self.traffic_limit_config = traffic_limit_config
        # The configuration of the traffic mirroring action.
        self.traffic_mirror_config = traffic_mirror_config
        # The action. Valid values:
        # 
        # *   **ForwardGroup**: distributes requests to multiple vServer groups.
        # *   **Redirect**: redirects requests.
        # *   **FixedResponse**: returns a custom response.
        # *   **Rewrite**: rewrites requests.
        # *   **InsertHeader**: inserts headers.
        # *   **RemoveHeaderConfig:** deletes the header of a request.
        # *   **TrafficLimit**: throttles traffic.
        # *   **TrafficMirror**: mirrors network traffic.
        # *   **Cors**: enables cross-origin resource sharing (CORS).
        # 
        # The following action types are supported:
        # 
        # *   **FinalType**: Each forwarding rule can contain only one FinalType action, which is performed at the end. You can specify only one of **ForwardGroup**, **Redirect**, and **FixedResponse**.
        # *   **ExtType**: Each forwarding rule can contain one or more **ExtType** actions, which are performed before the **FinalType** action. If you want to specify an ExtType action, you must also specify a **FinalType** action. You can specify multiple **InsertHeader** actions or one **Rewrite** action.
        # 
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
            temp_model = main_models.CreateRuleRequestRuleActionsCorsConfig()
            self.cors_config = temp_model.from_map(m.get('CorsConfig'))

        if m.get('FixedResponseConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleActionsFixedResponseConfig()
            self.fixed_response_config = temp_model.from_map(m.get('FixedResponseConfig'))

        if m.get('ForwardGroupConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m.get('ForwardGroupConfig'))

        if m.get('InsertHeaderConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleActionsInsertHeaderConfig()
            self.insert_header_config = temp_model.from_map(m.get('InsertHeaderConfig'))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('RedirectConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleActionsRedirectConfig()
            self.redirect_config = temp_model.from_map(m.get('RedirectConfig'))

        if m.get('RemoveHeaderConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleActionsRemoveHeaderConfig()
            self.remove_header_config = temp_model.from_map(m.get('RemoveHeaderConfig'))

        if m.get('RewriteConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleActionsRewriteConfig()
            self.rewrite_config = temp_model.from_map(m.get('RewriteConfig'))

        if m.get('TrafficLimitConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleActionsTrafficLimitConfig()
            self.traffic_limit_config = temp_model.from_map(m.get('TrafficLimitConfig'))

        if m.get('TrafficMirrorConfig') is not None:
            temp_model = main_models.CreateRuleRequestRuleActionsTrafficMirrorConfig()
            self.traffic_mirror_config = temp_model.from_map(m.get('TrafficMirrorConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateRuleRequestRuleActionsTrafficMirrorConfig(DaraModel):
    def __init__(
        self,
        mirror_group_config: main_models.CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig = None,
        target_type: str = None,
    ):
        # The configuration of the server group to which traffic is mirrored.
        self.mirror_group_config = mirror_group_config
        # The type of destination to which network traffic is mirrored. Valid values:
        # 
        # *   **ForwardGroupMirror**: a server group.
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
            temp_model = main_models.CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig()
            self.mirror_group_config = temp_model.from_map(m.get('MirrorGroupConfig'))

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_tuples: List[main_models.CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples] = None,
    ):
        # The configuration of the server group to which traffic is mirrored.
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
                temp_model = main_models.CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class CreateRuleRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # The server group ID.
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

class CreateRuleRequestRuleActionsTrafficLimitConfig(DaraModel):
    def __init__(
        self,
        per_ip_qps: int = None,
        qps: int = None,
    ):
        # The number of requests per IP address. Value values: **1 to 1000000**.
        # 
        # >  If both the **QPS** and **PerIpQps** parameters are specified, the value of the **QPS** parameter is smaller than the value of the PerIpQps parameter.
        self.per_ip_qps = per_ip_qps
        # The queries per second (QPS). Valid values: **1 to 1000000**.
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

class CreateRuleRequestRuleActionsRewriteConfig(DaraModel):
    def __init__(
        self,
        host: str = None,
        path: str = None,
        query: str = None,
    ):
        # The hostname to which requests are redirected. Valid values:
        # 
        # *   **${host}** (default): If you set the value to ${host}, you cannot append other characters.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The hostname must be 3 to 128 characters in length, and can contain lowercase letters, digits, and the following characters: - . \\* = ~ _ + \\ ^ ! $ & | ( ) [ ] ?.
        #     *   The hostname must contain at least one period (.) but cannot start or end with a period (.).
        #     *   The rightmost domain label can contain only letters and wildcard characters, and cannot contain digits or hyphens (-). The leftmost `domain label` can be an asterisk (\\*).
        #     *   The domain labels cannot start or end with hyphens (-). You can use asterisks (\\*) and question marks (?) anywhere in a domain label as wildcard characters.
        self.host = host
        # The URL to which requests are redirected. Valid values:
        # 
        # *   Default value: **${path}**. **${host}**, **${protocol}**, and **${port}** are also supported. Each variable can be specified only once. You can specify one or more of the preceding variables in each request. You can also combine them with a custom value.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The URL must be 1 to 128 characters in length, and is case-sensitive. You can use asterisks (\\*) and question marks (?) as wildcard characters.
        #     *   The URL must start with a forward slash (/) and can contain letters, digits, and the following special characters: `$ - _ . + / & ~ @ : \\" * ?`. It cannot contain the following special characters: `% # ; ! ( ) [ ] ^ , \\ "`. You can use asterisks (\\*) and question marks (?) as wildcard characters.
        self.path = path
        # The query string of the URL to which requests are distributed.
        # 
        # *   Default value: **${query}**. **${host}**, **${protocol}**, and **${port}** are also supported. Each variable can be specified only once. The preceding variables can be used at the same time or combined with a custom value.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The path must be 1 to 128 characters in length.
        #     *   It can contain printable characters, excluding space characters, the special characters `# [ ] { } \\ | < > "` and lowercase letters.
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

class CreateRuleRequestRuleActionsRemoveHeaderConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
    ):
        # The keys of the headers to be removed. The header keys must be 1 to 40 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The header keys specified in RemoveHeader must be unique.
        # 
        # *   If Direction is set to Request, the following request headers cannot be removed: `slb-id`, `slb-ip`, `x-forwarded-for`, `x-forwarded-proto`, `x-forwarded-eip`, `x-forwarded-port`, `x-forwarded-client-srcport`, `connection`, `upgrade`, `content-length`, `transfer-encoding`, `keep-alive`, `te`, `host`, `cookie`, `remoteip`, `authority`, and `x-forwarded-host`. Request headers are not case-sensitive.
        # *   If Direction is set to Response, the following response header keys are not supported: `connection`, `upgrade`, `content-length`, and `transfer-encoding`. The header keys are not case-sensitive.
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

class CreateRuleRequestRuleActionsRedirectConfig(DaraModel):
    def __init__(
        self,
        host: str = None,
        http_code: str = None,
        path: str = None,
        port: str = None,
        protocol: str = None,
        query: str = None,
    ):
        # The hostname to which requests are forwarded. Valid values:
        # 
        # *   **${host}** (default): If you set the value to ${host}, you cannot append other characters.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The hostname must be 3 to 128 characters in length, and can contain lowercase letters, digits, and the following characters: - . \\* = ~ _ + \\ ^ ! $ & | ( ) [ ] ?.
        #     *   The hostname must contain at least one period (.) but cannot start or end with a period (.).
        #     *   The rightmost domain label can contain only letters and wildcard characters, and cannot contain digits or hyphens (-). The leftmost `domain label` can be an asterisk (\\*).
        #     *   The domain labels cannot start or end with hyphens (-).
        #     *   You can use asterisks (\\*) and question marks (?) anywhere in a domain label as wildcard characters.
        self.host = host
        # The HTTP status code that indicates the redirect type. Valid values: **301**, **302**, **303**, **307**, and **308**.
        self.http_code = http_code
        # The URL to which requests are redirected. Valid values:
        # 
        # *   Default value: **${path}**. **${host}**, **${protocol}**, and **${port}** are also supported. Each variable can be specified only once. You can specify one or more of the preceding variables in each request. You can also combine them with a custom value.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The URL must be 1 to 128 characters in length, and is case-sensitive. You can use asterisks (\\*) and question marks (?) as wildcard characters.
        #     *   The URL must start with a forward slash (/) and can contain letters, digits, and the following special characters: `$ - _ . + / & ~ @ : \\" * ?`. It cannot contain the following special characters: `% # ; ! ( ) [ ] ^ , \\ "`. You can use asterisks (\\*) and question marks (?) as wildcard characters.
        self.path = path
        # The port to which requests are distributed.
        # 
        # *   **${port}** (default): If you set the value to ${port}, you cannot append other characters to the value.
        # *   You can also enter a port number. Valid values: **1 to 63335**.
        self.port = port
        # The redirect protocol. Valid values:
        # 
        # *   **${protocol}** (default): If you set the value to ${protocol}, you cannot modify the value or append other characters.
        # *   **HTTP**
        # *   **HTTPS**
        # 
        # > *   HTTPS listeners support only HTTPS redirection.
        # >*   HTTP listeners support HTTP and HTTPS redirection.
        self.protocol = protocol
        # The query string to which requests are redirected.
        # 
        # *   Default value: **${query}**. **${host}**, **${protocol}**, and **${port}** are also supported. Each variable can be specified only once. You can specify one or more of the preceding variables in each request. You can also combine them with a custom value.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The query string must be 1 to 128 characters in length.
        #     *   It can contain printable characters, excluding space characters, the special characters `# [ ] { } \\ | < > "`, and lowercase letters.
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

class CreateRuleRequestRuleActionsInsertHeaderConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # The key of the header. The header key must be 1 to 40 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The header keys specified by **InsertHeaderConfig** must be unique.
        # 
        # >  You cannot specify the following header keys: `slb-id`, `slb-ip`, `x-forwarded-for`, `x-forwarded-proto`, `x-forwarded-eip`, `x-forwarded-port`, `x-forwarded-client-srcport`, `connection`, `upgrade`, `content-length`, `transfer-encoding`, `keep-alive`, `te`, `host`, `cookie`, `remoteip`, `authority`, and `x-forwarded-host`. The header keys are case-insensitive.
        self.key = key
        # The value of the header to be inserted.
        # 
        # *   If **ValueType** is set to **SystemDefined**, you can set the Value parameter to one of the following values:
        # 
        #     *   **ClientSrcPort**: the client port.
        #     *   **ClientSrcIp**: the IP address of the client.
        #     *   **Protocol**: the request protocol (HTTP or HTTPS).
        #     *   **SLBId**: the ID of the ALB instance.
        #     *   **SLBPort**: the listener port.
        # 
        # *   If **ValueType** is set to **UserDefined**, a custom header value is supported. The header value must be 1 to 128 characters in length, and can contain printable characters whose ASCII values are `greater than or equal to 32 and lower than 127`. You can use asterisks (\\*) and question marks (?) as wildcard characters. `Quotation marks (")` are not supported. The header value cannot start or end with a space character, or end with a backslash (`\\`).
        # 
        # *   If **ValueType** is set to **ReferenceHeader**, you can reference a value from request headers. The value must be 1 to 128 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores (_).
        self.value = value
        # The type of the header. Valid values:
        # 
        # *   **UserDefined**: a custom header value.
        # *   **ReferenceHeader**: a header value that is referenced from one of the request headers.
        # *   **SystemDefined**: a header predefined by the system.
        self.value_type = value_type

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

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class CreateRuleRequestRuleActionsForwardGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_sticky_session: main_models.CreateRuleRequestRuleActionsForwardGroupConfigServerGroupStickySession = None,
        server_group_tuples: List[main_models.CreateRuleRequestRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # The configuration of session persistence for the server groups.
        self.server_group_sticky_session = server_group_sticky_session
        # The server groups to which requests are forwarded. You can specify at most five server groups for each forwarding rule.
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
            temp_model = main_models.CreateRuleRequestRuleActionsForwardGroupConfigServerGroupStickySession()
            self.server_group_sticky_session = temp_model.from_map(m.get('ServerGroupStickySession'))

        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k1 in m.get('ServerGroupTuples'):
                temp_model = main_models.CreateRuleRequestRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class CreateRuleRequestRuleActionsForwardGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        server_group_id: str = None,
        weight: int = None,
    ):
        # The server group to which requests are forwarded.
        self.server_group_id = server_group_id
        # The weight of the server group. A larger value specifies a higher weight. A server group with a higher weight receives more requests. Valid values: **0** to **100**.
        # 
        # *   If the number of destination server groups is 1, the default weight of the server group is **100**, unless you specify a weight.
        # *   If the number of destination server groups is larger than 1, you must specify a weight.
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

class CreateRuleRequestRuleActionsForwardGroupConfigServerGroupStickySession(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        timeout: int = None,
    ):
        # Specifies whether to enable session persistence. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.enabled = enabled
        # The timeout period of sessions. Unit: seconds. Valid values: **1** to **86400**. Default value: **1000**.
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

class CreateRuleRequestRuleActionsFixedResponseConfig(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        http_code: str = None,
    ):
        # The content of the custom response. The content cannot exceed 1 KB in size, and can contain only ASCII characters.
        self.content = content
        # The format of the response.
        # 
        # Valid values: **text/plain**, **text/css**, **text/html**, **application/javascript**, and **application/json**.
        self.content_type = content_type
        # The HTTP status code in responses. Valid values: **2xx**, **4xx**, **5xx**. The value must be a numeric string. **x** must be a digit.
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

class CreateRuleRequestRuleActionsCorsConfig(DaraModel):
    def __init__(
        self,
        allow_credentials: str = None,
        allow_headers: List[str] = None,
        allow_methods: List[str] = None,
        allow_origin: List[str] = None,
        expose_headers: List[str] = None,
        max_age: int = None,
    ):
        # Specifies whether credentials can be carried in CORS requests. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.allow_credentials = allow_credentials
        # The trusted headers of CORS requests.
        self.allow_headers = allow_headers
        # The allowed HTTP methods of CORS requests.
        self.allow_methods = allow_methods
        # The trusted origins of CORS requests. You can specify one or more values, or only the wildcard character (`*`).
        # 
        # *   Each value must start with `http://` or `https://`, which must be followed by a valid domain name, including top-level domain names. Example: `http://*.test.abc.example.com`.
        # *   You can specify a port in each value or leave the port empty. Valid values: **1** to **65535**.
        self.allow_origin = allow_origin
        # The headers that can be exposed.
        self.expose_headers = expose_headers
        # The maximum cache time of dry run requests in the browser. Unit: seconds.
        # 
        # Valid values: **-1** to **172800**.
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


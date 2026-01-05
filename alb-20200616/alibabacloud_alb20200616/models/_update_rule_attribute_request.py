# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class UpdateRuleAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        priority: int = None,
        rule_actions: List[main_models.UpdateRuleAttributeRequestRuleActions] = None,
        rule_conditions: List[main_models.UpdateRuleAttributeRequestRuleConditions] = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a `2xx HTTP` status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The priority of the forwarding rule. Valid values: **1 to 10000**. A lower value specifies a higher priority.
        # 
        # > The priorities of the forwarding rules created for the same listener must be unique.
        self.priority = priority
        # The actions of the forwarding rule.
        self.rule_actions = rule_actions
        # The match conditions of the forwarding rule.
        self.rule_conditions = rule_conditions
        # The ID of the forwarding rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the forwarding rule. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k1 in m.get('RuleActions'):
                temp_model = main_models.UpdateRuleAttributeRequestRuleActions()
                self.rule_actions.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.UpdateRuleAttributeRequestRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class UpdateRuleAttributeRequestRuleConditions(DaraModel):
    def __init__(
        self,
        cookie_config: main_models.UpdateRuleAttributeRequestRuleConditionsCookieConfig = None,
        header_config: main_models.UpdateRuleAttributeRequestRuleConditionsHeaderConfig = None,
        host_config: main_models.UpdateRuleAttributeRequestRuleConditionsHostConfig = None,
        method_config: main_models.UpdateRuleAttributeRequestRuleConditionsMethodConfig = None,
        path_config: main_models.UpdateRuleAttributeRequestRuleConditionsPathConfig = None,
        query_string_config: main_models.UpdateRuleAttributeRequestRuleConditionsQueryStringConfig = None,
        response_header_config: main_models.UpdateRuleAttributeRequestRuleConditionsResponseHeaderConfig = None,
        response_status_code_config: main_models.UpdateRuleAttributeRequestRuleConditionsResponseStatusCodeConfig = None,
        source_ip_config: main_models.UpdateRuleAttributeRequestRuleConditionsSourceIpConfig = None,
        type: str = None,
    ):
        # The key-value pairs of the cookie.
        self.cookie_config = cookie_config
        # The configuration of the header.
        self.header_config = header_config
        # The configuration of the hosts.
        self.host_config = host_config
        # The configuration of the request method.
        self.method_config = method_config
        # The configuration of the forwarding URL.
        self.path_config = path_config
        # The configuration of the query strings.
        self.query_string_config = query_string_config
        # The configuration of headers.
        self.response_header_config = response_header_config
        # The configuration of the response status codes.
        self.response_status_code_config = response_status_code_config
        # Traffic matching based on source IP addresses. You can specify up to five IP addresses, including CIDR blocks.
        self.source_ip_config = source_ip_config
        # The type of forwarding rule. You can specify up to seven types of forwarding rule. Valid values:
        # 
        # *   **Host**: Requests are forwarded based on hosts.
        # *   **Path**: Requests are forwarded based on URLs.
        # *   **Header**: Requests are forwarded based on HTTP headers.
        # *   **QueryString**: Requests are forwarded based on query strings.
        # *   **Method**: Requests are forwarded based on request methods.
        # *   **Cookie**: Requests are forwarded based on cookies.
        # *   **SourceIp**: Requests are forwarded based on source IP addresses.
        # *   **ResponseHeader**: Requests are forwarded based on HTTP response headers.
        # *   **ResponseStatusCode**: Requests are forwarded based on response status codes.
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
            temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsCookieConfig()
            self.cookie_config = temp_model.from_map(m.get('CookieConfig'))

        if m.get('HeaderConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsHeaderConfig()
            self.header_config = temp_model.from_map(m.get('HeaderConfig'))

        if m.get('HostConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m.get('HostConfig'))

        if m.get('MethodConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsMethodConfig()
            self.method_config = temp_model.from_map(m.get('MethodConfig'))

        if m.get('PathConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m.get('PathConfig'))

        if m.get('QueryStringConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsQueryStringConfig()
            self.query_string_config = temp_model.from_map(m.get('QueryStringConfig'))

        if m.get('ResponseHeaderConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsResponseHeaderConfig()
            self.response_header_config = temp_model.from_map(m.get('ResponseHeaderConfig'))

        if m.get('ResponseStatusCodeConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsResponseStatusCodeConfig()
            self.response_status_code_config = temp_model.from_map(m.get('ResponseStatusCodeConfig'))

        if m.get('SourceIpConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsSourceIpConfig()
            self.source_ip_config = temp_model.from_map(m.get('SourceIpConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateRuleAttributeRequestRuleConditionsSourceIpConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # You can add one or more IP addresses, including CIDR blocks.
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

class UpdateRuleAttributeRequestRuleConditionsResponseStatusCodeConfig(DaraModel):
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

class UpdateRuleAttributeRequestRuleConditionsResponseHeaderConfig(DaraModel):
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

class UpdateRuleAttributeRequestRuleConditionsQueryStringConfig(DaraModel):
    def __init__(
        self,
        values: List[main_models.UpdateRuleAttributeRequestRuleConditionsQueryStringConfigValues] = None,
    ):
        # The query strings. You can specify up to 20 query strings.
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
                temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsQueryStringConfigValues()
                self.values.append(temp_model.from_map(k1))

        return self

class UpdateRuleAttributeRequestRuleConditionsQueryStringConfigValues(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the query string. The key must be 1 to 100 characters in length, and can contain printable characters such as lowercase letters, asterisks (\\*), and question marks (?). The key cannot contain uppercase letters, space characters, or the following special characters: `# [ ] { } \\ | < > & "`.
        self.key = key
        # The value of the query string. The value must be 1 to 128 characters in length, and can contain printable characters such as lowercase letters, asterisks (\\*), and question marks (?). The value cannot contain uppercase letters, space characters, or the following special characters: `# [ ] { } \\ | < > & "`.
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

class UpdateRuleAttributeRequestRuleConditionsPathConfig(DaraModel):
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

class UpdateRuleAttributeRequestRuleConditionsMethodConfig(DaraModel):
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

class UpdateRuleAttributeRequestRuleConditionsHostConfig(DaraModel):
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

class UpdateRuleAttributeRequestRuleConditionsHeaderConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The header key. The header key must be 1 to 40 characters in length, and can contain letters, digits, hyphens (-), and underscores (_). Cookie and Host are not supported.
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

class UpdateRuleAttributeRequestRuleConditionsCookieConfig(DaraModel):
    def __init__(
        self,
        values: List[main_models.UpdateRuleAttributeRequestRuleConditionsCookieConfigValues] = None,
    ):
        # The key-value pairs of the cookie.
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
                temp_model = main_models.UpdateRuleAttributeRequestRuleConditionsCookieConfigValues()
                self.values.append(temp_model.from_map(k1))

        return self

class UpdateRuleAttributeRequestRuleConditionsCookieConfigValues(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The cookie key. The key must be 1 to 100 characters in length, and can contain printable characters such as lowercase letters, asterisks (\\*), and question marks (?). The key cannot contain uppercase letters, space characters, or the following special characters: `# [ ] { } \\ | < > & " ;`.
        self.key = key
        # The cookie value. The cookie value must be 1 to 128 characters in length, and can contain lowercase letters, printable ASCII characters, asterisks (\\*), and question marks (?). It cannot contain space characters or the following special characters: `# [ ] { } \\ | < > &`.
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

class UpdateRuleAttributeRequestRuleActions(DaraModel):
    def __init__(
        self,
        cors_config: main_models.UpdateRuleAttributeRequestRuleActionsCorsConfig = None,
        fixed_response_config: main_models.UpdateRuleAttributeRequestRuleActionsFixedResponseConfig = None,
        forward_group_config: main_models.UpdateRuleAttributeRequestRuleActionsForwardGroupConfig = None,
        insert_header_config: main_models.UpdateRuleAttributeRequestRuleActionsInsertHeaderConfig = None,
        order: int = None,
        redirect_config: main_models.UpdateRuleAttributeRequestRuleActionsRedirectConfig = None,
        remove_header_config: main_models.UpdateRuleAttributeRequestRuleActionsRemoveHeaderConfig = None,
        rewrite_config: main_models.UpdateRuleAttributeRequestRuleActionsRewriteConfig = None,
        traffic_limit_config: main_models.UpdateRuleAttributeRequestRuleActionsTrafficLimitConfig = None,
        traffic_mirror_config: main_models.UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfig = None,
        type: str = None,
    ):
        # The CORS configuration.
        self.cors_config = cors_config
        # The configuration of the custom response.
        self.fixed_response_config = fixed_response_config
        # The configuration of the server groups.
        self.forward_group_config = forward_group_config
        # The configuration of the header to be inserted.
        self.insert_header_config = insert_header_config
        # The priority of the action. Valid values: **1 to 50000**. A smaller value specifies a higher priority. The actions of a forwarding rule are applied in descending order of priority. This parameter cannot be left empty. The priority of each action within a forwarding rule must be unique. You can specify up to 20 forwarding rule priorities.
        self.order = order
        # The configuration of the redirect action. You can specify up to 20 redirect actions.
        self.redirect_config = redirect_config
        # The HTTP header to be removed.
        self.remove_header_config = remove_header_config
        # The configuration of the rewrite action.
        self.rewrite_config = rewrite_config
        # The configuration of the action to throttle traffic.
        self.traffic_limit_config = traffic_limit_config
        # The configuration of the traffic mirroring action.
        self.traffic_mirror_config = traffic_mirror_config
        # The type of the task. You can specify up to 11 types of action. Valid values:
        # 
        # *   **ForwardGroup**: forwards a request to multiple vServer groups.
        # *   **Redirect**: redirects requests.
        # *   **FixedResponse**: returns a fixed response.
        # *   **Rewrite**: rewrites requests.
        # *   **InsertHeader**: inserts a header.
        # *   **RemoveHeader**: deletes the header of a request.
        # *   **TrafficLimit**: throttles traffic.
        # *   **trafficMirror**: mirrors network traffic.
        # *   **Cors**: forwards requests based on CORS.
        # 
        # The preceding actions can be classified into two types:
        # 
        # *   **FinalType**: Each forwarding rule can contain only one FinalType action, which is performed at the end. You can specify only one of **ForwardGroup**, **Redirect**, and **FixedResponse**.
        # *   **ExtType**: Each forwarding rule can contain one or more **ExtType** actions, which are performed before the **FinalType** action. If you want to specify an ExtType action, you must also specify a **FinalType** action. You can specify multiple **InsertHeader** actions or one **Rewrite** action.
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
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsCorsConfig()
            self.cors_config = temp_model.from_map(m.get('CorsConfig'))

        if m.get('FixedResponseConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsFixedResponseConfig()
            self.fixed_response_config = temp_model.from_map(m.get('FixedResponseConfig'))

        if m.get('ForwardGroupConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m.get('ForwardGroupConfig'))

        if m.get('InsertHeaderConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsInsertHeaderConfig()
            self.insert_header_config = temp_model.from_map(m.get('InsertHeaderConfig'))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('RedirectConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsRedirectConfig()
            self.redirect_config = temp_model.from_map(m.get('RedirectConfig'))

        if m.get('RemoveHeaderConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsRemoveHeaderConfig()
            self.remove_header_config = temp_model.from_map(m.get('RemoveHeaderConfig'))

        if m.get('RewriteConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsRewriteConfig()
            self.rewrite_config = temp_model.from_map(m.get('RewriteConfig'))

        if m.get('TrafficLimitConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsTrafficLimitConfig()
            self.traffic_limit_config = temp_model.from_map(m.get('TrafficLimitConfig'))

        if m.get('TrafficMirrorConfig') is not None:
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfig()
            self.traffic_mirror_config = temp_model.from_map(m.get('TrafficMirrorConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfig(DaraModel):
    def __init__(
        self,
        mirror_group_config: main_models.UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig = None,
        target_type: str = None,
    ):
        # The server group to which network traffic is mirrored.
        self.mirror_group_config = mirror_group_config
        # The type of destination to which network traffic is mirrored. Valid values:
        # 
        # *   **ForwardGroupMirror**: a server group
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
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig()
            self.mirror_group_config = temp_model.from_map(m.get('MirrorGroupConfig'))

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_tuples: List[main_models.UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples] = None,
    ):
        # The server group to which traffic is mirrored.
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
                temp_model = main_models.UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class UpdateRuleAttributeRequestRuleActionsTrafficMirrorConfigMirrorGroupConfigServerGroupTuples(DaraModel):
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

class UpdateRuleAttributeRequestRuleActionsTrafficLimitConfig(DaraModel):
    def __init__(
        self,
        per_ip_qps: int = None,
        qps: int = None,
    ):
        # The number of requests per IP address. Value range: **1 to 1,000,000**.
        # 
        # >  If both the **QPS** and **PerIpQps** parameters are specified, make sure that the value of the **QPS** parameter is smaller than the value of the PerIpQps parameter.
        self.per_ip_qps = per_ip_qps
        # The number of queries per second (QPS). Value range: **1 to 1,000,000**.
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

class UpdateRuleAttributeRequestRuleActionsRewriteConfig(DaraModel):
    def __init__(
        self,
        host: str = None,
        path: str = None,
        query: str = None,
    ):
        # The hostname to which requests are rewritten. Valid values:
        # 
        # *   **${host}** (default): If you set the value to ${host}, you cannot append other characters.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The hostname must be 3 to 128 characters in length, and can contain lowercase letters, digits, hyphens (-), periods (.), asterisks (\\*), and question marks (?).
        #     *   The hostname contains at least one period (.) but does not start or end with a period (.).
        #     *   The rightmost domain label can contain only letters and wildcard characters. It cannot contain digits or hyphens (-).
        #     *   The domain labels do not start or end with a hyphen (-). You can use asterisks (\\*) and question marks (?) anywhere in a domain label as wildcard characters.
        self.host = host
        # The URL to which requests are redirected. Valid values:
        # 
        # *   Default value: **${path}**. \\*\\*${host}**, **${protocol}**, and **${port}\\*\\* are also supported. Each variable can be specified only once. The preceding variables can be used at the same time or combined with a custom value.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The header value must be 1 to 128 characters in length.
        #     *   It must start with a forward slash (/) and can contain letters, digits, and the following special characters: `$ - _ . + / & ~ @ :`. It does not contain the following special characters: `% # ; ! ( ) [ ] ^ , \\ "`. You can use asterisks (\\*) and question marks (?) as wildcard characters.
        self.path = path
        # The query string to which requests are redirected. Valid values:
        # 
        # *   Default value: **${query}**. \\*\\*${host}**, **${protocol}**, and **${port}\\*\\* are also supported. Each variable can be specified only once. The preceding variables can be used at the same time or combined with a custom value.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The header value must be 1 to 128 characters in length.
        #     *   It can contain printable characters, excluding space characters, the special characters `# [ ] { } \\ | < > "`, and uppercase letters.
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

class UpdateRuleAttributeRequestRuleActionsRemoveHeaderConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
    ):
        # The key of the header to be removed. The header key must be 1 to 40 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The header keys specified in RemoveHeader must be unique.
        # 
        # *   If Direction is set to Request, the following request headers cannot be removed: `slb-id`, `slb-ip`, `x-forwarded-for`, `x-forwarded-proto`, `x-forwarded-eip`, `x-forwarded-port`, `x-forwarded-client-srcport`, `x-forwarded-host`, `connection`, `upgrade`, `content-length`, `transfer-encoding`, `keep-alive`, `te`, `host`, `cookie`, `remoteip`, and `authority`. Request headers are not case-sensitive.
        # *   If Direction is set to Response, the following header keys are not supported: `connection`, `upgrade`, `content-length`, and `transfer-encoding`. The header keys are not case-sensitive.
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

class UpdateRuleAttributeRequestRuleActionsRedirectConfig(DaraModel):
    def __init__(
        self,
        host: str = None,
        http_code: str = None,
        path: str = None,
        port: str = None,
        protocol: str = None,
        query: str = None,
    ):
        # The hostname to which requests are redirected. Valid values:
        # 
        # *   **${host}** (default): If ${host} is returned, no other character is appended.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The hostname must be 3 to 128 characters in length, and can contain lowercase letters, digits, hyphens (-), periods (.), asterisks (\\*), and question marks (?).
        #     *   The hostname contains at least one period (.) but does not start or end with a period (.).
        #     *   The rightmost domain label can contain only letters and wildcard characters. It cannot contain digits or hyphens (-).
        #     *   The domain labels do not start or end with a hyphen (-).
        #     *   You can use asterisks (\\*) and question marks (?) anywhere in a domain label as wildcard characters.
        self.host = host
        # The forwarding method. Valid values: **301**, **302**, **303**, **307**, and **308**.
        self.http_code = http_code
        # The URL to which requests are redirected. Valid values:
        # 
        # *   Default value: **${path}**. \\*\\*${host}**, **${protocol}**, and **${port}\\*\\* are also supported. Each variable can be specified only once. The preceding variables can be used at the same time or combined with a custom value.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The header value must be 1 to 128 characters in length.
        #     *   It must start with a forward slash (/) and can contain letters, digits, and the following special characters: `$ - _ . + / & ~ @ :`. It does not contain the following special characters: `% # ; ! ( ) [ ] ^ , \\ "`. You can use asterisks (\\*) and question marks (?) as wildcard characters.
        self.path = path
        # The port to which requests are redirected. Valid values:
        # 
        # *   **${port}** (default): If you set the value to ${port}, you cannot append other characters.
        # *   Other valid values: **1 to 63335**.
        self.port = port
        # The redirect protocol. Valid values:
        # 
        # *   **${protocol}** (default): If you set the value to ${protocol}, you cannot append other characters.
        # *   **HTTP** or **HTTPS**.
        # 
        # >  HTTPS listeners support only HTTPS redirects.
        self.protocol = protocol
        # The query string of the URL to which requests are forwarded. Valid values:
        # 
        # *   Default value: **${query}**. \\*\\*${host}**, **${protocol}**, and **${port}\\*\\* are also supported. Each variable can be specified only once. The preceding variables can be used at the same time or combined with a custom value.
        # 
        # *   If you want to specify a custom value, make sure that the following requirements are met:
        # 
        #     *   The header value must be 1 to 128 characters in length.
        #     *   It can contain printable characters, excluding space characters, the special characters `# [ ] { } \\ | < > "`, and uppercase letters.
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

class UpdateRuleAttributeRequestRuleActionsInsertHeaderConfig(DaraModel):
    def __init__(
        self,
        cover_enabled: bool = None,
        key: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # Specifies whether to overwrite the request header values. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.cover_enabled = cover_enabled
        # The key of the header. The key must be 1 to 40 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The header keys specified by **InsertHeaderConfig** must be unique.
        # 
        # >  You cannot specify the following header keys: `slb-id`, `slb-ip`, `x-forwarded-for`, `x-forwarded-proto`, `x-forwarded-eip`, `x-forwarded-port`, `x-forwarded-client-srcport`, `x-forwarded-host`, `connection`, `upgrade`, `content-length`, `transfer-encoding`, `keep-alive`, `te`, `host`, `cookie`, `remoteip`, and `authority`. The header keys are case-insensitive.
        self.key = key
        # The value of the header.
        # 
        # *   If **ValueType** is set to **SystemDefined**, you can set the Value parameter to one of the following values:
        # 
        #     *   **ClientSrcPort**: the client port.
        #     *   **ClientSrcIp**: the IP address of the client.
        #     *   **Protocol**: the request protocol (HTTP or HTTPS).
        #     *   **SLBId**: the ID of the ALB instance.
        #     *   **SLBPort**: the listener port of the ALB instance.
        # 
        # *   If **ValueType** is set to **UserDefined**, a custom header value is supported. The header value must be 1 to 128 characters in length, and can contain printable characters whose ASCII values are `greater than or equal to 32 and lower than 127`. You can use asterisks (\\*) and question marks (?) as wildcard characters. Quotation marks (`"`) are not supported. The header value cannot start or end with a space character, or end with a backslash (`\\`).
        # 
        # *   If **ValueType** is set to **ReferenceHeader**, you can reference a value from request headers. The value must be 1 to 128 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores (_).
        self.value = value
        # The type of the header. Valid values:
        # 
        # *   **UserDefined**: a custom header.
        # *   **ReferenceHeader**: a header that references one of the request headers.
        # *   **SystemDefined**: a system-defined header value.
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

class UpdateRuleAttributeRequestRuleActionsForwardGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_sticky_session: main_models.UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupStickySession = None,
        server_group_tuples: List[main_models.UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # The configuration of session persistence for server groups.
        self.server_group_sticky_session = server_group_sticky_session
        # The server groups to which requests are forwarded.
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
            temp_model = main_models.UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupStickySession()
            self.server_group_sticky_session = temp_model.from_map(m.get('ServerGroupStickySession'))

        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k1 in m.get('ServerGroupTuples'):
                temp_model = main_models.UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        server_group_id: str = None,
        weight: int = None,
    ):
        # The ID of the server group to which requests are forwarded.
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

class UpdateRuleAttributeRequestRuleActionsForwardGroupConfigServerGroupStickySession(DaraModel):
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
        # The timeout period for sessions. Unit: seconds. Valid values: 1 to 86400.
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

class UpdateRuleAttributeRequestRuleActionsFixedResponseConfig(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        http_code: str = None,
    ):
        # The content of the response. The content can be up to 1 KB in size, and can contain only ASCII characters.
        self.content = content
        # The content type.
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

class UpdateRuleAttributeRequestRuleActionsCorsConfig(DaraModel):
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
        # The trusted HTTP methods of CORS requests.
        self.allow_methods = allow_methods
        # The trusted origins. You can specify one or more values, or only an asterisk (`*`).
        # 
        # *   The value must start with `http://` or `https://`, and be followed by a valid domain name, including top-level wildcard domain names. Example: `http://*.test.abc.example.com`.
        # *   You can specify ports for a single value. Valid values: **1** to **65535**.
        self.allow_origin = allow_origin
        # The headers that can be exposed.
        self.expose_headers = expose_headers
        # The maximum cache time of dry runs in the browser. Unit: seconds.
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


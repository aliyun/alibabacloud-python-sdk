# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class GetListenerHealthStatusResponseBody(DaraModel):
    def __init__(
        self,
        listener_health_status: List[main_models.GetListenerHealthStatusResponseBodyListenerHealthStatus] = None,
        next_token: str = None,
        request_id: str = None,
        rule_health_status: List[main_models.GetListenerHealthStatusResponseBodyRuleHealthStatus] = None,
    ):
        # The health check status of the server groups associated with the listener.
        self.listener_health_status = listener_health_status
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The health check status of the forwarding rules.
        self.rule_health_status = rule_health_status

    def validate(self):
        if self.listener_health_status:
            for v1 in self.listener_health_status:
                 if v1:
                    v1.validate()
        if self.rule_health_status:
            for v1 in self.rule_health_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ListenerHealthStatus'] = []
        if self.listener_health_status is not None:
            for k1 in self.listener_health_status:
                result['ListenerHealthStatus'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleHealthStatus'] = []
        if self.rule_health_status is not None:
            for k1 in self.rule_health_status:
                result['RuleHealthStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener_health_status = []
        if m.get('ListenerHealthStatus') is not None:
            for k1 in m.get('ListenerHealthStatus'):
                temp_model = main_models.GetListenerHealthStatusResponseBodyListenerHealthStatus()
                self.listener_health_status.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_health_status = []
        if m.get('RuleHealthStatus') is not None:
            for k1 in m.get('RuleHealthStatus'):
                temp_model = main_models.GetListenerHealthStatusResponseBodyRuleHealthStatus()
                self.rule_health_status.append(temp_model.from_map(k1))

        return self

class GetListenerHealthStatusResponseBodyRuleHealthStatus(DaraModel):
    def __init__(
        self,
        rule_id: str = None,
        server_group_infos: List[main_models.GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfos] = None,
    ):
        # The ID of the forwarding rule.
        self.rule_id = rule_id
        # The server groups.
        self.server_group_infos = server_group_infos

    def validate(self):
        if self.server_group_infos:
            for v1 in self.server_group_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        result['ServerGroupInfos'] = []
        if self.server_group_infos is not None:
            for k1 in self.server_group_infos:
                result['ServerGroupInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        self.server_group_infos = []
        if m.get('ServerGroupInfos') is not None:
            for k1 in m.get('ServerGroupInfos'):
                temp_model = main_models.GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfos()
                self.server_group_infos.append(temp_model.from_map(k1))

        return self

class GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfos(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        health_check_enabled: str = None,
        non_normal_servers: List[main_models.GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServers] = None,
        server_group_id: str = None,
    ):
        # The action specified for the server group.
        self.action_type = action_type
        # Indicates whether health checks are enabled. If **on** is returned, it indicates that health checks are enabled.
        self.health_check_enabled = health_check_enabled
        # A list of unhealthy backend servers.
        self.non_normal_servers = non_normal_servers
        # The ID of the server group that is associated with the listener.
        self.server_group_id = server_group_id

    def validate(self):
        if self.non_normal_servers:
            for v1 in self.non_normal_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled

        result['NonNormalServers'] = []
        if self.non_normal_servers is not None:
            for k1 in self.non_normal_servers:
                result['NonNormalServers'].append(k1.to_map() if k1 else None)

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')

        self.non_normal_servers = []
        if m.get('NonNormalServers') is not None:
            for k1 in m.get('NonNormalServers'):
                temp_model = main_models.GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServers()
                self.non_normal_servers.append(temp_model.from_map(k1))

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        return self

class GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServers(DaraModel):
    def __init__(
        self,
        port: int = None,
        reason: main_models.GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServersReason = None,
        server_id: str = None,
        server_ip: str = None,
        status: str = None,
    ):
        # The backend port.
        self.port = port
        # The cause for the unhealthy state of the backend servers.
        self.reason = reason
        # The ID of the backend server.
        self.server_id = server_id
        # The IP address of the server group.
        self.server_ip = server_ip
        # The status of the health check. Valid values: Valid values:
        # 
        # *   **Initial**: indicates that health checks are configured for the NLB instance, but no data was found.
        # *   **Unhealthy**: indicates that the backend server consecutively fails health checks.
        # *   **Unused**: indicates that the weight of the backend server is 0.
        # *   **Unavailable**: indicates that health checks are disabled.
        self.status = status

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.reason is not None:
            result['Reason'] = self.reason.to_map()

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Reason') is not None:
            temp_model = main_models.GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServersReason()
            self.reason = temp_model.from_map(m.get('Reason'))

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetListenerHealthStatusResponseBodyRuleHealthStatusServerGroupInfosNonNormalServersReason(DaraModel):
    def __init__(
        self,
        actual_response: str = None,
        expected_response: str = None,
        reason_code: str = None,
    ):
        # The HTTP status code returned from the server, for example, **302**.
        # 
        # > A value is returned only if **ReasonCode** is set to **RESPONSE_MISMATCH**.
        self.actual_response = actual_response
        # The HTTP status code returned after backend servers pass health checks.
        # 
        # Valid values: **HTTP_2xx**, **HTTP_3xx**, **HTTP_4xx**, and **HTTP_5xx**. Multiple status codes are separated by commas (,).
        # 
        # > A value is returned only if **ReasonCode** is set to **RESPONSE_MISMATCH**.
        self.expected_response = expected_response
        # The reason why the value of **Status** is Unhealthy. Only forwarding rules for HTTP and HTTPS listeners support this parameter.
        # 
        # *   **CONNECT_TIMEOUT**: ALB failed to connect to the backend server within the specified period of time.
        # *   **CONNECT_FAILED**: ALB failed to connect to the backend server.
        # *   **RECV_RESPONSE_FAILED**: ALB failed to receive a response from the backend server.
        # *   **RECV_RESPONSE_TIMEOUT**: ALB failed to receive a response from the backend server within the specified period of time.
        # *   **SEND_REQUEST_FAILED**: ALB failed to send a request to the backend server.
        # *   **SEND_REQUEST_TIMEOUT**: ALB failed to send a request to the backend server within the specified period of time.
        # *   **RESPONSE_FORMAT_ERROR**: The format of the response from the backend server is invalid.
        # *   **RESPONSE_MISMATCH**: The HTTP status code returned from the backend server is not the expected one.
        self.reason_code = reason_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_response is not None:
            result['ActualResponse'] = self.actual_response

        if self.expected_response is not None:
            result['ExpectedResponse'] = self.expected_response

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualResponse') is not None:
            self.actual_response = m.get('ActualResponse')

        if m.get('ExpectedResponse') is not None:
            self.expected_response = m.get('ExpectedResponse')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        return self

class GetListenerHealthStatusResponseBodyListenerHealthStatus(DaraModel):
    def __init__(
        self,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        server_group_infos: List[main_models.GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos] = None,
    ):
        # The listener ID.
        self.listener_id = listener_id
        # The listener port.
        self.listener_port = listener_port
        # The listener protocol.
        self.listener_protocol = listener_protocol
        # The information about the server group.
        self.server_group_infos = server_group_infos

    def validate(self):
        if self.server_group_infos:
            for v1 in self.server_group_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        result['ServerGroupInfos'] = []
        if self.server_group_infos is not None:
            for k1 in self.server_group_infos:
                result['ServerGroupInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        self.server_group_infos = []
        if m.get('ServerGroupInfos') is not None:
            for k1 in m.get('ServerGroupInfos'):
                temp_model = main_models.GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos()
                self.server_group_infos.append(temp_model.from_map(k1))

        return self

class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        health_check_enabled: str = None,
        non_normal_servers: List[main_models.GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers] = None,
        server_group_id: str = None,
    ):
        # The action specified for the server group. Valid values:
        # 
        # *   **ForwardGroup**: distributes requests to server groups.
        # *   **TrafficMirror**: mirrors requests to server groups.
        self.action_type = action_type
        # Indicates whether health checks are enabled. If **on** is returned, it indicates that health checks are enabled.
        self.health_check_enabled = health_check_enabled
        # A list of unhealthy backend servers.
        self.non_normal_servers = non_normal_servers
        # The ID of the server group that is associated with the listener.
        self.server_group_id = server_group_id

    def validate(self):
        if self.non_normal_servers:
            for v1 in self.non_normal_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled

        result['NonNormalServers'] = []
        if self.non_normal_servers is not None:
            for k1 in self.non_normal_servers:
                result['NonNormalServers'].append(k1.to_map() if k1 else None)

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')

        self.non_normal_servers = []
        if m.get('NonNormalServers') is not None:
            for k1 in m.get('NonNormalServers'):
                temp_model = main_models.GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers()
                self.non_normal_servers.append(temp_model.from_map(k1))

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        return self

class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers(DaraModel):
    def __init__(
        self,
        port: int = None,
        reason: main_models.GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason = None,
        server_id: str = None,
        server_ip: str = None,
        status: str = None,
    ):
        # The backend port.
        self.port = port
        # The cause for the unhealthy state of the backend servers.
        self.reason = reason
        # The ID of the backend server.
        self.server_id = server_id
        # The IP address of the backend server.
        self.server_ip = server_ip
        # The status of the health check. Valid values: Valid values:
        # 
        # *   **Initial**: indicates that health checks are configured for the NLB instance, but no data was found.
        # *   **Unhealthy**: indicates that the backend server consecutively fails health checks.
        # *   **Unused**: indicates that the weight of the backend server is 0.
        # *   **Unavailable**: indicates that health checks are disabled.
        self.status = status

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.reason is not None:
            result['Reason'] = self.reason.to_map()

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Reason') is not None:
            temp_model = main_models.GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason()
            self.reason = temp_model.from_map(m.get('Reason'))

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason(DaraModel):
    def __init__(
        self,
        actual_response: str = None,
        expected_response: str = None,
        reason_code: str = None,
    ):
        # The HTTP status code returned from the server, for example, **302**.
        # 
        # > A value is returned only if `ReasonCode` is set to **RESPONSE_MISMATCH**.
        self.actual_response = actual_response
        # The HTTP status code returned after backend servers pass health checks.
        # 
        # Valid values: **HTTP_2xx**, **HTTP_3xx**, **HTTP_4xx**, and **HTTP_5xx**. Multiple status codes are separated by commas (,).
        # 
        # > This value is returned only if **ReasonCode** is set to **RESPONSE_MISMATCH**.
        self.expected_response = expected_response
        # The reason why the value of **Status** is Unhealthy. Only HTTP and HTTPS listeners support this parameter.
        # 
        # *   **CONNECT_TIMEOUT**: ALB failed to connect to the backend server within the specified period of time.
        # *   **CONNECT_FAILED**: ALB failed to connect to the backend server.
        # *   **RECV_RESPONSE_FAILED**: ALB failed to receive a response from the backend server.
        # *   **RECV_RESPONSE_TIMEOUT**: ALB failed to receive a response from the backend server within the specified period of time.
        # *   **SEND_REQUEST_FAILED**: ALB failed to send a request to the backend server.
        # *   **SEND_REQUEST_TIMEOUT**: ALB failed to send a request to the backend server within the specified period of time.
        # *   **RESPONSE_FORMAT_ERROR**: The format of the response from the backend server is invalid.
        # *   **RESPONSE_MISMATCH**: The HTTP status code returned from the backend server is not the expected one.
        self.reason_code = reason_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_response is not None:
            result['ActualResponse'] = self.actual_response

        if self.expected_response is not None:
            result['ExpectedResponse'] = self.expected_response

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualResponse') is not None:
            self.actual_response = m.get('ActualResponse')

        if m.get('ExpectedResponse') is not None:
            self.expected_response = m.get('ExpectedResponse')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class GetListenerHealthStatusResponseBody(DaraModel):
    def __init__(
        self,
        listener_health_status: List[main_models.GetListenerHealthStatusResponseBodyListenerHealthStatus] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The health check status of the server group of the listener.
        self.listener_health_status = listener_health_status
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # - If **NextToken** is empty, it indicates that no next query is to be sent.
        # - If a value of **NextToken** is returned, the value is the token used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.listener_health_status:
            for v1 in self.listener_health_status:
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
        self.listener_health_status = []
        if m.get('ListenerHealthStatus') is not None:
            for k1 in m.get('ListenerHealthStatus'):
                temp_model = main_models.GetListenerHealthStatusResponseBodyListenerHealthStatus()
                self.listener_health_status.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetListenerHealthStatusResponseBodyListenerHealthStatus(DaraModel):
    def __init__(
        self,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        server_group_infos: List[main_models.GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos] = None,
    ):
        # The ID of the listener of the NLB instance.
        self.listener_id = listener_id
        # The listening port.
        self.listener_port = listener_port
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol
        # The information about the server groups.
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
        heath_check_enabled: bool = None,
        non_normal_servers: List[main_models.GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers] = None,
        server_group_id: str = None,
    ):
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.heath_check_enabled = heath_check_enabled
        # A list of unhealthy backend servers.
        self.non_normal_servers = non_normal_servers
        # The ID of the server group.
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
        if self.heath_check_enabled is not None:
            result['HeathCheckEnabled'] = self.heath_check_enabled

        result['NonNormalServers'] = []
        if self.non_normal_servers is not None:
            for k1 in self.non_normal_servers:
                result['NonNormalServers'].append(k1.to_map() if k1 else None)

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeathCheckEnabled') is not None:
            self.heath_check_enabled = m.get('HeathCheckEnabled')

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
        # The cause of the health check failure.
        self.reason = reason
        # The ID of the backend server.
        self.server_id = server_id
        # The IP address of the backend server.
        self.server_ip = server_ip
        # The health check status. Valid values:
        # 
        # *   **Initial**: indicates that health checks are configured for the NLB instance, but no data was found.
        # *   **Unhealthy**: indicates that the backend server consecutively fails health checks.
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
        reason_code: str = None,
    ):
        # The reason why the **status** is abnormal. Valid values:
        # 
        # *   **CONNECT_TIMEOUT**: The NLB instance failed to connect to the backend server within the specified period of time.
        # *   **CONNECT_FAILED**: The NLB instance failed to connect to the backend server.
        # *   **RECV_RESPONSE_TIMEOUT**: The NLB instance failed to receive a response from the backend server within the specified period of time.
        # *   **CONNECT_INTERRUPT**: The connection between the health check and the backend servers was interrupted.
        # *   **HTTP_CODE_NOT_MATCH**: The HTTP status code from the backend servers was not the expected one.
        # *   **HTTP_INVALID_HEADER**: The format of the response from the backend servers is invalid.
        self.reason_code = reason_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        return self


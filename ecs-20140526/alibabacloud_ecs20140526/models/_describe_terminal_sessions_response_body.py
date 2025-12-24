# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeTerminalSessionsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        sessions: main_models.DescribeTerminalSessionsResponseBodySessions = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information of the sessions.
        self.sessions = sessions

    def validate(self):
        if self.sessions:
            self.sessions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sessions is not None:
            result['Sessions'] = self.sessions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sessions') is not None:
            temp_model = main_models.DescribeTerminalSessionsResponseBodySessions()
            self.sessions = temp_model.from_map(m.get('Sessions'))

        return self

class DescribeTerminalSessionsResponseBodySessions(DaraModel):
    def __init__(
        self,
        session: List[main_models.DescribeTerminalSessionsResponseBodySessionsSession] = None,
    ):
        self.session = session

    def validate(self):
        if self.session:
            for v1 in self.session:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Session'] = []
        if self.session is not None:
            for k1 in self.session:
                result['Session'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.session = []
        if m.get('Session') is not None:
            for k1 in m.get('Session'):
                temp_model = main_models.DescribeTerminalSessionsResponseBodySessionsSession()
                self.session.append(temp_model.from_map(k1))

        return self

class DescribeTerminalSessionsResponseBodySessionsSession(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        connections: main_models.DescribeTerminalSessionsResponseBodySessionsSessionConnections = None,
        creation_time: str = None,
        identity_type: str = None,
        port_number: int = None,
        principal_id: str = None,
        session_id: str = None,
        target_server: str = None,
        username: str = None,
    ):
        # The IP address of the client used to establish connections.
        self.client_ip = client_ip
        # The information of the connections.
        self.connections = connections
        # The time when the session was created.
        self.creation_time = creation_time
        # The principal type. Valid values:
        # 
        # *   Account: an Alibaba Cloud account
        # *   RAMUser: a RAM user
        # *   AssumedRoleUser: a RAM role
        self.identity_type = identity_type
        # The port number of the instance, which is used for data forwarding. If no port number was specified for data forwarding when the session was created, this parameter is empty.
        self.port_number = port_number
        # The ID of the principal. Valid values based on the `IdentityType` value:
        # 
        # *   If the requester uses an Alibaba Cloud account to call the operation, the ID of the Alibaba Cloud account is returned.
        # *   If the requester uses a Resource Access Management (RAM) user to call the operation, the ID of the RAM user is returned.
        # *   If the requester uses a RAM role to call the operation, the ID of the principal that actually calls the operation is returned.
        self.principal_id = principal_id
        # The session ID.
        self.session_id = session_id
        # The address of the service that was accessed in a virtual private cloud (VPC) from the instance.
        self.target_server = target_server
        # The username used to establish connections.
        self.username = username

    def validate(self):
        if self.connections:
            self.connections.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip

        if self.connections is not None:
            result['Connections'] = self.connections.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.port_number is not None:
            result['PortNumber'] = self.port_number

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.target_server is not None:
            result['TargetServer'] = self.target_server

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')

        if m.get('Connections') is not None:
            temp_model = main_models.DescribeTerminalSessionsResponseBodySessionsSessionConnections()
            self.connections = temp_model.from_map(m.get('Connections'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('PortNumber') is not None:
            self.port_number = m.get('PortNumber')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TargetServer') is not None:
            self.target_server = m.get('TargetServer')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class DescribeTerminalSessionsResponseBodySessionsSessionConnections(DaraModel):
    def __init__(
        self,
        connection: List[main_models.DescribeTerminalSessionsResponseBodySessionsSessionConnectionsConnection] = None,
    ):
        self.connection = connection

    def validate(self):
        if self.connection:
            for v1 in self.connection:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Connection'] = []
        if self.connection is not None:
            for k1 in self.connection:
                result['Connection'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection = []
        if m.get('Connection') is not None:
            for k1 in m.get('Connection'):
                temp_model = main_models.DescribeTerminalSessionsResponseBodySessionsSessionConnectionsConnection()
                self.connection.append(temp_model.from_map(k1))

        return self

class DescribeTerminalSessionsResponseBodySessionsSessionConnectionsConnection(DaraModel):
    def __init__(
        self,
        closed_reason: str = None,
        end_time: str = None,
        failed_detail: str = None,
        instance_id: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The reason why the connection was closed. This parameter is returned only when the `Status` value is `Disconnected`, `Terminated`, or `Failed`. Valid values:
        # 
        # *   InstanceNotExists: The specified instance did not exist or was released.
        # *   InstanceNotRunning: The specified instance was not running.
        # *   DeliveryTimeout: The connection timed out.
        # *   AgentNeedUpgrade: Cloud Assistant Agent required an upgrade.
        # *   AgentNotOnline: Cloud Assistant Agent was not connected to the Cloud Assistant server.
        # *   MessageFormatInvalid: The message format was invalid.
        # *   AgentSocketClosed: The connection was closed as expected.
        # *   ClientClosed: Session Manager Client closed the connection.
        self.closed_reason = closed_reason
        # The time when the connection was closed.
        self.end_time = end_time
        # Cause of the connection failure. This parameter is returned only when the Status parameter is Failed.
        self.failed_detail = failed_detail
        # The instance ID.
        self.instance_id = instance_id
        # The time when the connection started to be established.
        self.start_time = start_time
        # The state of the session. Valid values:
        # 
        # *   Connecting: The connection is being established.
        # *   Connected: The connection is established.
        # *   Terminated: The session is terminated.
        # *   Failed: The connection failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.closed_reason is not None:
            result['ClosedReason'] = self.closed_reason

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.failed_detail is not None:
            result['FailedDetail'] = self.failed_detail

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClosedReason') is not None:
            self.closed_reason = m.get('ClosedReason')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FailedDetail') is not None:
            self.failed_detail = m.get('FailedDetail')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


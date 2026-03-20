# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateListenerAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_description: str = None,
        listener_id: str = None,
        server_group_id: str = None,
        tcp_idle_timeout: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters. If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The listener description.
        # 
        # The description must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.listener_description = listener_description
        # The listener ID.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The server group ID.
        self.server_group_id = server_group_id
        # The timeout period of an idle TCP connection. Unit: seconds.
        # 
        # Valid values: **60** to **6000**.
        self.tcp_idle_timeout = tcp_idle_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.tcp_idle_timeout is not None:
            result['TcpIdleTimeout'] = self.tcp_idle_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('TcpIdleTimeout') is not None:
            self.tcp_idle_timeout = m.get('TcpIdleTimeout')

        return self


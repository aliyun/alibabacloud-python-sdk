# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizationServersResponseBody(DaraModel):
    def __init__(
        self,
        authorization_servers: List[main_models.ListAuthorizationServersResponseBodyAuthorizationServers] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of authorization servers.
        self.authorization_servers = authorization_servers
        # The number of entries per page for a paged query.
        self.max_results = max_results
        # The pagination token returned in this call.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of authorization servers.
        self.total_count = total_count

    def validate(self):
        if self.authorization_servers:
            for v1 in self.authorization_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizationServers'] = []
        if self.authorization_servers is not None:
            for k1 in self.authorization_servers:
                result['AuthorizationServers'].append(k1.to_map() if k1 else None)

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
        self.authorization_servers = []
        if m.get('AuthorizationServers') is not None:
            for k1 in m.get('AuthorizationServers'):
                temp_model = main_models.ListAuthorizationServersResponseBodyAuthorizationServers()
                self.authorization_servers.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAuthorizationServersResponseBodyAuthorizationServers(DaraModel):
    def __init__(
        self,
        authorization_server_id: str = None,
        authorization_server_name: str = None,
        create_time: int = None,
        creation_type: str = None,
        description: str = None,
        instance_id: str = None,
        issuer: str = None,
        issuer_domain: str = None,
        issuer_mode: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # The unique identifier of the authorization server.
        self.authorization_server_id = authorization_server_id
        # The name of the authorization server.
        self.authorization_server_name = authorization_server_name
        # The creation time.
        self.create_time = create_time
        # The creation type.
        self.creation_type = creation_type
        # The description of the authorization server.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The currently active issuer address.
        self.issuer = issuer
        # The domain name used by the issuer.
        self.issuer_domain = issuer_domain
        # The issuer mode.
        self.issuer_mode = issuer_mode
        # The status.
        self.status = status
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_server_id is not None:
            result['AuthorizationServerId'] = self.authorization_server_id

        if self.authorization_server_name is not None:
            result['AuthorizationServerName'] = self.authorization_server_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creation_type is not None:
            result['CreationType'] = self.creation_type

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.issuer_domain is not None:
            result['IssuerDomain'] = self.issuer_domain

        if self.issuer_mode is not None:
            result['IssuerMode'] = self.issuer_mode

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationServerId') is not None:
            self.authorization_server_id = m.get('AuthorizationServerId')

        if m.get('AuthorizationServerName') is not None:
            self.authorization_server_name = m.get('AuthorizationServerName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('IssuerDomain') is not None:
            self.issuer_domain = m.get('IssuerDomain')

        if m.get('IssuerMode') is not None:
            self.issuer_mode = m.get('IssuerMode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self


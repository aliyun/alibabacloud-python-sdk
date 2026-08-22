# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeOpenSearchConnectionInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeOpenSearchConnectionInfoResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeOpenSearchConnectionInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The data struct.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeOpenSearchConnectionInfoResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeOpenSearchConnectionInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOpenSearchConnectionInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        dashboard_endpoint: main_models.DescribeOpenSearchConnectionInfoResponseBodyDataDashboardEndpoint = None,
        dashboard_public_endpoint: main_models.DescribeOpenSearchConnectionInfoResponseBodyDataDashboardPublicEndpoint = None,
        default_username: str = None,
        private_endpoint: main_models.DescribeOpenSearchConnectionInfoResponseBodyDataPrivateEndpoint = None,
        protocol: str = None,
        public_endpoint: main_models.DescribeOpenSearchConnectionInfoResponseBodyDataPublicEndpoint = None,
    ):
        # The internal endpoint of the OpenSearch Dashboard.
        self.dashboard_endpoint = dashboard_endpoint
        # The public network access endpoint of the OpenSearch Dashboard.
        self.dashboard_public_endpoint = dashboard_public_endpoint
        # The default account name of OpenSearch.
        self.default_username = default_username
        # The VPC endpoint of the instance.
        self.private_endpoint = private_endpoint
        # The protocol of the monitoring task. Valid values:
        # 
        # - **ICMP**.
        # - **TCP**.
        # - **HTTP**.
        # 
        # > Private network monitoring supports only the ICMP and TCP protocols.
        self.protocol = protocol
        # The public endpoint of the instance.
        self.public_endpoint = public_endpoint

    def validate(self):
        if self.dashboard_endpoint:
            self.dashboard_endpoint.validate()
        if self.dashboard_public_endpoint:
            self.dashboard_public_endpoint.validate()
        if self.private_endpoint:
            self.private_endpoint.validate()
        if self.public_endpoint:
            self.public_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_endpoint is not None:
            result['DashboardEndpoint'] = self.dashboard_endpoint.to_map()

        if self.dashboard_public_endpoint is not None:
            result['DashboardPublicEndpoint'] = self.dashboard_public_endpoint.to_map()

        if self.default_username is not None:
            result['DefaultUsername'] = self.default_username

        if self.private_endpoint is not None:
            result['PrivateEndpoint'] = self.private_endpoint.to_map()

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.public_endpoint is not None:
            result['PublicEndpoint'] = self.public_endpoint.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardEndpoint') is not None:
            temp_model = main_models.DescribeOpenSearchConnectionInfoResponseBodyDataDashboardEndpoint()
            self.dashboard_endpoint = temp_model.from_map(m.get('DashboardEndpoint'))

        if m.get('DashboardPublicEndpoint') is not None:
            temp_model = main_models.DescribeOpenSearchConnectionInfoResponseBodyDataDashboardPublicEndpoint()
            self.dashboard_public_endpoint = temp_model.from_map(m.get('DashboardPublicEndpoint'))

        if m.get('DefaultUsername') is not None:
            self.default_username = m.get('DefaultUsername')

        if m.get('PrivateEndpoint') is not None:
            temp_model = main_models.DescribeOpenSearchConnectionInfoResponseBodyDataPrivateEndpoint()
            self.private_endpoint = temp_model.from_map(m.get('PrivateEndpoint'))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('PublicEndpoint') is not None:
            temp_model = main_models.DescribeOpenSearchConnectionInfoResponseBodyDataPublicEndpoint()
            self.public_endpoint = temp_model.from_map(m.get('PublicEndpoint'))

        return self

class DescribeOpenSearchConnectionInfoResponseBodyDataPublicEndpoint(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        host: str = None,
        port: int = None,
    ):
        # Specifies whether to enable dead-letter message delivery.
        self.enabled = enabled
        # The machine.
        self.host = host
        # The port.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.host is not None:
            result['Host'] = self.host

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class DescribeOpenSearchConnectionInfoResponseBodyDataPrivateEndpoint(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        host: str = None,
        port: int = None,
    ):
        # Specifies whether to enable the echo feature. This parameter is required. Valid values: true/false.
        self.enabled = enabled
        # The OSS domain name.
        self.host = host
        # The port.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.host is not None:
            result['Host'] = self.host

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class DescribeOpenSearchConnectionInfoResponseBodyDataDashboardPublicEndpoint(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        host: str = None,
        port: int = None,
        url: str = None,
    ):
        # The service activation status. Valid values:
        # 
        # - **on**: Activated.
        # - **off**: Not activated.
        self.enabled = enabled
        # The hostname. Retrieves data under the specified host.
        self.host = host
        # The port.
        self.port = port
        # The URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.host is not None:
            result['Host'] = self.host

        if self.port is not None:
            result['Port'] = self.port

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeOpenSearchConnectionInfoResponseBodyDataDashboardEndpoint(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        host: str = None,
        port: int = None,
        url: str = None,
    ):
        # Specifies whether static frame check is enabled. Default value: false.
        self.enabled = enabled
        # The host address.
        self.host = host
        # The port.
        self.port = port
        # The URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.host is not None:
            result['Host'] = self.host

        if self.port is not None:
            result['Port'] = self.port

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeOpenSearchConnectionInfoResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The authentication action.
        self.auth_action = auth_action
        # The display name of the authentication principal.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authentication principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The description is the same as above.
        self.auth_principal_type = auth_principal_type
        # The diagnostic information.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # NoPermissionType
        self.no_permission_type = no_permission_type
        # The policy type.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self


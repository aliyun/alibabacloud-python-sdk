# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class ConnectorCreateInput(DaraModel):
    def __init__(
        self,
        authentication: main_models.ConnectorAuthenticationInput = None,
        capability_grants: List[Dict[str, Any]] = None,
        client_token: str = None,
        configuration: Dict[str, Any] = None,
        connector_name: str = None,
        description: str = None,
        display_name: str = None,
        enabled: bool = None,
        policy: Dict[str, Any] = None,
        provider: str = None,
        runtime: main_models.ConnectorRuntime = None,
        target: Dict[str, Any] = None,
    ):
        # The authentication configuration used to access the target service.
        # 
        # This parameter is required.
        self.authentication = authentication
        # The list of capabilities granted to the connector.
        # 
        # This parameter is required.
        self.capability_grants = capability_grants
        # Idempotency token
        # 
        # This parameter is required.
        self.client_token = client_token
        # Provider configuration
        # 
        # This parameter is required.
        self.configuration = configuration
        # Connector name
        # 
        # This parameter is required.
        self.connector_name = connector_name
        # Description
        self.description = description
        # Display name
        # 
        # This parameter is required.
        self.display_name = display_name
        # Specifies whether the connector is enabled after creation.
        self.enabled = enabled
        # The execution policy of the connector.
        # 
        # This parameter is required.
        self.policy = policy
        # Provider
        # 
        # This parameter is required.
        self.provider = provider
        # The runtime configuration of the connector.
        # 
        # This parameter is required.
        self.runtime = runtime
        # Provider target
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        if self.authentication:
            self.authentication.validate()
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()

        if self.capability_grants is not None:
            result['capabilityGrants'] = self.capability_grants

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.connector_name is not None:
            result['connectorName'] = self.connector_name

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.policy is not None:
            result['policy'] = self.policy

        if self.provider is not None:
            result['provider'] = self.provider

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        if self.target is not None:
            result['target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication') is not None:
            temp_model = main_models.ConnectorAuthenticationInput()
            self.authentication = temp_model.from_map(m.get('authentication'))

        if m.get('capabilityGrants') is not None:
            self.capability_grants = m.get('capabilityGrants')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('connectorName') is not None:
            self.connector_name = m.get('connectorName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('runtime') is not None:
            temp_model = main_models.ConnectorRuntime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        if m.get('target') is not None:
            self.target = m.get('target')

        return self


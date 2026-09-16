# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class ConnectorUpdateInput(DaraModel):
    def __init__(
        self,
        authentication: main_models.ConnectorAuthenticationUpdateInput = None,
        capability_grants: List[Dict[str, Any]] = None,
        configuration: Dict[str, Any] = None,
        description: str = None,
        display_name: str = None,
        enabled: bool = None,
        policy: Dict[str, Any] = None,
        runtime: main_models.ConnectorRuntime = None,
        target: Dict[str, Any] = None,
    ):
        # The authentication configuration used to replace the existing credentials.
        self.authentication = authentication
        # The list of capabilities used to replace the existing grants.
        self.capability_grants = capability_grants
        # The provider configuration used to update the Connector. Only AlibabaCloudResources allows null. Other providers must provide an object.
        self.configuration = configuration
        # The description of the Connector.
        self.description = description
        # The display name of the Connector.
        self.display_name = display_name
        # Specifies whether to enable the Connector.
        self.enabled = enabled
        # The execution policy used to replace the existing policy.
        self.policy = policy
        # The runtime configuration used to update the Connector.
        self.runtime = runtime
        # The provider target used to update the Connector.
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

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.policy is not None:
            result['policy'] = self.policy

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        if self.target is not None:
            result['target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication') is not None:
            temp_model = main_models.ConnectorAuthenticationUpdateInput()
            self.authentication = temp_model.from_map(m.get('authentication'))

        if m.get('capabilityGrants') is not None:
            self.capability_grants = m.get('capabilityGrants')

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('runtime') is not None:
            temp_model = main_models.ConnectorRuntime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        if m.get('target') is not None:
            self.target = m.get('target')

        return self


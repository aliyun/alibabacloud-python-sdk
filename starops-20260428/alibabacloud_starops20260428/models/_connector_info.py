# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class ConnectorInfo(DaraModel):
    def __init__(
        self,
        authentication: main_models.ConnectorAuthentication = None,
        capability_grants: List[Dict[str, Any]] = None,
        configuration: Dict[str, Any] = None,
        connector_name: str = None,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        enabled: bool = None,
        etag: str = None,
        name: str = None,
        policy: Dict[str, Any] = None,
        provider: str = None,
        revision: int = None,
        runtime: main_models.ConnectorRuntime = None,
        status: Dict[str, Any] = None,
        target: Dict[str, Any] = None,
        update_time: str = None,
    ):
        # Safe authentication identity
        # 
        # This parameter is required.
        self.authentication = authentication
        # The list of capabilities granted to the Connector.
        # 
        # This parameter is required.
        self.capability_grants = capability_grants
        # Provider configuration
        # 
        # This parameter is required.
        self.configuration = configuration
        # Connector name
        # 
        # This parameter is required.
        self.connector_name = connector_name
        # Creation time
        # 
        # This parameter is required.
        self.create_time = create_time
        # Description
        self.description = description
        # Display name
        # 
        # This parameter is required.
        self.display_name = display_name
        # Specifies whether the Connector is enabled.
        # 
        # This parameter is required.
        self.enabled = enabled
        # ETag
        # 
        # This parameter is required.
        self.etag = etag
        # Digital employee name
        # 
        # This parameter is required.
        self.name = name
        # The execution policy of the Connector.
        # 
        # This parameter is required.
        self.policy = policy
        # Provider
        # 
        # This parameter is required.
        self.provider = provider
        # Revision
        # 
        # This parameter is required.
        self.revision = revision
        # The runtime configuration of the Connector.
        # 
        # This parameter is required.
        self.runtime = runtime
        # Resource status
        # 
        # This parameter is required.
        self.status = status
        # Provider target
        # 
        # This parameter is required.
        self.target = target
        # Update time
        # 
        # This parameter is required.
        self.update_time = update_time

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

        if self.connector_name is not None:
            result['connectorName'] = self.connector_name

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.etag is not None:
            result['etag'] = self.etag

        if self.name is not None:
            result['name'] = self.name

        if self.policy is not None:
            result['policy'] = self.policy

        if self.provider is not None:
            result['provider'] = self.provider

        if self.revision is not None:
            result['revision'] = self.revision

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.target is not None:
            result['target'] = self.target

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication') is not None:
            temp_model = main_models.ConnectorAuthentication()
            self.authentication = temp_model.from_map(m.get('authentication'))

        if m.get('capabilityGrants') is not None:
            self.capability_grants = m.get('capabilityGrants')

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('connectorName') is not None:
            self.connector_name = m.get('connectorName')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('etag') is not None:
            self.etag = m.get('etag')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        if m.get('runtime') is not None:
            temp_model = main_models.ConnectorRuntime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self


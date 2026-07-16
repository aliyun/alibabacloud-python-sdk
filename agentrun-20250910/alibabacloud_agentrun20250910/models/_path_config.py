# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PathConfig(DaraModel):
    def __init__(
        self,
        agent_runtime_endpoint_name: str = None,
        compatible_protocol: str = None,
        flow_endpoint_name: str = None,
        methods: List[str] = None,
        path: str = None,
        remove_base_path_on_forward: bool = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The agent runtime version. This parameter takes effect only when `resourceType` is `runtime`.
        self.agent_runtime_endpoint_name = agent_runtime_endpoint_name
        # The compatible protocol, used to convert the backend response format. This parameter is required only when `resourceType` is `flow`. Valid values: `native` indicates an FnF native call; `openai`, `dify-workflow`, and `dify-chatflow` map to their corresponding compatible APIs.
        self.compatible_protocol = compatible_protocol
        # The Flow version/alias. This parameter takes effect only when `resourceType` is `flow`. Default value: `Default`.
        self.flow_endpoint_name = flow_endpoint_name
        # Supported methods: HEAD, GET, POST, PUT, DELETE, PATCH, and OPTIONS.
        self.methods = methods
        # The path for this routing rule.
        self.path = path
        self.remove_base_path_on_forward = remove_base_path_on_forward
        # The resource name.
        self.resource_name = resource_name
        # The resource type. This type must match the one associated with the credential.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_endpoint_name is not None:
            result['agentRuntimeEndpointName'] = self.agent_runtime_endpoint_name

        if self.compatible_protocol is not None:
            result['compatibleProtocol'] = self.compatible_protocol

        if self.flow_endpoint_name is not None:
            result['flowEndpointName'] = self.flow_endpoint_name

        if self.methods is not None:
            result['methods'] = self.methods

        if self.path is not None:
            result['path'] = self.path

        if self.remove_base_path_on_forward is not None:
            result['removeBasePathOnForward'] = self.remove_base_path_on_forward

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeEndpointName') is not None:
            self.agent_runtime_endpoint_name = m.get('agentRuntimeEndpointName')

        if m.get('compatibleProtocol') is not None:
            self.compatible_protocol = m.get('compatibleProtocol')

        if m.get('flowEndpointName') is not None:
            self.flow_endpoint_name = m.get('flowEndpointName')

        if m.get('methods') is not None:
            self.methods = m.get('methods')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('removeBasePathOnForward') is not None:
            self.remove_base_path_on_forward = m.get('removeBasePathOnForward')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self


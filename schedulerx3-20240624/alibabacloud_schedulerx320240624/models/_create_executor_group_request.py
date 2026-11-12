# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExecutorGroupRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        auth_type: str = None,
        auto_scale: bool = None,
        cluster_id: str = None,
        cms_workspace_id: str = None,
        description: str = None,
        integration_type: str = None,
        name: str = None,
        network: str = None,
        protocol: str = None,
        worker_type: str = None,
        workers: str = None,
        xattrs: str = None,
    ):
        # The client secret.
        self.api_key = api_key
        # The authentication type.
        self.auth_type = auth_type
        # The auto scaling configuration.
        self.auto_scale = auto_scale
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The CloudMonitor Service (CMS) workspace ID.
        self.cms_workspace_id = cms_workspace_id
        # The description of the worker group.
        self.description = description
        # The integration method of the executor. Valid values: manual (indicates manual entry) and acs (indicates ACS integration).
        self.integration_type = integration_type
        # The name of the worker group.
        # 
        # This parameter is required.
        self.name = name
        # The network type. Valid values: public and private.
        self.network = network
        # The backend protocol. Valid values:
        # 
        # - **HTTP** (default): Supports association with HTTPS, HTTP, and QUIC listeners.
        # 
        # - **HTTPS**: Supports association with HTTPS listeners.
        # 
        # - **gRPC**: Supports association with HTTPS and QUIC listeners.
        # 
        # > If **ServerGroupType** is set to **Fc**, you do not need to configure the backend protocol.
        self.protocol = protocol
        # The worker type.
        # 
        # This parameter is required.
        self.worker_type = worker_type
        # The list of workers in JSON format.
        # 
        # This parameter is required.
        self.workers = workers
        # The extended configuration of the executor group.
        self.xattrs = xattrs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.auto_scale is not None:
            result['AutoScale'] = self.auto_scale

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cms_workspace_id is not None:
            result['CmsWorkspaceId'] = self.cms_workspace_id

        if self.description is not None:
            result['Description'] = self.description

        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type

        if self.name is not None:
            result['Name'] = self.name

        if self.network is not None:
            result['Network'] = self.network

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.worker_type is not None:
            result['WorkerType'] = self.worker_type

        if self.workers is not None:
            result['Workers'] = self.workers

        if self.xattrs is not None:
            result['XAttrs'] = self.xattrs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('AutoScale') is not None:
            self.auto_scale = m.get('AutoScale')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CmsWorkspaceId') is not None:
            self.cms_workspace_id = m.get('CmsWorkspaceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('WorkerType') is not None:
            self.worker_type = m.get('WorkerType')

        if m.get('Workers') is not None:
            self.workers = m.get('Workers')

        if m.get('XAttrs') is not None:
            self.xattrs = m.get('XAttrs')

        return self


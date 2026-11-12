# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateExecutorGroupRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        auth_type: str = None,
        auto_scale: bool = None,
        cluster_id: str = None,
        cms_workspace_id: str = None,
        description: str = None,
        id: str = None,
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
        # Specifies whether to enable auto scaling.
        self.auto_scale = auto_scale
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The CMS workspace ID.
        self.cms_workspace_id = cms_workspace_id
        # The description of the executor group.
        self.description = description
        # The ID.
        # 
        # This parameter is required.
        self.id = id
        # The name of the executor group.
        self.name = name
        # The network configuration.
        self.network = network
        # The protocol.
        self.protocol = protocol
        # The executor type.
        self.worker_type = worker_type
        # The list of specified machines in JSON format.
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

        if self.id is not None:
            result['Id'] = self.id

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

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


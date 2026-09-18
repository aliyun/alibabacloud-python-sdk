# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkspaceAcrRamAuthorizeUrlRequest(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        namespace: str = None,
        repository: str = None,
    ):
        # The ACR Enterprise instance ID.
        # 
        # This parameter is required.
        self.acr_instance_id = acr_instance_id
        # The target ACR namespace, which corresponds to Agent artifact.container.namespace. This is not a Kubernetes namespace. Together with the instance and repository, this parameter determines the authorization scope.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The target repository name, which corresponds to Agent artifact.container.repo. Do not include a tag, namespace, or path separator. Wildcards are not accepted.
        # 
        # This parameter is required.
        self.repository = repository

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.repository is not None:
            result['repository'] = self.repository

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('repository') is not None:
            self.repository = m.get('repository')

        return self


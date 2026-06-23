# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourcesDeleteProtectionRequest(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        resources: str = None,
    ):
        # The namespace of the resource to query.
        # 
        # This parameter is required when resource_type is set to services. If this parameter is not specified, the namespace defaults to default.
        self.namespace = namespace
        # The name of the resource to query. Separate multiple resources with commas (,).
        # 
        # - If resource_type is set to namespaces, set this parameter to namespace names. If this parameter is not specified, the deletion protection status of all namespaces in the cluster is queried.
        # 
        # - If resource_type is set to services, this parameter is required. Set this parameter to service names.
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.resources is not None:
            result['resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('resources') is not None:
            self.resources = m.get('resources')

        return self


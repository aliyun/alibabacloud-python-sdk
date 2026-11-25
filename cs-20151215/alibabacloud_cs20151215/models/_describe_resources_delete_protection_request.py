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
        # The namespace to which the resource to query belongs.
        # 
        # This parameter is required when ResourceType is set to services. If this parameter is not specified, the default namespace is used.
        self.namespace = namespace
        # The names of the resources to query. Separate multiple resource names with commas (,).
        # 
        # - If ResourceType is set to namespaces, specify the namespace names. If this parameter is left empty, the deletion protection status of all namespaces in the cluster is queried.
        # 
        # - If ResourceType is set to services, this parameter is required. Specify the service names.
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


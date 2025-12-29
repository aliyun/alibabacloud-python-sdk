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
        # The namespace in which the resources that you want to query reside.
        # 
        # This parameter is required when you set resource_type to services. Default value: default.
        self.namespace = namespace
        # The names of the resources that you want to query. Separate multiple resource names with commas (,).
        # 
        # *   When you set resource_type to namespaces, you must specify namespace names. If you leave this parameter empty, all namespaces in the cluster are queried.
        # *   If you set resource_type to services, you must specify Service names.
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNamespaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        namespace: str = None,
        namespace_name: str = None,
        region_id: str = None,
    ):
        # The description of the namespace.
        self.description = description
        # The namespace ID. You can obtain the namespace ID on the Namespaces page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


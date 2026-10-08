# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateK8sResourceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        namespace: str = None,
        resource_content: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The ID of the namespace to which the Kubernetes resource belongs.
        self.namespace = namespace
        # The description of the resource in the YAML format.
        self.resource_content = resource_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.resource_content is not None:
            result['ResourceContent'] = self.resource_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ResourceContent') is not None:
            self.resource_content = m.get('ResourceContent')

        return self


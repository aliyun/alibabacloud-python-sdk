# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertK8sResourceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        namespace: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The ID of the cluster. For more information, see [ListCluster](https://help.aliyun.com/document_detail/154995.html).
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The namespace.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The name of the resource.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The resource type. Only deployment is supported.
        # 
        # This parameter is required.
        self.resource_type = resource_type

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

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self


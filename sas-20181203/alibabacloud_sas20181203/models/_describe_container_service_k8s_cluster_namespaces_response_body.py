# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeContainerServiceK8sClusterNamespacesResponseBody(DaraModel):
    def __init__(
        self,
        k_8s_cluster_namespaces: List[main_models.DescribeContainerServiceK8sClusterNamespacesResponseBodyK8sClusterNamespaces] = None,
        request_id: str = None,
    ):
        # The namespaces.
        self.k_8s_cluster_namespaces = k_8s_cluster_namespaces
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.k_8s_cluster_namespaces:
            for v1 in self.k_8s_cluster_namespaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['K8sClusterNamespaces'] = []
        if self.k_8s_cluster_namespaces is not None:
            for k1 in self.k_8s_cluster_namespaces:
                result['K8sClusterNamespaces'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.k_8s_cluster_namespaces = []
        if m.get('K8sClusterNamespaces') is not None:
            for k1 in m.get('K8sClusterNamespaces'):
                temp_model = main_models.DescribeContainerServiceK8sClusterNamespacesResponseBodyK8sClusterNamespaces()
                self.k_8s_cluster_namespaces.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContainerServiceK8sClusterNamespacesResponseBodyK8sClusterNamespaces(DaraModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # The namespace.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self


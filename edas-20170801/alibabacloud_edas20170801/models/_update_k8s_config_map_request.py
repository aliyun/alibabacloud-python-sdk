# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateK8sConfigMapRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data: Dict[str, Any] = None,
        name: str = None,
        namespace: str = None,
    ):
        # The ID of the Kubernetes cluster.
        self.cluster_id = cluster_id
        # The data of the ConfigMap. Set this parameter to a JSON string.
        self.data = data
        # The name of the ConfigMap. The name must start with a letter, and can contain digits, letters, and hyphens (-). It can be up to 63 characters in length.
        self.name = name
        # The namespace of the Kubernetes cluster.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data is not None:
            result['Data'] = self.data

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self


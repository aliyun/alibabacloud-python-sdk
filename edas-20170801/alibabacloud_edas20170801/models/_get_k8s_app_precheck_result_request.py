# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetK8sAppPrecheckResultRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        namespace: str = None,
    ):
        # The name of the application.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The ID of the cluster in Enterprise Distributed Application Service (EDAS).
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The namespace of the Kubernetes cluster.
        # 
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self


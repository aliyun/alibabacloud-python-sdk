# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateClusterDiagnosisRequest(DaraModel):
    def __init__(
        self,
        target: Dict[str, Any] = None,
        type: str = None,
    ):
        # The parameter used to specify the diagnostic object. Examples of parameters for different types of diagnostic objects:
        # 
        # node:
        # 
        #     {"name": "cn-shanghai.10.10.10.107"}
        # 
        # pod
        # 
        #     {"namespace": "kube-system", "name": "csi-plugin-2cg9f"}
        # 
        # network
        # 
        #     {"src": "10.10.10.108", "dst": "10.11.247.16", "dport": "80"}
        # 
        # ingress
        # 
        #     {"url": "https://example.com"}
        # 
        # memory
        # 
        #     {"node":"cn-hangzhou.172.16.9.240"}
        # 
        # service
        # 
        #     {"namespace": "kube-system", "name": "nginx-ingress-lb"}
        self.target = target
        # The type of the diagnostic.
        # 
        # Valid values:
        # 
        # *   node
        # *   ingress
        # *   cluster
        # *   memory
        # *   pod
        # *   service
        # *   network
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target is not None:
            result['target'] = self.target

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self


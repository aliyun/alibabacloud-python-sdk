# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportK8sClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        enable_asm: bool = None,
        mode: int = None,
        namespace_id: str = None,
    ):
        # The ID of the ACK cluster or serverless Kubernetes cluster. You can obtain the cluster ID by calling the GetK8sCluster operation. For more information, see [GetK8sCluster](https://help.aliyun.com/document_detail/181437.html).
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to enable the integration with Alibaba Cloud Service Mesh (ASM). Valid values:
        # 
        # - true: Enables the integration with ASM.
        # 
        # - false: Disables the integration with ASM.
        self.enable_asm = enable_asm
        # You can ignore this parameter.
        self.mode = mode
        # The ID of the namespace. It is in the format of `Region ID:Identifier of the microservices namespace`. Example: `cn-hangzhou:doc`.
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.enable_asm is not None:
            result['EnableAsm'] = self.enable_asm

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EnableAsm') is not None:
            self.enable_asm = m.get('EnableAsm')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class GetFabricTopologyResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.GetFabricTopologyResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Content') is not None:
            temp_model = main_models.GetFabricTopologyResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFabricTopologyResponseBodyContent(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        topo_info: List[main_models.GetFabricTopologyResponseBodyContentTopoInfo] = None,
        vpc_id: str = None,
        vpd_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The region ID.
        self.region_id = region_id
        # network interface controller Topology Information
        self.topo_info = topo_info
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # Lingjun CIDR block ID
        self.vpd_id = vpd_id

    def validate(self):
        if self.topo_info:
            for v1 in self.topo_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['TopoInfo'] = []
        if self.topo_info is not None:
            for k1 in self.topo_info:
                result['TopoInfo'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.topo_info = []
        if m.get('TopoInfo') is not None:
            for k1 in m.get('TopoInfo'):
                temp_model = main_models.GetFabricTopologyResponseBodyContentTopoInfo()
                self.topo_info.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        return self

class GetFabricTopologyResponseBodyContentTopoInfo(DaraModel):
    def __init__(
        self,
        layer_name: str = None,
        layer_type: str = None,
        next_layer: List[Any] = None,
    ):
        # The resource name.
        self.layer_name = layer_name
        # Hierarchical resource types
        # 
        # Valid value:
        # 
        # *   core: core layer.
        # *   node: Lingjun node.
        # *   lni: lingjun network interface controller.
        # *   spine: backbone layer.
        # *   leaf: access layer
        self.layer_type = layer_type
        # Next Level
        self.next_layer = next_layer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.layer_name is not None:
            result['LayerName'] = self.layer_name

        if self.layer_type is not None:
            result['LayerType'] = self.layer_type

        if self.next_layer is not None:
            result['NextLayer'] = self.next_layer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayerName') is not None:
            self.layer_name = m.get('LayerName')

        if m.get('LayerType') is not None:
            self.layer_type = m.get('LayerType')

        if m.get('NextLayer') is not None:
            self.next_layer = m.get('NextLayer')

        return self


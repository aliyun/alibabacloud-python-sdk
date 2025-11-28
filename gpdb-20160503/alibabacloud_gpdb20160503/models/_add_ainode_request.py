# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class AddAINodeRequest(DaraModel):
    def __init__(
        self,
        ainode_pool_id: str = None,
        ainode_spec_infos: List[main_models.AddAINodeRequestAINodeSpecInfos] = None,
        dbinstance_id: str = None,
    ):
        # The ID of the resource pool to which the AI node belongs.
        self.ainode_pool_id = ainode_pool_id
        # The AI node specifications.
        # 
        # This parameter is required.
        self.ainode_spec_infos = ainode_spec_infos
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        if self.ainode_spec_infos:
            for v1 in self.ainode_spec_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ainode_pool_id is not None:
            result['AINodePoolId'] = self.ainode_pool_id

        result['AINodeSpecInfos'] = []
        if self.ainode_spec_infos is not None:
            for k1 in self.ainode_spec_infos:
                result['AINodeSpecInfos'].append(k1.to_map() if k1 else None)

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AINodePoolId') is not None:
            self.ainode_pool_id = m.get('AINodePoolId')

        self.ainode_spec_infos = []
        if m.get('AINodeSpecInfos') is not None:
            for k1 in m.get('AINodeSpecInfos'):
                temp_model = main_models.AddAINodeRequestAINodeSpecInfos()
                self.ainode_spec_infos.append(temp_model.from_map(k1))

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self



class AddAINodeRequestAINodeSpecInfos(DaraModel):
    def __init__(
        self,
        node_num: str = None,
        node_spec: str = None,
    ):
        # The number of AI nodes.
        # 
        # This parameter is required.
        self.node_num = node_num
        # The AI node specifications.
        # 
        #     ADB.AIStandard.1
        #     ADB.AIMedium.1
        #     ADB.AILarge.1
        #     ADB.AIStandard.2
        #     ADB.AIMedium.2
        #     ADB.AILarge.2
        #     ADB.AIXLarge.2
        #     ADB.AIStandard.6
        #     ADB.AIMedium.6
        #     ADB.AILarge.6
        #     ADB.AIXLarge.6
        #     ADB.AIStandard.3
        #     ADB.AIMedium.3
        #     ADB.AILarge.3
        #     ADB.AIXLarge.3
        #     ADB.AIStandard.4
        #     ADB.AIMedium.4
        #     ADB.AILarge.4
        #     ADB.AIXLarge.4
        #     ADB.AIStandard.5
        #     ADB.AIMedium.5
        #     ADB.AILarge.5
        #     ADB.AIXLarge.5
        #     ADB.AIStandard.8
        #     ADB.AIMedium.8
        #     ADB.AILarge.8
        #     ADB.AIXLarge.8
        #     ADB.AI2XLarge.8
        # 
        # This parameter is required.
        self.node_spec = node_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_num is not None:
            result['NodeNum'] = self.node_num

        if self.node_spec is not None:
            result['NodeSpec'] = self.node_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')

        if m.get('NodeSpec') is not None:
            self.node_spec = m.get('NodeSpec')

        return self


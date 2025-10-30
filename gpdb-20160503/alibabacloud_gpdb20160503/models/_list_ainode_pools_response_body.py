# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListAINodePoolsResponseBody(DaraModel):
    def __init__(
        self,
        ainode_pool_infos: List[main_models.ListAINodePoolsResponseBodyAINodePoolInfos] = None,
        request_id: str = None,
    ):
        self.ainode_pool_infos = ainode_pool_infos
        self.request_id = request_id

    def validate(self):
        if self.ainode_pool_infos:
            for v1 in self.ainode_pool_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AINodePoolInfos'] = []
        if self.ainode_pool_infos is not None:
            for k1 in self.ainode_pool_infos:
                result['AINodePoolInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ainode_pool_infos = []
        if m.get('AINodePoolInfos') is not None:
            for k1 in m.get('AINodePoolInfos'):
                temp_model = main_models.ListAINodePoolsResponseBodyAINodePoolInfos()
                self.ainode_pool_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAINodePoolsResponseBodyAINodePoolInfos(DaraModel):
    def __init__(
        self,
        ainode_infos: List[main_models.ListAINodePoolsResponseBodyAINodePoolInfosAINodeInfos] = None,
        ainode_pool_id: str = None,
        node_num: str = None,
    ):
        self.ainode_infos = ainode_infos
        self.ainode_pool_id = ainode_pool_id
        self.node_num = node_num

    def validate(self):
        if self.ainode_infos:
            for v1 in self.ainode_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AINodeInfos'] = []
        if self.ainode_infos is not None:
            for k1 in self.ainode_infos:
                result['AINodeInfos'].append(k1.to_map() if k1 else None)

        if self.ainode_pool_id is not None:
            result['AINodePoolId'] = self.ainode_pool_id

        if self.node_num is not None:
            result['NodeNum'] = self.node_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ainode_infos = []
        if m.get('AINodeInfos') is not None:
            for k1 in m.get('AINodeInfos'):
                temp_model = main_models.ListAINodePoolsResponseBodyAINodePoolInfosAINodeInfos()
                self.ainode_infos.append(temp_model.from_map(k1))

        if m.get('AINodePoolId') is not None:
            self.ainode_pool_id = m.get('AINodePoolId')

        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')

        return self

class ListAINodePoolsResponseBodyAINodePoolInfosAINodeInfos(DaraModel):
    def __init__(
        self,
        bind_object: str = None,
        bind_status: str = None,
        create_time: str = None,
        namespace: str = None,
        node_name: str = None,
        node_spec: str = None,
        update_time: str = None,
    ):
        self.bind_object = bind_object
        self.bind_status = bind_status
        self.create_time = create_time
        self.namespace = namespace
        self.node_name = node_name
        self.node_spec = node_spec
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_object is not None:
            result['BindObject'] = self.bind_object

        if self.bind_status is not None:
            result['BindStatus'] = self.bind_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_spec is not None:
            result['NodeSpec'] = self.node_spec

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindObject') is not None:
            self.bind_object = m.get('BindObject')

        if m.get('BindStatus') is not None:
            self.bind_status = m.get('BindStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeSpec') is not None:
            self.node_spec = m.get('NodeSpec')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self


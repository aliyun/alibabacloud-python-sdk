# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class AttachNodesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        compute_node: main_models.AttachNodesRequestComputeNode = None,
        queue_name: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The list of compute nodes.
        # 
        # This parameter is required.
        self.compute_node = compute_node
        # The name of the queue to which the instance is to be added.
        self.queue_name = queue_name

    def validate(self):
        if self.compute_node:
            self.compute_node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.compute_node is not None:
            result['ComputeNode'] = self.compute_node.to_map()

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComputeNode') is not None:
            temp_model = main_models.AttachNodesRequestComputeNode()
            self.compute_node = temp_model.from_map(m.get('ComputeNode'))

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        return self

class AttachNodesRequestComputeNode(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        instance_ids: List[str] = None,
    ):
        # The image ID. This image will be used to replace the original system disk image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The IDs of ECS instances.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        return self


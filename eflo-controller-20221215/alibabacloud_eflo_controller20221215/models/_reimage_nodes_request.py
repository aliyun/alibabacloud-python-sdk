# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ReimageNodesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        nodes: List[main_models.ReimageNodesRequestNodes] = None,
        user_data: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The nodes.
        self.nodes = nodes
        # The user data.
        self.user_data = user_data

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ReimageNodesRequestNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class ReimageNodesRequestNodes(DaraModel):
    def __init__(
        self,
        hostname: str = None,
        image_id: str = None,
        login_password: str = None,
        node_id: str = None,
    ):
        # The hostname.
        self.hostname = hostname
        # The system image ID.
        self.image_id = image_id
        # The logon password.
        self.login_password = login_password
        # The node ID.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.login_password is not None:
            result['LoginPassword'] = self.login_password

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ListNodePodsResponseBody(DaraModel):
    def __init__(
        self,
        node_pod_infos: List[main_models.NodePodInfo] = None,
        request_id: str = None,
    ):
        # The node pod information.
        self.node_pod_infos = node_pod_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.node_pod_infos:
            for v1 in self.node_pod_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodePodInfos'] = []
        if self.node_pod_infos is not None:
            for k1 in self.node_pod_infos:
                result['NodePodInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_pod_infos = []
        if m.get('NodePodInfos') is not None:
            for k1 in m.get('NodePodInfos'):
                temp_model = main_models.NodePodInfo()
                self.node_pod_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


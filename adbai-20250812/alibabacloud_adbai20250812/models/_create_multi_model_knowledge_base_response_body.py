# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMultiModelKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        mmkb_name: str = None,
        request_id: str = None,
    ):
        # The ID of the created AnalyticDB for MySQL cluster.
        self.db_cluster_id = db_cluster_id
        # The name of the created multimodal knowledge engine service.
        self.mmkb_name = mmkb_name
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id

        if self.mmkb_name is not None:
            result['MmkbName'] = self.mmkb_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')

        if m.get('MmkbName') is not None:
            self.mmkb_name = m.get('MmkbName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


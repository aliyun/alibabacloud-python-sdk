# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class ClusterState(DaraModel):
    def __init__(
        self,
        cluster_stage: main_models.ClusterStage = None,
        status: str = None,
        sub_status: str = None,
    ):
        self.cluster_stage = cluster_stage
        self.status = status
        self.sub_status = sub_status

    def validate(self):
        if self.cluster_stage:
            self.cluster_stage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_stage is not None:
            result['ClusterStage'] = self.cluster_stage.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterStage') is not None:
            temp_model = main_models.ClusterStage()
            self.cluster_stage = temp_model.from_map(m.get('ClusterStage'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        return self


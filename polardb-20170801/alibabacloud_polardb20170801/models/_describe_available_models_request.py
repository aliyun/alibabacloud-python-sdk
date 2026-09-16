# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailableModelsRequest(DaraModel):
    def __init__(
        self,
        kube_type: str = None,
        model_type: str = None,
        region_id: str = None,
    ):
        # aideploy
        self.kube_type = kube_type
        # The model type. Valid values: custom or public. If this parameter is not specified, all models are returned.
        self.model_type = model_type
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kube_type is not None:
            result['KubeType'] = self.kube_type

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KubeType') is not None:
            self.kube_type = m.get('KubeType')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


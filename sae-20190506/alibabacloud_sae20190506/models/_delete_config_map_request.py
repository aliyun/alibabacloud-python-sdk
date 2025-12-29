# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteConfigMapRequest(DaraModel):
    def __init__(
        self,
        config_map_id: int = None,
    ):
        # The ID of the ConfigMap that you want to delete. You can call the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) operation to obtain the ID of a ConfigMap.
        # 
        # This parameter is required.
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')

        return self


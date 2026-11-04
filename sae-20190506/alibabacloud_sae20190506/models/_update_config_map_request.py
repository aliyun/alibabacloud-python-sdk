# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConfigMapRequest(DaraModel):
    def __init__(
        self,
        config_map_id: int = None,
        data: str = None,
        description: str = None,
    ):
        # Instance ID of the ConfigMap instance to be updated. To obtain instance ID, call the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) operation.
        # 
        # This parameter is required.
        self.config_map_id = config_map_id
        # The key-value pair data of the ConfigMap in JSON format. The format is as follows:
        # 
        # {"Data":"{\\"k1\\":\\"v1\\", \\"k2\\":\\"v2\\"}"}
        # 
        # k represents the key and v represents the value. For more information about ConfigMaps, see [Manage and use ConfigMaps](https://help.aliyun.com/document_detail/171326.html).
        # 
        # This parameter is required.
        self.data = data
        # The description.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id

        if self.data is not None:
            result['Data'] = self.data

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self


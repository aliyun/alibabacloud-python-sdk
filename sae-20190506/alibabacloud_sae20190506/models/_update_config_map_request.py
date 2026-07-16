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
        # The ID of the ConfigMap instance that you want to update. To view the ID, call the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) operation.
        # 
        # This parameter is required.
        self.config_map_id = config_map_id
        # The key-value pairs for the ConfigMap. The value must be a JSON-formatted string, as shown in the following example:
        # 
        # {"Data":"{"k1":"v1", "k2":"v2"}"}
        # 
        # In the JSON string, k represents a key and v represents a value. For more information about configuration items, see [Managing and using configuration items](https://help.aliyun.com/document_detail/171326.html).
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


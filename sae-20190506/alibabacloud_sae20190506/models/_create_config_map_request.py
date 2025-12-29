# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConfigMapRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
    ):
        # The ConfigMap data.
        # 
        # This parameter is required.
        self.data = data
        # The key-value pairs of the ConfigMap in the JSON format. Format:
        # 
        # {"Data":"{"k1":"v1", "k2":"v2"}"}
        # 
        # k specifies a key and v specifies a value. For more information, see [Manage a Kubernetes ConfigMap](https://help.aliyun.com/document_detail/171326.html).
        self.description = description
        # The name of the ConfigMap. The name can contain digits, letters, and underscores (_). The name must start with a letter.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the namespace to which the ConfigMap instance belongs.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self


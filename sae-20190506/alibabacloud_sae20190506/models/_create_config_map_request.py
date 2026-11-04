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
        # The key-value pair data of the ConfigMap in JSON format. The format is as follows:
        # 
        # {"Data":"{\\"k1\\":\\"v1\\", \\"k2\\":\\"v2\\"}"}
        # 
        # k represents the key, and v represents the value. For more information about ConfigMaps, see [Manage and use ConfigMaps](https://help.aliyun.com/document_detail/171326.html).
        # 
        # This parameter is required.
        self.data = data
        # The description. The description cannot contain spaces and can be up to 255 characters in length.
        self.description = description
        # The name of the ConfigMap instance. The name can contain digits, letters, and underscores (_), and must start with a letter.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the namespace where the ConfigMap instance resides.
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


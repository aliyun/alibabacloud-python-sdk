# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecretRequest(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        secret_id: int = None,
    ):
        # The ID of the namespace where the Secret resides. If the namespace is the default namespace, you need to only enter the region ID, such as `cn-beijing`.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The ID of the Secret instance to be queried. You can call the [ListSecrets](https://help.aliyun.com/document_detail/466929.html) operation to view the IDs of Secrete instances.
        # 
        # This parameter is required.
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        return self


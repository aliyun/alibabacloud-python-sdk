# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSecretRequest(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        secret_id: int = None,
    ):
        # The ID of the namespace in which the Secret resides. By default, the namespace ID is the same as the region ID.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The ID of the Secret to be deleted. You can call the [ListSecrets](https://help.aliyun.com/document_detail/466929.html) operation to view the Secret IDs.
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


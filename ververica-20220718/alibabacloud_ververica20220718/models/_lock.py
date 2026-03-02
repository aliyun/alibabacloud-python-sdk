# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Lock(DaraModel):
    def __init__(
        self,
        holder_id: str = None,
        holder_name: str = None,
        id: str = None,
        namespace: str = None,
        workspace: str = None,
    ):
        # The ID of the lock holder.
        self.holder_id = holder_id
        # The username of the lock holder.
        self.holder_name = holder_name
        # The lock ID.
        self.id = id
        # The name of the namespace.
        self.namespace = namespace
        # The workspace ID.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.holder_id is not None:
            result['holderId'] = self.holder_id

        if self.holder_name is not None:
            result['holderName'] = self.holder_name

        if self.id is not None:
            result['id'] = self.id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('holderId') is not None:
            self.holder_id = m.get('holderId')

        if m.get('holderName') is not None:
            self.holder_name = m.get('holderName')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self


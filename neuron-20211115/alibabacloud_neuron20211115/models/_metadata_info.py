# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetadataInfo(DaraModel):
    def __init__(
        self,
        enterprise_id: int = None,
        env: str = None,
        id: int = None,
        instance_id: int = None,
        namespace_id: int = None,
        namespace_name: str = None,
        org_id: int = None,
    ):
        self.enterprise_id = enterprise_id
        # This parameter is required.
        self.env = env
        self.id = id
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        # This parameter is required.
        self.namespace_name = namespace_name
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.env is not None:
            result['env'] = self.env

        if self.id is not None:
            result['id'] = self.id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['namespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.org_id is not None:
            result['orgId'] = self.org_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('namespaceId') is not None:
            self.namespace_id = m.get('namespaceId')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        return self


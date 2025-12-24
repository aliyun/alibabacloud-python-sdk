# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceInstanceRequest(DaraModel):
    def __init__(
        self,
        is_replica: bool = None,
        detach: bool = None,
        hibernate: bool = None,
        isolate: bool = None,
    ):
        self.is_replica = is_replica
        self.detach = detach
        self.hibernate = hibernate
        # Specifies whether to isolate the service instance. Valid values:
        # 
        # *   true
        # *   false
        self.isolate = isolate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_replica is not None:
            result['IsReplica'] = self.is_replica

        if self.detach is not None:
            result['Detach'] = self.detach

        if self.hibernate is not None:
            result['Hibernate'] = self.hibernate

        if self.isolate is not None:
            result['Isolate'] = self.isolate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsReplica') is not None:
            self.is_replica = m.get('IsReplica')

        if m.get('Detach') is not None:
            self.detach = m.get('Detach')

        if m.get('Hibernate') is not None:
            self.hibernate = m.get('Hibernate')

        if m.get('Isolate') is not None:
            self.isolate = m.get('Isolate')

        return self


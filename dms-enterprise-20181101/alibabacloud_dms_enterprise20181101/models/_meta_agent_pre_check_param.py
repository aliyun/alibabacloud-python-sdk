# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetaAgentPreCheckParam(DaraModel):
    def __init__(
        self,
        db_ids: str = None,
        description: str = None,
        instance_ids: str = None,
        supplement: str = None,
        table_names: str = None,
    ):
        self.db_ids = db_ids
        self.description = description
        self.instance_ids = instance_ids
        self.supplement = supplement
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_ids is not None:
            result['DbIds'] = self.db_ids

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.supplement is not None:
            result['Supplement'] = self.supplement

        if self.table_names is not None:
            result['TableNames'] = self.table_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbIds') is not None:
            self.db_ids = m.get('DbIds')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Supplement') is not None:
            self.supplement = m.get('Supplement')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        return self


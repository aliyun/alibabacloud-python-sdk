# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScriptProfileTemplatesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        nlu_engine: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The NLU engine type.
        self.nlu_engine = nlu_engine

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        return self


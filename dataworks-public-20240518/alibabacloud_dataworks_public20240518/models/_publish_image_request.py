# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishImageRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        process_id: str = None,
    ):
        # The image ID.
        # 
        # This parameter is required.
        self.id = id
        # The image publish execution ID, which is used as an idempotence identifier.
        self.process_id = process_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        return self


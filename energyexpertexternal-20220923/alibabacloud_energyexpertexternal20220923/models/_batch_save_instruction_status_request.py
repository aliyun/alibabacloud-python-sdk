# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSaveInstructionStatusRequest(DaraModel):
    def __init__(
        self,
        factory_id: str = None,
        p_key: str = None,
        status_list: str = None,
    ):
        # This parameter is required.
        self.factory_id = factory_id
        self.p_key = p_key
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id

        if self.p_key is not None:
            result['pKey'] = self.p_key

        if self.status_list is not None:
            result['statusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')

        if m.get('pKey') is not None:
            self.p_key = m.get('pKey')

        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')

        return self


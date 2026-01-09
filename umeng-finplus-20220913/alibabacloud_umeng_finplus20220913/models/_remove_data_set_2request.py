# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveDataSet2Request(DaraModel):
    def __init__(
        self,
        client_id: int = None,
        data_set_id: int = None,
    ):
        self.client_id = client_id
        self.data_set_id = data_set_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.data_set_id is not None:
            result['dataSetId'] = self.data_set_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('dataSetId') is not None:
            self.data_set_id = m.get('dataSetId')

        return self


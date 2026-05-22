# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCnameFlatteningResponseBody(DaraModel):
    def __init__(
        self,
        flatten_mode: str = None,
        request_id: str = None,
    ):
        # The CNAME flattening mode. Valid values:
        # 
        # *   flatten_all: flattens all CNAMEs.
        # *   flatten_all (default): flattens only the root domain.
        self.flatten_mode = flatten_mode
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flatten_mode is not None:
            result['FlattenMode'] = self.flatten_mode

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlattenMode') is not None:
            self.flatten_mode = m.get('FlattenMode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


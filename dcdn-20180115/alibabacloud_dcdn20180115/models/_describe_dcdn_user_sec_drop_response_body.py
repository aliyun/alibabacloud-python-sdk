# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnUserSecDropResponseBody(DaraModel):
    def __init__(
        self,
        drops: int = None,
        msg: str = None,
        request_id: str = None,
        uuid_str: str = None,
    ):
        # The number of packets that are blocked.
        self.drops = drops
        # Indicates whether the information is found.
        # 
        # *   Found
        # *   Not Found
        self.msg = msg
        # The ID of the request.
        self.request_id = request_id
        # The character string that is concatenated based on the request parameters and is used to locate causes when data is not found.
        self.uuid_str = uuid_str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drops is not None:
            result['Drops'] = self.drops

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.uuid_str is not None:
            result['UuidStr'] = self.uuid_str

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Drops') is not None:
            self.drops = m.get('Drops')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UuidStr') is not None:
            self.uuid_str = m.get('UuidStr')

        return self


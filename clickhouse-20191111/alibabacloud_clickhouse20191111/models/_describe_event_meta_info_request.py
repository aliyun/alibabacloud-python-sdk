# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventMetaInfoRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        security_token: str = None,
        source_code: str = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        self.security_token = security_token
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        return self


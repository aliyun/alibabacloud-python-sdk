# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class PutLogsHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_log_compresstype: str = None,
    ):
        self.common_headers = common_headers
        # The compression format. lz4 and gzip are supported.
        # 
        # This parameter is required.
        self.x_log_compresstype = x_log_compresstype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.x_log_compresstype is not None:
            result['x-log-compresstype'] = self.x_log_compresstype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('x-log-compresstype') is not None:
            self.x_log_compresstype = m.get('x-log-compresstype')

        return self


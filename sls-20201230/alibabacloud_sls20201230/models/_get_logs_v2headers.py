# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class GetLogsV2Headers(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        accept_encoding: str = None,
    ):
        self.common_headers = common_headers
        # The compression method for the response content. SDK users do not need to specify this parameter because the SDK automatically handles compression and decompression.
        # 
        # - Java, Python, and Go currently support lz4 and gzip decompression.
        # 
        # - php, JavaScript, and C# currently support only gzip decompression.
        self.accept_encoding = accept_encoding

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.accept_encoding is not None:
            result['Accept-Encoding'] = self.accept_encoding

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('Accept-Encoding') is not None:
            self.accept_encoding = m.get('Accept-Encoding')

        return self


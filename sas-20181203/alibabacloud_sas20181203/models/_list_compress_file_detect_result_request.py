# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCompressFileDetectResultRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        hash_key: str = None,
        page_size: int = None,
        source_ip: str = None,
    ):
        # The page number. Default value: 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The identifier of the file. Only MD5 hash values are supported.
        self.hash_key = hash_key
        # The number of entries per page. Default value: 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self


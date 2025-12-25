# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKvsRequest(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
        prefix: str = None,
    ):
        # The name of the namespace that you specify when you call the [CreatevNamespace](https://help.aliyun.com/document_detail/2850317.html) operation.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The page number. The product of PageNumber and PageSize cannot exceed 50,000.
        self.page_number = page_number
        # The number of entries per page. Default value: 50. Maximum value: 100.
        self.page_size = page_size
        # The prefix to query.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        return self


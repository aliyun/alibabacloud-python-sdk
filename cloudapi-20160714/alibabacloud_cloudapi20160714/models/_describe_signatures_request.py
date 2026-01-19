# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSignaturesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        signature_id: str = None,
        signature_name: str = None,
    ):
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        self.security_token = security_token
        # The IDs of the keys to query.
        self.signature_id = signature_id
        # The names of the keys to query.
        self.signature_name = signature_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id

        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')

        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')

        return self


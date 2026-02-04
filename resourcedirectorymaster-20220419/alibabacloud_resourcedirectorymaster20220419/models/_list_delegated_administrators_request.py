# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDelegatedAdministratorsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        service_principal: str = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The identifier of the trusted service.
        # 
        # For more information, see the `Trusted service identifier` column in [Supported trusted services](https://help.aliyun.com/document_detail/208133.html).
        self.service_principal = service_principal

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

        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')

        return self


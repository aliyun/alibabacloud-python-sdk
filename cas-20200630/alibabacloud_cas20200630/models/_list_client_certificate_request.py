# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClientCertificateRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        identifier: str = None,
        resource_group_id: str = None,
        show_size: int = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The unique identifier of the client certificate or the server certificate that you want to query.
        # 
        # >  You can call the [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) operation to query the unique identifiers of all client certificates and server certificates.
        self.identifier = identifier
        self.resource_group_id = resource_group_id
        # The number of certificates to return on each page. Default value: **20**.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        return self


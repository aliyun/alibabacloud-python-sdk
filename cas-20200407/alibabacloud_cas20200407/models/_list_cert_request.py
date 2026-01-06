# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCertRequest(DaraModel):
    def __init__(
        self,
        cert_type: str = None,
        current_page: int = None,
        key_word: str = None,
        show_size: int = None,
        source_type: str = None,
        status: str = None,
        warehouse_id: int = None,
    ):
        # 证书的类型 。取值：
        # 
        # - **CA**：表示CA证书。
        # - **CERT**：表示签发的证书。
        self.cert_type = cert_type
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # The keyword for the query. You can enter a name, domain name, or Subject Alternative Name (SAN) extension. Fuzzy match is supported.
        self.key_word = key_word
        # The number of entries to return on each page. Default value: 50.
        self.show_size = show_size
        # The source of the certificate. Valid values:
        # 
        # *   **upload**: uploaded certificate
        # *   **aliyun**: Alibaba Cloud certificate
        self.source_type = source_type
        # The status of the certificate. Valid values:
        # 
        # *   **ISSUE**: issued
        # *   **REVOKE**: revoked
        self.status = status
        # The ID of the certificate repository. You can call the ListCertWarehouse API operation to query the IDs of certificate repositories.
        self.warehouse_id = warehouse_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.status is not None:
            result['Status'] = self.status

        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')

        return self


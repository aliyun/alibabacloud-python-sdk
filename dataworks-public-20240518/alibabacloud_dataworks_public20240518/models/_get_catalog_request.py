# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCatalogRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The catalog entity ID. Currently supports dlf and starrocks types. You can refer to the results returned by the ListCatalogs operation and the [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # *   For the DLF type, the format is `dlf-catalog::catalog_id`.
        # *   For the StarRocks type, the format is `starrocks-catalog:(instance_id|encoded_jdbc_url):catalog_name`.
        # 
        # > \\
        # `catalog_id`: The ID of the DLF catalog.\\
        # `instance_id`: The instance ID, required if the data source is registered in instance mode.\\
        # `encoded_jdbc_url`: The URL-encoded JDBC connection string. Required if the data source is registered in connection string mode.\\
        # `catalog_name`: The name of the StarRocks catalog.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self


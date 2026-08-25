# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCatalogRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The ID of the data catalog entity. Currently, DLF and StarRocks types are supported. You can obtain the ID from the response of the ListCatalogs operation. For more information, see [Metadata entity concepts](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # 
        # - For the DLF type, the format is `dlf-catalog::catalog_id`.
        # 
        # - For the StarRocks type, the format is `starrocks-catalog:(instance_id|encoded_jdbc_url):catalog_name`.
        # 
        # > Where  
        # `catalog_id`: the ID of the DLF catalog.  
        # `instance_id`: the instance ID, which is required when the data source is registered in instance mode.  
        # `encoded_jdbc_url`: the URL-encoded JDBC connection string, which is required when the data source is registered in connection string mode.  
        # `catalog_name`: the name of the StarRocks catalog.
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


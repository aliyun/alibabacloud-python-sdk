# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataSourceTableFieldsRequest(DaraModel):
    def __init__(
        self,
        params: str = None,
        raw_type: bool = None,
    ):
        # The parameters of the data source. The value of the params parameter is a JSON string. The value must be URL-encoded.
        # 
        # Different types of data sources use different parameters. For more information, see the following sections of the "DataSource" topic:
        # 
        # *   [rds](https://help.aliyun.com/document_detail/170005.html)
        # *   [polardb](https://help.aliyun.com/document_detail/170005.html)
        # *   [odps](https://help.aliyun.com/document_detail/170005.html)
        # *   [mysql](https://help.aliyun.com/document_detail/173627.html)
        # *   [drds](https://help.aliyun.com/document_detail/173627.html)
        # 
        # This parameter is required.
        self.params = params
        # Specifies whether to return the original field types of the data source.
        self.raw_type = raw_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.params is not None:
            result['params'] = self.params

        if self.raw_type is not None:
            result['rawType'] = self.raw_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('rawType') is not None:
            self.raw_type = m.get('rawType')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataSourceTablesRequest(DaraModel):
    def __init__(
        self,
        params: str = None,
    ):
        # The parameters of the data source. The value is a JSON string which must be encoded in the urlencode format.
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

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.params is not None:
            result['params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')

        return self


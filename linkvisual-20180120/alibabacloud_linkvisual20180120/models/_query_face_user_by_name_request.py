# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryFaceUserByNameRequest(DaraModel):
    def __init__(
        self,
        isolation_id: str = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        params: str = None,
    ):
        # The business isolation ID, which is used to isolate data between different business applications under the same Alibaba Cloud account. Make sure that this parameter is consistent with the **IsolationId** set when you call the [AddFaceUser](https://help.aliyun.com/document_detail/288338.html) operation to add a user.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The username. The name can contain Chinese characters, uppercase and lowercase letters, digits, underscores (_), and hyphens (-), and can be up to 64 characters in length.
        # 
        # Fuzzy match is supported. If this parameter is not specified, all records are matched.
        self.name = name
        # The page number of the page to return. Minimum value: 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries to return on each page. Maximum value: 50. Minimum value: 1.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The custom user parameters.
        # 
        # Exact match is supported, but fuzzy match is not supported.
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.params is not None:
            result['Params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        return self


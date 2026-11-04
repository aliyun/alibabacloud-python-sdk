# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNamespaceChangeOrdersRequest(DaraModel):
    def __init__(
        self,
        co_status: str = None,
        co_type: str = None,
        current_page: int = None,
        key: str = None,
        namespace_id: str = None,
        page_size: int = None,
    ):
        # The status of the change order. Valid values:
        # 
        # - **0**: preparing
        # - **1**: executing
        # - **2**: succeeded
        # - **3**: failed
        # - **6**: terminated
        # - **10**: failed due to a system exception
        self.co_status = co_status
        # The type of the change order. Valid values:
        # 
        # - **CoBatchStartApplication**: Starts applications in batches.
        # - **CoBatchStopApplication**: Stops applications in batches.
        self.co_type = co_type
        # The current page number.
        self.current_page = current_page
        # The keyword used for fuzzy matching of the change order description. All change orders whose descriptions contain this **key** are returned.
        self.key = key
        # The namespace ID.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.co_status is not None:
            result['CoStatus'] = self.co_status

        if self.co_type is not None:
            result['CoType'] = self.co_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.key is not None:
            result['Key'] = self.key

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')

        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


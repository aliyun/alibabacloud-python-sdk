# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeContainerAppsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        current_page: int = None,
        field_value: str = None,
        page_size: int = None,
    ):
        # The ID of the container cluster.
        self.cluster_id = cluster_id
        # The page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The application value that you want to query. Fuzzy match is supported.
        self.field_value = field_value
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


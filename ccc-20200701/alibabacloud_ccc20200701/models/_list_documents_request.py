# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListDocumentsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        next_page_token: str = None,
        page_size: int = None,
        request_id: str = None,
        schema_id: str = None,
        search_pattern: str = None,
        sorts: List[main_models.ListDocumentsRequestSorts] = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token for the next page of results.
        self.next_page_token = next_page_token
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The schema ID.
        # 
        # This parameter is required.
        self.schema_id = schema_id
        # The search conditional expression.
        self.search_pattern = search_pattern
        # The custom sorting value.
        self.sorts = sorts

    def validate(self):
        if self.sorts:
            for v1 in self.sorts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        if self.search_pattern is not None:
            result['SearchPattern'] = self.search_pattern

        result['Sorts'] = []
        if self.sorts is not None:
            for k1 in self.sorts:
                result['Sorts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        if m.get('SearchPattern') is not None:
            self.search_pattern = m.get('SearchPattern')

        self.sorts = []
        if m.get('Sorts') is not None:
            for k1 in m.get('Sorts'):
                temp_model = main_models.ListDocumentsRequestSorts()
                self.sorts.append(temp_model.from_map(k1))

        return self

class ListDocumentsRequestSorts(DaraModel):
    def __init__(
        self,
        order: str = None,
        property_name: str = None,
    ):
        # The sorting order. Valid values:
        # 
        # - ASC (default): ascending order.
        # 
        # - DESC: descending order.
        self.order = order
        # The field name.
        self.property_name = property_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order

        if self.property_name is not None:
            result['PropertyName'] = self.property_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')

        return self


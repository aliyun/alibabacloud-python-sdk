# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductsRequest(DaraModel):
    def __init__(
        self,
        category_ids: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        portal_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The product category IDs, which correspond to the Categories property of the API product resource. The members are category IDs.
        self.category_ids = category_ids
        # The maximum number of entries to return per request.
        self.max_results = max_results
        # The name of the API product, which is the Name property of the API product resource. This is the same field as name in the response list items.
        self.name = name
        # The cursor token for the next page.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The ID of the HiMarket developer portal where the API product is published, which corresponds to the PortalId property of the API product resource. This property is used only for list queries in the product resource definition.
        self.portal_id = portal_id
        # The status of the API product, which corresponds to the Status property of the API product resource. This is the same field as status in the response list items. Valid values: Pending, Ready, and Published.
        self.status = status
        # The type of the API product, which corresponds to the Type property of the API product resource. This is the same field as type in the response list items. The valid values are not declared in the API definition. Refer to the types displayed in the console.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_ids is not None:
            result['categoryIds'] = self.category_ids

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.portal_id is not None:
            result['portalId'] = self.portal_id

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryIds') is not None:
            self.category_ids = m.get('categoryIds')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('portalId') is not None:
            self.portal_id = m.get('portalId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self


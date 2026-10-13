# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListPortalPublicationsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListPortalPublicationsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListPortalPublicationsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListPortalPublicationsResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListPortalPublicationsResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of published API products on the portal. The list elements are named portalConfig, and each element represents an API product publication record.
        self.content = content
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of items.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.ListPortalPublicationsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListPortalPublicationsResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        publication_id: str = None,
    ):
        # The creation time in ISO 8601 (RFC 3339) format in the UTC time zone, such as 2026-05-15T10:00:00Z.
        self.created_at = created_at
        # The description of the API product.
        self.description = description
        # The API product ID. This is the primary ID of the Product resource, which identifies the API product associated with this publication record.
        self.product_id = product_id
        # The API product name. This is the Name property of the Product resource.
        self.product_name = product_name
        # The API product type. The valid values are not defined in the API specification. Refer to the types displayed in the console.
        self.product_type = product_type
        # The publication record ID of the API product. This ID is returned when the PublishProduct operation publishes the API product to the portal. You can use it in the /himarket/v1/products/{productId}/publications/{publicationId} path to locate the publication record for the UnpublishProduct operation.
        self.publication_id = publication_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.product_type is not None:
            result['productType'] = self.product_type

        if self.publication_id is not None:
            result['publicationId'] = self.publication_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('productType') is not None:
            self.product_type = m.get('productType')

        if m.get('publicationId') is not None:
            self.publication_id = m.get('publicationId')

        return self


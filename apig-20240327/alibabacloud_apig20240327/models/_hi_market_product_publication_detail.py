# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HiMarketProductPublicationDetail(DaraModel):
    def __init__(
        self,
        portal_id: str = None,
        portal_name: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        publication_id: str = None,
    ):
        self.portal_id = portal_id
        self.portal_name = portal_name
        self.product_id = product_id
        self.product_name = product_name
        self.product_type = product_type
        self.publication_id = publication_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.portal_id is not None:
            result['portalId'] = self.portal_id

        if self.portal_name is not None:
            result['portalName'] = self.portal_name

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
        if m.get('portalId') is not None:
            self.portal_id = m.get('portalId')

        if m.get('portalName') is not None:
            self.portal_name = m.get('portalName')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('productType') is not None:
            self.product_type = m.get('productType')

        if m.get('publicationId') is not None:
            self.publication_id = m.get('publicationId')

        return self


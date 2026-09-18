# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQuotasRequest(DaraModel):
    def __init__(
        self,
        billing_type: str = None,
        marker: str = None,
        max_item: int = None,
        product_id: str = None,
        region: str = None,
        sale_tags: str = None,
        tenant_id: str = None,
    ):
        # The billing method.
        self.billing_type = billing_type
        # The token that specifies the position from which to start returning results. The results are sorted in alphabetical order.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        self.product_id = product_id
        self.region = region
        # The cost allocation tags that are used to filter quotas. You can create cost allocation tags in the Tag service.
        self.sale_tags = sale_tags
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_type is not None:
            result['billingType'] = self.billing_type

        if self.marker is not None:
            result['marker'] = self.marker

        if self.max_item is not None:
            result['maxItem'] = self.max_item

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.region is not None:
            result['region'] = self.region

        if self.sale_tags is not None:
            result['saleTags'] = self.sale_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingType') is not None:
            self.billing_type = m.get('billingType')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('saleTags') is not None:
            self.sale_tags = m.get('saleTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


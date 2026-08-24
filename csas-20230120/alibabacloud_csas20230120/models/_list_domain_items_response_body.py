# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListDomainItemsResponseBody(DaraModel):
    def __init__(
        self,
        domain_items: List[main_models.ListDomainItemsResponseBodyDomainItems] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # The list of domain name entries.
        self.domain_items = domain_items
        # Id of the request
        self.request_id = request_id
        # The total number of records that match the specified conditions. This is an optional parameter and may not be returned by default.
        self.total_num = total_num

    def validate(self):
        if self.domain_items:
            for v1 in self.domain_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainItems'] = []
        if self.domain_items is not None:
            for k1 in self.domain_items:
                result['DomainItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_items = []
        if m.get('DomainItems') is not None:
            for k1 in m.get('DomainItems'):
                temp_model = main_models.ListDomainItemsResponseBodyDomainItems()
                self.domain_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListDomainItemsResponseBodyDomainItems(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        item_id: int = None,
        item_value: str = None,
    ):
        # The time when the entry was created.
        self.gmt_create = gmt_create
        # The time when the entry was last modified.
        self.gmt_modified = gmt_modified
        self.item_id = item_id
        # The domain name. Wildcard domain names are supported.
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.item_value is not None:
            result['ItemValue'] = self.item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')

        return self


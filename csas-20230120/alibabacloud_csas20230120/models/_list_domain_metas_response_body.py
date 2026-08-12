# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListDomainMetasResponseBody(DaraModel):
    def __init__(
        self,
        domain_metas: List[main_models.ListDomainMetasResponseBodyDomainMetas] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # The list of domain name lists.
        self.domain_metas = domain_metas
        # The request ID.
        self.request_id = request_id
        # The total number of lists that match the specified conditions.
        self.total_num = total_num

    def validate(self):
        if self.domain_metas:
            for v1 in self.domain_metas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainMetas'] = []
        if self.domain_metas is not None:
            for k1 in self.domain_metas:
                result['DomainMetas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_metas = []
        if m.get('DomainMetas') is not None:
            for k1 in m.get('DomainMetas'):
                temp_model = main_models.ListDomainMetasResponseBodyDomainMetas()
                self.domain_metas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListDomainMetasResponseBodyDomainMetas(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        item_count: int = None,
        list_id: str = None,
        list_type: str = None,
        name: str = None,
        resource_id: str = None,
    ):
        # The time when the list was created.
        self.gmt_create = gmt_create
        # The time when the list was last modified.
        self.gmt_modified = gmt_modified
        # The number of domain name entries in the list.
        self.item_count = item_count
        # The list ID, which is a unique business identifier used for policy references and CRUD operations.
        self.list_id = list_id
        # The list type.
        self.list_type = list_type
        # The list name.
        self.name = name
        # The resource ID.
        self.resource_id = resource_id

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

        if self.item_count is not None:
            result['ItemCount'] = self.item_count

        if self.list_id is not None:
            result['ListId'] = self.list_id

        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ItemCount') is not None:
            self.item_count = m.get('ItemCount')

        if m.get('ListId') is not None:
            self.list_id = m.get('ListId')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListListsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        query_args: main_models.ListListsRequestQueryArgs = None,
    ):
        # Specifies the page number for paginated results.
        self.page_number = page_number
        # Specifies the number of results to return per page.
        self.page_size = page_size
        # A JSON object containing query parameters to filter the results.
        self.query_args = query_args

    def validate(self):
        if self.query_args:
            self.query_args.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_args is not None:
            result['QueryArgs'] = self.query_args.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryArgs') is not None:
            temp_model = main_models.ListListsRequestQueryArgs()
            self.query_args = temp_model.from_map(m.get('QueryArgs'))

        return self

class ListListsRequestQueryArgs(DaraModel):
    def __init__(
        self,
        desc: bool = None,
        description_like: str = None,
        id_like: str = None,
        item_like: str = None,
        kind: str = None,
        name_item_like: str = None,
        name_like: str = None,
        order_by: str = None,
    ):
        # If true, sorts the results in descending order.
        self.desc = desc
        # Filters by a partial match on the list description.
        self.description_like = description_like
        # Filters by a partial match on the list ID.
        self.id_like = id_like
        # Filters by a partial match on a list item.
        self.item_like = item_like
        # Filters by the list kind.
        self.kind = kind
        # Filters by a partial match on both the list name and list items.
        self.name_item_like = name_item_like
        # Filters by a partial match on the list name.
        self.name_like = name_like
        # Specifies the sort field.
        self.order_by = order_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.description_like is not None:
            result['DescriptionLike'] = self.description_like

        if self.id_like is not None:
            result['IdLike'] = self.id_like

        if self.item_like is not None:
            result['ItemLike'] = self.item_like

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.name_item_like is not None:
            result['NameItemLike'] = self.name_item_like

        if self.name_like is not None:
            result['NameLike'] = self.name_like

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('DescriptionLike') is not None:
            self.description_like = m.get('DescriptionLike')

        if m.get('IdLike') is not None:
            self.id_like = m.get('IdLike')

        if m.get('ItemLike') is not None:
            self.item_like = m.get('ItemLike')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('NameItemLike') is not None:
            self.name_item_like = m.get('NameItemLike')

        if m.get('NameLike') is not None:
            self.name_like = m.get('NameLike')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        return self


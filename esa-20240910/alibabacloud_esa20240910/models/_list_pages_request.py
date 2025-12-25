# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListPagesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        query_args: main_models.ListPagesRequestQueryArgs = None,
    ):
        # The page number. Valid values: **1 to 100000**. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
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
            temp_model = main_models.ListPagesRequestQueryArgs()
            self.query_args = temp_model.from_map(m.get('QueryArgs'))

        return self

class ListPagesRequestQueryArgs(DaraModel):
    def __init__(
        self,
        name_description_like: str = None,
    ):
        self.name_description_like = name_description_like

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_description_like is not None:
            result['NameDescriptionLike'] = self.name_description_like

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameDescriptionLike') is not None:
            self.name_description_like = m.get('NameDescriptionLike')

        return self


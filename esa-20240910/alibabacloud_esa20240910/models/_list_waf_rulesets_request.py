# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListWafRulesetsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        phase: str = None,
        query_args: main_models.ListWafRulesetsRequestQueryArgs = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # Page number, specifying the current page number for paginated queries.
        self.page_number = page_number
        # Page size, specifying the number of records per page for paginated queries.
        self.page_size = page_size
        # WAF operation phase, specifying the rule set phase to query.
        self.phase = phase
        # Query parameters, passed in JSON format, containing various filtering conditions.
        self.query_args = query_args
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) interface.
        self.site_id = site_id
        # Site version.
        self.site_version = site_version

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

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.query_args is not None:
            result['QueryArgs'] = self.query_args.to_map()

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('QueryArgs') is not None:
            temp_model = main_models.ListWafRulesetsRequestQueryArgs()
            self.query_args = temp_model.from_map(m.get('QueryArgs'))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

class ListWafRulesetsRequestQueryArgs(DaraModel):
    def __init__(
        self,
        any_like: str = None,
        desc: bool = None,
        name_like: str = None,
        order_by: str = None,
    ):
        # Fuzzy search for rule set ID, rule set name, rule ID, and rule name.
        self.any_like = any_like
        # Whether to sort in descending order.
        self.desc = desc
        # Fuzzy search for rule set name.
        self.name_like = name_like
        # Specify the column to sort by.
        self.order_by = order_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.any_like is not None:
            result['AnyLike'] = self.any_like

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.name_like is not None:
            result['NameLike'] = self.name_like

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnyLike') is not None:
            self.any_like = m.get('AnyLike')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('NameLike') is not None:
            self.name_like = m.get('NameLike')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        return self


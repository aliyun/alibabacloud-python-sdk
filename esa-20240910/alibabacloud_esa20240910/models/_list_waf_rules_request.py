# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListWafRulesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        phase: str = None,
        query_args: main_models.ListWafRulesRequestQueryArgs = None,
        ruleset_id: int = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # Query page number, used for pagination.
        self.page_number = page_number
        # Query page size, used for pagination.
        self.page_size = page_size
        # WAF rule type. Values:
        # 
        # - http_anti_scan: Scan protection
        # - http_bot: Bots
        # 
        # This parameter is required.
        self.phase = phase
        # Query filter conditions.
        self.query_args = query_args
        self.ruleset_id = ruleset_id
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) interface.
        # 
        # This parameter is required.
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

        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id

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
            temp_model = main_models.ListWafRulesRequestQueryArgs()
            self.query_args = temp_model.from_map(m.get('QueryArgs'))

        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

class ListWafRulesRequestQueryArgs(DaraModel):
    def __init__(
        self,
        config_value_like: str = None,
        desc: bool = None,
        id: int = None,
        id_name_like: str = None,
        name_like: str = None,
        order_by: str = None,
        status: str = None,
    ):
        # Fuzzy search for values in IP access control.
        self.config_value_like = config_value_like
        # Whether to reverse the sorting result.
        self.desc = desc
        # Exact query for WAF rule ID.
        self.id = id
        # Fuzzy query for WAF rule ID or name.
        self.id_name_like = id_name_like
        # Fuzzy query for WAF rule name.
        self.name_like = name_like
        # Sort the returned list by the specified column.
        self.order_by = order_by
        # Exact query for WAF rule status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_value_like is not None:
            result['ConfigValueLike'] = self.config_value_like

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.id is not None:
            result['Id'] = self.id

        if self.id_name_like is not None:
            result['IdNameLike'] = self.id_name_like

        if self.name_like is not None:
            result['NameLike'] = self.name_like

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigValueLike') is not None:
            self.config_value_like = m.get('ConfigValueLike')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdNameLike') is not None:
            self.id_name_like = m.get('IdNameLike')

        if m.get('NameLike') is not None:
            self.name_like = m.get('NameLike')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


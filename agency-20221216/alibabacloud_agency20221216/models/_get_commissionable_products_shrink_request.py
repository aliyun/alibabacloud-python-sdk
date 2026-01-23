# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCommissionableProductsShrinkRequest(DaraModel):
    def __init__(
        self,
        commodity_code_list: str = None,
        fiscal_year: str = None,
        list_show_status_list_shrink: str = None,
        page_no: int = None,
        page_size: int = None,
        pip_code_list: str = None,
        real_end_month: str = None,
        real_start_month: str = None,
    ):
        self.commodity_code_list = commodity_code_list
        self.fiscal_year = fiscal_year
        self.list_show_status_list_shrink = list_show_status_list_shrink
        self.page_no = page_no
        self.page_size = page_size
        self.pip_code_list = pip_code_list
        self.real_end_month = real_end_month
        self.real_start_month = real_start_month

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code_list is not None:
            result['CommodityCodeList'] = self.commodity_code_list

        if self.fiscal_year is not None:
            result['FiscalYear'] = self.fiscal_year

        if self.list_show_status_list_shrink is not None:
            result['ListShowStatusList'] = self.list_show_status_list_shrink

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pip_code_list is not None:
            result['PipCodeList'] = self.pip_code_list

        if self.real_end_month is not None:
            result['RealEndMonth'] = self.real_end_month

        if self.real_start_month is not None:
            result['RealStartMonth'] = self.real_start_month

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCodeList') is not None:
            self.commodity_code_list = m.get('CommodityCodeList')

        if m.get('FiscalYear') is not None:
            self.fiscal_year = m.get('FiscalYear')

        if m.get('ListShowStatusList') is not None:
            self.list_show_status_list_shrink = m.get('ListShowStatusList')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PipCodeList') is not None:
            self.pip_code_list = m.get('PipCodeList')

        if m.get('RealEndMonth') is not None:
            self.real_end_month = m.get('RealEndMonth')

        if m.get('RealStartMonth') is not None:
            self.real_start_month = m.get('RealStartMonth')

        return self


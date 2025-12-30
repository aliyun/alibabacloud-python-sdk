# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryBuyerDomainTradeRecordsRequest(DaraModel):
    def __init__(
        self,
        biz_id_list: List[str] = None,
        domain_name_list: List[str] = None,
        end_date: str = None,
        end_price: float = None,
        page_num: int = None,
        page_size: int = None,
        sorter: str = None,
        start_date: str = None,
        start_price: float = None,
        status_list: List[str] = None,
        suffix_list: List[str] = None,
        trade_type_list: List[str] = None,
    ):
        self.biz_id_list = biz_id_list
        self.domain_name_list = domain_name_list
        self.end_date = end_date
        self.end_price = end_price
        self.page_num = page_num
        self.page_size = page_size
        self.sorter = sorter
        self.start_date = start_date
        self.start_price = start_price
        self.status_list = status_list
        self.suffix_list = suffix_list
        self.trade_type_list = trade_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id_list is not None:
            result['BizIdList'] = self.biz_id_list

        if self.domain_name_list is not None:
            result['DomainNameList'] = self.domain_name_list

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.end_price is not None:
            result['EndPrice'] = self.end_price

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sorter is not None:
            result['Sorter'] = self.sorter

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.start_price is not None:
            result['StartPrice'] = self.start_price

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.suffix_list is not None:
            result['SuffixList'] = self.suffix_list

        if self.trade_type_list is not None:
            result['TradeTypeList'] = self.trade_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizIdList') is not None:
            self.biz_id_list = m.get('BizIdList')

        if m.get('DomainNameList') is not None:
            self.domain_name_list = m.get('DomainNameList')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('EndPrice') is not None:
            self.end_price = m.get('EndPrice')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Sorter') is not None:
            self.sorter = m.get('Sorter')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('StartPrice') is not None:
            self.start_price = m.get('StartPrice')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('SuffixList') is not None:
            self.suffix_list = m.get('SuffixList')

        if m.get('TradeTypeList') is not None:
            self.trade_type_list = m.get('TradeTypeList')

        return self


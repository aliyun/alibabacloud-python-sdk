# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20160511 import models as main_models
from darabonba.model import DaraModel

class QueryDomainListResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: main_models.QueryDomainListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        # The page number.
        self.current_page_num = current_page_num
        self.data = data
        # Indicates whether the current page is followed by a page.
        self.next_page = next_page
        # The number of entries per page.
        self.page_size = page_size
        # Indicates whether the current page follows another page.
        self.pre_page = pre_page
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_item_num = total_item_num
        # The total number of pages.
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        if m.get('Data') is not None:
            temp_model = main_models.QueryDomainListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryDomainListResponseBodyData(DaraModel):
    def __init__(
        self,
        domain: List[main_models.QueryDomainListResponseBodyDataDomain] = None,
    ):
        self.domain = domain

    def validate(self):
        if self.domain:
            for v1 in self.domain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domain'] = []
        if self.domain is not None:
            for k1 in self.domain:
                result['Domain'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain = []
        if m.get('Domain') is not None:
            for k1 in m.get('Domain'):
                temp_model = main_models.QueryDomainListResponseBodyDataDomain()
                self.domain.append(temp_model.from_map(k1))

        return self

class QueryDomainListResponseBodyDataDomain(DaraModel):
    def __init__(
        self,
        dead_date: str = None,
        dead_date_long: int = None,
        dead_date_status: str = None,
        domain_audit_status: str = None,
        domain_name: str = None,
        domain_reg_type: str = None,
        domain_status: str = None,
        domain_type: str = None,
        group_id: str = None,
        premium: bool = None,
        product_id: str = None,
        reg_date: str = None,
        reg_date_long: int = None,
        remark: str = None,
        sale_id: str = None,
    ):
        self.dead_date = dead_date
        self.dead_date_long = dead_date_long
        self.dead_date_status = dead_date_status
        self.domain_audit_status = domain_audit_status
        self.domain_name = domain_name
        self.domain_reg_type = domain_reg_type
        self.domain_status = domain_status
        self.domain_type = domain_type
        self.group_id = group_id
        self.premium = premium
        self.product_id = product_id
        self.reg_date = reg_date
        self.reg_date_long = reg_date_long
        self.remark = remark
        self.sale_id = sale_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dead_date is not None:
            result['DeadDate'] = self.dead_date

        if self.dead_date_long is not None:
            result['DeadDateLong'] = self.dead_date_long

        if self.dead_date_status is not None:
            result['DeadDateStatus'] = self.dead_date_status

        if self.domain_audit_status is not None:
            result['DomainAuditStatus'] = self.domain_audit_status

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_reg_type is not None:
            result['DomainRegType'] = self.domain_reg_type

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.premium is not None:
            result['Premium'] = self.premium

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.reg_date is not None:
            result['RegDate'] = self.reg_date

        if self.reg_date_long is not None:
            result['RegDateLong'] = self.reg_date_long

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.sale_id is not None:
            result['SaleId'] = self.sale_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadDate') is not None:
            self.dead_date = m.get('DeadDate')

        if m.get('DeadDateLong') is not None:
            self.dead_date_long = m.get('DeadDateLong')

        if m.get('DeadDateStatus') is not None:
            self.dead_date_status = m.get('DeadDateStatus')

        if m.get('DomainAuditStatus') is not None:
            self.domain_audit_status = m.get('DomainAuditStatus')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainRegType') is not None:
            self.domain_reg_type = m.get('DomainRegType')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Premium') is not None:
            self.premium = m.get('Premium')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')

        if m.get('RegDateLong') is not None:
            self.reg_date_long = m.get('RegDateLong')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')

        return self


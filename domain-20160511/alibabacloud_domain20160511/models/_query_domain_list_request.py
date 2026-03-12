# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDomainListRequest(DaraModel):
    def __init__(
        self,
        dead_end_date: int = None,
        dead_start_date: int = None,
        domain_name: str = None,
        domain_type: str = None,
        end_date: str = None,
        group_id: str = None,
        lang: str = None,
        order_by_type: str = None,
        order_key_type: str = None,
        page_num: int = None,
        page_size: int = None,
        product_domain_type: str = None,
        query_type: str = None,
        reg_end_date: int = None,
        reg_start_date: int = None,
        start_date: str = None,
        user_client_ip: str = None,
    ):
        # The end of the time range to query based on the time when domain names expire.
        self.dead_end_date = dead_end_date
        # The beginning of the time range to query based on the time when domain names expire.
        self.dead_start_date = dead_start_date
        # The domain name.
        self.domain_name = domain_name
        # The type of the domain name. Valid values:
        # 
        # GUOJI, TONGYONG, GUONEI, NAME, and WEIBO.
        self.domain_type = domain_type
        # The end of the time range to query based on the time when domain names expire.
        self.end_date = end_date
        # The group ID.
        self.group_id = group_id
        # The language of the error message to return if the request fails. Valid values:
        # 
        # zh: Chinese. en: English.
        self.lang = lang
        # The order in which you want to sort the queried domain names. Valid values:
        # 
        # ASC: ascending order. DESC: descending order.
        self.order_by_type = order_by_type
        # The field by which domain names to be queried are sorted. Valid values:
        # 
        # REGDATE: registration time. DEADDATE: expiration time. CREATEDATE: creation time.
        self.order_key_type = order_key_type
        # The page number.
        # 
        # This parameter is required.
        self.page_num = page_num
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type of the domain name. Valid values:
        # 
        # New gTLD, gTLD, ccTLD, and other.
        self.product_domain_type = product_domain_type
        # The type of the query. Valid values:
        # 
        # 1: renewal. 2: redemption. 4: transfer.
        self.query_type = query_type
        # The end of the time range to query based on the time when domain names were registered.
        self.reg_end_date = reg_end_date
        # The beginning of the time range to query based on the time when domain names were registered.
        self.reg_start_date = reg_start_date
        # The beginning of the time range to query based on the time when domain names expire.
        self.start_date = start_date
        # The IP address of the client. Set the value to 127.0.0.1.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dead_end_date is not None:
            result['DeadEndDate'] = self.dead_end_date

        if self.dead_start_date is not None:
            result['DeadStartDate'] = self.dead_start_date

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order_by_type is not None:
            result['OrderByType'] = self.order_by_type

        if self.order_key_type is not None:
            result['OrderKeyType'] = self.order_key_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_domain_type is not None:
            result['ProductDomainType'] = self.product_domain_type

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.reg_end_date is not None:
            result['RegEndDate'] = self.reg_end_date

        if self.reg_start_date is not None:
            result['RegStartDate'] = self.reg_start_date

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadEndDate') is not None:
            self.dead_end_date = m.get('DeadEndDate')

        if m.get('DeadStartDate') is not None:
            self.dead_start_date = m.get('DeadStartDate')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OrderByType') is not None:
            self.order_by_type = m.get('OrderByType')

        if m.get('OrderKeyType') is not None:
            self.order_key_type = m.get('OrderKeyType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductDomainType') is not None:
            self.product_domain_type = m.get('ProductDomainType')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('RegEndDate') is not None:
            self.reg_end_date = m.get('RegEndDate')

        if m.get('RegStartDate') is not None:
            self.reg_start_date = m.get('RegStartDate')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self


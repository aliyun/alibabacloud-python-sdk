# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDomainListRequest(DaraModel):
    def __init__(
        self,
        ccompany: str = None,
        domain_name: str = None,
        end_expiration_date: int = None,
        end_registration_date: int = None,
        lang: str = None,
        order_by_type: str = None,
        order_key_type: str = None,
        page_num: int = None,
        page_size: int = None,
        product_domain_type: str = None,
        query_type: str = None,
        start_expiration_date: int = None,
        start_registration_date: int = None,
        user_client_ip: str = None,
    ):
        self.ccompany = ccompany
        self.domain_name = domain_name
        self.end_expiration_date = end_expiration_date
        self.end_registration_date = end_registration_date
        self.lang = lang
        self.order_by_type = order_by_type
        self.order_key_type = order_key_type
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.product_domain_type = product_domain_type
        self.query_type = query_type
        self.start_expiration_date = start_expiration_date
        self.start_registration_date = start_registration_date
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ccompany is not None:
            result['Ccompany'] = self.ccompany

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_expiration_date is not None:
            result['EndExpirationDate'] = self.end_expiration_date

        if self.end_registration_date is not None:
            result['EndRegistrationDate'] = self.end_registration_date

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

        if self.start_expiration_date is not None:
            result['StartExpirationDate'] = self.start_expiration_date

        if self.start_registration_date is not None:
            result['StartRegistrationDate'] = self.start_registration_date

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ccompany') is not None:
            self.ccompany = m.get('Ccompany')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndExpirationDate') is not None:
            self.end_expiration_date = m.get('EndExpirationDate')

        if m.get('EndRegistrationDate') is not None:
            self.end_registration_date = m.get('EndRegistrationDate')

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

        if m.get('StartExpirationDate') is not None:
            self.start_expiration_date = m.get('StartExpirationDate')

        if m.get('StartRegistrationDate') is not None:
            self.start_registration_date = m.get('StartRegistrationDate')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self


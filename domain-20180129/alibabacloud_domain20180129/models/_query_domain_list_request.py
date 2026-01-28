# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDomainListRequest(DaraModel):
    def __init__(
        self,
        ccompany: str = None,
        dns: str = None,
        domain_group_id: str = None,
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
        registrar: str = None,
        resource_group_id: str = None,
        start_expiration_date: int = None,
        start_registration_date: int = None,
        tag: List[main_models.QueryDomainListRequestTag] = None,
        user_client_ip: str = None,
    ):
        # The name of the domain name registrant.
        self.ccompany = ccompany
        self.dns = dns
        # The ID of the domain name group.
        self.domain_group_id = domain_group_id
        # The domain name. You can search for the domain name in the domain name list.
        self.domain_name = domain_name
        # The end of the time range to query domain names based on expiration dates. Set the value to a UNIX timestamp representing the number of milliseconds that have elapsed from January 1, 1970, 00:00:00 UTC to the time you perform the query. Only queries by day are supported.
        self.end_expiration_date = end_expiration_date
        # The end of the time range to query domain names based on registration dates. Set the value to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Only queries by day are supported.
        self.end_registration_date = end_registration_date
        # The language of the error message to return if the request fails. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        # 
        # Default value: **en**.
        self.lang = lang
        # The order of the information based on which the domain names are sorted, such as the registration date and expiration date. Valid values:
        # 
        # *   **ASC**: ascending order
        # *   **DESC**: descending order
        # 
        # >  If this parameter is not specified, the default value **DESC** is used.
        self.order_by_type = order_by_type
        # The field that you use to sort the domain names. Valid values:
        # 
        # *   **RegistrationDate**: registration date
        # *   **ExpirationDate**: expiration date
        # 
        # >  If this parameter is not specified, the domain names are sorted by the time when they were added to the database.
        self.order_key_type = order_key_type
        # The page number.
        # 
        # This parameter is required.
        self.page_num = page_num
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The type of the domain name. Valid values:
        # 
        # *   **New gTLD**: new generic top-level domain names
        # *   **gTLD**: generic top-level domain names
        # *   **ccTLD**: country code top-level domain names
        self.product_domain_type = product_domain_type
        # The category of the domain names that you want to query. Valid values:
        # 
        # *   **1**: the domain names that need to be renewed
        # *   **2**: the domain names that need to be redeemed
        self.query_type = query_type
        self.registrar = registrar
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query domain names based on expiration dates. Set the value to a UNIX timestamp representing the number of milliseconds that have elapsed from January 1, 1970, 00:00:00 UTC to the time you perform the query. Only queries by day are supported.
        self.start_expiration_date = start_expiration_date
        # The beginning of the time range to query domain names based on registration dates. Set the value to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Only queries by day are supported.
        self.start_registration_date = start_registration_date
        # The tags to add to the resource.
        self.tag = tag
        # The IP address of the client. Set the value to **127.0.0.1**.
        self.user_client_ip = user_client_ip

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ccompany is not None:
            result['Ccompany'] = self.ccompany

        if self.dns is not None:
            result['Dns'] = self.dns

        if self.domain_group_id is not None:
            result['DomainGroupId'] = self.domain_group_id

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

        if self.registrar is not None:
            result['Registrar'] = self.registrar

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_expiration_date is not None:
            result['StartExpirationDate'] = self.start_expiration_date

        if self.start_registration_date is not None:
            result['StartRegistrationDate'] = self.start_registration_date

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ccompany') is not None:
            self.ccompany = m.get('Ccompany')

        if m.get('Dns') is not None:
            self.dns = m.get('Dns')

        if m.get('DomainGroupId') is not None:
            self.domain_group_id = m.get('DomainGroupId')

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

        if m.get('Registrar') is not None:
            self.registrar = m.get('Registrar')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartExpirationDate') is not None:
            self.start_expiration_date = m.get('StartExpirationDate')

        if m.get('StartRegistrationDate') is not None:
            self.start_registration_date = m.get('StartRegistrationDate')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.QueryDomainListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

class QueryDomainListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag to add to the resource.
        self.key = key
        # The value of the tag to add to the resource.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


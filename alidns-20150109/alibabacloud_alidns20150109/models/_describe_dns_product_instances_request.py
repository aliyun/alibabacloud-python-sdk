# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsProductInstancesRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        domain_type: str = None,
        lang: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        user_client_ip: str = None,
        version_code: str = None,
    ):
        # The sorting order. Valid values:
        # 
        # - DESC: Descending order. This is the default value.
        # 
        # - ASC: Ascending order.
        self.direction = direction
        # The type of the domain name. This parameter is not case-sensitive. Valid values:
        # 
        # - PUBLIC: authoritative domain name (default)
        # 
        # - CACHE: authoritative proxy domain name
        self.domain_type = domain_type
        # The language of the response. Valid values:
        # 
        # - zh: Chinese
        # 
        # - en: English
        # 
        # Default value: en
        self.lang = lang
        # The field to sort the results by. Valid values:
        # 
        # - createDate: Sorts the results by creation time. This is the default value.
        # 
        # - expireDate: Sorts the results by expiration time.
        self.order_by = order_by
        # The page number. Pages start from **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **100**. Default value: **20**.
        self.page_size = page_size
        # The client\\"s IP address.
        self.user_client_ip = user_client_ip
        # The edition code of the Alibaba Cloud DNS instance.
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self


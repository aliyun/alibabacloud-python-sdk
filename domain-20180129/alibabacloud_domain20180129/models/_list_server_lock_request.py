# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServerLockRequest(DaraModel):
    def __init__(
        self,
        begin_start_date: int = None,
        domain_name: str = None,
        end_expire_date: int = None,
        end_start_date: int = None,
        lang: str = None,
        lock_product_id: str = None,
        order_by: str = None,
        order_by_type: str = None,
        page_num: int = None,
        page_size: int = None,
        server_lock_status: int = None,
        start_expire_date: int = None,
        user_client_ip: str = None,
    ):
        # The start of the time range to query.
        self.begin_start_date = begin_start_date
        # The domain name for which you want to query the enabled registry lock.
        self.domain_name = domain_name
        # The end of the expiration time.
        self.end_expire_date = end_expire_date
        # The end of the time range to query.
        self.end_start_date = end_start_date
        # The language of the error message to return if the request fails. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The ID of the product to which the domain name with the registry lock enabled belongs.
        self.lock_product_id = lock_product_id
        # The field that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   EXPIRE_DATE
        self.order_by = order_by
        # The order of the information based on which you want to sort the domain names, such as the registration date and expiration date. Valid values: ASC and DESC. The value ASC specifies the ascending order. The value DESC specifies the descending order. If this parameter is not configured, the default value DESC is used.
        self.order_by_type = order_by_type
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The status of the registry lock. Valid values:
        # 
        # *   1: The registry lock is not enabled.
        # *   2: The registry lock is enabled.
        # *   3: The registry lock is disabled.
        self.server_lock_status = server_lock_status
        # The start of the expiration time.
        self.start_expire_date = start_expire_date
        # The IP address of the client. For example, you can set the value to **127.0.0.1**.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_start_date is not None:
            result['BeginStartDate'] = self.begin_start_date

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_expire_date is not None:
            result['EndExpireDate'] = self.end_expire_date

        if self.end_start_date is not None:
            result['EndStartDate'] = self.end_start_date

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.lock_product_id is not None:
            result['LockProductId'] = self.lock_product_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_by_type is not None:
            result['OrderByType'] = self.order_by_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.server_lock_status is not None:
            result['ServerLockStatus'] = self.server_lock_status

        if self.start_expire_date is not None:
            result['StartExpireDate'] = self.start_expire_date

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginStartDate') is not None:
            self.begin_start_date = m.get('BeginStartDate')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndExpireDate') is not None:
            self.end_expire_date = m.get('EndExpireDate')

        if m.get('EndStartDate') is not None:
            self.end_start_date = m.get('EndStartDate')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LockProductId') is not None:
            self.lock_product_id = m.get('LockProductId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderByType') is not None:
            self.order_by_type = m.get('OrderByType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ServerLockStatus') is not None:
            self.server_lock_status = m.get('ServerLockStatus')

        if m.get('StartExpireDate') is not None:
            self.start_expire_date = m.get('StartExpireDate')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self


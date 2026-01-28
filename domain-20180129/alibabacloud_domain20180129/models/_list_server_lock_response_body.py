# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class ListServerLockResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.ListServerLockResponseBodyData] = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        # The page number.
        self.current_page_num = current_page_num
        # The response parameters.
        self.data = data
        # Indicates whether the current page is followed by a page.
        self.next_page = next_page
        # The number of entries per page.
        self.page_size = page_size
        # Indicates whether the current page is preceded by a page.
        self.pre_page = pre_page
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_item_num = total_item_num
        # The total number of pages returned.
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListServerLockResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class ListServerLockResponseBodyData(DaraModel):
    def __init__(
        self,
        domain_instance_id: str = None,
        domain_name: str = None,
        expire_date: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        lock_instance_id: str = None,
        lock_product_id: str = None,
        server_lock_status: str = None,
        start_date: str = None,
        user_id: str = None,
    ):
        # The instance ID of the domain name.
        self.domain_instance_id = domain_instance_id
        # The domain name that has valid registry lock information.
        self.domain_name = domain_name
        # The expiration time.
        self.expire_date = expire_date
        # The creation time.
        self.gmt_create = gmt_create
        # The time when the domain name was last modified.
        self.gmt_modified = gmt_modified
        # The instance ID of the domain name for which the registry lock is enabled.
        self.lock_instance_id = lock_instance_id
        # The ID of the product to which the domain name with the registry lock enabled belongs.
        self.lock_product_id = lock_product_id
        # The status of the registry lock.
        self.server_lock_status = server_lock_status
        # The start time.
        self.start_date = start_date
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_instance_id is not None:
            result['DomainInstanceId'] = self.domain_instance_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.lock_instance_id is not None:
            result['LockInstanceId'] = self.lock_instance_id

        if self.lock_product_id is not None:
            result['LockProductId'] = self.lock_product_id

        if self.server_lock_status is not None:
            result['ServerLockStatus'] = self.server_lock_status

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainInstanceId') is not None:
            self.domain_instance_id = m.get('DomainInstanceId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LockInstanceId') is not None:
            self.lock_instance_id = m.get('LockInstanceId')

        if m.get('LockProductId') is not None:
            self.lock_product_id = m.get('LockProductId')

        if m.get('ServerLockStatus') is not None:
            self.server_lock_status = m.get('ServerLockStatus')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self


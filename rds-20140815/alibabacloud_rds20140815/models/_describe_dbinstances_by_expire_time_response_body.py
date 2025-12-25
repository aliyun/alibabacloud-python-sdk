# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesByExpireTimeResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstancesByExpireTimeResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The details of the instances.
        self.items = items
        # The page number of the returned page. Valid values: any **non-zero** positive integer.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of instances returned on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBInstancesByExpireTimeResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDBInstancesByExpireTimeResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance_expire_time: List[main_models.DescribeDBInstancesByExpireTimeResponseBodyItemsDBInstanceExpireTime] = None,
    ):
        self.dbinstance_expire_time = dbinstance_expire_time

    def validate(self):
        if self.dbinstance_expire_time:
            for v1 in self.dbinstance_expire_time:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceExpireTime'] = []
        if self.dbinstance_expire_time is not None:
            for k1 in self.dbinstance_expire_time:
                result['DBInstanceExpireTime'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_expire_time = []
        if m.get('DBInstanceExpireTime') is not None:
            for k1 in m.get('DBInstanceExpireTime'):
                temp_model = main_models.DescribeDBInstancesByExpireTimeResponseBodyItemsDBInstanceExpireTime()
                self.dbinstance_expire_time.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesByExpireTimeResponseBodyItemsDBInstanceExpireTime(DaraModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_status: str = None,
        expire_time: str = None,
        lock_mode: str = None,
        pay_type: str = None,
    ):
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The status of the instance. For more information, see [Instance state table](https://help.aliyun.com/document_detail/26315.html).
        self.dbinstance_status = dbinstance_status
        # The expiration time of the instance. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > : Pay-as-you-go instances never expire.
        self.expire_time = expire_time
        # The lock mode of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked after it expires.
        # *   **LockByRestoration**: The instance is automatically locked before it is rolled back.
        # *   **LockByDiskQuota**: The instance is automatically locked after its storage capacity is exhausted.
        # *   **LockReadInstanceByDiskQuota**: The instance is a read-only instance and is automatically locked after its storage capacity is exhausted.
        self.lock_mode = lock_mode
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceSwitchLogResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        log_items: List[main_models.DescribeDBInstanceSwitchLogResponseBodyLogItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The primary/secondary switchover logs.
        self.log_items = log_items
        # The page number returned.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of primary/secondary switching entries.
        self.total_count = total_count

    def validate(self):
        if self.log_items:
            for v1 in self.log_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        result['LogItems'] = []
        if self.log_items is not None:
            for k1 in self.log_items:
                result['LogItems'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.log_items = []
        if m.get('LogItems') is not None:
            for k1 in m.get('LogItems'):
                temp_model = main_models.DescribeDBInstanceSwitchLogResponseBodyLogItems()
                self.log_items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDBInstanceSwitchLogResponseBodyLogItems(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        switch_code: str = None,
        switch_status: str = None,
        switch_time: str = None,
    ):
        # The ID of the replica set instance or the ID of the node on which a primary/secondary switchover is performed.
        self.node_id = node_id
        # The code that indicates the reason of a primary/secondary switchover. Valid values:
        # 
        # *   USER_CONSOLE_OPERATION: The switchover is manually performed.
        # *   OPERATION_AND_MAINTENANCE: Potential risks exist.
        # *   MACHINE_DOWNTIME: The host is offline.
        # *   PRIMARY_UNHEALTHY: An exception occurs on the primary node of the instance.
        # *   SECONDARY_UNHEALTHY: An exception occurs on the secondary node of the instance.
        # *   MULTIPLE_NODE_FAILURES: An exception occurs on multiple nodes of the instance.
        self.switch_code = switch_code
        # The switchover status. Valid values: **1** and **0**. The value 1 indicates a successful primary/secondary switchover and the value 0 indicates a failed primary/secondary switchover.
        self.switch_status = switch_status
        # The point in time when a primary/secondary switchover was performed. The time follows the ISO 8601 standard in the *yyyy-mm-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.switch_time = switch_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.switch_code is not None:
            result['SwitchCode'] = self.switch_code

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('SwitchCode') is not None:
            self.switch_code = m.get('SwitchCode')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        return self


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
        # The list of primary/secondary switchover logs.
        self.log_items = log_items
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of primary/secondary switchover records returned in the query.
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
        # Instance ID of the instance if the instance is a replica set instance, or instance ID of the switched node if the instance is a sharded cluster instance.
        self.node_id = node_id
        # The cause code of the switchover. Valid values:
        # - USER_CONSOLE_OPERATION: manual operation
        # - OPERATION_AND_MAINTENANCE: potential risk
        # - MACHINE_DOWNTIME: host offline
        # - PRIMARY_UNHEALTHY: instance failures
        # - SECONDARY_UNHEALTHY: instance failures
        # - MULTIPLE_NODE_FAILURES: instance failures
        self.switch_code = switch_code
        # The switchover status. Valid values:
        # - **1**: The switchover is successful.
        # - **0**: The switchover failed.
        self.switch_status = switch_status
        # The switchover time. The time is in the <i>yyyy-mm-dd</i>T<i>hh:mm:ss</i>Z format (UTC).
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


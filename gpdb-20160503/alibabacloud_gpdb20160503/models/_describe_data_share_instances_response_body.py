# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDataShareInstancesResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDataShareInstancesResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The state of data sharing. Valid values:
        # 
        # *   **opening**
        # *   **opened**
        # *   **closing**
        # *   **closed**
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
            temp_model = main_models.DescribeDataShareInstancesResponseBodyItems()
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

class DescribeDataShareInstancesResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance: List[main_models.DescribeDataShareInstancesResponseBodyItemsDBInstance] = None,
    ):
        self.dbinstance = dbinstance

    def validate(self):
        if self.dbinstance:
            for v1 in self.dbinstance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k1 in self.dbinstance:
                result['DBInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance = []
        if m.get('DBInstance') is not None:
            for k1 in m.get('DBInstance'):
                temp_model = main_models.DescribeDataShareInstancesResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k1))

        return self

class DescribeDataShareInstancesResponseBodyItemsDBInstance(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbinstance_mode: str = None,
        data_share_status: str = None,
        description: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The resource type of the instance. Valid values:
        # 
        # *   **Serverless**: Serverless mode
        # *   **StorageElasic**: elastic storage mode
        # *   **Classic**: reserved storage mode
        self.dbinstance_mode = dbinstance_mode
        # The state of data sharing. Valid values:
        # 
        # *   **opening**: Data sharing is being enabled.
        # *   **opened**: Data sharing is enabled.
        # *   **closing**: Data sharing is being disabled.
        # *   **closed**: Data sharing is disabled.
        self.data_share_status = data_share_status
        # The description of the instance.
        self.description = description
        # The region ID of the instance.
        self.region_id = region_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode

        if self.data_share_status is not None:
            result['DataShareStatus'] = self.data_share_status

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')

        if m.get('DataShareStatus') is not None:
            self.data_share_status = m.get('DataShareStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self


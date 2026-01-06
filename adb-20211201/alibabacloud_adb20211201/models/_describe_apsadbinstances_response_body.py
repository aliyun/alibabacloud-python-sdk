# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAPSADBInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.DescribeAPSADBInstancesResponseBodyItems] = None,
        message: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: str = None,
    ):
        # The HTTP status code or the error code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The queried clusters.
        self.items = items
        # The returned message. Valid values:
        # 
        # *   If the request was successful, a success message is returned.****
        # *   If the request failed, an error message is returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAPSADBInstancesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAPSADBInstancesResponseBodyItems(DaraModel):
    def __init__(
        self,
        compute_resource: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_status: str = None,
        reserved_acu: str = None,
        storage_resource: int = None,
        zone_id: str = None,
    ):
        # The specifications of the reserved computing resources.
        self.compute_resource = compute_resource
        # The description of the cluster.
        self.dbcluster_description = dbcluster_description
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        self.dbcluster_id = dbcluster_id
        # The status of the cluster.
        self.dbcluster_status = dbcluster_status
        # The amount of remaining reserved computing resources that are available in the cluster.
        self.reserved_acu = reserved_acu
        # The specifications of the reserved storage resources.
        self.storage_resource = storage_resource
        # The zone ID of the cluster.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.reserved_acu is not None:
            result['ReservedACU'] = self.reserved_acu

        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('ReservedACU') is not None:
            self.reserved_acu = m.get('ReservedACU')

        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOrdersRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order_status: str = None,
        page_number: int = None,
        page_size: int = None,
        product_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The [edition](https://help.aliyun.com/document_detail/183258.html) of the cluster. Valid values:
        # 
        # - **Normal**: Cluster Edition
        # 
        # - **Basic**: single node
        # 
        # - **Archive**: X-Engine
        # 
        # - **NormalMultimaster**: Multi-master Cluster Edition
        # 
        # - **SENormal**: Standard Edition
        # 
        # > * The single node edition is not supported on PolarDB for PostgreSQL clusters that run PostgreSQL 11.
        # >
        # > * The Standard Edition is supported on PolarDB for MySQL clusters that run MySQL 8.0 or 5.7, and on PolarDB for PostgreSQL clusters that run PostgreSQL 14.
        # >
        # > * PolarDB for MySQL clusters that run MySQL 8.0 support X-Engine and the Multi-master Cluster Edition.
        self.category = category
        # The ID of the current instance.
        self.instance_id = instance_id
        # The maximum number of entries to return for the current request. Default value: 10.
        self.max_results = max_results
        # A pagination token. If the query results are not returned in a single call, this token is returned. Use this token in a subsequent call to retrieve the remaining results.
        self.next_token = next_token
        # The status of the order.
        # 
        # - **pending**: The task is waiting to start.
        # 
        # - **create**: The order is placed and is being processed.
        # 
        # - **fail**: The instance failed to be created.
        # 
        # - **cancel**: The order is canceled.
        # 
        # - **success**: The instance is created.
        self.order_status = order_status
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        # 
        # Default value: 30.
        self.page_size = page_size
        # The product code.
        self.product_code = product_code
        # The region ID.
        # 
        # > Call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to view the details of regions.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self


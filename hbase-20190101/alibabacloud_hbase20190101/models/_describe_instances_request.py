# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        db_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.DescribeInstancesRequestTag] = None,
    ):
        # The ID of target instance. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) operation to query target instance ID.
        self.cluster_id = cluster_id
        # The name of the ApsaraDB for HBase instance.
        self.cluster_name = cluster_name
        # The service type. Valid values:
        # - **hbase**: ApsaraDB for HBase Standard Edition or ApsaraDB for HBase single-node.
        # - **hbaseue**: ApsaraDB for HBase Performance-enhanced Edition.
        # - **bds**: BDS data synchronization service.
        self.db_type = db_type
        # The page number of the instance list. Minimum value: **1**. Default value: **1**.
        self.page_number = page_number
        # The maximum number of rows to display per page. Maximum value: **100**. Default value: **10**.
        self.page_size = page_size
        # The ID of the region to which the instance belongs. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/144489.html) operation to query the region ID.
        # 
        # > If you specify the **Tag.N.Key** and **Tag.N.Value** parameters, this parameter is required.
        self.region_id = region_id
        # The ID of the resource group. You can query the resource group ID in the Resource Group console.
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tag = tag

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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The tag key and tag value form a key-value pair in the format of {"key1":"value1","key2":"value2"}.
        self.key = key
        # The value of the tag key. The tag value and tag key form a key-value pair.
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


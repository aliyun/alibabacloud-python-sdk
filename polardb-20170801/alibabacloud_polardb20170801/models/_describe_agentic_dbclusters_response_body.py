# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAgenticDBClustersResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeAgenticDBClustersResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The cluster list.
        self.items = items
        # The maximum number of entries to return. Default value: 10.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous API call. If there is no next query, do not pass this parameter.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of clusters on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

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
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAgenticDBClustersResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeAgenticDBClustersResponseBodyItems(DaraModel):
    def __init__(
        self,
        agentic_db_cluster_description: str = None,
        agentic_db_cluster_id: str = None,
        category: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_status: str = None,
        dbtype: str = None,
        dbversion: str = None,
        expire_time: str = None,
        expired: str = None,
        lock_mode: str = None,
        pay_type: str = None,
        region_id: str = None,
        scale_max: str = None,
        scale_min: str = None,
        serverless_type: str = None,
        storage_type: str = None,
        storage_used: int = None,
        tags: List[main_models.DescribeAgenticDBClustersResponseBodyItemsTags] = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # The Agentic cluster description.
        self.agentic_db_cluster_description = agentic_db_cluster_description
        # The Agentic cluster ID.
        self.agentic_db_cluster_id = agentic_db_cluster_id
        # The cluster edition. Valid values:
        # 
        # - **Normal**: Cluster Edition
        # 
        # - **Basic**: Single Node Edition
        # 
        # - **Archive**: X-Engine Edition
        # 
        # - **NormalMultimaster**: Multi-master Cluster (Database/Table)
        self.category = category
        # The time when the cluster was created.
        self.create_time = create_time
        # The cluster description.
        self.dbcluster_description = dbcluster_description
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The cluster status.
        self.dbcluster_status = dbcluster_status
        # The database engine type.
        self.dbtype = dbtype
        # The database engine version.
        self.dbversion = dbversion
        # The expiration time of the cluster.
        # > A specific value is returned only for clusters whose billing method is **Prepaid** (subscription). An empty value is returned for **Postpaid** (pay-as-you-go) clusters.
        self.expire_time = expire_time
        # Indicates whether the cluster has expired. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        # 
        # > This parameter is returned only for clusters whose billing method is **Prepaid** (subscription).
        self.expired = expired
        # The lock status of the cluster. Valid values: 
        # 
        # - **Unlock**: Normal. 
        # - **ManualLock**: Manually locked. 
        # - **LockByExpiration**: Automatically locked due to cluster expiration.
        self.lock_mode = lock_mode
        # The billing method. Valid values: 
        # 
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        self.pay_type = pay_type
        # The region ID.
        self.region_id = region_id
        # The maximum value: 1 to 32 PCUs. Unit: PCU.
        self.scale_max = scale_max
        # The minimum value: 0 to 32 PCUs. The minimum value must be less than or equal to the maximum value. Unit: PCU.
        self.scale_min = scale_min
        # The serverless type. A value of **AgileServerless** indicates that the cluster is a serverless cluster.
        self.serverless_type = serverless_type
        # The storage type. Valid values:
        # * **essdpl0**
        # * **essdpl1**
        # * **essdpl2**
        # * **essdpl3**
        self.storage_type = storage_type
        # The storage usage of the cluster. Unit: bytes.
        self.storage_used = storage_used
        # The tag key. You can filter the cluster list by tag. You can specify up to 20 tag pairs. The number n for each tag pair must be unique and must be a consecutive integer starting from 1. The value of Tag.n.Key corresponds to Tag.n.Value.
        self.tags = tags
        # The ID of the virtual private cloud (VPC) in which the endpoint resides.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentic_db_cluster_description is not None:
            result['AgenticDbClusterDescription'] = self.agentic_db_cluster_description

        if self.agentic_db_cluster_id is not None:
            result['AgenticDbClusterId'] = self.agentic_db_cluster_id

        if self.category is not None:
            result['Category'] = self.category

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgenticDbClusterDescription') is not None:
            self.agentic_db_cluster_description = m.get('AgenticDbClusterDescription')

        if m.get('AgenticDbClusterId') is not None:
            self.agentic_db_cluster_id = m.get('AgenticDbClusterId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeAgenticDBClustersResponseBodyItemsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAgenticDBClustersResponseBodyItemsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


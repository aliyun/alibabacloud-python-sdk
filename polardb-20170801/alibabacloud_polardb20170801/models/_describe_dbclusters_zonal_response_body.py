# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClustersZonalResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDBClustersZonalResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
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
                temp_model = main_models.DescribeDBClustersZonalResponseBodyItems()
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

class DescribeDBClustersZonalResponseBodyItems(DaraModel):
    def __init__(
        self,
        ai_type: str = None,
        category: str = None,
        central_control_region_id: str = None,
        cloud_provider: str = None,
        cpu_cores: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_status: str = None,
        dbnode_class: str = None,
        dbnode_number: int = None,
        dbtype: str = None,
        dbversion: str = None,
        ensregion_id: str = None,
        expire_time: str = None,
        expired: str = None,
        lock_mode: str = None,
        pay_type: str = None,
        serverless_type: str = None,
        storage_space: int = None,
        storage_type: str = None,
        storage_used: int = None,
        strict_consistency: str = None,
        sub_category: str = None,
        tags: List[main_models.DescribeDBClustersZonalResponseBodyItemsTags] = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.ai_type = ai_type
        self.category = category
        self.central_control_region_id = central_control_region_id
        self.cloud_provider = cloud_provider
        self.cpu_cores = cpu_cores
        self.create_time = create_time
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id
        self.dbcluster_status = dbcluster_status
        self.dbnode_class = dbnode_class
        self.dbnode_number = dbnode_number
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.ensregion_id = ensregion_id
        self.expire_time = expire_time
        self.expired = expired
        self.lock_mode = lock_mode
        self.pay_type = pay_type
        self.serverless_type = serverless_type
        self.storage_space = storage_space
        self.storage_type = storage_type
        self.storage_used = storage_used
        self.strict_consistency = strict_consistency
        self.sub_category = sub_category
        self.tags = tags
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
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
        if self.ai_type is not None:
            result['AiType'] = self.ai_type

        if self.category is not None:
            result['Category'] = self.category

        if self.central_control_region_id is not None:
            result['CentralControlRegionId'] = self.central_control_region_id

        if self.cloud_provider is not None:
            result['CloudProvider'] = self.cloud_provider

        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_number is not None:
            result['DBNodeNumber'] = self.dbnode_number

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.ensregion_id is not None:
            result['ENSRegionId'] = self.ensregion_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used

        if self.strict_consistency is not None:
            result['StrictConsistency'] = self.strict_consistency

        if self.sub_category is not None:
            result['SubCategory'] = self.sub_category

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
        if m.get('AiType') is not None:
            self.ai_type = m.get('AiType')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CentralControlRegionId') is not None:
            self.central_control_region_id = m.get('CentralControlRegionId')

        if m.get('CloudProvider') is not None:
            self.cloud_provider = m.get('CloudProvider')

        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeNumber') is not None:
            self.dbnode_number = m.get('DBNodeNumber')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('ENSRegionId') is not None:
            self.ensregion_id = m.get('ENSRegionId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')

        if m.get('StrictConsistency') is not None:
            self.strict_consistency = m.get('StrictConsistency')

        if m.get('SubCategory') is not None:
            self.sub_category = m.get('SubCategory')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDBClustersZonalResponseBodyItemsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBClustersZonalResponseBodyItemsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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


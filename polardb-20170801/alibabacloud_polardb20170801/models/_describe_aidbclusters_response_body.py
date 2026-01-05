# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClustersResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeAIDBClustersResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        # Id of the request
        self.request_id = request_id
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
            temp_model = main_models.DescribeAIDBClustersResponseBodyItems()
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

class DescribeAIDBClustersResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbcluster: List[main_models.DescribeAIDBClustersResponseBodyItemsDBCluster] = None,
    ):
        self.dbcluster = dbcluster

    def validate(self):
        if self.dbcluster:
            for v1 in self.dbcluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k1 in self.dbcluster:
                result['DBCluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k1 in m.get('DBCluster'):
                temp_model = main_models.DescribeAIDBClustersResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k1))

        return self

class DescribeAIDBClustersResponseBodyItemsDBCluster(DaraModel):
    def __init__(
        self,
        ai_node_type: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_status: str = None,
        dbnode_class: str = None,
        dbtype: str = None,
        expire_time: str = None,
        expired: bool = None,
        kube_cluster_id: str = None,
        lock_mode: str = None,
        model_type: str = None,
        pay_type: str = None,
        region_id: str = None,
        relative_dbcluster_id: str = None,
        run_type: str = None,
        storage_space: int = None,
        storage_type: str = None,
        tags: main_models.DescribeAIDBClustersResponseBodyItemsDBClusterTags = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.ai_node_type = ai_node_type
        self.create_time = create_time
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id
        self.dbcluster_status = dbcluster_status
        self.dbnode_class = dbnode_class
        self.dbtype = dbtype
        self.expire_time = expire_time
        self.expired = expired
        self.kube_cluster_id = kube_cluster_id
        self.lock_mode = lock_mode
        self.model_type = model_type
        self.pay_type = pay_type
        self.region_id = region_id
        self.relative_dbcluster_id = relative_dbcluster_id
        self.run_type = run_type
        self.storage_space = storage_space
        self.storage_type = storage_type
        self.tags = tags
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_node_type is not None:
            result['AiNodeType'] = self.ai_node_type

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

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.kube_cluster_id is not None:
            result['KubeClusterId'] = self.kube_cluster_id

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.relative_dbcluster_id is not None:
            result['RelativeDBClusterId'] = self.relative_dbcluster_id

        if self.run_type is not None:
            result['RunType'] = self.run_type

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiNodeType') is not None:
            self.ai_node_type = m.get('AiNodeType')

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

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('KubeClusterId') is not None:
            self.kube_cluster_id = m.get('KubeClusterId')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelativeDBClusterId') is not None:
            self.relative_dbcluster_id = m.get('RelativeDBClusterId')

        if m.get('RunType') is not None:
            self.run_type = m.get('RunType')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeAIDBClustersResponseBodyItemsDBClusterTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAIDBClustersResponseBodyItemsDBClusterTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeAIDBClustersResponseBodyItemsDBClusterTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeAIDBClustersResponseBodyItemsDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAIDBClustersResponseBodyItemsDBClusterTagsTag(DaraModel):
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


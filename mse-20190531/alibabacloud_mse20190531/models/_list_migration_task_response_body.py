# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListMigrationTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListMigrationTaskResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The array structure.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

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
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListMigrationTaskResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

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

class ListMigrationTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        origin_instance_address: str = None,
        origin_instance_name: str = None,
        origin_instance_namespace: str = None,
        project_desc: str = None,
        sync_type: str = None,
        target_cluster_name: str = None,
        target_cluster_url: str = None,
        target_instance_id: str = None,
        user_id: str = None,
    ):
        # The type of the instance.
        # 
        # *   Nacos-Ans
        # *   ZooKeeper
        # *   Eureka
        self.cluster_type = cluster_type
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The ID of the job.
        self.id = id
        # The address of the source instance node.
        self.origin_instance_address = origin_instance_address
        # The name of the source instance.
        self.origin_instance_name = origin_instance_name
        # The list of namespaces. This parameter is optional if applications are migrated from a Nacos instance.
        self.origin_instance_namespace = origin_instance_namespace
        # The description.
        self.project_desc = project_desc
        self.sync_type = sync_type
        # The name of the destination instance.
        self.target_cluster_name = target_cluster_name
        # The URL of the destination instance.
        self.target_cluster_url = target_cluster_url
        # The ID of the destination instance.
        self.target_instance_id = target_instance_id
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.origin_instance_address is not None:
            result['OriginInstanceAddress'] = self.origin_instance_address

        if self.origin_instance_name is not None:
            result['OriginInstanceName'] = self.origin_instance_name

        if self.origin_instance_namespace is not None:
            result['OriginInstanceNamespace'] = self.origin_instance_namespace

        if self.project_desc is not None:
            result['ProjectDesc'] = self.project_desc

        if self.sync_type is not None:
            result['SyncType'] = self.sync_type

        if self.target_cluster_name is not None:
            result['TargetClusterName'] = self.target_cluster_name

        if self.target_cluster_url is not None:
            result['TargetClusterUrl'] = self.target_cluster_url

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OriginInstanceAddress') is not None:
            self.origin_instance_address = m.get('OriginInstanceAddress')

        if m.get('OriginInstanceName') is not None:
            self.origin_instance_name = m.get('OriginInstanceName')

        if m.get('OriginInstanceNamespace') is not None:
            self.origin_instance_namespace = m.get('OriginInstanceNamespace')

        if m.get('ProjectDesc') is not None:
            self.project_desc = m.get('ProjectDesc')

        if m.get('SyncType') is not None:
            self.sync_type = m.get('SyncType')

        if m.get('TargetClusterName') is not None:
            self.target_cluster_name = m.get('TargetClusterName')

        if m.get('TargetClusterUrl') is not None:
            self.target_cluster_url = m.get('TargetClusterUrl')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self


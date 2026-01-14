# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class AddMigrationTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.AddMigrationTaskResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Data structure.
        self.data = data
        # Error code.
        self.error_code = error_code
        # Message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # 请求结果，取值如下：
        # - `true`：请求成功。
        # - `false`：请求失败。
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.AddMigrationTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AddMigrationTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        id: str = None,
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
        # Cluster type.
        # 
        # - Nacos-Ans
        # - ZooKeeper
        # - Eureka
        self.cluster_type = cluster_type
        # Task ID.
        self.id = id
        # Source instance node address.
        self.origin_instance_address = origin_instance_address
        # Source instance name.
        self.origin_instance_name = origin_instance_name
        # Namespace list, required when the source cluster is Nacos.
        self.origin_instance_namespace = origin_instance_namespace
        # Description.
        self.project_desc = project_desc
        # SyncType
        self.sync_type = sync_type
        # Target instance name.
        self.target_cluster_name = target_cluster_name
        # Target instance URL.
        self.target_cluster_url = target_cluster_url
        # Target instance ID.
        self.target_instance_id = target_instance_id
        # User ID.
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


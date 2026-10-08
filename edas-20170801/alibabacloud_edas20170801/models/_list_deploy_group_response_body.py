# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListDeployGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        deploy_group_list: main_models.ListDeployGroupResponseBodyDeployGroupList = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code of the request or a POP error code.
        self.code = code
        self.deploy_group_list = deploy_group_list
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.deploy_group_list:
            self.deploy_group_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.deploy_group_list is not None:
            result['DeployGroupList'] = self.deploy_group_list.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DeployGroupList') is not None:
            temp_model = main_models.ListDeployGroupResponseBodyDeployGroupList()
            self.deploy_group_list = temp_model.from_map(m.get('DeployGroupList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDeployGroupResponseBodyDeployGroupList(DaraModel):
    def __init__(
        self,
        deploy_group: List[main_models.ListDeployGroupResponseBodyDeployGroupListDeployGroup] = None,
    ):
        self.deploy_group = deploy_group

    def validate(self):
        if self.deploy_group:
            for v1 in self.deploy_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeployGroup'] = []
        if self.deploy_group is not None:
            for k1 in self.deploy_group:
                result['DeployGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deploy_group = []
        if m.get('DeployGroup') is not None:
            for k1 in m.get('DeployGroup'):
                temp_model = main_models.ListDeployGroupResponseBodyDeployGroupListDeployGroup()
                self.deploy_group.append(temp_model.from_map(k1))

        return self

class ListDeployGroupResponseBodyDeployGroupListDeployGroup(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
        base_component_meta_name: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cpu_limit: str = None,
        cpu_request: str = None,
        create_time: int = None,
        cs_cluster_id: str = None,
        deployment_name: str = None,
        env: str = None,
        ephemeral_storage_limit: str = None,
        ephemeral_storage_request: str = None,
        group_id: str = None,
        group_name: str = None,
        group_type: int = None,
        labels: str = None,
        last_update_time: int = None,
        memory_limit: str = None,
        memory_request: str = None,
        name_space: str = None,
        package_public_url: str = None,
        package_url: str = None,
        package_version: str = None,
        package_version_id: str = None,
        post_start: str = None,
        pre_stop: str = None,
        reversion: str = None,
        selector: str = None,
        status: str = None,
        strategy: str = None,
        update_time: int = None,
        vext_server_group_id: str = None,
        vserver_group_id: str = None,
    ):
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.base_component_meta_name = base_component_meta_name
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cpu_limit = cpu_limit
        self.cpu_request = cpu_request
        self.create_time = create_time
        self.cs_cluster_id = cs_cluster_id
        self.deployment_name = deployment_name
        self.env = env
        self.ephemeral_storage_limit = ephemeral_storage_limit
        self.ephemeral_storage_request = ephemeral_storage_request
        self.group_id = group_id
        self.group_name = group_name
        self.group_type = group_type
        self.labels = labels
        self.last_update_time = last_update_time
        self.memory_limit = memory_limit
        self.memory_request = memory_request
        self.name_space = name_space
        self.package_public_url = package_public_url
        self.package_url = package_url
        self.package_version = package_version
        self.package_version_id = package_version_id
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.reversion = reversion
        self.selector = selector
        self.status = status
        self.strategy = strategy
        self.update_time = update_time
        self.vext_server_group_id = vext_server_group_id
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id

        if self.base_component_meta_name is not None:
            result['BaseComponentMetaName'] = self.base_component_meta_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit

        if self.cpu_request is not None:
            result['CpuRequest'] = self.cpu_request

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cs_cluster_id is not None:
            result['CsClusterId'] = self.cs_cluster_id

        if self.deployment_name is not None:
            result['DeploymentName'] = self.deployment_name

        if self.env is not None:
            result['Env'] = self.env

        if self.ephemeral_storage_limit is not None:
            result['EphemeralStorageLimit'] = self.ephemeral_storage_limit

        if self.ephemeral_storage_request is not None:
            result['EphemeralStorageRequest'] = self.ephemeral_storage_request

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit

        if self.memory_request is not None:
            result['MemoryRequest'] = self.memory_request

        if self.name_space is not None:
            result['NameSpace'] = self.name_space

        if self.package_public_url is not None:
            result['PackagePublicUrl'] = self.package_public_url

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.package_version_id is not None:
            result['PackageVersionId'] = self.package_version_id

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.reversion is not None:
            result['Reversion'] = self.reversion

        if self.selector is not None:
            result['Selector'] = self.selector

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vext_server_group_id is not None:
            result['VExtServerGroupId'] = self.vext_server_group_id

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')

        if m.get('BaseComponentMetaName') is not None:
            self.base_component_meta_name = m.get('BaseComponentMetaName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')

        if m.get('CpuRequest') is not None:
            self.cpu_request = m.get('CpuRequest')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CsClusterId') is not None:
            self.cs_cluster_id = m.get('CsClusterId')

        if m.get('DeploymentName') is not None:
            self.deployment_name = m.get('DeploymentName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('EphemeralStorageLimit') is not None:
            self.ephemeral_storage_limit = m.get('EphemeralStorageLimit')

        if m.get('EphemeralStorageRequest') is not None:
            self.ephemeral_storage_request = m.get('EphemeralStorageRequest')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')

        if m.get('MemoryRequest') is not None:
            self.memory_request = m.get('MemoryRequest')

        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')

        if m.get('PackagePublicUrl') is not None:
            self.package_public_url = m.get('PackagePublicUrl')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('PackageVersionId') is not None:
            self.package_version_id = m.get('PackageVersionId')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('Reversion') is not None:
            self.reversion = m.get('Reversion')

        if m.get('Selector') is not None:
            self.selector = m.get('Selector')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VExtServerGroupId') is not None:
            self.vext_server_group_id = m.get('VExtServerGroupId')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListAllInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAllInstancesResponseBodyData] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total = total

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
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListAllInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAllInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_config_id: str = None,
        agent_config_name: str = None,
        attributes: List[main_models.ListAllInstancesResponseBodyDataAttributes] = None,
        cluster_id: str = None,
        cluster_name: str = None,
        image_id: str = None,
        install_level: str = None,
        install_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        kernel_version: str = None,
        manage_level: str = None,
        manage_type: str = None,
        os_arch: str = None,
        os_health_score: int = None,
        os_name: str = None,
        private_ip: str = None,
        public_ip: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        status: str = None,
    ):
        self.agent_config_id = agent_config_id
        self.agent_config_name = agent_config_name
        self.attributes = attributes
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.image_id = image_id
        self.install_level = install_level
        self.install_type = install_type
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.kernel_version = kernel_version
        self.manage_level = manage_level
        self.manage_type = manage_type
        self.os_arch = os_arch
        self.os_health_score = os_health_score
        self.os_name = os_name
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.status = status

    def validate(self):
        if self.attributes:
            for v1 in self.attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_config_id is not None:
            result['agentConfigId'] = self.agent_config_id

        if self.agent_config_name is not None:
            result['agentConfigName'] = self.agent_config_name

        result['attributes'] = []
        if self.attributes is not None:
            for k1 in self.attributes:
                result['attributes'].append(k1.to_map() if k1 else None)

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name

        if self.image_id is not None:
            result['imageId'] = self.image_id

        if self.install_level is not None:
            result['installLevel'] = self.install_level

        if self.install_type is not None:
            result['installType'] = self.install_type

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.kernel_version is not None:
            result['kernelVersion'] = self.kernel_version

        if self.manage_level is not None:
            result['manageLevel'] = self.manage_level

        if self.manage_type is not None:
            result['manageType'] = self.manage_type

        if self.os_arch is not None:
            result['osArch'] = self.os_arch

        if self.os_health_score is not None:
            result['osHealthScore'] = self.os_health_score

        if self.os_name is not None:
            result['osName'] = self.os_name

        if self.private_ip is not None:
            result['privateIp'] = self.private_ip

        if self.public_ip is not None:
            result['publicIp'] = self.public_ip

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['resourceGroupName'] = self.resource_group_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentConfigId') is not None:
            self.agent_config_id = m.get('agentConfigId')

        if m.get('agentConfigName') is not None:
            self.agent_config_name = m.get('agentConfigName')

        self.attributes = []
        if m.get('attributes') is not None:
            for k1 in m.get('attributes'):
                temp_model = main_models.ListAllInstancesResponseBodyDataAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')

        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')

        if m.get('installLevel') is not None:
            self.install_level = m.get('installLevel')

        if m.get('installType') is not None:
            self.install_type = m.get('installType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('kernelVersion') is not None:
            self.kernel_version = m.get('kernelVersion')

        if m.get('manageLevel') is not None:
            self.manage_level = m.get('manageLevel')

        if m.get('manageType') is not None:
            self.manage_type = m.get('manageType')

        if m.get('osArch') is not None:
            self.os_arch = m.get('osArch')

        if m.get('osHealthScore') is not None:
            self.os_health_score = m.get('osHealthScore')

        if m.get('osName') is not None:
            self.os_name = m.get('osName')

        if m.get('privateIp') is not None:
            self.private_ip = m.get('privateIp')

        if m.get('publicIp') is not None:
            self.public_ip = m.get('publicIp')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('resourceGroupName') is not None:
            self.resource_group_name = m.get('resourceGroupName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListAllInstancesResponseBodyDataAttributes(DaraModel):
    def __init__(
        self,
        info_key: str = None,
        info_type: str = None,
        info_value: str = None,
    ):
        self.info_key = info_key
        self.info_type = info_type
        self.info_value = info_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_key is not None:
            result['infoKey'] = self.info_key

        if self.info_type is not None:
            result['infoType'] = self.info_type

        if self.info_value is not None:
            result['infoValue'] = self.info_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('infoKey') is not None:
            self.info_key = m.get('infoKey')

        if m.get('infoType') is not None:
            self.info_type = m.get('infoType')

        if m.get('infoValue') is not None:
            self.info_value = m.get('infoValue')

        return self


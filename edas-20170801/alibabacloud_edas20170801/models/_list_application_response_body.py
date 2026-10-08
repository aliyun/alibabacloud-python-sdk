# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application_list: main_models.ListApplicationResponseBodyApplicationList = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.application_list = application_list
        # The status code of the response.
        self.code = code
        # The additional information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application_list:
            self.application_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_list is not None:
            result['ApplicationList'] = self.application_list.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationList') is not None:
            temp_model = main_models.ListApplicationResponseBodyApplicationList()
            self.application_list = temp_model.from_map(m.get('ApplicationList'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListApplicationResponseBodyApplicationList(DaraModel):
    def __init__(
        self,
        application: List[main_models.ListApplicationResponseBodyApplicationListApplication] = None,
    ):
        self.application = application

    def validate(self):
        if self.application:
            for v1 in self.application:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Application'] = []
        if self.application is not None:
            for k1 in self.application:
                result['Application'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application = []
        if m.get('Application') is not None:
            for k1 in m.get('Application'):
                temp_model = main_models.ListApplicationResponseBodyApplicationListApplication()
                self.application.append(temp_model.from_map(k1))

        return self

class ListApplicationResponseBodyApplicationListApplication(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        application_type: str = None,
        build_package_id: int = None,
        cluster_id: str = None,
        cluster_type: int = None,
        create_time: int = None,
        ext_slb_ip: str = None,
        ext_slb_listener_port: int = None,
        instances: int = None,
        k_8s_namespace: str = None,
        name: str = None,
        namespace_id: str = None,
        port: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        running_instance_count: int = None,
        slb_ip: str = None,
        slb_listener_port: int = None,
        slb_port: int = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.application_type = application_type
        self.build_package_id = build_package_id
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.create_time = create_time
        self.ext_slb_ip = ext_slb_ip
        self.ext_slb_listener_port = ext_slb_listener_port
        self.instances = instances
        self.k_8s_namespace = k_8s_namespace
        self.name = name
        self.namespace_id = namespace_id
        self.port = port
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.running_instance_count = running_instance_count
        self.slb_ip = slb_ip
        self.slb_listener_port = slb_listener_port
        self.slb_port = slb_port
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.build_package_id is not None:
            result['BuildPackageId'] = self.build_package_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ext_slb_ip is not None:
            result['ExtSlbIp'] = self.ext_slb_ip

        if self.ext_slb_listener_port is not None:
            result['ExtSlbListenerPort'] = self.ext_slb_listener_port

        if self.instances is not None:
            result['Instances'] = self.instances

        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.running_instance_count is not None:
            result['RunningInstanceCount'] = self.running_instance_count

        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip

        if self.slb_listener_port is not None:
            result['SlbListenerPort'] = self.slb_listener_port

        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('BuildPackageId') is not None:
            self.build_package_id = m.get('BuildPackageId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExtSlbIp') is not None:
            self.ext_slb_ip = m.get('ExtSlbIp')

        if m.get('ExtSlbListenerPort') is not None:
            self.ext_slb_listener_port = m.get('ExtSlbListenerPort')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RunningInstanceCount') is not None:
            self.running_instance_count = m.get('RunningInstanceCount')

        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')

        if m.get('SlbListenerPort') is not None:
            self.slb_listener_port = m.get('SlbListenerPort')

        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self


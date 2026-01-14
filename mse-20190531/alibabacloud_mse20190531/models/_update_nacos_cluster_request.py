# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNacosClusterRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        check_port: int = None,
        cluster_name: str = None,
        group_name: str = None,
        health_checker: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        service_name: str = None,
        use_instance_port_for_check: bool = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The port used for health checks.
        self.check_port = check_port
        # The name of the Nacos cluster.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The name of the group.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The type of the health check.
        self.health_checker = health_checker
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The name of the service.
        # 
        # This parameter is required.
        self.service_name = service_name
        # Specifies whether to use the port of the instance for a health check.
        self.use_instance_port_for_check = use_instance_port_for_check

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.check_port is not None:
            result['CheckPort'] = self.check_port

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.health_checker is not None:
            result['HealthChecker'] = self.health_checker

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.use_instance_port_for_check is not None:
            result['UseInstancePortForCheck'] = self.use_instance_port_for_check

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('CheckPort') is not None:
            self.check_port = m.get('CheckPort')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HealthChecker') is not None:
            self.health_checker = m.get('HealthChecker')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('UseInstancePortForCheck') is not None:
            self.use_instance_port_for_check = m.get('UseInstancePortForCheck')

        return self


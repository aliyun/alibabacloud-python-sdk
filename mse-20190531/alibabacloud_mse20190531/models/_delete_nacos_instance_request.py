# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNacosInstanceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_name: str = None,
        ephemeral: bool = None,
        group_name: str = None,
        instance_id: str = None,
        ip: str = None,
        namespace_id: str = None,
        port: int = None,
        service_name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The alias of the cluster.
        self.cluster_name = cluster_name
        # Specifies whether the node is an ephemeral node. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        # 
        # This parameter is required.
        self.ephemeral = ephemeral
        # The name of the group.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The ID of the Nacos instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IP address of the Nacos instance.
        # 
        # This parameter is required.
        self.ip = ip
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The port of the Nacos instance.
        # 
        # This parameter is required.
        self.port = port
        # The name of the service.
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.port is not None:
            result['Port'] = self.port

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self


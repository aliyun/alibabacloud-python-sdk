# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNacosServiceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        ephemeral: bool = None,
        group_name: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        protect_threshold: str = None,
        service_name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the cluster.
        # 
        # > This operation contains both the InstanceId and ClusterId parameters. You must specify one of them.
        self.cluster_id = cluster_id
        # Specifies whether the instance is marked as a temporary node. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.ephemeral = ephemeral
        # The name of the group.
        self.group_name = group_name
        # The ID of the instance.
        # 
        # > This operation contains both the InstanceId and ClusterId parameters. You must specify one of them.
        self.instance_id = instance_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The protection threshold.
        self.protect_threshold = protect_threshold
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

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.protect_threshold is not None:
            result['ProtectThreshold'] = self.protect_threshold

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('ProtectThreshold') is not None:
            self.protect_threshold = m.get('ProtectThreshold')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self


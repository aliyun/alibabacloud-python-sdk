# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListOperationHostsResponseBody(DaraModel):
    def __init__(
        self,
        hosts: List[main_models.ListOperationHostsResponseBodyHosts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The hosts returned.
        self.hosts = hosts
        # The request ID.
        self.request_id = request_id
        # The total number of hosts returned.
        self.total_count = total_count

    def validate(self):
        if self.hosts:
            for v1 in self.hosts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hosts'] = []
        if self.hosts is not None:
            for k1 in self.hosts:
                result['Hosts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k1 in m.get('Hosts'):
                temp_model = main_models.ListOperationHostsResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOperationHostsResponseBodyHosts(DaraModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        host_id: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        ostype: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_state: str = None,
    ):
        # The address type of the host. Valid values:
        # 
        # *   **Public**
        # *   **Private**
        self.active_address_type = active_address_type
        # The remarks of the host.
        self.comment = comment
        # The host ID.
        self.host_id = host_id
        # The host name.
        self.host_name = host_name
        # The private IP address of the host.
        self.host_private_address = host_private_address
        # The public IP address of the host.
        self.host_public_address = host_public_address
        # The host OS.
        # 
        # *   **Linux**
        # *   **Windows**
        self.ostype = ostype
        # The host type. Valid values:
        # 
        # *   **Local**: on-premises host.
        # *   **Ecs**: Elastic Compute Service (ECS) instance.
        self.source = source
        # The ECS instance ID.
        self.source_instance_id = source_instance_id
        # The host status. Valid values:
        # 
        # *   **Normal**
        # *   **Release**
        self.source_instance_state = source_instance_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address

        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.source is not None:
            result['Source'] = self.source

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')

        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')

        return self


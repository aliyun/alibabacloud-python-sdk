# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetHostResponseBody(DaraModel):
    def __init__(
        self,
        host: main_models.GetHostResponseBodyHost = None,
        request_id: str = None,
    ):
        # The returned information about the host.
        self.host = host
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.host:
            self.host.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            temp_model = main_models.GetHostResponseBodyHost()
            self.host = temp_model.from_map(m.get('Host'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetHostResponseBodyHost(DaraModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        host_id: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        network_domain_id: str = None,
        ostype: str = None,
        pref_kex: str = None,
        protocols: List[main_models.GetHostResponseBodyHostProtocols] = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_state: str = None,
    ):
        # The address type of the host. Valid values:
        # 
        # *   **Public**: a public address
        # *   **Private**: a private address
        self.active_address_type = active_address_type
        # The description of the host.
        self.comment = comment
        # The ID of the host.
        self.host_id = host_id
        # The hostname.
        self.host_name = host_name
        # The internal endpoint of the host. The value is a domain name or an IP address.
        self.host_private_address = host_private_address
        # The public address of the host. The value is a domain name or an IP address.
        self.host_public_address = host_public_address
        # The ID of the network domain to which the host belongs.
        self.network_domain_id = network_domain_id
        # The operating system of the host. Valid values:
        # 
        # *   **Linux**
        # *   **Windows**
        self.ostype = ostype
        # The preferred key exchange algorithm of the host. The value of this parameter is returned if OSType is set to Linux. Valid values:
        # 
        # *   **default**
        # *   **diffie-hellman-group1-sha1**
        # *   **diffie-hellman-group14-sha1**
        # *   **diffie-hellman-group-exchange-sha1**
        self.pref_kex = pref_kex
        # The protocol information about the host.
        self.protocols = protocols
        # The source of the host. Valid values:
        # 
        # *   **Local**: a host in a data center
        # *   **Ecs**: an Elastic Compute Service (ECS) instance
        # *   **Rds**: a host in an ApsaraDB MyBase dedicated cluster
        self.source = source
        # The ID of the ECS instance or the host in an ApsaraDB MyBase dedicated cluster.
        # 
        # >  If **Local** is returned for the **Source** parameter, no value is returned for this parameter.
        self.source_instance_id = source_instance_id
        # The status of the host. Valid values:
        # 
        # *   **Normal**: normal
        # *   **Release**: released
        self.source_instance_state = source_instance_state

    def validate(self):
        if self.protocols:
            for v1 in self.protocols:
                 if v1:
                    v1.validate()

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

        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.pref_kex is not None:
            result['PrefKex'] = self.pref_kex

        result['Protocols'] = []
        if self.protocols is not None:
            for k1 in self.protocols:
                result['Protocols'].append(k1.to_map() if k1 else None)

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

        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('PrefKex') is not None:
            self.pref_kex = m.get('PrefKex')

        self.protocols = []
        if m.get('Protocols') is not None:
            for k1 in m.get('Protocols'):
                temp_model = main_models.GetHostResponseBodyHostProtocols()
                self.protocols.append(temp_model.from_map(k1))

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')

        return self

class GetHostResponseBodyHostProtocols(DaraModel):
    def __init__(
        self,
        host_finger_print: str = None,
        port: int = None,
        protocol_name: str = None,
    ):
        # The fingerprint of the host. This parameter uniquely identifies a host. A value is returned for this parameter only if you have performed O\\&M operations on the host by using the bastion host. Otherwise, no value is returned.
        self.host_finger_print = host_finger_print
        # The service port of the host.
        self.port = port
        # The protocol that is used to connect to the host. Valid values:
        # 
        # *   **SSH**
        # *   **RDP**
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_finger_print is not None:
            result['HostFingerPrint'] = self.host_finger_print

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostFingerPrint') is not None:
            self.host_finger_print = m.get('HostFingerPrint')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        return self


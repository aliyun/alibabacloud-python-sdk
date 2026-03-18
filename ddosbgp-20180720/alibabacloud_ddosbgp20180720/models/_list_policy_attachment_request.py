# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class ListPolicyAttachmentRequest(DaraModel):
    def __init__(
        self,
        ip_port_protocol_list: List[main_models.ListPolicyAttachmentRequestIpPortProtocolList] = None,
        page_no: int = None,
        page_size: int = None,
        policy_id: str = None,
        policy_type: str = None,
        port_version: str = None,
    ):
        # The protected objects.
        self.ip_port_protocol_list = ip_port_protocol_list
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        # The ID of the policy.
        self.policy_id = policy_id
        # The type of the policy. Valid values:
        # 
        # *   **default**: the default mitigation policies.
        # *   **l3**: IP-specific mitigation policies.
        # *   **l4**: port-specific mitigation policies.
        self.policy_type = policy_type
        self.port_version = port_version

    def validate(self):
        if self.ip_port_protocol_list:
            for v1 in self.ip_port_protocol_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpPortProtocolList'] = []
        if self.ip_port_protocol_list is not None:
            for k1 in self.ip_port_protocol_list:
                result['IpPortProtocolList'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.port_version is not None:
            result['PortVersion'] = self.port_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_port_protocol_list = []
        if m.get('IpPortProtocolList') is not None:
            for k1 in m.get('IpPortProtocolList'):
                temp_model = main_models.ListPolicyAttachmentRequestIpPortProtocolList()
                self.ip_port_protocol_list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('PortVersion') is not None:
            self.port_version = m.get('PortVersion')

        return self

class ListPolicyAttachmentRequestIpPortProtocolList(DaraModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        port_range: str = None,
        protocol: str = None,
    ):
        # The IP address of the protected object.
        # 
        # This parameter is required.
        self.ip = ip
        # The port number of the protected object.
        self.port = port
        self.port_range = port_range
        # The protocol type of the protected object. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self


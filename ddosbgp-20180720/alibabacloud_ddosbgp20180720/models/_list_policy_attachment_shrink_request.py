# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPolicyAttachmentShrinkRequest(DaraModel):
    def __init__(
        self,
        ip_port_protocol_list_shrink: str = None,
        page_no: int = None,
        page_size: int = None,
        policy_id: str = None,
        policy_type: str = None,
        port_version: str = None,
    ):
        # The protected objects.
        self.ip_port_protocol_list_shrink = ip_port_protocol_list_shrink
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
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_port_protocol_list_shrink is not None:
            result['IpPortProtocolList'] = self.ip_port_protocol_list_shrink

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
        if m.get('IpPortProtocolList') is not None:
            self.ip_port_protocol_list_shrink = m.get('IpPortProtocolList')

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


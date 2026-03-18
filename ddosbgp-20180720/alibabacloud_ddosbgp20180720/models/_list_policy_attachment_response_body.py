# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class ListPolicyAttachmentResponseBody(DaraModel):
    def __init__(
        self,
        attachment_list: List[main_models.ListPolicyAttachmentResponseBodyAttachmentList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The records of attachments to the mitigation policy.
        self.attachment_list = attachment_list
        # The request ID.
        self.request_id = request_id
        # The total number of attachments to the mitigation policy.
        self.total = total

    def validate(self):
        if self.attachment_list:
            for v1 in self.attachment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttachmentList'] = []
        if self.attachment_list is not None:
            for k1 in self.attachment_list:
                result['AttachmentList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachment_list = []
        if m.get('AttachmentList') is not None:
            for k1 in m.get('AttachmentList'):
                temp_model = main_models.ListPolicyAttachmentResponseBodyAttachmentList()
                self.attachment_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListPolicyAttachmentResponseBodyAttachmentList(DaraModel):
    def __init__(
        self,
        ip: str = None,
        member_uid: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_remark: str = None,
        policy_type: str = None,
        port: int = None,
        port_range: str = None,
        protocol: str = None,
        region: str = None,
    ):
        # The IP address of the protected object.
        self.ip = ip
        # The UID of the member to which the IP address of the protected object belongs.
        self.member_uid = member_uid
        # The ID of the policy.
        self.policy_id = policy_id
        # The name of the rule.
        self.policy_name = policy_name
        # The description of the policy.
        self.policy_remark = policy_remark
        # The type of the policy. Valid values:
        # 
        # *   **l3**: IP-specific mitigation policies.
        # *   **l4**: port-specific mitigation policies.
        self.policy_type = policy_type
        # The port number of the protected object.
        self.port = port
        self.port_range = port_range
        # The protocol type of the protected object. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.protocol = protocol
        # The region to which the IP address of the protected object belongs.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_remark is not None:
            result['PolicyRemark'] = self.policy_remark

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.port is not None:
            result['Port'] = self.port

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyRemark') is not None:
            self.policy_remark = m.get('PolicyRemark')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self


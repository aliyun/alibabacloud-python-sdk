# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyDomainOwnerRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        instance_id: str = None,
        protocol: str = None,
        verify_type: str = None,
    ):
        # The domain name of which you want to verify the ownership.
        # 
        # You can specify this parameter to check whether a domain name is added to WAF. Fuzzy match is supported.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The protocol type that is used for file verification. Specify this parameter when you set VerifyType to fileCheck. Valid values:
        # 
        # *   **HTTP**
        # *   **HTTPS**
        self.protocol = protocol
        # The verification method. Valid values:
        # 
        # *   **dnsCheck**: DNS verification
        # *   **fileCheck**: file verification
        # 
        # This parameter is required.
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')

        return self


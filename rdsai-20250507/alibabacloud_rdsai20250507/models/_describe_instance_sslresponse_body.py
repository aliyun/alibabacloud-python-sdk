# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceSSLResponseBody(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        catype: str = None,
        instance_name: str = None,
        request_id: str = None,
        sslenabled: str = None,
        server_cert: str = None,
        server_key: str = None,
    ):
        self.branch_name = branch_name
        # The certificate type. The value is **custom**, which indicates that a custom certificate is used.
        self.catype = catype
        # The instance ID of the AI application.
        self.instance_name = instance_name
        # The request ID.
        self.request_id = request_id
        # Indicates whether SSL is enabled. Valid values:
        # * **1**: Enabled.
        # * **0**: Disabled.
        self.sslenabled = sslenabled
        # The custom certificate content.
        self.server_cert = server_cert
        # The private key of the certificate.
        self.server_key = server_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.catype is not None:
            result['CAType'] = self.catype

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        if self.server_cert is not None:
            result['ServerCert'] = self.server_cert

        if self.server_key is not None:
            result['ServerKey'] = self.server_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('CAType') is not None:
            self.catype = m.get('CAType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        if m.get('ServerCert') is not None:
            self.server_cert = m.get('ServerCert')

        if m.get('ServerKey') is not None:
            self.server_key = m.get('ServerKey')

        return self


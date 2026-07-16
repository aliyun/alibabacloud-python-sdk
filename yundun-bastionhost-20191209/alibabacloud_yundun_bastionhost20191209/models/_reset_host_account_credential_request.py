# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetHostAccountCredentialRequest(DaraModel):
    def __init__(
        self,
        credential_type: str = None,
        host_account_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The type of logon credential to clear. Valid values:
        # 
        # - **Password**: The password.
        # 
        # - **PrivateKey**: The SSH private key.
        # 
        # This parameter is required.
        self.credential_type = credential_type
        # The ID of the host account. The logon credential of this account will be cleared.
        # 
        # > Call the [ListHostAccounts](https://help.aliyun.com/document_detail/204372.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.host_account_id = host_account_id
        # The ID of the Bastionhost instance. The instance contains the host account.
        # 
        # > Call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the Bastionhost instance.
        # 
        # > For information about region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


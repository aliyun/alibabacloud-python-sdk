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
        project_id: int = None,
        region_id: str = None,
    ):
        # The type of the logon credential to purge. Valid values:
        # - **Password**: password
        # - **PrivateKey**: SSH private key
        # 
        # This parameter is required.
        self.credential_type = credential_type
        # The ID of the host account whose logon credentials you want to purge.
        # > You can call the [ListHostAccounts](https://help.aliyun.com/document_detail/204372.html) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.host_account_id = host_account_id
        # The instance ID of the Bastionhost instance to which the host account whose logon credentials you want to purge belongs.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The project ID.
        self.project_id = project_id
        # The region ID of the Bastionhost instance to which the host account whose logon credentials you want to purge belongs.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


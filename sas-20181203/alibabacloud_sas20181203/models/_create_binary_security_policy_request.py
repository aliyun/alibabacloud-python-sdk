# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBinarySecurityPolicyRequest(DaraModel):
    def __init__(
        self,
        clusters: str = None,
        name: str = None,
        policy: str = None,
        remark: str = None,
        resource_owner_id: int = None,
        source_ip: str = None,
        status: str = None,
    ):
        # The information about the cluster.
        # 
        # This parameter is required.
        self.clusters = clusters
        # The name of the policy.
        self.name = name
        # The content of the policy. Specify a value in the JSON format. You can specify the following keys:
        # 
        # *   **policyMode**: the type of the policy. Default value: requireAttestor.
        # *   **requiredAttestors**: the required witnesses.
        # 
        # This parameter is required.
        self.policy = policy
        # The description.
        self.remark = remark
        self.resource_owner_id = resource_owner_id
        # The source IP address.
        self.source_ip = source_ip
        # The status of the policy. Valid values:
        # 
        # *   **enable**
        # *   **disable**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clusters is not None:
            result['Clusters'] = self.clusters

        if self.name is not None:
            result['Name'] = self.name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


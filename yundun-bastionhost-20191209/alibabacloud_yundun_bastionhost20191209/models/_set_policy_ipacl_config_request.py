# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class SetPolicyIPAclConfigRequest(DaraModel):
    def __init__(
        self,
        ipacl_config: main_models.SetPolicyIPAclConfigRequestIPAclConfig = None,
        instance_id: str = None,
        policy_id: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The source IP address restriction configuration.
        # 
        # This parameter is required.
        self.ipacl_config = ipacl_config
        # The ID of the bastion host instance.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain the bastion host instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the control policy that you want to modify.
        # 
        # > You can call the [ListPolicies](https://help.aliyun.com/document_detail/2758876.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The project ID.
        self.project_id = project_id
        # The region ID of the bastion host.
        # 
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        if self.ipacl_config:
            self.ipacl_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipacl_config is not None:
            result['IPAclConfig'] = self.ipacl_config.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPAclConfig') is not None:
            temp_model = main_models.SetPolicyIPAclConfigRequestIPAclConfig()
            self.ipacl_config = temp_model.from_map(m.get('IPAclConfig'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class SetPolicyIPAclConfigRequestIPAclConfig(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        ips: List[str] = None,
    ):
        # The source IP address restriction mode. Valid values:
        # 
        # - **black**: blacklist mode
        # - **white**: whitelist mode
        # 
        # This parameter is required.
        self.acl_type = acl_type
        # The list of restricted source IP addresses.
        # 
        # > - When AclType is set to white, the IPs list is required.
        # > - When AclType is set to black but you do not need to set a source IP blacklist, pass an empty list for IPs.
        # 
        # This parameter is required.
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.ips is not None:
            result['IPs'] = self.ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('IPs') is not None:
            self.ips = m.get('IPs')

        return self


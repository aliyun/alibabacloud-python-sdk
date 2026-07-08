# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPolicyRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        policy_content: str = None,
        policy_desc: str = None,
        policy_id: str = None,
        policy_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   false (default): performs a dry run and performs the actual request.
        # *   true: performs only a dry run.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The document of the tag policy.
        # 
        # For more information about the syntax of a tag policy, see [Syntax of a tag policy](https://help.aliyun.com/document_detail/417436.html).
        self.policy_content = policy_content
        # The description of the tag policy.
        # 
        # The description must be 0 to 512 characters in length.
        self.policy_desc = policy_desc
        # The ID of the tag policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The name of the tag policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and underscores (_).
        self.policy_name = policy_name
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content

        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')

        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        return self


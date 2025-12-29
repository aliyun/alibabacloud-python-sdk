# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class CreatePatchBaselineRequest(DaraModel):
    def __init__(
        self,
        approval_rules: str = None,
        approved_patches: List[str] = None,
        approved_patches_enable_non_security: bool = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        operation_system: str = None,
        region_id: str = None,
        rejected_patches: List[str] = None,
        rejected_patches_action: str = None,
        resource_group_id: str = None,
        sources: List[str] = None,
        tags: List[main_models.CreatePatchBaselineRequestTags] = None,
    ):
        # The rules of scanning and installing patches for the specified operating system.
        # 
        # This parameter is required.
        self.approval_rules = approval_rules
        # The approved patches.
        self.approved_patches = approved_patches
        # Specifies whether the approved patch involves updates other than security-related updates.
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the patch baseline.
        self.description = description
        # The name of the patch baseline.
        # 
        # This parameter is required.
        self.name = name
        # The type of the operating system. Valid values:
        # 
        # *   Windows
        # *   Ubuntu
        # *   CentOS
        # *   Debian
        # *   AliyunLinux
        # *   RedhatEnterpriseLinux
        # *   Anolis
        # *   AlmaLinux
        # 
        # This parameter is required.
        self.operation_system = operation_system
        # The ID of the region in which you want to create a patch baseline.
        self.region_id = region_id
        # The rejected patches.
        self.rejected_patches = rejected_patches
        # The action of the rejected patch.
        self.rejected_patches_action = rejected_patches_action
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The patch source configurations.
        self.sources = sources
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules

        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches

        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches

        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sources is not None:
            result['Sources'] = self.sources

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')

        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')

        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')

        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Sources') is not None:
            self.sources = m.get('Sources')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreatePatchBaselineRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreatePatchBaselineRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


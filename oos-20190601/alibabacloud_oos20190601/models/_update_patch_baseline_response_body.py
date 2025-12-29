# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class UpdatePatchBaselineResponseBody(DaraModel):
    def __init__(
        self,
        patch_baseline: main_models.UpdatePatchBaselineResponseBodyPatchBaseline = None,
        request_id: str = None,
    ):
        # The details of the patch baseline.
        self.patch_baseline = patch_baseline
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = main_models.UpdatePatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m.get('PatchBaseline'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdatePatchBaselineResponseBodyPatchBaseline(DaraModel):
    def __init__(
        self,
        approval_rules: str = None,
        approved_patches: List[str] = None,
        approved_patches_enable_non_security: bool = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        operation_system: str = None,
        rejected_patches: List[str] = None,
        rejected_patches_action: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        sources: List[str] = None,
        tags: List[main_models.UpdatePatchBaselineResponseBodyPatchBaselineTags] = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules
        # The approved patches.
        self.approved_patches = approved_patches
        # Indicates whether the approved patch involves updates other than security-related updates.
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The creator of the patch baseline.
        self.created_by = created_by
        # The time when the patch baseline was created.
        self.created_date = created_date
        # The description of the patch baseline.
        self.description = description
        # The ID of the patch baseline.
        self.id = id
        # The name of the patch baseline.
        self.name = name
        # The operating system.
        self.operation_system = operation_system
        # The rejected patches.
        self.rejected_patches = rejected_patches
        # The action of the rejected patch.
        self.rejected_patches_action = rejected_patches_action
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the patch baseline.
        self.share_type = share_type
        # The patch source configurations.
        self.sources = sources
        # The tags.
        self.tags = tags
        # The user who updated the patch baseline.
        self.updated_by = updated_by
        # The time when the patch baseline was updated.
        self.updated_date = updated_date

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

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system

        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches

        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.sources is not None:
            result['Sources'] = self.sources

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by

        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')

        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')

        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')

        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')

        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('Sources') is not None:
            self.sources = m.get('Sources')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UpdatePatchBaselineResponseBodyPatchBaselineTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        return self

class UpdatePatchBaselineResponseBodyPatchBaselineTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListPatchBaselinesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        patch_baselines: List[main_models.ListPatchBaselinesResponseBodyPatchBaselines] = None,
        request_id: str = None,
    ):
        # The number of entries per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The patch baselines.
        self.patch_baselines = patch_baselines
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.patch_baselines:
            for v1 in self.patch_baselines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PatchBaselines'] = []
        if self.patch_baselines is not None:
            for k1 in self.patch_baselines:
                result['PatchBaselines'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.patch_baselines = []
        if m.get('PatchBaselines') is not None:
            for k1 in m.get('PatchBaselines'):
                temp_model = main_models.ListPatchBaselinesResponseBodyPatchBaselines()
                self.patch_baselines.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPatchBaselinesResponseBodyPatchBaselines(DaraModel):
    def __init__(
        self,
        approved_patches: List[str] = None,
        approved_patches_enable_non_security: bool = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        is_default: bool = None,
        name: str = None,
        operation_system: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        sources: List[str] = None,
        tags: List[main_models.ListPatchBaselinesResponseBodyPatchBaselinesTags] = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The approved patches.
        self.approved_patches = approved_patches
        # Indicates whether the approved patch involves updates other than security-related updates.
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The user who created the patch baseline.
        self.created_by = created_by
        # The time when the patch baseline was created.
        self.created_date = created_date
        # The description of the patch baseline.
        self.description = description
        # The ID of the patch baseline.
        self.id = id
        # Indicates whether the patch baseline is set as the default patch baseline.
        self.is_default = is_default
        # The name of the patch baseline.
        self.name = name
        # The type of the operating system.
        self.operation_system = operation_system
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the patch baseline.
        self.share_type = share_type
        # The configurations of patch sources.
        self.sources = sources
        # The tags of the patch baseline.
        self.tags = tags
        # The user who last updated the patch baseline.
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

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.name is not None:
            result['Name'] = self.name

        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system

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

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('Sources') is not None:
            self.sources = m.get('Sources')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPatchBaselinesResponseBodyPatchBaselinesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        return self

class ListPatchBaselinesResponseBodyPatchBaselinesTags(DaraModel):
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class CreateSkillResponseBody(DaraModel):
    def __init__(
        self,
        catalog_revision: int = None,
        content: Dict[str, Any] = None,
        created_at: str = None,
        dbtypes: List[str] = None,
        description: str = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        skill: main_models.CreateSkillResponseBodySkill = None,
        skill_type: str = None,
        version: main_models.CreateSkillResponseBodyVersion = None,
    ):
        # The Skill catalog revision number.
        self.catalog_revision = catalog_revision
        # The content grouped by database type.
        self.content = content
        # The creation time.
        self.created_at = created_at
        # The list of database types.
        self.dbtypes = dbtypes
        # The Skill description.
        self.description = description
        # The unique identifier of the Skill.
        self.id = id
        # The Skill name.
        self.name = name
        # The unique request identifier.
        self.request_id = request_id
        # The created Skill.
        self.skill = skill
        # The Skill type.
        self.skill_type = skill_type
        # The created Skill version.
        self.version = version

    def validate(self):
        if self.skill:
            self.skill.validate()
        if self.version:
            self.version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_revision is not None:
            result['CatalogRevision'] = self.catalog_revision

        if self.content is not None:
            result['Content'] = self.content

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.dbtypes is not None:
            result['Dbtypes'] = self.dbtypes

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skill is not None:
            result['Skill'] = self.skill.to_map()

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        if self.version is not None:
            result['Version'] = self.version.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogRevision') is not None:
            self.catalog_revision = m.get('CatalogRevision')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Dbtypes') is not None:
            self.dbtypes = m.get('Dbtypes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Skill') is not None:
            temp_model = main_models.CreateSkillResponseBodySkill()
            self.skill = temp_model.from_map(m.get('Skill'))

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        if m.get('Version') is not None:
            temp_model = main_models.CreateSkillResponseBodyVersion()
            self.version = temp_model.from_map(m.get('Version'))

        return self

class CreateSkillResponseBodyVersion(DaraModel):
    def __init__(
        self,
        activated_at: str = None,
        created_at: str = None,
        credential_required: bool = None,
        id: str = None,
        package_size: int = None,
        revoke_reason: str = None,
        revoked_at: str = None,
        sha_256: str = None,
        skill_id: str = None,
        status: str = None,
        version: str = None,
    ):
        # The activation time of the Skill version.
        self.activated_at = activated_at
        # The creation time of the Skill version.
        self.created_at = created_at
        # Indicates whether the Skill requires a credential.
        self.credential_required = credential_required
        # The Skill version ID.
        self.id = id
        # The Skill package size, in bytes.
        self.package_size = package_size
        # The revocation reason of the Skill version.
        self.revoke_reason = revoke_reason
        # The revocation time of the Skill version.
        self.revoked_at = revoked_at
        # The SHA-256 digest of the Skill package.
        self.sha_256 = sha_256
        # The ID of the parent Skill.
        self.skill_id = skill_id
        # The status of the Skill version.
        self.status = status
        # The Skill version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activated_at is not None:
            result['ActivatedAt'] = self.activated_at

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.credential_required is not None:
            result['CredentialRequired'] = self.credential_required

        if self.id is not None:
            result['Id'] = self.id

        if self.package_size is not None:
            result['PackageSize'] = self.package_size

        if self.revoke_reason is not None:
            result['RevokeReason'] = self.revoke_reason

        if self.revoked_at is not None:
            result['RevokedAt'] = self.revoked_at

        if self.sha_256 is not None:
            result['Sha256'] = self.sha_256

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivatedAt') is not None:
            self.activated_at = m.get('ActivatedAt')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('CredentialRequired') is not None:
            self.credential_required = m.get('CredentialRequired')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PackageSize') is not None:
            self.package_size = m.get('PackageSize')

        if m.get('RevokeReason') is not None:
            self.revoke_reason = m.get('RevokeReason')

        if m.get('RevokedAt') is not None:
            self.revoked_at = m.get('RevokedAt')

        if m.get('Sha256') is not None:
            self.sha_256 = m.get('Sha256')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateSkillResponseBodySkill(DaraModel):
    def __init__(
        self,
        active_version_id: str = None,
        category: str = None,
        created_at: str = None,
        description: str = None,
        display_name: str = None,
        icon: str = None,
        id: str = None,
        is_deleted: bool = None,
        scope: str = None,
        slug: str = None,
        updated_at: str = None,
    ):
        # The ID of the currently active version.
        self.active_version_id = active_version_id
        # The Skill category.
        self.category = category
        # The Skill creation time.
        self.created_at = created_at
        # The Skill description.
        self.description = description
        # The Skill display name.
        self.display_name = display_name
        # The public HTTPS URL of the current icon. This value is empty if no icon is configured.
        self.icon = icon
        # Skill ID
        self.id = id
        # Indicates whether the Skill is deleted.
        self.is_deleted = is_deleted
        # The visibility scope of the Skill.
        self.scope = scope
        # The stable identifier of the Skill.
        self.slug = slug
        # The Skill update time.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_version_id is not None:
            result['ActiveVersionId'] = self.active_version_id

        if self.category is not None:
            result['Category'] = self.category

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.id is not None:
            result['Id'] = self.id

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveVersionId') is not None:
            self.active_version_id = m.get('ActiveVersionId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self


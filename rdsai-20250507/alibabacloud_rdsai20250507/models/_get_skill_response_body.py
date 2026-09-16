# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetSkillResponseBody(DaraModel):
    def __init__(
        self,
        active_version_id: str = None,
        category: str = None,
        content: Dict[str, Any] = None,
        created_at: str = None,
        dbtypes: List[str] = None,
        description: str = None,
        display_name: str = None,
        icon: str = None,
        id: str = None,
        is_deleted: bool = None,
        name: str = None,
        request_id: str = None,
        scope: str = None,
        skill_type: str = None,
        slug: str = None,
        updated_at: str = None,
        versions: List[main_models.GetSkillResponseBodyVersions] = None,
    ):
        # The currently active version ID.
        self.active_version_id = active_version_id
        # The Skill category.
        self.category = category
        # The content.
        self.content = content
        # The creation time.
        self.created_at = created_at
        # The list of database types.
        self.dbtypes = dbtypes
        # The Skill description, up to 1000 characters.
        self.description = description
        # The Skill display name.
        self.display_name = display_name
        # The public HTTPS URL of the current icon. This value is empty if no icon is configured.
        self.icon = icon
        # The unique identifier of the Skill.
        self.id = id
        # Indicates whether the Skill is deleted.
        self.is_deleted = is_deleted
        # The Skill name. The name can contain only lowercase letters, digits, and hyphens.
        self.name = name
        # The unique identifier of the request.
        self.request_id = request_id
        # The visibility scope of the Skill.
        self.scope = scope
        # The Skill type.
        self.skill_type = skill_type
        # The stable identifier of a private Skill.
        self.slug = slug
        # The update time.
        self.updated_at = updated_at
        # The list of versions visible to the current principal.
        self.versions = versions

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_version_id is not None:
            result['ActiveVersionId'] = self.active_version_id

        if self.category is not None:
            result['Category'] = self.category

        if self.content is not None:
            result['Content'] = self.content

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.dbtypes is not None:
            result['Dbtypes'] = self.dbtypes

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

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveVersionId') is not None:
            self.active_version_id = m.get('ActiveVersionId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Dbtypes') is not None:
            self.dbtypes = m.get('Dbtypes')

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.GetSkillResponseBodyVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class GetSkillResponseBodyVersions(DaraModel):
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
        skill_markdown: str = None,
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
        # The reason for revoking the Skill version.
        self.revoke_reason = revoke_reason
        # The revocation time of the Skill version.
        self.revoked_at = revoked_at
        # The SHA-256 digest of the Skill package.
        self.sha_256 = sha_256
        # The ID of the Skill to which this version belongs.
        self.skill_id = skill_id
        # The Markdown content of the Skill.
        self.skill_markdown = skill_markdown
        # The status of the Skill version.
        self.status = status
        # The version number of the Skill.
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

        if self.skill_markdown is not None:
            result['SkillMarkdown'] = self.skill_markdown

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

        if m.get('SkillMarkdown') is not None:
            self.skill_markdown = m.get('SkillMarkdown')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self


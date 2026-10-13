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
        bundle_hash: str = None,
        bundle_size_bytes: int = None,
        capabilities: main_models.GetSkillResponseBodyCapabilities = None,
        category: str = None,
        content: Dict[str, Any] = None,
        created_at: str = None,
        dbtypes: List[str] = None,
        description: str = None,
        display_name: str = None,
        download_url: str = None,
        expires_at: str = None,
        file: Dict[str, Any] = None,
        files: List[Dict[str, Any]] = None,
        frontmatter: Dict[str, Any] = None,
        icon: str = None,
        id: str = None,
        is_deleted: bool = None,
        name: str = None,
        request_id: str = None,
        scope: str = None,
        skill_id: str = None,
        skill_markdown: str = None,
        skill_type: str = None,
        slug: str = None,
        updated_at: str = None,
        version: str = None,
        version_id: str = None,
        versions: List[main_models.GetSkillResponseBodyVersions] = None,
        visibility: str = None,
    ):
        # The current active version ID.
        self.active_version_id = active_version_id
        # The content digest of the current skill bundle.
        self.bundle_hash = bundle_hash
        # The size of the current skill bundle, in bytes.
        self.bundle_size_bytes = bundle_size_bytes
        # The skill operations that the current user can perform.
        self.capabilities = capabilities
        # The skill category.
        self.category = category
        # The content.
        self.content = content
        # The creation time.
        self.created_at = created_at
        # The list of database types.
        self.dbtypes = dbtypes
        # The skill description. The description can be up to 1000 characters in length.
        self.description = description
        # The display name of the skill.
        self.display_name = display_name
        # The temporary download URL of the skill bundle.
        self.download_url = download_url
        # The expiration time of the temporary download URL.
        self.expires_at = expires_at
        # The file in the bundle that is read based on the specified path.
        self.file = file
        # The list of files in the current skill bundle.
        self.files = files
        # The metadata fields of SKILL.md.
        self.frontmatter = frontmatter
        # The public HTTPS URL of the current icon. This value is empty if no icon is configured.
        self.icon = icon
        # The unique identifier of the skill.
        self.id = id
        # Indicates whether the skill is deleted.
        self.is_deleted = is_deleted
        # The skill name. The name can contain only lowercase letters, digits, and hyphens.
        self.name = name
        # The unique request identifier.
        self.request_id = request_id
        # The visibility scope of the skill.
        self.scope = scope
        # The current skill ID.
        self.skill_id = skill_id
        # The full Markdown content of SKILL.md.
        self.skill_markdown = skill_markdown
        # The skill type.
        self.skill_type = skill_type
        # The stable identifier of the private skill.
        self.slug = slug
        # The update time.
        self.updated_at = updated_at
        # The current skill version number.
        self.version = version
        # The current skill version ID.
        self.version_id = version_id
        # The list of versions visible to the current principal.
        self.versions = versions
        # The visibility of the skill to the current user.
        self.visibility = visibility

    def validate(self):
        if self.capabilities:
            self.capabilities.validate()
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

        if self.bundle_hash is not None:
            result['BundleHash'] = self.bundle_hash

        if self.bundle_size_bytes is not None:
            result['BundleSizeBytes'] = self.bundle_size_bytes

        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities.to_map()

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

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.file is not None:
            result['File'] = self.file

        if self.files is not None:
            result['Files'] = self.files

        if self.frontmatter is not None:
            result['Frontmatter'] = self.frontmatter

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

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_markdown is not None:
            result['SkillMarkdown'] = self.skill_markdown

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.version is not None:
            result['Version'] = self.version

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveVersionId') is not None:
            self.active_version_id = m.get('ActiveVersionId')

        if m.get('BundleHash') is not None:
            self.bundle_hash = m.get('BundleHash')

        if m.get('BundleSizeBytes') is not None:
            self.bundle_size_bytes = m.get('BundleSizeBytes')

        if m.get('Capabilities') is not None:
            temp_model = main_models.GetSkillResponseBodyCapabilities()
            self.capabilities = temp_model.from_map(m.get('Capabilities'))

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

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('File') is not None:
            self.file = m.get('File')

        if m.get('Files') is not None:
            self.files = m.get('Files')

        if m.get('Frontmatter') is not None:
            self.frontmatter = m.get('Frontmatter')

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

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillMarkdown') is not None:
            self.skill_markdown = m.get('SkillMarkdown')

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.GetSkillResponseBodyVersions()
                self.versions.append(temp_model.from_map(k1))

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

class GetSkillResponseBodyVersions(DaraModel):
    def __init__(
        self,
        activated_at: str = None,
        created_at: str = None,
        credential_required: bool = None,
        file_count: int = None,
        id: str = None,
        package_size: int = None,
        revoke_reason: str = None,
        revoked_at: str = None,
        sha_256: str = None,
        skill_id: str = None,
        skill_markdown: str = None,
        source: str = None,
        status: str = None,
        update_note: str = None,
        version: str = None,
    ):
        # The activation time of the skill version.
        self.activated_at = activated_at
        # The creation time of the skill version.
        self.created_at = created_at
        # Indicates whether the skill requires a credential.
        self.credential_required = credential_required
        # The number of files in the skill bundle.
        self.file_count = file_count
        # The skill version ID.
        self.id = id
        # The size of the skill bundle, in bytes.
        self.package_size = package_size
        # The reason for revoking the skill version.
        self.revoke_reason = revoke_reason
        # The revocation time of the skill version.
        self.revoked_at = revoked_at
        # The SHA-256 digest of the skill package.
        self.sha_256 = sha_256
        # The ID of the skill to which the version belongs.
        self.skill_id = skill_id
        # The Markdown content of the skill.
        self.skill_markdown = skill_markdown
        # The creation source of the skill version.
        self.source = source
        # The status of the skill version.
        self.status = status
        # The update note for the version.
        self.update_note = update_note
        # The version number of the skill.
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

        if self.file_count is not None:
            result['FileCount'] = self.file_count

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

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.update_note is not None:
            result['UpdateNote'] = self.update_note

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

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

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

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateNote') is not None:
            self.update_note = m.get('UpdateNote')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetSkillResponseBodyCapabilities(DaraModel):
    def __init__(
        self,
        delete: bool = None,
        download: bool = None,
        edit: bool = None,
        rollback: bool = None,
        share: bool = None,
        upload: bool = None,
    ):
        # Indicates whether the skill can be deleted.
        self.delete = delete
        # Indicates whether the skill bundle can be downloaded.
        self.download = download
        # Indicates whether the skill can be edited.
        self.edit = edit
        # Indicates whether the skill version can be rolled back.
        self.rollback = rollback
        # Indicates whether the skill can be shared.
        self.share = share
        # Indicates whether a new version can be uploaded.
        self.upload = upload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete is not None:
            result['Delete'] = self.delete

        if self.download is not None:
            result['Download'] = self.download

        if self.edit is not None:
            result['Edit'] = self.edit

        if self.rollback is not None:
            result['Rollback'] = self.rollback

        if self.share is not None:
            result['Share'] = self.share

        if self.upload is not None:
            result['Upload'] = self.upload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        if m.get('Download') is not None:
            self.download = m.get('Download')

        if m.get('Edit') is not None:
            self.edit = m.get('Edit')

        if m.get('Rollback') is not None:
            self.rollback = m.get('Rollback')

        if m.get('Share') is not None:
            self.share = m.get('Share')

        if m.get('Upload') is not None:
            self.upload = m.get('Upload')

        return self


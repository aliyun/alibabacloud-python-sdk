# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Revision(DaraModel):
    def __init__(
        self,
        content_hash: str = None,
        content_hash_name: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        creator_id: str = None,
        creator_name: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        file_extension: str = None,
        file_id: str = None,
        is_latest_version: bool = None,
        keep_forever: bool = None,
        revision_description: str = None,
        revision_id: str = None,
        revision_name: str = None,
        revision_version: int = None,
        size: int = None,
        thumbnail: str = None,
        updated_at: str = None,
        url: str = None,
    ):
        # The hash value of the content.
        self.content_hash = content_hash
        # The name of the hash algorithm.
        self.content_hash_name = content_hash_name
        # The CRC64 value of the version.
        self.crc_64hash = crc_64hash
        # The time when the version was created.
        self.created_at = created_at
        # The ID of the user who created the version.
        self.creator_id = creator_id
        # The name of the user who created the version.
        self.creator_name = creator_name
        # The domain ID.
        self.domain_id = domain_id
        # The download URL. The ListRevision operation does not return this value. The GetRevision, UpdateRevision, and RestoreRevision operations return this value.
        self.download_url = download_url
        # The drive ID.
        self.drive_id = drive_id
        # The file extension.
        self.file_extension = file_extension
        # The file ID.
        self.file_id = file_id
        # Indicates whether it is the latest version.
        self.is_latest_version = is_latest_version
        # Indicates whether the version is permanently retained.
        self.keep_forever = keep_forever
        # The description of the version.
        self.revision_description = revision_description
        # The version ID.
        self.revision_id = revision_id
        # The version name.
        self.revision_name = revision_name
        # The version number.
        self.revision_version = revision_version
        # The version size.
        self.size = size
        # The URL of the thumbnail.
        self.thumbnail = thumbnail
        # The time when the version was modified.
        self.updated_at = updated_at
        # The preview URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash

        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name

        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator_id is not None:
            result['creator_id'] = self.creator_id

        if self.creator_name is not None:
            result['creator_name'] = self.creator_name

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.download_url is not None:
            result['download_url'] = self.download_url

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_extension is not None:
            result['file_extension'] = self.file_extension

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.is_latest_version is not None:
            result['is_latest_version'] = self.is_latest_version

        if self.keep_forever is not None:
            result['keep_forever'] = self.keep_forever

        if self.revision_description is not None:
            result['revision_description'] = self.revision_description

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        if self.revision_name is not None:
            result['revision_name'] = self.revision_name

        if self.revision_version is not None:
            result['revision_version'] = self.revision_version

        if self.size is not None:
            result['size'] = self.size

        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')

        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')

        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator_id') is not None:
            self.creator_id = m.get('creator_id')

        if m.get('creator_name') is not None:
            self.creator_name = m.get('creator_name')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('is_latest_version') is not None:
            self.is_latest_version = m.get('is_latest_version')

        if m.get('keep_forever') is not None:
            self.keep_forever = m.get('keep_forever')

        if m.get('revision_description') is not None:
            self.revision_description = m.get('revision_description')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        if m.get('revision_name') is not None:
            self.revision_name = m.get('revision_name')

        if m.get('revision_version') is not None:
            self.revision_version = m.get('revision_version')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self


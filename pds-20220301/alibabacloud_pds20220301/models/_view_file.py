# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class ViewFile(DaraModel):
    def __init__(
        self,
        category: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        fields: Dict[str, Any] = None,
        file_extension: str = None,
        file_id: str = None,
        file_revision_id: str = None,
        hidden: bool = None,
        investigation_info: main_models.ViewFileInvestigationInfo = None,
        joined_at: int = None,
        labels: List[str] = None,
        local_created_at: str = None,
        local_modified_at: str = None,
        name: str = None,
        parent_file_id: str = None,
        revision_id: str = None,
        size: int = None,
        starred: bool = None,
        status: str = None,
        thumbnail: str = None,
        thumbnail_urls: Dict[str, str] = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        view_id: str = None,
    ):
        self.category = category
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.content_type = content_type
        self.crc_64hash = crc_64hash
        self.created_at = created_at
        self.description = description
        self.domain_id = domain_id
        self.download_url = download_url
        self.drive_id = drive_id
        self.fields = fields
        self.file_extension = file_extension
        self.file_id = file_id
        self.file_revision_id = file_revision_id
        self.hidden = hidden
        self.investigation_info = investigation_info
        self.joined_at = joined_at
        self.labels = labels
        self.local_created_at = local_created_at
        self.local_modified_at = local_modified_at
        self.name = name
        self.parent_file_id = parent_file_id
        self.revision_id = revision_id
        self.size = size
        self.starred = starred
        self.status = status
        self.thumbnail = thumbnail
        self.thumbnail_urls = thumbnail_urls
        self.trashed_at = trashed_at
        self.type = type
        self.updated_at = updated_at
        self.upload_id = upload_id
        self.view_id = view_id

    def validate(self):
        if self.investigation_info:
            self.investigation_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.content_hash is not None:
            result['content_hash'] = self.content_hash

        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name

        if self.content_type is not None:
            result['content_type'] = self.content_type

        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.download_url is not None:
            result['download_url'] = self.download_url

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.fields is not None:
            result['fields'] = self.fields

        if self.file_extension is not None:
            result['file_extension'] = self.file_extension

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.file_revision_id is not None:
            result['file_revision_id'] = self.file_revision_id

        if self.hidden is not None:
            result['hidden'] = self.hidden

        if self.investigation_info is not None:
            result['investigation_info'] = self.investigation_info.to_map()

        if self.joined_at is not None:
            result['joined_at'] = self.joined_at

        if self.labels is not None:
            result['labels'] = self.labels

        if self.local_created_at is not None:
            result['local_created_at'] = self.local_created_at

        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at

        if self.name is not None:
            result['name'] = self.name

        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        if self.size is not None:
            result['size'] = self.size

        if self.starred is not None:
            result['starred'] = self.starred

        if self.status is not None:
            result['status'] = self.status

        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail

        if self.thumbnail_urls is not None:
            result['thumbnail_urls'] = self.thumbnail_urls

        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at

        if self.type is not None:
            result['type'] = self.type

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.upload_id is not None:
            result['upload_id'] = self.upload_id

        if self.view_id is not None:
            result['view_id'] = self.view_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')

        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')

        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')

        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('file_revision_id') is not None:
            self.file_revision_id = m.get('file_revision_id')

        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')

        if m.get('investigation_info') is not None:
            temp_model = main_models.ViewFileInvestigationInfo()
            self.investigation_info = temp_model.from_map(m.get('investigation_info'))

        if m.get('joined_at') is not None:
            self.joined_at = m.get('joined_at')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('local_created_at') is not None:
            self.local_created_at = m.get('local_created_at')

        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('starred') is not None:
            self.starred = m.get('starred')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')

        if m.get('thumbnail_urls') is not None:
            self.thumbnail_urls = m.get('thumbnail_urls')

        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')

        if m.get('view_id') is not None:
            self.view_id = m.get('view_id')

        return self

class ViewFileInvestigationInfo(DaraModel):
    def __init__(
        self,
        status: int = None,
        suggestion: str = None,
    ):
        self.status = status
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.suggestion is not None:
            result['suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('suggestion') is not None:
            self.suggestion = m.get('suggestion')

        return self


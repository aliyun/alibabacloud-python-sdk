# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from typing import Dict


class Snapshot(DaraModel):
    def __init__(
        self,
        base_manifest_list: str = None,
        changelog_manifest_list: str = None,
        changelog_record_count: int = None,
        commit_identifier: int = None,
        commit_kind: str = None,
        commit_user: str = None,
        delta_manifest_list: str = None,
        delta_record_count: int = None,
        id: int = None,
        index_manifest: str = None,
        log_offsets: Dict[str, int] = None,
        schema_id: int = None,
        statistics: str = None,
        time_millis: int = None,
        total_record_count: int = None,
        version: int = None,
        watermark: int = None,
    ):
        self.base_manifest_list = base_manifest_list
        self.changelog_manifest_list = changelog_manifest_list
        self.changelog_record_count = changelog_record_count
        self.commit_identifier = commit_identifier
        self.commit_kind = commit_kind
        self.commit_user = commit_user
        self.delta_manifest_list = delta_manifest_list
        self.delta_record_count = delta_record_count
        self.id = id
        self.index_manifest = index_manifest
        self.log_offsets = log_offsets
        self.schema_id = schema_id
        self.statistics = statistics
        self.time_millis = time_millis
        self.total_record_count = total_record_count
        self.version = version
        self.watermark = watermark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_manifest_list is not None:
            result['baseManifestList'] = self.base_manifest_list

        if self.changelog_manifest_list is not None:
            result['changelogManifestList'] = self.changelog_manifest_list

        if self.changelog_record_count is not None:
            result['changelogRecordCount'] = self.changelog_record_count

        if self.commit_identifier is not None:
            result['commitIdentifier'] = self.commit_identifier

        if self.commit_kind is not None:
            result['commitKind'] = self.commit_kind

        if self.commit_user is not None:
            result['commitUser'] = self.commit_user

        if self.delta_manifest_list is not None:
            result['deltaManifestList'] = self.delta_manifest_list

        if self.delta_record_count is not None:
            result['deltaRecordCount'] = self.delta_record_count

        if self.id is not None:
            result['id'] = self.id

        if self.index_manifest is not None:
            result['indexManifest'] = self.index_manifest

        if self.log_offsets is not None:
            result['logOffsets'] = self.log_offsets

        if self.schema_id is not None:
            result['schemaId'] = self.schema_id

        if self.statistics is not None:
            result['statistics'] = self.statistics

        if self.time_millis is not None:
            result['timeMillis'] = self.time_millis

        if self.total_record_count is not None:
            result['totalRecordCount'] = self.total_record_count

        if self.version is not None:
            result['version'] = self.version

        if self.watermark is not None:
            result['watermark'] = self.watermark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseManifestList') is not None:
            self.base_manifest_list = m.get('baseManifestList')

        if m.get('changelogManifestList') is not None:
            self.changelog_manifest_list = m.get('changelogManifestList')

        if m.get('changelogRecordCount') is not None:
            self.changelog_record_count = m.get('changelogRecordCount')

        if m.get('commitIdentifier') is not None:
            self.commit_identifier = m.get('commitIdentifier')

        if m.get('commitKind') is not None:
            self.commit_kind = m.get('commitKind')

        if m.get('commitUser') is not None:
            self.commit_user = m.get('commitUser')

        if m.get('deltaManifestList') is not None:
            self.delta_manifest_list = m.get('deltaManifestList')

        if m.get('deltaRecordCount') is not None:
            self.delta_record_count = m.get('deltaRecordCount')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('indexManifest') is not None:
            self.index_manifest = m.get('indexManifest')

        if m.get('logOffsets') is not None:
            self.log_offsets = m.get('logOffsets')

        if m.get('schemaId') is not None:
            self.schema_id = m.get('schemaId')

        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')

        if m.get('timeMillis') is not None:
            self.time_millis = m.get('timeMillis')

        if m.get('totalRecordCount') is not None:
            self.total_record_count = m.get('totalRecordCount')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('watermark') is not None:
            self.watermark = m.get('watermark')

        return self


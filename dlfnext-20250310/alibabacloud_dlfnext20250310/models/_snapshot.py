# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

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
        id_string: str = None,
        index_manifest: str = None,
        log_offsets: Dict[str, int] = None,
        parent_id_string: str = None,
        schema_id: int = None,
        sequence_number: int = None,
        statistics: str = None,
        summary: Dict[str, str] = None,
        time_millis: int = None,
        total_record_count: int = None,
        version: int = None,
        watermark: int = None,
    ):
        # The file name of the base manifest list.
        self.base_manifest_list = base_manifest_list
        # The file name of the manifest list that records all changelogs generated for the snapshot.
        self.changelog_manifest_list = changelog_manifest_list
        # The number of changelog records generated for the snapshot.
        self.changelog_record_count = changelog_record_count
        # The transaction ID of the streaming write.
        self.commit_identifier = commit_identifier
        # The streaming write type. Valid values: APPEND, COMPACT, OVERWRITE, and ANALYZE.
        self.commit_kind = commit_kind
        # The commit user, which is typically a UUID used to resume streaming writes.
        self.commit_user = commit_user
        # The file name of the manifest list that records all new changes in the snapshot.
        self.delta_manifest_list = delta_manifest_list
        # The number of new change records in the snapshot.
        self.delta_record_count = delta_record_count
        # The snapshot ID.
        self.id = id
        # The string representation of the snapshot ID.
        self.id_string = id_string
        # The file name of the manifest that records all index files of the table.
        self.index_manifest = index_manifest
        # The log offsets at the time of the commit.
        self.log_offsets = log_offsets
        # The string representation of the parent snapshot ID.
        self.parent_id_string = parent_id_string
        # The schema ID of the table when the snapshot was generated.
        self.schema_id = schema_id
        # The snapshot sequence number.
        self.sequence_number = sequence_number
        # The file name of the table statistics information.
        self.statistics = statistics
        # The summary.
        self.summary = summary
        # The commit time, which is a UNIX timestamp in milliseconds.
        self.time_millis = time_millis
        # The total number of records for all changes in the snapshot.
        self.total_record_count = total_record_count
        # The file format version of the snapshot. The current version is 3.
        self.version = version
        # The watermark value.
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

        if self.id_string is not None:
            result['idString'] = self.id_string

        if self.index_manifest is not None:
            result['indexManifest'] = self.index_manifest

        if self.log_offsets is not None:
            result['logOffsets'] = self.log_offsets

        if self.parent_id_string is not None:
            result['parentIdString'] = self.parent_id_string

        if self.schema_id is not None:
            result['schemaId'] = self.schema_id

        if self.sequence_number is not None:
            result['sequenceNumber'] = self.sequence_number

        if self.statistics is not None:
            result['statistics'] = self.statistics

        if self.summary is not None:
            result['summary'] = self.summary

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

        if m.get('idString') is not None:
            self.id_string = m.get('idString')

        if m.get('indexManifest') is not None:
            self.index_manifest = m.get('indexManifest')

        if m.get('logOffsets') is not None:
            self.log_offsets = m.get('logOffsets')

        if m.get('parentIdString') is not None:
            self.parent_id_string = m.get('parentIdString')

        if m.get('schemaId') is not None:
            self.schema_id = m.get('schemaId')

        if m.get('sequenceNumber') is not None:
            self.sequence_number = m.get('sequenceNumber')

        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('timeMillis') is not None:
            self.time_millis = m.get('timeMillis')

        if m.get('totalRecordCount') is not None:
            self.total_record_count = m.get('totalRecordCount')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('watermark') is not None:
            self.watermark = m.get('watermark')

        return self


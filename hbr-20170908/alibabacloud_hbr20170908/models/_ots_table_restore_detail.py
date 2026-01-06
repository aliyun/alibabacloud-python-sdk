# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OtsTableRestoreDetail(DaraModel):
    def __init__(
        self,
        batch_channel_count: int = None,
        index_name_suffix: str = None,
        overwrite_existing: bool = None,
        re_generate_auto_increment_pk: bool = None,
        restore_index: bool = None,
        restore_search_index: bool = None,
        search_index_name_suffix: str = None,
    ):
        self.batch_channel_count = batch_channel_count
        self.index_name_suffix = index_name_suffix
        self.overwrite_existing = overwrite_existing
        self.re_generate_auto_increment_pk = re_generate_auto_increment_pk
        self.restore_index = restore_index
        self.restore_search_index = restore_search_index
        self.search_index_name_suffix = search_index_name_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_channel_count is not None:
            result['BatchChannelCount'] = self.batch_channel_count

        if self.index_name_suffix is not None:
            result['IndexNameSuffix'] = self.index_name_suffix

        if self.overwrite_existing is not None:
            result['OverwriteExisting'] = self.overwrite_existing

        if self.re_generate_auto_increment_pk is not None:
            result['ReGenerateAutoIncrementPK'] = self.re_generate_auto_increment_pk

        if self.restore_index is not None:
            result['RestoreIndex'] = self.restore_index

        if self.restore_search_index is not None:
            result['RestoreSearchIndex'] = self.restore_search_index

        if self.search_index_name_suffix is not None:
            result['SearchIndexNameSuffix'] = self.search_index_name_suffix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchChannelCount') is not None:
            self.batch_channel_count = m.get('BatchChannelCount')

        if m.get('IndexNameSuffix') is not None:
            self.index_name_suffix = m.get('IndexNameSuffix')

        if m.get('OverwriteExisting') is not None:
            self.overwrite_existing = m.get('OverwriteExisting')

        if m.get('ReGenerateAutoIncrementPK') is not None:
            self.re_generate_auto_increment_pk = m.get('ReGenerateAutoIncrementPK')

        if m.get('RestoreIndex') is not None:
            self.restore_index = m.get('RestoreIndex')

        if m.get('RestoreSearchIndex') is not None:
            self.restore_search_index = m.get('RestoreSearchIndex')

        if m.get('SearchIndexNameSuffix') is not None:
            self.search_index_name_suffix = m.get('SearchIndexNameSuffix')

        return self


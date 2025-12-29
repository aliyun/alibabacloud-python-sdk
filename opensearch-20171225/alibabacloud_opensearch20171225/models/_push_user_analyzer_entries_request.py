# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class PushUserAnalyzerEntriesRequest(DaraModel):
    def __init__(
        self,
        entries: List[main_models.PushUserAnalyzerEntriesRequestEntries] = None,
        dry_run: bool = None,
    ):
        # The entries of the custom analyzer.
        self.entries = entries
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        if self.entries:
            for v1 in self.entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['entries'] = []
        if self.entries is not None:
            for k1 in self.entries:
                result['entries'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entries = []
        if m.get('entries') is not None:
            for k1 in m.get('entries'):
                temp_model = main_models.PushUserAnalyzerEntriesRequestEntries()
                self.entries.append(temp_model.from_map(k1))

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

class PushUserAnalyzerEntriesRequestEntries(DaraModel):
    def __init__(
        self,
        cmd: str = None,
        key: str = None,
        split_enabled: bool = None,
        value: str = None,
    ):
        # The operation to be performed on the entries.
        # 
        # Valid values:
        # 
        # *   add
        # *   delete
        self.cmd = cmd
        # The key to be used to query entries.
        self.key = key
        # Specifies whether to further analyze the terms that are generated after the search query is analyzed.
        # 
        # Default value: true.
        self.split_enabled = split_enabled
        # The analysis result.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cmd is not None:
            result['cmd'] = self.cmd

        if self.key is not None:
            result['key'] = self.key

        if self.split_enabled is not None:
            result['splitEnabled'] = self.split_enabled

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('splitEnabled') is not None:
            self.split_enabled = m.get('splitEnabled')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteBaselineCheckWhiteRecordRequest(DaraModel):
    def __init__(
        self,
        check_ids: List[int] = None,
        lang: str = None,
        record_ids: List[int] = None,
        source: str = None,
    ):
        # The IDs of check items.
        self.check_ids = check_ids
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The IDs of the whitelist records.
        self.record_ids = record_ids
        # The data source. Valid values:
        # 
        # *   **default**: host baseline
        # *   **agentless**: agentless detection
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.record_ids is not None:
            result['RecordIds'] = self.record_ids

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RecordIds') is not None:
            self.record_ids = m.get('RecordIds')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self


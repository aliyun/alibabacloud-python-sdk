# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HandleSimilarMaliciousFilesRequest(DaraModel):
    def __init__(
        self,
        event_id: int = None,
        lang: str = None,
        operation: str = None,
        scan_range: str = None,
        scenario: str = None,
    ):
        # Target alert ID
        # 
        # This parameter is required.
        self.event_id = event_id
        # Language type for request and response messages. Values include:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Handling action:
        # - addWhitelist: Add to whitelist;
        # - offWhitelist: Remove from whitelist;
        # - offline_handled: Handled offline;
        # - mark_mis_info: Report as false positive;
        # - ignore: Ignore.
        # 
        # This parameter is required.
        self.operation = operation
        # File source. Values include:
        # - agentless: Host detection;
        # - ecs_snapshot: User snapshot detection;
        # - ecs_image: User-defined image detection.
        self.scan_range = scan_range
        # Batch processing scenario:
        # - same_file_md5: Same file MD5;
        # - default (default value): Same alert type.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        return self


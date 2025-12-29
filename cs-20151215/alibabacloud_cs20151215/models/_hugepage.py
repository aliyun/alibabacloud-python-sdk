# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Hugepage(DaraModel):
    def __init__(
        self,
        khugepaged_alloc_sleep_millisecs: int = None,
        khugepaged_defrag: int = None,
        khugepaged_pages_to_scan: int = None,
        khugepaged_scan_sleep_millisecs: int = None,
        transparent_defrag: str = None,
        transparent_enabled: str = None,
    ):
        self.khugepaged_alloc_sleep_millisecs = khugepaged_alloc_sleep_millisecs
        self.khugepaged_defrag = khugepaged_defrag
        self.khugepaged_pages_to_scan = khugepaged_pages_to_scan
        self.khugepaged_scan_sleep_millisecs = khugepaged_scan_sleep_millisecs
        self.transparent_defrag = transparent_defrag
        self.transparent_enabled = transparent_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.khugepaged_alloc_sleep_millisecs is not None:
            result['khugepagedAllocSleepMillisecs'] = self.khugepaged_alloc_sleep_millisecs

        if self.khugepaged_defrag is not None:
            result['khugepagedDefrag'] = self.khugepaged_defrag

        if self.khugepaged_pages_to_scan is not None:
            result['khugepagedPagesToScan'] = self.khugepaged_pages_to_scan

        if self.khugepaged_scan_sleep_millisecs is not None:
            result['khugepagedScanSleepMillisecs'] = self.khugepaged_scan_sleep_millisecs

        if self.transparent_defrag is not None:
            result['transparentDefrag'] = self.transparent_defrag

        if self.transparent_enabled is not None:
            result['transparentEnabled'] = self.transparent_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('khugepagedAllocSleepMillisecs') is not None:
            self.khugepaged_alloc_sleep_millisecs = m.get('khugepagedAllocSleepMillisecs')

        if m.get('khugepagedDefrag') is not None:
            self.khugepaged_defrag = m.get('khugepagedDefrag')

        if m.get('khugepagedPagesToScan') is not None:
            self.khugepaged_pages_to_scan = m.get('khugepagedPagesToScan')

        if m.get('khugepagedScanSleepMillisecs') is not None:
            self.khugepaged_scan_sleep_millisecs = m.get('khugepagedScanSleepMillisecs')

        if m.get('transparentDefrag') is not None:
            self.transparent_defrag = m.get('transparentDefrag')

        if m.get('transparentEnabled') is not None:
            self.transparent_enabled = m.get('transparentEnabled')

        return self


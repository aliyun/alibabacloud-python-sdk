# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAgentlessMaliciousFilesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dealed: str = None,
        event_id: int = None,
        fuzzy_malicious_name: str = None,
        lang: str = None,
        levels: str = None,
        malicious_md_5: str = None,
        malicious_type: str = None,
        page_size: str = None,
        remark: str = None,
        scan_range: List[str] = None,
        uuid: str = None,
    ):
        # The page number of the current page in a paging query.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Specifies whether the alert has been handled. Valid values:
        # 
        # - Y: handled
        # - N: not handled.
        self.dealed = dealed
        # The event ID.
        self.event_id = event_id
        # The name of the malicious file to query.
        # > Fuzzy match is supported.
        self.fuzzy_malicious_name = fuzzy_malicious_name
        # The language type for the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The severity levels. Separate multiple values with commas (,). Valid values:
        # 
        # - serious: urgent
        # - suspicious: suspicious
        # - remind: reminder.
        self.levels = levels
        # The MD5 hash of the malicious file.
        self.malicious_md_5 = malicious_md_5
        # The alert type.
        # 
        # If Lang is set to zh, valid values:
        # 
        # - WebShell: WebShell
        # - 恶意软件: malware
        # - 恶意脚本: malicious script
        # 
        # If Lang is set to en, valid values:
        # 
        # - WebShell: WebShell
        # - Malicious Software: malware
        # - Malicious Script: malicious script.
        self.malicious_type = malicious_type
        # The maximum number of entries to return per page in a paging query.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The asset information for the vulnerability query. You can set this parameter to the asset name, public IP address, or private IP address. Fuzzy match is supported.
        self.remark = remark
        # The file source.
        self.scan_range = scan_range
        # The unique identifier of the asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.fuzzy_malicious_name is not None:
            result['FuzzyMaliciousName'] = self.fuzzy_malicious_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.levels is not None:
            result['Levels'] = self.levels

        if self.malicious_md_5 is not None:
            result['MaliciousMd5'] = self.malicious_md_5

        if self.malicious_type is not None:
            result['MaliciousType'] = self.malicious_type

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('FuzzyMaliciousName') is not None:
            self.fuzzy_malicious_name = m.get('FuzzyMaliciousName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Levels') is not None:
            self.levels = m.get('Levels')

        if m.get('MaliciousMd5') is not None:
            self.malicious_md_5 = m.get('MaliciousMd5')

        if m.get('MaliciousType') is not None:
            self.malicious_type = m.get('MaliciousType')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self


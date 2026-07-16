# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUnknownThreatDetectProcessRequest(DaraModel):
    def __init__(
        self,
        analyze_result: str = None,
        current_page: int = None,
        first_time_end: int = None,
        first_time_start: int = None,
        md_5: str = None,
        page_size: int = None,
        path: str = None,
        process_path: str = None,
        remark: str = None,
        sha_256: str = None,
        uuid: str = None,
    ):
        # The analysis result. Valid values:
        # 
        # - **black**: abnormal process
        # 
        # - **white**: normal process
        self.analyze_result = analyze_result
        # The page number to return.
        self.current_page = current_page
        # The end of the time range for the first detection, in milliseconds.
        self.first_time_end = first_time_end
        # The start of the time range for the first detection, in milliseconds.
        self.first_time_start = first_time_start
        # The MD5 value of the file.
        self.md_5 = md_5
        # The number of entries to return per page.
        self.page_size = page_size
        # The file path.
        self.path = path
        # The process path.
        self.process_path = process_path
        # The server name or IP address.
        self.remark = remark
        # The SHA-256 value of the file.
        self.sha_256 = sha_256
        # The UUID of the server to query.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyze_result is not None:
            result['AnalyzeResult'] = self.analyze_result

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.first_time_end is not None:
            result['FirstTimeEnd'] = self.first_time_end

        if self.first_time_start is not None:
            result['FirstTimeStart'] = self.first_time_start

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        if self.process_path is not None:
            result['ProcessPath'] = self.process_path

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.sha_256 is not None:
            result['Sha256'] = self.sha_256

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalyzeResult') is not None:
            self.analyze_result = m.get('AnalyzeResult')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FirstTimeEnd') is not None:
            self.first_time_end = m.get('FirstTimeEnd')

        if m.get('FirstTimeStart') is not None:
            self.first_time_start = m.get('FirstTimeStart')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('ProcessPath') is not None:
            self.process_path = m.get('ProcessPath')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Sha256') is not None:
            self.sha_256 = m.get('Sha256')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self


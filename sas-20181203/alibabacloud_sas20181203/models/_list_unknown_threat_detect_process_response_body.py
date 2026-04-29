# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListUnknownThreatDetectProcessResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListUnknownThreatDetectProcessResponseBodyData] = None,
        page_info: main_models.ListUnknownThreatDetectProcessResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data = data
        self.page_info = page_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListUnknownThreatDetectProcessResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListUnknownThreatDetectProcessResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUnknownThreatDetectProcessResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: str = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.count = count
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUnknownThreatDetectProcessResponseBodyData(DaraModel):
    def __init__(
        self,
        analyze_result: str = None,
        first_time: int = None,
        md_5: str = None,
        process_id: str = None,
        process_path: str = None,
        remark: str = None,
        sha_256: str = None,
    ):
        self.analyze_result = analyze_result
        self.first_time = first_time
        self.md_5 = md_5
        self.process_id = process_id
        self.process_path = process_path
        self.remark = remark
        self.sha_256 = sha_256

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyze_result is not None:
            result['AnalyzeResult'] = self.analyze_result

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_path is not None:
            result['ProcessPath'] = self.process_path

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.sha_256 is not None:
            result['Sha256'] = self.sha_256

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalyzeResult') is not None:
            self.analyze_result = m.get('AnalyzeResult')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessPath') is not None:
            self.process_path = m.get('ProcessPath')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Sha256') is not None:
            self.sha_256 = m.get('Sha256')

        return self


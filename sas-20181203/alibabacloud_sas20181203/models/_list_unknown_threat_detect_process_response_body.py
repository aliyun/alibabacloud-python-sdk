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
        # The returned data.
        self.data = data
        # The pagination information.
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
        # The number of entries on the current page.
        self.count = count
        # The page number of the current page in a paged query. This is used for paging.
        self.current_page = current_page
        # The maximum number of entries per page in a paged query. This is used for paging.
        self.page_size = page_size
        # The total number of entries.
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
        explanation_en: str = None,
        explanation_zh: str = None,
        first_time: int = None,
        md_5: str = None,
        process_id: str = None,
        process_path: str = None,
        remark: str = None,
        sha_256: str = None,
        tags: List[main_models.ListUnknownThreatDetectProcessResponseBodyDataTags] = None,
    ):
        # The analysis result. Valid values:
        # 
        # - **black**: Malicious process.
        # - **white**: Normal process.
        # - **abnormal**: Abnormal process.
        self.analyze_result = analyze_result
        self.explanation_en = explanation_en
        self.explanation_zh = explanation_zh
        # The timestamp when the process was first detected.
        self.first_time = first_time
        # The MD5 hash of the file.
        self.md_5 = md_5
        # The process ID of the event.
        self.process_id = process_id
        # The process path.
        self.process_path = process_path
        # The remarks.
        self.remark = remark
        # The SHA-256 hash of the file.
        self.sha_256 = sha_256
        # The process labels.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyze_result is not None:
            result['AnalyzeResult'] = self.analyze_result

        if self.explanation_en is not None:
            result['ExplanationEn'] = self.explanation_en

        if self.explanation_zh is not None:
            result['ExplanationZh'] = self.explanation_zh

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalyzeResult') is not None:
            self.analyze_result = m.get('AnalyzeResult')

        if m.get('ExplanationEn') is not None:
            self.explanation_en = m.get('ExplanationEn')

        if m.get('ExplanationZh') is not None:
            self.explanation_zh = m.get('ExplanationZh')

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

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListUnknownThreatDetectProcessResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListUnknownThreatDetectProcessResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        tag_en: str = None,
        tag_zh: str = None,
    ):
        # The English label of the process.
        self.tag_en = tag_en
        # The Chinese label of the process.
        self.tag_zh = tag_zh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_en is not None:
            result['TagEn'] = self.tag_en

        if self.tag_zh is not None:
            result['TagZh'] = self.tag_zh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagEn') is not None:
            self.tag_en = m.get('TagEn')

        if m.get('TagZh') is not None:
            self.tag_zh = m.get('TagZh')

        return self


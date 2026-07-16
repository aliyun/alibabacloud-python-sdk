# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class ScanFileOutput(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scan_file_info_list: List[main_models.ScanFileInfo] = None,
        search_information: main_models.UnifiedSearchInformation = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of scan result objects.
        self.scan_file_info_list = scan_file_info_list
        # The search execution information.
        self.search_information = search_information

    def validate(self):
        if self.scan_file_info_list:
            for v1 in self.scan_file_info_list:
                 if v1:
                    v1.validate()
        if self.search_information:
            self.search_information.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['scanFileInfoList'] = []
        if self.scan_file_info_list is not None:
            for k1 in self.scan_file_info_list:
                result['scanFileInfoList'].append(k1.to_map() if k1 else None)

        if self.search_information is not None:
            result['searchInformation'] = self.search_information.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.scan_file_info_list = []
        if m.get('scanFileInfoList') is not None:
            for k1 in m.get('scanFileInfoList'):
                temp_model = main_models.ScanFileInfo()
                self.scan_file_info_list.append(temp_model.from_map(k1))

        if m.get('searchInformation') is not None:
            temp_model = main_models.UnifiedSearchInformation()
            self.search_information = temp_model.from_map(m.get('searchInformation'))

        return self


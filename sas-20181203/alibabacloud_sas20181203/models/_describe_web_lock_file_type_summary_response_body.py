# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWebLockFileTypeSummaryResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.DescribeWebLockFileTypeSummaryResponseBodyList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of events on web tamper proofing returned.
        self.list = list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of events on web tamper proofing.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DescribeWebLockFileTypeSummaryResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWebLockFileTypeSummaryResponseBodyList(DaraModel):
    def __init__(
        self,
        count: int = None,
        type: str = None,
    ):
        # The number of attempts.
        self.count = count
        # The type of the protected file. Valid values:
        # 
        # *   **php**: PHP file
        # *   **jsp**: JSP file
        # *   **asp**: ASP file
        # *   **aspx**: ASPX file
        # *   **js**: JS file
        # *   **cgi**: CGI file
        # *   **html**: HTML file
        # *   **htm**: HTM file
        # *   **xml**: XML file
        # *   **shtml**: SHTML file
        # *   **shtm**: SHTM file
        # *   **jpg**: JPG file
        # *   **gif**: GIF file
        # *   **png**: PNG file
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


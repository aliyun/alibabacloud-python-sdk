# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVulListPageResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeVulListPageResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeVulListPageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVulListPageResponseBodyData(DaraModel):
    def __init__(
        self,
        cve_id: str = None,
        ext_aegis: str = None,
        id: int = None,
        is_aegis: int = None,
        is_sas: int = None,
        other_id: str = None,
        release_time: int = None,
        title: str = None,
    ):
        # The common vulnerabilities and exposures (CVE) ID of the vulnerability.
        self.cve_id = cve_id
        # The extended field for Server Guard.
        self.ext_aegis = ext_aegis
        # The primary key ID of the database.
        self.id = id
        # Indicates whether the vulnerability was detected based on version comparison. Valid values:
        # 
        # *   1: The vulnerability was detected based on version comparison.
        # *   0: The vulnerability was not detected based on version comparison.
        self.is_aegis = is_aegis
        # Indicates whether the vulnerability was detected based on proof of concept (POC) verification. Valid values:
        # 
        # *   1: The vulnerability was detected based on POC verification.
        # *   0: The vulnerability was not detected based on POC verification.
        self.is_sas = is_sas
        # The ID of the vulnerability.
        self.other_id = other_id
        # The time when the vulnerability was disclosed.
        self.release_time = release_time
        # The name of the vulnerability.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_id is not None:
            result['CveId'] = self.cve_id

        if self.ext_aegis is not None:
            result['ExtAegis'] = self.ext_aegis

        if self.id is not None:
            result['Id'] = self.id

        if self.is_aegis is not None:
            result['IsAegis'] = self.is_aegis

        if self.is_sas is not None:
            result['IsSas'] = self.is_sas

        if self.other_id is not None:
            result['OtherId'] = self.other_id

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')

        if m.get('ExtAegis') is not None:
            self.ext_aegis = m.get('ExtAegis')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsAegis') is not None:
            self.is_aegis = m.get('IsAegis')

        if m.get('IsSas') is not None:
            self.is_sas = m.get('IsSas')

        if m.get('OtherId') is not None:
            self.other_id = m.get('OtherId')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self


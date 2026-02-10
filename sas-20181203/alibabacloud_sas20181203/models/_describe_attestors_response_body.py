# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAttestorsResponseBody(DaraModel):
    def __init__(
        self,
        attestors: List[main_models.DescribeAttestorsResponseBodyAttestors] = None,
        page_info: main_models.DescribeAttestorsResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The witnesses.
        self.attestors = attestors
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.attestors:
            for v1 in self.attestors:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attestors'] = []
        if self.attestors is not None:
            for k1 in self.attestors:
                result['Attestors'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attestors = []
        if m.get('Attestors') is not None:
            for k1 in m.get('Attestors'):
                temp_model = main_models.DescribeAttestorsResponseBodyAttestors()
                self.attestors.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeAttestorsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAttestorsResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
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

class DescribeAttestorsResponseBodyAttestors(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        key_region_id: str = None,
        key_version_id: str = None,
        name: str = None,
        remark: str = None,
    ):
        # The ID of the KMS key.
        self.key_id = key_id
        # The region ID of the KMS key.
        self.key_region_id = key_region_id
        # The version ID of the Key Management Service (KMS) key.
        self.key_version_id = key_version_id
        # The name of the witness.
        self.name = name
        # The description.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_region_id is not None:
            result['KeyRegionId'] = self.key_region_id

        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id

        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyRegionId') is not None:
            self.key_region_id = m.get('KeyRegionId')

        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self


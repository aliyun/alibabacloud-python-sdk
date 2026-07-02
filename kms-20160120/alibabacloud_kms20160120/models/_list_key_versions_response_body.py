# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class ListKeyVersionsResponseBody(DaraModel):
    def __init__(
        self,
        key_versions: main_models.ListKeyVersionsResponseBodyKeyVersions = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.key_versions = key_versions
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned key versions.
        self.total_count = total_count

    def validate(self):
        if self.key_versions:
            self.key_versions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_versions is not None:
            result['KeyVersions'] = self.key_versions.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyVersions') is not None:
            temp_model = main_models.ListKeyVersionsResponseBodyKeyVersions()
            self.key_versions = temp_model.from_map(m.get('KeyVersions'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListKeyVersionsResponseBodyKeyVersions(DaraModel):
    def __init__(
        self,
        key_version: List[main_models.ListKeyVersionsResponseBodyKeyVersionsKeyVersion] = None,
    ):
        self.key_version = key_version

    def validate(self):
        if self.key_version:
            for v1 in self.key_version:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KeyVersion'] = []
        if self.key_version is not None:
            for k1 in self.key_version:
                result['KeyVersion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_version = []
        if m.get('KeyVersion') is not None:
            for k1 in m.get('KeyVersion'):
                temp_model = main_models.ListKeyVersionsResponseBodyKeyVersionsKeyVersion()
                self.key_version.append(temp_model.from_map(k1))

        return self

class ListKeyVersionsResponseBodyKeyVersionsKeyVersion(DaraModel):
    def __init__(
        self,
        creation_date: str = None,
        key_id: str = None,
        key_version_id: str = None,
    ):
        self.creation_date = creation_date
        self.key_id = key_id
        self.key_version_id = key_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')

        return self


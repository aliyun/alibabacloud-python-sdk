# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ListAlgorithmVersionsResponseBody(DaraModel):
    def __init__(
        self,
        algorithm_versions: List[main_models.ListAlgorithmVersionsResponseBodyAlgorithmVersions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.algorithm_versions = algorithm_versions
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.algorithm_versions:
            for v1 in self.algorithm_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlgorithmVersions'] = []
        if self.algorithm_versions is not None:
            for k1 in self.algorithm_versions:
                result['AlgorithmVersions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algorithm_versions = []
        if m.get('AlgorithmVersions') is not None:
            for k1 in m.get('AlgorithmVersions'):
                temp_model = main_models.ListAlgorithmVersionsResponseBodyAlgorithmVersions()
                self.algorithm_versions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAlgorithmVersionsResponseBodyAlgorithmVersions(DaraModel):
    def __init__(
        self,
        algorithm_id: str = None,
        algorithm_name: str = None,
        algorithm_provider: str = None,
        algorithm_version: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.algorithm_name = algorithm_name
        self.algorithm_provider = algorithm_provider
        self.algorithm_version = algorithm_version
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.tenant_id = tenant_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id

        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name

        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider

        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')

        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')

        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')

        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self


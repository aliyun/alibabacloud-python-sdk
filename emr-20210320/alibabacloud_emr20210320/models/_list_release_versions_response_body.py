# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListReleaseVersionsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        release_versions: List[main_models.ListReleaseVersionsResponseBodyReleaseVersions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # Returns the location of the data that was read.
        self.next_token = next_token
        # The major EMR versions.
        self.release_versions = release_versions
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.release_versions:
            for v1 in self.release_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ReleaseVersions'] = []
        if self.release_versions is not None:
            for k1 in self.release_versions:
                result['ReleaseVersions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.release_versions = []
        if m.get('ReleaseVersions') is not None:
            for k1 in m.get('ReleaseVersions'):
                temp_model = main_models.ListReleaseVersionsResponseBodyReleaseVersions()
                self.release_versions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListReleaseVersionsResponseBodyReleaseVersions(DaraModel):
    def __init__(
        self,
        iaas_type: str = None,
        release_version: str = None,
        series: str = None,
    ):
        # The IaaS type.
        self.iaas_type = iaas_type
        # The EMR version.
        self.release_version = release_version
        # The version series.
        self.series = series

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iaas_type is not None:
            result['IaasType'] = self.iaas_type

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.series is not None:
            result['Series'] = self.series

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IaasType') is not None:
            self.iaas_type = m.get('IaasType')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('Series') is not None:
            self.series = m.get('Series')

        return self


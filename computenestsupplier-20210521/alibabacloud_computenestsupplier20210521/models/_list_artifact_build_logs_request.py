# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListArtifactBuildLogsRequest(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_version: str = None,
        filter: List[main_models.ListArtifactBuildLogsRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        sort_order: str = None,
    ):
        # The artifact ID.
        # 
        # You can call the [ListArtifacts](https://help.aliyun.com/document_detail/469993.html) operation to obtain the artifact ID.
        # 
        # This parameter is required.
        self.artifact_id = artifact_id
        # The artifact version.
        # 
        # You can call the [ListArtifacts](https://help.aliyun.com/document_detail/469993.html) operation to obtain the artifact version.
        self.artifact_version = artifact_version
        # The filter.
        self.filter = filter
        # The number of entries to return on each page. Maximum value: 100. Default value: 20.
        self.max_results = max_results
        # The token to start the next paged query.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The sort order. Valid values:
        # 
        # - **Ascending**: sorts the results in ascending order.
        # 
        # - **Descending** (default): sorts the results in descending order.
        self.sort_order = sort_order

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version

        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')

        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.ListArtifactBuildLogsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

class ListArtifactBuildLogsRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The name of the filter.
        # 
        # Valid values:
        # 
        # - StartTime
        # 
        # - EndTime
        # 
        # - ApplicationGroupName
        # 
        # - ResouceName
        # 
        # - EventName
        self.name = name
        # The filter values.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


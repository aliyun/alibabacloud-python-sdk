# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListFeatureViewsRequest(DaraModel):
    def __init__(
        self,
        feature_name: str = None,
        feature_view_ids: List[str] = None,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_by: str = None,
        tag: str = None,
        type: str = None,
    ):
        # Filters the results by feature name.
        self.feature_name = feature_name
        # The feature view IDs by which to filter the results.
        self.feature_view_ids = feature_view_ids
        # Filters the results by feature view name.
        self.name = name
        # The sort order. Valid values: `Desc` (descending) and `Asc` (ascending).
        self.order = order
        # Filters the results by owner.
        self.owner = owner
        # The page number of the results to return.
        self.page_number = page_number
        # The number of feature views to return on each page.
        self.page_size = page_size
        # The project ID. You can obtain this ID by calling the `ListProjects` operation.
        self.project_id = project_id
        # The field by which to sort the results.
        self.sort_by = sort_by
        # Filters the results by tag.
        self.tag = tag
        # Filters the results by type. Valid values:
        # 
        # ● `Batch`: batch feature
        # 
        # ● `Stream`: stream feature
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.feature_view_ids is not None:
            result['FeatureViewIds'] = self.feature_view_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('FeatureViewIds') is not None:
            self.feature_view_ids = m.get('FeatureViewIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


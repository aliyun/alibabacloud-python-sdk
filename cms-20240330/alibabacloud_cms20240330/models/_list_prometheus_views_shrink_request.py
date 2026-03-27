# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPrometheusViewsShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_region_ids: str = None,
        max_results: int = None,
        next_token: str = None,
        prometheus_view_ids: str = None,
        prometheus_view_name: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        tag_shrink: str = None,
        version: str = None,
        workspace: str = None,
    ):
        # Filter by RegionID.
        self.filter_region_ids = filter_region_ids
        # Maximum number of records to return.
        self.max_results = max_results
        # Query token.
        self.next_token = next_token
        # List of Prometheus view instance IDs.
        self.prometheus_view_ids = prometheus_view_ids
        # Prometheus view name.
        self.prometheus_view_name = prometheus_view_name
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Resource type.
        self.resource_type = resource_type
        # List of tags.
        self.tag_shrink = tag_shrink
        # Instance version: V1 or V2
        self.version = version
        # Workspace name
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_region_ids is not None:
            result['filterRegionIds'] = self.filter_region_ids

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.prometheus_view_ids is not None:
            result['prometheusViewIds'] = self.prometheus_view_ids

        if self.prometheus_view_name is not None:
            result['prometheusViewName'] = self.prometheus_view_name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink

        if self.version is not None:
            result['version'] = self.version

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterRegionIds') is not None:
            self.filter_region_ids = m.get('filterRegionIds')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('prometheusViewIds') is not None:
            self.prometheus_view_ids = m.get('prometheusViewIds')

        if m.get('prometheusViewName') is not None:
            self.prometheus_view_name = m.get('prometheusViewName')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self


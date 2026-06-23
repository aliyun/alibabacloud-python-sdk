# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PurgeCachesShrinkRequest(DaraModel):
    def __init__(
        self,
        content_shrink: str = None,
        edge_compute_purge: bool = None,
        force: bool = None,
        site_id: int = None,
        type: str = None,
    ):
        # The refresh content.
        self.content_shrink = content_shrink
        # Specifies whether to refresh edge computing cached resources. For example, this allows you to refresh content cached by the Edge Routine CacheAPI API operation using the edge function.
        self.edge_compute_purge = edge_compute_purge
        # Specifies whether to refresh all resources under the corresponding directory when the back-to-origin content is inconsistent with the origin server resources. Default value: false.
        # - **true**: Refreshes all resources under the corresponding directory.
        # - **false**: Refreshes only the changed resources under the corresponding directory.
        # 
        # > 
        # >  This parameter takes effect for directory refresh, cache tag refresh, parameter-ignored refresh, hostname refresh, and full site refresh.
        self.force = force
        # The site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The type of the refresh node. Valid values:
        # - **file** (default): file refresh.
        # - **cachekey**: cache key refresh.
        # - **cachetag**: cache label refresh.
        # - **directory**: folder refresh.
        # - **ignoreParams**: parameter-ignored refresh. This refers to removing the question mark (?) and all parameters after it from the request URL. When you commit a parameter-stripped URL through this API operation, the committed URL is matched against cached resource URLs after their parameters are also stripped. If a cached resource URL matches the committed URL after parameter stripping, the point of presence executes the refresh on the cached resource.
        # - **hostname**: hostname refresh.
        # - **purgeall**: refreshes all cached content under the site.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.edge_compute_purge is not None:
            result['EdgeComputePurge'] = self.edge_compute_purge

        if self.force is not None:
            result['Force'] = self.force

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('EdgeComputePurge') is not None:
            self.edge_compute_purge = m.get('EdgeComputePurge')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchDeployHttpApiRoutesRequest(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        deploy_all: bool = None,
        route_ids: List[str] = None,
    ):
        # Specifies whether to publish routes asynchronously. Default value: true. If set to true, the acceptance results of the routes are returned. If set to false, the system waits for the batch processing to complete and returns the final results and statistics for each route.
        self.async_ = async_
        # Specifies whether to publish all routes visible to the current user under the API. Default value: false. If you set this parameter to true, all visible routes are published and the routeIds parameter is ignored.
        self.deploy_all = deploy_all
        # The list of route IDs to publish. If deployAll is omitted or set to false, at least one route ID must be provided. If any route does not exist or belongs to another API, the entire batch request is rejected.
        self.route_ids = route_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['async'] = self.async_

        if self.deploy_all is not None:
            result['deployAll'] = self.deploy_all

        if self.route_ids is not None:
            result['routeIds'] = self.route_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async') is not None:
            self.async_ = m.get('async')

        if m.get('deployAll') is not None:
            self.deploy_all = m.get('deployAll')

        if m.get('routeIds') is not None:
            self.route_ids = m.get('routeIds')

        return self


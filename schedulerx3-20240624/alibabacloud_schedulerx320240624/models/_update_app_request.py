# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppRequest(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        app_name: str = None,
        cluster_id: str = None,
        enable_log: bool = None,
        label_route_strategy: int = None,
        max_concurrency: int = None,
        title: str = None,
        worker_id: int = None,
    ):
        # The access token.
        self.access_token = access_token
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to enable logging.
        # 
        # - `true`: Enables logging.
        # 
        # - `false`: Disables logging.
        self.enable_log = enable_log
        self.label_route_strategy = label_route_strategy
        # The task execution queue size.
        # 
        # > Sets the maximum number of concurrent task instances in the application group. Additional task instances are queued for execution and not discarded.
        self.max_concurrency = max_concurrency
        # The title.
        # 
        # This parameter is required.
        self.title = title
        self.worker_id = worker_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log

        if self.label_route_strategy is not None:
            result['LabelRouteStrategy'] = self.label_route_strategy

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.title is not None:
            result['Title'] = self.title

        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')

        if m.get('LabelRouteStrategy') is not None:
            self.label_route_strategy = m.get('LabelRouteStrategy')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')

        return self


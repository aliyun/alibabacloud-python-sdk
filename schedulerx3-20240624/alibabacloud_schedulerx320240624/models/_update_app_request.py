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
    ):
        self.access_token = access_token
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.enable_log = enable_log
        self.label_route_strategy = label_route_strategy
        self.max_concurrency = max_concurrency
        # This parameter is required.
        self.title = title

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

        return self


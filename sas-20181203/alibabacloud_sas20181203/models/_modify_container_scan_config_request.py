# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyContainerScanConfigRequest(DaraModel):
    def __init__(
        self,
        app_names: str = None,
        cluster_id: str = None,
        lang: str = None,
    ):
        # The name of the container application.
        self.app_names = app_names
        # The cluster ID.
        # 
        # >  You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of clusters.
        self.cluster_id = cluster_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_names is not None:
            result['AppNames'] = self.app_names

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppNames') is not None:
            self.app_names = m.get('AppNames')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self


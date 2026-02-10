# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeClusterScannerListRequest(DaraModel):
    def __init__(
        self,
        cluster_id_list: List[str] = None,
        lang: str = None,
        status_list: List[str] = None,
    ):
        # List of cluster IDs.
        self.cluster_id_list = cluster_id_list
        # The language type for requests and responses.
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # List of scanner statuses. Values:
        # - **online**: Running
        # - **offline**: Offline
        # - **not_installed**: Not Installed
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id_list is not None:
            result['ClusterIdList'] = self.cluster_id_list

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIdList') is not None:
            self.cluster_id_list = m.get('ClusterIdList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        return self


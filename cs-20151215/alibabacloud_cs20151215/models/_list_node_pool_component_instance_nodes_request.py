# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListNodePoolComponentInstanceNodesRequest(DaraModel):
    def __init__(
        self,
        config_revision: str = None,
        max_results: int = None,
        next_token: str = None,
        node_names: List[str] = None,
        version: str = None,
    ):
        self.config_revision = config_revision
        self.max_results = max_results
        self.next_token = next_token
        self.node_names = node_names
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_revision is not None:
            result['config_revision'] = self.config_revision

        if self.max_results is not None:
            result['max_results'] = self.max_results

        if self.next_token is not None:
            result['next_token'] = self.next_token

        if self.node_names is not None:
            result['node_names'] = self.node_names

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config_revision') is not None:
            self.config_revision = m.get('config_revision')

        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')

        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

        if m.get('node_names') is not None:
            self.node_names = m.get('node_names')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self


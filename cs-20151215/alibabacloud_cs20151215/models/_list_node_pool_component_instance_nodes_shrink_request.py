# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodePoolComponentInstanceNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        config_revision: str = None,
        max_results: int = None,
        next_token: str = None,
        node_names_shrink: str = None,
        version: str = None,
    ):
        # Filters nodes by the specified configuration version number of the node component.
        self.config_revision = config_revision
        # The maximum number of records to return in a single response for pagination. Default value: 20.
        self.max_results = max_results
        # The pagination cursor. Do not specify this parameter for the first request. For subsequent requests, specify the token returned in the previous response.
        self.next_token = next_token
        # Specifies the list of node names to query.
        self.node_names_shrink = node_names_shrink
        # Filters nodes by the specified node component version.
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

        if self.node_names_shrink is not None:
            result['node_names'] = self.node_names_shrink

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
            self.node_names_shrink = m.get('node_names')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self


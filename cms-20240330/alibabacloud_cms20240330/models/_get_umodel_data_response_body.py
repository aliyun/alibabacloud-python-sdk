# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetUmodelDataResponseBody(DaraModel):
    def __init__(
        self,
        errors: List[main_models.GetUmodelDataResponseBodyErrors] = None,
        links: List[Any] = None,
        nodes: List[Any] = None,
        request_id: str = None,
        total_links_count: int = None,
        total_nodes_count: int = None,
    ):
        # Error information
        self.errors = errors
        # List of node link relationships
        self.links = links
        # List of nodes
        self.nodes = nodes
        # Request ID
        self.request_id = request_id
        # Total number of node links
        self.total_links_count = total_links_count
        # Total number of nodes
        self.total_nodes_count = total_nodes_count

    def validate(self):
        if self.errors:
            for v1 in self.errors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['errors'] = []
        if self.errors is not None:
            for k1 in self.errors:
                result['errors'].append(k1.to_map() if k1 else None)

        if self.links is not None:
            result['links'] = self.links

        if self.nodes is not None:
            result['nodes'] = self.nodes

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_links_count is not None:
            result['totalLinksCount'] = self.total_links_count

        if self.total_nodes_count is not None:
            result['totalNodesCount'] = self.total_nodes_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.errors = []
        if m.get('errors') is not None:
            for k1 in m.get('errors'):
                temp_model = main_models.GetUmodelDataResponseBodyErrors()
                self.errors.append(temp_model.from_map(k1))

        if m.get('links') is not None:
            self.links = m.get('links')

        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalLinksCount') is not None:
            self.total_links_count = m.get('totalLinksCount')

        if m.get('totalNodesCount') is not None:
            self.total_nodes_count = m.get('totalNodesCount')

        return self

class GetUmodelDataResponseBodyErrors(DaraModel):
    def __init__(
        self,
        message: str = None,
        type: str = None,
    ):
        # Details.
        self.message = message
        # Error type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self


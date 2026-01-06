# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeContainerClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        identifier: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The identifier of the container cluster. For a Container Service for Kubernetes (ACK) cluster, specify the cluster ID.
        self.identifier = identifier
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


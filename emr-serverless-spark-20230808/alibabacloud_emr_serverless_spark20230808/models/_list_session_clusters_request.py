# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSessionClustersRequest(DaraModel):
    def __init__(
        self,
        kind: str = None,
        max_results: int = None,
        next_token: str = None,
        queue_name: str = None,
        region_id: str = None,
        session_cluster_id: str = None,
    ):
        # The session type.
        # 
        # Valid values:
        # 
        # *   NOTEBOOK
        # *   THRIFT
        # *   SQL
        self.kind = kind
        # The maximum number of entries to return.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results.
        self.next_token = next_token
        # The name of the queue.
        self.queue_name = queue_name
        # The region ID.
        self.region_id = region_id
        # The name of the job.
        self.session_cluster_id = session_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kind is not None:
            result['kind'] = self.kind

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListStackConfigsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
        version: str = None,
    ):
        # The maximum number of records to return for the current query. Default value: 20. Maximum value: 200.
        self.max_results = max_results
        # The token that specifies the starting position for the query. If this parameter is left empty, the query starts from the beginning.
        self.next_token = next_token
        # The status of the stack configuration. Valid values:
        # | Name | Description |
        # |------|-------------|
        # | Creating | Creating |
        # | Created | Created |
        # | Waiting | Waiting for deployment |
        # | Deploying | Deploying |
        # | Deployed | Deployed |
        # | Errored | Deployment failed |
        # | Deleting | Deleting |
        # | Deleted | Deleted |
        # | DeleteFailed | Deletion failed |
        # | DetectTriggered | Drift detection triggered successfully |
        self.status = status
        # The version number of the stack configuration, such as v1. The initial value is v1. The version number increments each time the stack is updated or refreshed and the configuration is changed.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.status is not None:
            result['status'] = self.status

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self


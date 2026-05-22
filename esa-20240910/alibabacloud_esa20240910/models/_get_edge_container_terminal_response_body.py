# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEdgeContainerTerminalResponseBody(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        container: str = None,
        namespace: str = None,
        pod: str = None,
        request_id: str = None,
        session_id: str = None,
        token: str = None,
    ):
        # The cluster name.
        self.cluster = cluster
        # The container name.
        self.container = container
        # The name of the namespace.
        self.namespace = namespace
        # The name of the container group.
        self.pod = pod
        # The request ID.
        self.request_id = request_id
        # The session ID.
        self.session_id = session_id
        # The information about the shared token.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['Cluster'] = self.cluster

        if self.container is not None:
            result['Container'] = self.container

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')

        if m.get('Container') is not None:
            self.container = m.get('Container')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self


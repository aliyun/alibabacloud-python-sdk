# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExecutorGroupRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        auth_type: str = None,
        cluster_id: str = None,
        description: str = None,
        name: str = None,
        network: str = None,
        protocol: str = None,
        worker_type: str = None,
        workers: str = None,
    ):
        self.api_key = api_key
        self.auth_type = auth_type
        # This parameter is required.
        self.cluster_id = cluster_id
        self.description = description
        # This parameter is required.
        self.name = name
        self.network = network
        self.protocol = protocol
        # This parameter is required.
        self.worker_type = worker_type
        # This parameter is required.
        self.workers = workers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.network is not None:
            result['Network'] = self.network

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.worker_type is not None:
            result['WorkerType'] = self.worker_type

        if self.workers is not None:
            result['Workers'] = self.workers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('WorkerType') is not None:
            self.worker_type = m.get('WorkerType')

        if m.get('Workers') is not None:
            self.workers = m.get('Workers')

        return self


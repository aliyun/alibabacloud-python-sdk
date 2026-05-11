# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
        description: str = None,
        name: str = None,
        nlu_service_params_json: str = None,
        union_instance_id: str = None,
        union_source: str = None,
    ):
        # This parameter is required.
        self.concurrency = concurrency
        self.description = description
        # This parameter is required.
        self.name = name
        self.nlu_service_params_json = nlu_service_params_json
        self.union_instance_id = union_instance_id
        self.union_source = union_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.nlu_service_params_json is not None:
            result['NluServiceParamsJson'] = self.nlu_service_params_json

        if self.union_instance_id is not None:
            result['UnionInstanceId'] = self.union_instance_id

        if self.union_source is not None:
            result['UnionSource'] = self.union_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NluServiceParamsJson') is not None:
            self.nlu_service_params_json = m.get('NluServiceParamsJson')

        if m.get('UnionInstanceId') is not None:
            self.union_instance_id = m.get('UnionInstanceId')

        if m.get('UnionSource') is not None:
            self.union_source = m.get('UnionSource')

        return self


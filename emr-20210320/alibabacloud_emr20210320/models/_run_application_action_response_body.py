# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class RunApplicationActionResponseBody(DaraModel):
    def __init__(
        self,
        abn_instances: List[main_models.RunApplicationActionResponseBodyAbnInstances] = None,
        operation_id: str = None,
        request_id: str = None,
    ):
        # The abnormal nodes.
        self.abn_instances = abn_instances
        # The operation ID.
        self.operation_id = operation_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.abn_instances:
            for v1 in self.abn_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AbnInstances'] = []
        if self.abn_instances is not None:
            for k1 in self.abn_instances:
                result['AbnInstances'].append(k1.to_map() if k1 else None)

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abn_instances = []
        if m.get('AbnInstances') is not None:
            for k1 in m.get('AbnInstances'):
                temp_model = main_models.RunApplicationActionResponseBodyAbnInstances()
                self.abn_instances.append(temp_model.from_map(k1))

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RunApplicationActionResponseBodyAbnInstances(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        node_name: str = None,
    ):
        # The ID of the abnormal node.
        self.node_id = node_id
        # The name of the abnormal node.
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self


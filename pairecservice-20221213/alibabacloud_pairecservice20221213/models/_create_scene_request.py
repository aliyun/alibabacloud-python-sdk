# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class CreateSceneRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        flows: List[main_models.CreateSceneRequestFlows] = None,
        instance_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.flows = flows
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        if self.flows:
            for v1 in self.flows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['Flows'] = []
        if self.flows is not None:
            for k1 in self.flows:
                result['Flows'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.flows = []
        if m.get('Flows') is not None:
            for k1 in m.get('Flows'):
                temp_model = main_models.CreateSceneRequestFlows()
                self.flows.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreateSceneRequestFlows(DaraModel):
    def __init__(
        self,
        flow_code: str = None,
        flow_name: str = None,
    ):
        self.flow_code = flow_code
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListRenderingProjectInstancesResponseBody(DaraModel):
    def __init__(
        self,
        rendering_instances: List[main_models.ListRenderingProjectInstancesResponseBodyRenderingInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.rendering_instances = rendering_instances
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.rendering_instances:
            for v1 in self.rendering_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RenderingInstances'] = []
        if self.rendering_instances is not None:
            for k1 in self.rendering_instances:
                result['RenderingInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rendering_instances = []
        if m.get('RenderingInstances') is not None:
            for k1 in m.get('RenderingInstances'):
                temp_model = main_models.ListRenderingProjectInstancesResponseBodyRenderingInstances()
                self.rendering_instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRenderingProjectInstancesResponseBodyRenderingInstances(DaraModel):
    def __init__(
        self,
        association_time: str = None,
        rendering_instance_id: str = None,
        state_info: main_models.ListRenderingProjectInstancesResponseBodyRenderingInstancesStateInfo = None,
    ):
        self.association_time = association_time
        self.rendering_instance_id = rendering_instance_id
        self.state_info = state_info

    def validate(self):
        if self.state_info:
            self.state_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_time is not None:
            result['AssociationTime'] = self.association_time

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.state_info is not None:
            result['StateInfo'] = self.state_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationTime') is not None:
            self.association_time = m.get('AssociationTime')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('StateInfo') is not None:
            temp_model = main_models.ListRenderingProjectInstancesResponseBodyRenderingInstancesStateInfo()
            self.state_info = temp_model.from_map(m.get('StateInfo'))

        return self

class ListRenderingProjectInstancesResponseBodyRenderingInstancesStateInfo(DaraModel):
    def __init__(
        self,
        comment: str = None,
        state: str = None,
        update_time: str = None,
    ):
        self.comment = comment
        self.state = state
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.state is not None:
            result['State'] = self.state

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self


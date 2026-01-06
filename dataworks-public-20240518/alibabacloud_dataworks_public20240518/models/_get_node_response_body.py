# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetNodeResponseBody(DaraModel):
    def __init__(
        self,
        node: main_models.GetNodeResponseBodyNode = None,
        request_id: str = None,
    ):
        # Data Studio node details.
        self.node = node
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node is not None:
            result['Node'] = self.node.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Node') is not None:
            temp_model = main_models.GetNodeResponseBodyNode()
            self.node = temp_model.from_map(m.get('Node'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNodeResponseBodyNode(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        spec: str = None,
        task_id: int = None,
    ):
        # The time when the node was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The unique identifier of the Data Studio node.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The time when the node was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the node.
        self.name = name
        # The owner of the node.
        self.owner = owner
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The FlowSpec field information about this node. For more information, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow).
        self.spec = spec
        # The ID of the corresponding scheduling task after the node is published.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self


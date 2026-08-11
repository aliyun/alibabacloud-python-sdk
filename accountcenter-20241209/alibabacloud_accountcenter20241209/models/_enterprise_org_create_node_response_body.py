# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseOrgCreateNodeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.EnterpriseOrgCreateNodeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.EnterpriseOrgCreateNodeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EnterpriseOrgCreateNodeResponseBodyData(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        id: int = None,
        node_id: str = None,
        node_name: str = None,
        node_type: str = None,
        parent_node_id: str = None,
        parent_node_type: str = None,
        tree_id: int = None,
    ):
        self.gmt_create = gmt_create
        self.id = id
        self.node_id = node_id
        self.node_name = node_name
        self.node_type = node_type
        self.parent_node_id = parent_node_id
        self.parent_node_type = parent_node_type
        self.tree_id = tree_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id

        if self.parent_node_type is not None:
            result['ParentNodeType'] = self.parent_node_type

        if self.tree_id is not None:
            result['TreeId'] = self.tree_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')

        if m.get('ParentNodeType') is not None:
            self.parent_node_type = m.get('ParentNodeType')

        if m.get('TreeId') is not None:
            self.tree_id = m.get('TreeId')

        return self


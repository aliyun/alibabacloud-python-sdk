# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateNodeOpsOwnerRequest(DaraModel):
    def __init__(
        self,
        command: main_models.UpdateNodeOpsOwnerRequestCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The command for updating O&M owners.
        # 
        # This parameter is required.
        self.command = command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id

    def validate(self):
        if self.command:
            self.command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            temp_model = main_models.UpdateNodeOpsOwnerRequestCommand()
            self.command = temp_model.from_map(m.get('Command'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class UpdateNodeOpsOwnerRequestCommand(DaraModel):
    def __init__(
        self,
        node_id_list: List[main_models.UpdateNodeOpsOwnerRequestCommandNodeIdList] = None,
        ops_owner_list: List[str] = None,
    ):
        # The list of nodes. Only offline nodes are supported.
        # 
        # This parameter is required.
        self.node_id_list = node_id_list
        # The updated O&M owners. Specify a list of user account IDs. A maximum of 50 IDs are supported.
        # 
        # This parameter is required.
        self.ops_owner_list = ops_owner_list

    def validate(self):
        if self.node_id_list:
            for v1 in self.node_id_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeIdList'] = []
        if self.node_id_list is not None:
            for k1 in self.node_id_list:
                result['NodeIdList'].append(k1.to_map() if k1 else None)

        if self.ops_owner_list is not None:
            result['OpsOwnerList'] = self.ops_owner_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_id_list = []
        if m.get('NodeIdList') is not None:
            for k1 in m.get('NodeIdList'):
                temp_model = main_models.UpdateNodeOpsOwnerRequestCommandNodeIdList()
                self.node_id_list.append(temp_model.from_map(k1))

        if m.get('OpsOwnerList') is not None:
            self.ops_owner_list = m.get('OpsOwnerList')

        return self

class UpdateNodeOpsOwnerRequestCommandNodeIdList(DaraModel):
    def __init__(
        self,
        id: str = None,
        node_from_type: str = None,
        node_type: str = None,
    ):
        # The node ID.
        # 
        # This parameter is required.
        self.id = id
        # The node source type. Only offline nodes are supported. Valid values:
        # - DATA_PROCESS: compute node.
        # - PIPELINE: integration node.
        # - BLACK_BOX: logical table.
        # 
        # This parameter is required.
        self.node_from_type = node_from_type
        # The node type. Valid values:
        # - DATA_PROCESS: compute node.
        # - PIPELINE_NODE: integration node.
        # - BBOX_LOGIC_TABLE_NODE: logical table.
        # 
        # This parameter is required.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.node_from_type is not None:
            result['NodeFromType'] = self.node_from_type

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NodeFromType') is not None:
            self.node_from_type = m.get('NodeFromType')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self


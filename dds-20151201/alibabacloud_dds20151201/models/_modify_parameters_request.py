# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyParametersRequest(DaraModel):
    def __init__(
        self,
        character_type: str = None,
        dbinstance_id: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameters: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_mode: str = None,
    ):
        # The role of the instance. Valid values:
        # 
        # *   **db**: a shard node.
        # *   **cs**: a Configserver node.
        # *   **mongos**: a mongos node.
        self.character_type = character_type
        # The instance ID.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the mongos or shard node in the specified sharded cluster instance.
        # 
        # >  This parameter is valid only when DBInstanceId is set to the ID of a sharded cluster instance.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The instance parameters that you want to modify and their values. Specify this parameter in a JSON string. Sample format: {"ParameterName1":"ParameterValue1","ParameterName2":"ParameterValue2"}.
        # 
        # >  You can call the [DescribeParameterTemplates](https://help.aliyun.com/document_detail/67618.html) operation to query a list of default parameter templates.
        # 
        # This parameter is required.
        self.parameters = parameters
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.switch_mode = switch_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.character_type is not None:
            result['CharacterType'] = self.character_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self


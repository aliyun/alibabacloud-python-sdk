# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyParameterGroupRequest(DaraModel):
    def __init__(
        self,
        modify_mode: str = None,
        owner_id: int = None,
        parameter_group_desc: str = None,
        parameter_group_id: str = None,
        parameter_group_name: str = None,
        parameters: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The modification mode of the parameter template. Valid values:
        # 
        # *   **Collectivity** (default): adds new parameters or modifies parameters in the original parameter template.
        # 
        # >  If you set the ModifyMode parameter to Collectivity, the system adds the value of the **Parameters** parameter to the original parameter template or modifies the corresponding parameters in the original parameter template. Other parameters in the original parameter template are not affected.
        # 
        # *   **Individual**: overwrites original parameters.
        # 
        # >  If you set the ModifyMode parameter to Individual, the system uses the value of the **Parameters** parameter to overwrite the parameter settings in the original parameter template.
        self.modify_mode = modify_mode
        self.owner_id = owner_id
        # The new description of the parameter template. The description can be up to 200 characters in length.
        # 
        # > If you do not specify this parameter, the original description of the parameter template is retained.
        self.parameter_group_desc = parameter_group_desc
        # The parameter template ID. You can call the DescribeParameterGroups operation to query the parameter template ID.
        # 
        # This parameter is required.
        self.parameter_group_id = parameter_group_id
        # The parameter template name.
        # 
        # *   The name can contain letters, digits, periods (.), and underscores (_). It must start with a letter.
        # *   It can be 8 to 64 characters in length.
        # 
        # > If you do not specify this parameter, the original name of the parameter template is retained.
        self.parameter_group_name = parameter_group_name
        # A JSON string that consists of parameters and their values in the parameter template. Format: {"Parameter 1":"Value of Parameter 1","Parameter 2":"Value of Parameter 2"...}. For more information about the parameters that can be modified, see [Modify the parameters of an ApsaraDB RDS for MySQL instance](https://help.aliyun.com/document_detail/96063.html) or [Modify the parameters of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/96751.html).
        # 
        # > *   If **ModifyMode** is set to **Individual** and this parameter is specified, the new parameters overwrite the parameters in the original parameter template.
        # > *   If you set **ModifyMode** to **Collectivity** and specify this parameter, the new parameters are added to the original parameter template, or the parameters in the original parameter template are modified.
        # > *   If you do not specify this parameter, the parameters in the original parameter template remain unchanged.
        self.parameters = parameters
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # >  The region of a parameter template cannot be changed. You can call the CloneParameterGroup operation to replicate a parameter template to a specific region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. You can call the DescribeDBInstanceAttribute operation to query the resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self


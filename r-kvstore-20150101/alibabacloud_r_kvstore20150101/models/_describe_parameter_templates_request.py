# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeParameterTemplatesRequest(DaraModel):
    def __init__(
        self,
        character_type: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameter_category: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The architecture of the instance. For more information, see [Architecture overview](https://help.aliyun.com/document_detail/86132.html). Valid values:
        # 
        # * **logic**: cluster or read/write splitting architecture.
        # * **normal**: standard architecture (primary/secondary).
        # 
        # <props="china">If **EngineVersion** is set to **6.0**, this parameter does not support the value **logic**.
        # 
        # This parameter is required.
        self.character_type = character_type
        # The database type. Set the value to **Redis**.
        # 
        # This parameter is required.
        self.engine = engine
        # The major version of the instance. Valid values: **4.0**, **5.0**, **6.0**, and **7.0**.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The instance ID. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) operation to obtain the instance ID.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The parameter category.
        self.parameter_category = parameter_category
        # The resource group ID. You can invoke the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to obtain the resource group ID.
        # > You can also obtain the resource group ID in the console. For more information, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.character_type is not None:
            result['CharacterType'] = self.character_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameter_category is not None:
            result['ParameterCategory'] = self.parameter_category

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParameterCategory') is not None:
            self.parameter_category = m.get('ParameterCategory')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self


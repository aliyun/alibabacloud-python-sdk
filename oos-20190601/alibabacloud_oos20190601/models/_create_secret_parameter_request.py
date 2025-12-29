# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateSecretParameterRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        constraints: str = None,
        dkmsinstance_id: str = None,
        description: str = None,
        key_id: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        value: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (_). For more information, see "How to ensure idempotence".
        self.client_token = client_token
        # The constraints of the encryption parameter. By default, this parameter is null. Valid values:
        # 
        # *   AllowedValues: The value that is allowed for the encryption parameter. It must be an array string.
        # *   AllowedPattern: The pattern that is allowed for the encryption parameter. It must be a regular expression.
        # *   MinLength: The minimum length of the encryption parameter.
        # *   MaxLength: The maximum length of the encryption parameter.
        self.constraints = constraints
        # The instance ID of the KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The description of the encryption parameter. The description must be 1 to 200 characters in length.
        self.description = description
        # The key ID of Key Management Service (KMS) that is used to encrypt the parameter.
        self.key_id = key_id
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The type of the parameter. Set the value to Secret.
        self.type = type
        # The value of the encryption parameter. The value must be 1 to 4096 characters in length.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.constraints is not None:
            result['Constraints'] = self.constraints

        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')

        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


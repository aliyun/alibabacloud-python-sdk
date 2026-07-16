# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class CreateTagsRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        tag_key_value_param_list: List[main_models.CreateTagsRequestTagKeyValueParamList] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # > Only `cn-hangzhou` is supported.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The information about the tags.
        # 
        # This parameter is required.
        self.tag_key_value_param_list = tag_key_value_param_list

    def validate(self):
        if self.tag_key_value_param_list:
            for v1 in self.tag_key_value_param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        result['TagKeyValueParamList'] = []
        if self.tag_key_value_param_list is not None:
            for k1 in self.tag_key_value_param_list:
                result['TagKeyValueParamList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        self.tag_key_value_param_list = []
        if m.get('TagKeyValueParamList') is not None:
            for k1 in m.get('TagKeyValueParamList'):
                temp_model = main_models.CreateTagsRequestTagKeyValueParamList()
                self.tag_key_value_param_list.append(temp_model.from_map(k1))

        return self

class CreateTagsRequestTagKeyValueParamList(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        tag_value_param_list: List[main_models.CreateTagsRequestTagKeyValueParamListTagValueParamList] = None,
    ):
        # The description of the key for tag N.
        # 
        # Valid values of N: 1 to 10.
        self.description = description
        # The value of tag N.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        # 
        # Valid values of N: 1 to 10.
        # 
        # This parameter is required.
        self.key = key
        # The information about the tag values.
        self.tag_value_param_list = tag_value_param_list

    def validate(self):
        if self.tag_value_param_list:
            for v1 in self.tag_value_param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        result['TagValueParamList'] = []
        if self.tag_value_param_list is not None:
            for k1 in self.tag_value_param_list:
                result['TagValueParamList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        self.tag_value_param_list = []
        if m.get('TagValueParamList') is not None:
            for k1 in m.get('TagValueParamList'):
                temp_model = main_models.CreateTagsRequestTagKeyValueParamListTagValueParamList()
                self.tag_value_param_list.append(temp_model.from_map(k1))

        return self

class CreateTagsRequestTagKeyValueParamListTagValueParamList(DaraModel):
    def __init__(
        self,
        description: str = None,
        value: str = None,
    ):
        # The description of the value for tag N.
        # 
        # Valid values of N: 1 to 10.
        self.description = description
        # The value of tag N.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
        # 
        # Valid values of N: 1 to 10.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


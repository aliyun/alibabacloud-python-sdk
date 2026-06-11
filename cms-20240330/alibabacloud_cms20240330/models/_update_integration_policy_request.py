# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class UpdateIntegrationPolicyRequest(DaraModel):
    def __init__(
        self,
        fee_package: str = None,
        policy_name: str = None,
        resource_group_id: str = None,
        tags: List[main_models.UpdateIntegrationPolicyRequestTags] = None,
    ):
        # The type of the paid plan. Valid values: CS_Pro, CS_Basic, and empty.
        self.fee_package = fee_package
        # The name of the rule. The name must be 3 to 63 characters in length and start with a letter.
        self.policy_name = policy_name
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags of the resource.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee_package is not None:
            result['feePackage'] = self.fee_package

        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('feePackage') is not None:
            self.fee_package = m.get('feePackage')

        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.UpdateIntegrationPolicyRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class UpdateIntegrationPolicyRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self


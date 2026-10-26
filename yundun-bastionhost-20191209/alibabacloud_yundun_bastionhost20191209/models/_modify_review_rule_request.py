# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyReviewRuleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        region_id: str = None,
        review_rule_id: int = None,
        scope_type: int = None,
    ):
        # The new description of the audit policy. The description can be up to 500 characters in length.
        self.description = description
        # The instance ID of the Bastionhost instance.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new name of the audit policy. The name must be 1 to 128 characters in length. It cannot start with a special character and can contain only the following special characters: periods (.), underscores (_), hyphens (-), backslashes (\\), and spaces.
        self.name = name
        # The region ID of the Bastionhost instance. 
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the audit policy.
        # > You can invoke the ListReviewRules operation to obtain this parameter.
        # 
        # This parameter is required.
        self.review_rule_id = review_rule_id
        # The type of the asset scope rule for auditable assets. Valid values:
        # 
        # - **1**: All projects.
        # 
        # - **2**: Specified projects.
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.review_rule_id is not None:
            result['ReviewRuleId'] = self.review_rule_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReviewRuleId') is not None:
            self.review_rule_id = m.get('ReviewRuleId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self


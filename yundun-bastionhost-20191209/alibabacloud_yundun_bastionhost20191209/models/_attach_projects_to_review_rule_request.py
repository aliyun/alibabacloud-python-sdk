# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachProjectsToReviewRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        project_ids: str = None,
        region_id: str = None,
        review_rule_id: int = None,
    ):
        # The instance ID of the Bastionhost instance.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IDs of the projects to associate.
        # > You can call the ListProjects operation to obtain this parameter.
        # 
        # This parameter is required.
        self.project_ids = project_ids
        # The region ID of the Bastionhost instance.
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the audit policy.
        # > You can invoke the ListReviewRules operation to obtain this parameter.
        # 
        # This parameter is required.
        self.review_rule_id = review_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.review_rule_id is not None:
            result['ReviewRuleId'] = self.review_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReviewRuleId') is not None:
            self.review_rule_id = m.get('ReviewRuleId')

        return self


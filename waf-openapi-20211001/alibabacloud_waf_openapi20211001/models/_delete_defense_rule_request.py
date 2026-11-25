# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDefenseRuleRequest(DaraModel):
    def __init__(
        self,
        defense_type: str = None,
        dry_run: bool = None,
        instance_id: str = None,
        region_id: str = None,
        resource: str = None,
        resource_manager_resource_group_id: str = None,
        resource_type: str = None,
        rule_ids: str = None,
        template_id: int = None,
    ):
        # The type of the protection rule.
        self.defense_type = defense_type
        # Specifies whether to enable the dry run mode. If you do not specify this parameter, a normal request is initiated. Valid values:
        # - **true**: initiates a dry run request. The system only checks whether the request meets the execution conditions and does not perform the operations specified in the request. If the dry run fails, the system returns the corresponding error code. If the dry run succeeds, the system returns the Defense.Control.DryRunOperation error code.
        # - **false**: initiates a normal request. If the check succeeds, the system performs the operations specified in the request.
        self.dry_run = dry_run
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The protected object to which the rules to be deleted apply.
        # > This parameter is required only when **DefenseType** is set to **resource**.
        self.resource = resource
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The type of the protection target. This parameter applies to rules whose **DefenseType** is **resource**. Valid values:
        # 
        # - **single** (default): a single protected object.
        # - **group**: a protection group.
        self.resource_type = resource_type
        # The IDs of the protection rules to be deleted. Separate multiple rule IDs with commas (,).
        # 
        # This parameter is required.
        self.rule_ids = rule_ids
        # The ID of the protection template to be deleted.
        # > This parameter is required only when **DefenseType** is set to **template**.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self


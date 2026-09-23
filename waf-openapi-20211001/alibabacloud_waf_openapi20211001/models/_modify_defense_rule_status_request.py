# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDefenseRuleStatusRequest(DaraModel):
    def __init__(
        self,
        defense_type: str = None,
        dry_run: bool = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        rule_id: int = None,
        rule_status: int = None,
        template_id: int = None,
    ):
        # The type of the protection rule.
        self.defense_type = defense_type
        # Specifies whether to enable the dry run mode. If you do not specify this parameter, a normal request is sent. Valid values:
        # 
        # - **true**: A dry run request is sent. Only the request conditions are checked, and the specified operation is not performed. If the dry run fails, the corresponding error code is returned. If the dry run succeeds, the error code Defense.Control.DryRunOperation is returned.
        # 
        # - **false**: A normal request is sent. The specified operation is performed after the request passes the check.
        self.dry_run = dry_run
        # Instance ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query instance ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The ID of the protection rule that you want to modify.
        # 
        # > You can call the [DescribeDefenseRules](https://help.aliyun.com/document_detail/461426.html) operation to query the protection rule ID. You can create a protection rule by calling the [CreateDefenseRule](https://help.aliyun.com/document_detail/461421.html) operation.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The status of the protection rule that you want to modify. Valid values: 
        # - **0**: disabled.  
        # - **1**: enabled.
        # 
        # This parameter is required.
        self.rule_status = rule_status
        # The ID of the protection rule template.
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

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

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

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self


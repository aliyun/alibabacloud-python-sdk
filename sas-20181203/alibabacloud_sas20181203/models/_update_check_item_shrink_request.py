# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateCheckItemShrinkRequest(DaraModel):
    def __init__(
        self,
        assist_info_shrink: str = None,
        check_id: int = None,
        check_rule: str = None,
        check_show_name: str = None,
        description_shrink: str = None,
        instance_sub_type: str = None,
        instance_type: str = None,
        remark: str = None,
        risk_level: str = None,
        section_ids: List[int] = None,
        solution_shrink: str = None,
        status: str = None,
        vendor: str = None,
    ):
        # The help information for the check item.
        self.assist_info_shrink = assist_info_shrink
        # The ID of the custom check item to update.
        # > You can call the [ListCheckItems](~~ListCheckItems~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.check_id = check_id
        # The definition rule of the custom check item.
        self.check_rule = check_rule
        # The name of the custom check item.
        self.check_show_name = check_show_name
        # The description of the check item.
        self.description_shrink = description_shrink
        # The asset subtype of the cloud service.
        # > You can call the [ListCloudAssetSchemas](~~ListCloudAssetSchemas~~) operation to obtain this parameter.
        self.instance_sub_type = instance_sub_type
        # The asset type of the cloud service.
        # > You can call the [ListCloudAssetSchemas](~~ListCloudAssetSchemas~~) operation to obtain this parameter.
        self.instance_type = instance_type
        # The remarks.
        self.remark = remark
        # The risk level of the check item. Valid values:
        # - **HIGH**: High.
        # - **MEDIUM**: Medium.
        # - **LOW**: Low.
        self.risk_level = risk_level
        # The IDs of the sections associated with the check item.
        self.section_ids = section_ids
        # The solution information for the check item.
        self.solution_shrink = solution_shrink
        # The status of the check item. Valid values:
        # - **EDIT**: Being edited.
        # - **RELEASE**: Published.
        # 
        # > - Changing the status from **Published** to **Being edited** purges all historical records.
        # > - Only check items in the **Published** status can be used for checks.
        self.status = status
        # The cloud asset vendor.
        # > You can call the [ListCloudAssetSchemas](~~ListCloudAssetSchemas~~) operation to obtain the available vendors.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assist_info_shrink is not None:
            result['AssistInfo'] = self.assist_info_shrink

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_rule is not None:
            result['CheckRule'] = self.check_rule

        if self.check_show_name is not None:
            result['CheckShowName'] = self.check_show_name

        if self.description_shrink is not None:
            result['Description'] = self.description_shrink

        if self.instance_sub_type is not None:
            result['InstanceSubType'] = self.instance_sub_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.section_ids is not None:
            result['SectionIds'] = self.section_ids

        if self.solution_shrink is not None:
            result['Solution'] = self.solution_shrink

        if self.status is not None:
            result['Status'] = self.status

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssistInfo') is not None:
            self.assist_info_shrink = m.get('AssistInfo')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckRule') is not None:
            self.check_rule = m.get('CheckRule')

        if m.get('CheckShowName') is not None:
            self.check_show_name = m.get('CheckShowName')

        if m.get('Description') is not None:
            self.description_shrink = m.get('Description')

        if m.get('InstanceSubType') is not None:
            self.instance_sub_type = m.get('InstanceSubType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SectionIds') is not None:
            self.section_ids = m.get('SectionIds')

        if m.get('Solution') is not None:
            self.solution_shrink = m.get('Solution')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self


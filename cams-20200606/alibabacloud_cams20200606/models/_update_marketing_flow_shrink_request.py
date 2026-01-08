# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMarketingFLowShrinkRequest(DaraModel):
    def __init__(
        self,
        activity_code: str = None,
        activity_desc: str = None,
        activity_id: str = None,
        activity_name: str = None,
        cron_expression: str = None,
        end_date: str = None,
        execution_type: str = None,
        owner_id: int = None,
        param_flag: str = None,
        params_shrink: str = None,
        related_flow_code: str = None,
        related_flow_name: str = None,
        related_group_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_date: str = None,
    ):
        self.activity_code = activity_code
        self.activity_desc = activity_desc
        self.activity_id = activity_id
        self.activity_name = activity_name
        self.cron_expression = cron_expression
        self.end_date = end_date
        # This parameter is required.
        self.execution_type = execution_type
        self.owner_id = owner_id
        self.param_flag = param_flag
        self.params_shrink = params_shrink
        self.related_flow_code = related_flow_code
        self.related_flow_name = related_flow_name
        self.related_group_id = related_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_code is not None:
            result['ActivityCode'] = self.activity_code

        if self.activity_desc is not None:
            result['ActivityDesc'] = self.activity_desc

        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.execution_type is not None:
            result['ExecutionType'] = self.execution_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.param_flag is not None:
            result['ParamFlag'] = self.param_flag

        if self.params_shrink is not None:
            result['Params'] = self.params_shrink

        if self.related_flow_code is not None:
            result['RelatedFlowCode'] = self.related_flow_code

        if self.related_flow_name is not None:
            result['RelatedFlowName'] = self.related_flow_name

        if self.related_group_id is not None:
            result['RelatedGroupId'] = self.related_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityCode') is not None:
            self.activity_code = m.get('ActivityCode')

        if m.get('ActivityDesc') is not None:
            self.activity_desc = m.get('ActivityDesc')

        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ExecutionType') is not None:
            self.execution_type = m.get('ExecutionType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParamFlag') is not None:
            self.param_flag = m.get('ParamFlag')

        if m.get('Params') is not None:
            self.params_shrink = m.get('Params')

        if m.get('RelatedFlowCode') is not None:
            self.related_flow_code = m.get('RelatedFlowCode')

        if m.get('RelatedFlowName') is not None:
            self.related_flow_name = m.get('RelatedFlowName')

        if m.get('RelatedGroupId') is not None:
            self.related_group_id = m.get('RelatedGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self


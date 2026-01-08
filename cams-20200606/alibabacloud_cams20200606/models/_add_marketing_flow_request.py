# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class AddMarketingFlowRequest(DaraModel):
    def __init__(
        self,
        activity_desc: str = None,
        activity_name: str = None,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        cron_expression: str = None,
        end_date: str = None,
        execution_type: str = None,
        owner_id: int = None,
        param_flag: str = None,
        params: Dict[str, Any] = None,
        related_flow_code: str = None,
        related_flow_name: str = None,
        related_group_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_date: str = None,
    ):
        self.activity_desc = activity_desc
        # This parameter is required.
        self.activity_name = activity_name
        self.biz_code = biz_code
        self.biz_extend = biz_extend
        self.cron_expression = cron_expression
        self.end_date = end_date
        # This parameter is required.
        self.execution_type = execution_type
        self.owner_id = owner_id
        self.param_flag = param_flag
        self.params = params
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
        if self.activity_desc is not None:
            result['ActivityDesc'] = self.activity_desc

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend

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

        if self.params is not None:
            result['Params'] = self.params

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
        if m.get('ActivityDesc') is not None:
            self.activity_desc = m.get('ActivityDesc')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')

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
            self.params = m.get('Params')

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


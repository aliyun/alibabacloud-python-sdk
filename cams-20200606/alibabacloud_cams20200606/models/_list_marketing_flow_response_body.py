# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListMarketingFlowResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.ListMarketingFlowResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListMarketingFlowResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMarketingFlowResponseBodyData(DaraModel):
    def __init__(
        self,
        activity_code: str = None,
        activity_desc: str = None,
        activity_name: str = None,
        activity_status: str = None,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        cron_expression: str = None,
        end_date: str = None,
        execution_type: str = None,
        gmt_create: str = None,
        gmt_modifier: str = None,
        id: int = None,
        param_flag: str = None,
        params: Dict[str, Any] = None,
        related_flow_code: str = None,
        related_flow_name: str = None,
        related_group_id: str = None,
        related_group_name: str = None,
        specific_time: str = None,
        start_date: str = None,
        tenant_code: str = None,
    ):
        self.activity_code = activity_code
        self.activity_desc = activity_desc
        self.activity_name = activity_name
        self.activity_status = activity_status
        self.biz_code = biz_code
        self.biz_extend = biz_extend
        self.cron_expression = cron_expression
        self.end_date = end_date
        self.execution_type = execution_type
        self.gmt_create = gmt_create
        self.gmt_modifier = gmt_modifier
        self.id = id
        self.param_flag = param_flag
        self.params = params
        self.related_flow_code = related_flow_code
        self.related_flow_name = related_flow_name
        self.related_group_id = related_group_id
        self.related_group_name = related_group_name
        self.specific_time = specific_time
        self.start_date = start_date
        self.tenant_code = tenant_code

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

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.activity_status is not None:
            result['ActivityStatus'] = self.activity_status

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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modifier is not None:
            result['GmtModifier'] = self.gmt_modifier

        if self.id is not None:
            result['Id'] = self.id

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

        if self.related_group_name is not None:
            result['RelatedGroupName'] = self.related_group_name

        if self.specific_time is not None:
            result['SpecificTime'] = self.specific_time

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityCode') is not None:
            self.activity_code = m.get('ActivityCode')

        if m.get('ActivityDesc') is not None:
            self.activity_desc = m.get('ActivityDesc')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('ActivityStatus') is not None:
            self.activity_status = m.get('ActivityStatus')

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

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModifier') is not None:
            self.gmt_modifier = m.get('GmtModifier')

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

        if m.get('RelatedGroupName') is not None:
            self.related_group_name = m.get('RelatedGroupName')

        if m.get('SpecificTime') is not None:
            self.specific_time = m.get('SpecificTime')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')

        return self


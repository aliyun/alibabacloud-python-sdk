# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListBillingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        list: List[main_models.ListBillingResponseBodyList] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        self.list = list
        # 错误描述，成功时为空
        self.message = message
        # 页码
        self.page = page
        # 每页条数
        self.page_size = page_size
        # 请求追踪 ID
        self.request_id = request_id
        # 总数
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListBillingResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListBillingResponseBodyList(DaraModel):
    def __init__(
        self,
        billing_id: str = None,
        biz_id: str = None,
        biz_type: str = None,
        cost_source: List[str] = None,
        cost_source_display_name: List[str] = None,
        end_time: str = None,
        entry_object_id: str = None,
        entry_object_type: str = None,
        is_shadow: bool = None,
        operation: str = None,
        operation_display_name: str = None,
        start_time: str = None,
        status: str = None,
        status_display_name: str = None,
        tenant_id: int = None,
        total_credit_cost: str = None,
        wn_user_id: str = None,
    ):
        # 账单业务ID
        self.billing_id = billing_id
        # 业务来源ID
        self.biz_id = biz_id
        # 业务来源类型
        self.biz_type = biz_type
        # costSource
        self.cost_source = cost_source
        # costSourceDisplayName
        self.cost_source_display_name = cost_source_display_name
        # 结束时间
        self.end_time = end_time
        # 入口对象ID
        self.entry_object_id = entry_object_id
        # 入口对象类型
        self.entry_object_type = entry_object_type
        # 是否影子账单
        self.is_shadow = is_shadow
        # 操作类型
        self.operation = operation
        # 操作类型展示名称
        self.operation_display_name = operation_display_name
        # 开始时间
        self.start_time = start_time
        # 状态
        self.status = status
        # 状态展示名称
        self.status_display_name = status_display_name
        # 租户ID
        self.tenant_id = tenant_id
        # 汇总 credit 消耗
        self.total_credit_cost = total_credit_cost
        # WINNEXO 平台用户ID
        self.wn_user_id = wn_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_id is not None:
            result['billingId'] = self.billing_id

        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.cost_source is not None:
            result['costSource'] = self.cost_source

        if self.cost_source_display_name is not None:
            result['costSourceDisplayName'] = self.cost_source_display_name

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.entry_object_id is not None:
            result['entryObjectId'] = self.entry_object_id

        if self.entry_object_type is not None:
            result['entryObjectType'] = self.entry_object_type

        if self.is_shadow is not None:
            result['isShadow'] = self.is_shadow

        if self.operation is not None:
            result['operation'] = self.operation

        if self.operation_display_name is not None:
            result['operationDisplayName'] = self.operation_display_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.status_display_name is not None:
            result['statusDisplayName'] = self.status_display_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.total_credit_cost is not None:
            result['totalCreditCost'] = self.total_credit_cost

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingId') is not None:
            self.billing_id = m.get('billingId')

        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('costSource') is not None:
            self.cost_source = m.get('costSource')

        if m.get('costSourceDisplayName') is not None:
            self.cost_source_display_name = m.get('costSourceDisplayName')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('entryObjectId') is not None:
            self.entry_object_id = m.get('entryObjectId')

        if m.get('entryObjectType') is not None:
            self.entry_object_type = m.get('entryObjectType')

        if m.get('isShadow') is not None:
            self.is_shadow = m.get('isShadow')

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('operationDisplayName') is not None:
            self.operation_display_name = m.get('operationDisplayName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusDisplayName') is not None:
            self.status_display_name = m.get('statusDisplayName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('totalCreditCost') is not None:
            self.total_credit_cost = m.get('totalCreditCost')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self


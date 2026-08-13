# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBillingRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        end_time: str = None,
        ignore_zero: bool = None,
        operation: str = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
        status: str = None,
        tenant_id: str = None,
        wn_user_id: str = None,
    ):
        # 业务来源ID（可选筛选）
        self.biz_id = biz_id
        # 业务来源类型（可选筛选）
        self.biz_type = biz_type
        # 结束时间范围，ISO-8601 字符串，如 2026-08-05T16:30:00.000Z
        self.end_time = end_time
        # 是否过滤 credit 消耗为 0 的账单，默认 true（过滤）
        self.ignore_zero = ignore_zero
        # 操作类型（可选筛选）
        self.operation = operation
        # 页码
        self.page = page
        # 每页条数
        self.page_size = page_size
        # 开始时间范围，ISO-8601 字符串，如 2026-08-05T16:30:00.000Z
        self.start_time = start_time
        # 状态（可选筛选）
        self.status = status
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id
        # 用户ID（WINNEXO 平台用户ID，可选筛选）
        self.wn_user_id = wn_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.ignore_zero is not None:
            result['ignoreZero'] = self.ignore_zero

        if self.operation is not None:
            result['operation'] = self.operation

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('ignoreZero') is not None:
            self.ignore_zero = m.get('ignoreZero')

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self


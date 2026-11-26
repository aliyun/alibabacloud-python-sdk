# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBillingRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        biz_id: str = None,
        biz_type: str = None,
        end_time: str = None,
        ignore_zero: bool = None,
        operation: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
        status: str = None,
        tenant_id: str = None,
        wn_user_id: str = None,
    ):
        # The platform application token issued by the console. If you specify this parameter, the request is executed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The unique identifier of the business. When bizType is set to LibraryChat, bizId refers to the ID of the document library.
        self.biz_id = biz_id
        # The business type. Valid values: LlmChat (model Q&A) and LibraryChat (document library Q&A).
        self.biz_type = biz_type
        # The actual end timestamp of the live stream. The value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # Specifies whether to filter out bills with zero credit consumption. Default value: true.
        self.ignore_zero = ignore_zero
        # The operation item. Valid values:
        # - start: indicates the creation of a task. This is the default value and usually does not need to be explicitly specified.
        # - stop: stops a real-time meeting task. This corresponds to the creation of a real-time meeting and is set to stop to trigger a call after the meeting ends. This value is used in real-time meeting scenarios.
        # Note: When you end a real-time recording, you must set this parameter to stop.
        self.operation = operation
        # The code of the proxy user, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The ID of the proxy user, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The current page number.
        self.page = page
        # The number of entries per page. Default value: 20. Minimum value: 1. Maximum value: 50.
        self.page_size = page_size
        # The start time of the query. The value is a UNIX timestamp in seconds.
        self.start_time = start_time
        # The task status. A status of Running is returned immediately after the task is submitted.
        self.status = status
        # The tenant ID. This is a common parameter. For winnexo-cli, this parameter is explicitly passed by using --tenant-id.
        self.tenant_id = tenant_id
        # The user ID, which is the WINNEXO platform user ID. This parameter is optional for filtering.
        self.wn_user_id = wn_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

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

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

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

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

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


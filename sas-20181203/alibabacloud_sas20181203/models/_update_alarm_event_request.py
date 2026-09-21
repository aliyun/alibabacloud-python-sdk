# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAlarmEventRequest(DaraModel):
    def __init__(
        self,
        alarm_event_id_list: List[int] = None,
        lang: str = None,
        operation_code: str = None,
        resource_directory_account_id: int = None,
    ):
        # The list of alert event IDs.
        # 
        # You can call ListHoneypotAlarmEvents to obtain valid alert event IDs. Before calling this operation, ensure that honeypots are deployed and honeypot alert event data exists.
        # 
        # This parameter is required. If this parameter is not specified, the API returns HTTP 400 with the error code IllegalParam.
        self.alarm_event_id_list = alarm_event_id_list
        # The language of the request and response. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The processing method for the alert event. Valid values:
        # 
        # - **manual_handled**: Handled.
        # - **ignore**: Ignored.
        # - **cancel_ignore**: Removed from the whitelist.
        # 
        # This parameter is required. If this parameter is not specified, the API returns HTTP 400 with the error code IllegalParam.
        self.operation_code = operation_code
        # The Alibaba Cloud account ID of the member accounts in the resource folder.
        # >You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_event_id_list is not None:
            result['AlarmEventIdList'] = self.alarm_event_id_list

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventIdList') is not None:
            self.alarm_event_id_list = m.get('AlarmEventIdList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self


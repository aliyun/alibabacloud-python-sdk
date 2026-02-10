# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSuspEventDetailRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        lang: str = None,
        resource_directory_account_id: int = None,
        source_ip: str = None,
        suspicious_event_id: int = None,
    ):
        # The data source of the exception. Set the value to sas.
        # 
        # This parameter is required.
        self.from_ = from_
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to query the ID.
        self.resource_directory_account_id = resource_directory_account_id
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ID of the exception.
        # 
        # This parameter is required.
        self.suspicious_event_id = suspicious_event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.suspicious_event_id is not None:
            result['SuspiciousEventId'] = self.suspicious_event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SuspiciousEventId') is not None:
            self.suspicious_event_id = m.get('SuspiciousEventId')

        return self


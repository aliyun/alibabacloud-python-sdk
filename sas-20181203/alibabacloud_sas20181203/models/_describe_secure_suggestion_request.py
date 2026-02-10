# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecureSuggestionRequest(DaraModel):
    def __init__(
        self,
        cal_type: str = None,
        lang: str = None,
        resource_directory_account_id: int = None,
        source: int = None,
        source_ip: str = None,
    ):
        # Choose to query the new or old version of the security score rules. When the value is **home_security_score**, it queries the new version of the security score rules; otherwise, it defaults to querying the old version of the security score rules.
        self.cal_type = cal_type
        # The language type for request and response messages, default is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Resource directory member account ID (Alibaba Cloud account).
        # > You can obtain this parameter by calling the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) API.
        self.resource_directory_account_id = resource_directory_account_id
        # Source of the security score. If left empty, it defaults to Cloud Security Center. Enumerated values:
        # 
        # - 0: Cloud Security Center.
        # 
        # - 1: Yaochi Console.
        self.source = source
        # The IP address of the access source.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cal_type is not None:
            result['CalType'] = self.cal_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalType') is not None:
            self.cal_type = m.get('CalType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self


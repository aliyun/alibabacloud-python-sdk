# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecurityStatInfoRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        resource_directory_account_id: str = None,
        source_ip: str = None,
    ):
        # Specifies the language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The ID of the member account. This parameter is used for the multi-account security control feature of Security Center to query the security information of other member accounts in the resource directory.
        self.resource_directory_account_id = resource_directory_account_id
        # The source IP address.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self


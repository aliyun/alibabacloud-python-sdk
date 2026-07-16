# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEmgVulSubmitRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        name: str = None,
        resource_directory_account_id: int = None,
        user_agreement: str = None,
    ):
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The name of the vulnerability to query.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the member accounts in the resource folder (Alibaba Cloud account).
        # >Invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether to perform vulnerability detection. Valid values:
        # 
        # - **yes**: Perform vulnerability detection.
        # - **no**: Do not perform vulnerability detection.
        # 
        # This parameter is required.
        self.user_agreement = user_agreement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.user_agreement is not None:
            result['UserAgreement'] = self.user_agreement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('UserAgreement') is not None:
            self.user_agreement = m.get('UserAgreement')

        return self


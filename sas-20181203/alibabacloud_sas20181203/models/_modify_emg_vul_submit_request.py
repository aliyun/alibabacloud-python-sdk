# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEmgVulSubmitRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        lang: str = None,
        name: str = None,
        resource_directory_account_id: int = None,
        user_agreement: str = None,
    ):
        # The client token used to ensure the idempotence of the request. Use a different token for different requests. Only ASCII characters are supported. The token can be up to 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for this request. Valid values: true: performs only a dry run without executing the actual operation. false: executes the request normally. Default value: false.
        self.dry_run = dry_run
        # The language of the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The name of the vulnerability to query.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the member accounts in the resource directory (Alibaba Cloud account).
        # >Call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether to run vulnerability detection. Valid values:
        # 
        # - **yes**: Run.
        # 
        # - **no**: Do not run.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('UserAgreement') is not None:
            self.user_agreement = m.get('UserAgreement')

        return self


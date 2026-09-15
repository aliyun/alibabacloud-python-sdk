# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityEventMarkMissIndividuallyRequest(DaraModel):
    def __init__(
        self,
        delete_mark_miss_param: str = None,
        from_: str = None,
        insert_mark_miss_param: str = None,
        lang: str = None,
        resource_directory_account_id: int = None,
        source_ip: str = None,
    ):
        # The alert whitelisting rule to delete.
        self.delete_mark_miss_param = delete_mark_miss_param
        # The source identifier of the request. Set the value to **sas**.
        self.from_ = from_
        # The alert whitelisting rule to add.
        self.insert_mark_miss_param = insert_mark_miss_param
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The Alibaba Cloud account ID of the member accounts in the resource folder.
        # >Invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The source IP address of the request. You do not need to specify this parameter. The system automatically obtains the value.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_mark_miss_param is not None:
            result['DeleteMarkMissParam'] = self.delete_mark_miss_param

        if self.from_ is not None:
            result['From'] = self.from_

        if self.insert_mark_miss_param is not None:
            result['InsertMarkMissParam'] = self.insert_mark_miss_param

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteMarkMissParam') is not None:
            self.delete_mark_miss_param = m.get('DeleteMarkMissParam')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('InsertMarkMissParam') is not None:
            self.insert_mark_miss_param = m.get('InsertMarkMissParam')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self


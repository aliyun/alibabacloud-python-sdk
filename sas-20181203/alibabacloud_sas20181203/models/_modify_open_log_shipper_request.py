# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyOpenLogShipperRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        resource_directory_account_id: int = None,
    ):
        # The identifier of the request source. Default value: **aegis**. Valid values:
        # 
        # - **aegis**: Server Guard edition.
        # - **sas**: Security Center edition.
        # 
        # > Server Guard users must use **aegis**, and Security Center users must use **sas**.
        self.from_ = from_
        # The ID of the member accounts in the resource directory (Alibaba Cloud account).
        # > You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self


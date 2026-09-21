# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackSuspEventQuaraFileRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        quara_file_id: int = None,
        resource_directory_account_id: int = None,
        source_ip: str = None,
    ):
        # The source of the request. Set the value to sas.
        self.from_ = from_
        # The ID of the quarantined file. You can call [DescribeSuspEventQuaraFiles](~~DescribeSuspEventQuaraFiles~~) to obtain this value from the Id field in the response. This parameter is required. If this parameter is not specified, the API returns HTTP 400 with error code -101.
        # 
        # Before you call this operation, make sure that the Security Center agent is installed on the ECS instance, and that file-related security events and corresponding quarantined files exist. After a file is quarantined, call DescribeSuspEventQuaraFiles to query the quarantined file ID, and then call this operation to restore the file.
        self.quara_file_id = quara_file_id
        # The Alibaba Cloud account ID of the member account in the resource directory.
        # >You can call [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.quara_file_id is not None:
            result['QuaraFileId'] = self.quara_file_id

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('QuaraFileId') is not None:
            self.quara_file_id = m.get('QuaraFileId')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self


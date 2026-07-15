# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAgenticSpaceQuotaRequest(DaraModel):
    def __init__(
        self,
        agentic_space_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        file_count_limit: int = None,
        file_system_id: str = None,
        size_limit: int = None,
    ):
        # AgenticSpace Id。
        # 
        # This parameter is required.
        self.agentic_space_id = agentic_space_id
        # Ensures the idempotency of the request. Generate a unique parameter value from your client to ensure that the value is unique across different requests.
        # 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run for this request. A dry run checks parameter validity and dependencies without actually modifying the instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without modifying the protocol service. The check items include required parameters, request format, and business dependency conditions. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned.
        # - false (default): Sends a normal request. After the check passes, the protocol service is directly modified.
        self.dry_run = dry_run
        # The file count limit for the quota. Valid values:
        # 
        # - Minimum value: 10,000.
        # 
        # - Maximum value: 100,000,000.
        self.file_count_limit = file_count_limit
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The total capacity limit for the quota. Unit: bytes.
        # 
        # Valid values:
        # 
        # - Minimum value: 10,737,418,240 (10 GiB).
        # - Maximum value: 1,099,511,627,776,000 (1,024,000 GiB).
        # - Step: 1,073,741,824 (1 GiB).
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentic_space_id is not None:
            result['AgenticSpaceId'] = self.agentic_space_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgenticSpaceId') is not None:
            self.agentic_space_id = m.get('AgenticSpaceId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        return self


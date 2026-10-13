# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProtocolServiceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
        protocol_service_ids: str = None,
        status: str = None,
    ):
        # Ensures the idempotency of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        # >If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The description of the protocol service or a part of the description used for matching.
        # 
        # Limits:
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter and cannot start with `http://` or `https://`.
        # - The description can contain digits, colons (:), underscores (_), or hyphens (-).
        self.description = description
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The maximum number of results to return for each request.
        # 
        # - Maximum value: 100.
        # - Minimum value: 10.
        # - Default value: 20.
        self.max_results = max_results
        # The token used to initiate the next request if the response of the current request is truncated. You can use this token to retrieve the remaining results.
        self.next_token = next_token
        # The protocol service IDs.
        # - Format: CSV
        # 
        # - Limit: You can specify up to 10 protocol service IDs.
        self.protocol_service_ids = protocol_service_ids
        # The status of the protocol service used for matching.
        # 
        # Format: CSV
        # 
        # Valid values:
        # - Creating: The protocol service is being created.
        # - Starting: The protocol service is being started.
        # - Running: The protocol service is available.
        # - Updating: The protocol service is being updated.
        # - Deleting: The protocol service is being deleted.
        # - Stopping: The protocol service is being stopped.
        # - Stopped: The protocol service is stopped.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.protocol_service_ids is not None:
            result['ProtocolServiceIds'] = self.protocol_service_ids

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProtocolServiceIds') is not None:
            self.protocol_service_ids = m.get('ProtocolServiceIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


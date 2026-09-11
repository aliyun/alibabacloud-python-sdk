# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProtocolMountTargetRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        export_id: str = None,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
        protocol_service_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The export directory ID of the protocol service. **Required**.
        # 
        # **How to obtain**:
        # - Call [CreateProtocolMountTarget](https://www.alibabacloud.com/help/en/cpfs/cpfsonecs/developer-reference/api-nas-2017-06-26-createprotocolmounttarget-cpfs) to create an export directory and obtain the ExportId from the response.
        # - Or call [DescribeProtocolMountTarget](https://www.alibabacloud.com/help/en/cpfs/cpfsonecs/developer-reference/api-nas-2017-06-26-describeprotocolmounttarget-cpfs) to query the list of export directories and obtain the ExportId from the response.
        # 
        # This parameter is required.
        self.export_id = export_id
        # The file system ID.
        # 
        # - CPFS: The ID must start with `cpfs-`, such as cpfs-125487\\*\\*\\*\\*.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, such as bmcpfs-0015\\*\\*\\*\\*.
        # - CPFS SE: The ID must start with `cpfsse-`, such as cpfsse-022c71b134\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The maximum number of results to return per query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # If the response is truncated, you can use NextToken to send a subsequent request to retrieve the content after the current truncation point.
        self.next_token = next_token
        # The protocol service ID. **Required**.
        # 
        # **How to obtain**: Call the [DescribeProtocolService](https://www.alibabacloud.com/help/en/cpfs/cpfsonecs/developer-reference/api-nas-2017-06-26-describeprotocolservice-cpfs) operation to query the list of protocol services and obtain the ProtocolServiceId from the response.
        # 
        # This parameter is required.
        self.protocol_service_id = protocol_service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.export_id is not None:
            result['ExportId'] = self.export_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')

        return self


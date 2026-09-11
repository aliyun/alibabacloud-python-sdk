# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyProtocolServiceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        protocol_service_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The description of the protocol service.
        # 
        # Limits:
        # 
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter or a Chinese character and cannot start with `http://` or `https://`.
        # - The description can contain digits, colons (:), underscores (_), or hyphens (-).
        # - **Spaces and other special characters are not allowed**. Valid example: `My-Protocol-Service_01`.
        self.description = description
        # Specifies whether to perform a dry run for this modification request.
        # A dry run checks parameter validity and dependencies without actually modifying the instance or incurring charges.
        # 
        # Valid values:
        # - true: Sends a dry run request without modifying the protocol service. The dry run checks whether required parameters are specified, whether the request format is valid, and whether business constraints and dependencies are met. If the check fails, the corresponding error is returned. If the check succeeds, HTTP status code 200 is returned.
        # - false (default): Sends a normal request. After the check succeeds, the protocol service is directly modified.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the protocol service. You can obtain the protocol service ID from the response of the [CreateProtocolService](https://www.alibabacloud.com/help/en/cpfs/cpfsonecs/developer-reference/api-nas-2017-06-26-createprotocolservice-cpfs) operation, or query it by calling the [DescribeProtocolService](https://www.alibabacloud.com/help/en/cpfs/cpfsonecs/developer-reference/api-nas-2017-06-26-describeprotocolservice-cpfs) operation.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')

        return self


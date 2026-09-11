# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyProtocolMountTargetRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        export_id: str = None,
        file_system_id: str = None,
        protocol_service_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Generate a unique value from your client to ensure that different requests have unique ClientToken values.
        # 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The description of the export directory of the protocol service.
        # 
        # Limits:
        # 
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter or Chinese character and cannot start with `http://` or `https://`.
        # - The description can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run for this modification request.
        # 
        # A dry run checks parameter validity and dependency conditions without actually modifying the export directory or incurring charges.
        # 
        # Valid values:
        # 
        # - **true**: Sends a dry run request without modifying the export directory. The check items include required parameters, request format, and business dependency conditions.
        #   - **DryRun=true also performs resource status checks** (including the requirement that the export directory is in the AVAILABLE state).
        #   - If the export directory status does not meet the requirements (such as CREATING), the corresponding error is returned.
        #   - **DryRun does not bypass status checks**. It only validates request parameter validity and basic dependencies.
        #   - If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned.
        # 
        # - **false (default)**: Sends a normal request. After the check passes, the export directory parameters are directly modified.
        self.dry_run = dry_run
        # The export directory ID of the protocol service. Call [DescribeProtocolMountTarget](https://www.alibabacloud.com/help/en/cpfs/cpfsonecs/developer-reference/api-nas-2017-06-26-describeprotocolmounttarget-cpfs) to obtain the export directory information.
        # 
        # This parameter is required.
        self.export_id = export_id
        # The file system ID. Call [DescribeFileSystems](https://www.alibabacloud.com/help/en/cpfs/cpfsonecs/developer-reference/api-nas-2017-06-26-describefilesystems-cpfs) (with FileSystemType set to cpfs) to obtain the file system information.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The protocol service ID. Call [DescribeProtocolService](https://www.alibabacloud.com/help/en/cpfs/cpfsonecs/developer-reference/api-nas-2017-06-26-describeprotocolservice-cpfs) to obtain the protocol service information.
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

        if self.export_id is not None:
            result['ExportId'] = self.export_id

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

        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')

        return self


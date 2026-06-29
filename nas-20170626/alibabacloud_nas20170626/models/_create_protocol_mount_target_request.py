# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateProtocolMountTargetRequest(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        fset_id: str = None,
        path: str = None,
        protocol_service_id: str = None,
        v_switch_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # The name of the permission group.
        # 
        # Default value: DEFAULT_VPC_GROUP_NAME.
        self.access_group_name = access_group_name
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The description of the protocol service export directory. This parameter is displayed as **Export Directory Name** in the console.
        # 
        # Limits:
        # - The description must be 2 to 128 characters in length and can contain letters and Chinese characters.
        # - The description must start with a letter or a Chinese character and cannot start with `http://` or `https://`.
        # - The description can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run for this request. A dry run checks parameter validity, dependencies, and other conditions without actually creating the instance or incurring charges.
        # 
        # Valid values:
        # - true: sends a dry run request without creating the export directory. The dry run checks whether required parameters are specified, whether the request format is valid, and whether business limit dependencies are met. If the check fails, the corresponding error is returned. If the check succeeds, HTTP status code 200 is returned, but ExportId is empty.
        # 
        # - false (default): sends a normal request. After the check succeeds, the instance is created.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the fileset to export.
        # 
        # Limits:
        # - The fileset must already exist.
        # - Only one export directory can be created for each fileset.
        # - You must specify one and only one of FsetId and Path.
        self.fset_id = fset_id
        # The path of the CPFS directory to export.
        # 
        # Limits:
        # - The directory must already exist on the CPFS file system.
        # - Only one export can be created for each directory.
        # - You must specify one and only one of FsetId and Path.
        # 
        # Format:
        # - The path must be 1 to 1,024 characters in length.
        # - The path must be encoded in UTF-8.
        # - The path must start and end with a forward slash (/). The root directory is `/`.
        self.path = path
        # The ID of the protocol service.
        # 
        # This parameter is required.
        self.protocol_service_id = protocol_service_id
        # The ID of the vSwitch for the protocol service export.
        # 
        # If the storage redundancy type of the file system is not zone-redundant storage (ZRS), this parameter is required when VpcId is specified.
        # >  The vSwitch must be in the same zone as the target CPFS file system.
        self.v_switch_id = v_switch_id
        # The list of vSwitch IDs for the protocol service export.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC for the protocol service export.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.fset_id is not None:
            result['FsetId'] = self.fset_id

        if self.path is not None:
            result['Path'] = self.path

        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class AttachVscToFilesystemsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        resource_ids: List[main_models.AttachVscToFilesystemsRequestResourceIds] = None,
        role_chain: List[main_models.AttachVscToFilesystemsRequestRoleChain] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The ID information of file systems and virtual storage channels. A maximum of 10 entries can be specified per batch.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        self.role_chain = role_chain

    def validate(self):
        if self.resource_ids:
            for v1 in self.resource_ids:
                 if v1:
                    v1.validate()
        if self.role_chain:
            for v1 in self.role_chain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['ResourceIds'] = []
        if self.resource_ids is not None:
            for k1 in self.resource_ids:
                result['ResourceIds'].append(k1.to_map() if k1 else None)

        result['RoleChain'] = []
        if self.role_chain is not None:
            for k1 in self.role_chain:
                result['RoleChain'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.resource_ids = []
        if m.get('ResourceIds') is not None:
            for k1 in m.get('ResourceIds'):
                temp_model = main_models.AttachVscToFilesystemsRequestResourceIds()
                self.resource_ids.append(temp_model.from_map(k1))

        self.role_chain = []
        if m.get('RoleChain') is not None:
            for k1 in m.get('RoleChain'):
                temp_model = main_models.AttachVscToFilesystemsRequestRoleChain()
                self.role_chain.append(temp_model.from_map(k1))

        return self

class AttachVscToFilesystemsRequestRoleChain(DaraModel):
    def __init__(
        self,
        assume_role_for: str = None,
        role_arn: str = None,
        role_type: str = None,
    ):
        self.assume_role_for = assume_role_for
        self.role_arn = role_arn
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

class AttachVscToFilesystemsRequestResourceIds(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        vsc_id: str = None,
    ):
        # The file system ID.
        self.file_system_id = file_system_id
        # The virtual storage channel ID.
        self.vsc_id = vsc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        return self


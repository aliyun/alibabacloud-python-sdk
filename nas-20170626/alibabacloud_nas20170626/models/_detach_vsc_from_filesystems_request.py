# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DetachVscFromFilesystemsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        resource_ids: List[main_models.DetachVscFromFilesystemsRequestResourceIds] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The ID information of the file system and virtual storage channel. Each batch can contain up to 10 IDs.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids

    def validate(self):
        if self.resource_ids:
            for v1 in self.resource_ids:
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.resource_ids = []
        if m.get('ResourceIds') is not None:
            for k1 in m.get('ResourceIds'):
                temp_model = main_models.DetachVscFromFilesystemsRequestResourceIds()
                self.resource_ids.append(temp_model.from_map(k1))

        return self

class DetachVscFromFilesystemsRequestResourceIds(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        vsc_id: str = None,
    ):
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The ID of the virtual storage channel.
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


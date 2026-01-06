# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeFilesystemsVscAttachInfoRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_ids: List[main_models.DescribeFilesystemsVscAttachInfoRequestResourceIds] = None,
    ):
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # Query token, which is the NextToken value returned from the previous API call.
        self.next_token = next_token
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ResourceIds'] = []
        if self.resource_ids is not None:
            for k1 in self.resource_ids:
                result['ResourceIds'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.resource_ids = []
        if m.get('ResourceIds') is not None:
            for k1 in m.get('ResourceIds'):
                temp_model = main_models.DescribeFilesystemsVscAttachInfoRequestResourceIds()
                self.resource_ids.append(temp_model.from_map(k1))

        return self

class DescribeFilesystemsVscAttachInfoRequestResourceIds(DaraModel):
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


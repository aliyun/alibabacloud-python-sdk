# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeFilesystemsVscAttachInfoResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        vsc_attach_info: main_models.DescribeFilesystemsVscAttachInfoResponseBodyVscAttachInfo = None,
    ):
        # The number of directories to return for each query.
        # 
        # Valid values: 10 to 1000.
        # 
        # Default value: 10.
        self.max_results = max_results
        # Query token, which is the NextToken value returned from the previous API call.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of associated information.
        self.total_count = total_count
        # A collection of file system and virtual channel association data.
        self.vsc_attach_info = vsc_attach_info

    def validate(self):
        if self.vsc_attach_info:
            self.vsc_attach_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vsc_attach_info is not None:
            result['VscAttachInfo'] = self.vsc_attach_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VscAttachInfo') is not None:
            temp_model = main_models.DescribeFilesystemsVscAttachInfoResponseBodyVscAttachInfo()
            self.vsc_attach_info = temp_model.from_map(m.get('VscAttachInfo'))

        return self

class DescribeFilesystemsVscAttachInfoResponseBodyVscAttachInfo(DaraModel):
    def __init__(
        self,
        vsc_attach_info: List[main_models.DescribeFilesystemsVscAttachInfoResponseBodyVscAttachInfoVscAttachInfo] = None,
    ):
        self.vsc_attach_info = vsc_attach_info

    def validate(self):
        if self.vsc_attach_info:
            for v1 in self.vsc_attach_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VscAttachInfo'] = []
        if self.vsc_attach_info is not None:
            for k1 in self.vsc_attach_info:
                result['VscAttachInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vsc_attach_info = []
        if m.get('VscAttachInfo') is not None:
            for k1 in m.get('VscAttachInfo'):
                temp_model = main_models.DescribeFilesystemsVscAttachInfoResponseBodyVscAttachInfoVscAttachInfo()
                self.vsc_attach_info.append(temp_model.from_map(k1))

        return self

class DescribeFilesystemsVscAttachInfoResponseBodyVscAttachInfoVscAttachInfo(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        status: str = None,
        vsc_id: str = None,
    ):
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The association status of the file system and virtual channel. Valid values:
        # 
        # *   Attaching: The association is being made.
        # *   Attached: The association is complete.
        # *   Detaching: The association is being canceled.
        # *   Detached: The association is canceled.
        # *   Failed: The association failed.
        self.status = status
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

        if self.status is not None:
            result['Status'] = self.status

        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        return self


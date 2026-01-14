# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListAccelerationOfWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListAccelerationOfWorkspaceResponseBodyResult = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListAccelerationOfWorkspaceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAccelerationOfWorkspaceResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAccelerationOfWorkspaceResponseBodyResultData] = None,
        next: int = None,
        page_num: int = None,
        page_size: int = None,
        pre: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        self.data = data
        self.next = next
        self.page_num = page_num
        self.page_size = page_size
        self.pre = pre
        self.total_num = total_num
        self.total_pages = total_pages

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next is not None:
            result['Next'] = self.next

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre is not None:
            result['Pre'] = self.pre

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAccelerationOfWorkspaceResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Next') is not None:
            self.next = m.get('Next')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pre') is not None:
            self.pre = m.get('Pre')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListAccelerationOfWorkspaceResponseBodyResultData(DaraModel):
    def __init__(
        self,
        creator_name: str = None,
        cube_id: str = None,
        cube_name: str = None,
        enable_quickindex_time: str = None,
        job_history_id: str = None,
        job_id: str = None,
        job_status: int = None,
        last_modify_time: str = None,
        size: str = None,
    ):
        self.creator_name = creator_name
        self.cube_id = cube_id
        self.cube_name = cube_name
        self.enable_quickindex_time = enable_quickindex_time
        self.job_history_id = job_history_id
        self.job_id = job_id
        self.job_status = job_status
        self.last_modify_time = last_modify_time
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.cube_name is not None:
            result['CubeName'] = self.cube_name

        if self.enable_quickindex_time is not None:
            result['EnableQuickindexTime'] = self.enable_quickindex_time

        if self.job_history_id is not None:
            result['JobHistoryId'] = self.job_history_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('CubeName') is not None:
            self.cube_name = m.get('CubeName')

        if m.get('EnableQuickindexTime') is not None:
            self.enable_quickindex_time = m.get('EnableQuickindexTime')

        if m.get('JobHistoryId') is not None:
            self.job_history_id = m.get('JobHistoryId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self


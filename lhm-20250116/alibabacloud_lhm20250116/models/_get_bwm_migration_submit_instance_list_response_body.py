# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetBwmMigrationSubmitInstanceListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetBwmMigrationSubmitInstanceListResponseBodyData] = None,
        empty: bool = None,
        err_code: str = None,
        err_message: str = None,
        not_empty: bool = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_pages: int = None,
    ):
        # The response data.
        self.data = data
        # Indicates whether the result is empty.
        self.empty = empty
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # Indicates whether the result is not empty.
        self.not_empty = not_empty
        # The page number.
        self.page_index = page_index
        # The page size.
        self.page_size = page_size
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success. A value of false indicates failure. If the call fails, use errCode and errMessage to troubleshoot the issue.
        self.success = success
        # The total number of entries.
        self.total_count = total_count
        # The total number of pages.
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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.empty is not None:
            result['empty'] = self.empty

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.not_empty is not None:
            result['notEmpty'] = self.not_empty

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.total_pages is not None:
            result['totalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetBwmMigrationSubmitInstanceListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('empty') is not None:
            self.empty = m.get('empty')

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('notEmpty') is not None:
            self.not_empty = m.get('notEmpty')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')

        return self

class GetBwmMigrationSubmitInstanceListResponseBodyData(DaraModel):
    def __init__(
        self,
        detail: str = None,
        gmt_convert: str = None,
        instance_id: str = None,
        instance_name: str = None,
        src_meta_gmt_update: str = None,
        src_meta_info: str = None,
        status: str = None,
    ):
        # The reason for the conversion failure.
        self.detail = detail
        # The conversion execution time.
        self.gmt_convert = gmt_convert
        # The UUID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The time when the source metadata was last updated.
        self.src_meta_gmt_update = src_meta_gmt_update
        # The scheduling information of the source.
        self.src_meta_info = src_meta_info
        # The execution status of the instance. Valid values:
        # - NOT_START: Not started.
        # - READY: Pending execution.
        # - RUNNING: Running.
        # - ALL_SUCCESS: All succeeded.
        # - PARTIAL_SUCCESS: Partially succeeded.
        # - FAILURE: Failed.
        # - MANUAL: Manually uploaded.
        # 
        # If the status code cannot be recognized, the value defaults to NOT_START.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['detail'] = self.detail

        if self.gmt_convert is not None:
            result['gmtConvert'] = self.gmt_convert

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.src_meta_gmt_update is not None:
            result['srcMetaGmtUpdate'] = self.src_meta_gmt_update

        if self.src_meta_info is not None:
            result['srcMetaInfo'] = self.src_meta_info

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('gmtConvert') is not None:
            self.gmt_convert = m.get('gmtConvert')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('srcMetaGmtUpdate') is not None:
            self.src_meta_gmt_update = m.get('srcMetaGmtUpdate')

        if m.get('srcMetaInfo') is not None:
            self.src_meta_info = m.get('srcMetaInfo')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self


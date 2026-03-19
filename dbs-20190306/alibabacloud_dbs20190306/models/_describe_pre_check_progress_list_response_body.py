# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribePreCheckProgressListResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: main_models.DescribePreCheckProgressListResponseBodyItems = None,
        progress: int = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        self.items = items
        # The precheck progress. The value ranges from 0 to 100.
        self.progress = progress
        # The request ID.
        self.request_id = request_id
        # The precheck status. Valid values:
        # 
        # - **running**: The precheck is in progress.
        # 
        # - **failed**: The precheck failed.
        # 
        # - **finish**: The precheck is complete.
        self.status = status
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Items') is not None:
            temp_model = main_models.DescribePreCheckProgressListResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribePreCheckProgressListResponseBodyItems(DaraModel):
    def __init__(
        self,
        pre_check_progress_detail: List[main_models.DescribePreCheckProgressListResponseBodyItemsPreCheckProgressDetail] = None,
    ):
        self.pre_check_progress_detail = pre_check_progress_detail

    def validate(self):
        if self.pre_check_progress_detail:
            for v1 in self.pre_check_progress_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PreCheckProgressDetail'] = []
        if self.pre_check_progress_detail is not None:
            for k1 in self.pre_check_progress_detail:
                result['PreCheckProgressDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pre_check_progress_detail = []
        if m.get('PreCheckProgressDetail') is not None:
            for k1 in m.get('PreCheckProgressDetail'):
                temp_model = main_models.DescribePreCheckProgressListResponseBodyItemsPreCheckProgressDetail()
                self.pre_check_progress_detail.append(temp_model.from_map(k1))

        return self

class DescribePreCheckProgressListResponseBodyItemsPreCheckProgressDetail(DaraModel):
    def __init__(
        self,
        boot_time: int = None,
        err_msg: str = None,
        finish_time: int = None,
        item: str = None,
        job_id: str = None,
        names: str = None,
        order_num: str = None,
        state: str = None,
    ):
        self.boot_time = boot_time
        self.err_msg = err_msg
        self.finish_time = finish_time
        self.item = item
        self.job_id = job_id
        self.names = names
        self.order_num = order_num
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.item is not None:
            result['Item'] = self.item

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.names is not None:
            result['Names'] = self.names

        if self.order_num is not None:
            result['OrderNum'] = self.order_num

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self


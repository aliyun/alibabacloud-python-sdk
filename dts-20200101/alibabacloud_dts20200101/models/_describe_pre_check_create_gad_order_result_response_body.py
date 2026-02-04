# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribePreCheckCreateGadOrderResultResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        instance_id: str = None,
        pre_check_items: main_models.DescribePreCheckCreateGadOrderResultResponseBodyPreCheckItems = None,
        pre_check_result: bool = None,
        region_id: str = None,
        request_id: str = None,
        success: str = None,
        task_id: str = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.pre_check_items = pre_check_items
        self.pre_check_result = pre_check_result
        self.region_id = region_id
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        if self.pre_check_items:
            self.pre_check_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pre_check_items is not None:
            result['PreCheckItems'] = self.pre_check_items.to_map()

        if self.pre_check_result is not None:
            result['PreCheckResult'] = self.pre_check_result

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PreCheckItems') is not None:
            temp_model = main_models.DescribePreCheckCreateGadOrderResultResponseBodyPreCheckItems()
            self.pre_check_items = temp_model.from_map(m.get('PreCheckItems'))

        if m.get('PreCheckResult') is not None:
            self.pre_check_result = m.get('PreCheckResult')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribePreCheckCreateGadOrderResultResponseBodyPreCheckItems(DaraModel):
    def __init__(
        self,
        pre_check_items: List[main_models.DescribePreCheckCreateGadOrderResultResponseBodyPreCheckItemsPreCheckItems] = None,
    ):
        self.pre_check_items = pre_check_items

    def validate(self):
        if self.pre_check_items:
            for v1 in self.pre_check_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PreCheckItems'] = []
        if self.pre_check_items is not None:
            for k1 in self.pre_check_items:
                result['PreCheckItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pre_check_items = []
        if m.get('PreCheckItems') is not None:
            for k1 in m.get('PreCheckItems'):
                temp_model = main_models.DescribePreCheckCreateGadOrderResultResponseBodyPreCheckItemsPreCheckItems()
                self.pre_check_items.append(temp_model.from_map(k1))

        return self

class DescribePreCheckCreateGadOrderResultResponseBodyPreCheckItemsPreCheckItems(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        status: str = None,
    ):
        self.code = code
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


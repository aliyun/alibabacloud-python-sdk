# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetOperationRecordsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.GetOperationRecordsResponseBodyResult] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.GetOperationRecordsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetOperationRecordsResponseBodyResult(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_exit: str = None,
        active_time_gmt: str = None,
        activity_id: str = None,
        data_id: int = None,
        digital_sign: str = None,
        files: str = None,
        operate_time_gmt: str = None,
        operate_type: str = None,
        operator_display_name: str = None,
        operator_name: str = None,
        operator_nick_name: str = None,
        operator_photo_url: str = None,
        operator_status: str = None,
        operator_user_id: str = None,
        process_instance_id: str = None,
        remark: str = None,
        show_name: str = None,
        size: int = None,
        task_execute_type: str = None,
        task_hold_time_gmt: int = None,
        task_id: str = None,
        task_type: str = None,
        type: str = None,
    ):
        self.action = action
        self.action_exit = action_exit
        self.active_time_gmt = active_time_gmt
        self.activity_id = activity_id
        self.data_id = data_id
        self.digital_sign = digital_sign
        self.files = files
        self.operate_time_gmt = operate_time_gmt
        self.operate_type = operate_type
        self.operator_display_name = operator_display_name
        self.operator_name = operator_name
        self.operator_nick_name = operator_nick_name
        self.operator_photo_url = operator_photo_url
        self.operator_status = operator_status
        self.operator_user_id = operator_user_id
        self.process_instance_id = process_instance_id
        self.remark = remark
        self.show_name = show_name
        self.size = size
        self.task_execute_type = task_execute_type
        self.task_hold_time_gmt = task_hold_time_gmt
        self.task_id = task_id
        self.task_type = task_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_exit is not None:
            result['ActionExit'] = self.action_exit

        if self.active_time_gmt is not None:
            result['ActiveTimeGMT'] = self.active_time_gmt

        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.digital_sign is not None:
            result['DigitalSign'] = self.digital_sign

        if self.files is not None:
            result['Files'] = self.files

        if self.operate_time_gmt is not None:
            result['OperateTimeGMT'] = self.operate_time_gmt

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.operator_display_name is not None:
            result['OperatorDisplayName'] = self.operator_display_name

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.operator_nick_name is not None:
            result['OperatorNickName'] = self.operator_nick_name

        if self.operator_photo_url is not None:
            result['OperatorPhotoUrl'] = self.operator_photo_url

        if self.operator_status is not None:
            result['OperatorStatus'] = self.operator_status

        if self.operator_user_id is not None:
            result['OperatorUserId'] = self.operator_user_id

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.size is not None:
            result['Size'] = self.size

        if self.task_execute_type is not None:
            result['TaskExecuteType'] = self.task_execute_type

        if self.task_hold_time_gmt is not None:
            result['TaskHoldTimeGMT'] = self.task_hold_time_gmt

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionExit') is not None:
            self.action_exit = m.get('ActionExit')

        if m.get('ActiveTimeGMT') is not None:
            self.active_time_gmt = m.get('ActiveTimeGMT')

        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('DigitalSign') is not None:
            self.digital_sign = m.get('DigitalSign')

        if m.get('Files') is not None:
            self.files = m.get('Files')

        if m.get('OperateTimeGMT') is not None:
            self.operate_time_gmt = m.get('OperateTimeGMT')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('OperatorDisplayName') is not None:
            self.operator_display_name = m.get('OperatorDisplayName')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('OperatorNickName') is not None:
            self.operator_nick_name = m.get('OperatorNickName')

        if m.get('OperatorPhotoUrl') is not None:
            self.operator_photo_url = m.get('OperatorPhotoUrl')

        if m.get('OperatorStatus') is not None:
            self.operator_status = m.get('OperatorStatus')

        if m.get('OperatorUserId') is not None:
            self.operator_user_id = m.get('OperatorUserId')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TaskExecuteType') is not None:
            self.task_execute_type = m.get('TaskExecuteType')

        if m.get('TaskHoldTimeGMT') is not None:
            self.task_hold_time_gmt = m.get('TaskHoldTimeGMT')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


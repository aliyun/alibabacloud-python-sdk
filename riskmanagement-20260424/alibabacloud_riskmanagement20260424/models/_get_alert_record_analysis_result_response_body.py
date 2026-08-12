# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetAlertRecordAnalysisResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAlertRecordAnalysisResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the call fails. For more information, see error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # - **true**: The call is successful.                               
        # - **false**: The call fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAlertRecordAnalysisResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAlertRecordAnalysisResultResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis_code: str = None,
        unique_tag_list: List[main_models.GetAlertRecordAnalysisResultResponseBodyDataUniqueTagList] = None,
    ):
        # The code of the tracing result. (Deprecated)
        self.analysis_code = analysis_code
        # The list of tracing results.
        self.unique_tag_list = unique_tag_list

    def validate(self):
        if self.unique_tag_list:
            for v1 in self.unique_tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_code is not None:
            result['AnalysisCode'] = self.analysis_code

        result['UniqueTagList'] = []
        if self.unique_tag_list is not None:
            for k1 in self.unique_tag_list:
                result['UniqueTagList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisCode') is not None:
            self.analysis_code = m.get('AnalysisCode')

        self.unique_tag_list = []
        if m.get('UniqueTagList') is not None:
            for k1 in m.get('UniqueTagList'):
                temp_model = main_models.GetAlertRecordAnalysisResultResponseBodyDataUniqueTagList()
                self.unique_tag_list.append(temp_model.from_map(k1))

        return self

class GetAlertRecordAnalysisResultResponseBodyDataUniqueTagList(DaraModel):
    def __init__(
        self,
        alarm_unique_info: str = None,
        ali_uid: str = None,
        analysis_code: str = None,
        analysis_result: str = None,
        choose_like: bool = None,
        ip: str = None,
        machine_instance_id: str = None,
        type: str = None,
        unique_info: str = None,
        uuid: str = None,
    ):
        # The unique identifier of the alert event.
        self.alarm_unique_info = alarm_unique_info
        # The 16-digit AliUid of the user.
        self.ali_uid = ali_uid
        # The code of the tracing result.
        self.analysis_code = analysis_code
        # The text of the tracing result.
        self.analysis_result = analysis_result
        # Indicates whether the result is liked. Valid values:
        # 
        # - **true**: Liked.
        # - **false**: Not liked.
        self.choose_like = choose_like
        # The IP address.
        self.ip = ip
        # The instance ID of the server.
        self.machine_instance_id = machine_instance_id
        # The display mode of the exception event details. Valid values:
        # 
        # - **text**: plain text
        # - **html**: rich text
        self.type = type
        # The unique ID of the alert event.
        self.unique_info = unique_info
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.analysis_code is not None:
            result['AnalysisCode'] = self.analysis_code

        if self.analysis_result is not None:
            result['AnalysisResult'] = self.analysis_result

        if self.choose_like is not None:
            result['ChooseLike'] = self.choose_like

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.machine_instance_id is not None:
            result['MachineInstanceId'] = self.machine_instance_id

        if self.type is not None:
            result['Type'] = self.type

        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AnalysisCode') is not None:
            self.analysis_code = m.get('AnalysisCode')

        if m.get('AnalysisResult') is not None:
            self.analysis_result = m.get('AnalysisResult')

        if m.get('ChooseLike') is not None:
            self.choose_like = m.get('ChooseLike')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('MachineInstanceId') is not None:
            self.machine_instance_id = m.get('MachineInstanceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self


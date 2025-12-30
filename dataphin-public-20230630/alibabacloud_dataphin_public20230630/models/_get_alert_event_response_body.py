# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetAlertEventResponseBody(DaraModel):
    def __init__(
        self,
        alert_event_info: main_models.GetAlertEventResponseBodyAlertEventInfo = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.alert_event_info = alert_event_info
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.alert_event_info:
            self.alert_event_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_event_info is not None:
            result['AlertEventInfo'] = self.alert_event_info.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertEventInfo') is not None:
            temp_model = main_models.GetAlertEventResponseBodyAlertEventInfo()
            self.alert_event_info = temp_model.from_map(m.get('AlertEventInfo'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAlertEventResponseBodyAlertEventInfo(DaraModel):
    def __init__(
        self,
        alert_frequency: str = None,
        alert_object: main_models.GetAlertEventResponseBodyAlertEventInfoAlertObject = None,
        alert_reason: main_models.GetAlertEventResponseBodyAlertEventInfoAlertReason = None,
        alert_receiver_list: List[main_models.GetAlertEventResponseBodyAlertEventInfoAlertReceiverList] = None,
        belong_project: main_models.GetAlertEventResponseBodyAlertEventInfoBelongProject = None,
        do_not_disturb_end_time: str = None,
        first_alert_time: str = None,
        id: int = None,
        latest_alert_time: str = None,
        status: str = None,
        total_alert_times: int = None,
        url_config: main_models.GetAlertEventResponseBodyAlertEventInfoUrlConfig = None,
    ):
        self.alert_frequency = alert_frequency
        self.alert_object = alert_object
        self.alert_reason = alert_reason
        self.alert_receiver_list = alert_receiver_list
        self.belong_project = belong_project
        self.do_not_disturb_end_time = do_not_disturb_end_time
        self.first_alert_time = first_alert_time
        self.id = id
        self.latest_alert_time = latest_alert_time
        self.status = status
        self.total_alert_times = total_alert_times
        self.url_config = url_config

    def validate(self):
        if self.alert_object:
            self.alert_object.validate()
        if self.alert_reason:
            self.alert_reason.validate()
        if self.alert_receiver_list:
            for v1 in self.alert_receiver_list:
                 if v1:
                    v1.validate()
        if self.belong_project:
            self.belong_project.validate()
        if self.url_config:
            self.url_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_frequency is not None:
            result['AlertFrequency'] = self.alert_frequency

        if self.alert_object is not None:
            result['AlertObject'] = self.alert_object.to_map()

        if self.alert_reason is not None:
            result['AlertReason'] = self.alert_reason.to_map()

        result['AlertReceiverList'] = []
        if self.alert_receiver_list is not None:
            for k1 in self.alert_receiver_list:
                result['AlertReceiverList'].append(k1.to_map() if k1 else None)

        if self.belong_project is not None:
            result['BelongProject'] = self.belong_project.to_map()

        if self.do_not_disturb_end_time is not None:
            result['DoNotDisturbEndTime'] = self.do_not_disturb_end_time

        if self.first_alert_time is not None:
            result['FirstAlertTime'] = self.first_alert_time

        if self.id is not None:
            result['Id'] = self.id

        if self.latest_alert_time is not None:
            result['LatestAlertTime'] = self.latest_alert_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_alert_times is not None:
            result['TotalAlertTimes'] = self.total_alert_times

        if self.url_config is not None:
            result['UrlConfig'] = self.url_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertFrequency') is not None:
            self.alert_frequency = m.get('AlertFrequency')

        if m.get('AlertObject') is not None:
            temp_model = main_models.GetAlertEventResponseBodyAlertEventInfoAlertObject()
            self.alert_object = temp_model.from_map(m.get('AlertObject'))

        if m.get('AlertReason') is not None:
            temp_model = main_models.GetAlertEventResponseBodyAlertEventInfoAlertReason()
            self.alert_reason = temp_model.from_map(m.get('AlertReason'))

        self.alert_receiver_list = []
        if m.get('AlertReceiverList') is not None:
            for k1 in m.get('AlertReceiverList'):
                temp_model = main_models.GetAlertEventResponseBodyAlertEventInfoAlertReceiverList()
                self.alert_receiver_list.append(temp_model.from_map(k1))

        if m.get('BelongProject') is not None:
            temp_model = main_models.GetAlertEventResponseBodyAlertEventInfoBelongProject()
            self.belong_project = temp_model.from_map(m.get('BelongProject'))

        if m.get('DoNotDisturbEndTime') is not None:
            self.do_not_disturb_end_time = m.get('DoNotDisturbEndTime')

        if m.get('FirstAlertTime') is not None:
            self.first_alert_time = m.get('FirstAlertTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LatestAlertTime') is not None:
            self.latest_alert_time = m.get('LatestAlertTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalAlertTimes') is not None:
            self.total_alert_times = m.get('TotalAlertTimes')

        if m.get('UrlConfig') is not None:
            temp_model = main_models.GetAlertEventResponseBodyAlertEventInfoUrlConfig()
            self.url_config = temp_model.from_map(m.get('UrlConfig'))

        return self

class GetAlertEventResponseBodyAlertEventInfoUrlConfig(DaraModel):
    def __init__(
        self,
        alert_config_url: str = None,
        log_url: str = None,
        object_url: str = None,
    ):
        self.alert_config_url = alert_config_url
        self.log_url = log_url
        self.object_url = object_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_config_url is not None:
            result['AlertConfigUrl'] = self.alert_config_url

        if self.log_url is not None:
            result['LogUrl'] = self.log_url

        if self.object_url is not None:
            result['ObjectUrl'] = self.object_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConfigUrl') is not None:
            self.alert_config_url = m.get('AlertConfigUrl')

        if m.get('LogUrl') is not None:
            self.log_url = m.get('LogUrl')

        if m.get('ObjectUrl') is not None:
            self.object_url = m.get('ObjectUrl')

        return self

class GetAlertEventResponseBodyAlertEventInfoBelongProject(DaraModel):
    def __init__(
        self,
        biz_name: str = None,
        project_name: str = None,
    ):
        self.biz_name = biz_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

class GetAlertEventResponseBodyAlertEventInfoAlertReceiverList(DaraModel):
    def __init__(
        self,
        alert_channel_type_list: List[str] = None,
        custom_alert_channel_id_list: List[str] = None,
        on_call_table_name: str = None,
        type: str = None,
        user_list: List[main_models.GetAlertEventResponseBodyAlertEventInfoAlertReceiverListUserList] = None,
    ):
        self.alert_channel_type_list = alert_channel_type_list
        self.custom_alert_channel_id_list = custom_alert_channel_id_list
        self.on_call_table_name = on_call_table_name
        self.type = type
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for v1 in self.user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_channel_type_list is not None:
            result['AlertChannelTypeList'] = self.alert_channel_type_list

        if self.custom_alert_channel_id_list is not None:
            result['CustomAlertChannelIdList'] = self.custom_alert_channel_id_list

        if self.on_call_table_name is not None:
            result['OnCallTableName'] = self.on_call_table_name

        if self.type is not None:
            result['Type'] = self.type

        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertChannelTypeList') is not None:
            self.alert_channel_type_list = m.get('AlertChannelTypeList')

        if m.get('CustomAlertChannelIdList') is not None:
            self.custom_alert_channel_id_list = m.get('CustomAlertChannelIdList')

        if m.get('OnCallTableName') is not None:
            self.on_call_table_name = m.get('OnCallTableName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.GetAlertEventResponseBodyAlertEventInfoAlertReceiverListUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class GetAlertEventResponseBodyAlertEventInfoAlertReceiverListUserList(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetAlertEventResponseBodyAlertEventInfoAlertReason(DaraModel):
    def __init__(
        self,
        alert_reason_param_list: List[main_models.GetAlertEventResponseBodyAlertEventInfoAlertReasonAlertReasonParamList] = None,
        biz_date: str = None,
        type: str = None,
        unique_key: str = None,
    ):
        self.alert_reason_param_list = alert_reason_param_list
        self.biz_date = biz_date
        self.type = type
        self.unique_key = unique_key

    def validate(self):
        if self.alert_reason_param_list:
            for v1 in self.alert_reason_param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertReasonParamList'] = []
        if self.alert_reason_param_list is not None:
            for k1 in self.alert_reason_param_list:
                result['AlertReasonParamList'].append(k1.to_map() if k1 else None)

        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.type is not None:
            result['Type'] = self.type

        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_reason_param_list = []
        if m.get('AlertReasonParamList') is not None:
            for k1 in m.get('AlertReasonParamList'):
                temp_model = main_models.GetAlertEventResponseBodyAlertEventInfoAlertReasonAlertReasonParamList()
                self.alert_reason_param_list.append(temp_model.from_map(k1))

        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')

        return self

class GetAlertEventResponseBodyAlertEventInfoAlertReasonAlertReasonParamList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetAlertEventResponseBodyAlertEventInfoAlertObject(DaraModel):
    def __init__(
        self,
        name: str = None,
        source_system_type: str = None,
        type: str = None,
    ):
        self.name = name
        self.source_system_type = source_system_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.source_system_type is not None:
            result['SourceSystemType'] = self.source_system_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SourceSystemType') is not None:
            self.source_system_type = m.get('SourceSystemType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


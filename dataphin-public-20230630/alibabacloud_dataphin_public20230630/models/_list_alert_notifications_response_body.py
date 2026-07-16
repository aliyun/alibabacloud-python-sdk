# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListAlertNotificationsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list_result: main_models.ListAlertNotificationsResponseBodyListResult = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. A value of OK indicates that the request was successful.
        self.code = code
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The query result.
        self.list_result = list_result
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.list_result:
            self.list_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.list_result is not None:
            result['ListResult'] = self.list_result.to_map()

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('ListResult') is not None:
            temp_model = main_models.ListAlertNotificationsResponseBodyListResult()
            self.list_result = temp_model.from_map(m.get('ListResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAlertNotificationsResponseBodyListResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAlertNotificationsResponseBodyListResultData] = None,
        total_count: int = None,
    ):
        # The list of push records.
        self.data = data
        # The total number of records.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAlertNotificationsResponseBodyListResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAlertNotificationsResponseBodyListResultData(DaraModel):
    def __init__(
        self,
        alert_event_id: str = None,
        alert_object: main_models.ListAlertNotificationsResponseBodyListResultDataAlertObject = None,
        alert_reason: main_models.ListAlertNotificationsResponseBodyListResultDataAlertReason = None,
        alert_receiver: main_models.ListAlertNotificationsResponseBodyListResultDataAlertReceiver = None,
        alert_send: main_models.ListAlertNotificationsResponseBodyListResultDataAlertSend = None,
    ):
        # The alert event ID.
        self.alert_event_id = alert_event_id
        # The alert object.
        self.alert_object = alert_object
        # The alert reason.
        self.alert_reason = alert_reason
        # The receiver information.
        self.alert_receiver = alert_receiver
        # The alert sending information.
        self.alert_send = alert_send

    def validate(self):
        if self.alert_object:
            self.alert_object.validate()
        if self.alert_reason:
            self.alert_reason.validate()
        if self.alert_receiver:
            self.alert_receiver.validate()
        if self.alert_send:
            self.alert_send.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_event_id is not None:
            result['AlertEventId'] = self.alert_event_id

        if self.alert_object is not None:
            result['AlertObject'] = self.alert_object.to_map()

        if self.alert_reason is not None:
            result['AlertReason'] = self.alert_reason.to_map()

        if self.alert_receiver is not None:
            result['AlertReceiver'] = self.alert_receiver.to_map()

        if self.alert_send is not None:
            result['AlertSend'] = self.alert_send.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertEventId') is not None:
            self.alert_event_id = m.get('AlertEventId')

        if m.get('AlertObject') is not None:
            temp_model = main_models.ListAlertNotificationsResponseBodyListResultDataAlertObject()
            self.alert_object = temp_model.from_map(m.get('AlertObject'))

        if m.get('AlertReason') is not None:
            temp_model = main_models.ListAlertNotificationsResponseBodyListResultDataAlertReason()
            self.alert_reason = temp_model.from_map(m.get('AlertReason'))

        if m.get('AlertReceiver') is not None:
            temp_model = main_models.ListAlertNotificationsResponseBodyListResultDataAlertReceiver()
            self.alert_receiver = temp_model.from_map(m.get('AlertReceiver'))

        if m.get('AlertSend') is not None:
            temp_model = main_models.ListAlertNotificationsResponseBodyListResultDataAlertSend()
            self.alert_send = temp_model.from_map(m.get('AlertSend'))

        return self

class ListAlertNotificationsResponseBodyListResultDataAlertSend(DaraModel):
    def __init__(
        self,
        fail_reason: str = None,
        send_content: str = None,
        send_time: str = None,
        status: str = None,
    ):
        # The alert reason.
        self.fail_reason = fail_reason
        # The push content.
        self.send_content = send_content
        # The push time.
        self.send_time = send_time
        # The push status. Valid values:
        # - SUCCESS: Sent successfully.
        # - FAILE: Failed to send.
        # - SENDING: Sending in progress.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        if self.send_content is not None:
            result['SendContent'] = self.send_content

        if self.send_time is not None:
            result['SendTime'] = self.send_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        if m.get('SendContent') is not None:
            self.send_content = m.get('SendContent')

        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListAlertNotificationsResponseBodyListResultDataAlertReceiver(DaraModel):
    def __init__(
        self,
        alert_channel_type: str = None,
        custom_alert_channel_id: str = None,
        on_call_table_id: str = None,
        on_call_table_name: str = None,
        type: str = None,
        user: main_models.ListAlertNotificationsResponseBodyListResultDataAlertReceiverUser = None,
    ):
        # The push channel type. Valid values:
        # - VOICE: phone call.
        # - SMS: text message.
        # - MAIL: email.
        # - DINGTALK_ROBOT: DingTalk robot.
        # - DINGDING: DingTalk work notification.
        # - CUSTOM: custom message channel.
        # - WECHAT: WeCom.
        # - FEISHU: Lark.
        # - SILENCE: do not send.
        self.alert_channel_type = alert_channel_type
        # The custom message channel ID.
        self.custom_alert_channel_id = custom_alert_channel_id
        # The on-call schedule ID.
        self.on_call_table_id = on_call_table_id
        # The on-call schedule name.
        self.on_call_table_name = on_call_table_name
        # The alert receiver type. Valid values:
        # - ON_CALL_TABLE: on-call schedule.
        # - USER_DEFINED: custom user.
        # - OWNER: owner.
        self.type = type
        # The user information.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_channel_type is not None:
            result['AlertChannelType'] = self.alert_channel_type

        if self.custom_alert_channel_id is not None:
            result['CustomAlertChannelId'] = self.custom_alert_channel_id

        if self.on_call_table_id is not None:
            result['OnCallTableId'] = self.on_call_table_id

        if self.on_call_table_name is not None:
            result['OnCallTableName'] = self.on_call_table_name

        if self.type is not None:
            result['Type'] = self.type

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertChannelType') is not None:
            self.alert_channel_type = m.get('AlertChannelType')

        if m.get('CustomAlertChannelId') is not None:
            self.custom_alert_channel_id = m.get('CustomAlertChannelId')

        if m.get('OnCallTableId') is not None:
            self.on_call_table_id = m.get('OnCallTableId')

        if m.get('OnCallTableName') is not None:
            self.on_call_table_name = m.get('OnCallTableName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('User') is not None:
            temp_model = main_models.ListAlertNotificationsResponseBodyListResultDataAlertReceiverUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class ListAlertNotificationsResponseBodyListResultDataAlertReceiverUser(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the alert receiver.
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

class ListAlertNotificationsResponseBodyListResultDataAlertReason(DaraModel):
    def __init__(
        self,
        alert_reason_param_list: List[main_models.ListAlertNotificationsResponseBodyListResultDataAlertReasonAlertReasonParamList] = None,
        biz_date: str = None,
        type: str = None,
        unique_key: str = None,
    ):
        # The list of alert parameters.
        self.alert_reason_param_list = alert_reason_param_list
        # The business date.
        self.biz_date = biz_date
        # The alert reason type. Valid values:
        # - DQE_COLUMN: field rule exception.
        # - DQE_DATA_SOURCE: data source rule exception.
        # - DQE_CUSTOMIZE: custom rule exception.
        # - DQE_TABLE: table rule exception.
        # - DQE_REALTIME_TABLE: real-time table rule exception.
        # - DQE_INDEX: metric rule exception.
        # - OS_AVG_RESPONSE: average response time exception.
        # - OS_CALL_TIMES: call count exception.
        # - OS_ERROR_RATE: error rate exception.
        # - OS_OFFLINE: Offline percentage exception.
        # - STREAM_BIZ_DELAY: business delay too high.
        # - STREAM_DATA_RETENTION: data retention exceeds configuration.
        # - STREAM_MORE_THAN_FAILURE: failure frequency exceeds configuration.
        # - STREAM_TPS_OUT_RANGE: TPS out of range.
        # - STREAM_CHECKPOINT_FAILURE: checkpoint failures exceed configuration.
        # - STREAM_BACKPRESSURE: backpressure duration exceeds configuration.
        # - STREAM_JOB_FAILURE: job execution failed.
        # - VDM_BATCH_ERROR: error.
        # - VDM_BATCH_FINISH: completed.
        # - VDM_BATCH_TIME_OUT: execution timed out.
        # - VDM_BATCH_UNDONE: not completed.
        # - VDM_BATCH_LOGIC_DATA_DELAY: data delay.
        # - QD_DECISION_CALL_TIMES: decision call count exception.
        # - QD_DECISION_MAX_RESPONSE: maximum response time exception.
        # - QD_DECISION_ERROR_RATE: error rate exception.
        # - QD_DECISION_PARAM_COUNT: decision parameter count exception.
        # - QD_DECISION_PARAM_PERCENTAGE: decision parameter percentage exception.
        # - QD_DECISION_PARAM_SUM: decision parameter sum exception.
        # - QD_DECISION_PARAM_AVG: decision parameter average exception.
        # - LOGICAL_INSTANCE_GENERATION: logical instance generation monitoring.
        # - KGB_TASK_ERROR: baseline task error.
        # - KGB_TASK_SLOW_DOWN: baseline task slowdown.
        # - KGB_EARLY_WARNING: baseline early warning.
        # - KGB_BROKEN_LINE: baseline broken line.
        # 
        # And more.
        self.type = type
        # The unique identifier.
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
                temp_model = main_models.ListAlertNotificationsResponseBodyListResultDataAlertReasonAlertReasonParamList()
                self.alert_reason_param_list.append(temp_model.from_map(k1))

        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')

        return self

class ListAlertNotificationsResponseBodyListResultDataAlertReasonAlertReasonParamList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The alert parameter name.
        self.key = key
        # The alert parameter value.
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

class ListAlertNotificationsResponseBodyListResultDataAlertObject(DaraModel):
    def __init__(
        self,
        name: str = None,
        source_system_type: str = None,
        type: str = None,
    ):
        # The object name.
        self.name = name
        # The source system. Valid values:
        # 
        # - ALL: all.
        # - DQE: data quality.
        # - OS: data service.
        # - STREAM: real-time computing.
        # - VDM_BATCH: offline computing.
        # - SOP: O&M platform.
        # - REAL_TIME_PIPELINE: real-time integration.
        # - KGB: baseline monitoring.
        # 
        # And more.
        self.source_system_type = source_system_type
        # The alert object type. Valid values:
        # - OS_API: API operation.
        # - OS_APPLICATION_SERVICE: service application.
        # - STREAM_TASK: real-time computing.
        # - REAL_TIME_PIPELINE_TASK: real-time integration.
        # - VDM_BATCH_SHELL: SHELL.
        # - VDM_BATCH_PYTHON: PYTHON.
        # - VDM_BATCH_DATAX: DATAX.
        # - VDM_BATCH_DLINK: DLINK.
        # - VDM_BATCH_VIRTUAL: VIRTUAL.
        # - VDM_BATCH_PYTHON37: PYTHON37.
        # - VDM_BATCH_PYTHON311: PYTHON311.
        # - VDM_BATCH_MAX_COMPUTE_SQL: MAXCOMPUTE_SQL.
        # - VDM_BATCH_MAX_COMPUTE_MR: MAXCOMPUTE_MR.
        # - VDM_BATCH_SPARK_JAR_ON_MAX_COMPUTE: SPARK_JAR_ON_MAX_COMPUTE.
        # - VDM_BATCH_HIVE_SQL: HIVE_SQL.
        # - VDM_BATCH_HADOOP_MR: HADOOP_MR.
        # - VDM_BATCH_SPARK_JAR_ON_HIVE: SPARK_JAR_ON_HIVE.
        # - VDM_BATCH_SPARK_SQL_ON_HIVE: SPARK_SQL_ON_HIVE.
        # - VDM_BATCH_SPARK_SQL: VDM_BATCH_SPARK_SQL.
        # - DQE_LOGICAL_TABLE: logical table.
        # - DQE_PHYSICAL_TABLE: physical table.
        # - DQE_REALTIME_TABLE: real-time meta table.
        # - DQE_DATA_SOURCE: data source.
        # - DQE_INDEX: metric.
        # - QD_DECISION_INVOKE: QD decision invocation.
        # - BASELINE: baseline.
        # 
        # And more.
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


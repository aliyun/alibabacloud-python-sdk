# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetResourceControlEventResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetResourceControlEventResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data list.
        self.data = data
        # The prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # - **true**: The call was successful.
        # - **false**: The call failed.
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
            temp_model = main_models.GetResourceControlEventResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetResourceControlEventResponseBodyData(DaraModel):
    def __init__(
        self,
        apply_record_list: List[main_models.GetResourceControlEventResponseBodyDataApplyRecordList] = None,
        assistant_tip: str = None,
        block_ip: str = None,
        direction: str = None,
        dst_ip: str = None,
        dst_port: str = None,
        event_id: str = None,
        event_impact: str = None,
        leak_name: str = None,
        protocol: str = None,
        punish_reason: str = None,
        snapshot_url: str = None,
        src_ip: str = None,
        src_port: str = None,
        tip: str = None,
    ):
        # The list of application records.
        self.apply_record_list = apply_record_list
        # The recommended action from the assistant.
        self.assistant_tip = assistant_tip
        # The blocked IP address.
        self.block_ip = block_ip
        # The traffic direction. Valid values:
        # - **in**: inbound to the cloud. 
        # - **out**: outbound from the cloud.
        self.direction = direction
        # The destination IP address.
        self.dst_ip = dst_ip
        # The destination port.
        self.dst_port = dst_port
        # The ID of the alert event.
        self.event_id = event_id
        # The overview of the event impact.
        self.event_impact = event_impact
        # The vulnerability name.
        self.leak_name = leak_name
        # The protocol type.
        self.protocol = protocol
        # The reason for the penalty.
        self.punish_reason = punish_reason
        # The download URL of the penalty snapshot.
        self.snapshot_url = snapshot_url
        # The attack source IP address.
        self.src_ip = src_ip
        # The source port number.
        self.src_port = src_port
        # The recommended action.
        self.tip = tip

    def validate(self):
        if self.apply_record_list:
            for v1 in self.apply_record_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplyRecordList'] = []
        if self.apply_record_list is not None:
            for k1 in self.apply_record_list:
                result['ApplyRecordList'].append(k1.to_map() if k1 else None)

        if self.assistant_tip is not None:
            result['AssistantTip'] = self.assistant_tip

        if self.block_ip is not None:
            result['BlockIp'] = self.block_ip

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_impact is not None:
            result['EventImpact'] = self.event_impact

        if self.leak_name is not None:
            result['LeakName'] = self.leak_name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.punish_reason is not None:
            result['PunishReason'] = self.punish_reason

        if self.snapshot_url is not None:
            result['SnapshotUrl'] = self.snapshot_url

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.src_port is not None:
            result['SrcPort'] = self.src_port

        if self.tip is not None:
            result['Tip'] = self.tip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_record_list = []
        if m.get('ApplyRecordList') is not None:
            for k1 in m.get('ApplyRecordList'):
                temp_model = main_models.GetResourceControlEventResponseBodyDataApplyRecordList()
                self.apply_record_list.append(temp_model.from_map(k1))

        if m.get('AssistantTip') is not None:
            self.assistant_tip = m.get('AssistantTip')

        if m.get('BlockIp') is not None:
            self.block_ip = m.get('BlockIp')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventImpact') is not None:
            self.event_impact = m.get('EventImpact')

        if m.get('LeakName') is not None:
            self.leak_name = m.get('LeakName')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('PunishReason') is not None:
            self.punish_reason = m.get('PunishReason')

        if m.get('SnapshotUrl') is not None:
            self.snapshot_url = m.get('SnapshotUrl')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')

        if m.get('Tip') is not None:
            self.tip = m.get('Tip')

        return self

class GetResourceControlEventResponseBodyDataApplyRecordList(DaraModel):
    def __init__(
        self,
        approval_reason: str = None,
        event_time_record: main_models.GetResourceControlEventResponseBodyDataApplyRecordListEventTimeRecord = None,
        reject_reason: str = None,
        remark: str = None,
        status: str = None,
    ):
        # The reason for approval.
        self.approval_reason = approval_reason
        # The time records related to the application.
        self.event_time_record = event_time_record
        # The reason for rejection.
        self.reject_reason = reject_reason
        # The remarks.
        self.remark = remark
        # The task status. Valid values:
        # 
        # - **Executing**: executing
        # - **Removed**: removed
        # - **Alerting**: alerting
        # - **Ended**: ended
        # - **Processed**: processed by the user and under platform review
        self.status = status

    def validate(self):
        if self.event_time_record:
            self.event_time_record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_reason is not None:
            result['ApprovalReason'] = self.approval_reason

        if self.event_time_record is not None:
            result['EventTimeRecord'] = self.event_time_record.to_map()

        if self.reject_reason is not None:
            result['RejectReason'] = self.reject_reason

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalReason') is not None:
            self.approval_reason = m.get('ApprovalReason')

        if m.get('EventTimeRecord') is not None:
            temp_model = main_models.GetResourceControlEventResponseBodyDataApplyRecordListEventTimeRecord()
            self.event_time_record = temp_model.from_map(m.get('EventTimeRecord'))

        if m.get('RejectReason') is not None:
            self.reject_reason = m.get('RejectReason')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetResourceControlEventResponseBodyDataApplyRecordListEventTimeRecord(DaraModel):
    def __init__(
        self,
        alert_end_time: str = None,
        alert_start_time: str = None,
        anti_punish_time: str = None,
        apply_time: str = None,
        ignore_alert_time: str = None,
        instance_close_time: str = None,
        instance_scan_time: str = None,
        last_check_time: str = None,
        mining_alert_process_time: str = None,
        pre_close_time: str = None,
        process_time: str = None,
        punish_end_time: str = None,
        punish_start_time: str = None,
        reject_time: str = None,
        remove_time: str = None,
        risk_check_success_time: str = None,
    ):
        # The time when the alert ended.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.alert_end_time = alert_end_time
        # The time when the first alert was triggered.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.alert_start_time = alert_start_time
        # The time when the control action was lifted.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.anti_punish_time = anti_punish_time
        # The application time.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.apply_time = apply_time
        # The time when the alert was ignored.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.ignore_alert_time = ignore_alert_time
        # The time when the instance was shut down.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.instance_close_time = instance_close_time
        # The time when the instance was scanned.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.instance_scan_time = instance_scan_time
        # The time of the latest detection.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.last_check_time = last_check_time
        # The time when the mining alert was processed.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.mining_alert_process_time = mining_alert_process_time
        # The estimated shutdown time.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.pre_close_time = pre_close_time
        # The processing time.
        # 
        # > Format: yyyy-MM-dd HH:mm:ss
        self.process_time = process_time
        # The time when the control action ended.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.punish_end_time = punish_end_time
        # The time when the control action started.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.punish_start_time = punish_start_time
        # The rejection time.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.reject_time = reject_time
        # The removal time.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.remove_time = remove_time
        # The time when the risk check succeeded.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.risk_check_success_time = risk_check_success_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_end_time is not None:
            result['AlertEndTime'] = self.alert_end_time

        if self.alert_start_time is not None:
            result['AlertStartTime'] = self.alert_start_time

        if self.anti_punish_time is not None:
            result['AntiPunishTime'] = self.anti_punish_time

        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        if self.ignore_alert_time is not None:
            result['IgnoreAlertTime'] = self.ignore_alert_time

        if self.instance_close_time is not None:
            result['InstanceCloseTime'] = self.instance_close_time

        if self.instance_scan_time is not None:
            result['InstanceScanTime'] = self.instance_scan_time

        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        if self.mining_alert_process_time is not None:
            result['MiningAlertProcessTime'] = self.mining_alert_process_time

        if self.pre_close_time is not None:
            result['PreCloseTime'] = self.pre_close_time

        if self.process_time is not None:
            result['ProcessTime'] = self.process_time

        if self.punish_end_time is not None:
            result['PunishEndTime'] = self.punish_end_time

        if self.punish_start_time is not None:
            result['PunishStartTime'] = self.punish_start_time

        if self.reject_time is not None:
            result['RejectTime'] = self.reject_time

        if self.remove_time is not None:
            result['RemoveTime'] = self.remove_time

        if self.risk_check_success_time is not None:
            result['RiskCheckSuccessTime'] = self.risk_check_success_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertEndTime') is not None:
            self.alert_end_time = m.get('AlertEndTime')

        if m.get('AlertStartTime') is not None:
            self.alert_start_time = m.get('AlertStartTime')

        if m.get('AntiPunishTime') is not None:
            self.anti_punish_time = m.get('AntiPunishTime')

        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        if m.get('IgnoreAlertTime') is not None:
            self.ignore_alert_time = m.get('IgnoreAlertTime')

        if m.get('InstanceCloseTime') is not None:
            self.instance_close_time = m.get('InstanceCloseTime')

        if m.get('InstanceScanTime') is not None:
            self.instance_scan_time = m.get('InstanceScanTime')

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('MiningAlertProcessTime') is not None:
            self.mining_alert_process_time = m.get('MiningAlertProcessTime')

        if m.get('PreCloseTime') is not None:
            self.pre_close_time = m.get('PreCloseTime')

        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')

        if m.get('PunishEndTime') is not None:
            self.punish_end_time = m.get('PunishEndTime')

        if m.get('PunishStartTime') is not None:
            self.punish_start_time = m.get('PunishStartTime')

        if m.get('RejectTime') is not None:
            self.reject_time = m.get('RejectTime')

        if m.get('RemoveTime') is not None:
            self.remove_time = m.get('RemoveTime')

        if m.get('RiskCheckSuccessTime') is not None:
            self.risk_check_success_time = m.get('RiskCheckSuccessTime')

        return self


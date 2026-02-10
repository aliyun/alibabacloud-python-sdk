# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainSecureAlarmListResponseBody(DaraModel):
    def __init__(
        self,
        alarm_list: List[main_models.DescribeDomainSecureAlarmListResponseBodyAlarmList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The security alerts in your website assets.
        self.alarm_list = alarm_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.alarm_list:
            for v1 in self.alarm_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlarmList'] = []
        if self.alarm_list is not None:
            for k1 in self.alarm_list:
                result['AlarmList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_list = []
        if m.get('AlarmList') is not None:
            for k1 in m.get('AlarmList'):
                temp_model = main_models.DescribeDomainSecureAlarmListResponseBodyAlarmList()
                self.alarm_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDomainSecureAlarmListResponseBodyAlarmList(DaraModel):
    def __init__(
        self,
        alarm_event_name: str = None,
        alarm_event_name_original: str = None,
        alarm_event_type: str = None,
        alarm_unique_info: str = None,
        auto_breaking: bool = None,
        can_be_deal_on_line: bool = None,
        can_cancel_fault: bool = None,
        contain_hw_mode: bool = None,
        data_source: str = None,
        dealed: bool = None,
        description: str = None,
        end_time: int = None,
        gmt_modified: int = None,
        has_trace_info: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        level: str = None,
        operate_error_code: str = None,
        operate_time: int = None,
        sale_version: str = None,
        security_event_ids: str = None,
        solution: str = None,
        stages: str = None,
        start_time: int = None,
        suspicious_event_count: int = None,
        uuid: str = None,
    ):
        # The name of the alert event.
        self.alarm_event_name = alarm_event_name
        # The original parent name of the alert event.
        self.alarm_event_name_original = alarm_event_name_original
        # The type of the alert event.
        self.alarm_event_type = alarm_event_type
        # The unique ID of the alert event.
        self.alarm_unique_info = alarm_unique_info
        # Indicates whether automatic defense is enabled.
        self.auto_breaking = auto_breaking
        # Indicates whether the alert event can be handled online, such as quarantining the source file of the malicious process, adding the alert event to the whitelist, and ignoring the alert event. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.can_be_deal_on_line = can_be_deal_on_line
        # Indicates whether you can cancel marking the alert event as a false positive. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.can_cancel_fault = can_cancel_fault
        # Indicates whether the safeguard mode for major activities is supported.
        self.contain_hw_mode = contain_hw_mode
        # The data source of the alert event.
        self.data_source = data_source
        # Indicates whether the alert event is handled. Valid values:
        # 
        # *   **N**: unhandled
        # *   **Y**: handled
        self.dealed = dealed
        # The description of the alert event.
        self.description = description
        # The timestamp generated when the alert event was last detected. Unit: milliseconds.
        self.end_time = end_time
        # The time of the last modification.
        self.gmt_modified = gmt_modified
        # Indicates whether the alert event has tracing information. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.has_trace_info = has_trace_info
        # The instance ID of the affected asset.
        self.instance_id = instance_id
        # The instance name of the affected asset.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the affected instance.
        self.intranet_ip = intranet_ip
        # The risk level of the alert event. Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
        self.level = level
        # The handling result code of the alert event.
        self.operate_error_code = operate_error_code
        # The timestamp generated when the alert event was handled. Unit: milliseconds.
        self.operate_time = operate_time
        # The edition of Security Center in which the alert event can be detected. Valid values:
        # 
        # *   **0**: Basic edition.
        # *   **1**: Advanced edition.
        # *   **2**: Enterprise edition.
        self.sale_version = sale_version
        # The ID of the associated alert event.
        self.security_event_ids = security_event_ids
        # The solution to the alert event.
        self.solution = solution
        # The stage at which the attack or intrusion is detected.
        self.stages = stages
        # The timestamp generated when the alert event was first detected. Unit: milliseconds.
        self.start_time = start_time
        # The total number of security alerts in your website assets.
        self.suspicious_event_count = suspicious_event_count
        # The unique ID of the associated instance.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name

        if self.alarm_event_name_original is not None:
            result['AlarmEventNameOriginal'] = self.alarm_event_name_original

        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type

        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info

        if self.auto_breaking is not None:
            result['AutoBreaking'] = self.auto_breaking

        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line

        if self.can_cancel_fault is not None:
            result['CanCancelFault'] = self.can_cancel_fault

        if self.contain_hw_mode is not None:
            result['ContainHwMode'] = self.contain_hw_mode

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.has_trace_info is not None:
            result['HasTraceInfo'] = self.has_trace_info

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.level is not None:
            result['Level'] = self.level

        if self.operate_error_code is not None:
            result['OperateErrorCode'] = self.operate_error_code

        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time

        if self.sale_version is not None:
            result['SaleVersion'] = self.sale_version

        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids

        if self.solution is not None:
            result['Solution'] = self.solution

        if self.stages is not None:
            result['Stages'] = self.stages

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.suspicious_event_count is not None:
            result['SuspiciousEventCount'] = self.suspicious_event_count

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')

        if m.get('AlarmEventNameOriginal') is not None:
            self.alarm_event_name_original = m.get('AlarmEventNameOriginal')

        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')

        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')

        if m.get('AutoBreaking') is not None:
            self.auto_breaking = m.get('AutoBreaking')

        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')

        if m.get('CanCancelFault') is not None:
            self.can_cancel_fault = m.get('CanCancelFault')

        if m.get('ContainHwMode') is not None:
            self.contain_hw_mode = m.get('ContainHwMode')

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HasTraceInfo') is not None:
            self.has_trace_info = m.get('HasTraceInfo')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('OperateErrorCode') is not None:
            self.operate_error_code = m.get('OperateErrorCode')

        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')

        if m.get('SaleVersion') is not None:
            self.sale_version = m.get('SaleVersion')

        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        if m.get('Stages') is not None:
            self.stages = m.get('Stages')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SuspiciousEventCount') is not None:
            self.suspicious_event_count = m.get('SuspiciousEventCount')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self


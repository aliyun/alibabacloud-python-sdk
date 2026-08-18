# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class QueryResourceControlEventsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryResourceControlEventsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The metadata returned.
        self.data = data
        # The description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = main_models.QueryResourceControlEventsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryResourceControlEventsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryResourceControlEventsResponseBodyDataList] = None,
        page_info: main_models.QueryResourceControlEventsResponseBodyDataPageInfo = None,
    ):
        # The event list data.
        self.list = list
        # The pagination information.
        self.page_info = page_info

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryResourceControlEventsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.QueryResourceControlEventsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        return self

class QueryResourceControlEventsResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The current page number.
        self.current = current
        # The number of records returned per page.
        self.page_size = page_size
        # The total number of events.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['Current'] = self.current

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryResourceControlEventsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        action_code: str = None,
        action_name: str = None,
        alert_end_time: str = None,
        alert_start_time: str = None,
        anti_punish_time: str = None,
        apply_record_count: int = None,
        apply_status: str = None,
        apply_trial: bool = None,
        business_name: str = None,
        case_code: str = None,
        domain: str = None,
        event_id: str = None,
        event_name: str = None,
        extras: str = None,
        form_type: str = None,
        gmt_latest: str = None,
        instance_id: str = None,
        ip: str = None,
        last_check_time: str = None,
        pre_close_time: str = None,
        punish_from: str = None,
        punish_time: str = None,
        reason: str = None,
        region: str = None,
        region_id: str = None,
        reinforcement: str = None,
        status: str = None,
        support_batch_apply: bool = None,
        support_single_apply: bool = None,
        trigger_type: str = None,
        url: str = None,
    ):
        # The action code.
        self.action_code = action_code
        # The action name.
        self.action_name = action_name
        # The alert end time.
        self.alert_end_time = alert_end_time
        # The first alert time.
        self.alert_start_time = alert_start_time
        # The time when the control action was released.
        self.anti_punish_time = anti_punish_time
        # The number of unblock application records.
        self.apply_record_count = apply_record_count
        # The application status.
        # 
        # Valid values:
        # 
        # - **AUDIT**: Under review.
        # - **SUCCESS**: Approved.
        # - **FAIL**: Rejected.
        self.apply_status = apply_status
        # Indicates whether the unblock application is processed through the review platform.
        self.apply_trial = apply_trial
        # The product type name.
        self.business_name = business_name
        # The event name code.
        self.case_code = case_code
        # The controlled domain name.
        self.domain = domain
        # The event ID.
        self.event_id = event_id
        # The event name.
        self.event_name = event_name
        # The extended information about the penalty.
        self.extras = extras
        # The event type.
        self.form_type = form_type
        # The latest time.
        self.gmt_latest = gmt_latest
        # The instance ID.
        self.instance_id = instance_id
        # The controlled IP address.
        self.ip = ip
        # The latest detection time.
        self.last_check_time = last_check_time
        # The estimated shutdown time.
        self.pre_close_time = pre_close_time
        # The source of the penalty.
        self.punish_from = punish_from
        # The time when the control action was applied.
        self.punish_time = punish_time
        # The event reason.
        self.reason = reason
        # The region information.
        self.region = region
        # The region ID.
        self.region_id = region_id
        # The security hardening suggestion.
        self.reinforcement = reinforcement
        # The task status.
        # 
        # - **Executing**: executing
        # - **Removed**: removed
        # - **Alerting**: alerting
        # - **Ended**: ended
        # - **Processed**: processed by the user and under platform review
        self.status = status
        # Indicates whether batch unblock applications are supported.
        self.support_batch_apply = support_batch_apply
        # Indicates whether a single unblock application is supported.
        self.support_single_apply = support_single_apply
        # The trigger type.
        self.trigger_type = trigger_type
        # The controlled URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_code is not None:
            result['ActionCode'] = self.action_code

        if self.action_name is not None:
            result['ActionName'] = self.action_name

        if self.alert_end_time is not None:
            result['AlertEndTime'] = self.alert_end_time

        if self.alert_start_time is not None:
            result['AlertStartTime'] = self.alert_start_time

        if self.anti_punish_time is not None:
            result['AntiPunishTime'] = self.anti_punish_time

        if self.apply_record_count is not None:
            result['ApplyRecordCount'] = self.apply_record_count

        if self.apply_status is not None:
            result['ApplyStatus'] = self.apply_status

        if self.apply_trial is not None:
            result['ApplyTrial'] = self.apply_trial

        if self.business_name is not None:
            result['BusinessName'] = self.business_name

        if self.case_code is not None:
            result['CaseCode'] = self.case_code

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.extras is not None:
            result['Extras'] = self.extras

        if self.form_type is not None:
            result['FormType'] = self.form_type

        if self.gmt_latest is not None:
            result['GmtLatest'] = self.gmt_latest

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        if self.pre_close_time is not None:
            result['PreCloseTime'] = self.pre_close_time

        if self.punish_from is not None:
            result['PunishFrom'] = self.punish_from

        if self.punish_time is not None:
            result['PunishTime'] = self.punish_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reinforcement is not None:
            result['Reinforcement'] = self.reinforcement

        if self.status is not None:
            result['Status'] = self.status

        if self.support_batch_apply is not None:
            result['SupportBatchApply'] = self.support_batch_apply

        if self.support_single_apply is not None:
            result['SupportSingleApply'] = self.support_single_apply

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')

        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        if m.get('AlertEndTime') is not None:
            self.alert_end_time = m.get('AlertEndTime')

        if m.get('AlertStartTime') is not None:
            self.alert_start_time = m.get('AlertStartTime')

        if m.get('AntiPunishTime') is not None:
            self.anti_punish_time = m.get('AntiPunishTime')

        if m.get('ApplyRecordCount') is not None:
            self.apply_record_count = m.get('ApplyRecordCount')

        if m.get('ApplyStatus') is not None:
            self.apply_status = m.get('ApplyStatus')

        if m.get('ApplyTrial') is not None:
            self.apply_trial = m.get('ApplyTrial')

        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')

        if m.get('CaseCode') is not None:
            self.case_code = m.get('CaseCode')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('Extras') is not None:
            self.extras = m.get('Extras')

        if m.get('FormType') is not None:
            self.form_type = m.get('FormType')

        if m.get('GmtLatest') is not None:
            self.gmt_latest = m.get('GmtLatest')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('PreCloseTime') is not None:
            self.pre_close_time = m.get('PreCloseTime')

        if m.get('PunishFrom') is not None:
            self.punish_from = m.get('PunishFrom')

        if m.get('PunishTime') is not None:
            self.punish_time = m.get('PunishTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Reinforcement') is not None:
            self.reinforcement = m.get('Reinforcement')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportBatchApply') is not None:
            self.support_batch_apply = m.get('SupportBatchApply')

        if m.get('SupportSingleApply') is not None:
            self.support_single_apply = m.get('SupportSingleApply')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self


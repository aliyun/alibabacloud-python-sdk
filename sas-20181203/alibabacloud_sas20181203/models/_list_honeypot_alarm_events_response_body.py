# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListHoneypotAlarmEventsResponseBody(DaraModel):
    def __init__(
        self,
        honeypot_alarm_events: List[main_models.ListHoneypotAlarmEventsResponseBodyHoneypotAlarmEvents] = None,
        page_info: main_models.ListHoneypotAlarmEventsResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The alert events.
        self.honeypot_alarm_events = honeypot_alarm_events
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.honeypot_alarm_events:
            for v1 in self.honeypot_alarm_events:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HoneypotAlarmEvents'] = []
        if self.honeypot_alarm_events is not None:
            for k1 in self.honeypot_alarm_events:
                result['HoneypotAlarmEvents'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.honeypot_alarm_events = []
        if m.get('HoneypotAlarmEvents') is not None:
            for k1 in m.get('HoneypotAlarmEvents'):
                temp_model = main_models.ListHoneypotAlarmEventsResponseBodyHoneypotAlarmEvents()
                self.honeypot_alarm_events.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListHoneypotAlarmEventsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListHoneypotAlarmEventsResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: 100.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHoneypotAlarmEventsResponseBodyHoneypotAlarmEvents(DaraModel):
    def __init__(
        self,
        alarm_event_id: int = None,
        alarm_event_name: str = None,
        alarm_event_type: str = None,
        alarm_unique_info: str = None,
        event_count: int = None,
        first_time: int = None,
        last_time: int = None,
        merge_field_list: List[main_models.ListHoneypotAlarmEventsResponseBodyHoneypotAlarmEventsMergeFieldList] = None,
        operate_status: int = None,
        risk_level: str = None,
    ):
        # The event ID.
        self.alarm_event_id = alarm_event_id
        # The name of the alert event.
        self.alarm_event_name = alarm_event_name
        # The type of the alert event.
        self.alarm_event_type = alarm_event_type
        # The unique identifier of the alert event.
        self.alarm_unique_info = alarm_unique_info
        # The total number of times that the alert event was generated.
        self.event_count = event_count
        # The timestamp that indicates the time when the alert event was first detected. Unit: milliseconds.
        self.first_time = first_time
        # The timestamp that indicates the time when the alert event was last detected. Unit: milliseconds.
        self.last_time = last_time
        # The risk information.
        self.merge_field_list = merge_field_list
        # The handling status of the alert event. Valid values:
        # 
        # *   **1**: pending
        # *   **2**: ignored
        # *   **4**: confirmed
        self.operate_status = operate_status
        # The risk level. Valid values:
        # 
        # *   **2**: low
        # *   **3**: medium
        # *   **4**: high
        self.risk_level = risk_level

    def validate(self):
        if self.merge_field_list:
            for v1 in self.merge_field_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_event_id is not None:
            result['AlarmEventId'] = self.alarm_event_id

        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name

        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type

        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info

        if self.event_count is not None:
            result['EventCount'] = self.event_count

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        result['MergeFieldList'] = []
        if self.merge_field_list is not None:
            for k1 in self.merge_field_list:
                result['MergeFieldList'].append(k1.to_map() if k1 else None)

        if self.operate_status is not None:
            result['OperateStatus'] = self.operate_status

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventId') is not None:
            self.alarm_event_id = m.get('AlarmEventId')

        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')

        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')

        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')

        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        self.merge_field_list = []
        if m.get('MergeFieldList') is not None:
            for k1 in m.get('MergeFieldList'):
                temp_model = main_models.ListHoneypotAlarmEventsResponseBodyHoneypotAlarmEventsMergeFieldList()
                self.merge_field_list.append(temp_model.from_map(k1))

        if m.get('OperateStatus') is not None:
            self.operate_status = m.get('OperateStatus')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class ListHoneypotAlarmEventsResponseBodyHoneypotAlarmEventsMergeFieldList(DaraModel):
    def __init__(
        self,
        field_ext_info: str = None,
        field_key: str = None,
        field_type: str = None,
        field_value: str = None,
    ):
        # The extended value that corresponds to the field key.
        self.field_ext_info = field_ext_info
        # The key of the field.
        self.field_key = field_key
        # The type of the field. You can ignore this internal parameter.
        self.field_type = field_type
        # The value that corresponds to the field key.
        self.field_value = field_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_ext_info is not None:
            result['FieldExtInfo'] = self.field_ext_info

        if self.field_key is not None:
            result['FieldKey'] = self.field_key

        if self.field_type is not None:
            result['FieldType'] = self.field_type

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldExtInfo') is not None:
            self.field_ext_info = m.get('FieldExtInfo')

        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')

        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        return self


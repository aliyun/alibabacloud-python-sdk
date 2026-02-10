# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListHoneypotEventsResponseBody(DaraModel):
    def __init__(
        self,
        honeypot_events: List[main_models.ListHoneypotEventsResponseBodyHoneypotEvents] = None,
        page_info: main_models.ListHoneypotEventsResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The intrusion events.
        self.honeypot_events = honeypot_events
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.honeypot_events:
            for v1 in self.honeypot_events:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HoneypotEvents'] = []
        if self.honeypot_events is not None:
            for k1 in self.honeypot_events:
                result['HoneypotEvents'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.honeypot_events = []
        if m.get('HoneypotEvents') is not None:
            for k1 in m.get('HoneypotEvents'):
                temp_model = main_models.ListHoneypotEventsResponseBodyHoneypotEvents()
                self.honeypot_events.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListHoneypotEventsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListHoneypotEventsResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        last_row_key: str = None,
        next_token: str = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The key of the last data entry.
        self.last_row_key = last_row_key
        # The value of the NextToken parameter that is returned by using the NextToken method.
        self.next_token = next_token
        # The number of entries per page.
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

        if self.last_row_key is not None:
            result['LastRowKey'] = self.last_row_key

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('LastRowKey') is not None:
            self.last_row_key = m.get('LastRowKey')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHoneypotEventsResponseBodyHoneypotEvents(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        alarm_event_id: int = None,
        dst_ip: str = None,
        first_time: int = None,
        honeypot_name: str = None,
        last_time: int = None,
        location: str = None,
        merge_field_list: List[main_models.ListHoneypotEventsResponseBodyHoneypotEventsMergeFieldList] = None,
        protocol: str = None,
        risk_level: str = None,
        security_event_id: int = None,
        src_ip: str = None,
    ):
        # The probe ID.
        self.agent_id = agent_id
        # The name of the probe.
        self.agent_name = agent_name
        # The ID of the alert event.
        self.alarm_event_id = alarm_event_id
        # The destination IP address of the attack.
        self.dst_ip = dst_ip
        # The timestamp at which the event was first detected.
        self.first_time = first_time
        # The name of the honeypot.
        self.honeypot_name = honeypot_name
        # The timestamp at which the event was last detected.
        self.last_time = last_time
        # The region.
        self.location = location
        # The extended values that correspond to the field key.
        self.merge_field_list = merge_field_list
        # The protocol. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.protocol = protocol
        # The risk level. Valid values:
        # 
        # *   **2**: low
        # *   **3**: medium
        # *   **4**: high
        self.risk_level = risk_level
        # The ID of the intrusion event.
        self.security_event_id = security_event_id
        # The source IP address of the attack.
        self.src_ip = src_ip

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
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.alarm_event_id is not None:
            result['AlarmEventId'] = self.alarm_event_id

        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.honeypot_name is not None:
            result['HoneypotName'] = self.honeypot_name

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.location is not None:
            result['Location'] = self.location

        result['MergeFieldList'] = []
        if self.merge_field_list is not None:
            for k1 in self.merge_field_list:
                result['MergeFieldList'].append(k1.to_map() if k1 else None)

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AlarmEventId') is not None:
            self.alarm_event_id = m.get('AlarmEventId')

        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('HoneypotName') is not None:
            self.honeypot_name = m.get('HoneypotName')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        self.merge_field_list = []
        if m.get('MergeFieldList') is not None:
            for k1 in m.get('MergeFieldList'):
                temp_model = main_models.ListHoneypotEventsResponseBodyHoneypotEventsMergeFieldList()
                self.merge_field_list.append(temp_model.from_map(k1))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        return self

class ListHoneypotEventsResponseBodyHoneypotEventsMergeFieldList(DaraModel):
    def __init__(
        self,
        field_ext_info: str = None,
        field_key: str = None,
        field_type: str = None,
        field_value: str = None,
    ):
        # The supplementary information about the field.
        self.field_ext_info = field_ext_info
        # The key of the field.
        self.field_key = field_key
        # The type of the field.
        self.field_type = field_type
        # The value of the field key.
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


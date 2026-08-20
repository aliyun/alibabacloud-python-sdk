# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class QueryAccountSafetyIncidentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryAccountSafetyIncidentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # > 200: success. Other values (such as 500 or 400): error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**
        # - **false**
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
            temp_model = main_models.QueryAccountSafetyIncidentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAccountSafetyIncidentResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryAccountSafetyIncidentResponseBodyDataList] = None,
        page_info: main_models.QueryAccountSafetyIncidentResponseBodyDataPageInfo = None,
    ):
        # The event data.
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
                temp_model = main_models.QueryAccountSafetyIncidentResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.QueryAccountSafetyIncidentResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        return self

class QueryAccountSafetyIncidentResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current: str = None,
        page_size: str = None,
        total: str = None,
    ):
        # The current page number.
        self.current = current
        # The number of assets displayed on each page in a paging query.
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

class QueryAccountSafetyIncidentResponseBodyDataList(DaraModel):
    def __init__(
        self,
        action_code: str = None,
        action_name: str = None,
        anti_punish_time: str = None,
        call_api: str = None,
        date_extras: main_models.QueryAccountSafetyIncidentResponseBodyDataListDateExtras = None,
        event_id: str = None,
        event_impact: str = None,
        event_name: str = None,
        event_reason: str = None,
        event_type: str = None,
        exception_call_time: str = None,
        exception_ip: str = None,
        punish_time: str = None,
        reinforcement: str = None,
        resource_id: str = None,
        resource_type: str = None,
        status: str = None,
        tip: str = None,
        user_guide_name: str = None,
        user_guide_url: str = None,
    ):
        # The control action name code.
        self.action_code = action_code
        # The control action name.
        self.action_name = action_name
        # The control removal time.
        # 
        # > Format: yyyy-MM-dd HH:mm:ss
        self.anti_punish_time = anti_punish_time
        # The called API operation.
        self.call_api = call_api
        # The control time information.
        self.date_extras = date_extras
        # The event ID.
        self.event_id = event_id
        # The event impact.
        self.event_impact = event_impact
        # The control event name.
        self.event_name = event_name
        # The event reason.
        self.event_reason = event_reason
        # The event subtype name.
        self.event_type = event_type
        # The exception call time.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.exception_call_time = exception_call_time
        # The exception IP address.
        self.exception_ip = exception_ip
        # The control start time.
        # 
        # > Format: yyyy-MM-dd HH:mm:ss
        self.punish_time = punish_time
        # The hardening suggestion.
        self.reinforcement = reinforcement
        # The cloud resource ID.
        self.resource_id = resource_id
        # The control object type.
        self.resource_type = resource_type
        # The event status. Valid values:
        # 
        # - **Executing**: In progress.
        # - **Removed**: Removed.
        # - **Alerting**: Alerting.
        # - **Ended**: Ended.
        self.status = status
        # The handling suggestion.
        self.tip = tip
        # The help topic name.
        self.user_guide_name = user_guide_name
        # The help topic URL.
        self.user_guide_url = user_guide_url

    def validate(self):
        if self.date_extras:
            self.date_extras.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_code is not None:
            result['ActionCode'] = self.action_code

        if self.action_name is not None:
            result['ActionName'] = self.action_name

        if self.anti_punish_time is not None:
            result['AntiPunishTime'] = self.anti_punish_time

        if self.call_api is not None:
            result['CallApi'] = self.call_api

        if self.date_extras is not None:
            result['DateExtras'] = self.date_extras.to_map()

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_impact is not None:
            result['EventImpact'] = self.event_impact

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_reason is not None:
            result['EventReason'] = self.event_reason

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.exception_call_time is not None:
            result['ExceptionCallTime'] = self.exception_call_time

        if self.exception_ip is not None:
            result['ExceptionIp'] = self.exception_ip

        if self.punish_time is not None:
            result['PunishTime'] = self.punish_time

        if self.reinforcement is not None:
            result['Reinforcement'] = self.reinforcement

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tip is not None:
            result['Tip'] = self.tip

        if self.user_guide_name is not None:
            result['UserGuideName'] = self.user_guide_name

        if self.user_guide_url is not None:
            result['UserGuideUrl'] = self.user_guide_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')

        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        if m.get('AntiPunishTime') is not None:
            self.anti_punish_time = m.get('AntiPunishTime')

        if m.get('CallApi') is not None:
            self.call_api = m.get('CallApi')

        if m.get('DateExtras') is not None:
            temp_model = main_models.QueryAccountSafetyIncidentResponseBodyDataListDateExtras()
            self.date_extras = temp_model.from_map(m.get('DateExtras'))

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventImpact') is not None:
            self.event_impact = m.get('EventImpact')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventReason') is not None:
            self.event_reason = m.get('EventReason')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('ExceptionCallTime') is not None:
            self.exception_call_time = m.get('ExceptionCallTime')

        if m.get('ExceptionIp') is not None:
            self.exception_ip = m.get('ExceptionIp')

        if m.get('PunishTime') is not None:
            self.punish_time = m.get('PunishTime')

        if m.get('Reinforcement') is not None:
            self.reinforcement = m.get('Reinforcement')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tip') is not None:
            self.tip = m.get('Tip')

        if m.get('UserGuideName') is not None:
            self.user_guide_name = m.get('UserGuideName')

        if m.get('UserGuideUrl') is not None:
            self.user_guide_url = m.get('UserGuideUrl')

        return self

class QueryAccountSafetyIncidentResponseBodyDataListDateExtras(DaraModel):
    def __init__(
        self,
        alert_end_time: str = None,
        alert_start_time: str = None,
        last_check_time: str = None,
    ):
        # The alert end time.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.alert_end_time = alert_end_time
        # The first alert time.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.alert_start_time = alert_start_time
        # The latest detection time.
        # > Format: yyyy-MM-dd HH:mm:ss
        self.last_check_time = last_check_time

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

        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertEndTime') is not None:
            self.alert_end_time = m.get('AlertEndTime')

        if m.get('AlertStartTime') is not None:
            self.alert_start_time = m.get('AlertStartTime')

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        return self


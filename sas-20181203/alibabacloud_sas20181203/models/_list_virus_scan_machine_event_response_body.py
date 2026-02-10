# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListVirusScanMachineEventResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListVirusScanMachineEventResponseBodyData] = None,
        page_info: main_models.ListVirusScanMachineEventResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The details of the alert event.
        self.data = data
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListVirusScanMachineEventResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListVirusScanMachineEventResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListVirusScanMachineEventResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListVirusScanMachineEventResponseBodyData(DaraModel):
    def __init__(
        self,
        details: List[main_models.ListVirusScanMachineEventResponseBodyDataDetails] = None,
        event_id: int = None,
        event_name: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        last_time_stamp: int = None,
        level: str = None,
    ):
        # The details of the exception.
        self.details = details
        # The ID of the alert event.
        self.event_id = event_id
        # The name of the alert event. The value indicates a subtype.
        self.event_name = event_name
        # The name of the instance.
        self.instance_name = instance_name
        # The public IP address.
        self.internet_ip = internet_ip
        # The private IP address.
        self.intranet_ip = intranet_ip
        # The timestamp when the alert event was last generated. Unit: milliseconds.
        self.last_time_stamp = last_time_stamp
        # The risk level of the alert event. Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
        self.level = level

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.ListVirusScanMachineEventResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

class ListVirusScanMachineEventResponseBodyDataDetails(DaraModel):
    def __init__(
        self,
        info_type: str = None,
        name_display: str = None,
        type: str = None,
        value_display: str = None,
    ):
        # The display type of the value for ValueDisplay. Valid value:
        # 
        # *   **download_url**, which indicates a download URL.
        self.info_type = info_type
        # The display name of the alert event.
        self.name_display = name_display
        # The format in which the details of the exception are displayed.
        # 
        # Valid values:
        # 
        # *   **text**
        # *   **html**
        self.type = type
        # The attribute information about the exception. The information includes the logon time or location of an alert triggered by an unusual logon, and the trojan file path or trojan type of an alert.
        self.value_display = value_display

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_type is not None:
            result['InfoType'] = self.info_type

        if self.name_display is not None:
            result['NameDisplay'] = self.name_display

        if self.type is not None:
            result['Type'] = self.type

        if self.value_display is not None:
            result['ValueDisplay'] = self.value_display

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')

        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueDisplay') is not None:
            self.value_display = m.get('ValueDisplay')

        return self


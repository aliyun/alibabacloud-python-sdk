# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class ListVirusScanMachineEventResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListVirusScanMachineEventResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.ListVirusScanMachineEventResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListVirusScanMachineEventResponseBodyData(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        virus_scan_latest_task_statistic: main_models.ListVirusScanMachineEventResponseBodyDataVirusScanLatestTaskStatistic = None,
        virus_scan_machine_event_list: main_models.ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventList = None,
    ):
        self.request_id = request_id
        self.virus_scan_latest_task_statistic = virus_scan_latest_task_statistic
        self.virus_scan_machine_event_list = virus_scan_machine_event_list

    def validate(self):
        if self.virus_scan_latest_task_statistic:
            self.virus_scan_latest_task_statistic.validate()
        if self.virus_scan_machine_event_list:
            self.virus_scan_machine_event_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.virus_scan_latest_task_statistic is not None:
            result['VirusScanLatestTaskStatistic'] = self.virus_scan_latest_task_statistic.to_map()

        if self.virus_scan_machine_event_list is not None:
            result['VirusScanMachineEventList'] = self.virus_scan_machine_event_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VirusScanLatestTaskStatistic') is not None:
            temp_model = main_models.ListVirusScanMachineEventResponseBodyDataVirusScanLatestTaskStatistic()
            self.virus_scan_latest_task_statistic = temp_model.from_map(m.get('VirusScanLatestTaskStatistic'))

        if m.get('VirusScanMachineEventList') is not None:
            temp_model = main_models.ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventList()
            self.virus_scan_machine_event_list = temp_model.from_map(m.get('VirusScanMachineEventList'))

        return self

class ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventList(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventListData] = None,
        page_info: main_models.ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventListPageInfo = None,
    ):
        self.data = data
        self.page_info = page_info

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventListData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventListPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        return self

class ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventListPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
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

class ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventListData(DaraModel):
    def __init__(
        self,
        details: List[main_models.ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventListDataDetails] = None,
        event_id: int = None,
        event_name: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        last_time_stamp: int = None,
        level: str = None,
    ):
        self.details = details
        self.event_id = event_id
        self.event_name = event_name
        self.instance_name = instance_name
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.last_time_stamp = last_time_stamp
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
                temp_model = main_models.ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventListDataDetails()
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

class ListVirusScanMachineEventResponseBodyDataVirusScanMachineEventListDataDetails(DaraModel):
    def __init__(
        self,
        info_type: str = None,
        name_display: str = None,
        type: str = None,
        value_display: str = None,
    ):
        self.info_type = info_type
        self.name_display = name_display
        self.type = type
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

class ListVirusScanMachineEventResponseBodyDataVirusScanLatestTaskStatistic(DaraModel):
    def __init__(
        self,
        complete_machine: int = None,
        machine_name: str = None,
        progress: str = None,
        risk_level: str = None,
        safe_machine: int = None,
        scan_machine: int = None,
        scan_path: List[str] = None,
        scan_time: int = None,
        scan_type: str = None,
        status: int = None,
        suspicious_count: int = None,
        suspicious_machine: int = None,
        task_id: str = None,
        un_complete_machine: int = None,
    ):
        self.complete_machine = complete_machine
        self.machine_name = machine_name
        self.progress = progress
        self.risk_level = risk_level
        self.safe_machine = safe_machine
        self.scan_machine = scan_machine
        self.scan_path = scan_path
        self.scan_time = scan_time
        self.scan_type = scan_type
        self.status = status
        self.suspicious_count = suspicious_count
        self.suspicious_machine = suspicious_machine
        self.task_id = task_id
        self.un_complete_machine = un_complete_machine

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_machine is not None:
            result['CompleteMachine'] = self.complete_machine

        if self.machine_name is not None:
            result['MachineName'] = self.machine_name

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.safe_machine is not None:
            result['SafeMachine'] = self.safe_machine

        if self.scan_machine is not None:
            result['ScanMachine'] = self.scan_machine

        if self.scan_path is not None:
            result['ScanPath'] = self.scan_path

        if self.scan_time is not None:
            result['ScanTime'] = self.scan_time

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        if self.status is not None:
            result['Status'] = self.status

        if self.suspicious_count is not None:
            result['SuspiciousCount'] = self.suspicious_count

        if self.suspicious_machine is not None:
            result['SuspiciousMachine'] = self.suspicious_machine

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.un_complete_machine is not None:
            result['UnCompleteMachine'] = self.un_complete_machine

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteMachine') is not None:
            self.complete_machine = m.get('CompleteMachine')

        if m.get('MachineName') is not None:
            self.machine_name = m.get('MachineName')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SafeMachine') is not None:
            self.safe_machine = m.get('SafeMachine')

        if m.get('ScanMachine') is not None:
            self.scan_machine = m.get('ScanMachine')

        if m.get('ScanPath') is not None:
            self.scan_path = m.get('ScanPath')

        if m.get('ScanTime') is not None:
            self.scan_time = m.get('ScanTime')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuspiciousCount') is not None:
            self.suspicious_count = m.get('SuspiciousCount')

        if m.get('SuspiciousMachine') is not None:
            self.suspicious_machine = m.get('SuspiciousMachine')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UnCompleteMachine') is not None:
            self.un_complete_machine = m.get('UnCompleteMachine')

        return self


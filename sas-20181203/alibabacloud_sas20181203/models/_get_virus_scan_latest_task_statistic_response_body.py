# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetVirusScanLatestTaskStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetVirusScanLatestTaskStatisticResponseBodyData = None,
        request_id: str = None,
    ):
        # The custom result data.
        self.data = data
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetVirusScanLatestTaskStatisticResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVirusScanLatestTaskStatisticResponseBodyData(DaraModel):
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
        # The number of servers that completed the scan.
        self.complete_machine = complete_machine
        # The name of the server.
        self.machine_name = machine_name
        # The progress percentage of the scan task.
        self.progress = progress
        # The highest risk level of the alerts detected by the scan. Valid values:
        # 
        # - **high**: high-risk.
        # - **medium**: medium-risk.
        # - **low**: low-risk.
        self.risk_level = risk_level
        # The number of servers on which no risks are detected.
        self.safe_machine = safe_machine
        # The number of servers scanned in this virus scan.
        self.scan_machine = scan_machine
        # The file paths specified for scanning when the scan type is user-defined.
        self.scan_path = scan_path
        # The timestamp of the scan. Unit: milliseconds.
        self.scan_time = scan_time
        # The scan type of this virus scan. Valid values:
        # - **system**: automatic system scan.
        # - **user**: user-defined scan.
        self.scan_type = scan_type
        # The status of the scan task.
        # 
        # **Valid values for the main task:**
        # - **0**: The task is pending.
        # - **10**: The scan is in progress.
        # - **100**: The scan is complete.
        # 
        # **Valid values for the subtask:**
        # - **0**: The scan is pending.
        # - **20**: The detection script is delivered.
        # - **50**: The scan is running on the server.
        # - **100**: The scan is complete.
        self.status = status
        # The number of security alerts detected by the scan.
        self.suspicious_count = suspicious_count
        # The number of servers on which risks are detected.
        self.suspicious_machine = suspicious_machine
        # The ID of the scan task.
        self.task_id = task_id
        # The number of servers that have not completed the scan or failed the scan.
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


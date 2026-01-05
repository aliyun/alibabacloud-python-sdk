# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBLogFilesResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dbinstance_type: str = None,
        ha_log_items: List[main_models.DescribeDBLogFilesResponseBodyHaLogItems] = None,
        ha_status: int = None,
        items_numbers: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        switch_list_items: List[main_models.DescribeDBLogFilesResponseBodySwitchListItems] = None,
        switch_log_items: List[main_models.DescribeDBLogFilesResponseBodySwitchLogItems] = None,
        total_records: int = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.dbinstance_type = dbinstance_type
        self.ha_log_items = ha_log_items
        self.ha_status = ha_status
        self.items_numbers = items_numbers
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.switch_list_items = switch_list_items
        self.switch_log_items = switch_log_items
        self.total_records = total_records

    def validate(self):
        if self.ha_log_items:
            for v1 in self.ha_log_items:
                 if v1:
                    v1.validate()
        if self.switch_list_items:
            for v1 in self.switch_list_items:
                 if v1:
                    v1.validate()
        if self.switch_log_items:
            for v1 in self.switch_log_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        result['HaLogItems'] = []
        if self.ha_log_items is not None:
            for k1 in self.ha_log_items:
                result['HaLogItems'].append(k1.to_map() if k1 else None)

        if self.ha_status is not None:
            result['HaStatus'] = self.ha_status

        if self.items_numbers is not None:
            result['ItemsNumbers'] = self.items_numbers

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SwitchListItems'] = []
        if self.switch_list_items is not None:
            for k1 in self.switch_list_items:
                result['SwitchListItems'].append(k1.to_map() if k1 else None)

        result['SwitchLogItems'] = []
        if self.switch_log_items is not None:
            for k1 in self.switch_log_items:
                result['SwitchLogItems'].append(k1.to_map() if k1 else None)

        if self.total_records is not None:
            result['TotalRecords'] = self.total_records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        self.ha_log_items = []
        if m.get('HaLogItems') is not None:
            for k1 in m.get('HaLogItems'):
                temp_model = main_models.DescribeDBLogFilesResponseBodyHaLogItems()
                self.ha_log_items.append(temp_model.from_map(k1))

        if m.get('HaStatus') is not None:
            self.ha_status = m.get('HaStatus')

        if m.get('ItemsNumbers') is not None:
            self.items_numbers = m.get('ItemsNumbers')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.switch_list_items = []
        if m.get('SwitchListItems') is not None:
            for k1 in m.get('SwitchListItems'):
                temp_model = main_models.DescribeDBLogFilesResponseBodySwitchListItems()
                self.switch_list_items.append(temp_model.from_map(k1))

        self.switch_log_items = []
        if m.get('SwitchLogItems') is not None:
            for k1 in m.get('SwitchLogItems'):
                temp_model = main_models.DescribeDBLogFilesResponseBodySwitchLogItems()
                self.switch_log_items.append(temp_model.from_map(k1))

        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')

        return self

class DescribeDBLogFilesResponseBodySwitchLogItems(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dst_db_type: str = None,
        event_finish_time: str = None,
        event_start_time: str = None,
        simulate_list_id: str = None,
        simulate_status: str = None,
        simulatecode: str = None,
        src_db_type: str = None,
        switch_step_items: List[main_models.DescribeDBLogFilesResponseBodySwitchLogItemsSwitchStepItems] = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.dst_db_type = dst_db_type
        self.event_finish_time = event_finish_time
        self.event_start_time = event_start_time
        self.simulate_list_id = simulate_list_id
        self.simulate_status = simulate_status
        self.simulatecode = simulatecode
        self.src_db_type = src_db_type
        self.switch_step_items = switch_step_items

    def validate(self):
        if self.switch_step_items:
            for v1 in self.switch_step_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dst_db_type is not None:
            result['DstDbType'] = self.dst_db_type

        if self.event_finish_time is not None:
            result['EventFinishTime'] = self.event_finish_time

        if self.event_start_time is not None:
            result['EventStartTime'] = self.event_start_time

        if self.simulate_list_id is not None:
            result['SimulateListId'] = self.simulate_list_id

        if self.simulate_status is not None:
            result['SimulateStatus'] = self.simulate_status

        if self.simulatecode is not None:
            result['Simulatecode'] = self.simulatecode

        if self.src_db_type is not None:
            result['SrcDbType'] = self.src_db_type

        result['SwitchStepItems'] = []
        if self.switch_step_items is not None:
            for k1 in self.switch_step_items:
                result['SwitchStepItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DstDbType') is not None:
            self.dst_db_type = m.get('DstDbType')

        if m.get('EventFinishTime') is not None:
            self.event_finish_time = m.get('EventFinishTime')

        if m.get('EventStartTime') is not None:
            self.event_start_time = m.get('EventStartTime')

        if m.get('SimulateListId') is not None:
            self.simulate_list_id = m.get('SimulateListId')

        if m.get('SimulateStatus') is not None:
            self.simulate_status = m.get('SimulateStatus')

        if m.get('Simulatecode') is not None:
            self.simulatecode = m.get('Simulatecode')

        if m.get('SrcDbType') is not None:
            self.src_db_type = m.get('SrcDbType')

        self.switch_step_items = []
        if m.get('SwitchStepItems') is not None:
            for k1 in m.get('SwitchStepItems'):
                temp_model = main_models.DescribeDBLogFilesResponseBodySwitchLogItemsSwitchStepItems()
                self.switch_step_items.append(temp_model.from_map(k1))

        return self

class DescribeDBLogFilesResponseBodySwitchLogItemsSwitchStepItems(DaraModel):
    def __init__(
        self,
        dbnode_id: str = None,
        end_time: str = None,
        is_success: str = None,
        simulate_phase: str = None,
        start_time: str = None,
        step_msg: str = None,
        step_name: str = None,
        time_cost: str = None,
    ):
        self.dbnode_id = dbnode_id
        self.end_time = end_time
        self.is_success = is_success
        self.simulate_phase = simulate_phase
        self.start_time = start_time
        self.step_msg = step_msg
        self.step_name = step_name
        self.time_cost = time_cost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.simulate_phase is not None:
            result['SimulatePhase'] = self.simulate_phase

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.step_msg is not None:
            result['StepMsg'] = self.step_msg

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.time_cost is not None:
            result['TimeCost'] = self.time_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('SimulatePhase') is not None:
            self.simulate_phase = m.get('SimulatePhase')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StepMsg') is not None:
            self.step_msg = m.get('StepMsg')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('TimeCost') is not None:
            self.time_cost = m.get('TimeCost')

        return self

class DescribeDBLogFilesResponseBodySwitchListItems(DaraModel):
    def __init__(
        self,
        dbnode_crash_list: List[str] = None,
        end_time: str = None,
        event_finish_time: str = None,
        event_start_time: str = None,
        fault_injection_type: str = None,
        simulate_list_id: str = None,
        simulate_mode: str = None,
        simulate_status: str = None,
        simulate_task_id: str = None,
        start_time: str = None,
        switch_log_items: List[main_models.DescribeDBLogFilesResponseBodySwitchListItemsSwitchLogItems] = None,
        switch_step_items: List[main_models.DescribeDBLogFilesResponseBodySwitchListItemsSwitchStepItems] = None,
    ):
        self.dbnode_crash_list = dbnode_crash_list
        self.end_time = end_time
        self.event_finish_time = event_finish_time
        self.event_start_time = event_start_time
        self.fault_injection_type = fault_injection_type
        self.simulate_list_id = simulate_list_id
        self.simulate_mode = simulate_mode
        self.simulate_status = simulate_status
        self.simulate_task_id = simulate_task_id
        self.start_time = start_time
        self.switch_log_items = switch_log_items
        self.switch_step_items = switch_step_items

    def validate(self):
        if self.switch_log_items:
            for v1 in self.switch_log_items:
                 if v1:
                    v1.validate()
        if self.switch_step_items:
            for v1 in self.switch_step_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_crash_list is not None:
            result['DBNodeCrashList'] = self.dbnode_crash_list

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_finish_time is not None:
            result['EventFinishTime'] = self.event_finish_time

        if self.event_start_time is not None:
            result['EventStartTime'] = self.event_start_time

        if self.fault_injection_type is not None:
            result['FaultInjectionType'] = self.fault_injection_type

        if self.simulate_list_id is not None:
            result['SimulateListId'] = self.simulate_list_id

        if self.simulate_mode is not None:
            result['SimulateMode'] = self.simulate_mode

        if self.simulate_status is not None:
            result['SimulateStatus'] = self.simulate_status

        if self.simulate_task_id is not None:
            result['SimulateTaskId'] = self.simulate_task_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['SwitchLogItems'] = []
        if self.switch_log_items is not None:
            for k1 in self.switch_log_items:
                result['SwitchLogItems'].append(k1.to_map() if k1 else None)

        result['SwitchStepItems'] = []
        if self.switch_step_items is not None:
            for k1 in self.switch_step_items:
                result['SwitchStepItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeCrashList') is not None:
            self.dbnode_crash_list = m.get('DBNodeCrashList')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventFinishTime') is not None:
            self.event_finish_time = m.get('EventFinishTime')

        if m.get('EventStartTime') is not None:
            self.event_start_time = m.get('EventStartTime')

        if m.get('FaultInjectionType') is not None:
            self.fault_injection_type = m.get('FaultInjectionType')

        if m.get('SimulateListId') is not None:
            self.simulate_list_id = m.get('SimulateListId')

        if m.get('SimulateMode') is not None:
            self.simulate_mode = m.get('SimulateMode')

        if m.get('SimulateStatus') is not None:
            self.simulate_status = m.get('SimulateStatus')

        if m.get('SimulateTaskId') is not None:
            self.simulate_task_id = m.get('SimulateTaskId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.switch_log_items = []
        if m.get('SwitchLogItems') is not None:
            for k1 in m.get('SwitchLogItems'):
                temp_model = main_models.DescribeDBLogFilesResponseBodySwitchListItemsSwitchLogItems()
                self.switch_log_items.append(temp_model.from_map(k1))

        self.switch_step_items = []
        if m.get('SwitchStepItems') is not None:
            for k1 in m.get('SwitchStepItems'):
                temp_model = main_models.DescribeDBLogFilesResponseBodySwitchListItemsSwitchStepItems()
                self.switch_step_items.append(temp_model.from_map(k1))

        return self

class DescribeDBLogFilesResponseBodySwitchListItemsSwitchStepItems(DaraModel):
    def __init__(
        self,
        dbnode_id: str = None,
        end_time: str = None,
        is_success: str = None,
        simulate_phase: str = None,
        start_time: str = None,
        step_name: str = None,
        time_cost: str = None,
    ):
        self.dbnode_id = dbnode_id
        self.end_time = end_time
        self.is_success = is_success
        self.simulate_phase = simulate_phase
        self.start_time = start_time
        self.step_name = step_name
        self.time_cost = time_cost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.simulate_phase is not None:
            result['SimulatePhase'] = self.simulate_phase

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.time_cost is not None:
            result['TimeCost'] = self.time_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('SimulatePhase') is not None:
            self.simulate_phase = m.get('SimulatePhase')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('TimeCost') is not None:
            self.time_cost = m.get('TimeCost')

        return self

class DescribeDBLogFilesResponseBodySwitchListItemsSwitchLogItems(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dst_db_type: str = None,
        event_finish_time: str = None,
        event_start_time: str = None,
        simulate_list_id: str = None,
        simulate_log_id: str = None,
        simulate_status: str = None,
        src_db_type: str = None,
        switch_step_items: List[main_models.DescribeDBLogFilesResponseBodySwitchListItemsSwitchLogItemsSwitchStepItems] = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.dst_db_type = dst_db_type
        self.event_finish_time = event_finish_time
        self.event_start_time = event_start_time
        self.simulate_list_id = simulate_list_id
        self.simulate_log_id = simulate_log_id
        self.simulate_status = simulate_status
        self.src_db_type = src_db_type
        self.switch_step_items = switch_step_items

    def validate(self):
        if self.switch_step_items:
            for v1 in self.switch_step_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dst_db_type is not None:
            result['DstDbType'] = self.dst_db_type

        if self.event_finish_time is not None:
            result['EventFinishTime'] = self.event_finish_time

        if self.event_start_time is not None:
            result['EventStartTime'] = self.event_start_time

        if self.simulate_list_id is not None:
            result['SimulateListId'] = self.simulate_list_id

        if self.simulate_log_id is not None:
            result['SimulateLogId'] = self.simulate_log_id

        if self.simulate_status is not None:
            result['SimulateStatus'] = self.simulate_status

        if self.src_db_type is not None:
            result['SrcDbType'] = self.src_db_type

        result['SwitchStepItems'] = []
        if self.switch_step_items is not None:
            for k1 in self.switch_step_items:
                result['SwitchStepItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DstDbType') is not None:
            self.dst_db_type = m.get('DstDbType')

        if m.get('EventFinishTime') is not None:
            self.event_finish_time = m.get('EventFinishTime')

        if m.get('EventStartTime') is not None:
            self.event_start_time = m.get('EventStartTime')

        if m.get('SimulateListId') is not None:
            self.simulate_list_id = m.get('SimulateListId')

        if m.get('SimulateLogId') is not None:
            self.simulate_log_id = m.get('SimulateLogId')

        if m.get('SimulateStatus') is not None:
            self.simulate_status = m.get('SimulateStatus')

        if m.get('SrcDbType') is not None:
            self.src_db_type = m.get('SrcDbType')

        self.switch_step_items = []
        if m.get('SwitchStepItems') is not None:
            for k1 in m.get('SwitchStepItems'):
                temp_model = main_models.DescribeDBLogFilesResponseBodySwitchListItemsSwitchLogItemsSwitchStepItems()
                self.switch_step_items.append(temp_model.from_map(k1))

        return self

class DescribeDBLogFilesResponseBodySwitchListItemsSwitchLogItemsSwitchStepItems(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        is_success: str = None,
        simulate_phase: str = None,
        start_time: str = None,
        step_name: str = None,
        time_cost: str = None,
    ):
        self.end_time = end_time
        self.is_success = is_success
        self.simulate_phase = simulate_phase
        self.start_time = start_time
        self.step_name = step_name
        self.time_cost = time_cost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.simulate_phase is not None:
            result['SimulatePhase'] = self.simulate_phase

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.time_cost is not None:
            result['TimeCost'] = self.time_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('SimulatePhase') is not None:
            self.simulate_phase = m.get('SimulatePhase')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('TimeCost') is not None:
            self.time_cost = m.get('TimeCost')

        return self

class DescribeDBLogFilesResponseBodyHaLogItems(DaraModel):
    def __init__(
        self,
        affected_sessions: int = None,
        from_dbtype: str = None,
        switch_cause_code: str = None,
        switch_cause_detail: str = None,
        switch_finish_time: str = None,
        switch_id: str = None,
        switch_start_time: str = None,
        switch_type: int = None,
        total_sessions: int = None,
    ):
        self.affected_sessions = affected_sessions
        self.from_dbtype = from_dbtype
        self.switch_cause_code = switch_cause_code
        self.switch_cause_detail = switch_cause_detail
        self.switch_finish_time = switch_finish_time
        self.switch_id = switch_id
        self.switch_start_time = switch_start_time
        self.switch_type = switch_type
        self.total_sessions = total_sessions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_sessions is not None:
            result['AffectedSessions'] = self.affected_sessions

        if self.from_dbtype is not None:
            result['FromDBType'] = self.from_dbtype

        if self.switch_cause_code is not None:
            result['SwitchCauseCode'] = self.switch_cause_code

        if self.switch_cause_detail is not None:
            result['SwitchCauseDetail'] = self.switch_cause_detail

        if self.switch_finish_time is not None:
            result['SwitchFinishTime'] = self.switch_finish_time

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.switch_start_time is not None:
            result['SwitchStartTime'] = self.switch_start_time

        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type

        if self.total_sessions is not None:
            result['TotalSessions'] = self.total_sessions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedSessions') is not None:
            self.affected_sessions = m.get('AffectedSessions')

        if m.get('FromDBType') is not None:
            self.from_dbtype = m.get('FromDBType')

        if m.get('SwitchCauseCode') is not None:
            self.switch_cause_code = m.get('SwitchCauseCode')

        if m.get('SwitchCauseDetail') is not None:
            self.switch_cause_detail = m.get('SwitchCauseDetail')

        if m.get('SwitchFinishTime') is not None:
            self.switch_finish_time = m.get('SwitchFinishTime')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('SwitchStartTime') is not None:
            self.switch_start_time = m.get('SwitchStartTime')

        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')

        if m.get('TotalSessions') is not None:
            self.total_sessions = m.get('TotalSessions')

        return self


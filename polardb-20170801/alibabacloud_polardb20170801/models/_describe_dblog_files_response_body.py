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
        # The cluster ID.
        self.dbinstance_name = dbinstance_name
        # The instance type. Valid values:
        # 
        # - **polardb_mysql_rw**: read-write instance.
        # 
        # - **polardb_mysql_ro**: read-only instance.
        # 
        # - **polardb_mysql_standby**: standby instance.
        self.dbinstance_type = dbinstance_type
        # A list of failover logs.
        self.ha_log_items = ha_log_items
        # Indicates whether a failover record exists. Valid values:
        # 
        # - **1**: No
        # 
        # - **0**: Yes
        self.ha_status = ha_status
        # The number of log items on the current page.
        self.items_numbers = items_numbers
        # The page number. It must be a positive integer that does not exceed the maximum value of the Integer data type. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 5 to 50. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # A list of fault simulation records.
        self.switch_list_items = switch_list_items
        # A list of fault simulation logs.
        self.switch_log_items = switch_log_items
        # The total number of records.
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
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of your clusters, including the cluster IDs.
        self.dbinstance_id = dbinstance_id
        # The destination database type. Valid values:
        # 
        # - **PolarDBMySQL**: A major version upgrade of PolarDB for MySQL.
        # 
        # - **RDS**: A migration from RDS to PolarDB for MySQL.
        self.dst_db_type = dst_db_type
        # The time when the system event was complete. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.event_finish_time = event_finish_time
        # The time when the system event started. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.event_start_time = event_start_time
        # The simulation list ID.
        self.simulate_list_id = simulate_list_id
        # The fault simulation status. Valid values:
        # 
        # - **0**: Pending
        # 
        # - **1**: Success
        # 
        # - **2**: Running
        # 
        # - **3**: Failed
        # 
        # - **4**: Aborted
        # 
        # - **5**: Awaiting rollback
        self.simulate_status = simulate_status
        # The status code of the fault simulation.
        self.simulatecode = simulatecode
        # The source database type. Valid values:
        # 
        # - **PolarDBMySQL**: A major version upgrade of PolarDB for MySQL.
        # 
        # - **RDS**: A migration from RDS to PolarDB for MySQL.
        self.src_db_type = src_db_type
        # A list of failover steps.
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
        # The node ID.
        # 
        # > You must specify either the `DBNodeId` or `DBClusterId` parameter. You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of your clusters, including the node IDs.
        self.dbnode_id = dbnode_id
        # The time when the step was complete. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.end_time = end_time
        # Indicates whether the step was successful. Valid values:
        # 
        # - `true`: The step was successful.
        # 
        # - `false`: The step failed.
        self.is_success = is_success
        # The fault simulation phase. Valid values:
        # 
        # - **PolarDB.MySQL.FaultSimulate.Phase.FAULT_INJECTION**: The fault injection phase.
        # 
        # - **PolarDB.MySQL.FaultSimulate.Phase.RECOVERY**: The recovery phase.
        # 
        # - **PolarDB.MySQL.FaultSimulate.Phase.POST_PROCESS**: The post-processing phase.
        self.simulate_phase = simulate_phase
        # The time when the step started. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.start_time = start_time
        # A message about the execution status of the step.
        self.step_msg = step_msg
        # The name of the step.
        self.step_name = step_name
        # The duration of the step in milliseconds.
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
        # The IDs of nodes on which to simulate a fault.
        # 
        # > For a node-level fault simulation, specify the ID of a single node. For an availability zone-level fault simulation, you can either omit this parameter or specify the IDs of all nodes in the zone.
        self.dbnode_crash_list = dbnode_crash_list
        # The time when the fault simulation was complete. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.end_time = end_time
        # The time when the system event was complete. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.event_finish_time = event_finish_time
        # The time when the system event started. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.event_start_time = event_start_time
        # The fault injection method. Valid values:
        # 
        # - CrashSQLInjection: Injects a fault into the instance by using `Crash SQL`.
        self.fault_injection_type = fault_injection_type
        # The fault simulation record ID.
        self.simulate_list_id = simulate_list_id
        # The fault simulation mode.
        self.simulate_mode = simulate_mode
        # The fault simulation status. Valid values:
        # 
        # - **0**: Pending
        # 
        # - **1**: Success
        # 
        # - **2**: Running
        # 
        # - **3**: Failed
        # 
        # - **4**: Aborted
        # 
        # - **5**: Awaiting rollback
        self.simulate_status = simulate_status
        # The fault simulation task ID.
        self.simulate_task_id = simulate_task_id
        # The time when the fault simulation started. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.start_time = start_time
        # A list of fault simulation logs.
        self.switch_log_items = switch_log_items
        # A list of failover steps.
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
        # The cluster node ID.
        # 
        # > This parameter is returned only when the `Key` parameter in the request is not set to `PolarDBDiskUsage`.
        self.dbnode_id = dbnode_id
        # The time when the step was complete. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.end_time = end_time
        # Indicates whether the step was successful. Valid values:
        # 
        # - `true`: The step was successful.
        # 
        # - `false`: The step failed.
        self.is_success = is_success
        # The fault simulation phase. Valid values:
        # 
        # - **PolarDB.MySQL.FaultSimulate.Phase.FAULT_INJECTION**: The fault injection phase.
        # 
        # - **PolarDB.MySQL.FaultSimulate.Phase.RECOVERY**: The recovery phase.
        # 
        # - **PolarDB.MySQL.FaultSimulate.Phase.POST_PROCESS**: The post-processing phase.
        self.simulate_phase = simulate_phase
        # The time when the step started. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.start_time = start_time
        # The name of the current step. You can call the [DescribeHistoryTasks](https://help.aliyun.com/document_detail/2400077.html) operation to query the current step of a specified task. A common value is **do_pause**, which indicates that the system waits for a specified period of time.
        self.step_name = step_name
        # The duration of the step in milliseconds.
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
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of your clusters, including the cluster IDs.
        self.dbinstance_id = dbinstance_id
        # The destination database type. Valid values:
        # 
        # - **PolarDBMySQL**: A major version upgrade of PolarDB for MySQL.
        # 
        # - **RDS**: A migration from RDS to PolarDB for MySQL.
        self.dst_db_type = dst_db_type
        # The time when the system event was complete. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.event_finish_time = event_finish_time
        # The time when the system event started. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.event_start_time = event_start_time
        # The simulation list ID.
        self.simulate_list_id = simulate_list_id
        # The simulation log ID.
        self.simulate_log_id = simulate_log_id
        # The fault simulation status. Valid values:
        # 
        # - **0**: Pending
        # 
        # - **1**: Success
        # 
        # - **2**: Running
        # 
        # - **3**: Failed
        # 
        # - **4**: Aborted
        # 
        # - **5**: Awaiting rollback
        self.simulate_status = simulate_status
        # The source database type. Valid values:
        # 
        # - **PolarDBMySQL**: A major version upgrade of PolarDB for MySQL.
        # 
        # - **RDS**: A migration from RDS to PolarDB for MySQL.
        self.src_db_type = src_db_type
        # A list of fault simulation steps.
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
        # The time when the step was complete. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.end_time = end_time
        # Indicates whether the step was successful. Valid values:
        # 
        # - `true`: The step was successful.
        # 
        # - `false`: The step failed.
        self.is_success = is_success
        # The fault simulation phase. Valid values:
        # 
        # - **PolarDB.MySQL.FaultSimulate.Phase.FAULT_INJECTION**: The fault injection phase.
        # 
        # - **PolarDB.MySQL.FaultSimulate.Phase.RECOVERY**: The recovery phase.
        # 
        # - **PolarDB.MySQL.FaultSimulate.Phase.POST_PROCESS**: The post-processing phase.
        self.simulate_phase = simulate_phase
        # The time when the step started. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.start_time = start_time
        # The name of the current step. You can call the [DescribeHistoryTasks](https://help.aliyun.com/document_detail/2400077.html) operation to query the current step of a specified task. A common value is **do_pause**, which indicates that the system waits for a specified period of time.
        self.step_name = step_name
        # The duration of the step in milliseconds.
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
        # The number of affected sessions during the failover.
        self.affected_sessions = affected_sessions
        # The instance type before the failover. Valid values:
        # 
        # - **polardb_mysql_rw**: read-write instance.
        # 
        # - **polardb_mysql_ro**: read-only instance.
        # 
        # - **polardb_mysql_standby**: standby instance.
        self.from_dbtype = from_dbtype
        # The error code for the failover cause.
        self.switch_cause_code = switch_cause_code
        # Details about the failover cause.
        self.switch_cause_detail = switch_cause_detail
        # The time when the failover was complete. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.switch_finish_time = switch_finish_time
        # The failover log ID.
        self.switch_id = switch_id
        # The time when the failover started. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.switch_start_time = switch_start_time
        # The failover type.
        self.switch_type = switch_type
        # The total number of sessions during the failover.
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


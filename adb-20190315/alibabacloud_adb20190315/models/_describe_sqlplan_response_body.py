# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeSQLPlanResponseBody(DaraModel):
    def __init__(
        self,
        detail: main_models.DescribeSQLPlanResponseBodyDetail = None,
        origin_info: str = None,
        request_id: str = None,
        stage_list: List[main_models.DescribeSQLPlanResponseBodyStageList] = None,
    ):
        # The execution information about the SQL statement.
        self.detail = detail
        # The original information about the SQL statement.
        self.origin_info = origin_info
        # The request ID.
        self.request_id = request_id
        # The queried plan in different stages.
        self.stage_list = stage_list

    def validate(self):
        if self.detail:
            self.detail.validate()
        if self.stage_list:
            for v1 in self.stage_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.origin_info is not None:
            result['OriginInfo'] = self.origin_info

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StageList'] = []
        if self.stage_list is not None:
            for k1 in self.stage_list:
                result['StageList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = main_models.DescribeSQLPlanResponseBodyDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('OriginInfo') is not None:
            self.origin_info = m.get('OriginInfo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stage_list = []
        if m.get('StageList') is not None:
            for k1 in m.get('StageList'):
                temp_model = main_models.DescribeSQLPlanResponseBodyStageList()
                self.stage_list.append(temp_model.from_map(k1))

        return self

class DescribeSQLPlanResponseBodyStageList(DaraModel):
    def __init__(
        self,
        cputime_avg: int = None,
        cputime_max: int = None,
        cputime_min: int = None,
        input_size_avg: int = None,
        input_size_max: int = None,
        input_size_min: int = None,
        operator_cost: int = None,
        peak_memory: int = None,
        scan_size_avg: int = None,
        scan_size_max: int = None,
        scan_size_min: int = None,
        scan_time_avg: int = None,
        scan_time_max: int = None,
        scan_time_min: int = None,
        stage_id: int = None,
        state: str = None,
    ):
        # The average `CPU Time` value on each compute node in the stage. Unit: milliseconds.
        self.cputime_avg = cputime_avg
        # The maximum `CPU Time` value on each compute node in the stage. Unit: milliseconds.
        self.cputime_max = cputime_max
        # The minimum `CPU Time` value on each compute node in the stage. Unit: milliseconds.
        self.cputime_min = cputime_min
        # The average amount of input data on each compute node in the stage. Unit: bytes.
        self.input_size_avg = input_size_avg
        # The maximum amount of input data on each compute node in the stage. Unit: byte.
        self.input_size_max = input_size_max
        # The minimum amount of input data on each compute node in the stage. Unit: bytes.
        self.input_size_min = input_size_min
        # The total CPU time consumed by all operators in the stage, which is equivalent to the total CPU time of the stage. You can use this parameter to determine which parts of the stage consume a large amount of computing resources. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The maximum memory usage when the SQL statement is executed. Unit: bytes.
        self.peak_memory = peak_memory
        # The average amount of data scanned by a scan operator on each storage node in the stage. Unit: bytes.
        self.scan_size_avg = scan_size_avg
        # The maximum amount of data scanned by a scan operator on each storage node in the stage. Unit: bytes.
        self.scan_size_max = scan_size_max
        # The minimum amount of data scanned by a scan operator on each storage node in the stage. Unit: bytes.
        self.scan_size_min = scan_size_min
        # The average amount of time consumed by a scan operator to read data on each storage node in the stage. Unit: milliseconds.
        self.scan_time_avg = scan_time_avg
        # The maximum amount of time consumed by a scan operator to read data on each storage node in the stage. Unit: milliseconds.
        self.scan_time_max = scan_time_max
        # The minimum amount of time consumed by a scan operator to read data on each storage node in the stage. Unit: milliseconds.
        self.scan_time_min = scan_time_min
        # The stage ID.
        self.stage_id = stage_id
        # The final execution state of the stage. Valid values:
        # 
        # *   FINISHED
        # *   CANCELED
        # *   ABORTED
        # *   FAILED
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cputime_avg is not None:
            result['CPUTimeAvg'] = self.cputime_avg

        if self.cputime_max is not None:
            result['CPUTimeMax'] = self.cputime_max

        if self.cputime_min is not None:
            result['CPUTimeMin'] = self.cputime_min

        if self.input_size_avg is not None:
            result['InputSizeAvg'] = self.input_size_avg

        if self.input_size_max is not None:
            result['InputSizeMax'] = self.input_size_max

        if self.input_size_min is not None:
            result['InputSizeMin'] = self.input_size_min

        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.scan_size_avg is not None:
            result['ScanSizeAvg'] = self.scan_size_avg

        if self.scan_size_max is not None:
            result['ScanSizeMax'] = self.scan_size_max

        if self.scan_size_min is not None:
            result['ScanSizeMin'] = self.scan_size_min

        if self.scan_time_avg is not None:
            result['ScanTimeAvg'] = self.scan_time_avg

        if self.scan_time_max is not None:
            result['ScanTimeMax'] = self.scan_time_max

        if self.scan_time_min is not None:
            result['ScanTimeMin'] = self.scan_time_min

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPUTimeAvg') is not None:
            self.cputime_avg = m.get('CPUTimeAvg')

        if m.get('CPUTimeMax') is not None:
            self.cputime_max = m.get('CPUTimeMax')

        if m.get('CPUTimeMin') is not None:
            self.cputime_min = m.get('CPUTimeMin')

        if m.get('InputSizeAvg') is not None:
            self.input_size_avg = m.get('InputSizeAvg')

        if m.get('InputSizeMax') is not None:
            self.input_size_max = m.get('InputSizeMax')

        if m.get('InputSizeMin') is not None:
            self.input_size_min = m.get('InputSizeMin')

        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('ScanSizeAvg') is not None:
            self.scan_size_avg = m.get('ScanSizeAvg')

        if m.get('ScanSizeMax') is not None:
            self.scan_size_max = m.get('ScanSizeMax')

        if m.get('ScanSizeMin') is not None:
            self.scan_size_min = m.get('ScanSizeMin')

        if m.get('ScanTimeAvg') is not None:
            self.scan_time_avg = m.get('ScanTimeAvg')

        if m.get('ScanTimeMax') is not None:
            self.scan_time_max = m.get('ScanTimeMax')

        if m.get('ScanTimeMin') is not None:
            self.scan_time_min = m.get('ScanTimeMin')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeSQLPlanResponseBodyDetail(DaraModel):
    def __init__(
        self,
        cputime: int = None,
        client_ip: str = None,
        database: str = None,
        output_rows: int = None,
        output_size: int = None,
        peak_memory: int = None,
        planning_time: int = None,
        queued_time: int = None,
        sql: str = None,
        start_time: str = None,
        state: str = None,
        total_stage: int = None,
        total_task: int = None,
        total_time: int = None,
        user: str = None,
    ):
        # The total CPU time consumed by all operators on multithreaded servers when the SQL statement is executed. Unit: milliseconds.
        self.cputime = cputime
        # The IP address of the client that is used to execute the SQL statement.
        self.client_ip = client_ip
        # The name of the database on which the SQL statement was executed.
        self.database = database
        # The total number of rows generated by the SQL statement.
        self.output_rows = output_rows
        # The total amount of data generated by the SQL statement. Unit: bytes.
        self.output_size = output_size
        # The maximum memory usage when the SQL statement is executed. Unit: bytes.
        self.peak_memory = peak_memory
        # The amount of time consumed to generate the execution plan of the SQL statement. Unit: milliseconds.
        self.planning_time = planning_time
        # The amount of time consumed to queue the SQL statement. Unit: milliseconds.
        self.queued_time = queued_time
        # The SQL statement.
        self.sql = sql
        # The execution start time of the SQL statement. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The final execution state of the SQL statement. Valid values:
        # 
        # *   FINISHED
        # *   FAILED
        self.state = state
        # The total number of stages in the SQL statement.
        self.total_stage = total_stage
        # The total number of tasks in the SQL statement.
        self.total_task = total_task
        # The total amount of time consumed to execute the SQL statement. Unit: milliseconds.
        self.total_time = total_time
        # The name of the user who submitted the SQL statement.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cputime is not None:
            result['CPUTime'] = self.cputime

        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip

        if self.database is not None:
            result['Database'] = self.database

        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows

        if self.output_size is not None:
            result['OutputSize'] = self.output_size

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.planning_time is not None:
            result['PlanningTime'] = self.planning_time

        if self.queued_time is not None:
            result['QueuedTime'] = self.queued_time

        if self.sql is not None:
            result['SQL'] = self.sql

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.total_stage is not None:
            result['TotalStage'] = self.total_stage

        if self.total_task is not None:
            result['TotalTask'] = self.total_task

        if self.total_time is not None:
            result['TotalTime'] = self.total_time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPUTime') is not None:
            self.cputime = m.get('CPUTime')

        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')

        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('PlanningTime') is not None:
            self.planning_time = m.get('PlanningTime')

        if m.get('QueuedTime') is not None:
            self.queued_time = m.get('QueuedTime')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TotalStage') is not None:
            self.total_stage = m.get('TotalStage')

        if m.get('TotalTask') is not None:
            self.total_task = m.get('TotalTask')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self


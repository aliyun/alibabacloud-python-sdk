# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeFullProcessListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        config_list: Dict[str, Any] = None,
        dts_job_id: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        full_process_list: List[main_models.DescribeFullProcessListResponseBodyFullProcessList] = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The throttling configuration. Valid values:
        # 
        # *   **dts.datamove.blaster.qps.max**: The rate at which queries are made to the source database per second.
        # *   **dts.datamove.source.rps.max**: the number of rows that are fully synchronized or migrated per second.
        # *   **dts.datamove.source.bps.max**: the amount of data processed per second for full synchronization or migration. Unit: Byte/s.
        # 
        # > 
        # 
        # *   When you set the **JobCode** parameter to **03**, you need to specify the **EnableLimit** parameter as **true**. Otherwise, the configuration cannot take effect.
        # 
        # *   When you set the **JobCode** parameter to **04** or **07**, you only need to specify the **dts.datamove.source.rps.max** and **dts.datamove.source.bps.max** parameters.
        # *   A value of \\*\\*-1\\*\\* indicates no rate limit.
        self.config_list = config_list
        # The ID of the data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The dynamic part in the error message. This parameter is used to replace the \\*\\*%s\\*\\* variable in the **ErrMessage** parameter.
        # 
        # >  The request parameter **DtsJobId** is invalid if **The Value of Input Parameter %s is not valid** is returned for **ErrMessage** and **DtsJobId** is returned for **DynamicMessage**.
        self.dynamic_message = dynamic_message
        # The error code returned when the request failed.
        self.err_code = err_code
        # The error message returned when the request failed.
        self.err_message = err_message
        # The details of the GA instances.
        self.full_process_list = full_process_list
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.full_process_list:
            for v1 in self.full_process_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.config_list is not None:
            result['ConfigList'] = self.config_list

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        result['FullProcessList'] = []
        if self.full_process_list is not None:
            for k1 in self.full_process_list:
                result['FullProcessList'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConfigList') is not None:
            self.config_list = m.get('ConfigList')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        self.full_process_list = []
        if m.get('FullProcessList') is not None:
            for k1 in m.get('FullProcessList'):
                temp_model = main_models.DescribeFullProcessListResponseBodyFullProcessList()
                self.full_process_list.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeFullProcessListResponseBodyFullProcessList(DaraModel):
    def __init__(
        self,
        detail: str = None,
        exception: str = None,
        process_name: str = None,
        process_type: str = None,
        running_sql: str = None,
        state: str = None,
        task_id: str = None,
        time: int = None,
    ):
        # Details
        self.detail = detail
        # The abnormal status of the task. Valid values:**notstarted**. -**checking**. -**failed**. -**finished**.
        self.exception = exception
        # The name of the process.
        self.process_name = process_name
        # The type of the process. Valid values:
        # 
        # *   **1**: trusted
        # *   **2**: suspicious
        # *   **3**: malicious
        self.process_type = process_type
        # SQL that is running
        self.running_sql = running_sql
        # The log status.
        self.state = state
        # The ID of the task.
        self.task_id = task_id
        # The time when the logs were collected. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.exception is not None:
            result['Exception'] = self.exception

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_type is not None:
            result['ProcessType'] = self.process_type

        if self.running_sql is not None:
            result['RunningSQL'] = self.running_sql

        if self.state is not None:
            result['State'] = self.state

        if self.task_id is not None:
            result['TaskID'] = self.task_id

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Exception') is not None:
            self.exception = m.get('Exception')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessType') is not None:
            self.process_type = m.get('ProcessType')

        if m.get('RunningSQL') is not None:
            self.running_sql = m.get('RunningSQL')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskID') is not None:
            self.task_id = m.get('TaskID')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self


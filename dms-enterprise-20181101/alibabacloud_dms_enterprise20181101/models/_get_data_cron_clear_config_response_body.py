# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDataCronClearConfigResponseBody(DaraModel):
    def __init__(
        self,
        data_cron_clear_config: main_models.GetDataCronClearConfigResponseBodyDataCronClearConfig = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Data configuration.
        self.data_cron_clear_config = data_cron_clear_config
        # The error code.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.data_cron_clear_config:
            self.data_cron_clear_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_cron_clear_config is not None:
            result['DataCronClearConfig'] = self.data_cron_clear_config.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCronClearConfig') is not None:
            temp_model = main_models.GetDataCronClearConfigResponseBodyDataCronClearConfig()
            self.data_cron_clear_config = temp_model.from_map(m.get('DataCronClearConfig'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataCronClearConfigResponseBodyDataCronClearConfig(DaraModel):
    def __init__(
        self,
        cron_call_times: str = None,
        cron_format: str = None,
        cron_last_call_start_time: str = None,
        cron_next_call_time: str = None,
        cron_status: str = None,
        current_clear_task_count: int = None,
        duration: str = None,
        optimize_table_after_every_clear_times: int = None,
    ):
        # The number of times that the task is run.
        self.cron_call_times = cron_call_times
        # The crontab expression that you can use to run the task at a specified time. For more information, see [Crontab expression](https://help.aliyun.com/document_detail/206581.html).
        self.cron_format = cron_format
        # The time when the task was last run.
        self.cron_last_call_start_time = cron_last_call_start_time
        # The time when the task is run next time. This parameter is displayed only when the status of the scheduled task is SUCCESS.
        self.cron_next_call_time = cron_next_call_time
        # The status of the scheduled task. If this parameter is empty, it indicates the task is not run. Valid values:
        # 
        # *   PAUSE: The task is suspended.
        # *   WAITING: The task is waiting to be run.
        # *   SUCCESS: The task is complete.
        self.cron_status = cron_status
        # The number of times that the Optimize Table statement is automatically exeuted. This parameter is valid only when the value of the OptimizeTableAfterEveryClearTimes parameter is greater than 0.
        self.current_clear_task_count = current_clear_task_count
        # The execution duration of the task. Unit: hours. If the value is 0, it indicates the duration is not specified.
        self.duration = duration
        # Specifies whether to enable automatic execution of the OPTIMIZE TABLE statement. Valid values:
        # 
        # *   0: disables automatic execution
        # *   A number greater than 0: enables automatic execution. The number specifies the number of times that cleanup operations must be performed before the OPTIMIZE TABLE statement is automatically executed.
        self.optimize_table_after_every_clear_times = optimize_table_after_every_clear_times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_call_times is not None:
            result['CronCallTimes'] = self.cron_call_times

        if self.cron_format is not None:
            result['CronFormat'] = self.cron_format

        if self.cron_last_call_start_time is not None:
            result['CronLastCallStartTime'] = self.cron_last_call_start_time

        if self.cron_next_call_time is not None:
            result['CronNextCallTime'] = self.cron_next_call_time

        if self.cron_status is not None:
            result['CronStatus'] = self.cron_status

        if self.current_clear_task_count is not None:
            result['CurrentClearTaskCount'] = self.current_clear_task_count

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.optimize_table_after_every_clear_times is not None:
            result['OptimizeTableAfterEveryClearTimes'] = self.optimize_table_after_every_clear_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronCallTimes') is not None:
            self.cron_call_times = m.get('CronCallTimes')

        if m.get('CronFormat') is not None:
            self.cron_format = m.get('CronFormat')

        if m.get('CronLastCallStartTime') is not None:
            self.cron_last_call_start_time = m.get('CronLastCallStartTime')

        if m.get('CronNextCallTime') is not None:
            self.cron_next_call_time = m.get('CronNextCallTime')

        if m.get('CronStatus') is not None:
            self.cron_status = m.get('CronStatus')

        if m.get('CurrentClearTaskCount') is not None:
            self.current_clear_task_count = m.get('CurrentClearTaskCount')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('OptimizeTableAfterEveryClearTimes') is not None:
            self.optimize_table_after_every_clear_times = m.get('OptimizeTableAfterEveryClearTimes')

        return self


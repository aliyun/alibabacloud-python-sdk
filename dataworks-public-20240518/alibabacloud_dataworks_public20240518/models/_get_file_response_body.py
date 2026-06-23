# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetFileResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFileResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details of the file.
        self.data = data
        # Error code.
        self.error_code = error_code
        # Error message.
        self.error_message = error_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # Request ID. Used for troubleshooting when a fault occurs.
        self.request_id = request_id
        # Indicates whether the invocation succeeded. Valid values:
        # 
        # - true: The invocation succeeded.
        # 
        # - false: Failed to invoke.
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetFileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetFileResponseBodyData(DaraModel):
    def __init__(
        self,
        file: main_models.GetFileResponseBodyDataFile = None,
        node_configuration: main_models.GetFileResponseBodyDataNodeConfiguration = None,
        resource_download_link: main_models.GetFileResponseBodyDataResourceDownloadLink = None,
    ):
        # Basic information about the file.
        self.file = file
        # The schedule configuration of the file.
        self.node_configuration = node_configuration
        # Resource download link.
        self.resource_download_link = resource_download_link

    def validate(self):
        if self.file:
            self.file.validate()
        if self.node_configuration:
            self.node_configuration.validate()
        if self.resource_download_link:
            self.resource_download_link.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file is not None:
            result['File'] = self.file.to_map()

        if self.node_configuration is not None:
            result['NodeConfiguration'] = self.node_configuration.to_map()

        if self.resource_download_link is not None:
            result['ResourceDownloadLink'] = self.resource_download_link.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('File') is not None:
            temp_model = main_models.GetFileResponseBodyDataFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('NodeConfiguration') is not None:
            temp_model = main_models.GetFileResponseBodyDataNodeConfiguration()
            self.node_configuration = temp_model.from_map(m.get('NodeConfiguration'))

        if m.get('ResourceDownloadLink') is not None:
            temp_model = main_models.GetFileResponseBodyDataResourceDownloadLink()
            self.resource_download_link = temp_model.from_map(m.get('ResourceDownloadLink'))

        return self

class GetFileResponseBodyDataResourceDownloadLink(DaraModel):
    def __init__(
        self,
        download_link: str = None,
    ):
        # Link for downloading the resource.
        self.download_link = download_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_link is not None:
            result['downloadLink'] = self.download_link

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadLink') is not None:
            self.download_link = m.get('downloadLink')

        return self

class GetFileResponseBodyDataNodeConfiguration(DaraModel):
    def __init__(
        self,
        apply_schedule_immediately: str = None,
        auto_rerun_interval_millis: int = None,
        auto_rerun_times: int = None,
        cron_express: str = None,
        cycle_type: str = None,
        dependent_node_id_list: str = None,
        dependent_type: str = None,
        end_effect_date: int = None,
        ignore_parent_skip_running_property: str = None,
        image_id: str = None,
        input_list: List[main_models.GetFileResponseBodyDataNodeConfigurationInputList] = None,
        input_parameters: List[main_models.GetFileResponseBodyDataNodeConfigurationInputParameters] = None,
        output_list: List[main_models.GetFileResponseBodyDataNodeConfigurationOutputList] = None,
        output_parameters: List[main_models.GetFileResponseBodyDataNodeConfigurationOutputParameters] = None,
        para_value: str = None,
        rerun_mode: str = None,
        resource_group_id: int = None,
        scheduler_type: str = None,
        start_effect_date: int = None,
        start_immediately: bool = None,
        stop: bool = None,
        timeout: int = None,
    ):
        # Whether to apply the schedule configuration immediately after publishing.
        self.apply_schedule_immediately = apply_schedule_immediately
        # The time interval between automatic reruns after an error, in milliseconds.
        # 
        # This parameter corresponds to the "Rerun Interval" setting under "Schedule Configuration > Time Properties > Auto Rerun on Error" for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).<br>
        # Note that the time unit for "Rerun Interval" in the console is minutes; convert the time accordingly when invoking the API.
        self.auto_rerun_interval_millis = auto_rerun_interval_millis
        # The number of automatic reruns after an error.
        self.auto_rerun_times = auto_rerun_times
        # The Cron Expression for timed scheduling of the file.
        self.cron_express = cron_express
        # The type of recurrence, including NOT_DAY (minute, hour) and DAY (day, week, month).
        # 
        # This parameter corresponds to "Schedule Configuration > Time Properties > Recurrence" for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.cycle_type = cycle_type
        # When the DependentType parameter is set to USER_DEFINE, this parameter specifies the IDs of the nodes on which the current file depends. Separate multiple node IDs with commas (,).
        # 
        # This parameter corresponds to the configuration when, in the [DataWorks console](https://workbench.data.aliyun.com/console), the "Schedule Configuration > Schedule Dependency" of a Data Development job is set to "Previous Cycle" and the dependency option is set to "Other Nodes".
        self.dependent_node_id_list = dependent_node_id_list
        # The method of depending on the previous cycle. Valid values:
        # 
        # - SELF: The dependency is the current node itself.
        # 
        # - CHILD: The dependency is direct child nodes.
        # 
        # - USER_DEFINE: The dependency is other specified nodes.
        # 
        # - NONE: No dependency is selected, meaning the node does not depend on the previous cycle.
        self.dependent_type = dependent_type
        # The UNIX timestamp, in milliseconds, when automatic scheduling stops.
        # 
        # This parameter corresponds to the millisecond UNIX timestamp of the end time configured in the "Scan Configuration > Time Properties > Effective Date" setting for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.end_effect_date = end_effect_date
        # Schedule Configuration > Previous Cycle > Whether to ignore the upstream dry-run property.
        self.ignore_parent_skip_running_property = ignore_parent_skip_running_property
        # Custom image ID
        self.image_id = image_id
        # Information about outputs from upstream files on which this file depends.
        self.input_list = input_list
        # Return Result.
        self.input_parameters = input_parameters
        # Output information of the file.
        self.output_list = output_list
        # Return Result.
        self.output_parameters = output_parameters
        # Schedule parameter.
        # 
        # This parameter corresponds to the "Scan Configuration > Parameters" setting for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console). You can refer to the [Schedule Parameters](https://help.aliyun.com/document_detail/137548.html) documentation for configuration details.
        self.para_value = para_value
        # Rerun property. Valid values:
        # 
        # - ALL_ALLOWED: The job can be rerun regardless of whether it previously Succeeded or failed.
        # 
        # - FAILURE_ALLOWED: The job cannot be rerun if it previously Succeeded, but can be rerun if it previously failed.
        # 
        # - ALL_DENIED: The job cannot be rerun regardless of whether it previously Succeeded or failed.
        # 
        # This parameter corresponds to the "Scan Configuration > Time Properties > Rerun Property" setting for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.rerun_mode = rerun_mode
        # The resource group used when the file is published as a Job and executed. You can call [ListResourceGroups](https://help.aliyun.com/document_detail/173913.html) to obtain the list of available resource groups in the workspace.
        self.resource_group_id = resource_group_id
        # The schedule type. Valid values:
        # 
        # - NORMAL: Normal scheduling task.
        # 
        # - MANUAL: One-time task, which is not included in regular scheduling and corresponds to a node in a manually triggered workflow.
        # 
        # - PAUSE: Paused task.
        # 
        # - SKIP: Dry-run task, which is included in regular scheduling but is immediately marked as Succeeded when scheduled.
        self.scheduler_type = scheduler_type
        # The UNIX timestamp (in milliseconds) indicating when automatic scheduling starts.
        # 
        # This parameter corresponds to the start time (as a UNIX timestamp in milliseconds) configured under "Schedule Configuration > Time Properties > Effective Date" for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_effect_date = start_effect_date
        # Indicates whether to start immediately after publishing.
        # 
        # This parameter corresponds to the "Start Method" setting under "Configuration > Time Properties" in the right-side navigation bar on the editing page for EMR Spark Streaming and EMR Streaming SQL Data Development jobs in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_immediately = start_immediately
        # Indicates whether to skip execution. Valid values:
        # 
        # - true: Skip execution.
        # 
        # - false: Do not skip execution.
        # 
        # This parameter corresponds to the setting "Schedule Type" under "Schedule Configuration > Time Properties" for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console), when it is set to "skip execution".
        self.stop = stop
        # Timeout definition for scheduling configuration.
        self.timeout = timeout

    def validate(self):
        if self.input_list:
            for v1 in self.input_list:
                 if v1:
                    v1.validate()
        if self.input_parameters:
            for v1 in self.input_parameters:
                 if v1:
                    v1.validate()
        if self.output_list:
            for v1 in self.output_list:
                 if v1:
                    v1.validate()
        if self.output_parameters:
            for v1 in self.output_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_schedule_immediately is not None:
            result['ApplyScheduleImmediately'] = self.apply_schedule_immediately

        if self.auto_rerun_interval_millis is not None:
            result['AutoRerunIntervalMillis'] = self.auto_rerun_interval_millis

        if self.auto_rerun_times is not None:
            result['AutoRerunTimes'] = self.auto_rerun_times

        if self.cron_express is not None:
            result['CronExpress'] = self.cron_express

        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type

        if self.dependent_node_id_list is not None:
            result['DependentNodeIdList'] = self.dependent_node_id_list

        if self.dependent_type is not None:
            result['DependentType'] = self.dependent_type

        if self.end_effect_date is not None:
            result['EndEffectDate'] = self.end_effect_date

        if self.ignore_parent_skip_running_property is not None:
            result['IgnoreParentSkipRunningProperty'] = self.ignore_parent_skip_running_property

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        result['InputList'] = []
        if self.input_list is not None:
            for k1 in self.input_list:
                result['InputList'].append(k1.to_map() if k1 else None)

        result['InputParameters'] = []
        if self.input_parameters is not None:
            for k1 in self.input_parameters:
                result['InputParameters'].append(k1.to_map() if k1 else None)

        result['OutputList'] = []
        if self.output_list is not None:
            for k1 in self.output_list:
                result['OutputList'].append(k1.to_map() if k1 else None)

        result['OutputParameters'] = []
        if self.output_parameters is not None:
            for k1 in self.output_parameters:
                result['OutputParameters'].append(k1.to_map() if k1 else None)

        if self.para_value is not None:
            result['ParaValue'] = self.para_value

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type

        if self.start_effect_date is not None:
            result['StartEffectDate'] = self.start_effect_date

        if self.start_immediately is not None:
            result['StartImmediately'] = self.start_immediately

        if self.stop is not None:
            result['Stop'] = self.stop

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyScheduleImmediately') is not None:
            self.apply_schedule_immediately = m.get('ApplyScheduleImmediately')

        if m.get('AutoRerunIntervalMillis') is not None:
            self.auto_rerun_interval_millis = m.get('AutoRerunIntervalMillis')

        if m.get('AutoRerunTimes') is not None:
            self.auto_rerun_times = m.get('AutoRerunTimes')

        if m.get('CronExpress') is not None:
            self.cron_express = m.get('CronExpress')

        if m.get('CycleType') is not None:
            self.cycle_type = m.get('CycleType')

        if m.get('DependentNodeIdList') is not None:
            self.dependent_node_id_list = m.get('DependentNodeIdList')

        if m.get('DependentType') is not None:
            self.dependent_type = m.get('DependentType')

        if m.get('EndEffectDate') is not None:
            self.end_effect_date = m.get('EndEffectDate')

        if m.get('IgnoreParentSkipRunningProperty') is not None:
            self.ignore_parent_skip_running_property = m.get('IgnoreParentSkipRunningProperty')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        self.input_list = []
        if m.get('InputList') is not None:
            for k1 in m.get('InputList'):
                temp_model = main_models.GetFileResponseBodyDataNodeConfigurationInputList()
                self.input_list.append(temp_model.from_map(k1))

        self.input_parameters = []
        if m.get('InputParameters') is not None:
            for k1 in m.get('InputParameters'):
                temp_model = main_models.GetFileResponseBodyDataNodeConfigurationInputParameters()
                self.input_parameters.append(temp_model.from_map(k1))

        self.output_list = []
        if m.get('OutputList') is not None:
            for k1 in m.get('OutputList'):
                temp_model = main_models.GetFileResponseBodyDataNodeConfigurationOutputList()
                self.output_list.append(temp_model.from_map(k1))

        self.output_parameters = []
        if m.get('OutputParameters') is not None:
            for k1 in m.get('OutputParameters'):
                temp_model = main_models.GetFileResponseBodyDataNodeConfigurationOutputParameters()
                self.output_parameters.append(temp_model.from_map(k1))

        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')

        if m.get('StartEffectDate') is not None:
            self.start_effect_date = m.get('StartEffectDate')

        if m.get('StartImmediately') is not None:
            self.start_immediately = m.get('StartImmediately')

        if m.get('Stop') is not None:
            self.stop = m.get('Stop')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class GetFileResponseBodyDataNodeConfigurationOutputParameters(DaraModel):
    def __init__(
        self,
        description: str = None,
        parameter_name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The description of the output parameter in the edge zone context.
        self.description = description
        # The parameter name of the output parameter in the node context.
        # 
        # This parameter corresponds to the "Parameter Name" field under "Schedule Configuration > Node Context > Output Parameters of This Node" for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.parameter_name = parameter_name
        # The type of the expression for the edge zone context output parameter. Valid values are as follows:
        # 
        # - 1: constant
        # 
        # - 2: variable
        # 
        # - 3: pass-through variable from a parameter node
        # 
        # This parameter corresponds to the "Type" field in the "Scan Configuration > Edge Zone Context > Output Parameters of This Node" section for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.type = type
        # The expression of the output parameter in the edge zone context.
        # 
        # This parameter corresponds to the "Value" field in the "Scan Configuration > Edge Zone Context > Output Parameters of This Node" section for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetFileResponseBodyDataNodeConfigurationOutputList(DaraModel):
    def __init__(
        self,
        output: str = None,
        ref_table_name: str = None,
    ):
        # Output name of the file.
        # 
        # This parameter corresponds to the value in the "Output Name" column when "Same Cycle" is selected under "Scan Configuration > Schedule Dependency" for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output = output
        # Output value of the file.
        # 
        # This parameter corresponds to the value in the "Output Table" column when "Same Cycle" is selected under "Scan Configuration > Schedule Dependency" for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.ref_table_name = ref_table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['Output'] = self.output

        if self.ref_table_name is not None:
            result['RefTableName'] = self.ref_table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('RefTableName') is not None:
            self.ref_table_name = m.get('RefTableName')

        return self

class GetFileResponseBodyDataNodeConfigurationInputParameters(DaraModel):
    def __init__(
        self,
        parameter_name: str = None,
        value_source: str = None,
    ):
        # The parameter name of the input parameter in the node context. You can reference this parameter in code by using the ${...} syntax.
        # 
        # This parameter corresponds to the "Parameter Name" field under "Schedule Configuration > Node Context > Input Parameters of This Node" in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.parameter_name = parameter_name
        # The value source of the input parameter in the node context.
        # 
        # This parameter corresponds to the "Value Source" field under "Schedule Configuration > Node Context > Input Parameters of This Node" in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.value_source = value_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.value_source is not None:
            result['ValueSource'] = self.value_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ValueSource') is not None:
            self.value_source = m.get('ValueSource')

        return self

class GetFileResponseBodyDataNodeConfigurationInputList(DaraModel):
    def __init__(
        self,
        input: str = None,
        parse_type: str = None,
    ):
        # The output name of the upstream file on which this file depends.
        # 
        # This parameter corresponds to "Parent Node Output Name" when "Same Cycle" is selected under "Schedule Configuration > Schedule Dependency" for a Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.input = input
        # The method for configuring file dependencies. Valid values:
        # 
        # - MANUAL: Manually configured.
        # 
        # - AUTO: Automatically parsed.
        self.parse_type = parse_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input

        if self.parse_type is not None:
            result['ParseType'] = self.parse_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('ParseType') is not None:
            self.parse_type = m.get('ParseType')

        return self

class GetFileResponseBodyDataFile(DaraModel):
    def __init__(
        self,
        advanced_settings: str = None,
        auto_parsing: bool = None,
        biz_id: int = None,
        business_id: int = None,
        commit_status: int = None,
        connection_name: str = None,
        content: str = None,
        create_time: int = None,
        create_user: str = None,
        current_version: int = None,
        deleted_status: str = None,
        file_description: str = None,
        file_folder_id: str = None,
        file_id: int = None,
        file_name: str = None,
        file_type: int = None,
        is_max_compute: bool = None,
        last_edit_time: int = None,
        last_edit_user: str = None,
        node_id: int = None,
        owner: str = None,
        parent_id: int = None,
        use_type: str = None,
    ):
        # Advanced configuration of the job.
        # 
        # This parameter corresponds to "Advanced Settings" in the right-side navigation bar on the editing page of an EMR Data Development job in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # > Currently, EMR Shell jobs do not support advanced parameters.
        # 
        # For details about advanced parameters for different EMR job types, see [EMR Job Development](https://help.aliyun.com/document_detail/473077.html).
        self.advanced_settings = advanced_settings
        # Indicates whether automatic parsing is enabled for the file. Valid values:
        # 
        # - true: The code in the file is automatically parsed.
        # 
        # - false: The code in the file is not automatically parsed.
        # 
        # This parameter corresponds to the "Code Parsing" option in the DataWorks console (https\\://workbench.data.aliyun.com/console) when you select "Same Cycle" under Schedule Configuration > Schedule Dependency for a Data Development job.
        self.auto_parsing = auto_parsing
        # The ID of the Business Process to which the file belongs. This field is deprecated. Use the BusinessId field instead.
        self.biz_id = biz_id
        # The Business Process ID of the file.
        self.business_id = business_id
        # The current commit status of the file. Valid values:
        # 
        # - 0: The latest code has not been submitted.
        # 
        # - 1: The latest code has been submitted.
        self.commit_status = commit_status
        # The name of the data source used when executing the job corresponding to the file.
        self.connection_name = connection_name
        # The code of the file.
        self.content = content
        # UNIX timestamp when the file was created, in milliseconds.
        self.create_time = create_time
        # The Alibaba Cloud User ID of the file creator.
        self.create_user = create_user
        # Version number of the latest submitted version of the file.
        self.current_version = current_version
        # The deletion status of the file. Valid values:
        # 
        # - NORMAL: Not deleted.
        # 
        # - RECYCLE_BIN: In the recycle bin.
        # 
        # - DELETED: Deleted.
        self.deleted_status = deleted_status
        # The description of the file.
        self.file_description = file_description
        # The ID of the folder to which the file belongs.
        self.file_folder_id = file_folder_id
        # The ID of the file.
        self.file_id = file_id
        # Name of the file.
        self.file_name = file_name
        # The code type of the file. Different file types use different code. For more information, see [DataWorks Edge Zone Collection](https://help.aliyun.com/document_detail/600169.html).
        self.file_type = file_type
        # Indicates whether the resource file needs to be uploaded to MaxCompute.
        # Configure this parameter only when the file is a MaxCompute resource file.
        self.is_max_compute = is_max_compute
        # The UNIX timestamp of the most recent edit to the file, in milliseconds.
        self.last_edit_time = last_edit_time
        # The Alibaba Cloud User ID of the user who last edited the file.
        self.last_edit_user = last_edit_user
        # The ID of the scheduling task generated in the CDN mapping system after the file is submitted.
        self.node_id = node_id
        # Alibaba Cloud User ID of the file owner.
        self.owner = owner
        # If the current file is an internal file of a composite edge zone file, this field identifies the ID of the corresponding composite edge zone file.
        self.parent_id = parent_id
        # The function module to which the file belongs. Valid values:
        # 
        # - NORMAL: Data Development.
        # 
        # - MANUAL: One-time task.
        # 
        # - MANUAL_BIZ: Manually triggered workflow.
        # 
        # - SKIP: Dry-run scheduling in Data Development.
        # 
        # - ADHOCQUERY: Ad-hoc query.
        # 
        # - COMPONENT: Widget Management.
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_settings is not None:
            result['AdvancedSettings'] = self.advanced_settings

        if self.auto_parsing is not None:
            result['AutoParsing'] = self.auto_parsing

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.commit_status is not None:
            result['CommitStatus'] = self.commit_status

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.deleted_status is not None:
            result['DeletedStatus'] = self.deleted_status

        if self.file_description is not None:
            result['FileDescription'] = self.file_description

        if self.file_folder_id is not None:
            result['FileFolderId'] = self.file_folder_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.is_max_compute is not None:
            result['IsMaxCompute'] = self.is_max_compute

        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time

        if self.last_edit_user is not None:
            result['LastEditUser'] = self.last_edit_user

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.use_type is not None:
            result['UseType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedSettings') is not None:
            self.advanced_settings = m.get('AdvancedSettings')

        if m.get('AutoParsing') is not None:
            self.auto_parsing = m.get('AutoParsing')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('CommitStatus') is not None:
            self.commit_status = m.get('CommitStatus')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('DeletedStatus') is not None:
            self.deleted_status = m.get('DeletedStatus')

        if m.get('FileDescription') is not None:
            self.file_description = m.get('FileDescription')

        if m.get('FileFolderId') is not None:
            self.file_folder_id = m.get('FileFolderId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('IsMaxCompute') is not None:
            self.is_max_compute = m.get('IsMaxCompute')

        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')

        if m.get('LastEditUser') is not None:
            self.last_edit_user = m.get('LastEditUser')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('UseType') is not None:
            self.use_type = m.get('UseType')

        return self


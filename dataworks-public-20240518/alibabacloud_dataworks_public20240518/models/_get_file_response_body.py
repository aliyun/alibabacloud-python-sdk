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
        # The details of the file.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        # The basic information about the file.
        self.file = file
        # The scheduling configurations of the file.
        self.node_configuration = node_configuration
        # The download URL of the resource.
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
        # The download URL of the resource.
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
        # Indicates whether scheduling configurations immediately take effect after the deployment.
        self.apply_schedule_immediately = apply_schedule_immediately
        # The interval between automatic reruns after an error occurs. Unit: milliseconds.
        # 
        # This parameter corresponds to the Rerun interval parameter that is displayed after the Auto Rerun upon Failure check box is selected in the Schedule section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console). The interval that you specify in the DataWorks console is measured in minutes. Pay attention to the conversion between the units of time when you call the operation.
        self.auto_rerun_interval_millis = auto_rerun_interval_millis
        # The number of automatic reruns that are allowed after an error occurs.
        self.auto_rerun_times = auto_rerun_times
        # The cron expression that represents the periodic scheduling policy of the node.
        self.cron_express = cron_express
        # The type of the scheduling cycle. Valid values: NOT_DAY and DAY. The value NOT_DAY indicates that the node is scheduled to run by minute or hour. The value DAY indicates that the node is scheduled to run by day, week, or month.
        # 
        # This parameter corresponds to the Scheduling Cycle parameter in the Schedule section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.cycle_type = cycle_type
        # The ID of the node on which the node that corresponds to the file depends when the DependentType parameter is set to USER_DEFINE. Multiple IDs are separated by commas (,).
        # 
        # The value of this parameter is equivalent to the ID of the node that you specified after you select Previous Cycle and set Depend On to Other Nodes in the Dependencies section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.dependent_node_id_list = dependent_node_id_list
        # The type of the cross-cycle scheduling dependency of the node. Valid values:
        # 
        # *   SELF: The instance generated for the node in the current cycle depends on the instance generated for the node in the previous cycle.
        # *   CHILD: The instance generated for the node in the current cycle depends on the instances generated for the descendant nodes at the nearest level of the node in the previous cycle.
        # *   USER_DEFINE: The instance generated for the node in the current cycle depends on the instances generated for one or more specified nodes in the previous cycle.
        # *   NONE: No cross-cycle scheduling dependency type is selected for the node.
        self.dependent_type = dependent_type
        # The end of the time range for automatic scheduling. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # Configuring this parameter is equivalent to specifying an end time for the Validity Period parameter in the Schedule section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.end_effect_date = end_effect_date
        # Indicates whether the dry-run property of the ancestor nodes of the node is skipped. This parameter corresponds to the Skip the dry-run property of the ancestor node parameter that is displayed after you configure the Depend On parameter in the Dependencies section of the Properties tab on the DataStudio page in the DataWorks console.
        self.ignore_parent_skip_running_property = ignore_parent_skip_running_property
        # The custom image ID.
        self.image_id = image_id
        # The output information about the parent files on which the current file depends.
        self.input_list = input_list
        # The input parameters of the node.
        self.input_parameters = input_parameters
        # The output information about the current file.
        self.output_list = output_list
        # The output parameters of the node.
        self.output_parameters = output_parameters
        # The scheduling parameters of the node.
        # 
        # This parameter corresponds to the Scheduling Parameter section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console). For more information about the configurations of scheduling parameters, see [Configure scheduling parameters](https://help.aliyun.com/document_detail/137548.html).
        self.para_value = para_value
        # Indicates whether the node that corresponds to the file can be rerun. Valid values:
        # 
        # *   ALL_ALLOWED: The node can be rerun regardless of whether it is successfully run or fails to run.
        # *   FAILURE_ALLOWED: The node can be rerun only after it fails to run.
        # *   ALL_DENIED: The node cannot be rerun regardless of whether it is successfully run or fails to run.
        # 
        # This parameter corresponds to the Rerun parameter in the Schedule section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.rerun_mode = rerun_mode
        # The ID of the resource group that is used to run the node that corresponds to the file. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/173913.html) operation to query the available resource groups in the workspace.
        self.resource_group_id = resource_group_id
        # The scheduling type of the node. Valid values:
        # 
        # *   NORMAL: The node is an auto triggered node.
        # *   MANUAL: The node is a manually triggered node. Manually triggered nodes cannot be automatically triggered. They correspond to the nodes in the Manually Triggered Workflows pane.
        # *   PAUSE: The node is a paused node.
        # *   SKIP: The node is a dry-run node. Dry-run nodes are started as scheduled, but the system sets the status of the nodes to successful when it starts to run them.
        self.scheduler_type = scheduler_type
        # The beginning of the time range for automatic scheduling. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # Configuring this parameter is equivalent to specifying a start time for the Validity Period parameter in the Schedule section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_effect_date = start_effect_date
        # Indicates whether a node is immediately run after the node is deployed to the production environment.
        # 
        # This parameter is valid only for an EMR Spark Streaming node or an EMR Streaming SQL node. This parameter corresponds to the Start Method parameter in the Schedule section of the Configure tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_immediately = start_immediately
        # Indicates whether the scheduling for the node is suspended Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter corresponds to the Recurrence parameter in the Schedule section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.stop = stop
        # The timeout period.
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
        # The description of the output parameter of the node.
        self.description = description
        # The name of the output parameter of the node.
        # 
        # This parameter corresponds to the Parameter Name parameter in the Output Parameters table in the Input and Output Parameters section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.parameter_name = parameter_name
        # The type of the output parameter of the node. Valid values:
        # 
        # *   1: indicates a constant.
        # *   2: indicates a variable.
        # *   3: indicates a pass-through variable.
        # 
        # This parameter corresponds to the Type parameter in the Output Parameters table in the Input and Output Parameters section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.type = type
        # The value of the output parameter of the node.
        # 
        # This parameter corresponds to the Value parameter in the Output Parameters table in the Input and Output Parameters section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
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
        # The output name of the current file.
        # 
        # This parameter corresponds to the Output Name parameter under Output after Same Cycle is selected in the Dependencies section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output = output
        # The output table name of the current file.
        # 
        # This parameter corresponds to the Output Table Name parameter under Output after Same Cycle is selected in the Dependencies section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
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
        # The name of the input parameter of the node. In the code, you can use the ${...} method to reference the input parameter of the node.
        # 
        # This parameter corresponds to the Parameter Name parameter in the Input Parameters table in the Input and Output Parameters section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.parameter_name = parameter_name
        # The value source of the input parameter of the node.
        # 
        # This parameter corresponds to the Value Source parameter in the Input Parameters table in the Input and Output Parameters section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
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
        # The output name of the parent file on which the current file depends.
        # 
        # This parameter corresponds to the Output Name of Ancestor Node parameter under Parent Nodes after Same Cycle is selected in the Dependencies section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.input = input
        # The mode of the configuration file dependency. Valid values:
        # 
        # *   MANUAL: Scheduling dependencies are manually configured.
        # *   AUTO: Scheduling dependencies are automatically parsed.
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
        # The advanced configurations of the node.
        # 
        # This parameter is valid for an EMR node. This parameter corresponds to the Advanced Settings tab in the right-side navigation pane on the configuration tab of the node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # >  You cannot configure advanced parameters for EMR Shell nodes.
        # 
        # For information about the advanced parameters of each type of EMR node, see [Develop EMR tasks](https://help.aliyun.com/document_detail/473077.html).
        self.advanced_settings = advanced_settings
        # Indicates whether the automatic parsing feature is enabled for the file. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter corresponds to the Automatic Parsing From Code Before Node Committing parameter that is displayed after you select Same Cycle in the Dependencies section of the Properties tab on the DataStudio page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.auto_parsing = auto_parsing
        # The ID of the workflow to which the file belongs. This parameter is deprecated and replaced by the BusinessId parameter.
        self.biz_id = biz_id
        # The ID of the workflow to which the file belongs.
        self.business_id = business_id
        # Indicates whether the latest code in the file is committed. Valid values: 0 and 1. The value 0 indicates that the latest code in the file is not committed. The value 1 indicates that the latest code in the file is committed.
        self.commit_status = commit_status
        # The name of the data source that is used to run the node that corresponds to the file.
        self.connection_name = connection_name
        # The code in the file.
        self.content = content
        # The time when the file was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account used to create the file.
        self.create_user = create_user
        # The latest version number of the file.
        self.current_version = current_version
        # The status of the file. Valid values:
        # 
        # *   NORMAL: The file is not deleted.
        # *   RECYCLE_BIN: The file is stored in the recycle bin.
        # *   DELETED: The file is deleted.
        self.deleted_status = deleted_status
        # The description of the file.
        self.file_description = file_description
        # The ID of the folder to which the file belongs.
        self.file_folder_id = file_folder_id
        # The file ID.
        self.file_id = file_id
        # The name of the file.
        self.file_name = file_name
        # The type of the code for the file. The code for files varies based on the file type. For more information, see [DataWorks nodes](https://help.aliyun.com/document_detail/600169.html).
        self.file_type = file_type
        # Indicates whether the resource file needs to be uploaded to MaxCompute. This parameter is returned only if the file is a MaxCompute resource file.
        self.is_max_compute = is_max_compute
        # The time when the file was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_edit_time = last_edit_time
        # The ID of the Alibaba Cloud account used to last modify the file.
        self.last_edit_user = last_edit_user
        # The ID of the auto triggered node that is generated in the scheduling system after the file is committed.
        self.node_id = node_id
        # The ID of the Alibaba Cloud account used by the file owner.
        self.owner = owner
        # The ID of the node group file to which the current file belongs. This parameter is returned only if the current file is an inner file of the node group file.
        self.parent_id = parent_id
        # The module to which the file belongs. Valid values:
        # 
        # *   NORMAL: The file is used for DataStudio.
        # *   MANUAL: The file is used for a manually triggered node.
        # *   MANUAL_BIZ: The file is used for a manually triggered workflow.
        # *   SKIP: The file is used for a dry-run node in DataStudio.
        # *   ADHOCQUERY: The file is used for an ad hoc query.
        # *   COMPONENT: The file is used for a script template.
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


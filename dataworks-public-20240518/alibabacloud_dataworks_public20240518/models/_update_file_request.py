# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFileRequest(DaraModel):
    def __init__(
        self,
        advanced_settings: str = None,
        apply_schedule_immediately: bool = None,
        auto_parsing: bool = None,
        auto_rerun_interval_millis: int = None,
        auto_rerun_times: int = None,
        connection_name: str = None,
        content: str = None,
        cron_express: str = None,
        cycle_type: str = None,
        dependent_node_id_list: str = None,
        dependent_type: str = None,
        end_effect_date: int = None,
        file_description: str = None,
        file_folder_path: str = None,
        file_id: int = None,
        file_name: str = None,
        ignore_parent_skip_running_property: bool = None,
        image_id: str = None,
        input_list: str = None,
        input_parameters: str = None,
        output_list: str = None,
        output_parameters: str = None,
        owner: str = None,
        para_value: str = None,
        project_id: int = None,
        project_identifier: str = None,
        rerun_mode: str = None,
        resource_group_identifier: str = None,
        scheduler_type: str = None,
        start_effect_date: int = None,
        start_immediately: bool = None,
        stop: bool = None,
        timeout: int = None,
    ):
        # The advanced settings for the task.
        # 
        # This parameter corresponds to the Advanced Settings in the right-side navigation pane on the editing page for EMR Spark Streaming and EMR Streaming SQL tasks in Data Studio in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # Currently, only EMR Spark Streaming and EMR Streaming SQL tasks support this parameter, and the parameter must be in JSON format.
        self.advanced_settings = advanced_settings
        # Specifies whether to apply the scheduling configuration immediately after the file is published.
        self.apply_schedule_immediately = apply_schedule_immediately
        # Specifies whether to enable automatic parsing for the file. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter corresponds to the Analyze Code setting in Properties > Dependencies for data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.auto_parsing = auto_parsing
        # The interval at which the node is automatically rerun after a failure. Unit: milliseconds. Maximum value: 1800000 milliseconds (30 minutes).
        # 
        # This parameter corresponds to the Rerun interval parameter in Properties > Schedule > Auto Rerun upon Failure for data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console). In the console, the unit of the rerun interval is minutes. Convert the time unit when you call this operation.
        self.auto_rerun_interval_millis = auto_rerun_interval_millis
        # The number of automatic reruns after the file execution fails.
        self.auto_rerun_times = auto_rerun_times
        # The name of the data source that is used to run the node. You can call the [ListDataSources](https://help.aliyun.com/document_detail/211431.html) operation to query the available data sources.
        self.connection_name = connection_name
        # The file code content. Different code types (fileType) have different code formats. In Operation Center, you can right-click a task of the corresponding type and select View Code to view the specific code format.
        self.content = content
        # The cron expression for scheduled execution. This parameter corresponds to the Cron Expression setting in Scheduling > Scheduling Time for Data Studio tasks in the [DataWorks console](https://workbench.data.aliyun.com/console). After you configure Scheduling Cycle and Scheduled Time, DataWorks automatically generates a cron expression.
        # 
        # Examples:
        # 
        # *   Scheduled at 05:30 every day: `00 30 05 * * ?`
        # *   Scheduled at the 15th minute of every hour: `00 15 * * * ?`
        # *   Scheduled every 10 minutes: `00 00/10 * * * ?`
        # *   Scheduled every 10 minutes between 08:00 and 23:00 every day: `00 00-59/10 8-23 * * * ?`
        # *   Scheduled at 00:20 on the 1st day of every month: `00 20 00 1 * ?`
        # *   Scheduled every 3 months starting from 00:10 on January 1: `00 10 00 1 1-12/3 ?`
        # *   Scheduled at 00:05 on every Tuesday and Friday: `00 05 00 * * 2,5`
        # 
        # Due to the rules of the DataWorks scheduling system, cron expressions have the following restrictions:
        # 
        # *   The minimum scheduling interval is 5 minutes.
        # *   The earliest scheduling time each day is 00:05.
        self.cron_express = cron_express
        # The type of scheduling cycle. Valid values: NOT_DAY (minute, hour) and DAY (day, week, month).
        # 
        # This parameter corresponds to the Scheduling Cycle setting in Scheduling > Scheduling Time for Data Studio tasks in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.cycle_type = cycle_type
        # The IDs of the nodes on which the current node depends. This parameter takes effect only when the DependentType parameter is set to USER_DEFINE. Separate multiple node IDs with commas (,).
        # 
        # This parameter corresponds to the Other Nodes option in Properties > Dependencies > Cross-cycle Dependency (Original Previous-cycle Dependency) for data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.dependent_node_id_list = dependent_node_id_list
        # The dependency mode on the previous cycle. Valid values:
        # 
        # *   SELF: Depends on the current node.
        # *   CHILD: Depends on the child nodes.
        # *   USER_DEFINE: Depends on other nodes.
        # *   NONE: No dependencies. Does not depend on the previous cycle.
        self.dependent_type = dependent_type
        # The timestamp (in milliseconds) when automatic scheduling stops.
        # 
        # This parameter corresponds to the end time of Effective Period in Scheduling > Scheduling Time for Data Studio tasks in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.end_effect_date = end_effect_date
        # The file description.
        self.file_description = file_description
        # The path to the folder where the file is located.
        self.file_folder_path = file_folder_path
        # The file ID. You can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to obtain the file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The file name. You can modify the file name by setting a new value for FileName. For example, you can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to query the file ID in the target directory, and then call the [UpdateFile](https://help.aliyun.com/document_detail/173951.html) operation with the file ID specified in the FileId parameter and a new value specified in the FileName parameter to modify the file name.
        self.file_name = file_name
        # This parameter corresponds to the Skip The Dry-Run Property Of The Ancestor Node option in Properties > Dependencies > Cross-cycle Dependency (Original Previous-cycle Dependency) when Instances of Current Node or Level-1 Child Node is selected for data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.ignore_parent_skip_running_property = ignore_parent_skip_running_property
        # The custom image ID.
        self.image_id = image_id
        # The output names of the ancestor nodes on which the current node depends. Separate multiple output names with commas (,).
        # 
        # This parameter corresponds to the Output Name of Ancestor Node setting in Properties > Dependencies for data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # > This parameter is required when you call the CreateDISyncTask or UpdateFile operation to create a batch synchronization node.
        self.input_list = input_list
        # The input context parameters of the node. The value must be in the JSON format. For more information about the parameter structure, see the InputContextParameterList parameter in the response parameters of the [GetFile](https://help.aliyun.com/document_detail/173954.html) operation.
        # 
        # This parameter corresponds to the Input Parameters setting in Properties > Input and Output Parameters for data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.input_parameters = input_parameters
        # The outputs of the node.
        # 
        # This parameter corresponds to the Output Name setting in Properties > Dependencies for data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output_list = output_list
        # The output context parameters of the node. The value must be in the JSON format. For more information about the parameter structure, see the OutputContextParameterList parameter in the response parameters of the [GetFile](https://help.aliyun.com/document_detail/173954.html) operation.
        # 
        # This parameter corresponds to the Output Parameters setting in Properties > Input and Output Parameters for data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output_parameters = output_parameters
        # The file owner ID.
        self.owner = owner
        # The scheduling parameters of the node.
        # 
        # This parameter corresponds to the Scheduling Parameter setting in Properties for data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console). For more information, see [Scheduling parameters](https://help.aliyun.com/document_detail/137548.html).
        self.para_value = para_value
        # The DataWorks workspace ID. To obtain the ID, log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and navigate to the workspace management page.
        self.project_id = project_id
        # The DataWorks workspace name. To obtain the workspace name, log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and navigate to the workspace configuration page.
        # 
        # You must specify either this parameter or ProjectId to identify the target DataWorks workspace for this API call.
        self.project_identifier = project_identifier
        # The rerun policy. Valid values:
        # 
        # *   ALL_ALLOWED: Reruns are allowed regardless of whether the task succeeds or fails.
        # *   FAILURE_ALLOWED: Reruns are allowed only when the task fails.
        # *   ALL_DENIED: Reruns are not allowed regardless of whether the task succeeds or fails.
        # 
        # This parameter corresponds to the Support for Rerun setting in Scheduling > Scheduling Policies for Data Studio tasks in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # Valid values:
        # 
        # *   ALL_ALLOWD
        # *   FAILURE_ALLOWED
        # *   ALL_DENIED
        # *   ALL_ALLOWED
        self.rerun_mode = rerun_mode
        # The resource group for the task published from the file. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/173913.html) operation to query the available resource groups in the workspace.
        self.resource_group_identifier = resource_group_identifier
        # The scheduling type. Valid values:
        # 
        # *   NORMAL: Normal scheduled task.
        # *   MANUAL: Manually triggered node. Not scheduled for daily execution. Corresponds to nodes in manually triggered workflows.
        # *   PAUSE: Paused task.
        # *   SKIP: Dry-run task. Scheduled for daily execution but is directly marked as successful when scheduling starts.
        self.scheduler_type = scheduler_type
        # The timestamp (in milliseconds) when automatic scheduling starts.
        # 
        # This parameter corresponds to the start time of Effective Period in Scheduling > Scheduling Time for Data Studio tasks in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_effect_date = start_effect_date
        # Specifies whether to start the task immediately after it is published. Valid values:
        # 
        # *   true: Start the task immediately after it is published.
        # *   false: Do not start the task immediately after it is published.
        # 
        # This parameter corresponds to the Start Method setting in Configuration > Scheduling Policies in the right-side navigation pane on the editing page for EMR Spark Streaming and EMR Streaming SQL tasks in Data Studio in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_immediately = start_immediately
        # Specifies whether to skip execution. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter corresponds to the Skip Execution option in Properties > Schedule > Recurrence for data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.stop = stop
        # The timeout settings for scheduling configuration.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_settings is not None:
            result['AdvancedSettings'] = self.advanced_settings

        if self.apply_schedule_immediately is not None:
            result['ApplyScheduleImmediately'] = self.apply_schedule_immediately

        if self.auto_parsing is not None:
            result['AutoParsing'] = self.auto_parsing

        if self.auto_rerun_interval_millis is not None:
            result['AutoRerunIntervalMillis'] = self.auto_rerun_interval_millis

        if self.auto_rerun_times is not None:
            result['AutoRerunTimes'] = self.auto_rerun_times

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.content is not None:
            result['Content'] = self.content

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

        if self.file_description is not None:
            result['FileDescription'] = self.file_description

        if self.file_folder_path is not None:
            result['FileFolderPath'] = self.file_folder_path

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.ignore_parent_skip_running_property is not None:
            result['IgnoreParentSkipRunningProperty'] = self.ignore_parent_skip_running_property

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.input_list is not None:
            result['InputList'] = self.input_list

        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters

        if self.output_list is not None:
            result['OutputList'] = self.output_list

        if self.output_parameters is not None:
            result['OutputParameters'] = self.output_parameters

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.para_value is not None:
            result['ParaValue'] = self.para_value

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier

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
        if m.get('AdvancedSettings') is not None:
            self.advanced_settings = m.get('AdvancedSettings')

        if m.get('ApplyScheduleImmediately') is not None:
            self.apply_schedule_immediately = m.get('ApplyScheduleImmediately')

        if m.get('AutoParsing') is not None:
            self.auto_parsing = m.get('AutoParsing')

        if m.get('AutoRerunIntervalMillis') is not None:
            self.auto_rerun_interval_millis = m.get('AutoRerunIntervalMillis')

        if m.get('AutoRerunTimes') is not None:
            self.auto_rerun_times = m.get('AutoRerunTimes')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

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

        if m.get('FileDescription') is not None:
            self.file_description = m.get('FileDescription')

        if m.get('FileFolderPath') is not None:
            self.file_folder_path = m.get('FileFolderPath')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('IgnoreParentSkipRunningProperty') is not None:
            self.ignore_parent_skip_running_property = m.get('IgnoreParentSkipRunningProperty')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InputList') is not None:
            self.input_list = m.get('InputList')

        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')

        if m.get('OutputList') is not None:
            self.output_list = m.get('OutputList')

        if m.get('OutputParameters') is not None:
            self.output_parameters = m.get('OutputParameters')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')

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


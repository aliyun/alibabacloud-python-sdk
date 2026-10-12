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
        # The advanced settings of the task.
        # 
        # This parameter corresponds to the Advanced Settings section in the right-side navigation pane of the edit page for EMR Spark Streaming and EMR Streaming SQL data development tasks in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # Currently, only EMR Spark Streaming and EMR Streaming SQL tasks support this parameter, and the parameter value must be in JSON format.
        self.advanced_settings = advanced_settings
        # Specifies whether the scheduling configuration takes effect immediately after the file is published.
        self.apply_schedule_immediately = apply_schedule_immediately
        # Specifies whether to enable the automatic parsing feature for the file. Valid values:
        # - true: The file automatically parses code.
        # - false: The file does not automatically parse code.
        # 
        # This parameter corresponds to the Code Parsing parameter in the Schedule > Scheduling Dependencies section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.auto_parsing = auto_parsing
        # The interval between automatic reruns after a failure, in milliseconds. The maximum value is 1800000, which indicates 30 minutes.
        # 
        # This parameter corresponds to the Rerun Interval parameter in the Schedule > Time Attributes > Auto Rerun upon Failure section of the [DataWorks console](https://workbench.data.aliyun.com/console). The unit of the Rerun Interval parameter in the console is minutes. Convert the time unit when you call this operation.
        self.auto_rerun_interval_millis = auto_rerun_interval_millis
        # The number of automatic reruns allowed after an error occurs.
        self.auto_rerun_times = auto_rerun_times
        # The identifier of the data source used when the task corresponding to the file is executed. You can call the [ListDataSources](https://help.aliyun.com/document_detail/211431.html) operation to obtain the list of available data sources.
        self.connection_name = connection_name
        # The code content of the file. The code format varies based on the file type. You can go to Operation Center, right-click a task of the corresponding type, and select View Code to view the specific code format.
        self.content = content
        # The cron expression for periodic scheduling. This parameter corresponds to the cron expression in the Schedule > Time Property section for the data development task in the [DataWorks console](https://workbench.data.aliyun.com/console). After you configure the scheduling cycle and timed scheduling time, DataWorks automatically generates the corresponding cron expression.
        # 
        # Examples:
        # 
        # - Schedule a task at 05:30 every day: `00 30 05 * * ?`.
        # 
        # - Schedule a task at the 15th minute of every hour: `00 15 * * * ?`.
        # 
        # - Schedule a task every 10 minutes: `00 00/10 * * * ?`.
        # 
        # - Schedule a task every 10 minutes from 08:00 to 17:00 every day: `00 00-59/10 8-23 * * * ?`.
        # 
        # - Schedule a task at 00:20 on the first day of every month: `00 20 00 1 * ?`.
        # 
        # - Schedule a task every three months starting from 00:10 on January 1: `00 10 00 1 1-12/3 ?`.
        # 
        # - Schedule a task at 00:05 every Tuesday and Friday: `00 05 00 * * 2,5`.
        # 
        # Due to the rules of the DataWorks scheduling system, cron expressions have the following limits:
        # 
        # - The minimum scheduling interval is 5 minutes.
        # 
        # - The earliest scheduling time of a day is 00:05.
        self.cron_express = cron_express
        # The type of the scheduling cycle. Valid values: NOT_DAY (minutes and hours) and DAY (days, weeks, and months).
        # 
        # This parameter corresponds to the Schedule Type parameter in the Schedule > Time Attributes section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.cycle_type = cycle_type
        # The IDs of the nodes on which the current file depends when the parameter settings of DependentType are set to USER_DEFINE. Separate multiple node IDs with commas (,).
        # 
        # This parameter corresponds to the content configured when you set the Dependency parameter to Cross-cycle Dependency (Previous Cycle) and select Other Nodes in the Schedule > Scheduling Dependencies section for the data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.dependent_node_id_list = dependent_node_id_list
        # The dependency on the previous cycle. Valid values:
        # 
        # - SELF: The current node.
        # - CHILD: The child nodes at the first level.
        # - USER_DEFINE: Other nodes.
        # - NONE: No dependency on the previous cycle.
        self.dependent_type = dependent_type
        # The end time of automatic scheduling, in the form of a millisecond timestamp.
        # 
        # This parameter corresponds to the end time in the Schedule > Time Attributes > Effective Date section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.end_effect_date = end_effect_date
        # The description of the file.
        self.file_description = file_description
        # The path where the file is stored.
        self.file_folder_path = file_folder_path
        # The ID of the file. You can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to obtain the file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The name of the file. You can change the file name by resetting the value of FileName. For example, you can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to query the ID of a file in the destination directory, call the [UpdateFile](https://help.aliyun.com/document_detail/173951.html) operation, specify the queried file ID in the FileId parameter, and configure the FileName parameter to change the name of the file.
        self.file_name = file_name
        # This parameter corresponds to the Skip Dry Run of Upstream Nodes parameter that is configured when you set the Dependency parameter to Cross-cycle Dependency (Previous Cycle) and select Current Node or Child Nodes at First Level in the Schedule > Scheduling Dependencies section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.ignore_parent_skip_running_property = ignore_parent_skip_running_property
        # The ID of the custom image.
        self.image_id = image_id
        # The output names of the upstream files on which the current file depends. Separate multiple output names with commas (,).
        # 
        # This parameter corresponds to the Output Name of Upstream Node parameter in the Schedule > Scheduling Dependencies section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # > This parameter is required when you create a offline synchronization task by calling the CreateDISyncTask or UpdateFile operation.
        self.input_list = input_list
        # The context input parameters of the node. The parameter value is in JSON format. For the included fields, refer to the InputContextParameterList parameter structure in the response of the [GetFile](https://help.aliyun.com/document_detail/173954.html) operation.
        # 
        # This parameter corresponds to the Input Parameters of Current Node parameter in the Schedule > Node Context Parameters section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.input_parameters = input_parameters
        # The output of the file.
        # 
        # This parameter corresponds to the Output Name of Current Node parameter in the Schedule > Scheduling Dependencies section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output_list = output_list
        # The context output parameters of the node. The parameter value is in JSON format. For the included fields, refer to the OutputContextParameterList parameter structure in the response of the [GetFile](https://help.aliyun.com/document_detail/173954.html) operation.
        # 
        # This parameter corresponds to the Output Parameters of Current Node parameter in the Schedule > Node Context Parameters section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output_parameters = output_parameters
        # The user ID of the file owner.
        self.owner = owner
        # The scheduling parameters.
        # 
        # This parameter corresponds to the Scheduling Parameters section in the Schedule section of the [DataWorks console](https://workbench.data.aliyun.com/console). For more information, see [Scheduling parameters](https://help.aliyun.com/document_detail/137548.html).
        self.para_value = para_value
        # The ID of the DataWorks workspace. You can logon to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the ID.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Settings page to obtain the workspace name.
        # 
        # You must specify either this parameter or the ProjectId parameter to determine the DataWorks workspace for this API call.
        self.project_identifier = project_identifier
        # The rerun mode. Valid values:
        # 
        # - ALL_ALLOWED: The task can be rerun regardless of whether it is successfully run or fails to run.
        # - FAILURE_ALLOWED: The task can be rerun only after it fails to run.
        # - ALL_DENIED: The task cannot be rerun regardless of whether it is successfully run or fails to run.
        # 
        # This parameter corresponds to the Rerun Mode parameter in the Schedule > Time Attributes section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.rerun_mode = rerun_mode
        # The resource group used when the task is executed after the file is published as a task. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/173913.html) operation to obtain the list of available resource groups in the workspace.
        self.resource_group_identifier = resource_group_identifier
        # The scheduling type. Valid values:
        # 
        # - NORMAL: Normal scheduling task.
        # - MANUAL: Manual task. It is not scheduled on a daily basis and corresponds to a node in a manual workflow.
        # - PAUSE: Paused task.
        # - SKIP: Dry-run task. It is scheduled on a daily basis, but its status is directly set to successful when the scheduling is triggered.
        self.scheduler_type = scheduler_type
        # The start time of automatic scheduling, in the form of a millisecond timestamp.
        # 
        # This parameter corresponds to the start time in the Schedule > Time Attributes > Effective Date section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_effect_date = start_effect_date
        # Specifies whether to start the task immediately after it is published. Valid values:
        # 
        # - true: Start the task immediately after it is published.
        # - false: Do not start the task immediately after it is published.
        # 
        # This parameter corresponds to the Startup Method parameter in the Configuration > Time Attributes section in the right-side navigation pane of the edit page for EMR Spark Streaming and EMR Streaming SQL data development tasks in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_immediately = start_immediately
        # Specifies whether to pause scheduling. Valid values:
        # 
        # - true: Pause scheduling.
        # - false: Do not pause scheduling.
        # 
        # This parameter corresponds to the Pause Scheduling option in the Schedule > Time Attributes > Schedule Type section of the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.stop = stop
        # The timeout definition in the scheduling configuration.
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


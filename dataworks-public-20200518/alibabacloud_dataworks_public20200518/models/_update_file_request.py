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
        # The advanced settings of the node.
        # 
        # This parameter corresponds to the Advanced Settings in the right-side navigation pane on the editing page for EMR Spark Streaming and EMR Streaming SQL data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # Currently, only EMR Spark Streaming and EMR Streaming SQL nodes support this parameter. The parameter value is in JSON format.
        self.advanced_settings = advanced_settings
        # Specifies whether the scheduling configuration takes effect immediately after publishing.
        self.apply_schedule_immediately = apply_schedule_immediately
        # Specifies whether to enable the automatic parsing feature for the file. Valid values:
        # - true: The file automatically parses code.
        # - false: The file does not automatically parse code.
        # 
        # This parameter corresponds to the Code Parsing setting when you select Same Cycle under Scheduling Configuration > Scheduling Dependency for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.auto_parsing = auto_parsing
        # The interval between automatic reruns upon an error, in milliseconds. The maximum value is 1800000 milliseconds (30 minutes).
        # 
        # This parameter corresponds to the Rerun Interval setting under Scheduling Configuration > Time Properties > Auto Rerun upon Error for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # The time unit for Rerun Interval in the console is minutes. Convert the time accordingly when calling this operation.
        self.auto_rerun_interval_millis = auto_rerun_interval_millis
        # The number of automatic reruns after an error occurs.
        self.auto_rerun_times = auto_rerun_times
        # The identifier of the data source used when the node corresponding to the file runs. You can call the [ListDataSources](https://help.aliyun.com/document_detail/211431.html) operation to obtain the list of available data sources.
        self.connection_name = connection_name
        # The code content of the file. Files of different code types (fileType) have different code formats. In Operation Center, right-click a node of the corresponding type and select View Code to view the specific code format.
        self.content = content
        # The cron expression for timed scheduling. This parameter corresponds to the cron Expression setting under Scheduling Configuration > Time Property for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console). After you configure the Scheduling Epoch and Timed Scheduling time, DataWorks automatically generates the corresponding cron expression.
        # 
        # Examples:
        # 
        # - Timed scheduling at 05:30 every day: `00 30 05 * * ?`.
        # 
        # - Timed scheduling at the 15th minute of every hour: `00 15 * * * ?`.
        # 
        # - Schedule every 10 minutes: `00 00/10 * * * ?`.
        # 
        # - Schedule every 10 minutes from 08:00 to 17:00 every day: `00 00-59/10 8-23 * * * ?`.
        # 
        # - Timed scheduling at 00:20 on the 1st of every month: `00 20 00 1 * ?`.
        # 
        # - Schedule every 3 months starting from 00:10 on January 1: `00 10 00 1 1-12/3 ?`.
        # 
        # - Timed scheduling at 00:05 every Tuesday and Friday: `00 05 00 * * 2,5`.
        # 
        # 
        # The cron expression has the following limits due to the DataWorks scheduling system rules:
        # 
        # - The minimum scheduling interval is 5 minutes.
        # 
        # - The earliest scheduling time each day is 00:05.
        self.cron_express = cron_express
        # The type of the scheduling cycle. Valid values: NOT_DAY (minute or hour) and DAY (day, week, or month).
        # 
        # This parameter corresponds to the Scheduling Cycle setting under Scheduling Configuration > Time Properties for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.cycle_type = cycle_type
        # The IDs of the nodes on which the current file depends when DependentType is set to USER_DEFINE. Separate multiple node IDs with commas (,).
        # 
        # This parameter corresponds to the Settings when you select Other Nodes as the dependency after configuring Scheduling Configuration > Scheduling Dependency to Previous Epoch for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console). This is part of the parameter settings for scheduling dependencies.
        self.dependent_node_id_list = dependent_node_id_list
        # The mode in which the node depends on the previous cycle. Valid values:
        # - SELF: The dependency is set to the current node.
        # - CHILD: The dependency is set to first-level child nodes.
        # - USER_DEFINE: The dependency is set to other nodes.
        # - NONE: No dependency is selected. The node does not depend on the previous cycle.
        self.dependent_type = dependent_type
        # The timestamp in milliseconds when automatic scheduling stops.
        # 
        # This parameter corresponds to the end time in milliseconds under Scheduling Configuration > Time Properties > Effective Date for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.end_effect_date = end_effect_date
        # The description of the file.
        self.file_description = file_description
        # The path of the file.
        self.file_folder_path = file_folder_path
        # The ID of the file. You can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to obtain the file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The name of the file. You can modify the file name by setting FileName to a new value.
        # For example, call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to query the file ID in the target folder, and then call the [UpdateFile](https://help.aliyun.com/document_detail/173951.html) operation to specify the file ID for the FileId parameter and configure the FileName parameter to rename the file.
        self.file_name = file_name
        # Specifies whether to skip the dry-run property of the upstream node under Scheduling Configuration > Previous Cycle.
        self.ignore_parent_skip_running_property = ignore_parent_skip_running_property
        # The custom image ID.
        self.image_id = image_id
        # The output names of the upstream files on which the current file depends. Separate multiple output names with commas (,).
        # 
        # This parameter corresponds to the Parent Node Output Name setting when you select Same Cycle under Scheduling Configuration > Scheduling Dependency for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # > This parameter is required when you create a batch synchronization node by calling CreateDISyncTask and UpdateFile.
        self.input_list = input_list
        # The input context parameters of the node. The parameter value is in JSON format. For the fields included, refer to the InputContextParameterList parameter structure in the response of the [GetFile](https://help.aliyun.com/document_detail/173954.html) operation.
        # 
        # This parameter corresponds to the Input Parameters of Current Node setting under Scheduling Configuration > Node Context for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.input_parameters = input_parameters
        # The output of the file.
        # 
        # This parameter corresponds to the Output Name of Current Node setting when you select Same Cycle under Scheduling Configuration > Scheduling Dependency for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output_list = output_list
        # The output context parameters of the node. The parameter value is in JSON format. For the fields included, refer to the OutputContextParameterList parameter structure in the response of the [GetFile](https://help.aliyun.com/document_detail/173954.html) operation.
        # 
        # This parameter corresponds to the Output Parameters of Current Node setting under Scheduling Configuration > Node Context for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output_parameters = output_parameters
        # The user ID of the file owner.
        self.owner = owner
        # The scheduling parameters.
        # 
        # This parameter corresponds to the Parameters setting under Scheduling Configuration for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console). For more information, see [Scheduling parameters](https://help.aliyun.com/document_detail/137548.html).
        self.para_value = para_value
        # The ID of the DataWorks workspace. You can logon to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Storage Management page to obtain the ID.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Settings page to obtain the workspace name.
        # 
        # You must specify either this parameter or ProjectId to determine the DataWorks workspace for this API call.
        self.project_identifier = project_identifier
        # The rerun property. Valid values:
        # - ALL_ALLOWED: The node can be rerun regardless of whether it runs successfully or fails.
        # - FAILURE_ALLOWED: The node can be rerun only after it fails.
        # - ALL_DENIED: The node cannot be rerun regardless of whether it runs successfully or fails.
        # 
        # This parameter corresponds to the Rerun Property setting under Scheduling Configuration > Time Properties > Rerun Property for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.rerun_mode = rerun_mode
        # The schedule resource used when the file is published as a node and the node runs. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/173913.html) operation to obtain the list of available resource groups for the workspace.
        self.resource_group_identifier = resource_group_identifier
        # The scheduling type. Valid values:
        # - NORMAL: A normal scheduling node.
        # - MANUAL: A manual node that is not scheduled on a daily basis. This corresponds to nodes in a manual workflow.
        # - PAUSE: A paused node.
        # - SKIP: A dry-run node that is scheduled on a daily basis but is directly set to successful when scheduling starts.
        self.scheduler_type = scheduler_type
        # The timestamp in milliseconds when automatic scheduling starts.
        # 
        # This parameter corresponds to the start time in milliseconds under Scheduling Configuration > Time Properties > Effective Date for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_effect_date = start_effect_date
        # Specifies whether to start the node immediately after publishing. Valid values:
        # - true: Starts immediately after publishing.
        # - false: Does not start after publishing.
        # 
        # This parameter corresponds to the Start Mode setting under Configuration > Time Properties in the right-side navigation pane on the editing page for EMR Spark Streaming and EMR Streaming SQL data development nodes in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_immediately = start_immediately
        # Specifies whether to pause scheduling. Valid values:
        # - true: Pauses scheduling.
        # - false: Does not pause scheduling.
        # 
        # This parameter corresponds to the setting when Scheduling Type is set to Pause Scheduling under Scheduling Configuration > Time Properties > Scheduling Type for a data development node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.stop = stop
        # The timeout setting for the scheduling configuration.
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


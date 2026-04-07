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
        # The advanced configurations of the node.
        # 
        # This parameter is valid only for an EMR Spark Streaming node or an EMR Streaming SQL node. This parameter corresponds to the Advanced Settings tab of the node in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # This parameter is configured in the JSON format.
        self.advanced_settings = advanced_settings
        # Specifies whether scheduling configurations immediately take effect after the node is deployed.
        self.apply_schedule_immediately = apply_schedule_immediately
        # Specifies whether the automatic parsing feature is enabled for the file. Valid values:
        # 
        # *   true: The automatic parsing feature is enabled for the file.
        # *   false: The automatic parsing feature is not enabled for the file.
        # 
        # This parameter corresponds to the Analyze Code parameter that is displayed after Same Cycle is selected in the Dependencies section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.auto_parsing = auto_parsing
        # The interval between two consecutive automatic reruns after an error occurs. Unit: milliseconds. Maximum value: 1800000 (30 minutes).
        # 
        # This parameter corresponds to the Rerun Interval parameter that is displayed after the Auto Rerun upon Error check box is selected in the Schedule section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # The interval that you specify in the DataWorks console is measured in minutes. Pay attention to the conversion between the units of time when you call the operation.
        self.auto_rerun_interval_millis = auto_rerun_interval_millis
        # The number of automatic reruns that are allowed after an error occurs.
        self.auto_rerun_times = auto_rerun_times
        # The name of the connected data source that is used to run the node. You can call the [ListDataSources](https://help.aliyun.com/document_detail/211431.html) operation to query the available data sources of the workspace.
        self.connection_name = connection_name
        # The code of the file. The code format varies based on the file type. To view the code format for a specific file type, go to Operation Center, right-click a node of the file type, and then select View Code.
        self.content = content
        # The CRON expression that represents the periodic scheduling policy of the node. This parameter corresponds to the Cron Expression parameter in the Schedule section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console). After you configure the Scheduling Cycle and Run At parameters in the DataWorks console, DataWorks automatically generates a value for the Cron Expression parameter.
        # 
        # Examples:
        # 
        # *   CRON expression for a node that is scheduled to run at 05:30 every day: `00 30 05 * * ?`
        # *   CRON expression for a node that is scheduled to run at the fifteenth minute of each hour: `00 15 * * * ?`
        # *   CRON expression for a node that is scheduled to run every 10 minutes: `00 00/10 * * * ?`
        # *   CRON expression for a node that is scheduled to run every 10 minutes from 08:00 to 17:00 every day: `00 00-59/10 8-23 * * * ?`
        # *   CRON expression for a node that is scheduled to run at 00:20 on the first day of each month: `00 20 00 1 * ?`
        # *   CRON expression for a node that is scheduled to run every three months starting from 00:10 on January 1: `00 10 00 1 1-12/3 ?`
        # *   CRON expression for a node that is scheduled to run at 00:05 every Tuesday and Friday: `00 05 00 * * 2,5`
        # 
        # The scheduling system of DataWorks imposes the following limits on CRON expressions:
        # 
        # *   A node can be scheduled to run at a minimum interval of 5 minutes.
        # *   A node can be scheduled to run at 00:05 every day at the earliest.
        self.cron_express = cron_express
        # The type of the scheduling cycle of the node that corresponds to the file. Valid values: NOT_DAY and DAY. The value NOT_DAY indicates that the node is scheduled to run by minute or hour. The value DAY indicates that the node is scheduled to run by day, week, or month.
        # 
        # This parameter corresponds to the Scheduling Cycle parameter in the Schedule section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.cycle_type = cycle_type
        # The ID of the node on which the node corresponding to the file depends when the DependentType parameter is set to USER_DEFINE. Multiple IDs are separated by commas (,).
        # 
        # The value of this parameter corresponds to the ID of the node that you specified after you select Previous Cycle and set Depend On to Other Nodes in the Dependencies section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.dependent_node_id_list = dependent_node_id_list
        # The type of the cross-cycle scheduling dependency of the node. Valid values:
        # 
        # *   SELF: The instance generated for the node in the current cycle depends on the instance generated for the node in the previous cycle.
        # *   CHILD: The instance generated for the node in the current cycle depends on the instances generated for the descendant nodes at the nearest level of the node in the previous cycle.
        # *   USER_DEFINE: The instance generated for the node in the current cycle depends on the instances generated for one or more specified nodes in the previous cycle.
        # *   NONE: No cross-cycle scheduling dependency type is selected for the node.
        self.dependent_type = dependent_type
        # The end time of automatic scheduling. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter corresponds to the end time specified for the Validity Period parameter in the Schedule section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.end_effect_date = end_effect_date
        # The description of the file.
        self.file_description = file_description
        # The path of the file.
        self.file_folder_path = file_folder_path
        # The ID of the file. You can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The name of the file. You can set the FileName parameter to a new value to change the file name.
        # 
        # You can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to query the ID of the file whose name you want to change. Then, you can set the FileId parameter to the ID and set the FileName parameter to a new value when you call the [UpdateFile](https://help.aliyun.com/document_detail/173951.html) operation.
        self.file_name = file_name
        # Specifies whether to skip the dry-run property of the ancestor nodes of the node. This parameter corresponds to the Skip the dry-run property of the ancestor node parameter that is displayed after you configure the Depend On parameter in the Dependencies section of the Properties tab in the DataWorks console.
        self.ignore_parent_skip_running_property = ignore_parent_skip_running_property
        # The ID of the custom image.
        self.image_id = image_id
        # The output name of the parent file on which the current file depends. If you specify multiple output names, separate them with commas (,).
        # 
        # This parameter corresponds to the Parent Nodes parameter that is displayed after you select Same Cycle in the Dependencies section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # >  You must configure this parameter when you call the CreateDISyncTask or UpdateFile operation to create a batch synchronization task.
        self.input_list = input_list
        # The input parameters of the node. This parameter is configured in the JSON format. For more information about the input parameters, refer to the InputContextParameterList parameter in the Response parameters section of the [GetFile](https://help.aliyun.com/document_detail/173954.html) operation.
        # 
        # This parameter corresponds to the Input Parameters table in the Input and Output Parameters section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.input_parameters = input_parameters
        # The output name of the current file.
        # 
        # This parameter corresponds to the Output Name parameter in the Dependencies section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output_list = output_list
        # The output parameters of the node. This parameter is configured in the JSON format. For more information about the output parameters, refer to the OutputContextParameterList parameter in the Response parameters section of the [GetFile](https://help.aliyun.com/document_detail/173954.html) operation.
        # 
        # This parameter corresponds to the Output Parameters table in the Input and Output Parameters section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output_parameters = output_parameters
        # The ID of the file owner.
        self.owner = owner
        # The scheduling parameters of the node.
        # 
        # This parameter corresponds to the Parameters section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console). For more information, see [Configure scheduling parameters](https://help.aliyun.com/document_detail/137548.html).
        self.para_value = para_value
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the workspace name.
        # 
        # You must configure this parameter or the ProjectId parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_identifier = project_identifier
        # Specifies whether the node that corresponds to the file can be rerun. Valid values:
        # 
        # *   ALL_ALLOWED: The node can be rerun regardless of whether it is successfully run or fails to run.
        # *   FAILURE_ALLOWED: The node can be rerun only after it fails to run.
        # *   ALL_DENIED: The node cannot be rerun regardless of whether it is successfully run or fails to run.
        # 
        # This parameter corresponds to the Rerun parameter in the Schedule section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # Valid values:
        # 
        # *   ALL_ALLOWD
        # *   FAILURE_ALLOWED
        # *   ALL_DENIED
        # *   ALL_ALLOWED
        self.rerun_mode = rerun_mode
        # The identifier of the resource group that is used to run the node. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/173913.html) operation to query the available resource groups in the workspace.
        self.resource_group_identifier = resource_group_identifier
        # The scheduling type of the node. Valid values:
        # 
        # *   NORMAL: The node is an auto triggered node.
        # *   MANUAL: The node is a manually triggered node. Manually triggered nodes cannot be automatically triggered. They correspond to the nodes in the Manually Triggered Workflows pane.
        # *   PAUSE: The node is a paused node.
        # *   SKIP: The node is a dry-run node. Dry-run nodes are started as scheduled, but the system sets the status of the nodes to successful when it starts to run them.
        self.scheduler_type = scheduler_type
        # The start time of automatic scheduling. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter corresponds to the Validity Period parameter in the Schedule section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_effect_date = start_effect_date
        # Specifies whether to immediately run a node after the node is deployed to the production environment. Valid values:
        # 
        # *   true: A node is immediately run after the node is deployed to the production environment.
        # *   false: A node is not immediately run after the node is deployed to the production environment.
        # 
        # This parameter is valid only for an EMR Spark Streaming node or an EMR Streaming SQL node. This parameter corresponds to the Start Method parameter in the Schedule section of the Configure tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.start_immediately = start_immediately
        # Specifies whether to suspend the scheduling of the node. Valid values:
        # 
        # *   true: suspends the scheduling of the node.
        # *   false: does not suspend the scheduling of the node.
        # 
        # This parameter corresponds to the Recurrence parameter in the Schedule section of the Properties tab in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.stop = stop
        # The timeout period.
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


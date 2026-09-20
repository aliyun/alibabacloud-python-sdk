# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetIDEEventDetailResponseBody(DaraModel):
    def __init__(
        self,
        event_detail: main_models.GetIDEEventDetailResponseBodyEventDetail = None,
        request_id: str = None,
    ):
        # The data snapshot at the time the extension point event was triggered.
        # 
        # Different types of message events have different valid fields in the data snapshot. For details, refer to the field descriptions of each message event.
        self.event_detail = event_detail
        # The unique ID of the request, which can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.event_detail:
            self.event_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_detail is not None:
            result['EventDetail'] = self.event_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventDetail') is not None:
            temp_model = main_models.GetIDEEventDetailResponseBodyEventDetail()
            self.event_detail = temp_model.from_map(m.get('EventDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetIDEEventDetailResponseBodyEventDetail(DaraModel):
    def __init__(
        self,
        committed_file: main_models.GetIDEEventDetailResponseBodyEventDetailCommittedFile = None,
        deleted_file: main_models.GetIDEEventDetailResponseBodyEventDetailDeletedFile = None,
        file_execution_command: main_models.GetIDEEventDetailResponseBodyEventDetailFileExecutionCommand = None,
        table_model: main_models.GetIDEEventDetailResponseBodyEventDetailTableModel = None,
    ):
        # The snapshot when a file is committed or deployed.
        # 
        # This field is valid only when the Message type is IDE_FILE_SUBMIT_BEFORE or IDE_FILE_DEPLOY_BEFORE.
        self.committed_file = committed_file
        # The snapshot information when a file is deleted. This field is valid only when the Message type is IDE_FILE_DELETE_BEFORE.
        self.deleted_file = deleted_file
        # The snapshot when file code is executed. This field is valid only when the Message type is IDE_FILE_EXECUTE_BEFORE.
        self.file_execution_command = file_execution_command
        # The snapshot when a table is committed or deployed. This field is valid only when the Message type is IDE_TABLE_SUBMIT_BEFORE or IDE_TABLE_DEPLOY_BEFORE.
        self.table_model = table_model

    def validate(self):
        if self.committed_file:
            self.committed_file.validate()
        if self.deleted_file:
            self.deleted_file.validate()
        if self.file_execution_command:
            self.file_execution_command.validate()
        if self.table_model:
            self.table_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.committed_file is not None:
            result['CommittedFile'] = self.committed_file.to_map()

        if self.deleted_file is not None:
            result['DeletedFile'] = self.deleted_file.to_map()

        if self.file_execution_command is not None:
            result['FileExecutionCommand'] = self.file_execution_command.to_map()

        if self.table_model is not None:
            result['TableModel'] = self.table_model.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommittedFile') is not None:
            temp_model = main_models.GetIDEEventDetailResponseBodyEventDetailCommittedFile()
            self.committed_file = temp_model.from_map(m.get('CommittedFile'))

        if m.get('DeletedFile') is not None:
            temp_model = main_models.GetIDEEventDetailResponseBodyEventDetailDeletedFile()
            self.deleted_file = temp_model.from_map(m.get('DeletedFile'))

        if m.get('FileExecutionCommand') is not None:
            temp_model = main_models.GetIDEEventDetailResponseBodyEventDetailFileExecutionCommand()
            self.file_execution_command = temp_model.from_map(m.get('FileExecutionCommand'))

        if m.get('TableModel') is not None:
            temp_model = main_models.GetIDEEventDetailResponseBodyEventDetailTableModel()
            self.table_model = temp_model.from_map(m.get('TableModel'))

        return self

class GetIDEEventDetailResponseBodyEventDetailTableModel(DaraModel):
    def __init__(
        self,
        columns: List[main_models.GetIDEEventDetailResponseBodyEventDetailTableModelColumns] = None,
        comment: str = None,
        data_source_name: str = None,
        env: str = None,
        life_cycle: int = None,
        location: str = None,
        table_name: str = None,
    ):
        # The list of columns.
        self.columns = columns
        # The comment of the table.
        self.comment = comment
        # The unique identifier of the data source to which the table belongs.
        self.data_source_name = data_source_name
        # The environment to which the table belongs. Valid values:
        # - DEV: development environment.
        # - PROD: production environment.
        self.env = env
        # The lifecycle of the table. Unit: days.
        self.life_cycle = life_cycle
        # The location information of the external table.
        self.location = location
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.env is not None:
            result['Env'] = self.env

        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle

        if self.location is not None:
            result['Location'] = self.location

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.GetIDEEventDetailResponseBodyEventDetailTableModelColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('LifeCycle') is not None:
            self.life_cycle = m.get('LifeCycle')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetIDEEventDetailResponseBodyEventDetailTableModelColumns(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        column_type: str = None,
        comment: str = None,
        is_partition_column: bool = None,
    ):
        # The name of the column.
        self.column_name = column_name
        # The type of the column.
        self.column_type = column_type
        # The comment of the column.
        self.comment = comment
        # Indicates whether the column is a partition column. Valid values:
        # - true: The column is a partition column.
        # - false: The column is not a partition column.
        self.is_partition_column = is_partition_column

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.is_partition_column is not None:
            result['IsPartitionColumn'] = self.is_partition_column

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('IsPartitionColumn') is not None:
            self.is_partition_column = m.get('IsPartitionColumn')

        return self

class GetIDEEventDetailResponseBodyEventDetailFileExecutionCommand(DaraModel):
    def __init__(
        self,
        content: str = None,
        data_source_name: str = None,
        file_id: int = None,
        file_type: int = None,
    ):
        # The file code that generated this file version.
        self.content = content
        # The unique identifier of the data source associated with the file.
        self.data_source_name = data_source_name
        # The ID of the file.
        self.file_id = file_id
        # The file type. Different file types have different code. For more information, see [DataWorks nodes](https://help.aliyun.com/document_detail/600169.html).
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_type is not None:
            result['FileType'] = self.file_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        return self

class GetIDEEventDetailResponseBodyEventDetailDeletedFile(DaraModel):
    def __init__(
        self,
        business_id: int = None,
        content: str = None,
        current_version: int = None,
        data_source_name: str = None,
        file_id: int = None,
        file_name: str = None,
        file_type: int = None,
        folder_id: str = None,
        node_id: int = None,
        owner: str = None,
        parent_file_id: int = None,
        use_type: str = None,
    ):
        # The ID of the workflow to which the file belongs.
        self.business_id = business_id
        # The file code that generated this file version.
        self.content = content
        # The latest version of the file.
        self.current_version = current_version
        # The unique identifier of the data source associated with the file.
        self.data_source_name = data_source_name
        # The ID of the file.
        self.file_id = file_id
        # The name of the file.
        self.file_name = file_name
        # The file type. Different file types have different code. For more information, see [DataWorks nodes](https://help.aliyun.com/document_detail/600169.html).
        self.file_type = file_type
        # The ID of the folder to which the file belongs. You can call the [GetFolder](https://help.aliyun.com/document_detail/173952.html) operation to query file details by folder ID.
        self.folder_id = folder_id
        # The ID of the scheduling node.
        self.node_id = node_id
        # The owner of the file.
        self.owner = owner
        # The node ID of the loop node or traversal node to which the file belongs.
        self.parent_file_id = parent_file_id
        # The functional module to which the file belongs. Valid values:
        # - NORMAL: DataStudio.
        # - MANUAL: manual task.
        # - MANUAL_BIZ: manual workflow.
        # - SKIP: dry-run scheduling in DataStudio.
        # - ADHOCQUERY: ad hoc query.
        # - COMPONENT: component management.
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.content is not None:
            result['Content'] = self.content

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parent_file_id is not None:
            result['ParentFileId'] = self.parent_file_id

        if self.use_type is not None:
            result['UseType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParentFileId') is not None:
            self.parent_file_id = m.get('ParentFileId')

        if m.get('UseType') is not None:
            self.use_type = m.get('UseType')

        return self

class GetIDEEventDetailResponseBodyEventDetailCommittedFile(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        comment: str = None,
        committor: str = None,
        content: str = None,
        file_id: int = None,
        file_name: str = None,
        file_property_content: main_models.GetIDEEventDetailResponseBodyEventDetailCommittedFileFilePropertyContent = None,
        file_type: int = None,
        node_configuration: main_models.GetIDEEventDetailResponseBodyEventDetailCommittedFileNodeConfiguration = None,
        node_id: int = None,
        use_type: str = None,
    ):
        # The change type of this file version. Valid values: CREATE, UPDATE, and DELETE.
        self.change_type = change_type
        # The description of this file version.
        self.comment = comment
        # The Alibaba Cloud user ID that generated this file version.
        self.committor = committor
        # The file code that generated this file version.
        self.content = content
        # The ID of the file.
        self.file_id = file_id
        # The name of the file.
        self.file_name = file_name
        # The additional properties of the file.
        self.file_property_content = file_property_content
        # The file type. Different file types have different code. For more information, see [DataWorks nodes](https://help.aliyun.com/document_detail/600169.html).
        self.file_type = file_type
        # The scheduling configuration of the file.
        self.node_configuration = node_configuration
        # The ID of the scheduling node.
        self.node_id = node_id
        # The functional module to which the file belongs. Valid values:
        # - NORMAL: DataStudio.
        # - MANUAL: manual task.
        # - MANUAL_BIZ: manual workflow.
        # - SKIP: dry-run scheduling in DataStudio.
        # - ADHOCQUERY: ad hoc query.
        # - COMPONENT: component management.
        self.use_type = use_type

    def validate(self):
        if self.file_property_content:
            self.file_property_content.validate()
        if self.node_configuration:
            self.node_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.committor is not None:
            result['Committor'] = self.committor

        if self.content is not None:
            result['Content'] = self.content

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_property_content is not None:
            result['FilePropertyContent'] = self.file_property_content.to_map()

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.node_configuration is not None:
            result['NodeConfiguration'] = self.node_configuration.to_map()

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.use_type is not None:
            result['UseType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Committor') is not None:
            self.committor = m.get('Committor')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FilePropertyContent') is not None:
            temp_model = main_models.GetIDEEventDetailResponseBodyEventDetailCommittedFileFilePropertyContent()
            self.file_property_content = temp_model.from_map(m.get('FilePropertyContent'))

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('NodeConfiguration') is not None:
            temp_model = main_models.GetIDEEventDetailResponseBodyEventDetailCommittedFileNodeConfiguration()
            self.node_configuration = temp_model.from_map(m.get('NodeConfiguration'))

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('UseType') is not None:
            self.use_type = m.get('UseType')

        return self

class GetIDEEventDetailResponseBodyEventDetailCommittedFileNodeConfiguration(DaraModel):
    def __init__(
        self,
        auto_rerun_interval_millis: int = None,
        auto_rerun_times: int = None,
        cron_express: str = None,
        cycle_type: str = None,
        dependent_node_id_list: str = None,
        dependent_type: str = None,
        input_list: List[main_models.GetIDEEventDetailResponseBodyEventDetailCommittedFileNodeConfigurationInputList] = None,
        output_list: List[main_models.GetIDEEventDetailResponseBodyEventDetailCommittedFileNodeConfigurationOutputList] = None,
        para_value: str = None,
        rerun_mode: str = None,
        resource_group_id: int = None,
        scheduler_type: str = None,
    ):
        # The interval between automatic reruns, in milliseconds.
        self.auto_rerun_interval_millis = auto_rerun_interval_millis
        # The number of automatic reruns.
        self.auto_rerun_times = auto_rerun_times
        # The scheduling cron expression.
        self.cron_express = cron_express
        # The type of the scheduling cycle. Valid values: NOT_DAY (minute or hour) and DAY (day, week, or month).
        # 
        # This parameter corresponds to the "Schedule Configuration > Time Properties > Scheduling Cycle" setting of a DataStudio task in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.cycle_type = cycle_type
        # The IDs of the nodes on which the current file depends when the DependentType parameter settings are set to USER_DEFINE. Separate multiple node IDs with commas (,).
        # 
        # This parameter corresponds to the "Settings > Scheduling Dependencies > Cross-epoch Dependencies (Previous Epoch)" setting of a DataStudio task in the [DataWorks console](https://workbench.data.aliyun.com/console), when the dependency is set to "Other Nodes".
        self.dependent_node_id_list = dependent_node_id_list
        # The method of depending on the previous cycle. Valid values:
        # - SELF: the dependency is set to the current node.
        # - CHILD: the dependency is set to first-level child nodes.
        # - USER_DEFINE: the dependency is set to other nodes.
        # - NONE: no dependency is selected, meaning the node does not depend on the previous cycle.
        self.dependent_type = dependent_type
        # The upstream file outputs on which the file depends.
        self.input_list = input_list
        # The outputs of the file.
        # 
        # This parameter corresponds to the "Schedule Configuration > Scheduling Dependencies > Output Name of Current Node" setting of a DataStudio task in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output_list = output_list
        # The scheduling parameters.
        # 
        # This parameter corresponds to the "Schedule Configuration > Parameters" setting of a DataStudio task in the [DataWorks console](https://workbench.data.aliyun.com/console). For more information, see [Scheduling parameters](https://help.aliyun.com/document_detail/137548.html).
        self.para_value = para_value
        # The rerun property. Valid values:
        # - ALL_ALLOWED: The node can be rerun regardless of whether it runs successfully or fails.
        # - FAILURE_ALLOWED: The node can be rerun only after it fails.
        # - ALL_DENIED: The node cannot be rerun regardless of whether it runs successfully or fails.
        # 
        # This parameter corresponds to the "Schedule Configuration > Time Properties > Rerun Properties" setting of a DataStudio task in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.rerun_mode = rerun_mode
        # The resource group used when the task is executed after the file is deployed. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/173913.html) operation to obtain the list of available resource groups for the workspace.
        self.resource_group_id = resource_group_id
        # The scheduling type. Valid values:
        # - NORMAL: normal scheduling task.
        # - MANUAL: manual task that is not scheduled on a regular basis. This corresponds to nodes in a manual workflow.
        # - PAUSE: paused task.
        # - SKIP: dry-run task that is scheduled on a regular basis but is directly set to successful when scheduling starts.
        self.scheduler_type = scheduler_type

    def validate(self):
        if self.input_list:
            for v1 in self.input_list:
                 if v1:
                    v1.validate()
        if self.output_list:
            for v1 in self.output_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        result['InputList'] = []
        if self.input_list is not None:
            for k1 in self.input_list:
                result['InputList'].append(k1.to_map() if k1 else None)

        result['OutputList'] = []
        if self.output_list is not None:
            for k1 in self.output_list:
                result['OutputList'].append(k1.to_map() if k1 else None)

        if self.para_value is not None:
            result['ParaValue'] = self.para_value

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        self.input_list = []
        if m.get('InputList') is not None:
            for k1 in m.get('InputList'):
                temp_model = main_models.GetIDEEventDetailResponseBodyEventDetailCommittedFileNodeConfigurationInputList()
                self.input_list.append(temp_model.from_map(k1))

        self.output_list = []
        if m.get('OutputList') is not None:
            for k1 in m.get('OutputList'):
                temp_model = main_models.GetIDEEventDetailResponseBodyEventDetailCommittedFileNodeConfigurationOutputList()
                self.output_list.append(temp_model.from_map(k1))

        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')

        return self

class GetIDEEventDetailResponseBodyEventDetailCommittedFileNodeConfigurationOutputList(DaraModel):
    def __init__(
        self,
        output: str = None,
        ref_table_name: str = None,
    ):
        # The output name of the file.
        # 
        # This parameter corresponds to the "Output Name" in the "Schedule Configuration > Scheduling Dependencies > Output Name of Current Node" setting of a DataStudio task in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.output = output
        # The output table name of the file.
        # 
        # This parameter corresponds to the "Output Table Name" in the "Schedule Configuration > Scheduling Dependencies > Output Name of Current Node" setting of a DataStudio task in the [DataWorks console](https://workbench.data.aliyun.com/console).
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

class GetIDEEventDetailResponseBodyEventDetailCommittedFileNodeConfigurationInputList(DaraModel):
    def __init__(
        self,
        input: str = None,
        parse_type: str = None,
    ):
        # The output name of the upstream file on which the file depends.
        # 
        # This parameter corresponds to the "Output Name of Upstream Node" in the "Schedule Configuration > Scheduling Dependencies > Depends On Upstream Nodes" setting of a DataStudio task in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.input = input
        # The method used to configure file dependencies. Valid values:
        # - MANUAL: manual configuration.
        # - AUTO: automatic parsing.
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

class GetIDEEventDetailResponseBodyEventDetailCommittedFileFilePropertyContent(DaraModel):
    def __init__(
        self,
        business_id: int = None,
        current_version: int = None,
        data_source_name: str = None,
        folder_id: str = None,
        owner: str = None,
        parent_file_id: int = None,
    ):
        # The ID of the workflow to which the file belongs.
        self.business_id = business_id
        # The latest version of the file.
        self.current_version = current_version
        # The unique identifier of the data source associated with the file.
        self.data_source_name = data_source_name
        # The ID of the folder to which the file belongs. You can call the [GetFolder](https://help.aliyun.com/document_detail/173952.html) operation to query file details by folder ID.
        self.folder_id = folder_id
        # The owner of the file.
        self.owner = owner
        # The node ID of the loop node or traversal node to which the file belongs.
        self.parent_file_id = parent_file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parent_file_id is not None:
            result['ParentFileId'] = self.parent_file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParentFileId') is not None:
            self.parent_file_id = m.get('ParentFileId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDIJobShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_data_source_settings_shrink: str = None,
        destination_data_source_type: str = None,
        job_name: str = None,
        job_settings_shrink: str = None,
        migration_type: str = None,
        project_id: int = None,
        resource_settings_shrink: str = None,
        source_data_source_settings_shrink: str = None,
        source_data_source_type: str = None,
        system_debug: str = None,
        table_mappings_shrink: str = None,
        transformation_rules_shrink: str = None,
    ):
        # The description of the synchronization task.
        self.description = description
        # The settings of the destination. Only a single destination is supported.
        self.destination_data_source_settings_shrink = destination_data_source_settings_shrink
        # The destination type. Valid values: Hologres and Hive.
        self.destination_data_source_type = destination_data_source_type
        # The name of the synchronization task.
        self.job_name = job_name
        # The settings for the dimension of the synchronization task. The settings include processing policies for DDL messages, policies for data type mappings between source fields and destination fields, and runtime parameters of the synchronization task.
        self.job_settings_shrink = job_settings_shrink
        # The synchronization type. Valid values:
        # 
        # *   FullAndRealtimeIncremental (one-time full synchronization and real-time incremental synchronization)
        # *   RealtimeIncremental (real-time incremental synchronization)
        # *   Full (full synchronization)
        # *   OfflineIncremental (batch incremental synchronization)
        # *   FullAndOfflineIncremental (one-time full synchronization and batch incremental synchronization)
        self.migration_type = migration_type
        # The DataWorks workspace ID. You can call the [ListProjects](https://help.aliyun.com/document_detail/178393.html) operation to obtain the ID.
        self.project_id = project_id
        # The resource settings.
        self.resource_settings_shrink = resource_settings_shrink
        # The settings of the source. Only a single source is supported.
        self.source_data_source_settings_shrink = source_data_source_settings_shrink
        # The source type. Set this parameter to MySQL.
        self.source_data_source_type = source_data_source_type
        # Specifies whether to perform system debugging. Valid values: true and false. Default value: false.
        self.system_debug = system_debug
        # The list of mappings between rules used to select synchronization objects in the source and transformation rules applied to the selected synchronization objects. Each entry in the list displays a mapping between a rule used to select synchronization objects and a transformation rule applied to the selected synchronization objects.
        self.table_mappings_shrink = table_mappings_shrink
        # The list of transformation rules that you want to apply to the synchronization objects selected from the source. Each entry in the list defines a transformation rule.
        self.transformation_rules_shrink = transformation_rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_data_source_settings_shrink is not None:
            result['DestinationDataSourceSettings'] = self.destination_data_source_settings_shrink

        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_settings_shrink is not None:
            result['JobSettings'] = self.job_settings_shrink

        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_settings_shrink is not None:
            result['ResourceSettings'] = self.resource_settings_shrink

        if self.source_data_source_settings_shrink is not None:
            result['SourceDataSourceSettings'] = self.source_data_source_settings_shrink

        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type

        if self.system_debug is not None:
            result['SystemDebug'] = self.system_debug

        if self.table_mappings_shrink is not None:
            result['TableMappings'] = self.table_mappings_shrink

        if self.transformation_rules_shrink is not None:
            result['TransformationRules'] = self.transformation_rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationDataSourceSettings') is not None:
            self.destination_data_source_settings_shrink = m.get('DestinationDataSourceSettings')

        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobSettings') is not None:
            self.job_settings_shrink = m.get('JobSettings')

        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceSettings') is not None:
            self.resource_settings_shrink = m.get('ResourceSettings')

        if m.get('SourceDataSourceSettings') is not None:
            self.source_data_source_settings_shrink = m.get('SourceDataSourceSettings')

        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')

        if m.get('SystemDebug') is not None:
            self.system_debug = m.get('SystemDebug')

        if m.get('TableMappings') is not None:
            self.table_mappings_shrink = m.get('TableMappings')

        if m.get('TransformationRules') is not None:
            self.transformation_rules_shrink = m.get('TransformationRules')

        return self


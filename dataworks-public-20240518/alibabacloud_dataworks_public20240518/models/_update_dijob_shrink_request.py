# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDIJobShrinkRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        description: str = None,
        file_spec: str = None,
        id: int = None,
        job_settings_shrink: str = None,
        owner: str = None,
        project_id: int = None,
        resource_settings_shrink: str = None,
        table_mappings_shrink: str = None,
        transformation_rules_shrink: str = None,
    ):
        # This parameter is deprecated. Use the Id parameter instead.
        self.dijob_id = dijob_id
        # The task description.
        self.description = description
        self.file_spec = file_spec
        # The ID of the synchronization task.
        self.id = id
        # The task-level settings, including DDL handling policies, column data type mapping between source and destination, and runtime parameters.
        self.job_settings_shrink = job_settings_shrink
        # The task owner.
        self.owner = owner
        # The DataWorks workspace ID. You can call the [ListProjects](https://help.aliyun.com/document_detail/178393.html) operation to obtain the ID.
        self.project_id = project_id
        # The resource settings.
        self.resource_settings_shrink = resource_settings_shrink
        # The list of synchronization object transformation mappings. Each element describes a set of source object selection rules and the transformation rules applied to those objects.
        # 
        # >  [ { "SourceObjectSelectionRules":[ { "ObjectType":"Database", "Action":"Include", "ExpressionType":"Exact", "Expression":"biz_db" }, { "ObjectType":"Schema", "Action":"Include", "ExpressionType":"Exact", "Expression":"s1" }, { "ObjectType":"Table", "Action":"Include", "ExpressionType":"Exact", "Expression":"table1" } ], "TransformationRuleNames":[ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema" } ] } ]
        self.table_mappings_shrink = table_mappings_shrink
        # The list of synchronization object transformation rule definitions.
        # 
        # >  [ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema", "RuleExpression":"{"expression":"${srcDatasoureName}_${srcDatabaseName}"}" } ]
        self.transformation_rules_shrink = transformation_rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.description is not None:
            result['Description'] = self.description

        if self.file_spec is not None:
            result['FileSpec'] = self.file_spec

        if self.id is not None:
            result['Id'] = self.id

        if self.job_settings_shrink is not None:
            result['JobSettings'] = self.job_settings_shrink

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_settings_shrink is not None:
            result['ResourceSettings'] = self.resource_settings_shrink

        if self.table_mappings_shrink is not None:
            result['TableMappings'] = self.table_mappings_shrink

        if self.transformation_rules_shrink is not None:
            result['TransformationRules'] = self.transformation_rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSpec') is not None:
            self.file_spec = m.get('FileSpec')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JobSettings') is not None:
            self.job_settings_shrink = m.get('JobSettings')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceSettings') is not None:
            self.resource_settings_shrink = m.get('ResourceSettings')

        if m.get('TableMappings') is not None:
            self.table_mappings_shrink = m.get('TableMappings')

        if m.get('TransformationRules') is not None:
            self.transformation_rules_shrink = m.get('TransformationRules')

        return self


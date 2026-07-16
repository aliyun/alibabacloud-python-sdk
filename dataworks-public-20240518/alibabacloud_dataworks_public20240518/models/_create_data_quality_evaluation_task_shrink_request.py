# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataQualityEvaluationTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        data_quality_rules_shrink: str = None,
        data_source_id: int = None,
        description: str = None,
        hooks_shrink: str = None,
        name: str = None,
        notifications_shrink: str = None,
        project_id: int = None,
        runtime_conf: str = None,
        target_shrink: str = None,
        trigger_shrink: str = None,
    ):
        # The list of data quality rules associated with the data quality monitor. If DataQualityRule.Id is specified, the rule corresponding to that ID is associated with the newly created quality monitor. If not specified, a new rule is created from the other fields and associated with the newly created quality monitor.
        self.data_quality_rules_shrink = data_quality_rules_shrink
        # The ID of the data source. You can call [ListDataSources](https://help.aliyun.com/document_detail/211431.html) to obtain the ID of the data source.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The description of the quality monitoring task.
        self.description = description
        # The hook settings.
        self.hooks_shrink = hooks_shrink
        # The name of the quality monitoring task.
        # 
        # This parameter is required.
        self.name = name
        # The notification subscription configuration.
        self.notifications_shrink = notifications_shrink
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace used by this API call.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The extended configuration, a JSON-formatted string. This setting takes effect only for EMR-type data quality monitors.
        # - queue: The YARN queue used when running EMR data quality validation. The default is the queue configured for the current project.
        # - sqlEngine: The SQL engine used when running EMR data validation.
        #     + HIVE_SQL
        #     + SPARK_SQL
        self.runtime_conf = runtime_conf
        # The data quality monitoring object.
        # 
        # This parameter is required.
        self.target_shrink = target_shrink
        # The trigger configuration of the data quality validation task.
        self.trigger_shrink = trigger_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_rules_shrink is not None:
            result['DataQualityRules'] = self.data_quality_rules_shrink

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.description is not None:
            result['Description'] = self.description

        if self.hooks_shrink is not None:
            result['Hooks'] = self.hooks_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.notifications_shrink is not None:
            result['Notifications'] = self.notifications_shrink

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_conf is not None:
            result['RuntimeConf'] = self.runtime_conf

        if self.target_shrink is not None:
            result['Target'] = self.target_shrink

        if self.trigger_shrink is not None:
            result['Trigger'] = self.trigger_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityRules') is not None:
            self.data_quality_rules_shrink = m.get('DataQualityRules')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Hooks') is not None:
            self.hooks_shrink = m.get('Hooks')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Notifications') is not None:
            self.notifications_shrink = m.get('Notifications')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeConf') is not None:
            self.runtime_conf = m.get('RuntimeConf')

        if m.get('Target') is not None:
            self.target_shrink = m.get('Target')

        if m.get('Trigger') is not None:
            self.trigger_shrink = m.get('Trigger')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SkillAddMetaProfilingJobRequest(DaraModel):
    def __init__(
        self,
        component_id: int = None,
        job_desc: str = None,
        job_id: int = None,
        job_name: str = None,
        meta_ids: List[str] = None,
        plugin_id: str = None,
        profiling_flag: int = None,
        profiling_permission: int = None,
        profiling_rule: str = None,
        profiling_schema_list: List[str] = None,
        profiling_type: int = None,
    ):
        # The component ID, which is the primary key identifier of the data source component.
        self.component_id = component_id
        # The description of the profiling task.
        self.job_desc = job_desc
        # The profiling task ID.
        self.job_id = job_id
        # The name of the profiling task.
        self.job_name = job_name
        # The list of metadata object IDs to be profiled or operated on.
        self.meta_ids = meta_ids
        # The profiling plugin ID, which specifies the plugin used to perform the profiling.
        self.plugin_id = plugin_id
        # Specifies whether to enable data profiling.
        self.profiling_flag = profiling_flag
        # The profiling permission configuration identifier.
        self.profiling_permission = profiling_permission
        # The profiling rule configuration content.
        self.profiling_rule = profiling_rule
        # The list of schemas to be profiled.
        self.profiling_schema_list = profiling_schema_list
        # The profiling type identifier.
        self.profiling_type = profiling_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['componentId'] = self.component_id

        if self.job_desc is not None:
            result['jobDesc'] = self.job_desc

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.job_name is not None:
            result['jobName'] = self.job_name

        if self.meta_ids is not None:
            result['metaIds'] = self.meta_ids

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.profiling_flag is not None:
            result['profilingFlag'] = self.profiling_flag

        if self.profiling_permission is not None:
            result['profilingPermission'] = self.profiling_permission

        if self.profiling_rule is not None:
            result['profilingRule'] = self.profiling_rule

        if self.profiling_schema_list is not None:
            result['profilingSchemaList'] = self.profiling_schema_list

        if self.profiling_type is not None:
            result['profilingType'] = self.profiling_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentId') is not None:
            self.component_id = m.get('componentId')

        if m.get('jobDesc') is not None:
            self.job_desc = m.get('jobDesc')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')

        if m.get('metaIds') is not None:
            self.meta_ids = m.get('metaIds')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('profilingFlag') is not None:
            self.profiling_flag = m.get('profilingFlag')

        if m.get('profilingPermission') is not None:
            self.profiling_permission = m.get('profilingPermission')

        if m.get('profilingRule') is not None:
            self.profiling_rule = m.get('profilingRule')

        if m.get('profilingSchemaList') is not None:
            self.profiling_schema_list = m.get('profilingSchemaList')

        if m.get('profilingType') is not None:
            self.profiling_type = m.get('profilingType')

        return self


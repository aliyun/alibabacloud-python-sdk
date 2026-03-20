# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateJobScriptRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        job_id: int = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        script_content: str = None,
        version_description: str = None,
    ):
        # The application ID. You can obtain the application ID on the Applications page in the SchedulerX console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The job ID. You can obtain the ID on the Tasks page in the SchedulerX console.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The namespace ID. You can obtain the namespace ID on the Namespaces page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The script content.
        self.script_content = script_content
        # The description of the script version.
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.script_content is not None:
            result['ScriptContent'] = self.script_content

        if self.version_description is not None:
            result['VersionDescription'] = self.version_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        return self


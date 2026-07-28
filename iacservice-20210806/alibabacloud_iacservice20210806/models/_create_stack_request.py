# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateStackRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
        parameter_set_ids: List[str] = None,
        ram_role: str = None,
        source: str = None,
        source_path: str = None,
        working_directory: str = None,
    ):
        # The idempotency token. Format: [0-9a-zA-Z-]{1,64}. We recommend that you use a UUID.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The description of the resource stack. The value cannot exceed 256 characters.
        self.description = description
        # The resource stack name. The name must be 2 to 128 characters in length and can contain letters, digits, Chinese characters, hyphens (-), underscores (_), and periods (.). The name cannot start or end with a hyphen, underscore, or period.
        self.name = name
        self.parameter_set_ids = parameter_set_ids
        # The RAM role to be assigned to the task. This role is used to automatically continue the execution of scheduled tasks during automatic triggers or offline scenarios.
        self.ram_role = ram_role
        # The creation source. Valid values:
        # 
        # - OSS: a template from OSS.
        # - IAC_SERVICE_MODULE: a template created in the automation service console.
        # 
        # This parameter is required.
        self.source = source
        # The path of the configuration source. The value cannot exceed 1000 characters.
        # 
        # - If the source is OSS, the value is in the format oss::<file link> and must be a zip file. Example: oss::https://terraform-pipeline.oss-eu-central-1.aliyuncs.com/code.zip
        # - If the source is IAC_SERVICE_MODULE, the value is a template ID. Example: mod-xxxxx
        self.source_path = source_path
        # The working directory where the configuration file is located. Enter / if it is in the root directory. Example: config/ or /
        self.working_directory = working_directory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.parameter_set_ids is not None:
            result['parameterSetIds'] = self.parameter_set_ids

        if self.ram_role is not None:
            result['ramRole'] = self.ram_role

        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.working_directory is not None:
            result['workingDirectory'] = self.working_directory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parameterSetIds') is not None:
            self.parameter_set_ids = m.get('parameterSetIds')

        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('workingDirectory') is not None:
            self.working_directory = m.get('workingDirectory')

        return self


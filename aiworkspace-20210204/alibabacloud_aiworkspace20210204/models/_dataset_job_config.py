# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatasetJobConfig(DaraModel):
    def __init__(
        self,
        config: str = None,
        config_type: str = None,
        create_time: str = None,
        dataset_job_config_id: str = None,
        dataset_version: str = None,
        modify_time: str = None,
        workspace_id: str = None,
    ):
        self.config = config
        self.config_type = config_type
        self.create_time = create_time
        self.dataset_job_config_id = dataset_job_config_id
        self.dataset_version = dataset_version
        self.modify_time = modify_time
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dataset_job_config_id is not None:
            result['DatasetJobConfigId'] = self.dataset_job_config_id

        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatasetJobConfigId') is not None:
            self.dataset_job_config_id = m.get('DatasetJobConfigId')

        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self


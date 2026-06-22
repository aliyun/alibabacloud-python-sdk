# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplicationConfigurationFile(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        cluster_id: str = None,
        config_file_format: str = None,
        config_file_group: str = None,
        config_file_link: str = None,
        config_file_mode: str = None,
        config_file_name: str = None,
        config_file_owner: str = None,
        config_file_path: str = None,
        description: str = None,
        node_group_id: str = None,
        node_id: str = None,
    ):
        self.application_name = application_name
        self.cluster_id = cluster_id
        self.config_file_format = config_file_format
        self.config_file_group = config_file_group
        self.config_file_link = config_file_link
        self.config_file_mode = config_file_mode
        self.config_file_name = config_file_name
        self.config_file_owner = config_file_owner
        self.config_file_path = config_file_path
        self.description = description
        self.node_group_id = node_group_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.config_file_format is not None:
            result['ConfigFileFormat'] = self.config_file_format

        if self.config_file_group is not None:
            result['ConfigFileGroup'] = self.config_file_group

        if self.config_file_link is not None:
            result['ConfigFileLink'] = self.config_file_link

        if self.config_file_mode is not None:
            result['ConfigFileMode'] = self.config_file_mode

        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name

        if self.config_file_owner is not None:
            result['ConfigFileOwner'] = self.config_file_owner

        if self.config_file_path is not None:
            result['ConfigFilePath'] = self.config_file_path

        if self.description is not None:
            result['Description'] = self.description

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConfigFileFormat') is not None:
            self.config_file_format = m.get('ConfigFileFormat')

        if m.get('ConfigFileGroup') is not None:
            self.config_file_group = m.get('ConfigFileGroup')

        if m.get('ConfigFileLink') is not None:
            self.config_file_link = m.get('ConfigFileLink')

        if m.get('ConfigFileMode') is not None:
            self.config_file_mode = m.get('ConfigFileMode')

        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')

        if m.get('ConfigFileOwner') is not None:
            self.config_file_owner = m.get('ConfigFileOwner')

        if m.get('ConfigFilePath') is not None:
            self.config_file_path = m.get('ConfigFilePath')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self


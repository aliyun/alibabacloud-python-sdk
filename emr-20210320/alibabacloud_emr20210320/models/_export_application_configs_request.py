# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ExportApplicationConfigsRequest(DaraModel):
    def __init__(
        self,
        application_config_files: List[main_models.ApplicationConfigFile] = None,
        cluster_id: str = None,
        config_scope: str = None,
        export_mode: str = None,
        file_format: str = None,
        node_group_ids: List[str] = None,
        node_ids: List[str] = None,
        region_id: str = None,
    ):
        # The list of application configurations to export.
        self.application_config_files = application_config_files
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        self.config_scope = config_scope
        # The mode for exporting service configurations. Valid values:
        # 
        # - MODIFICATION
        # 
        # - ALL
        self.export_mode = export_mode
        # The file format of the exported application configurations. Valid values:
        # 
        # - JSON
        # 
        # - XML
        self.file_format = file_format
        self.node_group_ids = node_group_ids
        self.node_ids = node_ids
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.application_config_files:
            for v1 in self.application_config_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationConfigFiles'] = []
        if self.application_config_files is not None:
            for k1 in self.application_config_files:
                result['ApplicationConfigFiles'].append(k1.to_map() if k1 else None)

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.config_scope is not None:
            result['ConfigScope'] = self.config_scope

        if self.export_mode is not None:
            result['ExportMode'] = self.export_mode

        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.node_group_ids is not None:
            result['NodeGroupIds'] = self.node_group_ids

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_config_files = []
        if m.get('ApplicationConfigFiles') is not None:
            for k1 in m.get('ApplicationConfigFiles'):
                temp_model = main_models.ApplicationConfigFile()
                self.application_config_files.append(temp_model.from_map(k1))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConfigScope') is not None:
            self.config_scope = m.get('ConfigScope')

        if m.get('ExportMode') is not None:
            self.export_mode = m.get('ExportMode')

        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('NodeGroupIds') is not None:
            self.node_group_ids = m.get('NodeGroupIds')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


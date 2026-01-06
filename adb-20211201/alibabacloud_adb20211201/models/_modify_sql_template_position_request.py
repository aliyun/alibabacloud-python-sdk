# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySqlTemplatePositionRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        target_template_group_id: int = None,
        template_id: int = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the template group.
        # 
        # This parameter is required.
        self.target_template_group_id = target_template_group_id
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_template_group_id is not None:
            result['TargetTemplateGroupId'] = self.target_template_group_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetTemplateGroupId') is not None:
            self.target_template_group_id = m.get('TargetTemplateGroupId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self


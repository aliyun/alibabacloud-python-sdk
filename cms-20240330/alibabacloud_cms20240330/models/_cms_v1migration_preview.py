# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CmsV1MigrationPreview(DaraModel):
    def __init__(
        self,
        checks: List[main_models.CmsV1MigrationCheck] = None,
        group_name: str = None,
        migratable: bool = None,
        observe_group_id: str = None,
        origin_group_id: str = None,
        reason: str = None,
        source_read_only: bool = None,
        source_type: str = None,
        target_group_name: str = None,
    ):
        # The itemized check results for name and resource support.
        self.checks = checks
        # The name of the source application group.
        self.group_name = group_name
        # Indicates whether the dry run is passed.
        self.migratable = migratable
        # The ID of the target observation group.
        self.observe_group_id = observe_group_id
        # The ID of the source CloudMonitor 1.0 application group.
        self.origin_group_id = origin_group_id
        # The reason for the dry run failure.
        self.reason = reason
        # Indicates whether the source 1.0 group is persistently read-only.
        self.source_read_only = source_read_only
        # The type of the source application group. custom indicates a custom group, tag indicates a tag-based group, and regMgr indicates a resource group-based group.
        self.source_type = source_type
        # The name of the target observation group.
        self.target_group_name = target_group_name

    def validate(self):
        if self.checks:
            for v1 in self.checks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['checks'] = []
        if self.checks is not None:
            for k1 in self.checks:
                result['checks'].append(k1.to_map() if k1 else None)

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.migratable is not None:
            result['migratable'] = self.migratable

        if self.observe_group_id is not None:
            result['observeGroupId'] = self.observe_group_id

        if self.origin_group_id is not None:
            result['originGroupId'] = self.origin_group_id

        if self.reason is not None:
            result['reason'] = self.reason

        if self.source_read_only is not None:
            result['sourceReadOnly'] = self.source_read_only

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.target_group_name is not None:
            result['targetGroupName'] = self.target_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.checks = []
        if m.get('checks') is not None:
            for k1 in m.get('checks'):
                temp_model = main_models.CmsV1MigrationCheck()
                self.checks.append(temp_model.from_map(k1))

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('migratable') is not None:
            self.migratable = m.get('migratable')

        if m.get('observeGroupId') is not None:
            self.observe_group_id = m.get('observeGroupId')

        if m.get('originGroupId') is not None:
            self.origin_group_id = m.get('originGroupId')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('sourceReadOnly') is not None:
            self.source_read_only = m.get('sourceReadOnly')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('targetGroupName') is not None:
            self.target_group_name = m.get('targetGroupName')

        return self


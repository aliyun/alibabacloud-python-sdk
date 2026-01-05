# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataQualityScanRunShrinkRequest(DaraModel):
    def __init__(
        self,
        data_quality_scan_id: int = None,
        parameters_shrink: str = None,
        project_id: int = None,
        runtime_resource_shrink: str = None,
    ):
        # The ID of the data quality monitor.
        self.data_quality_scan_id = data_quality_scan_id
        # The parameter settings used during the actual run. The `triggerTime` parameter is required.
        self.parameters_shrink = parameters_shrink
        # The project ID.
        self.project_id = project_id
        # The scheduling resource group used when running the data quality monitor. This resource group uses the same data structure as in the scheduling API.
        self.runtime_resource_shrink = runtime_resource_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_scan_id is not None:
            result['DataQualityScanId'] = self.data_quality_scan_id

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_resource_shrink is not None:
            result['RuntimeResource'] = self.runtime_resource_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityScanId') is not None:
            self.data_quality_scan_id = m.get('DataQualityScanId')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            self.runtime_resource_shrink = m.get('RuntimeResource')

        return self


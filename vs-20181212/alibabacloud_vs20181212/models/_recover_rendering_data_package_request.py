# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecoverRenderingDataPackageRequest(DaraModel):
    def __init__(
        self,
        data_package_id: str = None,
        load_mode: str = None,
        rendering_instance_id: str = None,
    ):
        # The ID of the cloud application service data package.
        # 
        # This parameter is required.
        self.data_package_id = data_package_id
        # The data loading mode. Valid values:
        # - System: system-level loading, which provides high stability but takes a relatively long time.
        # - Process: process-level loading, which provides high loading timeliness but relatively low stability.
        # Default value: System.
        self.load_mode = load_mode
        # The cloud application service instance ID.
        # 
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_package_id is not None:
            result['DataPackageId'] = self.data_package_id

        if self.load_mode is not None:
            result['LoadMode'] = self.load_mode

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPackageId') is not None:
            self.data_package_id = m.get('DataPackageId')

        if m.get('LoadMode') is not None:
            self.load_mode = m.get('LoadMode')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self


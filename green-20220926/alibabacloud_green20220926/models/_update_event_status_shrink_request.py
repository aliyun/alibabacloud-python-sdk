# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEventStatusShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        event_ids_shrink: str = None,
        operation_code: str = None,
        operation_params: str = None,
        region_id: str = None,
        source: str = None,
    ):
        # The application ID that identifies the application to which the operation belongs.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The list of risk event IDs.
        self.event_ids_shrink = event_ids_shrink
        # The operation code that defines the specific type of event status change operation.
        # 
        # This parameter is required.
        self.operation_code = operation_code
        # The operation parameters that contain additional parameter information required to execute the operation.
        self.operation_params = operation_params
        # The region ID.
        self.region_id = region_id
        # The operation source that identifies the source system or module that triggered this status update request.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.event_ids_shrink is not None:
            result['EventIds'] = self.event_ids_shrink

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EventIds') is not None:
            self.event_ids_shrink = m.get('EventIds')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self


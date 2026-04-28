# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class MovePolarFsObjectsRequest(DaraModel):
    def __init__(
        self,
        objects_to_move: List[main_models.MovePolarFsObjectsRequestObjectsToMove] = None,
        polar_fs_instance_id: str = None,
    ):
        self.objects_to_move = objects_to_move
        self.polar_fs_instance_id = polar_fs_instance_id

    def validate(self):
        if self.objects_to_move:
            for v1 in self.objects_to_move:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ObjectsToMove'] = []
        if self.objects_to_move is not None:
            for k1 in self.objects_to_move:
                result['ObjectsToMove'].append(k1.to_map() if k1 else None)

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.objects_to_move = []
        if m.get('ObjectsToMove') is not None:
            for k1 in m.get('ObjectsToMove'):
                temp_model = main_models.MovePolarFsObjectsRequestObjectsToMove()
                self.objects_to_move.append(temp_model.from_map(k1))

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        return self

class MovePolarFsObjectsRequestObjectsToMove(DaraModel):
    def __init__(
        self,
        destination_path: str = None,
        source_path: str = None,
    ):
        self.destination_path = destination_path
        self.source_path = source_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_path is not None:
            result['DestinationPath'] = self.destination_path

        if self.source_path is not None:
            result['SourcePath'] = self.source_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationPath') is not None:
            self.destination_path = m.get('DestinationPath')

        if m.get('SourcePath') is not None:
            self.source_path = m.get('SourcePath')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class ListRecyclebinRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        limit: int = None,
        marker: str = None,
        thumbnail_processes: Dict[str, main_models.ImageProcess] = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The fields of an entry (file or folder) to return.
        # 
        # 1\\. If you set this parameter to \\*, all fields are returned.
        # 
        # 2\\. If you set this parameter to a null value or leave this parameter empty, the fields, such as file creator, file modifier, and custom tags, are not returned.
        # 
        # The default value is a null value, which indicates that only some fields are returned.
        self.fields = fields
        # The maximum number of entries to return. Valid values: 1 to 200. Default value: 50.
        # 
        # The number of returned entries must be less than or equal to the value of this parameter.
        self.limit = limit
        # The name of the entry after which the list begins. Entries whose names are alphabetically after the value of this parameter are returned. If you do not specify this parameter, all entries are returned. This parameter is left empty by default.
        self.marker = marker
        # The thumbnail configurations. Up to five thumbnails can be returned at a time. The value contains key-value pairs. You can customize the keys. The URL of a thumbnail is returned based on the key.
        self.thumbnail_processes = thumbnail_processes

    def validate(self):
        if self.thumbnail_processes:
            for v1 in self.thumbnail_processes.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.fields is not None:
            result['fields'] = self.fields

        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        result['thumbnail_processes'] = {}
        if self.thumbnail_processes is not None:
            for k1, v1 in self.thumbnail_processes.items():
                result['thumbnail_processes'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        self.thumbnail_processes = {}
        if m.get('thumbnail_processes') is not None:
            for k1, v1 in m.get('thumbnail_processes').items():
                temp_model = main_models.ImageProcess()
                self.thumbnail_processes[k1] = temp_model.from_map(v1)

        return self


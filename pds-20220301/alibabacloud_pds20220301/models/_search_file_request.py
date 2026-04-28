# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class SearchFileRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        limit: int = None,
        marker: str = None,
        order_by: str = None,
        query: str = None,
        recursive: bool = None,
        return_total_count: bool = None,
        thumbnail_processes: Dict[str, main_models.ImageProcess] = None,
    ):
        # The drive ID.
        self.drive_id = drive_id
        # The field that is used to return additional information about files. Valid values:
        # 
        # *   dir_size: returns the statistics on each subfolder in the response.
        # *   id_path: returns the id_path value of each child subject in the response.
        # *   name_path: returns the name_path value of each child subject in the response.
        # 
        # You can specify multiple fields by separating them with commas (,). Example: "id_path,name_path,dir_size".
        self.fields = fields
        # The maximum number of entries to return. Valid values: 1 to 100.
        # 
        # The number of returned entries must be less than or equal to the value of this parameter.
        self.limit = limit
        # The name of the entry after which the list begins. Entries whose names are alphabetically after the value of this parameter are returned. If you do not specify this parameter, all entries are returned.\\
        # This parameter is left empty by default.
        self.marker = marker
        # The field by which to sort the returned entries. Default value: created_at. Valid values:
        # 
        # *   created_at: sorts the entries by creation time.
        # *   updated_at: sorts the entries by update time.
        # *   size: sorts the entries by file size.
        # *   name: sorts the entries by file name.
        # 
        # The order in which you want to sort the returned entries. Valid values:
        # 
        # *   ASC: ascending order
        # *   DESC: descending order
        # 
        # You must specify this parameter in the \\<field> \\<ASC or DESC> format. Separate multiple fields with commas (,). A preceding field has a higher priority than a following field. Examples:
        # 
        # *   If you want to sort the entries by file name in ascending order, set this parameter to "name ASC".
        # *   If you want to sort the entries by creation time in descending order, set this parameter to "created_at DESC".
        # *   If you want to sort the entries by creation time in descending order and sort the entries by file name in ascending order in case of the same creation time, set this parameter to "created_at DESC,name ASC".
        self.order_by = order_by
        # The search conditions. Fuzzy searches based on the file name or directory name are supported. The value of this parameter can be up to 4,096 characters in length.
        # 
        # This parameter is required.
        self.query = query
        # Specifies whether to perform recursive search on a folder that is specified by setting parent_file_id in the query parameter.
        self.recursive = recursive
        # Specifies whether to return the total number of retrieved files.
        self.return_total_count = return_total_count
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

        if self.order_by is not None:
            result['order_by'] = self.order_by

        if self.query is not None:
            result['query'] = self.query

        if self.recursive is not None:
            result['recursive'] = self.recursive

        if self.return_total_count is not None:
            result['return_total_count'] = self.return_total_count

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

        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('recursive') is not None:
            self.recursive = m.get('recursive')

        if m.get('return_total_count') is not None:
            self.return_total_count = m.get('return_total_count')

        self.thumbnail_processes = {}
        if m.get('thumbnail_processes') is not None:
            for k1, v1 in m.get('thumbnail_processes').items():
                temp_model = main_models.ImageProcess()
                self.thumbnail_processes[k1] = temp_model.from_map(v1)

        return self


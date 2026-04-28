# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class ListFileRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        drive_id: str = None,
        fields: str = None,
        limit: int = None,
        marker: str = None,
        order_by: str = None,
        order_direction: str = None,
        parent_file_id: str = None,
        share_id: str = None,
        status: str = None,
        thumbnail_processes: Dict[str, main_models.ImageProcess] = None,
        type: str = None,
    ):
        # The file category. Valid values:
        # 
        # app: installation package zip: compressed package image doc: document video audio others
        # 
        # By default, files of all categories are returned.
        self.category = category
        # The drive ID.
        self.drive_id = drive_id
        # The field that is used to return additional information about a child subject. Valid values:
        # 
        # *   url: returns the URL of the thumbnail of a file in the response.
        # *   exif: returns the Exchangeable Image File Format (EXIF) data of a file in the response.
        # *   cropping_suggestion: returns the cropping suggestion on a file in the response.
        # *   characteristic_hash: returns the characteristic hash value of a file in the response.
        # *   video_metadata: returns the metadata of a video file, such as the video duration, bitrate, height, and width, in the response.
        # *   video_preview_metadata: returns the transcoding information of a video file, such as the transcoding specification for each definition, in the response.
        # *   investigation_info: returns the investigation information in the response.
        # *   dir_size: returns the statistics on each subfolder in the response.
        # *   user_tags: returns the user tags of each child subject in the response.
        # 
        # You can specify multiple fields by separating them with commas (,). Example: "url,dir_size,user_tags".
        self.fields = fields
        # The maximum number of results to return. Valid values: 1 to 100.
        # 
        # The number of returned entries must be less than or equal to the value of this parameter.
        self.limit = limit
        # The name of the entry after which the list begins. Entries whose names are alphabetically after the value of this parameter are returned. If you do not specify this parameter, all entries are returned.\\
        # This parameter is left empty by default.
        self.marker = marker
        # The sorting field. Valid values:
        # 
        # created_at: sorts the entries by creation time. updated_at: sorts the entries by update time. size: sorts the entries by file size. name: sorts the entries by file name.
        # 
        # Default value: created_at.
        # 
        # Enumeration:
        # 
        # *   updated_at: update time
        # *   size: file size
        # *   name: file name
        # *   created_at: creation time
        self.order_by = order_by
        # The sorting direction. Valid values:
        # 
        # ASC: ascending order DESC: descending order
        # 
        # Default value: ASC.
        self.order_direction = order_direction
        # The ID of the parent folder. If the parent folder is a root directory, set this parameter to root.
        # 
        # This parameter is required.
        self.parent_file_id = parent_file_id
        # The share ID. If you want to share a file, carry the `x-share-token` header for authentication in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify one of `share_id` and `drive_id`.
        self.share_id = share_id
        # The state of the files to return. Valid values:
        # 
        # available: returns only normal files. uploading: returns only files that are being uploaded.
        # 
        # By default, only files in the available state are returned.
        self.status = status
        # The thumbnail configurations. Up to five thumbnails can be returned at a time. The value contains key-value pairs. You can customize the keys. The URL of a thumbnail is returned based on the key.
        self.thumbnail_processes = thumbnail_processes
        # The file type. Valid values:
        # 
        # file: returns only files. folder: returns only folders.
        # 
        # By default, files of all types are returned.
        self.type = type

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
        if self.category is not None:
            result['category'] = self.category

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

        if self.order_direction is not None:
            result['order_direction'] = self.order_direction

        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id

        if self.share_id is not None:
            result['share_id'] = self.share_id

        if self.status is not None:
            result['status'] = self.status

        result['thumbnail_processes'] = {}
        if self.thumbnail_processes is not None:
            for k1, v1 in self.thumbnail_processes.items():
                result['thumbnail_processes'][k1] = v1.to_map() if v1 else None

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

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

        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')

        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.thumbnail_processes = {}
        if m.get('thumbnail_processes') is not None:
            for k1, v1 in m.get('thumbnail_processes').items():
                temp_model = main_models.ImageProcess()
                self.thumbnail_processes[k1] = temp_model.from_map(v1)

        if m.get('type') is not None:
            self.type = m.get('type')

        return self


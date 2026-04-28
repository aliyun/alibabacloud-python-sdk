# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SearchAddressGroupsRequest(DaraModel):
    def __init__(
        self,
        address_level: str = None,
        address_names: List[str] = None,
        br_geo_point: str = None,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        tl_geo_point: str = None,
        video_thumbnail_process: str = None,
    ):
        # The level of the location.
        # 
        # Valid values:
        # 
        # *   country
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   province
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   city
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   district
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   township
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.address_level = address_level
        # The locations.
        self.address_names = address_names
        # The coordinates of the bottom right vertex of the rectangle. Set the value in the format of latitude,longitude.
        self.br_geo_point = br_geo_point
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The method used to generate the thumbnail of an image.
        self.image_thumbnail_process = image_thumbnail_process
        # The coordinates of the top left vertex of the rectangle. Set the value in the format of latitude,longitude.
        self.tl_geo_point = tl_geo_point
        # The method used to generate the thumbnail of a video.
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_level is not None:
            result['address_level'] = self.address_level

        if self.address_names is not None:
            result['address_names'] = self.address_names

        if self.br_geo_point is not None:
            result['br_geo_point'] = self.br_geo_point

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process

        if self.tl_geo_point is not None:
            result['tl_geo_point'] = self.tl_geo_point

        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_level') is not None:
            self.address_level = m.get('address_level')

        if m.get('address_names') is not None:
            self.address_names = m.get('address_names')

        if m.get('br_geo_point') is not None:
            self.br_geo_point = m.get('br_geo_point')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')

        if m.get('tl_geo_point') is not None:
            self.tl_geo_point = m.get('tl_geo_point')

        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')

        return self


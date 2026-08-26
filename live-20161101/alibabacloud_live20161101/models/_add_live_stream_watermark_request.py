# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLiveStreamWatermarkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        domain: str = None,
        height: int = None,
        name: str = None,
        offset_corner: str = None,
        owner_id: int = None,
        picture_url: str = None,
        ref_height: int = None,
        ref_width: int = None,
        region_id: str = None,
        transparency: int = None,
        type: int = None,
        xoffset: float = None,
        yoffset: float = None,
    ):
        # A custom description for the watermark.
        self.description = description
        # The streaming domain.
        self.domain = domain
        # The height of the watermark image, in pixels. This value is relative to `RefHeight` and will be scaled proportionally with the actual video resolution.
        # 
        # This parameter is required.
        self.height = height
        # The name of the watermark template.
        # 
        # This parameter is required.
        self.name = name
        # The anchor point for the watermark\\"s position. Valid values:
        # 
        # - TopLeft
        # 
        # - TopRight
        # 
        # - BottomLeft
        # 
        # - BottomRight
        # 
        # This parameter is required.
        self.offset_corner = offset_corner
        self.owner_id = owner_id
        # The URL of the watermark image.
        # 
        # This parameter is required.
        self.picture_url = picture_url
        # The reference height of the video background, in pixels.
        # 
        # This parameter is required.
        self.ref_height = ref_height
        # The reference width of the video background, in pixels.
        # 
        # This parameter is required.
        self.ref_width = ref_width
        # The region ID.
        self.region_id = region_id
        # The opacity of the watermark. Value range: `0` (fully transparent) to `255` (fully opaque).
        # 
        # This parameter is required.
        self.transparency = transparency
        # The type of the watermark. Valid value:
        # 
        # - **0**: image.
        # 
        # This parameter is required.
        self.type = type
        # The X-axis offset of the watermark, in pixels.
        # 
        # > Relative to RefWidth. If OffsetCorner is TopLeft, XOffset is the horizontal distance between the top‑left corner of the watermark and the top‑left corner of the background video. Positive X points to the right.
        # 
        # This parameter is required.
        self.xoffset = xoffset
        # The Y-axis offset of the watermark, in pixels.
        # 
        # > Relative to RefHeight. If OffsetCorner is TopLeft, YOffset is the vertical distance between the top‑left corner of the watermark and the top‑left corner of the background video. Positive Y points downward.
        # 
        # This parameter is required.
        self.yoffset = yoffset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.height is not None:
            result['Height'] = self.height

        if self.name is not None:
            result['Name'] = self.name

        if self.offset_corner is not None:
            result['OffsetCorner'] = self.offset_corner

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.picture_url is not None:
            result['PictureUrl'] = self.picture_url

        if self.ref_height is not None:
            result['RefHeight'] = self.ref_height

        if self.ref_width is not None:
            result['RefWidth'] = self.ref_width

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.transparency is not None:
            result['Transparency'] = self.transparency

        if self.type is not None:
            result['Type'] = self.type

        if self.xoffset is not None:
            result['XOffset'] = self.xoffset

        if self.yoffset is not None:
            result['YOffset'] = self.yoffset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OffsetCorner') is not None:
            self.offset_corner = m.get('OffsetCorner')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PictureUrl') is not None:
            self.picture_url = m.get('PictureUrl')

        if m.get('RefHeight') is not None:
            self.ref_height = m.get('RefHeight')

        if m.get('RefWidth') is not None:
            self.ref_width = m.get('RefWidth')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Transparency') is not None:
            self.transparency = m.get('Transparency')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('XOffset') is not None:
            self.xoffset = m.get('XOffset')

        if m.get('YOffset') is not None:
            self.yoffset = m.get('YOffset')

        return self


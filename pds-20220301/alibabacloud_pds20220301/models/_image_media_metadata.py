# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class ImageMediaMetadata(DaraModel):
    def __init__(
        self,
        address_line: str = None,
        city: str = None,
        country: str = None,
        district: str = None,
        exif: str = None,
        faces_thumbnail: List[main_models.FaceThumbnail] = None,
        height: int = None,
        image_quality: main_models.ImageQuality = None,
        image_tags: List[main_models.SystemTag] = None,
        location: str = None,
        province: str = None,
        time: str = None,
        township: str = None,
        width: int = None,
    ):
        # The full address.
        self.address_line = address_line
        # The city in which the image was taken.
        self.city = city
        # The country or region in which the image was taken.
        self.country = country
        # The district in which the image was taken.
        self.district = district
        # The EXIF information about the image.
        self.exif = exif
        # The thumbnails of the faces.
        self.faces_thumbnail = faces_thumbnail
        # The height of the image. Unit: pixel.
        self.height = height
        # The rating of the image.
        self.image_quality = image_quality
        # The details of the image tags.
        self.image_tags = image_tags
        # The location of the image.
        self.location = location
        # The province in which the image was taken.
        self.province = province
        # The time when the image was taken. The time follows the RFC3339 standard.
        self.time = time
        # The street in which the image was taken.
        self.township = township
        # The width of the image. Unit: pixel.
        self.width = width

    def validate(self):
        if self.faces_thumbnail:
            for v1 in self.faces_thumbnail:
                 if v1:
                    v1.validate()
        if self.image_quality:
            self.image_quality.validate()
        if self.image_tags:
            for v1 in self.image_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_line is not None:
            result['address_line'] = self.address_line

        if self.city is not None:
            result['city'] = self.city

        if self.country is not None:
            result['country'] = self.country

        if self.district is not None:
            result['district'] = self.district

        if self.exif is not None:
            result['exif'] = self.exif

        result['faces_thumbnail'] = []
        if self.faces_thumbnail is not None:
            for k1 in self.faces_thumbnail:
                result['faces_thumbnail'].append(k1.to_map() if k1 else None)

        if self.height is not None:
            result['height'] = self.height

        if self.image_quality is not None:
            result['image_quality'] = self.image_quality.to_map()

        result['image_tags'] = []
        if self.image_tags is not None:
            for k1 in self.image_tags:
                result['image_tags'].append(k1.to_map() if k1 else None)

        if self.location is not None:
            result['location'] = self.location

        if self.province is not None:
            result['province'] = self.province

        if self.time is not None:
            result['time'] = self.time

        if self.township is not None:
            result['township'] = self.township

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_line') is not None:
            self.address_line = m.get('address_line')

        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('country') is not None:
            self.country = m.get('country')

        if m.get('district') is not None:
            self.district = m.get('district')

        if m.get('exif') is not None:
            self.exif = m.get('exif')

        self.faces_thumbnail = []
        if m.get('faces_thumbnail') is not None:
            for k1 in m.get('faces_thumbnail'):
                temp_model = main_models.FaceThumbnail()
                self.faces_thumbnail.append(temp_model.from_map(k1))

        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('image_quality') is not None:
            temp_model = main_models.ImageQuality()
            self.image_quality = temp_model.from_map(m.get('image_quality'))

        self.image_tags = []
        if m.get('image_tags') is not None:
            for k1 in m.get('image_tags'):
                temp_model = main_models.SystemTag()
                self.image_tags.append(temp_model.from_map(k1))

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('province') is not None:
            self.province = m.get('province')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('township') is not None:
            self.township = m.get('township')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class AddressGroup(DaraModel):
    def __init__(
        self,
        address_detail: main_models.Address = None,
        count: int = None,
        cover_file_id: str = None,
        cover_url: str = None,
        location: str = None,
        name: str = None,
    ):
        # The information about the site.
        self.address_detail = address_detail
        # The number of files in the site group.
        self.count = count
        # The ID of the cover image of the site.
        self.cover_file_id = cover_file_id
        # The URL of the cover image of the site.
        self.cover_url = cover_url
        # The latitude and longitude of the site.
        self.location = location
        # The name of the site.
        self.name = name

    def validate(self):
        if self.address_detail:
            self.address_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_detail is not None:
            result['address_detail'] = self.address_detail.to_map()

        if self.count is not None:
            result['count'] = self.count

        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id

        if self.cover_url is not None:
            result['cover_url'] = self.cover_url

        if self.location is not None:
            result['location'] = self.location

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_detail') is not None:
            temp_model = main_models.Address()
            self.address_detail = temp_model.from_map(m.get('address_detail'))

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')

        if m.get('cover_url') is not None:
            self.cover_url = m.get('cover_url')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self


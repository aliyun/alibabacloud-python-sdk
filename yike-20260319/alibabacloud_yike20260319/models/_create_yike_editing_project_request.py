# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateYikeEditingProjectRequest(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        material_maps: str = None,
        timeline: str = None,
        title: str = None,
    ):
        # The cover URL of the cloud editing project.
        self.cover_url = cover_url
        # The materials associated with the project. Separate multiple materials with commas (,). A maximum of 10 material IDs are supported for each type.
        self.material_maps = material_maps
        # The timeline of the cloud editing project in JSON format.
        self.timeline = timeline
        # The title of the cloud editing project.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.material_maps is not None:
            result['MaterialMaps'] = self.material_maps

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('MaterialMaps') is not None:
            self.material_maps = m.get('MaterialMaps')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self


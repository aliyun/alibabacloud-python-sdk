# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetEditingProjectMaterialsResponseBody(DaraModel):
    def __init__(
        self,
        material_list: main_models.GetEditingProjectMaterialsResponseBodyMaterialList = None,
        request_id: str = None,
    ):
        self.material_list = material_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.material_list:
            self.material_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.material_list is not None:
            result['MaterialList'] = self.material_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialList') is not None:
            temp_model = main_models.GetEditingProjectMaterialsResponseBodyMaterialList()
            self.material_list = temp_model.from_map(m.get('MaterialList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetEditingProjectMaterialsResponseBodyMaterialList(DaraModel):
    def __init__(
        self,
        material: List[main_models.GetEditingProjectMaterialsResponseBodyMaterialListMaterial] = None,
    ):
        self.material = material

    def validate(self):
        if self.material:
            for v1 in self.material:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Material'] = []
        if self.material is not None:
            for k1 in self.material:
                result['Material'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.material = []
        if m.get('Material') is not None:
            for k1 in m.get('Material'):
                temp_model = main_models.GetEditingProjectMaterialsResponseBodyMaterialListMaterial()
                self.material.append(temp_model.from_map(k1))

        return self

class GetEditingProjectMaterialsResponseBodyMaterialListMaterial(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        duration: float = None,
        material_id: str = None,
        material_type: str = None,
        modified_time: str = None,
        size: int = None,
        snapshots: main_models.GetEditingProjectMaterialsResponseBodyMaterialListMaterialSnapshots = None,
        source: str = None,
        sprite_config: str = None,
        sprites: main_models.GetEditingProjectMaterialsResponseBodyMaterialListMaterialSprites = None,
        status: str = None,
        tags: str = None,
        title: str = None,
    ):
        self.cate_id = cate_id
        self.cate_name = cate_name
        self.cover_url = cover_url
        self.creation_time = creation_time
        self.description = description
        self.duration = duration
        self.material_id = material_id
        self.material_type = material_type
        self.modified_time = modified_time
        self.size = size
        self.snapshots = snapshots
        self.source = source
        self.sprite_config = sprite_config
        self.sprites = sprites
        self.status = status
        self.tags = tags
        self.title = title

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()
        if self.sprites:
            self.sprites.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.material_id is not None:
            result['MaterialId'] = self.material_id

        if self.material_type is not None:
            result['MaterialType'] = self.material_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()

        if self.source is not None:
            result['Source'] = self.source

        if self.sprite_config is not None:
            result['SpriteConfig'] = self.sprite_config

        if self.sprites is not None:
            result['Sprites'] = self.sprites.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')

        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Snapshots') is not None:
            temp_model = main_models.GetEditingProjectMaterialsResponseBodyMaterialListMaterialSnapshots()
            self.snapshots = temp_model.from_map(m.get('Snapshots'))

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SpriteConfig') is not None:
            self.sprite_config = m.get('SpriteConfig')

        if m.get('Sprites') is not None:
            temp_model = main_models.GetEditingProjectMaterialsResponseBodyMaterialListMaterialSprites()
            self.sprites = temp_model.from_map(m.get('Sprites'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetEditingProjectMaterialsResponseBodyMaterialListMaterialSprites(DaraModel):
    def __init__(
        self,
        sprite: List[str] = None,
    ):
        self.sprite = sprite

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sprite is not None:
            result['Sprite'] = self.sprite

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sprite') is not None:
            self.sprite = m.get('Sprite')

        return self

class GetEditingProjectMaterialsResponseBodyMaterialListMaterialSnapshots(DaraModel):
    def __init__(
        self,
        snapshot: List[str] = None,
    ):
        self.snapshot = snapshot

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')

        return self


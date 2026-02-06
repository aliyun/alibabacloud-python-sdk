# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class AddEditingProjectMaterialsResponseBody(DaraModel):
    def __init__(
        self,
        material_list: List[main_models.AddEditingProjectMaterialsResponseBodyMaterialList] = None,
        request_id: str = None,
    ):
        # The materials.
        self.material_list = material_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.material_list:
            for v1 in self.material_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MaterialList'] = []
        if self.material_list is not None:
            for k1 in self.material_list:
                result['MaterialList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.material_list = []
        if m.get('MaterialList') is not None:
            for k1 in m.get('MaterialList'):
                temp_model = main_models.AddEditingProjectMaterialsResponseBodyMaterialList()
                self.material_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddEditingProjectMaterialsResponseBodyMaterialList(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        cover_url: str = None,
        create_time: str = None,
        customer_id: int = None,
        description: str = None,
        duration: float = None,
        material_id: str = None,
        material_type: str = None,
        modify_time: str = None,
        size: int = None,
        snapshots: List[str] = None,
        sprite_config: str = None,
        sprites: List[str] = None,
        status: str = None,
        tags: str = None,
        title: str = None,
    ):
        # The ID of the category.
        self.cate_id = cate_id
        # The category name of the material.
        self.cate_name = cate_name
        # The thumbnail URL.
        self.cover_url = cover_url
        # The time when the material was created. The time follows the ISO 8601 standard in the *YYYY-MM-DD**Thh:mm:ss* format. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the user.
        self.customer_id = customer_id
        # The description of the material.
        self.description = description
        # The duration of the material. Unit: seconds. The value is accurate to four decimal places.
        self.duration = duration
        # The ID of the material.
        self.material_id = material_id
        # The type of the material. Valid values:
        # 
        # *   **video**
        # *   **audio**
        # *   **image**
        self.material_type = material_type
        # The time when the material was last updated. The time follows the ISO 8601 standard in the *YYYY-MM-DD**Thh:mm:ss* format. The time is displayed in UTC.
        self.modify_time = modify_time
        # The size of the material.
        self.size = size
        # The URLs of snapshots.
        self.snapshots = snapshots
        # The configuration of the sprite snapshot.
        self.sprite_config = sprite_config
        # The URLs of sprite snapshots.
        self.sprites = sprites
        # The status of the material. Valid values:
        # 
        # *   **Normal**
        # *   **Uploading**
        # *   **UploadFail**
        self.status = status
        # The tag of the material. Multiple tags are separated by commas (,).
        self.tags = tags
        # The title of the material.
        self.title = title

    def validate(self):
        pass

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.material_id is not None:
            result['MaterialId'] = self.material_id

        if self.material_type is not None:
            result['MaterialType'] = self.material_type

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots

        if self.sprite_config is not None:
            result['SpriteConfig'] = self.sprite_config

        if self.sprites is not None:
            result['Sprites'] = self.sprites

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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')

        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')

        if m.get('SpriteConfig') is not None:
            self.sprite_config = m.get('SpriteConfig')

        if m.get('Sprites') is not None:
            self.sprites = m.get('Sprites')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self


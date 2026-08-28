# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class SaveChannelDraftRequest(DaraModel):
    def __init__(
        self,
        adapted_content: str = None,
        adapted_title: str = None,
        cover_images: List[main_models.SaveChannelDraftRequestCoverImages] = None,
        draft_id: str = None,
    ):
        # The channel content (overseas only).
        self.adapted_content = adapted_content
        # The channel title.
        self.adapted_title = adapted_title
        # The collection of channel cover images (full overwrite).
        self.cover_images = cover_images
        # The ID of the channel draft.
        # 
        # This parameter is required.
        self.draft_id = draft_id

    def validate(self):
        if self.cover_images:
            for v1 in self.cover_images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adapted_content is not None:
            result['AdaptedContent'] = self.adapted_content

        if self.adapted_title is not None:
            result['AdaptedTitle'] = self.adapted_title

        result['CoverImages'] = []
        if self.cover_images is not None:
            for k1 in self.cover_images:
                result['CoverImages'].append(k1.to_map() if k1 else None)

        if self.draft_id is not None:
            result['DraftId'] = self.draft_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptedContent') is not None:
            self.adapted_content = m.get('AdaptedContent')

        if m.get('AdaptedTitle') is not None:
            self.adapted_title = m.get('AdaptedTitle')

        self.cover_images = []
        if m.get('CoverImages') is not None:
            for k1 in m.get('CoverImages'):
                temp_model = main_models.SaveChannelDraftRequestCoverImages()
                self.cover_images.append(temp_model.from_map(k1))

        if m.get('DraftId') is not None:
            self.draft_id = m.get('DraftId')

        return self

class SaveChannelDraftRequestCoverImages(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        material_file_id: str = None,
        sort_order: int = None,
    ):
        # The image URL.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The file ID in the material center (optional).
        self.material_file_id = material_file_id
        # The sort order.
        # 
        # This parameter is required.
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.material_file_id is not None:
            result['MaterialFileId'] = self.material_file_id

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('MaterialFileId') is not None:
            self.material_file_id = m.get('MaterialFileId')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self


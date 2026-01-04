# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSelfImagesRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        page_number: int = None,
        page_size: int = None,
        snapshot_id: str = None,
    ):
        # The ID of the image. Fuzzy search is supported.
        self.image_id = image_id
        # The name of the image. Fuzzy search is supported.
        self.image_name = image_name
        # The page number to return. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The ID of the snapshot.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self


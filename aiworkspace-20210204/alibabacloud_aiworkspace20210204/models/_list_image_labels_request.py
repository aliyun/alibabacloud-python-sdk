# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListImageLabelsRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        label_filter: str = None,
        label_keys: str = None,
        region: str = None,
        workspace_id: str = None,
    ):
        # The image ID. For more information about how to obtain an image ID, see [ListImages](https://help.aliyun.com/document_detail/449118.html).
        self.image_id = image_id
        # The filter conditions for labels. Separate multiple conditions with commas.
        # The format for a single condition is `key=value`.
        # This parameter works independently of the LabelKeys parameter.
        self.label_filter = label_filter
        # The list of tag keys. Separate multiple keys with commas (,).
        # System tags start with "system". This parameter works independently of the LabelFilter parameter.
        self.label_keys = label_keys
        # The region where the image resides.
        self.region = region
        # The workspace ID. For more information about how to obtain a workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.label_filter is not None:
            result['LabelFilter'] = self.label_filter

        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys

        if self.region is not None:
            result['Region'] = self.region

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('LabelFilter') is not None:
            self.label_filter = m.get('LabelFilter')

        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudAppInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        patch_shrink: str = None,
        pkg_labels_shrink: str = None,
        stable_patch_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.description = description
        self.patch_shrink = patch_shrink
        self.pkg_labels_shrink = pkg_labels_shrink
        self.stable_patch_id = stable_patch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.description is not None:
            result['Description'] = self.description

        if self.patch_shrink is not None:
            result['Patch'] = self.patch_shrink

        if self.pkg_labels_shrink is not None:
            result['PkgLabels'] = self.pkg_labels_shrink

        if self.stable_patch_id is not None:
            result['StablePatchId'] = self.stable_patch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Patch') is not None:
            self.patch_shrink = m.get('Patch')

        if m.get('PkgLabels') is not None:
            self.pkg_labels_shrink = m.get('PkgLabels')

        if m.get('StablePatchId') is not None:
            self.stable_patch_id = m.get('StablePatchId')

        return self


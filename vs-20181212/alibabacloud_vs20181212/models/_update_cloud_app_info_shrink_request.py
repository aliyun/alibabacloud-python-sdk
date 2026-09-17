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
        # The cloud application ID, which corresponds to a unique application package.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The description of the application.
        self.description = description
        # The information about the patch package to upload.
        # 1. Not supported when PkgType is set to android.
        # 2. Only one patch can be in the uploading state at a time for the same AppId (only one patch in a non-final state is allowed per AppId).
        self.patch_shrink = patch_shrink
        # The cloud application labels. You can select multiple labels. This operation resets the cloud application labels.
        # 1. Valid values:
        #   a. hot
        #   b. game
        #   c. app
        # 2. Special cases:
        #   a. To delete all labels, set this parameter to ["NULL"].
        self.pkg_labels_shrink = pkg_labels_shrink
        # The stable PatchId. When a PatchId is not specified during business operations (such as session startup), this PatchId is used by default. Not supported when PkgType is set to android.
        # Special values:
        # 1. origin: cancels the patch version and uses the initial version by default.
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


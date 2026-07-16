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
        # The ID of the cloud application, which corresponds to a unique application package.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The description of the application.
        self.description = description
        # Information about the patch package to upload.
        # 
        # 1. This parameter is not supported when PkgType is android.
        # 
        # 2. For the same AppId, only one patch can be in the process of uploading at a time. This means only one patch can be in a state other than its desired state.
        self.patch_shrink = patch_shrink
        # The tags for the cloud application. You can select multiple tags. This action resets all existing tags for the cloud application.
        # 
        # 1. Valid values:
        #    hot, game, and app.
        # 
        # 2. Special case:
        #    To delete all tags, enter ["NULL"].
        self.pkg_labels_shrink = pkg_labels_shrink
        # The ID of the stable patch. This patch is used by default if you do not specify a PatchId when the application is in use, such as during a session startup. This parameter is not supported when PkgType is android.
        # Special value:
        # 
        # 1. If you set this parameter to origin, the patch version is removed and the initial version is used.
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


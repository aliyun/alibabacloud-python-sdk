# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class UpdateCloudAppInfoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        patch: main_models.UpdateCloudAppInfoRequestPatch = None,
        pkg_labels: List[str] = None,
        stable_patch_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.description = description
        self.patch = patch
        self.pkg_labels = pkg_labels
        self.stable_patch_id = stable_patch_id

    def validate(self):
        if self.patch:
            self.patch.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.description is not None:
            result['Description'] = self.description

        if self.patch is not None:
            result['Patch'] = self.patch.to_map()

        if self.pkg_labels is not None:
            result['PkgLabels'] = self.pkg_labels

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
            temp_model = main_models.UpdateCloudAppInfoRequestPatch()
            self.patch = temp_model.from_map(m.get('Patch'))

        if m.get('PkgLabels') is not None:
            self.pkg_labels = m.get('PkgLabels')

        if m.get('StablePatchId') is not None:
            self.stable_patch_id = m.get('StablePatchId')

        return self

class UpdateCloudAppInfoRequestPatch(DaraModel):
    def __init__(
        self,
        as_stable_patch: bool = None,
        download_url: str = None,
        md_5: str = None,
        patch_name: str = None,
        pkg_format: str = None,
        rendering_instance_id: str = None,
    ):
        self.as_stable_patch = as_stable_patch
        self.download_url = download_url
        self.md_5 = md_5
        self.patch_name = patch_name
        self.pkg_format = pkg_format
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.as_stable_patch is not None:
            result['AsStablePatch'] = self.as_stable_patch

        if self.download_url is not None:
            result['DownloadURL'] = self.download_url

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.patch_name is not None:
            result['PatchName'] = self.patch_name

        if self.pkg_format is not None:
            result['PkgFormat'] = self.pkg_format

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsStablePatch') is not None:
            self.as_stable_patch = m.get('AsStablePatch')

        if m.get('DownloadURL') is not None:
            self.download_url = m.get('DownloadURL')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('PatchName') is not None:
            self.patch_name = m.get('PatchName')

        if m.get('PkgFormat') is not None:
            self.pkg_format = m.get('PkgFormat')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self


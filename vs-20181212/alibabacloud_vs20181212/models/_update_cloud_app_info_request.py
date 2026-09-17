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
        # The cloud application ID, which corresponds to a unique application package.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The description of the application.
        self.description = description
        # The information about the patch package to upload.
        # 1. Not supported when PkgType is set to android.
        # 2. Only one patch can be in the uploading state at a time for the same AppId (only one patch in a non-final state is allowed per AppId).
        self.patch = patch
        # The cloud application labels. You can select multiple labels. This operation resets the cloud application labels.
        # 1. Valid values:
        #   a. hot
        #   b. game
        #   c. app
        # 2. Special cases:
        #   a. To delete all labels, set this parameter to ["NULL"].
        self.pkg_labels = pkg_labels
        # The stable PatchId. When a PatchId is not specified during business operations (such as session startup), this PatchId is used by default. Not supported when PkgType is set to android.
        # Special values:
        # 1. origin: cancels the patch version and uses the initial version by default.
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
        post_command_path: str = None,
        post_command_timeout_sec: int = None,
        rendering_instance_id: str = None,
    ):
        # Specifies whether to automatically set the patch as the stable patch after a successful upload. Default value: false.
        self.as_stable_patch = as_stable_patch
        # The download URL of the patch package.
        # Either RenderingInstanceId or DownloadURL is required. DownloadURL takes priority.
        self.download_url = download_url
        # The MD5 hash of the patch package, used for integrity verification. Valid only when DownloadURL is not empty. Required when DownloadURL is not empty.
        self.md_5 = md_5
        # The name or description of the patch package, which serves as a unique identifier under the AppId.
        # Naming conventions:
        # 1. Cannot be set to origin or all.
        # 2. Must be 1 to 50 characters in length.
        # 3. Can contain lowercase letters, digits, underscores (_), hyphens (-), and periods (.).
        # 4. Must start and end with a letter or digit.
        self.patch_name = patch_name
        # The format of the installation package. The default value is the file extension of the download URL. Valid only when DownloadURL is not empty. Valid values:
        # 1. tar.gz
        # 2. tar
        # 3. zip
        # 4. rar
        self.pkg_format = pkg_format
        # The relative path of the post-command within the application package. Only supported for Windows applications.
        self.post_command_path = post_command_path
        # The timeout period for the post-command execution, in seconds. Only supported for Windows applications.
        self.post_command_timeout_sec = post_command_timeout_sec
        # The instance ID of the instance used to create the patch package. Valid only for Android application marketplace scenarios (PkgType=andrpid_appmarket). Either RenderingInstanceId or DownloadURL is required. DownloadURL takes priority.
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

        if self.post_command_path is not None:
            result['PostCommandPath'] = self.post_command_path

        if self.post_command_timeout_sec is not None:
            result['PostCommandTimeoutSec'] = self.post_command_timeout_sec

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

        if m.get('PostCommandPath') is not None:
            self.post_command_path = m.get('PostCommandPath')

        if m.get('PostCommandTimeoutSec') is not None:
            self.post_command_timeout_sec = m.get('PostCommandTimeoutSec')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self


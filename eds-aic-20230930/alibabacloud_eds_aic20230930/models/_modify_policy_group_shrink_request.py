# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPolicyGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy_shrink: str = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        watermark_shrink: str = None,
    ):
        # Specifies whether to enable the webcam redirection feature.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.camera_redirect = camera_redirect
        # The read/write permissions on the clipboard.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write disabled.
        self.clipboard = clipboard
        # The file transfer policy of the Alibaba Cloud Workspace web client.
        # 
        # Valid values:
        # 
        # *   all: File upload and download are supported.
        # *   download: Only file download is supported.
        # *   upload: Only file upload is supported.
        # *   off: File upload or download is forbidden.
        self.html_5file_transfer = html_5file_transfer
        # The read/write permissions on the on-premises drive.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write disabled.
        self.local_drive = local_drive
        # Specifies whether to lock the resolution.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.lock_resolution = lock_resolution
        # The network redirection policy.
        self.net_redirect_policy_shrink = net_redirect_policy_shrink
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The name of the policy.
        self.policy_group_name = policy_group_name
        # The height of the resolution. Unit: pixels.
        self.resolution_height = resolution_height
        # The width of the resolution. Unit: pixels.
        self.resolution_width = resolution_width
        self.watermark_shrink = watermark_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect

        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard

        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer

        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive

        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution

        if self.net_redirect_policy_shrink is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy_shrink

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name

        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height

        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width

        if self.watermark_shrink is not None:
            result['Watermark'] = self.watermark_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')

        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')

        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')

        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')

        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')

        if m.get('NetRedirectPolicy') is not None:
            self.net_redirect_policy_shrink = m.get('NetRedirectPolicy')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')

        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')

        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')

        if m.get('Watermark') is not None:
            self.watermark_shrink = m.get('Watermark')

        return self


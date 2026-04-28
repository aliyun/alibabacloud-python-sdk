# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoDRMLicenseRequest(DaraModel):
    def __init__(
        self,
        drm_type: str = None,
        license_request: str = None,
    ):
        # The type of DRM encryption.
        # 
        # Valid values:
        # 
        # *   fairplay
        # *   widevine
        # 
        # This parameter is required.
        self.drm_type = drm_type
        # The request that is initiated to obtain the license.
        self.license_request = license_request

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drm_type is not None:
            result['drmType'] = self.drm_type

        if self.license_request is not None:
            result['licenseRequest'] = self.license_request

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drmType') is not None:
            self.drm_type = m.get('drmType')

        if m.get('licenseRequest') is not None:
            self.license_request = m.get('licenseRequest')

        return self


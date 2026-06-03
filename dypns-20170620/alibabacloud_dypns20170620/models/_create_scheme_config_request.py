# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSchemeConfigRequest(DaraModel):
    def __init__(
        self,
        android_package_name: str = None,
        android_package_sign: str = None,
        app_name: str = None,
        h_5origin: str = None,
        h_5url: str = None,
        ios_bundle_id: str = None,
        owner_id: int = None,
        platform: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_name: str = None,
    ):
        self.android_package_name = android_package_name
        self.android_package_sign = android_package_sign
        self.app_name = app_name
        self.h_5origin = h_5origin
        self.h_5url = h_5url
        self.ios_bundle_id = ios_bundle_id
        self.owner_id = owner_id
        # This parameter is required.
        self.platform = platform
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scheme_name = scheme_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_package_name is not None:
            result['AndroidPackageName'] = self.android_package_name

        if self.android_package_sign is not None:
            result['AndroidPackageSign'] = self.android_package_sign

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.h_5origin is not None:
            result['H5Origin'] = self.h_5origin

        if self.h_5url is not None:
            result['H5Url'] = self.h_5url

        if self.ios_bundle_id is not None:
            result['IosBundleId'] = self.ios_bundle_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPackageName') is not None:
            self.android_package_name = m.get('AndroidPackageName')

        if m.get('AndroidPackageSign') is not None:
            self.android_package_sign = m.get('AndroidPackageSign')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('H5Origin') is not None:
            self.h_5origin = m.get('H5Origin')

        if m.get('H5Url') is not None:
            self.h_5url = m.get('H5Url')

        if m.get('IosBundleId') is not None:
            self.ios_bundle_id = m.get('IosBundleId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')

        return self


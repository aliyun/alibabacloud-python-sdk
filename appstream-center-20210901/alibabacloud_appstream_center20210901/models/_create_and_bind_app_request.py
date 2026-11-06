# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAndBindAppRequest(DaraModel):
    def __init__(
        self,
        app_icon_url: str = None,
        app_name: str = None,
        image_id: str = None,
        origin_app_type: str = None,
        port: str = None,
        url_suffix: str = None,
        version_id: str = None,
    ):
        # The URL of the application icon. Specify an accessible icon URL to display a custom icon.
        self.app_icon_url = app_icon_url
        # The name of the application to be created, which is used to identify the application in the image.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The ID of the image to which the application is bound. The image must be a custom image or community image that can be managed by the current account.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The application type. If omitted, the default value is CLIENT_BASE. Valid values:
        # 
        # - **CLIENT_BASE**: Client application.
        # - **WEB_BASE**: Browser application.
        # - **CLOUD_NATIVE_BASE**: Cloud-native application.
        # - **PORT_SERVICE_BASE**: Port service application.
        # - **AGENT_SERVICE_BASE**: Agent application.
        self.origin_app_type = origin_app_type
        # The application service port. For applications that require port-based access, specify the actual port number that the application listens on.
        self.port = port
        # The path suffix of the application access URL, which is used together with the application service port to describe the access entry point.
        self.url_suffix = url_suffix
        # The ID of the image version to which the application is bound. If omitted, the current active version of the image specified by ImageId is used. If specified, the version must belong to the image.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_icon_url is not None:
            result['AppIconUrl'] = self.app_icon_url

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.origin_app_type is not None:
            result['OriginAppType'] = self.origin_app_type

        if self.port is not None:
            result['Port'] = self.port

        if self.url_suffix is not None:
            result['UrlSuffix'] = self.url_suffix

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIconUrl') is not None:
            self.app_icon_url = m.get('AppIconUrl')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('OriginAppType') is not None:
            self.origin_app_type = m.get('OriginAppType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('UrlSuffix') is not None:
            self.url_suffix = m.get('UrlSuffix')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self


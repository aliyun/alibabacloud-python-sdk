# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveApgroupPortalConfigRequest(DaraModel):
    def __init__(
        self,
        apgroup_id: int = None,
        app_auth_url: str = None,
        app_code: str = None,
        app_name: str = None,
        auth_key: str = None,
        auth_secret: str = None,
        check_url: str = None,
        client_download: int = None,
        client_upload: int = None,
        countdown: int = None,
        network: int = None,
        portal_types: List[str] = None,
        portal_url: str = None,
        time_stamp: int = None,
        total_download: int = None,
        total_upload: int = None,
        web_auth_url: str = None,
        whitelist: str = None,
    ):
        # This parameter is required.
        self.apgroup_id = apgroup_id
        self.app_auth_url = app_auth_url
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        self.auth_key = auth_key
        self.auth_secret = auth_secret
        self.check_url = check_url
        self.client_download = client_download
        self.client_upload = client_upload
        self.countdown = countdown
        self.network = network
        self.portal_types = portal_types
        self.portal_url = portal_url
        self.time_stamp = time_stamp
        self.total_download = total_download
        self.total_upload = total_upload
        self.web_auth_url = web_auth_url
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id

        if self.app_auth_url is not None:
            result['AppAuthUrl'] = self.app_auth_url

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret

        if self.check_url is not None:
            result['CheckUrl'] = self.check_url

        if self.client_download is not None:
            result['ClientDownload'] = self.client_download

        if self.client_upload is not None:
            result['ClientUpload'] = self.client_upload

        if self.countdown is not None:
            result['Countdown'] = self.countdown

        if self.network is not None:
            result['Network'] = self.network

        if self.portal_types is not None:
            result['PortalTypes'] = self.portal_types

        if self.portal_url is not None:
            result['PortalUrl'] = self.portal_url

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.total_download is not None:
            result['TotalDownload'] = self.total_download

        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload

        if self.web_auth_url is not None:
            result['WebAuthUrl'] = self.web_auth_url

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')

        if m.get('AppAuthUrl') is not None:
            self.app_auth_url = m.get('AppAuthUrl')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')

        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')

        if m.get('ClientDownload') is not None:
            self.client_download = m.get('ClientDownload')

        if m.get('ClientUpload') is not None:
            self.client_upload = m.get('ClientUpload')

        if m.get('Countdown') is not None:
            self.countdown = m.get('Countdown')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('PortalTypes') is not None:
            self.portal_types = m.get('PortalTypes')

        if m.get('PortalUrl') is not None:
            self.portal_url = m.get('PortalUrl')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')

        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')

        if m.get('WebAuthUrl') is not None:
            self.web_auth_url = m.get('WebAuthUrl')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeFotaPendingDesktopsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        fota_pending_desktops: List[main_models.DescribeFotaPendingDesktopsResponseBodyFotaPendingDesktops] = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The cloud computers whose images can be and are pending to be updated to the version specified in `TaskUid`.
        self.fota_pending_desktops = fota_pending_desktops
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.fota_pending_desktops:
            for v1 in self.fota_pending_desktops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['FotaPendingDesktops'] = []
        if self.fota_pending_desktops is not None:
            for k1 in self.fota_pending_desktops:
                result['FotaPendingDesktops'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.fota_pending_desktops = []
        if m.get('FotaPendingDesktops') is not None:
            for k1 in m.get('FotaPendingDesktops'):
                temp_model = main_models.DescribeFotaPendingDesktopsResponseBodyFotaPendingDesktops()
                self.fota_pending_desktops.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFotaPendingDesktopsResponseBodyFotaPendingDesktops(DaraModel):
    def __init__(
        self,
        current_app_version: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        fota_project: str = None,
        office_site_id: str = None,
        sessions: List[main_models.DescribeFotaPendingDesktopsResponseBodyFotaPendingDesktopsSessions] = None,
        status: int = None,
    ):
        # The current version of the image used by the cloud computer.
        self.current_app_version = current_app_version
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The name of the cloud computer.
        self.desktop_name = desktop_name
        # > This parameter is not publicly available.
        self.fota_project = fota_project
        # The ID of the office network.
        self.office_site_id = office_site_id
        # The connected sessions.
        self.sessions = sessions
        # The status of the cloud computer.
        # 
        # Valid values:
        # 
        # *   0: The cloud computer is being created.
        # *   1: The cloud computer is being started.
        # *   2: The cloud computer is running.
        # *   3: The cloud computer is being stopped.
        # *   5: The cloud computer is stopped.
        # *   6: The cloud computer expires.
        # *   7: The cloud computer is deleted.
        # *   9: Failed to create the cloud computer.
        self.status = status

    def validate(self):
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_app_version is not None:
            result['CurrentAppVersion'] = self.current_app_version

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.fota_project is not None:
            result['FotaProject'] = self.fota_project

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentAppVersion') is not None:
            self.current_app_version = m.get('CurrentAppVersion')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('FotaProject') is not None:
            self.fota_project = m.get('FotaProject')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.DescribeFotaPendingDesktopsResponseBodyFotaPendingDesktopsSessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeFotaPendingDesktopsResponseBodyFotaPendingDesktopsSessions(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
    ):
        # The ID of the end user that connects to the cloud computer.
        self.end_user_id = end_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        return self


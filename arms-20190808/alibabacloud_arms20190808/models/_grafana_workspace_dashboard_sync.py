# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceDashboardSync(DaraModel):
    def __init__(
        self,
        dashboard_title: str = None,
        dashboard_url: str = None,
        dashboard_uid: str = None,
        folder_id: str = None,
        folder_title: str = None,
        folder_url: str = None,
        folder_uid: str = None,
        org_id: str = None,
        org_name: str = None,
        type: str = None,
    ):
        self.dashboard_title = dashboard_title
        self.dashboard_url = dashboard_url
        self.dashboard_uid = dashboard_uid
        self.folder_id = folder_id
        self.folder_title = folder_title
        self.folder_url = folder_url
        self.folder_uid = folder_uid
        self.org_id = org_id
        self.org_name = org_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_title is not None:
            result['dashboardTitle'] = self.dashboard_title

        if self.dashboard_url is not None:
            result['dashboardURL'] = self.dashboard_url

        if self.dashboard_uid is not None:
            result['dashboardUid'] = self.dashboard_uid

        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.folder_title is not None:
            result['folderTitle'] = self.folder_title

        if self.folder_url is not None:
            result['folderURL'] = self.folder_url

        if self.folder_uid is not None:
            result['folderUid'] = self.folder_uid

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.org_name is not None:
            result['orgName'] = self.org_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dashboardTitle') is not None:
            self.dashboard_title = m.get('dashboardTitle')

        if m.get('dashboardURL') is not None:
            self.dashboard_url = m.get('dashboardURL')

        if m.get('dashboardUid') is not None:
            self.dashboard_uid = m.get('dashboardUid')

        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('folderTitle') is not None:
            self.folder_title = m.get('folderTitle')

        if m.get('folderURL') is not None:
            self.folder_url = m.get('folderURL')

        if m.get('folderUid') is not None:
            self.folder_uid = m.get('folderUid')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self


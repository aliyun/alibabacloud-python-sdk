# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryInfoFromMdpRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        mobile: str = None,
        mobile_md_5: str = None,
        mobile_sha_256: str = None,
        mobile_sm_3: str = None,
        risk_scene: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.mobile = mobile
        self.mobile_md_5 = mobile_md_5
        self.mobile_sha_256 = mobile_sha_256
        self.mobile_sm_3 = mobile_sm_3
        # This parameter is required.
        self.risk_scene = risk_scene
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.mobile_md_5 is not None:
            result['MobileMd5'] = self.mobile_md_5

        if self.mobile_sha_256 is not None:
            result['MobileSha256'] = self.mobile_sha_256

        if self.mobile_sm_3 is not None:
            result['MobileSm3'] = self.mobile_sm_3

        if self.risk_scene is not None:
            result['RiskScene'] = self.risk_scene

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('MobileMd5') is not None:
            self.mobile_md_5 = m.get('MobileMd5')

        if m.get('MobileSha256') is not None:
            self.mobile_sha_256 = m.get('MobileSha256')

        if m.get('MobileSm3') is not None:
            self.mobile_sm_3 = m.get('MobileSm3')

        if m.get('RiskScene') is not None:
            self.risk_scene = m.get('RiskScene')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self


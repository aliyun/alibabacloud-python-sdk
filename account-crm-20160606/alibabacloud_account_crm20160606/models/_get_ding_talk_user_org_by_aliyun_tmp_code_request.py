# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDingTalkUserOrgByAliyunTmpCodeRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        ding_talk_channel: str = None,
        tmp_code: str = None,
        version: str = None,
    ):
        self.app_name = app_name
        self.ding_talk_channel = ding_talk_channel
        self.tmp_code = tmp_code
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.ding_talk_channel is not None:
            result['DingTalkChannel'] = self.ding_talk_channel

        if self.tmp_code is not None:
            result['TmpCode'] = self.tmp_code

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DingTalkChannel') is not None:
            self.ding_talk_channel = m.get('DingTalkChannel')

        if m.get('TmpCode') is not None:
            self.tmp_code = m.get('TmpCode')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self


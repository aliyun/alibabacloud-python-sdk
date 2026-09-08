# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TokenSettings(DaraModel):
    def __init__(
        self,
        enable_cross_account_access: bool = None,
        enable_log_download_job: bool = None,
    ):
        self.enable_cross_account_access = enable_cross_account_access
        self.enable_log_download_job = enable_log_download_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_cross_account_access is not None:
            result['EnableCrossAccountAccess'] = self.enable_cross_account_access

        if self.enable_log_download_job is not None:
            result['EnableLogDownloadJob'] = self.enable_log_download_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableCrossAccountAccess') is not None:
            self.enable_cross_account_access = m.get('EnableCrossAccountAccess')

        if m.get('EnableLogDownloadJob') is not None:
            self.enable_log_download_job = m.get('EnableLogDownloadJob')

        return self


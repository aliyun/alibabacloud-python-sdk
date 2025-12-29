# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetricsCollectConfig(DaraModel):
    def __init__(
        self,
        enable_push_to_user_sls: bool = None,
        logstore_name: str = None,
        project_name: str = None,
    ):
        self.enable_push_to_user_sls = enable_push_to_user_sls
        self.logstore_name = logstore_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_push_to_user_sls is not None:
            result['EnablePushToUserSLS'] = self.enable_push_to_user_sls

        if self.logstore_name is not None:
            result['LogstoreName'] = self.logstore_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePushToUserSLS') is not None:
            self.enable_push_to_user_sls = m.get('EnablePushToUserSLS')

        if m.get('LogstoreName') is not None:
            self.logstore_name = m.get('LogstoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self


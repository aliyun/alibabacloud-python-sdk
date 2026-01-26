# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GrafanaWorkspaceTrans(DaraModel):
    def __init__(
        self,
        api_url: str = None,
        auth_type: str = None,
        gmt_create: float = None,
        gmt_modified: float = None,
        grafana_workspace_id: str = None,
        id: int = None,
        msg: str = None,
        process_status: str = None,
        trans_details: List[main_models.GrafanaWorkspaceTransDetail] = None,
        user_id: str = None,
    ):
        self.api_url = api_url
        self.auth_type = auth_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grafana_workspace_id = grafana_workspace_id
        self.id = id
        self.msg = msg
        self.process_status = process_status
        self.trans_details = trans_details
        self.user_id = user_id

    def validate(self):
        if self.trans_details:
            for v1 in self.trans_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_url is not None:
            result['apiUrl'] = self.api_url

        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.grafana_workspace_id is not None:
            result['grafanaWorkspaceId'] = self.grafana_workspace_id

        if self.id is not None:
            result['id'] = self.id

        if self.msg is not None:
            result['msg'] = self.msg

        if self.process_status is not None:
            result['processStatus'] = self.process_status

        result['transDetails'] = []
        if self.trans_details is not None:
            for k1 in self.trans_details:
                result['transDetails'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiUrl') is not None:
            self.api_url = m.get('apiUrl')

        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('grafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('grafanaWorkspaceId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('processStatus') is not None:
            self.process_status = m.get('processStatus')

        self.trans_details = []
        if m.get('transDetails') is not None:
            for k1 in m.get('transDetails'):
                temp_model = main_models.GrafanaWorkspaceTransDetail()
                self.trans_details.append(temp_model.from_map(k1))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self


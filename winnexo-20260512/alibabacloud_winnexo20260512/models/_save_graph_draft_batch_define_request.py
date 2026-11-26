# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveGraphDraftBatchDefineRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        draft_change_ids: List[int] = None,
        graph_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        save_mode: str = None,
        tenant_id: str = None,
        yaml_edit: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The list of draft change IDs.
        self.draft_change_ids = draft_change_ids
        # The graph name.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The save mode.
        self.save_mode = save_mode
        # The tenant ID.
        self.tenant_id = tenant_id
        # The raw YAML text of the graph schema trimmed by READ permissions, with $ref references retained within the authorized subgraph.
        # 
        # This parameter is required.
        self.yaml_edit = yaml_edit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.draft_change_ids is not None:
            result['draftChangeIds'] = self.draft_change_ids

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.save_mode is not None:
            result['saveMode'] = self.save_mode

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.yaml_edit is not None:
            result['yamlEdit'] = self.yaml_edit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('draftChangeIds') is not None:
            self.draft_change_ids = m.get('draftChangeIds')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('saveMode') is not None:
            self.save_mode = m.get('saveMode')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('yamlEdit') is not None:
            self.yaml_edit = m.get('yamlEdit')

        return self


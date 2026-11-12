# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateServiceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        develop: str = None,
        dry_run: bool = None,
        labels: Dict[str, str] = None,
        workspace_id: str = None,
        body: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # Specifies whether to enter development mode.
        self.develop = develop
        # Specifies whether to only perform a dry run for this request.
        # 
        # - true: A check request is sent, and no actual operation is performed. If the check fails, the corresponding error is returned. If the check succeeds, the error code DryRunOperation is returned.
        # 
        # - false (default): A normal request is sent.
        self.dry_run = dry_run
        # The user-defined labels.
        self.labels = labels
        # The workspace ID.
        self.workspace_id = workspace_id
        # The request body. For instructions on key request parameter settings, see **Table 1. Request body parameters** and **Table 2. Metadata parameters** below. For more details about parameter settings, see [All related metric description for service models](https://help.aliyun.com/document_detail/450525.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.develop is not None:
            result['Develop'] = self.develop

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.body is not None:
            result['body'] = self.body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Develop') is not None:
            self.develop = m.get('Develop')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('body') is not None:
            self.body = m.get('body')

        return self


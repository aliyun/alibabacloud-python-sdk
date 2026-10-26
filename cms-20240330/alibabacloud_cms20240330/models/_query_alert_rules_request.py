# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class QueryAlertRulesRequest(DaraModel):
    def __init__(
        self,
        body: main_models.QueryAlertRulesInput = None,
        client_token: str = None,
        max_results: int = None,
        next_token: str = None,
        query_json: str = None,
    ):
        # The request body for querying alert rules.
        self.body = body
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The maximum number of data records to return in the current read operation.
        self.max_results = max_results
        # The token that specifies the starting position for the current read operation. If this parameter is left empty, the read operation starts from the beginning.
        self.next_token = next_token
        # The query filter conditions in JSON string format. The field semantics are the same as those in the request body. Supported fields include filter (such as uuid, displayName, labels, status, and enabled, where sibling fields use the AND logical operator), pagination (pageNumber and pageSize), and workspace. You must specify either this parameter or the body parameter. If both are specified, the body parameter takes precedence.
        self.query_json = query_json

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.query_json is not None:
            result['queryJson'] = self.query_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.QueryAlertRulesInput()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('queryJson') is not None:
            self.query_json = m.get('queryJson')

        return self

